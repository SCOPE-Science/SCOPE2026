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

Marking the j-cycle gives E[C_j]=s_(n-j)/(j s_n); marking the two different lengths leaves r labels and gives E[C_j C_k]=s_r/(jk s_n). The signed determinant required for covariance follows from strict opposite monotonicities of the even and odd partial-sum subsequences for mixed-parity offsets, and comparison to e^-1 when both offsets are odd. With both offsets even, the decrements d_t of u_t=s_(2t) satisfy d_t/d_(t+1)=(2t+1)(2t+4)>=4>u_(t+1)/u_(t+2), giving strict log-convexity. The positive increments c_t of v_t=s_(2t+1) decrease strictly, giving v_(t+1)^2-v_t v_(t+2)=v_(t+1)(c_t-c_(t+1))+c_t c_(t+1)>0. Products of adjacent ratios extend the resulting inequalities to arbitrary positive offsets, using ratios only at positive entries. The omitted endpoint explanation at v_0=s_1=0 is immediate: v_0 v_(h+l)=0<v_h v_l when h,l>0. This also explains why no logarithm at zero is required. The denominator is positive and the three sample fractions follow by substitution. Taylor's integral remainder has magnitude a_m=(m!)^-1 integral_0^1 exp(u-1)u^m du, asymptotic to 1/(m+1)!. For fixed j,k its r-indexed term dominates the three shifted remainders, giving the numerator's signed coefficient e^-1 and the covariance's coefficient e after division by s_n^2.

## originality

FAIL

A distinct published Resultary record, SCOPE-alternating-covariance-of-cycle-classes-in-uniform-derangements--f219fce56fec, already contains the same strict sign over the same uniform-derangement domain, the same signed leading factorial coefficient, and the same all-positive-offset determinant inequality. This is demonstrated coverage, not a possible overlap inferred from a title or date. The exact covariance identity separately follows from published general factorial moments. No distinct theorem remains in the frozen Finding.

## value

FAIL

The strict sign across all admissible sizes and the factorial-scale correction are meaningful for this natural conditioned permutation model. As a new result, however, this record repeats the same invariant, offset lemma and sharp correction already available in a distinct catalogue record. It does not identify a new regime, applicable extension, or materially different proof contribution; substituting a few small sizes in the known formula adds no scientific result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
