---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

On the smooth rational elliptic model, Shioda–Tate gives rank zero and the discriminant/index of the trivial lattice in the unimodular Néron–Severi lattice gives order three. The explicit nonzero flex confirms the torsion, and the height equation c(9−c)/9=2+2(P·O) forces c=3 or 6 and P·O=0; inversion gives the other component. The sections are pairwise disjoint. Nefness of the fiber and adjunction with K=−F force every negative irreducible curve to be a reducible-fiber component or a section, exhausting the graph. After taking the negative intersection form and eliminating each selected section, only marked cycle vertices have diagonal lowered to one. A proper cycle subset breaks into paths: unmarked paths and paths with one endpoint mark are positive definite; an internal mark contains the singular marked star, and two endpoint marks contain the singular arc with both sections. The full fiber is already singular. The ten sets form an antichain, so the obstructions are exactly the minimal ones. Independent exact inclusion–exclusion over their union sizes (python3 /workspace/independent_checks/chambers.py) gave coefficients 1,12,66,220,492,768,837,612,270,48 with all higher coefficients zero and sum 3326. The established chamber correspondence adds precisely one nef chamber.

## originality

PASS

The established surface classification and the general chamber-counting algorithm are not original here. The supported distinct result is the ten minimal singular configurations and the evaluated size distribution for X_9111. Inspected same-date studies treat related but different surfaces; the exact indexed hit is this very record. No inspected distinct source covered this explicit classification.

## value

PASS

This surface is the classical extremal rational elliptic surface with the nine-gon fiber, not an arbitrary graph slice. The ten exclusions characterize individual supports without a matrix test for each subset. The size-refined count then measures the negative-part strata, including 48 largest supports; the structural characterization is useful separately from the evaluated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
