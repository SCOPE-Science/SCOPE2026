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

Functional calculus gives 0≤X−X²≤I/4 and hence forward invariance under 0<B≤2I. If X is fixed and C=B⁻¹, then CXC=X−X². An eigenvector v with Xv=v would give XCv=0 and therefore ⟨v,Cv⟩=0, impossible. Thus X−X² has support S=ran X. Invertibility gives ran(CXC)=CS, so C reduces S. On S, X is invertible and the positive matrix X^(1/2) C X^(1/2) has square X²(I−X). Its unique positive square root is X(I−X)^(1/2), yielding C=(I−X)^(1/2) on S and the asserted commuting projection formula, including X=0. Conversely each eligible projection satisfies the equation. Ranks in each eligible eigenspace index the compact Grassmannian components. In a common eigenbasis the Hermitian derivative has real multiplier b_i b_j(1−x_i−x_j) on each real coordinate. An omitted b>1 produces b²>1, so only the fully occupied X_* can attract exponentially. Its inactive and mixed multipliers are strictly subunit under the proposed condition. On the active square [1,√3]² the multiplier b/a+a/b−ab decreases strictly in each argument, with opposite corners 1 and −1; hence all interior pairs are strictly inside. Frobenius norm diagonalization and derivative continuity give a local contraction, with equivalent estimates in any fixed matrix norm. The uniform exponential estimate, differentiated for each iterate at the fixed point, forces spectral radius <1, which rules out b=1, b=√3, and b>√3 via diagonal modes. No boundary behavior slower than exponential is ruled out by this argument.

## originality

PASS

The map, scalar dynamics, and scalar stability window are prior; the fixed-point rigidity for arbitrary strictly positive Hermitian anisotropic coupling and the sharp ambient stability classification are not present in the closest inspected statements. In particular, the matching interval in the earlier two-mode fluctuation record concerns stability transverse to an invariant channel, not stability of the matrix equilibrium against all perturbations.

## value

PASS

This is a complete equilibrium classification of an established noncommutative dynamical map in a natural coupling regime. It distinguishes repetition-induced fixed manifolds from genuinely noncommuting fixed points and proves that unequal-eigenvalue perturbations cannot silently tighten the scalar local threshold. The exact criterion simultaneously treats nonattraction, degeneracy, and both neutral boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
