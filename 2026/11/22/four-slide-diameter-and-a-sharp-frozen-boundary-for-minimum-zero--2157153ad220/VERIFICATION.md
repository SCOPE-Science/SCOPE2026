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

# Reproducible checks

All required inputs are embedded in this package. The generator `profile_certificate.cpp` enumerates 23,659 canonical length-4/5/6 cyclic gap profiles and writes one shortest-enough path for each of 10,713 eligible ordered-index source–target pairs, with no failures. The included certificate is deterministic and is byte-for-byte reproducible by compilation and execution. The independent Python script `verify_gap_certificate.py` regenerates the entire finite case universe and checks every path using literal ordinary zero forcing rather than the generator's closed-form validity predicate. `verify_small.py` independently constructs the minimum configurations and slide graph for all orders 6 through 18, and computes exact all-pairs shortest distances. `verify_lower_bound.py` checks that the prescribed disjoint optimal pairs cannot be connected in three moves.

## Invocation

```bash
g++ -O3 -std=c++17 profile_certificate.cpp -o profile_certificate
./profile_certificate > gap_certificate_replay.tsv
cmp gap_certificate_replay.tsv gap_certificate.tsv
python3 verify_gap_certificate.py
python3 verify_small.py
python3 verify_lower_bound.py
```

## Expected outcomes

- Generator terminal summary: `profiles=23659 cases=10713 failed=0 max_representative_n=42`.
- Certificate checker: `VALID_CERTIFICATE profiles=23659 eligible_pairs=10713 all_paths_at_most_four=PASS`.
- Direct small-order checker: `ALL_DIRECT_SMALL_ORDER_CHECKS_PASS`.
- Extremal-obstruction checker: `LOWER_BOUND_CERTIFICATE_PASS`.

The unbounded mathematical conclusion uses the cyclic-gap truncation/lifting lemma in `RESULT.md`; the finite case data alone would not establish an infinite statement. This is the full extent of validation performed here; independent scientific audit remains unperformed.
