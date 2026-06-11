#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skill_name="gpt-image-ux-partner"
source_dir="$repo_root/skills/$skill_name"
dest_root="${CODEX_HOME:-$HOME/.codex}/skills"
dest_dir="$dest_root/$skill_name"

if [[ ! -d "$source_dir" ]]; then
  echo "Missing skill source: $source_dir" >&2
  exit 1
fi

if [[ -e "$dest_dir" ]]; then
  echo "Destination already exists: $dest_dir" >&2
  echo "Remove it first if you want to reinstall." >&2
  exit 1
fi

mkdir -p "$dest_root"
cp -R "$source_dir" "$dest_dir"

echo "Installed $skill_name to $dest_dir"
echo "Restart Codex to pick up new skills."

