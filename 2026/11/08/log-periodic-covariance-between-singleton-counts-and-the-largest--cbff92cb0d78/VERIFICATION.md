---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In the independent cut-bit representation the boundary terms each have mean 1/2 and the n−2 interior singleton indicators each have mean 1/4, also giving the formula for n=2. The marked truncated composition series generates both a and b, and M=1+Σ 1_{M>m} gives the minus sign. Association gives nonnegative indicator covariances and m=1 makes the sum strictly positive before negation. The fixed |z|=3/5 contour has one simple pole uniformly in the marker disk for m≥5. At u=1, 2ρ−1=ε+O(mε²), ε=2^(−m−1); substituting into A'_m(ρ)=[2−(m+1)ρ^m]/(1−ρ) gives 4(1−mε+O(m²ε²)). Differentiation of the pole residue cancels the two 1/A'_m terms and leaves ρA''_m/(A'_m)^2=1/2+O(m²ε) besides n/A'_m. This is why centering gives m nε/4 without an additional order-one term per cutoff. Contour remainders and the central-window polynomial-log/n errors sum to o(1); below the window independent blocks suppress M≤m, and above it forcing the singleton's two cuts only matters if an original all-zero block of length m touches them, giving the summable 2nm2^(−m) bound. The lattice reindexing resolves both terms; unfolding the Fourier integral gives Γ(1−2πik/ln 2)/ln 2, with no zeros. Independent exact-integer sliding-window checks through cutoff 47 give differences from the two-term sum of −0.00546, −0.00139, −0.000353 and −0.0000892 at n=64,256,1024,4096; the omitted exact covariance tail is bounded by the same proven tail inequality. Replay: python -B /workspace/independent_checks.py 3. The infinite error claim rests on the analytic estimates, not the finite checks.

## originality

PASS

The earlier two-term Resultary law is exceptionally close in method and even shares the digital profiles. It is for total part count, not singleton count. Independent joint first-moment information is necessary; no inspected predecessor supplies this marking direction with additive o(1). Credit is limited to this dependence law and not the two-profile technique or the Gamma spectrum in isolation.

## value

PASS

The result quantifies local-versus-global dependence in the standard uniform composition model: a count of the shortest parts has a diverging covariance with the extreme part size, with a resolvable bounded correction. The correction is mathematically meaningful even though the periodic harmonic is small: it distinguishes singleton response from a constant rescaling of the already known total-count response. Uniform mixed-moment estimates and control of both remote cutoff tails are needed; separate limit laws or the earlier total-count result do not deliver this invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
