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

# Reproducibility and proof boundary

Run `python3 verify_modal_word_monoid.py` with Python 3 and no third-party dependencies. The script evaluates necessity and possibility from the adjacency matrix of the nonempty-subset intersection relation, independently computes the closed-form functions, and checks every event for \(n=1,2,3,4\).

For the four-atom case it checks all \(2^{15}=32768\) events; the count of nine distinct operations is corroborated for two, three, and four atoms. It verifies the complete left-prefix transition table, all paired-observation fibers, the \(2^{n+1}-1\) spectrum count, and the inclusion-exclusion values. The printed verification totals are:

```
{'n': 1, 'events': 2, 'distinct_words': 1, 'joint_profiles': 2, 'cover_count': 1, 'unprotected_full_support': 0}
{'n': 2, 'events': 8, 'distinct_words': 9, 'joint_profiles': 7, 'cover_count': 5, 'unprotected_full_support': 2}
{'n': 3, 'events': 128, 'distinct_words': 9, 'joint_profiles': 15, 'cover_count': 109, 'unprotected_full_support': 90}
{'n': 4, 'events': 32768, 'distinct_words': 9, 'joint_profiles': 31, 'cover_count': 32297, 'unprotected_full_support': 31826}
PASS: exhaustive event cases, nine normal forms, profile fibers, and prefix table
```

The unrestricted parameter \(n\ge2\) is proved symbolically through the support identities, transition table, two-atom separation plus bounded morphisms, and inclusion-exclusion. Finite checking is not presented as proof of the infinite family. Literature non-detection is not proof of priority. An independent audit has not been performed.
