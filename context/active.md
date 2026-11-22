# Where the project stands

Rewritten with each change, never appended to. Last rewritten 2026-11-21.

## Phase

Phase 0, paper architecture ([charter](https://github.com/citrusunshiu/project-fa/blob/main/docs/charter.md)). It's done when every planned component has a design doc, every founding decision record is decided, the company brief's estimates have been challenged, and the checks find nothing over the whole history. The repositories go public during Phase 0 rather than at its end, so that rulesets can require an approval before every merge ([#5](https://github.com/citrusunshiu/project-fa/issues/5)).

## In flight

- [#9](https://github.com/citrusunshiu/project-fa/pull/9) closes [#3](https://github.com/citrusunshiu/project-fa/issues/3): CODEOWNERS assigns the maintainer the protected paths, and AGENTS.md says who merges.
- [#5](https://github.com/citrusunshiu/project-fa/issues/5): the repositories are public and the rulesets require an approval before every merge ([#8](https://github.com/citrusunshiu/project-fa/pull/8)); an App's merge without an approval was refused. The reviewer App, project-fa-reviewer, exists. Still to test: that its approval lets an agent merge outside the protected paths, and doesn't stand in for the maintainer's on them.
- [#4](https://github.com/citrusunshiu/project-fa/issues/4): who authors the squash commits from agents' pull requests. [#7](https://github.com/citrusunshiu/project-fa/issues/7): post to GitHub only after the public-text check passes.
- Decision records 0001 to 0012 wait on the maintainer's rulings.

## Next

1. Test the reviewer App's approval on both kinds of pull request, then close #5. #7 splits into both kinds.
2. #4.
3. File the first issues in the hub: one per decision record waiting on a ruling, one per missing design doc (16), and one to challenge the company brief's estimates.
4. Write the design docs once the decision records they depend on are ruled.

## Open questions

- Whether GitHub counts the reviewer App's approval toward a required review.
- Whether the skill links get made by a script once the first skill exists, instead of by hand.
