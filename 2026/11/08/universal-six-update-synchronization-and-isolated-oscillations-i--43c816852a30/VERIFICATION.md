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

The reduced-state checker `verify_reduced.py` tested every one of the 2158 saturated support-multiplicity vectors realizable with at least three nonempty parts; it confirmed preperiod at most six, only primitive periods three and four, no transient access to asynchronous cycles, exact recurrent pattern types, and sharp example trajectories. The raw output is in `reduced_output.txt`.

The separately implemented adjacency-list checker `verify_direct.py` evolved 84753 labelled configurations across 19 distinct positive part-size vectors (three to six parts), without invoking the reduced transition. It verified the formulas for recurrent phase-three and phase-four populations, the absence of transient asynchronous attraction, and sharp convergence cutoffs. The raw output is in `direct_output.txt`.

The infinite-family argument additionally uses the exact same-part initial-color representative reduction and the proof that counts of identical support types saturate at two. Finite graph tests are corroboration; full quantification follows from that reduction and a complete finite state check. No independent external audit or formal proof assistant certification was performed.
