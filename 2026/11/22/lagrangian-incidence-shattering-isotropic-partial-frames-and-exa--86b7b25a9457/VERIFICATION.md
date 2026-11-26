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

All-positive forces isotropy; a dependent circuit would require one vector to be excluded from a subspace containing the other circuit vectors that span it. Conversely, extend an isotropic independent support to the e-side of a symplectic basis, and in each coordinate select e_i for positive labels and f_i for negative labels. The generators are independent and orthogonal, including for the all-negative pattern and in characteristic two. If i vectors have span U, choices for a next vector lie in U⊥ outside U, giving q^{2n−i}−q^i and the unordered /k! factor. Extension to a Lagrangian gives purity and VC dimension n. At a first online query v the positive subfamily descends to the symplectic quotient v⊥/〈v〉, and constant or duplicate restricted queries add no depth, so induction gives Ldim≤n; using a shattered basis gives equality. Equivalently, on the all-positive path in any shattered tree of fixed-rank subspaces each subsequent query must escape the span of the earlier positives because its negative child is realizable. For n≥2 the singleton {f_1+f_2} cannot be augmented by either vertex of the larger face {e_1,e_2}, and e_1,e_2,e_1+e_2 form a clique but not a face. Independent face enumeration and binary boundary elimination reproduced face counts (1,3), (1,15,45), (1,63,945,3780), with augmented ranks (1), (1,14), (1,62,883), respectively; these give the claimed reduced Betti numbers with the other groups zero.

## originality

PASS

The isotropic partial-frame geometry itself is directly prior: over a field, the sequences of Mirzaii–van der Kallen's IU poset have precisely these sets as supports. Neither prior existence of the complex nor standard dimension bounds are credited as discoveries. The supported distinct claim is the identification of all Boolean traces of Lagrangian membership through the shattering criterion, which also gives the exact face polynomial and static/online dimension for this concept class. The small homology ranks are corroborating invariants of the identified complex, not the basis of the originality decision. No equivalent trace classification was found in the inspected sources.

## value

PASS

This is a natural complete classification for the ordinary point-incidence family of a symplectic polar space, over every finite field and rank. It identifies which finite membership observations can vary independently, not only the largest size, and distinguishes the resulting pure complex from matroid and clique models. Exact VC and online dimensions give its learning parameters. The small mod-two examples make the complex concrete but are not independently needed to establish value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
