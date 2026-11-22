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

# Reproduction and mathematical verification

The analytic theorem, hypotheses and all boundary cases are proved in `RESULT.md`. Run `python3 check.py` with any recent Python 3 interpreter; there are no third-party dependencies. The script independently recomputes six positive thresholds, confirms the identity linking the second logarithmic PGF derivative to the generalized polynomial, and evaluates a negative one-count innovation quotient for \(\beta=1/2\), \(q=4/5\), \(c=99/100\). It also recomputes the linear near-geometric endpoint constant.

The calculation uses 65-digit decimal arithmetic. With \(z=1-c=0.01\) and 21 nonnegative mass terms, the omitted generating-function tail is at most \(z^{21}\) and its derivative tail at most \(21z^{20}\), both negligible compared with the strictly negative coefficient margin approximately \(-2.14832801326\times10^{-4}\). Finite numerical evidence is not used as a proof of all-parameter sign uniqueness or the asymptotics. The proof uses an elementary generalized sign-variation argument and uniform Taylor expansions.

Scientific limitation: the excluded region is necessary, not a full characterization of thinning self-decomposability. Bibliographic historical-priority comparison is incomplete because the 2024 source full text was not accessible. Independent audit is not yet performed.
