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

Matroid shellability yields the labeled wedge; the wheel forest counts give Euler characteristic 31. Every element fixes the spanning-spoke barycenter, so Armstrong gives simple connectivity for every ordinary quotient. Flag orientation by increasing cardinality gives genuine cellular quotient chains (setwise stabilizers act pointwise), with multiplicities handled by signed sums. The frozen script's unit pivot is the chain cancellation obtained by clearing the pivot row with column operations and splitting off the two-term unit summand, not a rational rank calculation. The reported three orbit-cell vectors were independently reproduced by Burnside and Stirling counts. I also checked integral vanishing without running the frozen script: for a prime-order subgroup G, the relative flag chains C*(K,K^G) are free over Z[G], because all nonfixed flag orbits are free. K^G for rotations is the single point supported by all spokes. For the reflection i↦−i label the forest edge-orbits A={e2}, B={e0,e4}, C={e1,e3}, D={s0}, E={s1,s4}, F={s2,s3}. The fixed locus has facets ABD, ACD, ADE, BCD, BDF, CDE, CDF, DEF, by testing unions of the orbits for acyclicity. Collapsing the respective free edges AB, AC, AD, BC, BD, CE, CD, DE leaves the star with center F, hence the locus is contractible. The relative chain complex is exact below degree four; splitting the surjections onto C0 and then onto successive projective kernels gives a split complex below degree four even over Z[G]. Passing to coinvariants preserves that split exactness; these are the relative chains of (K/G,K^G). For D5, at each prime choose a subgroup of prime-to-that-prime index (C2 at 2, C5 at 5, identity otherwise). The transfer on orbit chains from D5-coinvariants to subgroup coinvariants is the sum over left cosets; its composite with projection is multiplication by the index. Thus quotient homology in degrees 1–3 vanishes at every prime, hence integrally. Top homology is free as a subgroup of the free top chains. Euler characteristic gives ranks 30, 15, 6, 3; successive Hurewicz and simply connected homology Whitehead identify the wedges. Replay for the fixed facets, collapses and exact orbit counts: python3 /workspace/branches/independent_topology.py. This does not replay the individual frozen unit pivots. The uploaded script was inspected, not executed; its use of int.bit_count means the stated Python 3.9 minimum is a minor reproducibility erratum (use 3.10+).

## originality

PASS

The supported distinct claim is the integral and homotopy classification of ordinary subgroup quotients of this specific cycle-matroid complex, not the already known labeled wedge or its automorphism representation. The strongest inspected comparisons do not identify these geometric quotients. Kook's primary full text could not be directly retrieved; the accessible abstract and the explicit restatement of his theorem in Moci–Pezzoli support the narrower known result, not an exhaustive statement about his inaccessible paper.

## value

PASS

The wheel and its dihedral automorphisms form a natural symmetric matroid example, with both prime rotation and reflection stabilizers rather than an arbitrary finite cutoff. The quotient classification tests whether fixed points and the regular character produce torsion-free geometric quotients even at primes dividing the group order, and determines the actual homotopy type for each subgroup. Its usefulness is precisely that rational character data alone cannot answer this integral question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
