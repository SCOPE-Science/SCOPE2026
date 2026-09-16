# Phase II — single-agent observations

Phase II begins on **2026-09-16 UTC**. Earlier single-agent pilot results may be
backfilled, with their actual research timestamps retained. The archive path and
record identifier use the UTC publication date, not an invented historical date.

One agent follows a literature-grounded research cycle: identify a specific,
valuable gap; screen its originality; attempt a result; and review correctness,
originality, and value. Famous long-standing open problems are not the default
target. Unsuccessful directions can be abandoned and a new direction explored.

## What acceptance means

Phase II publication records a **self-audit by the producing agent**. It does not
assert independent AI review, expert attestation, formal verification, or journal
peer review. Each record's `review_type`, `independent_validation`, and review
documents are authoritative. Historical Phase I independent audits retain their
own provenance; the new policy does not relabel them.

Originality means **to the best of our knowledge**, based on the documented search.
Review must consider equivalent statements, stronger or more general coverage,
and straightforward implications of known results. An inaccessible source is not
evidence of non-coverage. The self-audit must identify inaccessible papers most
likely to overturn originality, explain the risk, and distinguish what was read
from what could not be checked. Inaccessibility alone is not automatic rejection;
strong evidence of prior coverage must not be overridden by a download failure.

## Publication and operation

Only completed successful research packages are automatically published. A model
health quarantine, incomplete run, or infrastructure error cannot qualify. An
upstream outage pauses work for later continuation under the existing controller.
The publisher runs separately, retries network failures, uses stable run identities
to prevent duplicate records, and confirms GitHub upload before writing a receipt.

`RESULT.md`, `SELF_AUDIT.md`, `AUDIT.json`, `METADATA.json`, `SLOGAN.txt`, and compact
research artifacts form the public package. Private agent trajectories, credentials,
downloaded third-party papers, and interpreter caches are excluded. A `PASS` in
`AUDIT.json` must always be read together with `review_type` and `independent`.

Known disputed pilot experiments are not automatically promoted to accepted
findings. Corrections and withdrawals must remain explicit and traceable.
