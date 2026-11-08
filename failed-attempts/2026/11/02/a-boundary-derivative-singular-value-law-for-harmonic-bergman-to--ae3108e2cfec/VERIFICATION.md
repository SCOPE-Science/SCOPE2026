---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Exact angular compression on harmonic Bergman monomials has weights from h_k=Gamma(k+1)Gamma(alpha+2)/Gamma(k+alpha+2) for all k positive, negative and central crossings. For monomial pairs, direct shift-compression yields opposite signed tail coefficients ±(alpha+1)mn/k²+O(k^-3). For polynomial f,g these combine into finite-band weighted Laurent tails with symbol q=f_prime*conjugate(g_prime), reflected on the negative tail; crossing rows are finite rank. The full proof’s weighted-Laurent block counting lemma is valid for finite Laurent q by Toeplitz finite-section spectral distribution and low-rank block cuts; O(k^-3) perturbations contribute o(t^-1/2) counts. Two tails each supply sqrt(alpha+1)L; summation gives j²s_j→4(alpha+1)L² and associated Schatten/log endpoint. Independently checked e.g. alpha=0, m=n=1: the positive-end commutator diagonal is (k/(k+1)-(k+1)/(k+2))=−1/((k+1)(k+2)), so k² coefficient →−1. The symbolic infinite asymptotics, not finite SVD, establish the claim.

## originality

FAIL

Decisive preexisting stronger theorem: Alexander Pushnitski, arXiv:1710.02652 (2017), Theorem 1.2 gives exact singular-value Weyl constant for EVERY finite-band matrix with diagonals a_(j,j+m)=b_m j^(−gamma)+o(j^(−gamma)). Take gamma=2, b_m=−(alpha+1)q_m for the positive harmonic tail and the reflected symbol for the negative one; Theorem 1.2 independently gives each tail constant (alpha+1)*L², and direct-sum counting gives 4(alpha+1)*L². The asserted sharp law, Schatten threshold and log endpoint are therefore routine consequences of older general spectral theory once the explicit harmonic matrix leading term is computed. A special case need not appear verbatim in the predecessor to be covered. The package did not compare this dominating theorem and the original final claim cannot pass O.

## value

PASS

An explicit coefficient for a natural harmonic Toeplitz commutator and exact Schatten threshold can be useful in operator theory, and the two conjugate frequency tails require normalization care. Scientific utility is separate from novelty: here it is already a corollary of general banded-matrix singular-value results, so V PASS does not produce acceptance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
