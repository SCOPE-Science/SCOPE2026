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
# Reproducible checks

Run `python verify.py` using Python 3 with its standard library only. Its exhaustive independent-by-algorithm construction enumerates binary action profiles and reconstructs connected susceptible components and every player's payoffs after unilateral action changes; a separate transfer dynamic program evaluates the coefficient/trace formula.

The run checked 86 instances over cycle orders three through eleven at rational and integer values of \(t=nC/L\), including equality boundaries; the first open-cell Perrin and coefficient counts; 27 cost/PoA cases for \(1<t<2\); and 27 price-of-stability cases for \(2<t<3\). It emitted `VERIFY_OK`. Finite enumeration is not a proof for unbounded graph order or real parameters. The proof of the all-order statements is in `RESULT.md`.

The originality assessment is a literature comparison, not independent external certification. No independent audit has yet been performed.
