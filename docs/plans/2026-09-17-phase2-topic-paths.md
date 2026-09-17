# Phase II topic-path migration

Approved design: replace daily numeric folders for explicitly identified Phase II
records with an English topic slug and a deterministic 12-character SHA-256 Run ID
suffix. Existing record IDs, review decisions and all record file bytes remain
unchanged. Phase I is excluded even when published on the Phase II starting date.

Implementation order:
1. Snapshot current remote main in an isolated worktree.
2. Install backward-compatible discovery and stable-ID source-path reconciliation
   in the Resultary synchronizer; test old and new records and idempotency.
3. Update the self-hosted publisher to allocate deterministic topic paths without
   daily counters. Keep research/probe shutdown unchanged.
4. Rename directories in one ordinary commit and add a permanent migration map.
   Non-fast-forward pushes must fail, never overwrite concurrent publication.
5. Update asynchronous upload instructions, push, run synchronization and verify
   unchanged Resultary identities and updated source URLs.

The public repository cannot redirect old GitHub folder URLs. The migration map
resolves those aliases; commit-pinned historical links remain intact. New ChatGPT
uploads must follow UPLOAD_PROTOCOL.md; changing repository documentation cannot
silently replace prompts in already-running external ChatGPT tasks.

Verification: compare SHA-256 of every moved file before/after; ensure full source
discovery count is unchanged; run legacy sync tests plus migration/idempotency and
new-topic tests, and run publisher tests. Do not start any research model calls.
