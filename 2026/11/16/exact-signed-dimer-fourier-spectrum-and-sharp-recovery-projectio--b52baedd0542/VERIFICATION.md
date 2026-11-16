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

# Exact arithmetic verification

`verify_walsh.py` enumerates all perfect matchings of the 16-vertex hypercube recursively, derives a canonical 15-edge spanning-tree gauge, constructs the 17-bit matching indicator and applies two full Walsh--Hadamard transforms to obtain the multiplier histogram and projection-kernel norm. It exhaustively tests all singleton and two-edge frequencies. `verify_permanent.cpp` instead computes every signed partition function as an exact 8-by-8 permanent by subset dynamic programming; after constructing the same canonical gauge from the graph, it independently computes the support transform and histogram. The two implementations agree on every asserted shared scalar and histogram entry.

Execution in the final package:

```sh
python3 verify_walsh.py > walsh_result.json
c++ -O2 -std=c++17 verify_permanent.cpp -o verify_permanent
./verify_permanent > permanent_result.json
python3 - <<'PY'
import json
w=json.load(open('walsh_result.json'))
p=json.load(open('permanent_result.json'))
assert all(w[k] == v for k,v in p.items())
print('Exact two-method verification: PASS')
PY
```

The supplied `verification_results.json` records the evaluated exact integer reference values, including the full 15-level absolute histogram. The calculations exhaust 131,072 reduced Fourier characters, which represent all \(2^{32}\) full characters by the proved 15-dimensional gauge quotient. The use of a spanning tree is exact and its basis does not alter the zero spectrum, norm or histogram. No probabilistic approximations, timeout-based impossibility claims, or external computational certifications are used.

The verification establishes the explicitly finite theorem. It does not prove any formula for higher-dimensional cubes, rule out unindexed prior literature, or substitute for independent external audit.
