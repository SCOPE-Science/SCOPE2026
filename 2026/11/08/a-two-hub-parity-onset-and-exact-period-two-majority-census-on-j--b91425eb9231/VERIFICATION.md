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

# Verification record

The following commands are reproducible with Python 3 and require no external dependencies:

```bash
python verify_formula.py
python verify_direct.py
```

`verify_formula.py` compares the exact binomial expressions with independently evaluated cyclic-word erosion, dilation and radius-one majority criteria for every \(3\le n\le16\). It checks the two claimed mechanism populations separately and tests the explicit length-five binary-block subfamily for \(2\le m\le6\). Its observed terminal assertion is `FORMULA_AND_RUN_CLASSIFICATION_PASS`.

`verify_direct.py` builds the complete graph \(K_2\vee C_n\), enumerates all \(2^{n+2}\) binary initial states for each \(3\le n\le16\), evaluates simultaneous open-neighbor strict majority twice with tie retention, and independently counts fixed states, least-period-two states and hub-phase transitions. This totals 524,256 simulated initial configurations. Its observed terminal assertion is `INDEPENDENT_EXHAUSTIVE_DYNAMICS_PASS`.

Both programs were run successfully from their embedded source files, and their captured outputs are `formula_output.txt` and `direct_output.txt`. Direct enumeration for finite lengths is not an exhaustive test over the infinite graph family; that extension rests on the self-contained proof in `RESULT.md`. No independent external scientific audit has been performed.
