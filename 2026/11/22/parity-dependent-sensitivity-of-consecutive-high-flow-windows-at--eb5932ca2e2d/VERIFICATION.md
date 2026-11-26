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

With v=1-s and r=(1-pi)/pi, the two-state WW-killed kernel has trace 1-v/r and determinant -v^2/r. Thus A_(N+2)=(1-v/r)A_(N+1)+(v^2/r)A_N for A_N=1-F_N, with A_1=1 and A_2=1-pi*s. At s=s0 (v=r), A_(2m)=2*pi*r^m and A_(2m+1)=r^m. Differentiating the recurrence there gives D_(N+2)=r*D_N+A_(N+1)/r-2*A_N for D_N=A'_N, with D_1=0 and D_2=-pi. Solving separately in each parity gives precisely the two claimed derivatives after negation, including m=1. The criterion is conditional, not unconditional sign alternation: the even derivative is negative only for pi>pi_m. The same recurrence gives F_4=pi*s*(3-2s) and the stated cubic factor in F'_5. Its G'_pi is strictly positive on the admissible interval: for pi<=6/7 use s(1-s)<=1/4 (equality in the resulting bound at pi=6/7 could only occur at an inadmissible s=1/2), and for pi>6/7 minimize G'_pi at s0>1/2, where (10*pi^2-15*pi+6)/pi>0. F'_5 has the stated strict opposite signs at the endpoints; clipping the separate four-day parabola and using strict concavity for five days proves both global results.

## originality

PASS

The probability and fair-chain extrema have identifiable precedents; the distinguishing classification holds at varying persistence under an unequal stationary marginal and is not given by those fair-chain conclusions or by the inspected general run probabilities alone.

## value

PASS

At fixed frequency, greater wet persistence can initially reduce the chance of any wet pair for sufficiently wet even horizons, despite strictly increasing it for all odd horizons at the same boundary. The explicit threshold sequence and the four-versus-five day change in optimizer status quantify when relying on persistence alone gives the wrong intuition; they give a sharp benchmark for constrained Markov run risk.

The dated certificate retains the supplied scientific assessment, sources and limitations.
