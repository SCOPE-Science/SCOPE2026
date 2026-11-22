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

# Verification of the MUPS census

The theorem concerns all strictly positive integers \(a,b,c\); no finite program by itself certifies this infinite domain. The proof in `RESULT.md` exhaustively distinguishes palindromic factors containing zero, one, or two markers, and then proves their occurrence/miminality conditions.

The standalone script `verify_mups_bruteforce.py` enumerates literal contiguous substrings independently of the proof template and compares every palindrome string and interval against the proposed three-family list for \(3375\) triples. It additionally compares the three-valued count classification. The exact program output is in `verify_mups_bruteforce_output.txt`.

The script `verify_mups_census.py` independently creates a map from each palindromic factor to all its positions and counts MUPS without calling the list formula. For every length from \(5\) through \(50\), it exhausts all positive gap compositions (\(17296\) triples in all) and checks the closed counts implied by the rational generating functions. Its program output is in `verify_mups_census_output.txt`.

Reproduce with `python3 verify_mups_bruteforce.py` and `python3 verify_mups_census.py` in the directory containing the four checker files. Python 3 standard library only. Both checks finished successfully. No independent scientific audit was performed.
