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

With N=2^n and s/N the target slope, the reversed column bits are independent selectors of coefficients e_i=(b_i-x_i)/2, x_0=0, x_{i+1}=(x_i+b_i)/2. Their sum is s/N by telescoping the offset at t=N-1. Thus the positive maximum P(s) is at least the magnitude Q(s) of the negative minimum, and the column with reversed slope bits attains P(s) by selecting all positive coefficients. For optimization over slope bits, the two affine Bellman candidates from state x intersect at x=1/2, with difference (1-u_{m-1})(1/2-x), where u_1=1/2 and u_m=1-u_{m-1}/2. This proves the asserted piecewise affine form inductively, including ties and endpoints. The intercept recurrence a_1=1/2 and a_m=a_{m-1}+(1-u_{m-1})/2 yields V_n(0)=n/6+7/18+(-1)^n/(9·2^n), with an admissible optimizing bit word. It holds also for n=1 and zero slope. This is entirely consistent with the independent exact discrepancy identification recorded under originality. The faulty historical comparison is not required for the proof.

## originality

FAIL

There is positive earlier coverage of both proposed contributions. The sharp finite correction is exactly half the classical Béjian–Faure maximum of scaled van der Corput discrepancy on the dyadic interval. The per-slope profile and bit-reversed witness also follow directly from the exact chord profile of Smirnov–Karpenko, by a coefficient sign-preserving normalization change. Rim's coarse n/2 bound at the same normalization is not the strongest prior comparison. This is a coverage failure, not an argument from a failed search or inaccessible paper.

## value

FAIL

Exact row errors at the s/N slope would be a useful sampling tolerance if the invariant were previously unknown. Here the finite sharp value is an exact change of variables from a known extremum, and the entire slope-specific profile and witness are routine transfers of the existing chord formula. A self-contained Bellman rederivation does not leave a distinct mathematical result under review, and no further computational enclosure, application theorem or new extremal characterization is established by the frozen claim. No surviving repair is warranted for these submitted claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
