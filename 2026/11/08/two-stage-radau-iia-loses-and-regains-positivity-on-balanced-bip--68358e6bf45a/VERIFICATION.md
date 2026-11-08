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

# Verification of the stated theorem

Run `python verify.py` in the directory containing the bundled file (Python 3 standard library only). The observed output was:

```
PASS: 77 exact-rational matrix cases; 9680 checked entries; polynomial and sign witnesses verified
```

The script constructs each combinatorial Laplacian, evaluates the projector-based rational step, checks that the matrix denominator times the result equals the matrix numerator exactly, confirms row sums and symmetric entries, and checks all off-diagonal signs and diagonal polynomial expressions in seven graph sizes and eleven rational scaled steps. It also checks specific root/sign witnesses and the strict positivity sum-of-squares identity at the borderline safe size.

The mathematical proof, not a finite experiment, handles the unbounded parameter ranges \(m\ge2\) and \(h\ge0\). It uses the three projectors, two explicit positive off-diagonal expressions, the exact quartic formula, the \(m=5\) sum of squares, and Descartes' rule for \(m\ge6\). The two roots need not be approximated for the theorem. This is an independent-to-the-symbolic-derivation computational spot-check, not an independently audited proof.
