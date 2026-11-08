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
# Reproducibility and scope

Run `python3 artifacts/verify.py` with Python 3.9 or newer. The verifier constructs each rook graph metric directly by row and column equality, enumerates forbidden geodesic triples and computes both minimax scores by exhaustive recursive search with memoization. It tests every first move and every same-row second reply, without using the proof's star-forest reduction to decide legality.

The verified finite output for \(n=3,4,5,6,7,8\) was:

```text
GRAPH_OK n=3 forbidden_triples=36 B=4 Bprime=3 solved_states=206 legality_states=103
GRAPH_OK n=4 forbidden_triples=72 B=4 Bprime=5 solved_states=712 legality_states=356
GRAPH_OK n=5 forbidden_triples=120 B=6 Bprime=5 solved_states=2538 legality_states=1269
GRAPH_OK n=6 forbidden_triples=180 B=6 Bprime=7 solved_states=9356 legality_states=4678
GRAPH_OK n=7 forbidden_triples=252 B=8 Bprime=7 solved_states=35470 legality_states=17735
GRAPH_OK n=8 forbidden_triples=336 B=8 Bprime=9 solved_states=137232 legality_states=68616
VERIFY_OK graph_orders=3..8 independent_distance_triples=PASS adversarial_minimax=PASS same_row_best_reply=PASS solved_states=185514
```

This is a finite test only; it neither proves the unrestricted theorem nor constitutes independent validation. The proof in `RESULT.md` supplies the parameter-uniform strategy arguments and terminal-state classification.
