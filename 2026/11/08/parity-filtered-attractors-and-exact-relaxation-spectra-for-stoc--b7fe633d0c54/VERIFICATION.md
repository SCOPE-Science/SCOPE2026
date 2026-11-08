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

Two verification programs accompany the result. Both were executed using Python 3; `verification/class_scc.py` additionally requires the third-party `networkx` package. Run each script from any directory with its ordinary Python entry point; no input data files are necessary. Their captured stdout is in correspondingly named `_output.txt` files.

The first script constructs the actual Markov transition digraph and computes closed strongly connected components for every nonempty marked subset of every labelled cycle of size 3 through 7. This covers 243 graph instances and 335,632 initial binary states across those instances. The observed class-size multisets agree with the formula in all cases.

The second script implements a separate local-flip simulator; it constructs candidate classes from arc-particle positions, verifies all outgoing transitions stay inside the class, and checks each proposed class is connected by legal moves. It also directly checks the reflecting-path Laplacian cosine eigenvectors through path length 20. Its finite sample covers 32 graph instances through cycle length 9.

These programs are finite checks, not a substitute for the all-size proof. They do not estimate hitting probabilities or absorption times, and no independent audit has been performed.
