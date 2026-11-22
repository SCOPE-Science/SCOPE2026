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

The included `verify.py` enumerates **all** vertex subsets for each of the ten graphs (two per parameter) with \(2\le m\le6\), tests acyclicity by union-find, and independently compares the resulting face sets with the proposed combinatorial description. It also confirms exact boundary equations over \(\mathbb Z\) for the surviving tetrahedral sphere cycles and compares full simplicial reduced Betti numbers over characteristics 2, 3 and 5. `verification_output.txt` is the literal output of that script.

The all-parameter proof instead uses a complete face classification, sphere attachment along trees, primitive graph-cycle attaching maps, and a direct relative homology computation. It does not infer integral torsion-freeness or infinite cases from finite experiments. No test of all possible equivalent publications or independent audit is asserted.
