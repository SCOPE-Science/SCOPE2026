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

The standalone `verify_tritangents.py` enumerates the exactly 120 labeled tritangent classes (8 singletons, two copies of 28 unordered pairs, and 56 unordered triples) and computes the induced permutation orbits for every one of the 22 partitions of eight. It checks fixed point counts using two independent calculations (direct orbit spectra and the disjoint-cycle subset formula) for all extension exponents up to each Frobenius order.

Successful exact run: `PASS: 120 Bertini pairs; 22 S8 classes; prefix signatures 13,20,22; sharp degree 3` and `PASS: direct subset orbit calculations agree with cycle formula at every period`. Output table `tritangent_22_spectra.csv` records each partition, the first three extension counts, its full tritangent permutation-cycle spectrum and Frobenius order. The CSV is generated deterministically from the program.

The program checks the finite S8 problem only; it does not independently verify the classical Bertini geometric correspondence. That correspondence is justified by the primary sources cited in `RESULT.md`. The existence over q greater than 1456 is a proof by descent and a nonzero-polynomial zero bound, not a computer-search result. Independent mathematical audit has not been performed.
