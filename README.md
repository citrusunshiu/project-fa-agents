# Project FA agents

The working memory of the AI agents that help build [Project FA](https://github.com/citrusunshiu/project-fa), a made-up delivery company designed and built in public. It holds where the project stands, what's done, each class of mistake and the check that now stops it, which agents do what, the prompts they work from and the procedures they follow. [ADR-0012](https://github.com/citrusunshiu/project-fa/blob/main/docs/adr/0012-agent-working-memory-in-public.md) explains why it's public and why it has a repository of its own.

## What's here

```
context/active.md     where the project stands: the phase, what's in flight, the next steps, the open questions
context/progress.md   what's done in each phase, with links
context/lessons.md    each class of defect found, and the check that now prevents it
seats.md              which agents, models and effort levels do which kinds of work
handoffs/             the prompts agents work from, each linked to its issues
skills/               procedures for recurring tasks, in the Agent Skills format
tools/                the public-text and pull request checks, copies of the hub's
```

## How agents use it

An agent keeps a clone of this repository on `main` beside the one it works in, and reads [AGENTS.md](AGENTS.md) and [context/active.md](context/active.md) before it starts. The skills are linked into each checkout as `.agents/skills` and `.claude/skills`. The links are local and git-ignored.

## How it changes

Through pull requests that only the maintainer merges, after the same checks as the hub and a cold read by an agent that hasn't seen the private context. A memory update that goes with work in another repository is its own pull request here, linked both ways with the work's. [AGENTS.md](AGENTS.md) has the rules.

## Issues

Filed in [project-fa](https://github.com/citrusunshiu/project-fa/issues), with the rest of the project.

## Licence

[Apache-2.0](LICENSE).
