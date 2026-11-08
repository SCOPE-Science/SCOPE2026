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

The exact recurrence checker `checks/verify_fast_entry.py` uses eight three-time histories; its arithmetic is over integers and has no external dependencies. Run `python3 checks/verify_fast_entry.py`. Its captured output is `checks/verify_fast_entry.out`. It reproduces all six tabulated populations.

The independent simulation checker `checks/direct_tree.c` constructs the rooted cubic tree explicitly, evolves each initial bit mask three times under strict neighborhood majority, and counts `step(x)==step(step(step(x)))`. Compile using `cc -O3 -std=c11 checks/direct_tree.c -o direct_tree`; run `./direct_tree`. Captured output is `checks/direct_tree.out`. It checks \(2^4+2^{10}+2^{22}=4195344\) initial configurations, exhausting heights one through three only.

The proof of the all-height formula is a state-history bijection. The exponential bound follows from independent radius-three obstruction events and is not inferred from finite simulation. No infinite computation or independent audit is claimed. The bound is not optimal and the precise asymptotic entropy is unknown here.
