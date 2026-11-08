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
# Exact verification

Execute `python3 verify.py` in a directory containing the supplied standalone file. Compare stdout verbatim with `verification_output.txt`; execution must end with `ALL_CHECKS_PASS`.

The checker enumerates all valid cells of the sufficiently subdivided unordered configuration model, verifies independent combinatorial counts and all degree-two and degree-three boundary-square identities, then repeatedly performs only free-face elementary CW collapses. It checks that the surviving complex is closed under all cell boundaries and has no three-cells. A maximal spanning tree in the connected surviving one-skeleton is contracted. Complete unimodular integer elimination checks the Smith invariants (1907 units and one two), rather than inferring torsion from modular Betti numbers. The final Euler characteristic provides a separate numerical consistency check.

The Prue–Scrimshaw stable-equivalence theorem is the mathematical justification connecting this finite model to the continuous configuration space; that external general theorem is a cited premise, not re-proved by the checker. The result is not an independently audited mathematical certification.
