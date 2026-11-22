---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Maximal independence is equivalent to avoiding cyclic 11 and 000; the unique periodic three-state path gives a signed integer transfer trace without double-counting. Unweighted trace P_n has recurrence P_n=P_{n-2}+P_{n-3} with (3,0,2); Q_n containing a marked vertex has (1,0,1). Finite recurrence-state transitions establish P_n mod 2 period 7, mod 4 period 14, and Q_n mod2 period 7, not an empirical extrapolation. Odd P_n makes all W odd; at n=8 mod14, character expansion modulo 4 yields W= P_n-2|b|Q_n=2 mod4. Explicit trace-zero seeds at n=4,9,11,15,16 cover singular residue representatives, and 7-letter transfer J with J^2=I extends seeds by 14. Boundary n=3 and unnormalized convention checked. Independent integer checks recomputed all five seed traces, J^2 and recurrence parity patterns; this is supplementary, not the all-n proof.

## originality

PASS

Unweighted Perrin counts equal the zero-frequency specialization only; their parity offers sufficient zero-free classes but not the exact cancellation/no-cancellation pattern for all signs. This law is not a restatement of those counting formulas. A general signed independence-domination polynomial specialized to ±1 could subsume the zero locus if one proved all values; no demonstrably dominating theorem found. Unexamined weighted-domination literature is residual risk. Prior cycle gap combinatorics is a structural premise, not a theorem about Fourier invertibility. Even P_n does not itself force zeros; n≡8 mod14 is a counterexample to that potential shortcut.

## value

PASS

Classifies singularity of the natural Boolean-group convolution by the entire maximal-independent-set indicator in every cycle length, with a mathematically distinctive even-mass but zero-free n=8 mod14 class. The transfer involution and mod-four obstruction constitute structural rather than artificial finite sampling information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
