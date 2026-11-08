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

# Reproduction and verification

Run `python3 verify.py` using Python 3 without external packages. The verifier directly computes the valuation-defined word for bases \(2\)–\(7\), checks recursively constructed words for unborderedness, reversal, length, residues, and all occurrence indices over a finite window, and enumerates all short unbordered factors independently.

Observed output:

`VERIFY_OK occurrence_comparisons= 537764 complete_unbordered_classifications= 56 bases=2..7 lengths=2..96 positions=0..11999`

The proof of the unlimited base/length claim is mathematical and uses the exact parent-letter marker equivalences and elementary density arguments. These finite diagnostics verify implementation consistency only. The external published 2012 generalized two-factor theorem and Lemma 5 are stated as prior inputs, not newly certified results. No independent audit has occurred.
