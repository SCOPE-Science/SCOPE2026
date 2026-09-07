# Public time standard

SCOPE uses Coordinated Universal Time (UTC) for every date and timestamp visible
in the public research record.

- Machine-readable timestamps use RFC 3339 and end in `Z`.
- Human-readable timestamps explicitly include `UTC`.
- `YYYY/MM/DD` repository paths use the UTC publication date.
- Dates embedded in record identifiers use the UTC publication date.
- Audit, version, and publication times preserve the same UTC standard.

Example: `2026-09-07T12:34:56Z` is displayed as
`7 September 2026, 12:34 UTC`.

An older record that contains only a date is not assigned an invented time of
day. Its date is interpreted as UTC.
