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

# Verification of the radius-two Boolean-ball theorem

Run `python3 verify.py` using Python 3.10 or later. No third-party packages or network access are required. The checker uses exact integers and exact Hamming distances.

The critical universal step is the exhaustive template certificate: 31 distinct nonzero five-row masks, at most two instances of each, and five row-degree upper bounds of two. All allowed assignments are enumerated. A valid template is tested against all center active-coordinate masks of weight at most four and auxiliary zero-coordinate weights from zero to four minus that weight. The script verifies 14,778 allowed templates, 7,260 with pairwise distinct rows, zero fully shattered five-row templates, and a sharp maximum of 27 traces. The histogram check follows from the full enumeration. The mathematical reduction from arbitrary ambient dimension to these finite templates is proved in `RESULT.md`.

Independently of that template evaluation, `basic_dimensions` directly constructs all radius-two Boolean balls for dimensions one through six and enumerates support candidates within the ball centered at zero (every shattered support can be translated into that ball). It checks the sharp VC dimensions zero, zero, one, three, four, four. Separate direct checks verify that five stated points in the six-cube have precisely 27 traces and that four basis vectors in the five-cube are shattered.

Expected terminal lines include:

```
TEMPLATE_CERTIFICATE_PASS 14778 7260 0 27
DIRECT_DIMENSION_PASS 1 0
DIRECT_DIMENSION_PASS 2 0
DIRECT_DIMENSION_PASS 3 1
DIRECT_DIMENSION_PASS 4 3
DIRECT_DIMENSION_PASS 5 4
DIRECT_DIMENSION_PASS 6 4
SHARP_27_TRACE_WITNESS_PASS [16, 3, 5, 6, 24] [15, 19, 21, 25, 30]
FOUR_SHATTERED_WITNESS_PASS [1, 2, 4, 8]
ALL_RADIUS_TWO_CUBE_CERTIFICATES_PASS
```

The script fails an assertion if a checked claim is false. The direct checks are finite cross-checks; the proof of the unrestricted dimension theorem additionally uses the exhaustive dimension-independent reduction. No independent audit has been performed.
