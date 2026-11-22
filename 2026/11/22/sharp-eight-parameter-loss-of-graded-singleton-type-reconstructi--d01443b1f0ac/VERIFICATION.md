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

# Reproducibility of the finite census

All computations use integer arithmetic. `verify.cpp` requires a C++17 compiler and standard library. Run in a directory containing the package artifacts:

```sh
c++ -O2 -std=c++17 verify.cpp -o verify
./verify
c++ -O2 -std=c++17 independent_count.cpp -o independent_count
./independent_count
python3 check_catalogue.py
python3 spectrum_witness.py
```

The final optional line requires the third-party Python package SymPy; the reconstruction census and collision proof do not depend on it. The four respective expected terminal markers are `VERIFY_OK`, `INDEPENDENT_VERIFY_OK`, `CATALOGUE_VERIFY_OK`, and `SPECTRA_DISTINCT_OK`. Complete exact output is supplied in the four matching output text files.

The first C++ verifier reconstructs every isomorphism orbit of every normalized graph on at most eight points, computes the polynomial on each representative by enumerating all binary extension assignments, and checks all nonsingleton fibers with the sorted coherent-triple incidence degrees. At size eight, the exhaustive range contains exactly \(2^{21}=2{,}097{,}152\) normalized labeled graph encodings, and the number of their two-graph isomorphism orbits is \(243\). The second verifier does not use an isomorphism quotient: it enumerates all normalized encodings and counts \(219\) distinct grade polynomials. The Python certificate checker independently evaluates the polynomial and the incidence degrees of every listed representative directly from its 21-bit integer mask. The spectrum checker computes integer Seidel characteristic polynomials of the three explicit witnesses.

The accompanying `collision_catalogue.json` contains each of the \(21\) nontrivial polynomial fibers, its exact nonzero coefficients, the complete list of selected orbit representative masks, and their distinct sorted incidence-degree sequences. The three triple fibers contain nine different two-graphs, and the 18 double fibers contain 36, for 45 ambiguous structures in all. The remaining 198 eight-point structures are singletons. Distinctness of incidence signatures certifies nonisomorphism within each catalogued fiber, while the explicit complete orbit enumeration certifies that no further fibers were missed.

**Limits.** These finite exhaustive calculations establish only the stated finite boundary. They do not show that the stronger signature is injective for any parameter size above eight. The recorded executions were reproduced from the supplied source in the package preparation environment; no external independent validation or audit is asserted.
