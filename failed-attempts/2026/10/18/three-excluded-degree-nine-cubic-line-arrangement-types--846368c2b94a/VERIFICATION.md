---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For 1 smooth cubic+6 distinct lines, a flex A5 consumes the full cubic-line Bezout intersection and cannot participate in a mixed triple. At most four pure three-line triple points occur because each of six lines meets five other lines, two per pure triple (3t<=6floor(5/2)=12). Thus (0,7,4) needs at least three mixed triples but at most C(2,2)=1; (3,5,5) needs five pure triples but max four. For 2 cubics+3 lines with n2=0,n3=2,t5=8, the three lines must concur at one triple; the other triple comprises both cubics and a line, forcing cubic-cubic Bezout 9=1+3s, impossible mod3. Imported Talar free-degree-nine Tjurina and intersection formulas yield four potential types; independent integer enumeration reproduces candidates [(0,7,4),(3,5,5)] and [(0,2,8),(3,0,9)]. Consequence only the last remains necessary; no existence claimed.

## originality

FAIL

Although the three geometric impossibilities extend Talar 2024, this final claim is fully duplicated by another frozen same-day public package in the identical assignment: identical hypotheses, three excluded types, and necessary surviving type. Neither publication nor creation precedence is proven, so scientific originality cannot be decided by arbitrary assignment order. Applying the same exact-coverage bar symmetrically, both redundant packages are rejected as independent novel contributions; their correct and valuable mathematical result is preserved.

## value

PASS

The natural degree-nine freeness boundary in smooth cubic/line arrangements was explicitly undecided numerically; the three independent geometric impossibility arguments narrow the genuine realization question. The result has mathematical use even if the remaining case stays unknown.

The dated certificate retains the supplied scientific assessment, sources and limitations.
