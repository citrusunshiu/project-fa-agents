# Where the project stands

Rewritten with each change, never appended to. Last rewritten 2026-11-21.

## Phase

Phase 0, paper architecture ([charter](https://github.com/citrusunshiu/project-fa/blob/main/docs/charter.md)). It's done when every planned component has a design doc, every founding decision record is decided, the company brief's estimates have been challenged, and the checks find nothing over the whole history. Then the repositories go public.

## In flight

- Setting up the repositories: the first push, the agents' GitHub App, the labels and milestones (`tools/sync_tracker.py` in the hub) and the project board. The repositories stay private until Phase 0 ends.
- Decision records 0001 to 0012 wait on the maintainer's rulings. ADR-0012 was revised to keep this memory in its own repository.

## Next

1. File the first issues in the hub: one per decision record waiting on a ruling, one per missing design doc (16), one to challenge the company brief's estimates, and one to make the repositories public.
2. Test the flow end to end with the first agent pull request: an issue, a draft pull request that claims it, the checks, the maintainer's review and merge, and the board following along.
3. Write the design docs once the decision records they depend on are ruled.

## Open questions

- Whose name GitHub records as a squash commit's author when the agents' App opened the pull request. Check it on the first agent pull request.
- Whether the skill links get made by a script once the first skill exists, instead of by hand.
