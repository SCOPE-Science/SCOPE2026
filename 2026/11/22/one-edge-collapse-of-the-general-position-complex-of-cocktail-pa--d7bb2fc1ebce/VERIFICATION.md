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

# Verification record

The `check.py` file is a standalone Python 3.9+ script requiring no third-party packages. Run `python3 check.py` in a directory containing the script and compare standard output against `expected-output.txt`.

For every integer \(3\leq n\leq8\), the program independently builds the edge-deleted cocktail-party graph, recomputes the shortest-path metric by breadth-first search from every vertex, tests all \(2^{2n}\) potential faces by inspecting all triples, and checks every face against the closed structural description used in the proof. It checks the exact face polynomial and mod-two boundary ranks in every dimension. The output reproduced the supplied reference output on execution.

The finite checks do not establish the infinite theorem. The general proof is the complete graph-distance characterization, two free-face collapses, and a CW homotopy quotient of a contractible join with \(n-1\) attached edges. These steps yield the full integral homotopy type. No separate independent mathematical audit or formal proof assistant certification has been performed.
