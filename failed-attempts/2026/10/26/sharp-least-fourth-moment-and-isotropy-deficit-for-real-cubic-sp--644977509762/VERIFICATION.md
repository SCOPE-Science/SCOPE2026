---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An independent spherical Wick contraction gives the moment formulas. For the second moment only pairings between the two tensors survive trace-freeness, giving 6t/7!!=2t/35. For the fourth moment the loopless cubic multigraphs on the four tensor copies have opposite-edge multiplicities (3,0,0), (2,1,0), or (1,1,1), up to permuting the three opposite-edge pairs. They contribute 108t², 1944u and 1296v, respectively, divided by 13!!; the count per ordered triple (a,b,c) is (3!)⁴/(a!b!c!)². Writing A_i=(T_ijk)_{jk}, the tetrahedral contraction is v=Σ_ij tr(A_i A_j A_i A_j), and Σ_i A_i²=M by full symmetry. For a traceless 3×3 matrix X, tr(X⁴)=tr(X²)²/2 by Cayley–Hamilton. Taking the coefficient of s² at X=A_i+sA_j and summing over i,j yields 4u+2v=t²+2u, hence v=t²/2−u. The resulting fourth moment is 4(7t²+6u)/5005. Subtraction gives the stated squared Frobenius deficit. For xyz, M=I/18 and the probability-measure moments are 1/105 and 1/5005, so the lower bound is sharp and isotropy is necessary and sufficient.

## originality

FAIL

A distinct published catalogue record states the identical universal bound, quartic formula and equality deficit, with the same xyz witness and scope. This is a finding of complete statement-level coverage in the checked catalogue, not a claim of historical priority or an inference about discovery order from the two path dates.

## value

FAIL

The sharp lower moment and equality deficit are meaningful for this eigenspace, but the frozen finding supplies no distinct mathematical contribution beyond the already indexed exact invariant. Neither a new proof of the result nor a new classification of isotropic cubics is a contribution of the frozen record: its basis and coefficientwise method also appear in the matched record.

The dated certificate retains the supplied scientific assessment, sources and limitations.
