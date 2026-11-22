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

# Verification of the one-edge higher-independence theorem

The accompanying `verify.py` is executable with Python 3 and standard-library modules alone. From its package directory, run `python3 verify.py`. Its unchanged corresponding execution output is embedded as `verify_output.txt`.

The program builds the graph directly from each tuple of part sizes and deletes the specified edge. A graph-component traversal determines directly allowed subsets, rather than employing the theorem's explicit face description. It verifies equality with the proposed collection of new faces, performs every elementary face–coface collapse checking that the face has exactly one surviving proper coface, and calculates all reduced mod-two homology ranks by binary Gaussian elimination. It also checks both algebraically equivalent binomial formulas.

The output records 1,111 tested tuples/thresholds; 224,180 total examined faces; and 1,177 checked elementary collapses. The check covers all ordered tuples with two, three, or four parts, each size one to four, total order at most nine, and all thresholds from two through the number of vertices. No sampled finite range exhausts all graph sizes. Exact integral ranks and split-surjectivity are proved by the argument in `RESULT.md`, not by a mod-two calculation. No independent audit has been conducted.
