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

# Verification record

The finite checks use the independently executable standard-library programs `verify_prym.py` and `verify_gcd.py`. Both completed and printed `VERIFY_OK`.

`verify_prym.py` tests each odd prime below 110. It independently computes the elliptic Hasse invariants by quartic multinomial extraction and the Legendre recurrence, confirming equality up to a nonzero scalar. For every smooth \(\mathbb F_p\)-coefficient for those primes, it directly expands the defining degree-eight polynomial and checks the rank of its entire genus-three Cartier matrix against the predicted factor ranks. Its checks also confirm the excluded coefficients are not roots of the elliptic Hasse polynomials.

`verify_gcd.py` uses a separate factorial formula for Legendre coefficients and exact modular polynomial Euclid division to reconstruct specified superspecial-Jacobian parameter counts in characteristics \(3,5,7,11,13,17,19,23,31,47,73,97\). This is a finite cross-check, not an independent proof of the infinite-characteristic statement.

The proof for all odd primes is the rational-map/isogeny argument, two exact coefficient identities, and the characteristic-\(p\) Legendre differential equation; the programs are supporting reproducibility evidence only. Independent mathematical validation was not performed.
