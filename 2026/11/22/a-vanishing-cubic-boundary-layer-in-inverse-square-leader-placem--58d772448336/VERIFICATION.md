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

# Reproduction and limits

Install the dependency in `requirements.txt` and execute `python verify.py` in a directory containing the supplied files. The exact symbolic checks construct the cost formulas independently from the declared eigenvalue decomposition, clear denominators, verify the degree-six threshold polynomial and its coefficient signs, and test strict positive coefficients for unmatched-pair domination. They also verify the first-power rational witness and the first two terms of the large-size threshold expansion. An independent exact matrix construction compares all three pair representatives for sizes \(3\le n\le6\) at five rational weights, and all unordered leader pairs for sizes \(3\le n\le5\), a total of 500 exact grounded-matrix checks.

The all-size and continuous-weight conclusions depend on the explicit algebra and positive-resolvent proof in `RESULT.md` and `CERTIFICATES.md`; finite tests alone cannot certify them. The verifier uses symbolic algebra, not a proof assistant or external mathematical certification. No independent audit is represented or implied.
