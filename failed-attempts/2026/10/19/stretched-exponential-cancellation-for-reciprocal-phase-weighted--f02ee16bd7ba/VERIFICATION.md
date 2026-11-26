---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For each fixed real α>−1, the stated monomial normalization and angular orthogonality reduce the eigenvalues of the bounded Toeplitz operator to the beta-normalized scalar integral. Take s=1−t and ζ=exp(−iπ/4). On the tiny lower-sector arc, |exp(i/s)|≤1 and the arc integral is O(ε^(α+1)); the bridge from ζ to 1 has |1−s|≤|1−ζ|<1. On s=ζu/√n, the leading exponential is exp(−ζ√n(u+1/u)), since i/ζ=−ζ; the subleading analytic factor at u=1 is exp(−ζ²/2)=exp(i/2). Along the ray |1−ζr|²=1−√2 r+r² for 0≤r≤1, giving a uniform exponential tail bound for large u; the reciprocal term bounds small u. On a compact interval away from the minimum u=1 there is a strict real-part gap. On u=1+n^(−1/4)v, the exact identity u+1/u−2=(u−1)^2/u gives Gaussian localization. For example, in the symmetric window |v|≤n^(1/20) the order n^(−1/4) correction is an odd linear-plus-cubic term and integrates to zero; Taylor's remaining integrand is bounded by n^(−1/2) times a fixed polynomial against a decaying Gaussian, while the rest of the neighborhood is negligible. The integral is thus asymptotic to √π ζ^(α+1/2) exp(i/2) n^(−α/2−3/4) exp(−2ζ√n) with the stated relative error. Dividing by Γ(α+1)n^(−α−1)(1+O_α(n^−1)) gives the exact constant, power and phase. The nonzero leading term gives the logarithmic limit, and diagonal singular values are the moduli, giving every Schatten class. The independent Kummer-function reduction in the originality evidence checks the same constants and error. The supplied quadrature source was inspected, not executed; its reported 12 ratio checks and four decay checks are corroboration only.

## originality

FAIL

The claim is mathematically correct but directly implied, including its full complex leading term and relative remainder, by the established Kummer U and Bessel K asymptotics after a single moment substitution. The distinct later-dated catalogue matches are material corroboration of equivalent coverage, not the basis for priority. Failure rests on a verified classical implication, not on an inaccessible article or lack of an exact earlier Toeplitz title.

## value

FAIL

The unimodular example is instructive, and its asymptotic is correct, but the exact invariant is mechanically supplied by standard special-function expansions after a single substitution. The logarithmic limit and all-Schatten conclusion are routine consequences of that same asymptotic and diagonalization. The frozen record supplies no genuinely distinct invariant or operator phenomenon beyond this application to support a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
