# Where the project stands

Rewritten with each change, never appended to. Last rewritten 2026-11-21.

## Phase

Phase 0, paper architecture ([charter](https://github.com/citrusunshiu/project-fa/blob/main/docs/charter.md)). It's done when every planned component has a design doc, every founding decision record is decided, the company brief's estimates have been challenged, and the checks find nothing over the whole history. Then the repositories go public.

## In flight

- The first change through the whole flow: [issue #1](https://github.com/citrusunshiu/project-fa/issues/1) and [pull request #3](https://github.com/citrusunshiu/project-fa/pull/3), which add CODEOWNERS.
- [Issue #2](https://github.com/citrusunshiu/project-fa/issues/2): the public-text check loads no private terms in a linked worktree, so the pre-push hook there checks nothing private.
- Decision records 0001 to 0012 wait on the maintainer's rulings. ADR-0012 was revised to keep this memory in its own repository.

## Next

1. Fix issue #2.
2. File the first issues in the hub: one per decision record waiting on a ruling, one per missing design doc (16), one to challenge the company brief's estimates, and one to make the repositories public.
3. Write the design docs once the decision records they depend on are ruled.

## Open questions

- Whose name GitHub records as a squash commit's author when the agents' App opened the pull request. Pull request #3 answers it.
- Whether the skill links get made by a script once the first skill exists, instead of by hand.
