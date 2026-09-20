# Phase II — research observations

Phase II begins on **2026-09-16 UTC**. The archive path and record identifier use
the UTC publication date, including for retrospectively published findings.

The archive emphasizes concrete, valuable gaps in the literature and reports
evidence for correctness, originality and scientific value.

## What acceptance means

For accepted results the standard label is **Same-model review: passed.
Independent audit: not yet performed.** Later review outcomes and withdrawals
override this default when supported by evidence. The label does not specify
execution architecture or establish reviewer independence.

Phase II publication records a **same-model review**. It does not
assert independent AI review, expert attestation, formal verification, or journal
peer review. Each record's `review_type`, `independent_validation`, and review
documents are authoritative. Historical Phase I independent audits retain their
own provenance; the new policy does not relabel them.

Originality means **to the best of our knowledge**, based on the documented search.
Review must consider equivalent statements, stronger or more general coverage,
and straightforward implications of known results. An inaccessible source is not
evidence of non-coverage. The same-model review must identify inaccessible papers most
likely to overturn originality, explain the risk, and distinguish what was read
from what could not be checked. Inaccessibility alone is not automatic rejection;
strong evidence of prior coverage must not be overridden by a download failure.

## Publication

Phase II uses topic-label folders with stable publication-identity suffixes, not daily
sequence allocation. Follow `UPLOAD_PROTOCOL.md`; retain existing record IDs.
Consult `PATH_MIGRATIONS.json` to resolve pre-migration source links.

Only complete research packages with passing review are published. Incomplete work and infrastructure errors do not qualify. Stable publication identities prevent duplicates, and uploads are verified.

`RESULT.md`, `REVIEW.md`, `AUDIT.json`, `METADATA.json`, `SLOGAN.txt`, and compact
research artifacts form the public package. Only scientific evidence and publication
metadata belong in this package. A `PASS` in
`AUDIT.json` must always be read together with `review_type` and `independent`.

Known disputed pilot experiments are not automatically promoted to accepted
findings. Corrections and withdrawals must remain explicit and traceable.
