---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: On the frozen RESULT.md, conditional on k distinct moved cards, the final deck is a uniform ordered k-prefix followed by increasing untouched labels. The exact Lehmer-digit decomposition gives E[D|k]=(k+1)/2-1/(n-k+1), E[I|k]=k(2n-k-1)/4, Cov(D,I|k)=(k-1)/4+(n-k)/(2(n-k+1))=E[D|k]/2. Monotone conditional means establish unconditional positive covariance for every n>=2,r>=1. One-dependent/Hoeffding and occupancy CLTs imply the stated bivariate covariance for fixed c>0, not a finite-experiment extrapolation. Inspected check.py independently enumerates uniform permutations up to n=7 and histories for n<=5; earlier full mathematical proofs agree. No assertion for varying c.

## originality

FAIL

FAIL: Complete earlier published proofs on 2026-10-26 and 2026-11-02 establish precisely the same law for the same random-to-top kernel. In particular the November 2 theorem already gives all finite conditional moments, the identical conditional covariance, its total-covariance decomposition, and exactly the same bivariate critical Gaussian matrix. This is decisive direct implication, not an unsuccessful-title search. No additional independent final claim survives.

## value

FAIL

FAIL: Both substantive findings—the exact all-r finite covariance identity and the bivariate fixed-c Gaussian limit—are already published in the same mathematical model, not merely similar statistics. Reproving them with equivalent Lehmer and occupancy arguments cannot supply a distinct valuable fact; correctness and code checks do not rescue a complete duplicate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
