# Where the project stands

Rewritten with each change, never appended to. Last rewritten 2026-11-21.

## Phase

Phase 0, paper architecture ([charter](https://github.com/citrusunshiu/project-fa/blob/main/docs/charter.md)). It's done when every planned component has a design doc, every founding decision record is decided, the company brief's estimates have been challenged, and the checks find nothing over the whole history. The repositories go public during Phase 0 rather than at its end, so that rulesets can require an approval before every merge ([#5](https://github.com/citrusunshiu/project-fa/issues/5)).

## In flight

- [#12](https://github.com/citrusunshiu/project-fa/pull/12) closes [#7](https://github.com/citrusunshiu/project-fa/issues/7): AGENTS.md says to post only through `tools/post_checked.py`, which [#11](https://github.com/citrusunshiu/project-fa/pull/11) added, and the maintainer owns the wrapper.
- [#5](https://github.com/citrusunshiu/project-fa/issues/5): the rulesets and the reviewer App work. The App's merge without an approval was refused ([#8](https://github.com/citrusunshiu/project-fa/pull/8)); the reviewer App's approval let the agents App merge #11, which touched no protected path; #12 touches protected paths and waits for the maintainer even with the reviewer's approval. The reviewer needed write access: GitHub counts an approval only from an author who can push.
- [#4](https://github.com/citrusunshiu/project-fa/issues/4): squash commits from agents' pull requests are authored by `project-fa-agents[bot]`. An agent's merge through the API with the description as the message gives a clean commit; a merge from the web page wraps the message and adds co-author lines.
- [#10](https://github.com/citrusunshiu/project-fa/issues/10): small follow-ups from the review of #9.
- Decision records 0001 to 0012 wait on the maintainer's rulings.

## Next

1. Close #5 once #12 shows the maintainer's paths waiting for the maintainer.
2. #4 and #10.
3. File the first issues in the hub: one per decision record waiting on a ruling, one per missing design doc (16), and one to challenge the company brief's estimates.
4. Write the design docs once the decision records they depend on are ruled.

## Open questions

- Whether the maintainer's merges of protected pull requests go through the web page or are handed to an agent after approval, so every squash commit is clean (#4).
- Whether the skill links get made by a script once the first skill exists, instead of by hand.
