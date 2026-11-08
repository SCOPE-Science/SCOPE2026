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

# Verification procedures

The standalone file `verify_ignorance.py` is executable using Python 3's standard library. Run `python3 verify_ignorance.py` for the bounded computation (do not request `--extended` unless a complete six-world census is intended).

Direct evaluator: repeatedly filter current worlds whose two S5 class neighborhoods each contain both truth values. Independent graph evaluator: orient each world-arc by its Boolean label, then check existence of incoming walks at the source and outgoing walks at the target, of every relevant length. All evaluated stages were equal.

Exhaustive case counts at 1, 2, 3, 4, and 5 worlds: 2, 16, 200, 3600, and 86528. A deterministic stratified (not exhaustive) set of 13888 six-world cases was additionally checked. Extremal directed paths, 2-cycles with tails, and 4-cycles with tails were checked through 40 arcs. These are finite consistency tests; the arbitrary-size conclusion follows from the mathematical proof in `RESULT.md`.

The ordinary and proper extremal predictions are separately checked. No independent mathematical audit or historical priority check has been performed. The known finite core characterization is attributed to prior literature.
