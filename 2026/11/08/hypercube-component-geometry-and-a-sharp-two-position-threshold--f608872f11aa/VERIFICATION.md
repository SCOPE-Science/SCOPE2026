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

# Reproducible verification

Run the Python 3 script directly:

```sh
python3 verify_structure.py
```

It enumerates all derangements for orders three through eight, reconstructs signature fibers and all distance-one edges, verifies each fiber is connected, checks the isolated states and full quotient adjacency, and checks each possible constructive coordinate crossing for orders four through fourteen. It also runs shortest-path search from a specified order-six witness, confirming restricted adjacent-swap distance seven compared with unrestricted Kendall distance five. The expected final line is `PYTHON_INDEPENDENT_PASS`.

Compile and run the independent C++17 implementation:

```sh
g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify_components.cpp -o verify_components
./verify_components
```

This separately enumerates all derangements for orders three through nine, constructs legal swaps by direct position pairs, uses disjoint-set unions to verify adjacent-swap components and distance-two connectivity, and verifies the actual quotient adjacency matrix against Hamming distance one. At order nine it reports `states=133496 fibers=128 qedges=448`; the expected final line is `CPP_EXHAUSTIVE_PASS`.

Both programs were executed successfully. The Python procedure checks all coordinate patterns through order fourteen; the C++ procedure exhaustively checks graphs through order nine. Neither finite check is used to establish the universal quantifier; that conclusion is supplied by the proof in `RESULT.md`. This work has received self-review but no independent scholarly audit.
