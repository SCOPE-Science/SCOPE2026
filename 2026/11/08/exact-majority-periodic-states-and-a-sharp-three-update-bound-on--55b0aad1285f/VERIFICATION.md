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

# Reproducibility and actual checks

The mathematical proof in `RESULT.md` supplies all-parameter correctness; numerical experiments are independent consistency checks, not a replacement for the proof. From the package root run:

```
python3 code/direct_enumeration.py
python3 code/weighted_profiles.py
```

`code/direct_enumeration.py` builds actual graph neighbor lists, then exhausts every labelled configuration for 36 parameter pairs (15,876 configurations). It independently counts fixed states and primitive two-cycles by applying the open-neighbor majority rule, and verifies an entrance time of at most three for every state. It verifies sharpness where the finite parameter domain includes the strict parity subfamily. The captured stdout is `evidence/direct_enumeration.txt`.

`code/weighted_profiles.py` uses an algebraically separate clique/independent-set update formula and the orbit weights \(\binom ck\binom sj\). It checks the exact periodic-state formula for all 900 parameter pairs with \(1\le c,s\le30\), traversing 245,025 population profiles, and independently tests 2,304 explicit three-step witnesses for larger clique and independent-set sizes. The captured stdout is `evidence/weighted_profiles.txt`.

The programs do not certify historical originality. Boundary cases \(c=1\), \(s=1\), parity equality, and the dominance transition \(c=s\) are included. No claim about unrestricted split graphs or finite enumeration proving arbitrary parameters is made.
