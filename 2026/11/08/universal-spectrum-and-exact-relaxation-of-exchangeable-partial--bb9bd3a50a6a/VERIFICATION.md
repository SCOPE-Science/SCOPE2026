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

Exact pinned proof: the kernel is a central mixture of subgroup-averaged orthogonal projections, so Fourier scalars are nonnegative and equal to f^{lambda/(k)}/f^lambda by Young branching, with regular-representation multiplicity (f^lambda)^2. For nontrivial lambda, conditioning on first k tableau labels in row one, a specified minimal cell in the second row is first in at least 1/(n-k) of linear extensions; telescope to f^{lambda/(k)}/f^lambda <= (n-k)/(n-1), sharp for (n-1,1). Include k=0 separately, leading to eta_*=(n-E K-w_0)/(n-1), gap=(E K+w_0-1)/(n-1); Pr[K>=2]>0 iff transpositions possible. Independent finite S_3 and S_4 transition/eigenvalue checks corroborated several fixed-size values; no extrapolation from them.

## originality

PASS

Best-of-knowledge: a central group convolution with conjugate subgroup Haar averages is diagonalized by restriction-to-trivial multiplicities f^{lambda/(k)}, while the sharp uniform nontrivial tableau bound yields an all-size-law gap depending solely on E[K] and w_0. Inspected earlier work uses a single-pass record statistic, contiguous rather than exchangeable blocks, different generators, or spectral comparisons; none of the checked full statements implies this complete spectrum. General character theory and unpublished classical hypergraph shuffle results remain a real priority risk.

## value

PASS

Determining the entire Markov spectrum for arbitrary exchangeable size laws and proving a two-statistic exact relaxation rate is a structural universality result: laws with different higher moments share the spectral gap but not higher eigenvalues. It is beyond standard numerical checks or a mere parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
