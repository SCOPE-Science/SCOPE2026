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

# Verification and reproducibility

The files `verify_transfer.py`, `verify_direct.cpp`, and `perron_vector.txt` are complete and standalone within this package. For the symbolic transfer certificate, install SymPy 1.10 or later and run `python verify_transfer.py` with the vector in the same directory. For direct original-state enumeration, compile `g++ -std=c++17 -O3 verify_direct.cpp -o verify_direct` and run `./verify_direct`. Both were run from this package directory. No network access or downloaded data are required for either scientific computation.

`verify_transfer.py` enumerates every possible transition among \(4096\) ordered pairs of sixty-four symbolic vertical-column histories. It builds and decomposes the entire graph, checks the sole cyclic strongly connected component and its complete characteristic factorization using exact integer arithmetic, and directly evaluates all spatially labelled closed-walk counts through circumference twelve. The vector certificate consists of \(184\) positive integers in the canonical increasing-code order of the cyclic component; the program checks every strict Collatz–Wielandt inequality with only integer multiplication. This finite, complete transfer construction establishes the stated counts for all \(n\ge3\).

`verify_direct.cpp` independently enumerates each of the \(3^{3n}\) original three-state configurations for \(n=3,4,5\), computes the actual synchronous Moore update exactly three times, and counts returns. It uses explicit eight-distinct-neighbor masks rather than symbolic history constraints. The expected return counts are \(1,145,181\), respectively. These direct finite checks are corroboration, not the all-size proof. The saved output files are comparison artifacts, not substitutes for executing the computations.

The factorization and the strict spectral bounds are finite computer-assisted certificates reproducible from the included files; they are not a proof about all temporal periods, attraction basins, or historical uniqueness. Independent external auditing has not been performed.
