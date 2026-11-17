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

Run the following from the directory containing the three standalone Python programs, using Python 3.9 or later and no external dependencies:

```sh
python verify_symbolic.py
python verify_direct.py
python verify_census.py
```

The programs were executed in this order. Their exact captured standard outputs are stored in `verify_symbolic_output.txt`, `verify_direct_output.txt`, and `verify_census_output.txt` respectively.

`verify_symbolic.py` exhaustively processes 729 truncated count signatures augmented with six origin tags. It verifies the equality of the complete signature/tag system after updates three and fifteen for every signature, confirms the 666/15/48 period classification and the twelve-entry four-period type-pair census. The reduction from arbitrary labelled graphs is proved in `RESULT.md`: a finite certificate only proves the all-size statement because the quotient is lossless for the relevant transitions and the tags track individual groups.

`verify_direct.py` separately simulates individual vertices, checking all 164,754 labelled initial configurations over six graph sizes, each against the claimed basin formula. It checks explicit sharpness and primitive-four-cycle examples. Its graph-by-graph totals are in the recorded output.

`verify_census.py` uses exact integer arithmetic for the multinomial and binomial census weights through 100 vertices per part and reports large-size ratios through 240. Its floating-point ratios are illustrative only; the analytic asymptotics are obtained from the exact inclusion–exclusion expansions displayed in `RESULT.md`.

Scope: no arbitrary graphs, different colour counts, different thresholds, asynchronous updates or independent external validation. A computer-checked finite lemma is not a machine-checked formal proof, and historical priority is not independently certified.
