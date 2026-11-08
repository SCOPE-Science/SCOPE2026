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

The theorem has a complete algebraic proof in `RESULT.md`. The separate computation checks finite examples, and cannot establish a claim over all finite fields by itself.

Run `python checks/verify.py` from this package's root. It needs Python 3 only. The script uses polynomial moduli `0b111` and `0b1011` for the binary extensions of sizes four and eight, respectively, as well as prime fields of orders three, five, and seven. It builds every first factor, computes the linear anticommutator map on the six-dimensional triangular algebra, and sums exact kernel sizes. It then performs a literal full multiplication census over fields of orders two and three, looping over both factors and all nine matrix entries independently of the linear-map construction. The complete standard output is `checks/verify_output.txt`.

Verified values for \(q=2,3,4,5,7,8\) are \(928,7965,418816,230625,1957501,179863552\), respectively. Both independent literal-multiplication checks return \(928\) and \(7965\). Exhaustive field tests and comparisons with the closed formulas all pass.

No higher-dimensional triangular algebra, nonzero target Jordan product, or solution-orbit enumeration is verified. No external independent review was performed.
