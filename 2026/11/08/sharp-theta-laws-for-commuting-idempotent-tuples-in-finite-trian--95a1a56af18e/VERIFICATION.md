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

# Reproducibility and verification

Run `python verify.py` with standard-library Python 3. The script builds full incidence-algebra multiplication matrices, enumerates actual idempotents and their ordered commuting pairs/triples over prime fields of orders two and three, and compares all counts with the independent colored-poset sum. In separate arithmetic checks, its dynamic multinomial convolution reproduces the color counts across further parameter values. It prints `VERIFY_OK` only after all assertions succeed.

The direct comparison includes chain sizes up to four, two nonchain posets, and small-size arithmetic sums up to seven. The script does not exhaustively enumerate all finite fields or prove the asymptotic theorem. The unrestricted proof uses unitriangular conjugacy, orbit-stabilizer and fixed-parameter theta-weighted Stirling analysis as detailed in `RESULT.md`; no infinite theorem is inferred solely from the finite output.

The simultaneous-conjugacy ingredient is known from Garcés–Khrypchenko (2021, Lemma 5.4). The exact tuple enumeration and the sharp theta law were checked against accessible literature, but a complete priority certification and any independent mathematical audit remain unperformed. The complete published full texts of two relevant single-idempotent enumeration papers were inaccessible.
