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

# Reproduction and boundaries

The supplied file `check_squares.py` independently constructs the fixed point through nine substitution levels and compares direct equal-block detection against each closed-form square/cube criterion. Use `python3 check_squares.py` in the folder containing that file. The successful diagnostic output was:

```
VERIFY_OK periods=1..600 word_length= 19683 square_checks= 11449800 cube_checks= 11269500 fourth_checks= 11089200 distinct_counts= 6 finite_window_counts= 48
```

The script checks all start positions where the full tested factor fits inside 19,683 symbols; verifies fourth-power absence for the same finite region and periods; determines distinct-square counts for all permitted periods through 243; and tests exact finite count formulas at available triadic scales. These finite checks cannot prove absence beyond the tested prefix or all integral periods. The symbolic difference-word argument and substitution-block proof in `RESULT.md` establish the infinite assertions. No external formal certification or independent mathematical audit is asserted.
