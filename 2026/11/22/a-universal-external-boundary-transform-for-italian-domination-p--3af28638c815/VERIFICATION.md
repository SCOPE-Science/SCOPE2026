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

# Verification of the universal Italian-corona transform

## Proof-level checks
The partition by positive core support \(P\) is unique. The five valid states at a positive core are \((1,1),(1,2),(2,0),(2,1),(2,2)\), producing \(z^2(2+2z+z^2)\). A zero core with a positive base neighbor allows leaf labels one and two, producing \(z(1+z)\); a zero core without a positive base neighbor forces leaf label two, producing \(z^2\). This is necessary and sufficient locally, with no interactions after \(P\) is fixed. Their product over the three disjoint core classes is the claimed polynomial summand.

For the minimum-weight consequence, the set \(P\cup(V\setminus(P\cup B_G(P)))\) dominates the base and has \(n-b_G(P)\) vertices, showing \(b_G(P)\le n-\gamma(G)\). A minimum dominating set attains equality. Every maximizing subset contributes exactly \(2^{|P|}\) to the leading coefficient. The scalar part was proved by earlier literature, not newly discovered here.

## Independent code paths
The file `verify.py` uses standard-library `itertools.product` to enumerate valid Italian labels directly and a separate subset convolution to compute the claimed formula. It checks every labeled simple graph with one through four base vertices, plus four distinct five-vertex graph families. It also checks \(\gamma(G)\) and the explicit minimum multiplicity. It reports `VERIFY_OK`.

The file `verify_all_small.cpp` is an independent C++17 implementation: it enumerates all \(3^{2n}\) full root/leaf labelings for each of all 1,099 labeled simple base graphs with \(1\le n\le5\), compares 22,719 exact coefficient positions with the boundary transform, and separately checks minimum weight and minimum coefficient. Its final report is `VERIFY_OK graphs=1099 coefficient_comparisons=22719`.

Reproduction commands from the package directory:

```sh
python3 verify.py
c++ -O3 -std=c++17 verify_all_small.cpp -o verify_all_small
./verify_all_small
```

## Scope and limits
All numerical comparisons are finite tests rather than all-order proof or historical priority evidence. The proof covers every finite simple graph with one leaf per base vertex. The unrestricted enumeration is potentially exponential in the base order; the code does not assert a polynomial-time algorithm. There has not been an independent mathematical audit.
