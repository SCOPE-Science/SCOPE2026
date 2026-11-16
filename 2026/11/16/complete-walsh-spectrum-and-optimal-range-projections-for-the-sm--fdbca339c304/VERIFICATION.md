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

Run `python3 check_ice3.py` beside `SPECTRUM.json` using standard Python 3. The program performs a second complete integer-equation enumeration in addition to brute-force checking all 262,144 orientations, calculates all 262,144 integer Walsh coefficients, checks independently evaluated signed sums at the 1,024 non-tree frequency representatives, and verifies the full signed-level table and the Parseval identity.

It then computes the frequency support indicator's entire inverse Walsh transform, checks its absolute sum 1,822,720 and reduced norm 445/64, and verifies the classification of all weight-two zero frequencies. No floating-point arithmetic or unproved extrapolation appears.

Expected marker: `ICE3_WALSH_EXACT_PASS orientations=148 frequencies=262144 zeros=162816 rank=99328 extra_even_zeros=31744 two_edge_zeros=45 min_nonzero=4 endpoint=445/64`.

The checker certifies this finite graph only. Optimality among unrestricted linear projections additionally uses the translation-averaging lemma proved in `RESULT.md`; the checker does not replace that argument. No independent external audit has been performed.
