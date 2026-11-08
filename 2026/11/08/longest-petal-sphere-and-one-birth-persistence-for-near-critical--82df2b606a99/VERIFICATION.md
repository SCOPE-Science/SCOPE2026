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
# Reproducibility and verification

Run `python3 verify.py` in a directory containing that file; it uses only the Python standard library. The file `verification_output.txt` records the actual output of the included implementation. The terminal line is `ALL_VERIFY_OK`.

The verifier constructs every ordered petal-length tuple for \(2\le k\le5\) with \(3\le L_i\le7\), including repeated lengths. It explicitly simulates synchronous firing until the first repeated full chip configuration; verifies return to the initial state, the exact period, and the fully predicted collection of firing sets; confirms the total initial chip count is one below the arc count; exhaustively enumerates every proper intersection of the firing-set cover; checks the early common intersection at every prefix; and verifies that one extra hub chip yields the full vertex set at the first step. There are 3900 length tuples and 25516 verified firing steps.

As an independent chain-level spot check, the verifier enumerates the simplices of six sample complexes and reduces their simplicial boundary operators over \(\mathbb F_2\). Each has one nonzero reduced Betti number, equal to one in the predicted dimension. No claims about integral torsion or universal parameters are inferred from these finite-field computations: integrality and universality follow from the explicit nerve homotopy equivalence in RESULT.md.

The preprint's source convention excludes sinks from firing sets; the directed rose has none. The initial hub has \(k-1<k\) chips and is stable at time zero. The first nonzero reduced class is born at the final new facet of the first period and is never killed, since the configuration thereafter repeats.

The checks are same-model and computational; independent mathematical audit is not performed.
