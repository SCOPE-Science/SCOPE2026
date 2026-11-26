---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For k>=1 the selected divisors of 3*2^k have sum 4*2^k-2, exactly half the total. Multiplying a balanced divisor partition by every divisor of a coprime factor preserves equality. Factoring out the complete power of 2 and the unique factor of 3 proves both progression rules. All table starts have the claimed residues, and adding 18 each time preserves the variable summand's membership. The only uncovered odd targets above 983 are 1001 and 1019, both settled by the displayed exceptional decompositions. I independently enumerated paired divisors through 1200, doing exact subset-sum by remainders for the half containing n, and reconstructed the residue minima and the finite two- and three-sum sets. This confirmed 945 is the only odd Zumkeller number through 983, the six possible even summands below 38, and the absence of 38 from their two-sum set. Any decomposition of 983 must have exactly one odd summand, so the deficit 38 is decisive. Replay: python3 /workspace/branches/local_exact_audit.py 1. The symbolic progression argument, not the finite computation, proves the infinite tail.

## originality

FAIL

The earlier indexed fixed-length Zumkeller result explicitly proves G_3=983 with the same positive summands, repetition convention, and exact number of terms; this is equivalent to conductor 984. Its companion results give all greater fixed-length thresholds. The frozen modular covering offers an alternative proof of an already covered result, not a distinct threshold.

## value

FAIL

The exact conductor answers a natural additive question, but it is already established, and the alternative modular cover here neither improves a threshold nor yields a distinct valuable claim: even targets are already covered from 46 by the older two-sum theorem. This submission is not a new scientific answer to the posed problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
