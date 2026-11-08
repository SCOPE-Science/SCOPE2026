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

The general theorem follows from a local classification of square-gcd residues modulo prime powers, the Chinese remainder theorem, and the double finite-difference identity for the spectrum of maximal cyclic runs.

With standard-library Python, execute `python3 verify_square_gcd_runs.py`. A successful replay prints `VERIFY_OK` for 899 moduli, 16077 window checks, and 65343 maximal-run multiplicity checks, together with illustrative exact run histograms.

The checker directly enumerates square-gcd residues using exact integer square roots, then compares observed window counts and run multiplicities against separately calculated closed-form values. It does not exhaust infinitely many moduli or lengths, and does not independently establish historical originality.
