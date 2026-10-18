---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For A(V*)=(K,V*,K) with lower-left multiplication, R=(0,V*,0) is square zero. Given any two-sided ideal I, nonzero first diagonal scalar forces e0 by e0 I e0 and hence all R by R e0; similarly for e1 and e1 R. If neither appears, I=0⊕W⊕0 for closed W⊂V*; one diagonal forces its full kernel-of-opposite-character ideal; both give the unit. Closed ideals containing K(X) correspond to those in the Calkin quotient. Liu–Shen Corollary 9.6 supplies E(X)/K(X)=R. Works for V=0 and real/complex scalars. Correct as a short direct algebraic consequence.

## originality

FAIL

FAIL: The exact stronger algebraic realization by Liu–Shen already implies the entire claimed lattice without a new mathematical ingredient: the radical ideal interval is expressly proved in Theorem 1.4 and all additional cases follow immediately from multiplying by the two canonical diagonal idempotents (and the universal quotient ideal correspondence). The audited theorem is a routine corollary of those explicit stronger results even though they do not state this precise list in one proposition. Original wording not separately found is insufficient.

## value

FAIL

FAIL: The complete-ideal classification of an explicitly given two-by-two square-zero triangular algebra is an immediate textbook two-idempotent exercise and routine quotient-correspondence exercise. It adds no nonstandard lemma, boundary, invariant calculation, or mathematical difficulty beyond those already supplied explicitly by Liu–Shen, notwithstanding the natural object and convenient restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
