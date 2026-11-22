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
The proof reduces the operator on the full tree Lipschitz space to an exact three-block Banach operator on root values, spine increments and tooth increments. For uniformly bounded tooth length, the finite geometric inverse of the tooth block exists uniformly for all nonzero spectral parameters; a telescoping range functional computes index \(-1\) for the spine shift. For unbounded lengths, two explicit families of tooth-supported vectors witness failure of closed range for the nonzero closed unit disk. At zero, independent tooth terminal coordinates lie in the kernel.

Run `python check_comb.py` from the same folder. The expected output is `COMB_EXACT_FINITE_CHECK_OK 1085`. The 1,085 assertions test exact rational finite-tooth inverses, residual estimates and spine telescoping. They do not prove the infinite-dimensional claims, whose estimates and quantifiers are fully established in `RESULT.md`.

The empirical checker does not certify research priority or independent correctness. The named full texts are arXiv:2611.11737v1 and arXiv:1906.02372; independently obtained publication dates and spectral claims must be assessed against those sources. This is an internal self-review only.
