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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or newer, with no third-party packages required. The checker constructs each labeled graph on one to six vertices, tests for a four-cycle as a subgraph, reconstructs every nonempty closed-neighborhood face and graph clique, and verifies each proposed unique-center elementary collapse by checking that its lower face has precisely one surviving proper coface. It also checks the final face complex and Euler characteristic against the triangle-adjusted circle-rank formula.

The exhaustive run considers 33,867 graphs, 8,597 of which are four-cycle-free. Additional tests check the pairing under every graph automorphism of a five-cycle, two triangles sharing a vertex, and a star with five leaves. The four-cycle counterexample is independently reconstructed as a tetrahedral boundary. The exact execution record is in `verify_output.txt` and ends in `ALL_VERIFY_OK`.

The program checks finite instances only. It does not establish the theorem for arbitrarily large graphs, or independently certify the claimed integral module; these follow from the symbolic unique-center collapse and primitive triangle-edge argument in `RESULT.md`. No independent mathematical audit has occurred.
