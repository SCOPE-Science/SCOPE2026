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

# Verification scope and reproducibility

Run the included standard-library script with `python3 verify.py`. It builds Stern numbers and the coefficient polynomials exactly through degree \(131\), checks each shift identity for \(0\le n<128\), proves gcd one *over a prime field* for each tested pair by Euclidean division, verifies adjacent Stern coprimality and the power-of-two unity criterion in the tested range, checks the even-index polynomial decomposition and the discriminant/primitivity arguments for odd indices.

An additional independent exact symbolic-polynomial computation compared \(\gcd_{\mathbb Q[X]}(P_n,P_{n+d})\) for \(d=2,3\) and \(0\le n\le81\); all computed gcds were one. These checks are finite regressions, not proof of the all-index theorem. The proof is contained in RESULT.md and rests on the elementary Stern recursions, a stated general positive-coefficient root bound, and Gauss's lemma.

The modulo-prime gcd calculations do not assert that the integer resultant is nonzero modulo every prime. No independent audit or external certification has been performed. Publication priority remains subject to the cited source-inspection limits.
