---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The exact residual recursion a_(2n+rho)=a_n+E[a_B]+rho for B~Bin(n,1/2) and base a_0=0,a_1=1 follows from pairwise XOR and conditionally unbiased equal-pair bits. The pointwise quadratic support z^alpha >= 1+alpha(z-1)-(z-1)^2 for z>=0 yields binomial concavity deficit <= (1/2)(n/2)^(alpha-1) <= 1-2^-n (n>=2); n=1 is direct. The strong induction with atom B=0 then proves the tighter lower envelope, Jensen proves the upper envelope including the odd case. Own independent rational recurrence reproduced a_1..a_8 and 1..300 finite inequalities; these are corroboration, not the infinite induction.

## originality

PASS

The previously published November 2 Resultary theorem already proves the very same expectation has Theta(N^alpha) growth and supplies bounds N^alpha/10+9/10 <= a_N <= 3N^alpha-2. Thus neither the recurrence, exponent nor existence of uniform constants is original. The new precise two-sided constants are strictly stronger for N>1 and are NOT logically implied by those prior bounds; a separate binomial deficit estimate and induction proves them. O=PASS is limited to this quantitative all-length strengthening, not the submitted overly broad novelty framing.

## value

PASS

Although the polynomial order and alpha are known, the specific all-N lower coefficient increases from 1/10 to 1/2 and the upper from 3 to 2 (with exact intercepts), providing a substantial quantitative extraction-loss guarantee for every input length. The sharper binomial-deficit inequality is a motivated technical improvement rather than a mere reparameterization; no optimality or new exponent is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
