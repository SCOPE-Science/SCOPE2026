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

# Verification performed

Run `python check_exhaustive.py` and `python check_identities.py` from a directory containing the accompanying files. Both require only Python 3 standard library.

The independent exhaustive checker applies a Dhar burning stabilization criterion rather than assuming the claimed recurrent-word test. It separately simulates every legal avalanche, tabulates exact interval support counts, tests all zero events and the exact expected total toppling count. It examined all stable configurations for all fan lengths from two through nine and all drive positions, totaling 35,044 recurrent-state/addition tests. It also separately tested the forbidden-zero-word characterization against Dhar burning.

The second checker derives the reduced-Laplacian determinant by a continuant recurrence and tests normalization, conditional factorization, exact mean and finite forms for 536 integer parameter pairs, with fan lengths through 100. It also tests 25 limiting local probabilities at length 200, plus analytic normalization and moment constants.

## Scope and limitations

The code is a finite consistency check and is not a computer proof for all sizes. The infinite-size argument rests on the explicit Fibonacci identities and Binet asymptotics in `RESULT.md`; the exact spatial factorization is proved from the burning criterion and path structure. No external scientific or independent validation is asserted.
