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

The proof is the exact face-poset decomposition, acyclic matching, and relative chain calculation in `RESULT.md`. The mathematical claims are for all \(k\ge3\), not merely the tested cases.

`verify.py` is standalone Python 3. Running `python3 verify.py` enumerates the faces directly from induced-component sizes for the parameter range \(2\le k\le5\) and \(1\le r\le2k+1\). It computes reduced mod-two boundary-matrix ranks; it independently builds the link and all directed matching Hasse edges and verifies a topological ordering; and it calculates signed simplicial Lefschetz numbers for every arm permutation. The recorded output is in `verify_output.txt`.

The finite checks cannot establish an infinite-family theorem or rule out hidden integral torsion. Those properties are established by the symbolic integral chain decomposition, direct-sum splitting of the augmentation map, and acyclic-matching proof, respectively. No independent audit or external certificate is claimed.
