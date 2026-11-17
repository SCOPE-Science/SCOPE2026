---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For a complete multipartite graph, the r-independence faces are exactly the (r-1)-skeleton plus complete part simplices. The long exact sequence relative to the skeleton gives H~_(r-1) = wedge^r U / sum_i wedge^r U_i, and basis vectors e_v-e_rep_i show the partwise sum is a primitive direct summand over Z. This proves torsion-freeness. Permutation exterior-character determinants give the full trace. For H=product_i S_{m_i}, the invariant quotient reduces to wedge^r W where W is the part-constant augmentation module; letting the equal-sized-part permutation factors act, its invariant component is wedge^r Q^(t-1), so the full geometric quotient rational Betti rank is binom(t-1,r). At r=1 this reduces to the number of part orbits minus one; at r>=N the simplex is contractible. Fresh independent finite homology profiles agree in 16 parameter/threshold instances; no finite computation replaces the general chain proof.

## originality

FAIL

The dated 25 Oct 2026 prior Resultary theorem establishes, for the SAME complete multipartite higher independence complexes, exactly the SAME canonical full-automorphism integral exterior-augmentation quotient lattice, torsion freeness, every automorphism character, and within-part quotient rank. It also establishes the full quotient in the equal-size case. The submitted additional rank binom(t-1,r) for arbitrary size multiplicities is mechanically implied by that earlier full automorphism module: take invariants of the already-known representation under block exchanges among equal-size parts and use exterior-power hook non-invariant factors. No independent new module theorem remains. O FAIL is based on direct implication, not title matching or unsuccessful searches.

## value

FAIL

The integral module, complete character, within-part quotient and equal-size full quotient are previously established exactly. The remaining arbitrary-size quotient dimension is an elementary finite-group invariant extraction from the previously known full module: decompose its part-index representation into t-1 trivial coordinates and standard representations on equal-size block orbits; positive exterior powers of standard factors contain no invariants. It supplies no new difficult classification or motivated invariant not implied by prior results. The naturalness of quotient homology is acknowledged but cannot turn a mechanical corollary into independent value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
