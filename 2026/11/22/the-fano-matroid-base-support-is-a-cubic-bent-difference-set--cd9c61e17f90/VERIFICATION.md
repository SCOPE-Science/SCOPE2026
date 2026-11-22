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

# Reproduction of finite Fourier and Fano checks

Run `python3 verify_fano.py` under Python 3.8 or later using only the standard library. The script verifies the seven Fano lines and their unique-pair property; exactly 28 noncollinear bases; all 128 Fano signed character sums against a separate Krawtchouk-minus-lines formula and exact ten-category table; all 64 chart Fourier coefficients by both direct character sums and the integer Walsh-Hadamard transform; all 63 nonzero autocorrelation counts and balanced Boolean derivatives; and the complete 64-coefficient binary Mobius inversion producing 12 quadratic and 16 cubic ANF terms.

Expected completion text: `CHECK_OK: Fano lines=7, bases=28, full Walsh frequencies=128, six-bit characters=64, autocorrelation differences=63, ANF degrees=12 quadratic +16 cubic; rank=64; condition=7.`

All claims are about the explicitly enumerated finite six-dimensional Boolean group; exhaustive arithmetic is a complete certificate for that fixed domain. The analytic signed-character table and Fourier inversion provide independent derivations of the spectrum and autocorrelation. The historical literature comparison is bounded; an independently performed mathematical or priority audit is not supplied.
