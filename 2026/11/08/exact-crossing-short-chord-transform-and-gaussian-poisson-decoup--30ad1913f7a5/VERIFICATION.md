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

# Verification of the crossing–short-chord theorem

The proof is contained in `RESULT.md`: mark \(k\) nonincident boundary edges, delete them, count the residual matching, apply the binomial transform, and use the published crossing CLT with a summable coefficient bound.

The standalone program `verify.py` requires only Python 3's standard library. Run `python3 verify.py` from the extracted directory. It exhaustively enumerates uniform labeled matchings for each size \(n\le6\), including all 10,395 diagrams at six chords; independently enumerates boundary-cycle edge matchings through five chords; checks the entire mixed binomial identity at every possible crossing count; inverts the transform; and checks exact rational means, variances and covariance.

On the assembled source files the test completed and printed `PASS: 385 exact assertions (all pairings through n=6 and independent cycle-submatchings through n=5)`.

The finite exhaustive checks are not substituted for an infinite proof or for literature priority verification. The asymptotic Gaussian–Poisson independence follows analytically from the fully quantified identity and the cited univariate central limit theorem. The claim is self-reviewed, not independently audited.
