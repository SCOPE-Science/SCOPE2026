---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The minimum identifying-code state space is precisely the 584 size-eight sets on the explicitly labeled GP(8,3), determined by all nonempty closed-neighborhood signatures and all 120 pairwise signature differences. An independent fresh checker tested all 65,536 masks, recovered exactly 584 size-eight feasible masks, then independently generated all single-vertex exchanges and distinguished host-adjacent slides from unrestricted jumps. It reproduced 864 slide edges, one 488-state component and 96 singletons, slide diameter 10, and degrees 0:96,2:240,4:168,6:48,8:30,24:2. It also reproduced 2496 jump edges, a connected graph of diameter 8 and radius 7, jump degrees 4:96,6:48,8:48,9:192,10:144,12:48,24:8; frozen host-edge classes 5:48 and 7:48. Exhaustive code and move rules prove finite completeness.

## originality

PASS

PASS qualified: the prior Möbius–Kantor code census gives the already-known minimum 8 and 584 optimum codes with 13 automorphism orbits, while the general token-slide reconfiguration results explain the framework but not the host-specific transition graph. No searched prior source established the 96 frozen/488 mobile partition, exact radii/diameters, both degree sequences and jump-slide gap for the specific identifying-code invariant.

## value

PASS

PASS: identifying-code reconfiguration is a motivated graph-theoretic robustness/relocation question, and the complete optimum-state graph of the canonical 16-vertex cubic symmetric Möbius–Kantor graph is a naturally bounded exact invariant. The contrast between connected unrestricted jumps and 96 frozen adjacent slides, with sharp distance data, is independently useful even without a larger graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
