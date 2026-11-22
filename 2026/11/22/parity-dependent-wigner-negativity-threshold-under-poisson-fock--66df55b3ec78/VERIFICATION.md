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

Exact algebraic checker: `python checker.py` with SymPy installed. The checker evaluates exact rate-dependent stationary probabilities and the loss/re-preparation balance equations for integer indices 1 through 9, confirms equal-rate uniformity, independent Laguerre polynomial coefficients, the balanced-half-loss binomial identity, the full two-photon Wigner polynomial and its minimum, plus sample strict majorization inequalities at rational rates. The checker reports `PASS: 642 symbolic identity and rational-inequality checks`.

The rate-resolvent positivity order, all-index parity proof, global finite positive even-index threshold and stationary trace-distance contraction are mathematical arguments in RESULT.md and are not replaced by numerical tests. External balanced-beamsplitter Wigner positivity is a published input explicitly cited to Vanbever (2021), Lemma 2 and Eq. (30). No independent validation or external certification has occurred.
