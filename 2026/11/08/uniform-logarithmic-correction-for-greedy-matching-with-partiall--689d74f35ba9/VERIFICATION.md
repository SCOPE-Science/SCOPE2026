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

Run `python verify.py` with standard Python 3. A successful replay prints `VERIFY_OK 4937 exact assertions`.

The implementation separately computes the greedy failure probability from (a) the reduced \((k,t)\) Markov chain and (b) the full unmatched-left and unmatched-right vertex subsets on every \(G_{n,r}\) for \(2\le n\le6\). It compares the resulting fractions exactly. It also tests the normalization of transition weights and both conditional moment identities for \(2\le k\le40\), and evaluates the finite bound for \(2\le n\le30\) and all \(r\). No external packages are needed.

The full uniform asymptotic and universal error constant are justified by the analytical inequalities in `RESULT.md`, not by finite-case testing. The computation cannot establish bibliographic priority or independent certification.
