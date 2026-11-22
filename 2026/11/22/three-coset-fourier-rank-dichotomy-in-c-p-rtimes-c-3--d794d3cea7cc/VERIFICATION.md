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

Run `python3 check_regular.py` and `python3 check_blocks.py` from this directory using only Python 3 standard library. Their outputs are embedded verbatim in `CHECK_OUTPUT.txt` after execution from extracted package files.

`check_regular.py` tests all 1330 unnormalized supports for \(p=7\) and all 703 identity-containing supports for \(p=13\); rank is computed modulo \(2147483647\) from a fresh 0–1 regular-convolution matrix for every test. Hadamard's inequality bounds every minor by \(3^{3p/2}\), strictly below the modulus for these two values of \(p\). Thus modular and complex ranks agree *exactly* on these finite domains. The normalization factor is \(3p/3=p\), since each unordered support admits exactly three choices of a distinguished element.

`check_blocks.py` independently checks the cyclotomic determinant nonvanishing conditions and full occupancy count for \(p\in\{7,13,19,31\}\) using an integer coefficient criterion in the prime cyclotomic field. Its finite tests are not substitutes for the uniform representation-theoretic proof.

The theorem asserts rank only for distinct three-point coefficient-one supports in \(C_p\rtimes C_3\), where \(p\equiv1\pmod3\). No calculations justify extension to arbitrary weights, composite kernel orders, conditioning bounds, or nonlinear recovery. No independent audit has been conducted.
