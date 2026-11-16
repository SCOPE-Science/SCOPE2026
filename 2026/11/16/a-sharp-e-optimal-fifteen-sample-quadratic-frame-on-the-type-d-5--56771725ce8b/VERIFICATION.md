---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Mathematical verification

Run `python3 verify_exact.py` with SymPy installed. Its exact rational operations cover all \(252\) possible five-edge graphs and identify all \(162\) with invertible unsigned incidence, separated into four types. It constructs one explicit direct rational fifteen-by-fifteen row Gram matrix per graph shape and verifies the full characteristic polynomial against the five-by-five signless-Laplacian formula. Sturm counting with rational endpoints isolates every smallest squared singular value and establishes the strict ranking of the three levels and the common optimal quartic factor.

Run `python3 verify_numeric.py` with NumPy installed. This separate implementation directly constructs measurement rows for each of the \(5,184\) full-rank sample sets and checks the three least-eigenvalue multiplicities and universal Gram determinant \(1/256\). Floating-point enumeration is a consistency check; it is not the justification for exact root-ordering or completeness.

The proof uses the fixed explicit twenty-line root set, the Frobenius coefficient basis, a finite graph classification, algebraic determinant identities and certified rational Sturm counts; it makes no unverified claim about other point sets, higher-degree harmonics, or external independent certification.
