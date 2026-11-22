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

# Verification and limits

This statement has a fully specified overlapping LZ longest-previous-factor definition. The proof is the three-regime greedy-parse case analysis in `RESULT.md`, followed by exact inequality partitions and the independent-uniform-pair limit derivation.

The two standalone Python 3 programs have no third-party dependencies. In the directory containing these files, run `python3 verify_lz.py` and `python3 verify_counts.py`. Their recorded deterministic standard outputs are in `verify_lz.out` and `verify_counts.out`.

`verify_lz.py` compares the literal-greedy parse of \(0^a1^b0^c1^d\) and its reversal with both closed forms for all positive integer run lengths 1 through 13, a total of 28561 quadruples. The copy source may overlap the phrase. `verify_counts.py` enumerates all positive compositions of each length 4 through 30 and checks symmetry and the first \(|\Delta|=3\) instances; it also verifies the seven rational limiting probabilities and the expectation \(13/9\).

Finite execution does not certify the universal all-length claim or historical priority. These rely respectively on the supplied case-analysis proof and the literature comparison. No independent audit has been performed.
