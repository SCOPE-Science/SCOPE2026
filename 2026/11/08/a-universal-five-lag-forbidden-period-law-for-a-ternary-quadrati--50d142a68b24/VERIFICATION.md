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

# Reproducibility and limitations

Run `python3 verify.py` with a standard Python 3 interpreter. The script uses exact integers and no external libraries. It enumerates all ten two-zero masks of a five-cycle, three additive offsets per mask, and checks that exactly ten valid transitions exist. Every valid transition goes from nonadjacent source zeros to adjacent destination zeros, so two successive transitions are impossible. This exhaustively verifies the finite local lemma used in the symbolic proof.

It also enumerates all \(3^k\) initial states for each \(k=2,3,\ldots,10\), iterates the stated map exactly \(5k\) times, and verifies there is only one fixed state each time. The expected output is:

```text
VERIFY_OK masks=10 transitions=10 square_zero=yes lags=9 states=88569 fixed_each=1 exact_modular=yes
```

The global, unrestricted theorem follows from the structural proof in `RESULT.md`; nine sample memory lengths cannot by themselves prove the result for all lengths. No independent audit or external validation is claimed.
