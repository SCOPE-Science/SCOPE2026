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

# Reproduction and finite proof checks

Use Python 3 standard library, without third-party dependencies:

```
python3 verify_chvatal.py
```

The checker hardcodes the complete labelled edge set and tests triangle-freeness and four-chromaticity, then constructs all 52 distinct vertex-covering perfect-matchings by a first-unmatched-vertex recursion. It independently derives all 8192 signed counts by direct fast Walsh transform of projected incidence vectors and by a signed dynamic-programming recurrence over unmatched vertex masks. The methods agree coefficient by coefficient. The full absolute multiplicity distribution, twelve 12-incidence edges, twelve 14-incidence edges, 48 mixed-type adjacent cancellation pairs, absence of one-edge zeros, and exhaustive two-edge classification are verified with exact integers. A second exact Walsh transform of the 0–1 support indicator verifies the projection-kernel numerator 162144 and denominator 8192, reducing to 5067/256. All 8192 reduced signings represent the complete 24-coordinate frequency cube by the proved vertex-star switching symmetry.

Expected terminal record:

```
PASS: matching count, two independent signed spectra, low-degree cancellation, projection norm
spectrum [(0, 2536), (4, 2864), (8, 1708), (12, 574), (16, 304), (20, 120), (24, 52), (28, 24), (32, 8), (52, 2)]
projection 5067/256 full rank 11583488 nullity 5193728
```

The checker proves finite exact statements when its enumeration is complete and its displayed recurrences hold; it is not an infinite graph-family proof. The unrestricted projection minimum also requires the translation-averaging argument in the paper, not merely these integer calculations. Originality is bounded by the inspected literature, and no independent external validation is asserted.
