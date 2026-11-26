---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

For the two specified labelled 16-vertex graphs and open-neighborhood NOR, `verify_direct.py` exhausts all 65,536 inputs per graph, checks \(F^3=F\), and tabulates recurrent orbits and their basins. `verify_structural.py` uses row and column occupancies for the rook graph and checks the separate input/output permutations on all pairs of vertices and all input subsets. It compares the output-size/fiber census and independently tests fixed configurations via independence and domination. Agreement of one-step outputs and their fibers is after the indicated permutations, not literal equality on the shared label set. The proof in `RESULT.md` includes direct witnesses to the unequal labelled output supports and labelled empty/full basins.

```
python3 verify_direct.py
python3 verify_structural.py
```

The recorded outputs in `direct_output.txt` and `structural_output.txt` contain the census and success summaries. The finite calculation makes no assertion for other graph pairs.
