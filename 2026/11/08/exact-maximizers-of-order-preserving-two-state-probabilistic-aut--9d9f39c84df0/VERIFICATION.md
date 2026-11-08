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

# Verification instructions

The theorem has two logical components. For necessity, check the affine reduction \(f_a(x)=q_a+(p_a-q_a)x\), the monotone greedy envelope and the ordered-slope comparison of active lines. For sufficiency, check that every rational map in `RESULT.md` sends \([0,1]\) strictly into \((0,1)\), has positive derivative, that adjacent maps cross at the declared switch thresholds, and that the orbit perturbation is strictly smaller than the half-spacing separating those thresholds from baseline orbit points. The all-length proof is analytic and does not rely on the finite checker.

Execute `python checker.py` from a directory containing the extracted package files. The script enumerates 162 positive-composition profiles through total length eight, checks strict greedy selection and exact rational probabilities, and for lengths up to six compares every competing word. An independent random-seeded grid audit checks 1,750 monotone two-state machines of three-symbol alphabets, including both possible single accepting states. The reproducible sample is not a proof of necessity. No external solver or network access is required.

Scientific limitations: the theorem applies to monotone (nonnegative determinant) two-state PFAs; unrestricted two-state PFAs may isolate other words. No independent audit has been performed.
