---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

For k>=3, r>=2 the center deletion is a simplex and X is its homotopy cofiber of the link; the link faces (I,J) obey exactly 1+|I|+|I cap J|<=r. Fiberwise acyclic toggle of b_i for the least missing a_i cancels all non-full-inner fibers; toggling b_1 on I=[k] leaves precisely C(k-1,h) critical faces dimension r-2 for h=r-k-1 in [0,k-1], and none outside. One suspension yields the proposed contractibility and sphere-window formula. The S_k invariant subcomplex I neq [k] is contractible, and the relative chain groups with all a_i selected identify integrally as sign tensor wedge^j Z^k, differential contraction by augmentation; its top kernel is wedge^h U_k. For r=1, the join of k zero-spheres gives S^(k-1) with arm-sign action. Independent exact mod-two chain ranks checked every r for k=3 and 4, and source verifier additionally checks acyclicity and signed characters for k<=5; finite tests do not prove all k.

## originality

PASS

A published tree theorem establishes vertex decomposability for all higher independence complexes of trees, a qualitative wedge statement; fully whiskered and perfect regular-branching formulas have hypotheses not met by once-subdivided star T_k. The exact binomial ranks and integral signed exterior powers of the arm augmentation lattice are not implied by those broader qualitative results. Searches included the different discrete Morse complex of extended stars and did not identify an equivalent higher independence family.

## value

PASS

The once-subdivided star is a canonical partially whiskered family. Its exact higher independence homotopy undergoes a contractibility interval then a nontrivial binomial window, and the natural arm action has a complete integral augmentation-exterior-power description. Both rank and module are mathematically meaningful exact invariants not mechanically determined by qualitative tree shellability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
