# Independent mathematical audit

## correctness

PASS

Periodic integration gives uniform margins. I checked the concordance normalization using independent uniform U and generator X, with V=(X−U) mod 1: E[UV|X=x]=1/6+x(1−x)/2. For ordered generator locations x≤y and d=y−x, integrating the two ordered triangles in the two uniform coordinates gives concordance probability y−(x²+y²+d²)/2+x(1−y)+d(1−d)=x(1−x)+y(1−y)+d−d². Averaging recovers the cited Kendall formula. With q=E[(X−1/2)²] and J the centered CDF squared norm, these formulas give r=1/2−6q and t=1−8q−4J. The CDF constraint follows by integration by parts. At r≤0, projecting the centered CDF on x−1/2 proves J≥(1+r)²/12; equality requires an affine CDF of slope 1+r and the density endpoint conditions force r=0. For each r<0 the two endpoint blocks have centered second moment 1/4−ε/2+ε²/3, so blending them with the full uniform at the stated weight fixes q exactly; dominated convergence gives the claimed supremum although the limiting endpoint atoms are inadmissible. For positive r, the centered-uniform CDF G has q=a²/3 and J=1/4−a/3. Subtracting the moment direction from the first variation leaves zero inside the interval and the correct signs on both saturated tails. The remaining squared norm can vanish only when F−G is constant, hence zero by continuity and endpoints. This gives uniqueness, the positive formula, and consistency at independence. The feasible endpoints r=−1 and 1/2 would require atomic generators and are properly excluded. The supplied checker was inspected, not run; the recorded exact finite assertions supplement the proof.

## originality

PASS

Credit the known exact rank identities, the unconditional Kendall maximum, the proportional bound, and the prior CDF variational method. The positive branch bound can in fact be obtained using the known iid Gini–standard-deviation inequality, not just at the prior global maximizing point. The supported distinct contribution is the full fixed-r envelope, in particular the sharp negative-r formula, nonattainment and approximation at each exactly fixed r, and the resulting change in attainment. No inspected stronger statement gave that result.

## value

PASS

Joint calibration of the two concordance coefficients in the same rotational density family is not determined by their separate ranges. In particular, at each prescribed negative Spearman value the precise Kendall upper limit is strictly stronger than the known proportional line and cannot be realized by a density, yet it is approached without changing the prescribed rank coefficient. The full boundary and the change from singular limits to smooth-in-the-interior uniform generators answer a natural constrained extremal question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
