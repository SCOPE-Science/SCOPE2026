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

# Reproduction and scientific boundaries

Run `python3 verify_y3.py` with a standard Python 3 interpreter. It has no third-party dependencies. The expected output is embedded as `verification_output.txt`.

The primary graph implementation constructs ordered distributions of three distinct labels along each arm, either with or without a center-occupying label. It constructs one oriented edge for each possible movement of a label between the center and the innermost location of a selected arm. Exhaustive group enumeration over all \(S_m\times S_3\) elements checks the fixed-cell character for \(m=3,4,5,6\), with vertex/edge counts and connectivity independently checked. A second, geometrically distinct cubical discretization of the three-arm case, with each arm subdivided into two, three, and four unit edges, checks all nine conjugacy-class traces using signed fixed cubes.

These are exact finite calculations for the stated ranges. They do not constitute a proof for unbounded \(m\). The general proof is the signed-cellular (in this case, orientation-preserving graph-cellular) fixed-point argument in RESULT.md. The result does not determine integral group-lattice isomorphism classes or higher-particle spaces.
