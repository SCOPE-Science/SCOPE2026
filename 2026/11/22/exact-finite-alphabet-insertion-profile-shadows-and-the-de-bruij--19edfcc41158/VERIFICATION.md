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

Run `python3 verify_profile.py` with Python 3 and its standard library. The script recomputes the ordered-pair count vector separately for each literal insertion output and checks the analytic profile-ball formula against brute force for every input word over alphabets of sizes \(2\), \(3\), \(4\) and \(5\), up to lengths \(10\), \(8\), \(5\) and \(4\), respectively. That is \(14{,}030\) source words in these shorter ranges. A separate literal census of all \(3^{10}=59{,}049\) length-ten ternary source words brings the total to \(73{,}079\) direct profile comparisons. It independently enumerates integer-vector signature types and checks the de Bruijn construction for alphabets through size \(7\). A complete ternary length-ten maximizer census finds \(216\), matching the classical cycle count.

`verification_output.txt` is captured stdout from this script and ends with `ALL CHECKS PASSED`. The mathematical proof in `RESULT.md` establishes the all-word formula and sharp extremal consequences; exhaustive tests at bounded lengths cannot, by themselves, certify infinitely many alphabet sizes or word lengths. The classical BEST/directed matrix-tree theorem is explicitly used for the shortest-maximizer enumeration. No independent scientific audit has been performed.
