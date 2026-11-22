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

# Exact finite checks and limitations

The source `verify_fast.cpp` independently constructs all 14 cyclic-rotation orbits, enumerates one deleted word from each, uses Kahn's topological sort and computes maximal vertex-count paths in the survivor DAG. It prints 14 exact length/frequency pairs. Compile with `g++ -std=c++17 -O3 verify_fast.cpp -o check_fast` and run `./check_fast`.

`verify_independent.py` separately enumerates the same mathematical domain by a differently ordered recursion, checks cycles by tri-color DFS rather than Kahn's algorithm, computes path lengths recursively, and groups all 408 optimum sets under bitwise complementation and reversal. Run `python3 verify_independent.py`. Python standard library only.

The independent executions returned the same complete length distribution and 68,288 valid minimum sets, with 408 global length-13 minimizers. The second script gave 101 size-four orbits and two size-two orbits, exhausting all 408 objects. Their source code and `SPECTRUM.tsv` are embedded in this package, with byte counts and SHA-256 checksums in the containing manifest.

The proof is a finite exhaustive classification of all size-14 transversals; it does not claim generality for other word lengths or alphabet sizes. A published total of 68,288 and sharp endpoint range 13–26 independently corroborate the run but do not replace the internal exhaustive proof. External independent mathematical audit has not been performed.
