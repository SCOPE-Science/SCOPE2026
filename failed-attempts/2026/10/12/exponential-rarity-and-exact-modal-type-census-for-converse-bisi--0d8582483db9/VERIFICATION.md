---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Equal outward types of siblings yield a two-way bisimulation by matching descendants whose chains of outward types from the sibling roots agree. The shared parent matches itself; equal child-type sets give forth and back. Conversely, following the unique parent distinguishes depths, and at each depth two bisimilar vertices have bisimilar parents. Inductively their parents agree, so distinct sibling types force the two vertices to agree. The root type of a rigid tree is its color and a q-element set of rigid child types; placing the types at fixed positions gives q! choices per internal vertex. This proves the two recurrences, the impossibility at positive height with a<q, and the fixed point at a=q. For the rate, the logarithmic correction Φ is bounded because R_h≥a≥q, so telescoping q^(−h) log R_h gives the absolutely convergent series. For a>q the ratio R_{h+1}/R_h is at least a/q>1; once log R_m>K/(q−1) for K a bound on |Φ|, the recurrence gives C≥q^(−m)(log R_m−K/(q−1))>0. The q^(h−1) disjoint bottom sibling families give probability at most p^{q^(h−1)}, p=(a)_q/a^q<1, so the limiting decay constant is positive. The frozen refinement script and output were inspected; a separate enumeration of binary two-color assignments refined by color and both child and parent class sets, reproducing 16/128 at height 2 and 256/32768 at height 3. These finite checks do not establish the rate.

## originality

FAIL

The main census is covered by Cheng (2006), Theorem 3.2, under the equivalent formulation as distinguishing labelings of rooted trees. The equivalence applies to the whole rigidity condition, not to outward-type equality versus isomorphism on arbitrary colored subtrees. The positioned count, threshold and critical specialization follow directly from that theorem, and the rate follows by bounded-correction iteration of the known exact recurrence plus independent bottom sibling families. The exact rate was not located verbatim; that does not make the central enumeration distinct.

## value

FAIL

The modal interpretation is useful and the formulas are correct, but the positioned enumeration is a free-orbit conversion of a known exact rooted-tree formula. The remaining exponential statement uses elementary log iteration and the independent obstruction already present at the bottom stars. The record neither supplies a new count not mechanically implied by the known one nor identifies a scientific need met by that limited asymptotic corollary beyond the rephrasing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
