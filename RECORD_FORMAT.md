# Record format

An accepted record lives at `YYYY/MM/DD/NNN/` and contains:

- `RESULT.md`: statement, context, definitions, proof or evidence, limitations,
  reproducibility information, and references;
- `SLOGAN.txt`: one to three high-information sentences for later retrieval;
- `METADATA.json`: taxonomy, provenance, source URLs, limitations, and stable ID;
- `AUDIT.json`: correctness, originality, and value judgments, with reviewer type;
- `SELF_AUDIT.md`: Phase II producing-agent review, including search/access limitations;
- `artifacts/`: optional compact verification or reuse materials.

Rejected drafts and private agent traces are not published.

For Phase II, `AUDIT.json` has `review_type: "self_audit"` and `independent: false`;
`METADATA.json` has `phase: "II"`, `independent_validation: false`, and
`verification_state: "self_audited"`. A `PASS` is a reported self-assessment,
not an independent verification badge. Historical Phase I formats are unchanged.

`scope_run_id` is the stable publication identity. Research start/completion and
publication are separate UTC timestamps. Paths use the UTC publication date.
The publisher records source file hashes and confirms upload before writing a
private publication receipt. Only compact research artifacts are included, never
private trajectories, credentials, downloaded third-party papers, or bytecode.
