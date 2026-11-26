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

Border length j pairs with length n-j by cancellation of the central overlap. The independent outer pairs yield a lazy walk in dimension q-1, with all its positive returns through m=floor(n/2) counted twice except a return at the even midpoint. The exact expectation follows by linearity, and the excursion-plus-surviving-tail decomposition gives the formal return-count PGF with v=u² at odd length. The Fourier integrand is the squared modulus of the average of q phases, with unique maximum one on the torus; its quadratic matrix is diag(1/q) minus the all-ones matrix divided by q², with eigenvalues 1/q (multiplicity q-2) and 1/q². Scaling the neighborhood by sqrt(k), the fourth-order local remainder integrates to a relative O(1/k) correction against a Gaussian, giving the stated p_q. For q=2 the return-count factorial moments sum products over a time simplex; summable domination near each face by the k^-1/2 bound justifies the Dirichlet integral. The normalized moments r!/Gamma(1+r/2) give sqrt(2)|Z| on the m scale, hence 2|Z| on the stated border n scale. In q=3 the factorial moments are squeezed using time cutoffs m/r and m, giving moments r! of the normalized exponential and border scale factor 2c_3. For q≥4 the positive-return renewal is defective, giving the asserted geometric count. Under continuation of the same path the finite border count differs from twice that count only if a return occurs at or after m (including the even midpoint), so the tail sum gives the stated TV rate. The no-border probability is first-return survival; the binary Green function, monotone logarithmic Tauberian estimate at q=3, and total escape probability at q≥4 give the displayed calibrations. All statements use fixed q and iid uniform letters, not independence across lengths.

## originality

FAIL

The main package is a direct consequence of the previously explicit arbitrary-alphabet paired path and return problem, the exact Abelian-square count and its already published leading asymptotic, and generic local-time renewal identities. The binary full law is previously explicit. The nonbinary PGF need not have appeared with Abelian-border notation: putting u² into the law of the number of completed excursions is a mechanical corollary of the exact model already given by Goč et al. Richmond–Shallit provides the claim's allegedly model-specific leading constant at every q. The relative error improvement for the return kernel follows from the next order of the same Gaussian calculation; the transient TV estimate is the generic sum of remaining return probabilities, with the same already-known kernel tail. No claim is made that a prior paper explicitly printed every sharpened estimate or the full aggregation as a single theorem.

## value

FAIL

The statistic itself is natural and the synthesis is useful exposition, but the frozen package does not resolve a mathematical gap beyond direct application of renewal counting and known Abelian-square asymptotics to the known paired path. The all-q constant and the regimes do not require a new kernel analysis, and the remaining relative-error and variation-rate refinements are routine Gaussian and return-tail estimates, with no separate motivated precision problem or new mechanism established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
