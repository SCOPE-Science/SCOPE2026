# SCOPE 2026

This repository is the dated record of findings accepted by the 2026 SCOPE
mathematical sky survey.

Records are organized as `YYYY/MM/DD/NNN`.  Each accepted record includes a
self-contained `RESULT.md`, a retrieval-oriented `SLOGAN.txt`, provenance metadata,
an independent audit, and only the compact artifacts needed to verify or reuse the
finding.

## Time standard

All public dates and timestamps in this repository use Coordinated Universal Time
(UTC). Machine-readable timestamps use RFC 3339 and end in `Z`, for example
`2026-09-07T12:34:56Z`. Date-only paths such as `YYYY/MM/DD`, and the dates encoded
in record identifiers, are derived from the UTC publication date.

Historical records that contain only a calendar date retain that date without an
invented time of day; the date is interpreted as UTC.

Publication requires independent acceptance on three separate axes:

1. correctness;
2. originality relative to the closest located prior results; and
3. scientific value as a finding worth recovering later.

Inclusion records the outcome of the SCOPE review process.  It does not by itself
establish scholarly priority.

## Failed attempts

Scientifically meaningful attempts that do not produce an accepted finding are
retained separately under `failed-attempts/YYYY/MM/DD/NNN`. Each record begins
with **FAILED ATTEMPT — NOT A VALIDATED FINDING** and documents the attempted
claim, method, decisive audit failure, and conditions for a legitimate retry.
These records are negative research memory, not findings, and must not be cited
as established results.

Infrastructure failures such as provider errors, timeouts, malformed output, or
process crashes are operational logs and are never published in this archive.
