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
# Verification procedures and boundaries

The saved `census_output.txt` and `walk_output.txt` are produced by two different complete-state algorithms. The 7 cycle totals and 48 nonzero entry-time/period populations agree exactly after the alternative program's nonessential example field is omitted. Both total \(43,046,721\) labelled states. The maximum observed entry time is eleven and no state is left unclassified.

The `clebsch_walk.c` executable also writes `period13_reps.txt` and `period16_reps.txt`; these contain exactly 9,600 and 2,400 distinct minimal base-three encodings of temporal orbits. `clebsch_symmetry.py` constructs the whole 1,920-element automorphism group, verifies edge preservation, and computes the orbit sizes on those lists. `clebsch_stabilizers.py` enumerates stabilizer elements of representative cycles and `clebsch_phase.py` checks uniform excitation counts over all cycles of both lengths. Outputs are included, and replay from the supplied source paths was performed.

To replay, from the containing directory:

```
cc -std=c11 -O3 -Wall -Wextra -o clebsch_census clebsch_census.c
cc -std=c11 -O3 -Wall -Wextra -o clebsch_walk clebsch_walk.c
./clebsch_census > census_output.txt
./clebsch_walk > walk_output.txt
python3 clebsch_symmetry.py > symmetry_output.txt
python3 clebsch_phase.py > phase_output.txt
python3 clebsch_stabilizers.py > stabilizer_output.txt
```

The exact finite-census proof rests on executable source and exhaustive integer counting, not on statistical testing. Software defects, alternative graph-name conventions, and historical priority are residual risks. No outside independent or formal audit is claimed.
