#!/usr/bin/env python3
"""Regenerate plugin folders, zips and checksums from the skill folders.

The top-level skill folders (effort-optimizer/, supersystem-integrate/,
linktree-search/) are the single source of truth. Run this after editing one:

    python scripts/build.py

It rewrites plugins/<name>/ (a Claude plugin wrapper around the skill) and
dist/<name>.zip plus dist/SHA256SUMS.txt. Bump PLUGIN_VERSION below on every
release so installed plugins update.
"""
import hashlib
import json
import os
import shutil
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN_VERSION = "1.0.1"
AUTHOR = {"name": "mmc7676", "url": "https://github.com/mmc7676"}
HOME = "https://github.com/mmc7676/skills"

SKILLS = {
    "effort-optimizer": {
        "displayName": "Effort Optimizer",
        "description": "Skill that matches reasoning and verification effort to a task's real stakes: fast on mechanical, reversible steps; slow and directly verified on auth, security, production, or claims you will act on unchecked.",
        "keywords": ["agent-skills", "effort", "verification", "reliability"],
    },
    "supersystem-integrate": {
        "displayName": "SuperSystem Integrate",
        "description": "Generative engineering skill: discover, model, bound, design, integrate, implement, validate, package and verify a new capability in an existing system, with an explicit consent boundary before anything outward-facing.",
        "keywords": ["agent-skills", "integration", "engineering", "shipping"],
    },
    "linktree-search": {
        "displayName": "LINKTREE Search",
        "description": "The LINKTREE method: deterministic, level-preserving URL crawling and indexing (tree, graph, outline) with sitemap-first, same-origin, robots-aware, polite, bounded defaults. A specification package with no crawler code.",
        "keywords": ["agent-skills", "crawling", "sitemap", "robots"],
    },
}
PLUGIN_ONLY = {"README.md", "LICENSE"}  # live at the plugin root, not inside the skill


def files_of(base):
    out = []
    for d, dirs, fs in os.walk(base):
        dirs.sort()
        for f in sorted(fs):
            p = os.path.join(d, f).replace("\\", "/")
            out.append(p[len(base) + 1:])
    return sorted(out)


def write(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(data)


def build_plugin(name, meta):
    src = f"{ROOT}/{name}"
    dst = f"{ROOT}/plugins/{name}"
    if os.path.isdir(dst):
        shutil.rmtree(dst)
    for rel in files_of(src):
        data = open(f"{src}/{rel}", "rb").read()
        target = f"{dst}/{rel}" if rel in PLUGIN_ONLY else f"{dst}/skills/{name}/{rel}"
        write(target, data)
    manifest = {
        "name": name,
        "displayName": meta["displayName"],
        "version": PLUGIN_VERSION,
        "description": meta["description"],
        "author": AUTHOR,
        "homepage": HOME,
        "repository": HOME,
        "license": "MIT",
        "keywords": meta["keywords"],
    }
    write(f"{dst}/.claude-plugin/plugin.json", (json.dumps(manifest, indent=2) + "\n").encode("utf8"))


def build_zip(name):
    base = f"{ROOT}/{name}"
    members = sorted(files_of(base), key=lambda m: (m != "SKILL.md", m))
    zp = f"{ROOT}/dist/{name}.zip"
    os.makedirs(os.path.dirname(zp), exist_ok=True)
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for m in members:
            data = open(f"{base}/{m}", "rb").read()
            if b"\r\n" in data:
                raise SystemExit(f"{name}/{m} has CRLF line endings; normalize to LF first")
            zi = zipfile.ZipInfo(f"{name}/{m}", date_time=(2026, 10, 5, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(zi, data)
    return hashlib.sha256(open(zp, "rb").read()).hexdigest()


def main():
    sums = []
    for name, meta in SKILLS.items():
        build_plugin(name, meta)
        sums.append(f"{build_zip(name)}  {name}.zip")
    with open(f"{ROOT}/dist/SHA256SUMS.txt", "w", newline="\n") as fh:
        fh.write("\n".join(sums) + "\n")
    print("\n".join(sums))


if __name__ == "__main__":
    main()
