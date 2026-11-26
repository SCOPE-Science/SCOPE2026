---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For the 15 duads versus 15 synthemes, each symbol indicator s_i has s_i B equal to the all-ones row. The six indicators are independent over Q since each two-symbol coordinate tests c_i+c_j; hence five differences are independent left-kernel vectors and rank_Q B≤10. My independent script enumerates triples of duads with six distinct symbols, reconstructs the five numbered flags from the table and checks them as ones with distinct endpoints. Signed partial-permutation dynamic programming for the Leibniz determinant, not the supplied Bareiss code, gives core determinant −1 and 32 augmented minors all ±1, including full determinant −1 in the stated order. Replay: python3 /workspace/branches/independent_incidence.py; output /workspace/branches/independent_incidence.txt. An independent rational-elimination check agrees. For any selected subset of k flags, expanding the augmented minor in the k edit cells kills every term of degree below k because its coefficient is a minor of B of order greater than ten. Distinct endpoints leave the unit core as the coefficient of their joint product, so the maximal minor is unimodular; rank rises by at most k. The determinantal divisors give 10+k unit Smith factors and 5−k zeros, including the k=0 baseline over every d. For C the edited matrix, the cut amplitude matrix is d^−15 ω^(xᵀCy). Character orthogonality makes the reduced density matrix a direct sum of constant-entry blocks on the cosets of ker Cᵀ over Z/d, with one nonzero eigenvalue per coset; the Smith form gives precisely d^(10+k) equal eigenvalues d^−(10+k). The Schmidt coefficients are their square roots and each positive-order Rényi and von Neumann entropy is (10+k) log₂ d. For fewer than five arbitrary original incidence omissions, reduction modulo any prime divisor of d has rank at most 10+k<15, so C cannot be surjective modulo d and the cut cannot be maximally entangled. This proves necessity for composite as well as prime d; the specified five achieve surjectivity. Bundled scripts and verification notes were read but not executed. The proof says neither that every set of five omissions works nor that other cuts obey the same law.

## originality

PASS

The binary cut-rank method, rank-one edit bound and Smith determinant-divisor theory are prior tools. The distinct result is an optimal allowed incidence deletion pattern on the Tutte–Coxeter cut that raises the rank by one for every selected omission, with a unit maximal minor for every subpattern and therefore a sharp preserved law at every integer dimension. Related omission laws for projective planes are substantive precedents in method and interpretation, not statements implying this generalized-quadrangle certificate. This is a bounded evidence judgment, not historical priority.

## value

PASS

The classical 30-vertex Levi graph and its natural incidence cut motivate the resource question independently of a particular minor. Reaching the deficiency lower bound while deleting only allowed nonzero entries is nontrivial; the unit determinant and every-subset stability make this an exact entanglement benchmark even for composite local dimension, not a binary rank table or routine graph-state application. The work is an ideal preparation benchmark, not a claim about noisy devices or arbitrary cuts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
