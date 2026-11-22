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

# Reproducibility of sparse Hamilton-tour Fourier zeros

The numerical checks use integer operations only. Execute from this package directory:

```sh
python3 verify_signatures.py
c++ -std=c++17 -O2 verify_tours.cpp -o verify_tours
./verify_tours
```

The first checker enumerates all degree-zero-through-four edge sets of \(K_8\), constructs exact path-forest completion weights for each, asserts that precisely 17 signature types occur, and evaluates each at every integer order from six through seventeen. It reports zero only for the four-edge signature \((4,9,6,0)\) at nine vertices and the three-edge signature \((3,3,0,0)\) at ten vertices. It verifies the labelled multiplicities \(6300\) and \(960\). The second checker fixes a starting vertex, enumerates Hamiltonian-cycle permutations modulo reversal, and independently computes six exact signed cycle sums at both nine and ten vertices, including the exceptional triangle/star examples and nonvanishing controls. Both reproduced their expected assertions on the embedded source files.

The theorem beyond order seventeen follows from the symbolic union bound, not from finite test extrapolation. These tests do not address spectral behavior for supports of size five or more and do not establish historical uniqueness. An independent mathematical audit has not been performed.
