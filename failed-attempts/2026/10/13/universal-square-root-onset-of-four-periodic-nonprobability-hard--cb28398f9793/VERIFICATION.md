---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Taking the ratio of the two boundary-law equations gives a/c=t^k. Writing H=1+λ2, the definition of t then gives c=H/(t+⋯+t^{k−1}) for t≠1, and either equation gives the stated λ(t). At t=1 its limit is λ_c and a=c=H/(k−1); uniqueness still holds exactly at λ_c, with the additional pair only strictly above. Reciprocal symmetry makes L(s)=log(λ(e^s)/λ_c) even. The three exponent-set variances are k²/4, k(k−2)/12, (k²−1)/12, so L''(0)=k(2k²−k+3)/12>0 also at k=2. For fixed k, δ=λ/λ_c−1 is analytic in s² with positive first derivative in that variable, hence the positive root has the stated expansion through remainder O(δ^(3/2)). Substituting M=tanh(ks/2) and log(a/c)=ks gives both coefficients; normalization cancels H and the first coefficient is asymptotic to √(3/k). These are statements about the q=4 spin-index-periodic translation-invariant branch, not thermodynamic stability. Verification caveat: contrary to the verification prose, frozen verify.py, lines 34–49, checks boundary-equation residuals and the contrast identity at two s values, not convergence of M/√δ or the stated remainder. The coefficient and remainder are justified by the analytic calculation, not that finite script; it was inspected, not executed.

## originality

FAIL

The same-branch primary source supplies the exact analytic parameterization, reciprocal symmetry and, in its monotonicity proof, the exact first nonzero numerator coefficient of the displayed derivative. These data give the normalized quadratic coefficient by taking the leading term of the supplied derivative, and analytic inversion plus the exact ratio a/c=t^k gives precisely the reported amplitude and remainder. This is prior implication coverage on the full parameter class, although the source does not expressly phrase the contrast expansion.

## value

FAIL

The symmetry-breaking contrast is a natural observable. The variance computation is a tidy alternative derivation, but as an exact finding the coefficient and remainder reduce to the existing leading derivative coefficient, reciprocal symmetry, analytic inversion at a nondegenerate minimum, and a change of observable. No distinct boundary-law regime or additional mathematical invariant is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
