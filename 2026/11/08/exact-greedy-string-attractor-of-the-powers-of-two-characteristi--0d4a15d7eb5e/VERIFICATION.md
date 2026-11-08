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

Run `python3 verify.py` using a standard Python 3 installation (no external modules). The checker generates the same one-sided binary characteristic word and implements three independent finite tests:

1. It recomputes the canonical greedy set from first principles, checking every nonempty substring of each of the first \(128\) prefixes and all selected-position intersections, not merely a proposed list.
2. It independently simulates the novel-suffix stopping rule through \(800\) prefixes, checking the geometric formula at each step.
3. It checks exact copied-suffix identities and first-run witness conditions for \(13\) scales, counting \(24{,}573\) individual gap tests.

Expected output:

`VERIFY_OK direct_prefixes=128 selected_direct=7 suffix_prefixes=800 selected_suffix=10 explicit_gap_checks=24573`

The main proof in `RESULT.md` handles *every* integer scale and every prefix, so the proof—not this finite computation—supports the universal statement. The rule uses zero-based positions and the word with ones at \(0,1,3,7,15,\ldots\). For any alternative convention that inserts a leading zero, first normalize the indices before comparing the reported greedy positions.
