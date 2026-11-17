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

# Verification

For the exact graph and rule specified in `RESULT.md`, execute:

```sh
g++ -O3 -std=c++17 census.cpp -o census
./census > check_census.out
diff -u census.out check_census.out

g++ -O3 -std=c++17 independent.cpp -o independent
./independent > check_independent.out
diff -u independent.out check_independent.out
diff -u check_census.out check_independent.out

g++ -O3 -std=c++17 census_with_reps.cpp -o census_with_reps
./census_with_reps > check_reps.out
diff -u census_with_reps.out check_reps.out
python3 symmetry_check.py

g++ -O3 -std=c++17 phase_coloring.cpp -o phase_coloring
./phase_coloring
```

The symmetry script reads the packaged `census_with_reps.out`. The two all-state algorithms independently produced identical 21 joint classes, covering 16,777,216 states, with primitive periods only 1 and 4. They give 29,602 four-cycles, max first-entry time 12 and 48 equality cases. Separate direct coloring enumeration confirms 118,408 rotating periodic configurations. Exhaustive adjacency-preserving permutation search finds eight graph automorphisms and partitions the 48 extremizers into six orbits of size eight.

This is a finite computational certificate accompanied by source code and exact captured outputs; the recurrence classification and its mathematical interpretation are explained in `RESULT.md`. The independent external mathematical audit has not been performed. There are no claims about a larger graph family or infinitely many systems.
