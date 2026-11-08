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

The derivation in `RESULT.md` supplies the infinite proof. The independent finite checker in `verify.py` constructs finite fixed-point prefixes, computes observed one-count spectra for contiguous factors, and compares exact minima, maxima and spectrum cardinalities to the residue formulas. Reproduce with `python3 verify.py`. The captured output in `verification_results.txt` is a convenience and is not substituted for execution. Tests include \(49\) explicit block-run parameter pairs across \(3136\) factor lengths and \(365\) other sampled image pairs across \(14764\) factor lengths.

The sample's finite-period filter does not establish aperiodicity for an infinite sequence. The explicit block-run family has a separate aperiodicity proof in `RESULT.md`. No formal theorem prover, third-party validation or independent scientific audit was used. The result does not classify nonbinary, nonuniform, non-prefix-dominant or periodic cases.
