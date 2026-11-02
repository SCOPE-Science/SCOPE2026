---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For the ordinary Chari–Joswig graph Morse matching complex, a simplex is an acyclic partial successor function v->w (one outgoing per used vertex; opposite arrow pair prohibited by the 2-cycle). A face fixed setwise by g chooses either no arrows or one equivariant arrow orbit per vertex orbit A. The target orbit B must satisfy d_B|d_A, same-orbit targets force a directed cycle, and the number of equivariant choices is w_AB=|N(a)∩B|. A cycle in the orbit digraph lifts to a cycle because lengths around a quotient cycle divide cyclically, hence are equal and the composite is a finite cyclic shift; every original directed cycle projects to a quotient directed cycle. Thus invariant faces equal weighted rooted quotient forests. The action on its d_A chosen incidence vertices is a d_A-cycle, with sign (-1)^(d_A-1); its chain-degree weight is t^(d_A). The source-weighted directed matrix-forest/principal-minor identity yields det(I+D_g(t)L_g) coefficientwise. Augmented Hopf trace has λtilde=-F(-1); each D_A(-1)=-1 gives -det(I-L_g), including the empty and isolated-vertex cases. For K_n, nonzero orbit weights d_B occur exactly for divisor-sized targets; length-class blocks are (1+y_d(s_d+d r_d))I-y_d d J, with eigenvalues (1+y_ds_d) once and (1+y_d(s_d+d r_d)) multiplicity r_d-1. Product gives the claimed cycle-type formula, including possible zero factors and n=1. Separately wrote a distinct exact checker that enumerated unoriented edge-supported subsets of directed incidence pairs, enforced forestness by disjoint-set cycle detection, and calculated action signs from permutation inversions; it verified full signed graded polynomials against symbolic orbit-determinants on all 293 labeled graph-automorphism pairs for 1<=n<=4. These checks corroborate, not replace, the arbitrary-order combinatorial proof.

## originality

FAIL

The exact universal fixed-orbit forest reduction and -det(I-L_g) reduced Lefschetz formula in the submitted finding are already present, for arbitrary graphs and automorphisms, in proof steps 2-3 of the published fixed-vertex-square SCOPE finding. That prior proof identifies all weighted quotient outgoing arrow choices and their signs, not merely its special cone-over-tree theorem. The submitted multigraded refinement substitutes source-specific z_A=(-1)^(d_A-1)t^(d_A) into the same preexisting directed weighted matrix-forest/minors identity, with q+1=sum_A d_A; this is a formal weighting of the already described bijection, not a new structural lemma. The K_n divisor weights and determinant are independently present in the published isolated-rooted-forest character source; the cycle-length block eigenvalue product is routine algebra from those values. The latter two findings share the same 2026-10-11 published reconciliation commit timestamp with the audited target, so no temporal-priority assertion between them is justified; the objective issue is overlap/implication and absence of a separate new result, not invented earlier authorship. Chari/Joswig and Contreras/Tawfeek give the older identity specialization; Chebotarev/Shamis the general determinant.

## value

FAIL

The equivariant graded chain polynomial is a natural mathematically useful invariant, and its determinant form is computationally convenient. As a distinct new research claim, however, its only nonstandard graph-symmetry step—the complete arbitrary-(G,g) orbit forest bijection and signed determinant—is already proved in the contemporaneously published fixed-vertex-square SCOPE result. The grading consists of replacing each selected source-orbit weight -1 by (-1)^(d_A-1)t^(d_A) in the classical weighted matrix-forest polynomial, which introduces no separate structural classification. The K_n factor is a straightforward block-eigenvalue evaluation of the cycle-divisibility weights already used in the published isolated-rooted-forest result. No additional unexpected boundary, unknown invariant beyond that prior method, or independent mathematical gap is resolved. Expository usefulness does not amount to a distinct research contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
