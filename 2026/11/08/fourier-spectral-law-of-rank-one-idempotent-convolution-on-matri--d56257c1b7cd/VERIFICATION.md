---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For every prime p and n≥3, rank-one idempotents are uv^T with v^Tu=1, modulo p−1 rescalings. Summing over v enforces u as a rational eigenvector of frequency A, so the exact complex multiplier is p^{n−1}/(p−1) sum_{λ∈Fp} p^{mλ(A)}ζ_p^λ; cyclotomic minimal polynomial gives zero iff all eigenspace dimensions coincide. Counting invariant subspaces of specified λ and imposing A|Uλ=λI yields exact Gaussian-binomial mixed moments and finite q-binomial inversion of joint eigenspace distribution, hence exact nullity/rank for every n. For fixed p, the mixed moments converge to products and Gaussian tails dominate the inversion, yielding asymptotically independent Jλ with π(k)=Q∞p^{-k²}/Q_k², the full complex/singular pushforward law, zero atom H_p=sum π(k)^p and iterated p→∞ limit e^{-1}. Independently checked small p2 Gaussian-moment normalization and the proof of the character coefficient and joint limit; stored checks are supplemental.

## originality

PASS

The random-matrix eigenspace marginal and limiting independent primary components follow older finite-field cycle-index theory. The submitted distinct contribution is their assembly with the exact rank-one idempotent convolution multiplier, finite joint Gaussian inversion for zero modes, and the complete limiting complex spectral measure including zero atom. No inspected earlier result states this combined operator result.

## value

PASS

An explicit finite-rank formula and a complete limiting *complex* spectral law for a natural non-selfadjoint additive matrix Cayley operator yield an exact positive zero atom and surprising e^{-1} limit. These are distinct natural operator invariants and not just a small-case matrix enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
