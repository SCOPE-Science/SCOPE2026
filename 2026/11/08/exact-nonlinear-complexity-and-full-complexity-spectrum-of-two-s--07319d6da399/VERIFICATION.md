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

# Reproduction

Run `python3 checker.py` using Python 3's standard library. Successful execution prints exactly `CHECK_OK complete-word tests 28280 histograms 60 pairwise-rotation cases 210`.

The first test enumerates every length-\(n\) word with exactly two nonzero entries for each \(4\le n\le23\), \(2\le q\le4\); it constructs all cyclic factors, checks successor consistency at each candidate register length and compares the answer to the formula. It independently sums each histogram and checks the population identity. The second test uses comparisons between distinct starting residues for three nonzero-label assignments and \(4\le n\le17\).

The mathematical argument for arbitrary \(q\) and \(n\) is in `RESULT.md`: only one aligned nonzero value can appear in a common factor at unequal gaps, and the two zero runs bound all other conflicts. The finite checks do not prove the infinite statement. No independent audit or computational certification is asserted.
