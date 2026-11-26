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

For the continuous Cesàro adjoint C*f(x)=∫_x^1 f(y)/y dy, exchanging the integrals on a dense class and extending gives HC*=DH. The row map x^(z−1)/z is L²-holomorphic on Re z>1/2 and has norm 1/(|z|√(2 Re z−1)). On the parameter-2 ellipse in the scaled variable for a=2^j, Re z≥7a/8 and 2 Re z−1≥3a/4; Cauchy's coefficient estimate and the geometric tail give per-row error at most 4M a^(−3/2)2^(−J), M=16/(7√3). Summing squares over a rows and j<J, then bounding the omitted squared row norms by Σ_(n≥2^J)n^(−3)≤(3/2)4^(−J), gives the claimed constant 128/21+√(3/2)<8. There are J coefficient vectors per block, so rank is at most J², not necessarily exactly J². Approximation numbers, J=floor(√(n−1)) for n≥2, and the Hilbert–Schmidt norm for n=1 give the displayed bound. Superpolynomial decay is severe under the cited definition; neither a sharp rate nor a matching lower bound follows. The supplied NumPy script was read, not run; it diagnoses interpolation and finite sections, not the analytic series truncation.

## originality

FAIL

The frozen quantitative existence claim and the severe classification are already a direct consequence of a pre-existing generalized-Cauchy singular-value bound. Proof of implication: let N=2^J−1 and T_N retain the first N rows. Its Gram matrix G_N=T_NT_N* has entries 1/[ij(i+j−1)], with Cauchy nodes i−1/2 and −j+1/2 and weights 1/i and 1/j (column order is immaterial). In Beckermann–Townsend Corollary 4.2, the endpoint cross-ratio is γ=N²/(2N−1)≤N for N>1. For r=J²<N the weakened version gives σ_(r+1)(G_N)≤4 exp(−π²r/log(16γ))‖G_N‖. Hence its truncated singular expansion yields a rank-r approximation to T_N with error ≤2√2 exp(−π²J²/[2(J+4)log 2])≤2√2·2^(−J); use ‖T‖_HS<√2 and J²/(J+4)≥J/5. The approximation is specified by the top r eigendirections of the explicit finite Gram matrix, projecting T_N onto them. If r≥N retain T_N exactly. Zero-extension plus the elementary tail ≤√(3/2)2^(−J) gives a smaller constant than 8, and the same approximation-number consequences for the infinite operator. Thus even the stated all-J numeric guarantee, not just its asymptotic order, is implied. This does not identify the frozen Chebyshev coefficient vectors in prior work, nor claim the 2016 paper explicitly mentions the composition.

## value

FAIL

Severity of this inverse problem is a worthwhile question, and the elementary analytic-row proof is clear. But the frozen claimed advance is the bound and resulting classification, both obtained by direct specialization of an older quantitative theorem. The record does not separately establish a substantive new structural, complexity, or optimality guarantee for the Chebyshev construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
