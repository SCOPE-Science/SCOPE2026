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

# Exact computational verification and limits

The complete certificate comprises the published-source mathematical reduction, plus an exhaustive group calculation; neither finite-field sampling nor a timeout argument is used to infer an infinite theorem.

To replay in a working directory containing all five attached data/code files:

```sh
python3 make_markings.py
c++ -O2 -std=c++17 census.cpp -o census
./census > census.out
python3 verify_witness.py
```

The generator produces and verifies the complete standard \(56\)-exceptional-curve model, all \(576\) unordered disjoint seven-curve sets, the seven reflections, and \(288\) fixed-point-free Geiser pairs. The C++ program exhaustively enumerates all \(2{,}903{,}040\) elements of \(W(E_7)\), exhaustively partitions them into \(60\) conjugacy classes by simple-generator conjugation, and tests all \(576\) contraction sets for each class representative. The sums by minimum cycle length are contained at the end of `census.out`. The witness checker reconstructs the degree-eighteen representative and independently verifies its cycle profiles \(2^1 18^3\), \(18^{32}\), and \(9^{32}\) on the respective \(56\), \(576\), and \(288\) objects.

In a fresh working-directory replay, compilation and full enumeration succeeded; the generated `census.out` was byte-identical to the bundled census, and the witness verifier passed all assertions. A separate direct enumeration by individual group elements also agreed with the nine orbit-minimum totals. The mathematical passage from finite group action to finite-field surfaces uses Theorem 1.2 of Loughran–Trepalin; its independent correctness is not re-proved here. Explicit surfaces in the extremal class are not constructed in the package. No characteristic-two or small-odd-field sharpness assertion is certified.
