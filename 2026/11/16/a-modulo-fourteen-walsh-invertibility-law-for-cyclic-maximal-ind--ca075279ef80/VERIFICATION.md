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

# Exact reproducibility

The included `verify.py` is a standalone Python 3 program using no packages other than the standard library. Run `python3 verify.py` in the extracted directory.

The script uses two independent constructions: direct enumeration of maximal independent sets in a cycle and their complete Walsh–Hadamard transform, and the three-state signed transfer product. It compares the transfer formula with direct integer signed sums for all frequencies at lengths \(3\) through \(10\), then checks full Walsh transforms for lengths \(3\) through \(18\). It also verifies the five seed frequencies, the length-seven involution (including its square), the length-fourteen zero-preserving padding, and the modular recurrence patterns.

Observed output: `PASS: transfer/direct n=3..10; Walsh n=3..18; periodic residues; seed/nullword/block` and zero counts at lengths \(3\) through \(18\): `0,8,0,0,0,0,126,0,342,0,0,0,7635,6608,0,23580`.

These finite computations do not establish the classification for untested lengths; the recurrence-state periodicity and exact transfer involution in RESULT.md do. No independent audit or external validation has been performed.
