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

# Reproducibility and verification

From the directory containing the files, run `python3 verify.py`. The verifier independently generates all cyclic triple-count vectors of every binary word at lengths \(1\)–\(17\) (\(262142\) words total) and compares sets of observed vectors with a connected-flow parameter enumeration. This produces \(1460\) distinct profile instances when counts for each length are added. It also checks coefficients versus a separate direct nested-sum computation through length \(80\), and verifies the illustrative colliding circular words.

The expected output begins with `PASS exhaustive_lengths=1..17`, and reports `262142` enumerated words. The exact formulas and their all-length validity follow from the explicit Eulerian support classification and geometric summations in `RESULT.md`; finite test success is neither an infinite proof nor an independent scientific audit. Full external validation has not been performed.
