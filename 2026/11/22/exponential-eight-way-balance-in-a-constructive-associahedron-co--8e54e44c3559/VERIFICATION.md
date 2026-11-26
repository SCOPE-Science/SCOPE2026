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

The map agrees with Wood, including counting preferred left edges by the parent's even depth from the top of its preferred path. Both one-argument restrictions of Q are invertible affine maps, so varying a replacement label permutes the full root labels. Independent evaluation of the four five-leaf label witnesses gives 00, 01, 10, 11 in order. Independent evaluation of the two parity witnesses gives the same label 00 and parity pairs (0,0) and (1,1); the two incoming-depth cases are essential. Replacements preserve the first preorder occurrence (other equal-size occurrences are disjoint) and label-preserving replacements leave the preferred-path data outside unchanged. The four-element label orbits and parity involution therefore cancel the corresponding contributions exactly. With j forbidden patterns of size five the root recurrence subtracts exactly j z^5; coefficients are nonnegative, and nesting avoidance shows a_4(n) <= a_2(n). At r=0.251 the discriminants are 0.003970005010008 and 0.011940010020016 and decrease on [0,r]. The formal branch continues analytically through that interval, so Pringsheim's theorem is sufficient for the claimed evaluation and coefficient bound. Catalan asymptotics give the relative error. The supplied colour enumeration through n=10 is corroboration, inspected but not rerun; the exact witnesses and analytic argument do not rely on that enumeration.

## originality

PASS

The credited original result is the quantitative class distribution of Wood's actual fixed map with all leaf labels zero, not the map or the proper eight-colouring theorem. The inspected alternatives do not cover both label and parity frequencies for that map.

## value

PASS

It quantifies how the classes in an explicit proper colouring of a natural graph are actually used. It proves eventual presence of all eight colours and controls finite-size imbalance, neither of which follows from an eight-colour upper bound. The depth-robust parity switch is a useful part of the explanation rather than a numerical observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
