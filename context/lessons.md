# Lessons

Each class of defect found, the path it took, which check missed it, and the check that now prevents it. Never the text itself.

- **Pull request text checked only after it was public.** CI checks a pull request's title and body once the pull request exists, which is too late to stop private text. Now text bound for GitHub is written to a file, checked with `tools/check_public_text.py --text`, and posted from the file.
- **Private facts in new words.** The term list catches exact terms, not a private fact said another way. Now every change to this memory gets a cold read by an agent without the private context.
- **An author identity from the agent's environment.** An agent's harness set its own author name and email as environment variables, which override the repository's git configuration. The public-text check caught it on the commit, before any push. Now agents commit with those variables unset, and the check runs over every commit in a push.
- **A check aimed at the wrong repository.** The public-text check always scanned the repository holding it, so running it from a client repository re-checked the hub and reported it clean. Now `--repo` names the repository to scan, and the summary line names the repository it scanned.
