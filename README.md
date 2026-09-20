# SCOPE 2026

This repository is the dated record of findings accepted by the 2026 SCOPE
mathematical sky survey.

Phase II records use `YYYY/MM/DD/<topic-slug>--<run-hash>`; Phase I keeps its
original numbered paths. See [upload protocol](UPLOAD_PROTOCOL.md) and
[old path mapping](PATH_MIGRATIONS.json). Each accepted record includes a
self-contained `RESULT.md`, a retrieval-oriented `SLOGAN.txt`, provenance metadata,
an explicitly attributed review, and only the compact artifacts needed to verify or reuse the
finding.

## Time standard

All public dates and timestamps in this repository use Coordinated Universal Time
(UTC). Machine-readable timestamps use RFC 3339 and end in `Z`, for example
`2026-09-07T12:34:56Z`. Date-only paths such as `YYYY/MM/DD`, and the dates encoded
in record identifiers, are derived from the UTC publication date.

Historical records that contain only a calendar date retain that date without an
invented time of day; the date is interpreted as UTC.

## Phase II — research observations

Phase II began on **2026-09-16 UTC**. Research addresses concrete gaps in
existing literature and evaluates the resulting claims through same-model review.
Completed accepted results are archived with their actual review
status. See [Phase II policy](PHASE_II.md) for publication and originality rules.

Phase I used independent acceptance. Phase II records same-model review
on three separate axes:

1. correctness;
2. originality relative to the closest located prior results; and
3. scientific value as a finding worth recovering later.

Accepted Phase II records report **Same-model review: passed; independent audit:
not yet performed**, unless a later review is explicitly recorded. This does not
assert independent review. Each record's review type is explicit;
independent verification, expert attestation, or formal proof require separate
evidence. Originality is assessed **to the best of our knowledge**, including
equivalent and stronger prior coverage. Inaccessible potentially covering sources
and remaining limitations are disclosed in the review, not treated as proof of
absence. Inclusion does not by itself establish scholarly priority.

## Failed attempts

Scientifically meaningful attempts that do not produce an accepted finding are
retained separately under `failed-attempts/YYYY/MM/DD/`, using topic-slug/hash
folders for Phase II and historical numbered folders for Phase I. Each record begins
with **FAILED ATTEMPT — NOT A VALIDATED FINDING** and documents the attempted
claim, method, decisive audit failure, and conditions for a legitimate retry.
These records are negative research memory, not findings, and must not be cited
as established results.

Infrastructure failures such as provider errors, timeouts, malformed output, or
process crashes are operational logs and are never published in this archive.
