# Seats

Which agents, models and effort levels do which kinds of work. Commit trailers come from here ([how changes land](https://github.com/citrusunshiu/project-fa/blob/main/AGENTS.md#how-changes-land)).

| Seat | Agent and model | Effort | Work |
|---|---|---|---|
| Planner and reviewer | Claude Code, Claude Opus 5.5 | xhigh | Decision records, design docs, tooling and reviews in Phase 0; plans and reviews from Phase 1 |
| Implementer | Codex | To be recorded | Implementation from Phase 1. The model and effort go here when the first Codex seat starts |
| Reviewer | A second agent session that didn't write the change | As the planner | Reviews a pull request and approves it as the reviewer App, project-fa-reviewer |

The planner's trailers:

```
Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Assisted-by: claude-code:claude-opus-5-5
Agent-Effort: xhigh
```


The maintainer rules on every decision record. An agent merges its own pull request once the reviewer App has approved it, unless it touches a path the hub's [CODEOWNERS](https://github.com/citrusunshiu/project-fa/blob/main/.github/CODEOWNERS) assigns to the maintainer; the maintainer approves and merges those, and every change here. The rulesets enforce the approvals.
