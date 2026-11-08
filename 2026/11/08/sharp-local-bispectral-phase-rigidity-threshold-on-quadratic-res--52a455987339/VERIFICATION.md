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

## Checks

`python3 check_paley_bispectrum.py` prints `PALEY_BISPECTRAL_LOCAL_RIGIDITY_CHECK_PASS` and independently constructs supported Schur triples for every odd prime through \(101\), comparing ranks over two large finite coefficient fields with the theorem. Exact rational ranks are additionally checked through \(31\). The script checks that every relation annihilates the additive-character phase vector modulo \(p\) and directly exhibits the full two-parameter family at \(p=13\).

## Scope of verification

No computational finite test establishes a theorem quantified over all primes. The exact mathematical proof is the character-diagonalization plus the quadratic-residue count and the sixth-root obstruction in `RESULT.md`. Rational rank is the object proved. A finite phase fiber may have multiple discrete components; only its identity-component dimension is established for all primes. The full two-torus is additionally established at \(p=13\). Independent mathematical validation has not been performed.
