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

The doubling action shifts binary digits, so the two half-open holes correspond to 000 and 111. Away from null dyadic ambiguities, n tests use n+2 digits, each word having Lebesgue probability 2^(−n−2). Independent exhaustive inclusion–exclusion over subsets of hole-test positions for each schedule through n=5 accounts for compatible fixed digits and zeroes inconsistent intersections. The minima are 7,12,21,37,64; alternation attains the first four and has 65 at n=5. Exactly 01001,01101,10010,10110 attain 64. Independently counting admissible whole-period words by their initial and final suffix states, then applying the Newton trace identities, gives the two stated period matrices and characteristic polynomials t(t³−2t²−3t−1) and t(t³−6t²+4t−1). The second matrix is positive and the square of the first is positive. By Perron–Frobenius theory multiplication by the fixed partial-period prefix for each residue class gives a positive leading scalar (each suffix always has a valid continuation), proving the full limits. The unique-real-root discriminants are −23 and −139. Exact rational brackets were checked as stated; 3079595³−10⁶·5278040²=1348881297924569875>0. Thus the period-three growth is strictly smaller, producing faster escape, with no global all-schedule optimality claim. Replay: python3 /workspace/branches/check_4.py and check_4.out beside it. Frozen verify.py and VERIFICATION.md were inspected, not executed.

## originality

PASS

The supported contribution is the sharp depth-three deterministic switching reversal and its strict limiting rate comparison. Neither annealed iid optimization on the same hole family nor deterministic optimization at depth two gives the claimed comparisons; switch-count matrices and Perron growth are established methods. This judgment is bounded by the evidence available, with explicit access gaps, not a priority certification.

## value

PASS

Increasing cylinder depth by one is a natural test of a genuine all-horizon alternation principle. The minimal failure and the persistence of the reversal in the escape exponent rule out two distinct extrapolations and give exact benchmark schedules for optimization, even without claiming a global optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
