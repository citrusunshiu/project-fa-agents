# Where the project stands

Rewritten with each change, never appended to. Last rewritten 2026-11-21.

## Phase

Phase 0, paper architecture ([charter](https://github.com/citrusunshiu/project-fa/blob/main/docs/charter.md)). It's done when every planned component has a design doc, every founding decision record is decided, the company brief's estimates have been challenged, and the checks find nothing over the whole history. The repositories go public during Phase 0 rather than at its end, so that rulesets can require an approval before every merge ([#5](https://github.com/citrusunshiu/project-fa/issues/5)).

## In flight

- [Pull request #6](https://github.com/citrusunshiu/project-fa/pull/6) fixes [#1](https://github.com/citrusunshiu/project-fa/issues/1), the public-text check loading no private terms in a linked worktree, and [#2](https://github.com/citrusunshiu/project-fa/issues/2), the check rejecting GitHub's committer address. The copy here follows it.
- Going public, with rulesets that require an approval before every merge, and a reviewer App for the second agent's approval ([#5](https://github.com/citrusunshiu/project-fa/issues/5)).
- [#3](https://github.com/citrusunshiu/project-fa/issues/3): the maintainer owns only the protected paths, and agents merge the rest. [#4](https://github.com/citrusunshiu/project-fa/issues/4): who authors the squash commits from agents' pull requests. [#7](https://github.com/citrusunshiu/project-fa/issues/7): post to GitHub only after the public-text check passes.
- Decision records 0001 to 0012 wait on the maintainer's rulings.

## Next

1. Go public, apply the rulesets and set up the reviewer App (#5).
2. #3, #4 and #7.
3. File the first issues in the hub: one per decision record waiting on a ruling, one per missing design doc (16), and one to challenge the company brief's estimates.
4. Write the design docs once the decision records they depend on are ruled.

## Open questions

- Whether GitHub counts the reviewer App's approval toward a required review (#5).
- Whether the skill links get made by a script once the first skill exists, instead of by hand.
