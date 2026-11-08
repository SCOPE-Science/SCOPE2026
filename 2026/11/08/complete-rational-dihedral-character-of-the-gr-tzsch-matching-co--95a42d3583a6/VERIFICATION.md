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

The standalone `verify.py` is a Python-standard-library script for exactly the eleven-vertex Grötzsch matching complex. Run `python3 verify.py`; its expected output is embedded verbatim in `verification_output.txt`.

It enumerates all matching simplices, verifies the full signed boundary-square identity, and computes the boundary ranks by sparse elimination modulo \(2\), \(3\), and \(101\). The rational-rank proof uses corresponding *upper* bounds from the chain equations; it does not equate a field rank with a rational rank without proof. The code then evaluates oriented simplex traces for every element of the pentagon's dihedral symmetry and checks the proposed character equality.

The computation contains no assumptions about other graphs. It does not establish an integral homology module, equivariant homotopy decomposition or publication priority. Independent audit remains unperformed.
