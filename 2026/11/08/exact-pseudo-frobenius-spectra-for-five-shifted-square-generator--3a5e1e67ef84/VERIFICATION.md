---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For each a>=34, the exact coin-length recurrence yields ell(n+16)=ell(n)+1 (n>=16) by finite base rows and strong induction. With generator offsets 1,4,9,16, all alternate wraps cost at least as much and the Apéry representatives are w(r)=r+a*ell(r). The PF condition w(r)-a+generator∈S is equivalent to the four displayed coin-length inequalities. Low residues yield only 7,15; interior residues are excluded by the 16-shift identity; terminal residues reduce to 16×16 congruence tests plus monotonic wrap checks at a=34..49. Recalculated the entire table and independent Apéry/Dijkstra PF sets for a=34..90. A=33 has the documented failed member 65+49=114. Thus exact spectrum, type period 16 and stated sharp domain hold; finite checks corroborate the infinite induction rather than replace it.

## originality

PASS

Best-of-knowledge original exact PF-set classification and sharp threshold; previously published formulas cover Frobenius maximum and eventual translation, not this complete 16-case table.

## value

PASS

For a natural 5-generator shifted-square numerical-semigroup family the complete pseudo-Frobenius set and Cohen–Macaulay type are structural invariants; an explicit 16-class periodic table with an optimal starting threshold is a meaningful classification not mechanically supplied by the known Frobenius maximum formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
