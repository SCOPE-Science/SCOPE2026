---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For N=2^n and Boolean Walsh-Weyl basis W_{u,v}, Hilbert–Schmidt orthogonality and covariance of the full N² orbit give singular values sqrt(N)|A_z(u,v)| (for unnormalized g_z). Only shifts of weights 0,2,4 have nonzero ambiguity. Weight0: |z|²+K_{n,2}(w). Weight2: unequal Walsh signs give −2i Im z, equal signs give 2(Re z+epsilon(n−2−2j)). Weight4: K_{4,2}(r), magnitudes 6 for N/8, 2 for 3N/8, zero N/2 each. Counting zeros produces rank N−Z0+binom(n,2)(N−Z2)+binom(n,4)N/2, with defect loci explicit; z=n+i avoids them. Weight4 positive modes dominate all others by O(n^-2), proving uniform weak law 3/4 delta_2 +1/4 delta_6 for ANY z_n. Independent direct autocorrelation enumeration verified dimensions 4..6 multiple rational/complex z; all-order proof is algebraic.

## originality

PASS

PASS best of knowledge: Bojarovska–Flinth and Goldberger–Kang–Okoudjou give the general Gabor/Weyl ambiguity spectral reduction, which is credited, but not the complete Boolean apex-weighted weight-two-shell correlation enumeration, exact complex-parameter rank discriminant, or parameter-uniform two-atom positive spectrum. Indexed cyclic near-flat rank and Boolean Turán shell results concern different windows or operators. A hidden association-scheme specialization remains a priority risk.

## value

PASS

PASS: It provides the complete finite-parameter rank and singular-spectrum loci for a motivated sparse Boolean Gabor measurement family, including additive rank defects at intersections and a robust universal bulk law. This exact natural operator invariant could be used to design or rule out matrix recovery directions, even though parity prevents full phase retrieval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
