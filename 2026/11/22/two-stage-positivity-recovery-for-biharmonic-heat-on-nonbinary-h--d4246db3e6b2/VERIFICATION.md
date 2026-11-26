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

The frozen Finding incorrectly says every other off-diagonal entry is positive at either threshold. At T_(2,q), u=rho_q>rho_* and F_3(u)<0, so the distance-three entries are still strictly negative. The complete corrected RESULT.md in /workspace/repairs/1 explicitly lists both threshold signs and removes an ambiguous interval description; at T_(3,q) the other two off-diagonal shells really are positive. I rederived the distance-r entry from the coefficient of z^k in (1-z)^r(1+(q-1)z)^(3-r), weighted by u^(k²)/q³: each coordinate eigenvalue is 0 or q. For r=1, replacing the negative u⁹ term by negative u⁴ gives the stated positive lower bound, and r=0 is positive. The factored F_3 has one interior zero by strict quintic monotonicity; F_2 has exactly two simple positive zeros by Descartes, F_2(0)=1, and F_2'(1)=2q>0 at its known zero u=1. At rho_*<1/2, F_2=F_3+q(u-2u⁴+u⁹)>0, ordering the zeros. The positive row sum is exactly one, so summing negative mass over shell multiplicities gives the induced infinity norm, and symmetry gives the one-norm. Descartes and the sign near 1 give the unique interior zero sigma of 1-2u³+u⁸; F_2(sigma)=F_3(sigma)<0 and F_2 increases in q at rho_q, yielding rho_q increasing to sigma. The independent bounded replay python /workspace/reproduce_frozen.py confirms the shell and factor identities and the stated far/limit decimals. The proof, not this replay, supplies the all-q statements. Frozen numerical checker inspected, not run.

## originality

PASS

Best of current knowledge, the corrected distinctive claim is the exact nonbinary three-factor semigroup shell ordering and its whole positivity/norm law, with different alphabet dependence at the two recoveries. Tensor spectral calculus, eventual positivity, lower-factor examples and Boolean-cube recoveries are credited. The corrected source identifies the distinct Boolean finding without claiming priority from its date.

## value

PASS

Three factors are the first product with a distance-three shell and hence the first opportunity for two distinct off-diagonal recoveries. The result certifies the whole interval where sign and maximum-norm contraction fail, with an exact normalized last cutoff and a first cutoff whose alphabet dependence is genuinely different. Neither qualitative eventual positivity nor the known exact two-factor result answers that finite threshold question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
