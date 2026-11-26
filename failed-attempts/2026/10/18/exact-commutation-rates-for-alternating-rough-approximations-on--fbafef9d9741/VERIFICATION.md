---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

An E-block survives L_E L_F precisely when its F-expanded neighborhood is contained in S; similarly for the reverse order. Equal outputs are saturated by both partitions, hence by their join, and both outputs are subsets of S. On a partially included join-component equality therefore means both outputs are empty there, which proves the component criterion. On the connected alternating cycle the two neighborhood families together give all indexed four-point windows; at n=2 they all coincide as sets, and every proper input avoids them. For n≥3 a proper input containing exactly four consecutive points witnesses failure of universal commutation. The run-state automaton has a unique closed state sequence for each admissible indexed word, since a zero resets the state; the trace counts indexed words, not rotation classes. Adding the full set and normalizing by 2^(2n) is correct. The matrix is primitive with characteristic polynomial t^4-t^3-t^2-t-1 and its Perron root lies strictly between one and two, giving the claimed decay. Separate literal composition checks agreed on all 90346 partition-pair/subset cases through size five and all 87376 cyclic inputs for n=2 through 8; the replay reproduced the seven counts and the trace recurrence through length 44. The component and transfer arguments, not the finite replay, prove the unbounded results.

## originality

FAIL

The cyclic finding is a direct consequence of a distinct indexed exact trajectory theorem for the same alternating pair partitions, applied at time two in both phases; the remaining enumeration and root formula are already the indexed tetranacci-Lucas count. The general component criterion adds the ordinary join-saturation observation to the earlier minimal-input characterization of block survival. The comparison concerns mathematical coverage and direct implication, not chronology: the indexed trajectory result has the same catalogue date as the frozen record.

## value

FAIL

Measuring order sensitivity is motivated, but the frozen quantitative claim offers no substantive increment over the established pointwise trajectories and the exact indexed run table: it takes time two in both phases and adds the full input. The general block criterion is the known minimal-input test intersected with the two saturation conditions. Beyond a useful exposition of these consequences, the record does not isolate a nonroutine new agreement phenomenon or a gap left by that coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
