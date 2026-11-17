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

# Exact finite certificate and independent mathematical limits

Run `python verify_ladder.py` with Python 3 and NumPy available. The code enumerates all connected equality partitions by directed-edge subsets of the two-row grid, filters those whose directed quotient fails topological sorting, tests all \(2^{2k}-2\) binary cuts for each feasible partition, and compares rational upper bounds by signed 64-bit **integer cross products** with means scaled by \(\operatorname{lcm}(1,\dots,2k)\). No floating-point optimization or random data is used.

Expected passing results: \(k=2\): 10 faces and 140 cut comparisons, sharp \(1\); \(k=3\): 52 and 3224, sharp \(4/3\); \(k=4\): 272 and 69088, sharp \(3/2\); \(k=5\): 1424 and 1455328, sharp \(19/10\); \(k=6\): 7456 and 30524864, sharp \(9/4\). The script emits an attaining partition and cut mask at every width and checks the explicit top-row-pooling lower witness at ten further sizes. All checks returned `ALL_EXACT_LADDER_ISOTONIC_VARIATION_CERTIFICATES_PASS` when replayed from the actual bundled script.

The *proof of exhaustive coverage* (not the checker runtime) rests on all active equalities defining connected components, feasibility of a partition exactly when the contracted directed cover graph is acyclic, and the full-dimensional local realization by strictly positive active KKT multipliers. The coarea formula reduces every real vector to a positive integral of binary cuts for linear block averaging. These analytical facts are detailed in `RESULT.md`.

The width-asymptotic bound has an independent analytical proof and is not extrapolated from the finite table: whole-row pooling yields \(C_k\ge1/2+\lfloor k^2/4\rfloor/k\), and coordinatewise isotonicity plus \(3k-2\) graph edges yields \(C_k\le3k-2\). No equality formula for \(k\ge7\), sharp leading asymptotic constant, weighted variant or independent audit is asserted.
