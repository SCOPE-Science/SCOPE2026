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

# Verification

The proof uses the exact inversion partition function \(Z_n(q)=\prod_{k=1}^n[k]_q\), deletion of fixed boundary entries, a complete split over \(\Pi_n(1)\) conditional on \(\Pi_n(2)=2\), and elementary root and asymptotic expansions. All claimed equalities have stated domains.

Run `python3 verify.py` in this directory. The script uses exact rational weights for enumerations of all permutations of sizes \(3,\ldots,7\) at seven positive rational parameters and verifies the exact probabilities and covariances against independent enumeration. A small set of floating-point tests checks the root and asymptotic formulas, not the infinite theorem. The mathematical derivation, rather than those checks, is the proof.

No machine formal proof or independent mathematical audit is claimed. The scientific literature comparisons remain subject to future external historical-priority review.
