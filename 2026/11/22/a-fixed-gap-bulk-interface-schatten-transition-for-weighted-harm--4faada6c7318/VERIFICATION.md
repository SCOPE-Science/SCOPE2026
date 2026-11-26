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

Radial integration gives μ_j=β B(j+1,β), with μ_0=1. On the unnormalized mode r^|j| e^(ijθ), projection after z^a multiplication yields the one coefficient μ_[(a+|j|+|j+a|)/2]/μ_|j+a|. Composing and normalizing gives all three coefficient branches including k=n,m. Both ordered products telescope on each tail (j≥0 and j≤−(2n+d)); reflection k→2n+d−k negates the normalized coefficient and forces the midpoint to vanish if integral. Distinct output modes give exactly the singular-value list. An independent Python Fraction diagnostic constructed the moments with μ_j/μ_(j−1)=j/(j+β), worked on unnormalized Fourier modes, and compared the two products with the three branches after removing the common normalization sqrt(μ_(2n+d−k)/μ_k). It agreed exactly on all 6048 checks for β=1/5,1/2,4/5, n=1..12, d=1..7 and −3≤k≤2n+d+3, including antisymmetry after clearing the square roots. The frozen checker was read, not run. For the infinite limit a useful independent reconstruction avoids differentiation: with F_l(k)=μ_l/μ_(l−k), the exact quotient F_(l+1)/F_l is 1+βk/[(l+1+β)(l−k+1)] for l≥k. Summing these d increments at l=n..n+d−1 and multiplying by the moment square-root prefactor gives the left branch with a minus sign. Gamma ratios show F_l≤C((l−k+1)/(l+1))^β and the square root is bounded there. Thus k=n−u gives the uniform bound C n^(−β)(1+u)^(β−1); reflection and the finitely many intermediate modes give the global bound. For t=k/n in a compact subset of (0,1), the same increments give nc/d→−β t(1−t)^(β−1)(t/(2−t))^(β/2). To justify the bulk Riemann sum rigorously, trim both ends of the left interval: the interface near t=1 costs O(ε^(1−p(1−β))) in rescaled mass, and near t=0 the uniform bound gives |c|≤C/n and hence O(ε). This supplies the endpoint detail implicit in Step 3. For fixed signed r=k−n, the three branches give n^βc→Gβ(|r|)−Gβ(|d−r|). The differences Gβ(j+1)−Gβ(j)=βGβ(j)/(j+1) are positive and decreasing and ∼βj^(β−1), so the tail gives exactly the stated convergence threshold and the maximum occurs at r=0,d. The same majorant yields dominated convergence of the upper-regime mass and tightness of the scaled maximum. In the critical region R≤u≤εn the exact increments have F_l=(u/n)^β[1+O(1/u+u/n)], the prefactor is 1+O((u+1)/n), and βk/[(l+1+β)(l−k+1)]=(β/u)[1+O(1/u+u/n)]. This proves the required uniform intermediate law. Reflection shifts u by the fixed d only; each tail contributes the same harmonic log coefficient. At fixed R,ε the central and outer strips have O(1) mass after n^(βp) scaling, so the two-sided coefficient is 2(βd)^p. All results require fixed d,β,p and measure asymptotic mass, not membership of individual finite-rank operators.

## originality

PASS

Best of knowledge for the fixed-positive-gap asymptotic theorem, not for the Fourier coefficient representation, finite rank, reflection, or the finite-rank mechanism. It is important that the two-degree regime does not just substitute ratio one into the positive fixed-ratio result.

## value

PASS

The fixed integer difference is the natural neighboring-degree limit where the established fixed-ratio profile degenerates. The finding determines which spectral modes carry each Schatten mass, including the borderline residue and the nonzero trace norm despite operator norm going to zero. Exact gamma constants and a proof of the change of scale provide new spectral information beyond the algebraic finite support.

The dated certificate retains the supplied scientific assessment, sources and limitations.
