#!/usr/bin/env python3
"""Save lightweight UX ideation run state as JSON."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def read_state(path: Path) -> dict:
    if not path.exists():
        return {"rounds": []}
    return json.loads(path.read_text(encoding="utf-8"))


def write_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def split_values(values: list[str] | None) -> list[str]:
    if not values:
        return []
    items: list[str] = []
    for value in values:
        items.extend(part.strip() for part in value.split(";") if part.strip())
    return items


def cmd_init(args: argparse.Namespace) -> None:
    state = {
        "project": args.project,
        "skill": "gpt-image-ux-partner",
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "collaboration_cadence": args.cadence,
        "scope": args.scope,
        "loop_depth": args.loop_depth,
        "loop_depth_reason": args.loop_depth_reason,
        "user_job": args.user_job,
        "avoid_list": split_values(args.avoid),
        "rounds": [],
        "selected_direction": None,
    }
    write_state(Path(args.file), state)
    print(args.file)


def cmd_round(args: argparse.Namespace) -> None:
    path = Path(args.file)
    state = read_state(path)
    state.setdefault("rounds", [])
    round_entry = {
        "round": args.round,
        "phase": args.phase,
        "created_at": now_iso(),
        "prompt": args.prompt,
        "images": split_values(args.image),
        "liked": split_values(args.liked),
        "patterns": split_values(args.pattern),
        "failure_signals": split_values(args.failure),
        "avoid_added": split_values(args.avoid),
        "decision": args.decision,
        "next_prompt_change": args.next_prompt_change,
    }
    state["rounds"].append(round_entry)
    state["updated_at"] = now_iso()
    avoid_list = state.setdefault("avoid_list", [])
    for item in round_entry["avoid_added"]:
        if item not in avoid_list:
            avoid_list.append(item)
    write_state(path, state)
    print(f"saved round {args.round} to {args.file}")


def cmd_select(args: argparse.Namespace) -> None:
    path = Path(args.file)
    state = read_state(path)
    state["selected_direction"] = {
        "name": args.name,
        "why_it_won": split_values(args.why),
        "primary_object": args.primary_object,
        "primary_action": args.primary_action,
        "handoff": args.handoff,
    }
    state["updated_at"] = now_iso()
    write_state(path, state)
    print(f"selected {args.name}")


def cmd_summary(args: argparse.Namespace) -> None:
    state = read_state(Path(args.file))
    print(json.dumps({
        "project": state.get("project"),
        "scope": state.get("scope"),
        "loop_depth": state.get("loop_depth"),
        "round_count": len(state.get("rounds", [])),
        "avoid_list": state.get("avoid_list", []),
        "selected_direction": state.get("selected_direction"),
    }, indent=2, ensure_ascii=False))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(required=True)

    init = sub.add_parser("init", help="create a run-state JSON file")
    init.add_argument("--file", required=True)
    init.add_argument("--project", required=True)
    init.add_argument("--cadence", required=True)
    init.add_argument("--scope", required=True)
    init.add_argument("--loop-depth", required=True, choices=["quick", "standard", "deep"])
    init.add_argument("--loop-depth-reason", default="")
    init.add_argument("--user-job", default="")
    init.add_argument("--avoid", action="append")
    init.set_defaults(func=cmd_init)

    rnd = sub.add_parser("round", help="append notes for one round")
    rnd.add_argument("--file", required=True)
    rnd.add_argument("--round", type=int, required=True)
    rnd.add_argument("--phase", required=True, choices=["divergent", "synthesis", "convergent", "handoff"])
    rnd.add_argument("--prompt", default="")
    rnd.add_argument("--image", action="append")
    rnd.add_argument("--liked", action="append")
    rnd.add_argument("--pattern", action="append")
    rnd.add_argument("--failure", action="append")
    rnd.add_argument("--avoid", action="append")
    rnd.add_argument("--decision", default="")
    rnd.add_argument("--next-prompt-change", default="")
    rnd.set_defaults(func=cmd_round)

    select = sub.add_parser("select", help="save selected direction")
    select.add_argument("--file", required=True)
    select.add_argument("--name", required=True)
    select.add_argument("--why", action="append")
    select.add_argument("--primary-object", default="")
    select.add_argument("--primary-action", default="")
    select.add_argument("--handoff", default="")
    select.set_defaults(func=cmd_select)

    summary = sub.add_parser("summary", help="print compact state summary")
    summary.add_argument("--file", required=True)
    summary.set_defaults(func=cmd_summary)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
