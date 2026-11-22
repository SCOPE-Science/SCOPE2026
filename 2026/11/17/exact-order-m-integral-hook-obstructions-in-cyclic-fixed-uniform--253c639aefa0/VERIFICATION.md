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

PASS: geometric fixed barycentric coordinates on each p-cycle must be constant. Original support condition p*(number of nonzero heavy orbit coordinates)+indicator(apex)>0<=kp gives exactly an S_m-equivariant PL (k-1)-skeleton on vertices 0,1,...,m. Contractible S_m-stable closed star of apex 0 collapses non-equivariantly to C(m,k) oriented heavy k-faces, yielding top homology ∧^k P_m and other reduced groups zero. Augmentation ε:P_m→Z with A=ker ε splits as ordinary abelian lattices; interior contraction gives 0→∧^k A→∧^k P→∧^(k-1)A→0 S_m-equivariantly. Invariant v=sum e_i, ε(v)=m, lifts m times identity via v∧- and kills Ext class. Over Q, the adjacent exterior hook modules ∧^k A_Q and ∧^(k-1) A_Q are inequivalent irreducibles for 2<=k<=m-2, so Hom=0 and rational lift of q identity unique: (q/m)v∧-. On primitive z=(e1-em)∧...∧(e[k-1]-em), its coefficient on e1∧...∧ek equals ±q/m, integral only when m divides q. Thus exact order m and nonsplitting for all parameters, not just finite checked cases; Ext torsion is not homology torsion. Checked source verify.py only corroborates finite orbit faces, signed characters; it cannot by itself prove Ext.

## originality

PASS

PASS with bounded priority risk: known simplex-skeleton wedge and apex-induced exact sequence are explicitly credited; prior all-n universal-apex theorem establishes an extremal cyclic norm extension of order m, not the exact full S_m order for every interior k. The current uniform sharpness argument across all degrees, with specific geometric fixed-space realization, is not obtained by merely substituting extremal k into the prior result. Standard hook irreducibility and integral Ext background acknowledged.

## value

PASS

PASS: the precise additive order in an integral equivariant extension is a natural obstruction to lifting the known rational hook decomposition; its uniform sharp value across every interior degree answers the exact intrinsic integrality question for a canonical permutation lattice. This is independently meaningful even though skeleton homotopy and the natural exact sequence are known; it is not a tiny unmotivated numeral or an arbitrary example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
