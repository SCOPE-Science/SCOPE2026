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

The unrestricted proof is presented in `RESULT.md` and is mathematical, not computer-assisted certification.

Run `python3 verify_dihedral_permutation.py` in the same directory. The program uses only the Python standard library and constructs all faces directly from ordered words. It checks (i) the complete common-face graph, (ii) each cyclic attachment intersection, (iii) both integer one-cocycle identities and the determinant-one winding pair, and (iv) full ranks of the finite boundary matrices modulo two and, at smaller sizes, modulo three.

The actual run checked all \(n=3,4,5,6,7,8\) over \(\mathbb F_2\), and all \(n=3,4,5,6,7\) over \(\mathbb F_3\). Expected reduced second Betti numbers were \(2,7,14,23,34,47\), with all other reduced Betti numbers zero. For each orientation separately, only reduced first Betti number one was observed. The recorded program output is embedded as `verification_output.txt`.

These bounded checks alone cannot establish arbitrary-dimensional homotopy, simple connectivity, integral torsion-freeness, or bibliographic priority. Those statements require the written proof and separate literature assessment. No independent audit was conducted.
