---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The theorem is mathematically correct. The exact-degree-two Laplace eigenvalue is 2d, so the global Dirichlet form is 2d times the scalar L² form. In coordinates u=x_d², the beta density has a=1/2, b=(d−1)/2. Conditioning y on u gives E[y₁²|u]=(1−u)/(d−1), E[(y₁²−y₂²)²|u]=4(1−u)²/[(d−1)(d+1)]. Applying 4(|Ax|²−|xᵀAx|²) to z²−1/d, zy₁ and y₁²−y₂² gives exactly 4q_Z, q_M/(d−1) and 8q_T/[(d−1)(d+1)]. The beta first and second moments yield all three m_j. Symmetry makes the diagonal blocks scalar and the cross blocks vanish, including the distinct O(2) types in d=3; at the crossing the two top blocks sum to the full maximal eigenspace. Alternatively the Green-identity differential transform recorded below directly recomputes all three gaps. Their signs prove strict minimality of T and the unique switch at s=1/2. Positivity on both open regions follows from the nonzero nonnegative energy polynomials, so interior eigenvalues lie in (0,1); t=0 and t=1 give identity and zero. At s→1, q_M/m_M→(d+2)/2 and q_T/m_T∼(d+2)(1−u)/(d−1); integrating the two beta tails gives the ratio (d+1)/(2(1−s)) for fixed d. Replay: RESULT.md, proof steps (1)–(4), substituting the above moments. verify.py was inspected, not executed: the 5×5 sweep evaluates 75 branch integrals, not the stated 125 (lines 49–63); this is a reporting error in supplemental checks, not a flaw in the theorem.

## originality

FAIL

The frozen spectrum and switch are a direct differential corollary of the earlier fully evaluated scalar quadrupole spectrum on the same cap family in every d>=3. The scalar and gradient quotients are indeed different, but the earlier record supplies the *entire aperture-dependent* scalar spectrum and its factored gaps; Green's identity transforms them explicitly into all the frozen gaps. This is decisive mathematical coverage, not similarity of titles, equality of the maximizing cutoff, or a claim that generic vector Slepian theory alone covers it.

## value

PASS

As a mathematical description of derivative-only observation, the exact eigenvalues and thin-cap conditioning constant are meaningful. Neither the maximizing sector nor its transition may be inferred by simply reusing the scalar optimizer, which goes the opposite way as caps shrink. The coverage issue is that the known full scalar curves mechanically give this distinct observation law via Green's identity. No discrete or noisy recovery claim is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
