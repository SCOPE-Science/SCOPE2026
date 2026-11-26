---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The frozen Step 3 is false where it claims strict speed inequality at c=0: both rates are s there. In repairs/3/RESULT.md the endpoint argument instead integrates f_K/f_L along the K-trajectory. For every positive time the trajectory is strictly positive and f_K/f_L>1 there, so δ(0)>a rigorously, without a strict inequality at the initial point. No hypothesis or conclusion has been dropped. Re-audited the repaired proof: differentiating the primitive gives 1/f_H and its monotone inverse conjugates the L-flow to translation. The ratio is 1+k(K−L)c/[(K+c)(sL+wc)], where w=s−k; its divided difference has sign sKL−wcy. Taking y=F_K^a(c) and using the strict increase of cF_K^a(c) gives precisely one maximum z₀ of the displacement. The ratio tends uniformly to 1 along a fixed-time trajectory as its inlet tends to infinity, so δ tends to a, establishing the unique positive b_c through δ(b_c)=δ(0). For the outlet-coordinate difference δ(z+b)−δ(z), the same-side signs are immediate and the sign changes at most once across the maximum since the derivative there is negative. The sign at z=0 separates all three regimes and gives the sole boundary tie. At the interior root the implicit derivative is negative; the straddling inequalities and continuity give the two endpoint limits. Independently bisected the repaired equations at 50-digit working precision for (s,k,K,L,a)=(2,1,4,1,1), obtaining z₀≈1.4180063940276094, b_c≈8.1850904349017187 and x_*(1)≈1.5621163376635477. The accompanying numerical evidence was read without executing the uploaded script. The displayed b is residence time, not physical length without a specified velocity.

## originality

PASS

Reassessed the corrected manuscript. The identifiable contribution remains the joint inlet and second-residence-time classification for exact continuously loaded Monod flow with a common source above both removal maxima. The closest located exact comparisons use finite-step maps, a discrete source jump, or a different continuous objective. The literature assessment is bounded.

## value

PASS

Even though the low-affinity stage has the higher local net rate at every positive concentration, this pointwise inequality does not settle order. For fixed first-stage residence time, the theorem gives precisely when a finite inlet crossover exists, in which direction the recommended order changes, and when the crossover reaches zero. This resolves an exact design question within a stylized monotone model rather than extrapolating empirical water-quality effects. The endpoint correction preserves those conclusions and their value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
