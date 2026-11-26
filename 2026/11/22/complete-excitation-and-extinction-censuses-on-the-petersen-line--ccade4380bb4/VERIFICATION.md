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

Independently recomputed every one of the 3^15 labelled states at each threshold, without executing frozen scripts. checks/petersen_images.py computes the successor of each resting edge from disjoint active incidences at its two Petersen endpoints; the other phases have their unconditional successors. Iterated images of the complete state set are nested and stabilize precisely on the periodic set. Traversing this set gives each orbit once; successive synchronous predecessor layers give exact first entry and inherit the orbit label. For all four thresholds the attractor/period/basin populations, entry histogram, joint time and period histogram, and individual basin-size histogram match both frozen output tables in full. The four recorded max depths are 12,6,3,3; directly checked 94238 at depth 12, and 66495→5626834→12602018→3228168→169→2→0 with exact depths 6 through 0. All-rest is fixed and the only fixed state since phases 1 and 2 always change. The threshold-one period lcm is 120, giving equality after 12 and failure one update earlier. Run python3 checks/petersen_images.py with theta=1,2,3,4 as the positional argument (NumPy); each checks/petersen_images_*.out is saved. This certifies the stated finite graph and thresholds only.

## originality

PASS

The exact all-threshold census and sharp finite settling statistics are supported as distinct findings. Qualitative eventual threshold-two extinction is already implied by a matching same-day structural Resultary theorem and the earlier Tait correspondence. Do not claim that qualitative extinction itself is distinct or infer order from the shared date. Neither structural theorem nor the other inspected results supply the sharp depth 6, its 930 initial states, or the labelled threshold-one census.

## value

PASS

This line graph is a natural small four-regular example at the critical half-degree threshold, built from a canonical snark. The sharp worst-case settling time and how many states attain it are additional natural invariants even after eventual extinction is structurally known. The complete low-threshold basin/period census and the finite cutoff provide an exact comparative benchmark beyond detecting recurrence on a few states.

The dated certificate retains the supplied scientific assessment, sources and limitations.
