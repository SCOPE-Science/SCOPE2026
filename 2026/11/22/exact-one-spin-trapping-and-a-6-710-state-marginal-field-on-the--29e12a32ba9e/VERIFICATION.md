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

# Exact finite verification

Run the two standalone scripts in the same directory as this file:

```bash
python3 verify_bruteforce.py
python3 verify_structural.py
```

The first script traverses all \(2^{20}=1,048,576\) binary spin assignments and evaluates exact integer local flip costs at the two critical field values and rational representatives of every open interval. It also independently minimizes the exact energy over the full spin space at each representative. The second script uses no complete energy scan: it builds the pentagonal face dual and enumerates its perfect matchings, and it independently generates (i) all independent subsets, (ii) maximal independent subsets, and (iii) dominating subsets of induced maximum degree one. The resulting certificates establish 125 dual perfect matchings, 250 zero-field exchange minimizers, 295 maximal independent sets and 6710 field-one marginal configurations. The analytic sign analysis proves the classification across continuous field intervals.

Successful exact replay produced:

```text
EXHAUSTIVE_PASS states=1048576
h_over_J= 0 /2 strict= 250 weak= 250 ground= 250
h_over_J= 1 /2 strict= 250 weak= 250 ground= 5
h_over_J= 2 /2 strict= 5 weak= 6710 ground= 5
h_over_J= 4 /2 strict= 295 weak= 295 ground= 5
h_over_J= 6 /2 strict= 0 weak= 5828 ground= 5828
h_over_J= 8 /2 strict= 1 weak= 1 ground= 1
STRUCTURAL_PASS dual_matchings=125 zero_field_ground=250
magnetization_distribution= {-4: 5, 0: 240, 4: 5}
independent_sets= {0: 1, 1: 20, 2: 160, 3: 660, 4: 1510, 5: 1912, 6: 1240, 7: 320, 8: 5}
maximal_independent_sets= {6: 10, 7: 280, 8: 5}
h_equal_1_weak= 6710 h_equal_1_strict= 5
```

These are finite exact enumerations, not dynamic trajectories. The number of weakly stable configurations at a critical field is not the number of absorbing states, because zero-energy flips remain allowed. No independent external validation was performed.
