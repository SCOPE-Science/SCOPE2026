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

# Reproducibility and validation

Run `python3 CHECK.py` with Python 3, no third-party dependencies. The program constructs both finite maps entirely with integers. Exact tie-to-even rounding, the graph traversal, and all accepted counts appear in the code. It verifies all 15,361 inputs for each evaluation and explicitly checks that the staged alternative parenthesization remains identical on this domain. It reports three cycles for each map and their complete basin sizes, periods, and transient maxima; the final output is:

`VERIFY_OK exact_integer_full_graphs=2 states_each=15361 edge_comparisons=15361`

Optionally run `python3 VERIFY_NUMPY.py` with NumPy installed. It independently constructs the 30,722 successors and verifies exact bit-level equality to the integer certificate:

`NUMPY_OK bitwise_transition_match=30722 binary16_double_independent=1`

The binary64 polynomial check is exact on binary16 inputs: each scaled argument is an integer multiple of \(2^{-24}\), the polynomial numerator is bounded by 50 binary digits, and IEEE binary64 has 53 significand bits. The cross-check therefore does not rely on approximate higher-precision output near ties. Both commands were executed and their verified output markers are reproduced above.

The proof is **finite exhaustive**: the source domain has exactly 15,361 states and each state is represented and visited. The checker does not establish any uncountable-domain, high-precision, or device-specific result. Independent scientific audit has not been performed.
