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

# Verification and reproduction

From the package directory run `python3 verify.py certificate.csv` under Python 3. The program uses only the standard library and prints:

`VERIFIED_W_E6_51840_CLASSES_25_STEINER_PAIRS_120_TRIPLETS_40_SPECTRA_25_PREFIX_10_14_20_22_23_24_24_24_25`

The checker reconstructs all geometric line classes, anticanonical triples, paired Steiner trihedra and complementary triplets, then enumerates the full Weyl group and its conjugacy classes using simple-root reflections and conjugation. It generates all 25 CSV rows from exact permutations, compares the certificate file byte-for-byte and checks: 25 distinct 40-triplet cycle spectra; only 20 distinct line spectra; 25 distinct joint signatures given by line spectra and one rational-triplet count; the exact first-nine prefix distinctions; and the 40-element Weyl orbit of one triplet. CSV row numbers are program-local enumeration labels, not external Atlas identifiers.

The two classes indistinguishable by the first eight consecutive extension counts have respective triplet cycle partitions \(1^1 3^1 12^3\) and \(1^1 3^1 9^4\). At degree nine they give \(4\) and \(40\) rational triplets. Their identity as distinct conjugacy classes follows from the exhaustive conjugation calculation, not merely their different line cycles.

Limitations: finite enumeration is exact but not a formal proof assistant certificate; the link between the classical line configuration and geometric finite étale schemes uses cited algebraic geometry. No independent audit or external certification has been performed.
