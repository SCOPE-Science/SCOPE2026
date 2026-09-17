# Phase II publication format

## Identity and paths

Phase I paths remain unchanged. Phase II records use
`YYYY/MM/DD/<topic-slug>--<run-hash>/` (UTC publication date).
Failed Phase II attempts use the same convention beneath `failed-attempts/`.

- For each new finding, use a random UUIDv4 in the legacy-named `scope_run_id`
  field. It is an opaque publication identity, not a research-session identifier.
  Do not encode timestamps, platforms, models or task relationships in it.
  Preserve it through publication corrections.
- Use a short descriptive English topic label: lowercase ASCII words separated by
  hyphens, at most 72 characters, with no leading or trailing hyphen. The complete
  slogan belongs in `SLOGAN.txt`, not in the folder name.
- `run-hash` is the first 12 lowercase hex characters of SHA-256 of the exact
  UTF-8 `scope_run_id`. Do not invent the hash or allocate a daily sequence number.
- Before creating a record, search existing metadata for this publication ID. An existing
  record is the same publication: update its current path, do not create another
  folder because the title or date changed.
- For new successful records use `SCOPE-YYYYMMDD-<run-hash>` as `record_id`.
  Existing record IDs are immutable, including old numeric ones. For new failed
  attempts use `SCOPE-FAIL-YYYYMMDD-<run-hash>`. Separate records have distinct
  publication identities. Legacy records without `scope_run_id` are identified
  by their immutable `record_id` or `failed_attempt_id`; do not rename them.
- A hash suffix greatly reduces accidental collisions; it is not a substitute
  for checking metadata. If an occupied path belongs to another identity, STOP;
  never overwrite it or silently merge records.

## Atomic upload and retries

Read the current default-branch head, construct one Git tree/commit containing the
complete package, then update the branch only if it still has that parent. If
another writer updates the branch, fetch the new head, preserve its changes, recheck
identity/path collisions, and retry. Never force-push. Do not upload the final
`AUDIT.json` PASS marker before all other required files are present.

After upload, read back every file and verify hashes/provenance. If the client
cannot commit the package atomically, upload result and artifacts first, metadata
and slogan next, and AUDIT last; use the same identity when resuming. Do not mark
an incomplete upload as published.

## Content and migration

Keep the existing record package and same-model review policy from `RECORD_FORMAT.md`.
Do not upgrade review status during upload. Do not include private trajectories,
credentials, third-party full-text papers, or invented missing attachments.

`PATH_MIGRATIONS.json` maps old paths to current paths. Old IDs and immutable
commit links remain valid identifiers; GitHub main-branch folder links do not
automatically redirect. Consult the mapping when resolving old paths. Record
identities remain stable after editorial corrections.

Resultary sync resolves migrated legacy records by immutable record ID, retaining
their existing Resultary paths to avoid duplicate indexing. New nonnumeric records
use an explicitly SCOPE-prefixed topic folder in Resultary. Failed attempts are
never synchronized to Resultary.
