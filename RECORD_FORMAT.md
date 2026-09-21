# Record format

An accepted Phase II record lives at `YYYY/MM/DD/<topic-slug>--<run-hash>/`.
Phase I retains `YYYY/MM/DD/NNN/`. See `UPLOAD_PROTOCOL.md` for deterministic
identity, concurrency-safe upload and retries, and `PATH_MIGRATIONS.json` for
the old-to-new directory mapping. Each record contains:

- `RESULT.md`: a concise, self-contained mathematical note with necessary definitions,
  a precise statement, sufficient proof or derivation, mathematical limitations,
  reproducibility information, and references; not an administrative review report;
- `SLOGAN.txt`: one to three high-information sentences for later retrieval;
- `METADATA.json`: taxonomy, provenance, source URLs, limitations, and stable ID;
- `AUDIT.json`: correctness, originality, and value judgments, with reviewer type;
- `REVIEW.md`: Phase II same-model review, including search/access limitations;
- `artifacts/`: optional compact verification or reuse materials.

Review-status labels, assessor descriptions, independence disclaimers and originality-search
reports belong in `REVIEW.md` and structured review metadata, never in `RESULT.md`
or `SLOGAN.txt`. Keep mathematical assumptions, unresolved cases and proof gaps
explicit in the mathematical note. Concision must not omit essential proof steps.

Rejected drafts do not qualify as accepted findings.

For Phase II, `AUDIT.json` has `review_type: "same_model_review"` and `independent: false`;
`METADATA.json` has `phase: "II"`, `independent_validation: false`, and
`verification_state: "same_model_reviewed"`. A `PASS` is a reported same-model assessment,
not an independent verification badge. Historical Phase I formats are unchanged.

For accepted Phase II records, use `same_model_review_status: "passed"` and
`independent_audit_status: "not_performed"`. The wording in `REVIEW.md` is: **Same-model
review: passed. Independent audit: not yet performed.** A missing independent
audit is not a failed review. Preserve actual failures, disputes, withdrawals,
and any subsequently evidenced reviews; never reset their status to PASS.

Public records describe scientific evidence and verification status, not execution
topology, internal delivery channels, scheduling, runtime infrastructure, private
prompts, or account information. These details are not part of public provenance.

New records use a random UUIDv4 as the opaque publication identity in the
legacy-named `scope_run_id` field. Existing record IDs and paths are immutable;
legacy records may omit this field. Paths use the UTC publication date.
Public timestamps describe publication or scientific corrections, not research
start, completion, elapsed time or scheduling. Artifact hashes cover the actual
published file bytes. Only standalone scientific verification and reuse artifacts
belong in the public package.
