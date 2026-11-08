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
# Verification and limits

Run `python verify.py` with Python 3 and no external dependencies. The program independently constructs all faces directly from adjacency, compares them to the proposed simplicial cover, computes exact mod-two simplicial boundary ranks, and computes signed Lefschetz numbers by enumerating fixed oriented simplices. Its expected final line is `ALL_VERIFY_OK 5 22`.

Test coverage: 121 small-graph pairs for the two-factor cover identity; five joins of cycles (including length-four contrasts) for mod-two homology; 22 generator traces, including equal-factor swaps. These tests do not verify the infinite-family proof, equivariant homotopy equivalences, or scientific priority. The proof uses finite-cover homotopy pushouts and an integral augmented Čech resolution. Full external review and an exhaustive publication search have not been performed.
