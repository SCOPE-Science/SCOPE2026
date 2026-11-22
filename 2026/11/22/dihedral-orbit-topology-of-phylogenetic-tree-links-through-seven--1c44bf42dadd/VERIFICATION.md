---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 verify_dihedral_tree_links.py` and `python3 verify_tree_burnside.py` using Python 3 and its standard library. The scripts must finish with `DIHEDRAL_PHYLOGENETIC_SPLIT_QUOTIENT_CERTIFICATE_OK` and `BURNSIDE_7_TREE_LINK_EULER_OK`, respectively.

The primary program constructs every nontrivial unordered split as a bitmask with canonical side containing leaf zero. Compatibility is checked by the four-set-intersection criterion. It enumerates every face and nonempty strict chain through seven leaves; it then generates the complete dihedral action and canonically quotients the subdivision chains, preserving dimension order for orientations. It builds exact integer boundary matrices and checks every consecutive composition is identically zero. For five and six leaves, it constructs successive free face–coface collapses, checking that the purported free face is incident to exactly one currently active higher cell. For seven leaves, sparse modular elimination computes all differential ranks over the fields of two and seven elements.

The independent program builds seven-leaf original faces without using the primary quotient enumeration. It computes the signed permutation trace on each original chain space for each element of the fourteen-element dihedral group. The fourteen alternating Lefschetz numbers, whose total is \(-168\), independently give the quotient Euler characteristic \(-12\).

**Observed results:** original faces for seven leaves \((56,490,1260,945)\); orbit cells \((232,1660,3072,1656)\); seven-leaf modular differential ranks \((231,1429,1643)\) over each of \(\mathbb F_2\) and \(\mathbb F_7\); five-leaf four collapses; six-leaf 59 triangle-edge and 36 edge-vertex collapses; Burnside traces \(-119\) at the identity, zero at each nonidentity rotation, and \(-7\) at each reflection.

**Not established by program execution alone:** the global tree-space sphere-wedge theorem, the orbit-space fundamental-group theorem, and the homological Whitehead theorem. These are applied in the paper proof with explicit hypotheses. No result for \(n\ge8\) is claimed. No independent external mathematical review has been performed.
