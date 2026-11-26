---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For initial downstream position j, gate times s are b-1-j modulo b, and the source index at that crossing is -s modulo a. The first L updates therefore test precisely the a/g source positions congruent to j+1 modulo g, once each; erasure at gate time s enters the state at time s+1. If an active downstream bit has any future erasure, the state is not periodic because its downstream population will drop. Otherwise both words simply rotate, returning within L steps. Hence the last erasure is exactly first periodic entry, with zero for the empty maximum. At any t an initial downstream bit is free if already scheduled to be erased by t or immune forever; otherwise it must be zero. Summing the resulting weights independently over source residue classes gives C_t and the stated C_0 and C_L. For 0 <= r <= b, only bits j<r can first die after L-r, and their last encounter has source index j+1 modulo a. A death there requires precisely one zero in that source class, at that index. Grouping those singleton-zero source patterns gives the late product; the other 2^(a/g)-a/g patterns in each class have all downstream choices free. At r=1 exactly one position incurs a half weight, giving 2^(a+b-a/g-1) terminal states and sharpness; substituting equal and consecutive lengths gives the reported probabilities. Independent direct simulation of all states for 2 <= a,b <= 5 matched the products and terminal counts in all 16 cases (236 cumulative/tail comparisons). The finite replay corroborates the indexing, not the general proof.

## originality

PASS

The supported distinct claim is the full first-periodic-entry census, the arithmetic late-tail product and the exact terminal population. Eventual projection by the LCM, periodic-orbit counting and general transient bounds have antecedents and are not credited as new. Neither the matching one-bridge projection nor the closest alternative-topology shell or basin records establishes these counts. Priority is bounded by the statements inspected.

## value

PASS

First periodic entry is a natural transient statistic not captured by a period census or worst-case upper bound. The formula quantifies every shell on all pairs of lengths and resolves a sharp arithmetic contrast, with the worst case frequent for equal lengths but exponentially rare for consecutive lengths. The terminal population and the late-tail product supply exact information beyond a generic finite state enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
