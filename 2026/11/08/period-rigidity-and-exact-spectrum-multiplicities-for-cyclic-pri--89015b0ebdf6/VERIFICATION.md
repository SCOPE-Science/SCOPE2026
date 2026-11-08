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

# Reproducibility

Run `python3 CHECK.py` with Python 3 and no third-party dependencies. It prints `CHECK_OK` upon passing the finite exact-arithmetic tests. All Fourier-zero decisions use polynomial remainders over the integers modulo the appropriate cyclotomic polynomial; no approximations to roots of unity or numerical rank thresholds are used.

The checker verifies every graph and every candidate frequency subset at cyclic orders 6, 10, 12, 14 and 15; one representative of each period stratum at order 18 and 30 is compared against **all** candidate frequency subsets of the required size. It separately enumerates all graphs at orders 18 and 30 to certify the complete multiplicity histograms, and verifies a larger histogram at order 30 for the alternate prime factor. These bounded experiments do not constitute proof for arbitrary dimensions, primes or functions. The analytic proof in `RESULT.md` supplies the universal quantifiers.

The exact coefficient-comparison step follows from the irreducibility of the prime cyclotomic polynomial over the coprime cyclotomic field. The last step uses Fourier inversion and double-annihilator duality on a finite cyclic group.
