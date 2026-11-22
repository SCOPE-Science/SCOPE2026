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

# Reproducibility and limits

Run `python verify_tropical_lyness.py` in the directory containing the packaged files with Python 3 and SymPy installed. The recorded stdout is `verification_output.txt`; the final line must be `VERIFY_OK`.

The code checks the positive rational two-periodic Lyness first integral by exact symbolic substitution and cancellation. It separately checks the heptagon's area, primitive perimeter, and exact arclength translation for 441 rationally parameterized boundary positions. It enumerates every integer point of the boundary on each energy \(k=4,\ldots,200\) and checks that iteration traverses every point exactly once before returning, plus the seven integer states on \(H=3\). The area-action derivative is symbolically verified.

The finite checks do not establish statements at irrational levels or on infinitely many energy shells. Those statements follow from the conservation limit, unimodular arclength argument, exact translation and Bézout identity in `RESULT.md`. Neither this record nor the computations constitute an independent external audit.
