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

# Verification

The reproducible exact checker `checker.py` uses Python's standard-library `fractions.Fraction` and `itertools.combinations`, with no external datasets or packages. The command `python checker.py` returned:

```
EXACT_FRAME_CHECKS_PASS 14764
FIRST_FIVE_PELL_PAIRS [(1, 3, 1), (2, 8, 2), (3, 27, 6), (4, 98, 21), (5, 363, 77)]
```

It directly builds the Gram matrix \(G_{I,J}=\langle u_I,u_J\rangle^2-1/d\) for five small pairs, verifies its predicted zero and two nonzero spectral scalars via exact matrix identities and trace moments, checks the Pell recurrence for eight solutions, and tests exact equality of the two explicit frame eigenvalues for every permissible integer pair with \(5\le n\le200\). These checks are finite. The all-integer theorem relies on the counting and Pell proofs in `RESULT.md`. No independent audit, external proof certification, or numerical noise analysis has been performed.
