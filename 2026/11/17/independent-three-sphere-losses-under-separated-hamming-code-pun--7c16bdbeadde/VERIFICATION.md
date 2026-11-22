---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

Known Adamaszek–Adams theorem gives VR≤2(Q_n) ≃ wedge^{c_n} S³ for n≥3 with c_n=Σ_{j=0}^{n−3}2^j binom(j+3,3). The link of a cube vertex has precisely maximal cliques U, S_i, T_ij, V_ijk; a sequence of free-face collapses reduces the subcomplex B without V_ijk to simplex U, with each independent V_ijk 2-cell attached around its boundary. Hence link ≃ wedge^{binom n3} S² with integral V_ijk coordinates. If punctures have Hamming separation at least four, relative deleted-star cone-link chain groups split. Each 3-coordinate subcube through deleted p is an integral S³ whose relative 3-cycle hits the local V_ijk basis by ±1 and no other deleted point, making the global map H3(ambient)→H3(ambient,X_T) a split surjection. Long exact sequence gives primitive H3 rank c_n−|T|binom n3, no other reduced homology. Connectedness by two-coordinate detours, link simply-connected van Kampen, Hurewicz and Whitehead imply the full wedge homotopy type and natural intermediate primitive inclusions/cofibers. Independently enumerated all link maximal cliques n=3,4,5,6,7 with counts 8,15,26,42,64; matches exact U,S_i,T_ij,V_ijk formula. Finite tests do not establish universal homotopy.

## originality

PASS

Global Rips complexes and selected one-puncture cases are already Adamaszek–Adams; these are inputs. Published two-point Hamming deletion profiles classify n=3,4,5 only, with the same n=4,5 rank 1/29 examples. They do not entail all-dimensional arbitrary distance-4 code subsets or primitive inclusion diagrams. Bendersky–Elia–Grbić study full-cube cohomology/ghost vertices; Galetto–Montaño–Wellner studies equivariant full-cube homology. No inspected stronger puncture theorem covered the exact quantification.

## value

PASS

Arbitrary separated code punctures form a natural and unbounded multiple-missing-data perturbation of a well-studied Rips family. A uniform all-dimensional wedge classification, precise independent loss per removed codeword and full integral inclusion diagram are structural facts with practical reuse in code-based topology and persistence, not a re-enumeration of isolated examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
