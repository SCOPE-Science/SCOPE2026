---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Conditioning on X_(k)=x splits the remaining data into the two independent truncated uniform samples. With m=k−1 and r=n−k, the pair-sum contributions are m(m+2)x/6, r(r+2)(1−x)/6 and mr/2. Normalization and centering give the stated slope and intercept. As an independent variance check, a single gap has variance 1/18, disjoint pairs give zero covariance, and two gaps sharing one observation have covariance Var(X²−X+1/2)=1/180. Thus Var(G_n)=[C(n,2)/18+6C(n,3)/180]/C(n,2)²=(n+3)/[45n(n−1)]. The beta order-statistic variance then gives the stated R²; the true conditional mean is affine, so this is optimal even without a linearity restriction. For N=n+1 the objective is N⁴/16−(t²−N²/2)²/4 with t=|2k−N|. The closest adjacent squares tie just when N²−2j²=2 with j=t+1; N even and j odd ensure parity. Every noninitial positive solution is admissible: it has j≥3, 4/3<N/j<3/2, and descent (3N−4j,3j−2N) gives smaller positive coordinates. The first post-initial pair is (10,7) and N−j≥3 thereafter, so t+2≤N−2. The solution at n=1 is excluded and t=0 cannot maximize for n≥2. The maximizers and limiting R² follow. The uploaded checker was inspected, not executed.

## originality

PASS

Credit only the explicit Gini-specific projection and explained-variance values, not generic uniform L-statistic affineness, a new optimizing score, or new limiting optimal fractions. The exact prior uniform sample-variance Pearson profile already has the identical finite optimizing score and therefore the same set of maximizing ranks and ties under the corresponding optimization. It does not give the Gini conditional projection or its exact explained fraction. The explicit Pell description is a deduction about that already available score, not independent evidence of a distinct optimizing phenomenon. No inspected source supplied the explicit Gini formulas for the same parent and prediction target.

## value

FAIL

The prediction question is natural, but the distinct Gini-specific numerical coefficients are routine substitutions of its linear order-statistic weights into the standard conditional uniform means and spacing moments. The proposed substantive optimizer gain is the four-way tie description: the earlier uniform sample-variance result already supplies the exact finite score, not merely its limit, and the tie criterion is the midpoint equality of two adjacent squared lattice values of that score followed by standard Pell descent. It gives no new rank-choice information beyond an elementary analysis of the available finite profile. The unrestricted-versus-linear interpretation is correct, but follows directly from the generic uniform L-statistic affine projection. In combination this does not establish a distinct result of sufficient scientific value at the stated scope; the decision is not based on the size of the sample checks or on the inaccessible Hosking text.

The dated certificate retains the supplied scientific assessment, sources and limitations.
