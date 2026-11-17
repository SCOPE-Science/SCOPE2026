---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

For arbitrary fixed Hadamard ratio q>1 and exceptional indices Λ={N_j}, the compressed multiplier matrix B_ji=a_{N_j+ℓ−N_i} has constant diagonal a_ℓ. The off-diagonal multiplicity for a fixed positive difference N_j−N_i is bounded by the number of N_j in [t,q t/(q−1)], which is uniformly finite; the lower triangular part is eventually zero. Because bounded φ has ℓ² Taylor coefficients, B−a_ℓI is Hilbert–Schmidt. A tail invertibility bound transfers square-summability of the complementary Fourier coefficients of φ^n into square-summability of the lacunary coefficients, using φ^{n+1}=φφ^n and geometric decay of finitely many low coefficients. The reverse weighted-to-unweighted inclusion thus holds for all q>1. The other direction follows from monotone H² powers and the lacunary charging inequality N_j u_{N_j}≤q/(q−1)Σ_{n=N_{j−1}+1}^{N_j}u_n. Necessity follows by Paley H¹ lacunary projection and a bounded outer-function modulus concentrated on separated arcs E_k to force divergence when inf N_jβ_{N_j}=0. Source finite checker is corroboration, not all-q proof.

## originality

FAIL

With the enlarged exceptional set Λ_F, all target weights remain unchanged; the target off-Λ lower bound ensures all extra unweighted offsets are innocuous. Thus the earlier exact equivalence on Λ_F is precisely the target equivalence on Λ, despite requiring at least two offsets.

Strongly covering prior statement: the target q>1 classification is the F={0,1} special case (added weights 1). Neither the weaker q>2 2026 initiating article nor dyadic gap creates novelty once this later stronger theorem is included.

The published cluster theorem contains the exact singleton threshold, not merely a related example; full source RESULT.md was inspected rather than judging by its title or abstract.

Let E be earlier cluster theorem, choose F={0,1}, Λ_F=Λ∪(Λ+1), assigning β=1 on the new offset positions. Positivity, root and good-index lower bounds remain, and inf_{n∈Λ_F}nβ_n>0 iff inf_jN_jβ_{N_j}>0 (finite initial exceptions harmless). Therefore E logically implies the entire target iff for all q>1. The submitted compact compression is a 1×1 block instance of E, so O FAIL decisively.

## value

FAIL

The ratio threshold q>1 is a naturally significant problem, but a previously published stronger theorem already solves it for every fixed finite collection of lacunary offsets F with |F|≥2. Embedding the single exceptional set as F={0,1}, with all added offset weights equal to one, gives the target as an immediate special case. The submitted scalar-plus-compact diagonal lemma is also a one-by-one case of the stronger finite block-Toeplitz compression. Thus there is no surviving new exact classification or independently valuable alternative theorem here.

The dated certificate retains the supplied scientific assessment, sources and limitations.
