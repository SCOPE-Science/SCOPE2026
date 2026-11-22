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

# Reproduction

The following commands require a C++17 compiler and Python 3 only, and are executed in the directory containing the package files:

```sh
g++ -O3 -std=c++17 enumerate.cpp -o enumerate
./enumerate 5 2
./enumerate 6 2
./enumerate 6 3
./enumerate 7 2
./enumerate 7 3
./enumerate 8 3
./enumerate 9 3
python3 independent.py
python3 verify_witnesses.py
g++ -O3 -std=c++17 emit_best.cpp -o emit_best
./emit_best 9 3 > best_summary.txt 2> regenerated_best_kernels_9.txt
cmp best_kernels_9.txt regenerated_best_kernels_9.txt
python3 verify_orbits.py
```

`independent_results.jsonl` contains the entire seven-profile frequency distributions produced by the independent Python enumeration. The seven recorded Gaussian-binomial totals are respectively 155, 651, 1395, 2667, 11811, 97155, and 788035, with the \(n=9,k=3\) maximum exactly \(63\) occurring in 2304 kernels and no complete covering. The auxiliary program `emit_best.cpp` regenerates `best_kernels_9.txt` from the same exhaustive kernel space, and the 2304 canonical bases in that file provide the candidate set on which `verify_orbits.py` verifies the four \(S_9\) orbit sizes and canonical representatives. `verify_witnesses.py` checks all four full-cover constructions and the 63-pattern example. The C++ program computes quotient coset representatives while the independently written Python program computes full coset unions; this avoids sharing the critical test algorithm.

The finite profile enumeration is complete because every binary \(k\)-plane has exactly one reduced row-echelon basis and all its free bits are explored; the counts equal the Gaussian binomial coefficient. The orbit calculation is complete because adjacent transpositions generate the whole coordinate-permutation group. These finite computations do not assert formulas for larger \(d\), and no independent external mathematical audit is recorded.
