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

Kitajima's defining equations and Lemma 2.1 specialize to the stated p=1 series and positive order-raising integral with the distorted angle. Expanding H_r and using (a^(2k+2)−b^(2k+2))/(a−b)=(a+b)Σ a^(2j)b^(2(k−j)), with a+b=1, verifies the fourth-order divided difference coefficient by coefficient, including axes by the removable limit at x=0 and the diagonal by differentiation. The derivative has numerator −F(rx) where F(t)=t(2+cos t)−3sin t. On 0<t<π, F'''(t)=t sin t>0 with F(0)=F'(0)=F''(0)=0, and for t≥π the bound F(t)≥t−3>0 applies. Thus H'_r(x)<0 for every x>0. The strict inequality for F''' need not and does not hold at t=π, an immaterial endpoint slip; the strict inequality for F does hold there. The order-raising formula follows directly by integrating the series using the beta integral, with compact convergence and integrable weight at t=1 for every positive raising increment. Its positive weight propagates the fourth-order strict sign. The axis witness at order 0 is the sinc at 3π/2; the diagonal limits at orders 1 and 2 are 4sin(r/2) and −8cos(r/2)+16sin(r/2)/r, giving −4 and −8; at a=2/5, b=3/5 and r=5π the order-3 numerator has contributions 0 and −2/b², giving −200/(9π) after the prefactor. The claim is correct as to the strict threshold among integers and real orders at least 4, without classifying other real orders in the frozen statement. The inspected CHECK.py is finite supplementary corroboration, not the continuum proof.

## originality

FAIL

The classification's sharp positivity threshold is materially covered by Berens–Xu's 1997 sharp ℓ1-Riesz positivity theorem: their d=2 case has δ≥3 for the same continuous Fourier kernel, which under the exact transform below is order ω=δ+1≥4. Even interpreting their 'positive' as only nonnegative, this implies the strict claim for every ω>4 by Kitajima's positive raising formula and the positive leading series term near r=0; their sharpness implies negative values at orders 1–3. The order-0 example is the elementary axis sinc. This is verified overlap with the central threshold, not a fail based on an inaccessible citation. The strict no-zero statement exactly at order 4 is a potential separate refinement, but the available prior theorem statement does not establish whether the prior proof already gives it. Its distinct originality has not been established, and the review does not assert it was proved earlier. Explicit witnesses and a short divided-difference derivation do not restore originality to the frozen threshold claim. No repaired finding is accepted.

## value

PASS

The sign classification addresses a natural critical order for a Fourier-derived kernel, with exact witnesses distinguishing the threshold and a strict statement that prevents zeros in any direction at the critical order. The all-radii and all-angles conclusion is mathematically meaningful; the proof gives an explicit mechanism rather than a numerical sign survey. This scientific relevance does not give the known threshold originality credit or establish independent novelty of the endpoint refinement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
