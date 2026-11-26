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

With initial normalized height 1, the crossing near 2π of X=0 is transverse; analyticity and continuity of clockwise angle on compact annuli identify the return and its analytic dependence on A,B,C. For B=C=0, reflection in the section is a reversor; the two distinct fixed-axis crossings yield a closed orbit by reversing the segment, so Q(A,0,0)=1 exactly. Differentiating the energy integral at the harmonic circle gives Q_B=−I_m and Q_C=−I_n, with no endpoint contribution because the unperturbed energy derivative is zero. Factoring out B,C leaves analytic coefficient functions, hence with r=δu and (A,B,C)=(a1 δ^(2N−1) u^(2N−1),−δ^(2n)u^(2m),δ^(2n)u^(2n)) the scaled remainder is o(δ^(2n)) also after one u derivative, uniformly on positive compacts. For the Euler limit take a slightly larger compact around the exact trajectory between u0 and u_*; discrete Grönwall up to first exit bounds the error by o(1) on each finite slow-time interval and prevents exit. The simple root with G'(u_*)=−2(n−m)I_n u_*^(2n) gives the attracting fixed point, the nontrivial transverse multiplier, and the analytic crossing time tends to 2π in physical time. Chen–Lu–Wang–Zhang arXiv:2611.19873v1 verifies global uniqueness for the exact exponents, a1≠0 and a2<0; it is not invoked at a2=0. At criticality the analytic expansion gives positive strictly decreasing returns with no positive fixed point locally, and successive increments of r_k^(−2n) tend to 2nI_n. Independently evaluated I_2/π=5/8, I_3/π=35/64, giving the printed example's constants. Frozen numerical script inspected but not executed; convergence and uniform quantifiers are analytic, not supported by extrapolating those finite tests.

## originality

PASS

The established global count is credited to the exact same-family 2026 theorem. Established focal-constant methods and an earlier cubic relaxation law overlap in tools or subphenomena. On checked evidence the distinct contribution is the matched compact-uniform C¹ return and finite-slow-time dynamics, with leading amplitude and stability constants and the critical iteration law for this higher-power path, not a new general averaging or weak-focus theorem.

## value

PASS

The singular limit is natural at the birth of the already classified stable cycle. It explains why even-power terms of parametrically larger size do not mask the leading drift, predicts the transient over a diverging number of turns, and gives sharp selection and stability constants and critical slowing. This adds quantifiable dynamics to the qualitative count; it is not a claim of general unfolding, unbounded slow-time uniformity or a full basin description.

The dated certificate retains the supplied scientific assessment, sources and limitations.
