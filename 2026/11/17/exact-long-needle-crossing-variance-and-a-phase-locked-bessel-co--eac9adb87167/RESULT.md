# Exact long-needle crossing variance and a phase-locked Bessel correction on rectangular grids

## Finding
Let a segment of length \(L>0\) have independent uniform orientation and uniform position modulo a rectangular grid of horizontal and vertical spacings \(a,b>0\). Let \(N_L\) be its total number of grid-line crossings, counting each crossed line once. The count of visited open grid tiles is \(N_L+1\) almost surely, and hence has the same variance.

Define
\[
K_{a,b}=\left(\frac12-\frac4{\pi^2}\right)\left(\frac1{a^2}+\frac1{b^2}\right)
+\left(\frac2\pi-\frac8{\pi^2}\right)\frac1{ab}.
\]
For **every** \(L,a,b>0\),
\[
\boxed{\operatorname{Var}(N_L)
=K_{a,b}L^2+\frac13
-\frac1{\pi^2}\sum_{k=1}^{\infty}\frac{J_0(2\pi kL/a)+J_0(2\pi kL/b)}{k^2}.}
\]
Here \(J_0\) is the Bessel function of the first kind of order zero. The series is absolutely convergent. Additionally, if \(N_x\) and \(N_y\) are the numbers of crossings of the two perpendicular line families, then
\[
\mathbb E N_L=\frac{2L}{\pi}\left(\frac1a+\frac1b\right),\qquad
\operatorname{Cov}(N_x,N_y)
=\frac{L^2}{ab}\left(\frac1\pi-\frac4{\pi^2}\right)<0.
\]
Thus the covariance of the two crossing counts is exactly quadratic even though each marginal variance has nontrivial oscillations.

Define the continuous, one-periodic, absolutely convergent series
\[
S(x)=\sum_{k=1}^{\infty}\frac{\cos(2\pi kx-\pi/4)}{k^{5/2}}.
\]
For fixed positive grid spacings, as \(L\to\infty\),
\[
\boxed{\operatorname{Var}(N_L)=K_{a,b}L^2+\frac13
-\frac{\sqrt a\,S(L/a)+\sqrt b\,S(L/b)}{\pi^3\sqrt L}
+O_{a,b}(L^{-3/2}).}
\]
In particular, for the unit square grid, let \(K=1+2/\pi-16/\pi^2\), \(\zeta\) denote the Riemann zeta function, and \(\eta(s)=(1-2^{1-s})\zeta(s)\). Then the normalized variance remainders have **distinct, oppositely signed** limits along integer and half-integer lengths:
\[
\lim_{m\to\infty}\sqrt m\left[\operatorname{Var}(N_m)-Km^2-\frac13\right]
=-\frac{\sqrt2\,\zeta(5/2)}{\pi^3},
\]
\[
\lim_{m\to\infty}\sqrt{m+1/2}\left[\operatorname{Var}(N_{m+1/2})-K(m+1/2)^2-\frac13\right]
=\frac{\sqrt2\,\eta(5/2)}{\pi^3}.
\]
The variance therefore has a genuine phase-sensitive correction, not an ordinary nonoscillatory third term.

## Assumptions and scope
The grid is the union of vertical lines \(x=ja\) and horizontal lines \(y=kb\) for integers \(j,k\). An endpoint is chosen uniformly from one fundamental tile \([0,a)\times[0,b)\), independently of an angle uniform on \([0,2\pi)\); the other endpoint is displaced by the length-\(L\) vector at that angle. Choosing the midpoint instead gives the same probability law. Grid vertices and coincident segment/grid-line alignments have probability zero, so multiplicities and tangencies need no exceptional convention. There is no restriction relating \(L\) to the spacings. The large-length statement holds for each *fixed* \(a,b>0\), with a constant depending on those spacings.

## Proof
Write \(X,Y\) for independent uniform fractional starting coordinates, both in \([0,1)\), and let \(\Theta\) be the independent orientation. The two projected absolute lengths in units of grid spacing are
\[
u=\frac{L|\cos\Theta|}{a},\qquad v=\frac{L|\sin\Theta|}{b}.
\]
For a line family, the number of crossed lines, conditionally on projected length \(u\), has the distribution of \(\lfloor u\rfloor+B\), where \(B\) is Bernoulli with success probability \(\{u\}\). (Translate the segment along that coordinate by an independent uniform phase; reversing direction does not change the distribution.) Consequently, conditional on \(\Theta\), the two line-family crossing counts are independent and have means \(u,v\) and variances \(g(u),g(v)\), where
\[
g(t)=\{t\}\bigl(1-\{t\}\bigr).
\]
The law of total variance therefore gives
\[
\operatorname{Var}(N_L)
=\operatorname{Var}(u+v)+\mathbb E\bigl[g(u)+g(v)\bigr].
\]
The elementary angular identities
\[
\mathbb E|\cos\Theta|=\mathbb E|\sin\Theta|=\frac2\pi,\quad
\mathbb E\cos^2\Theta=\mathbb E\sin^2\Theta=\frac12,\quad
\mathbb E|\sin\Theta\cos\Theta|=\frac1\pi
\]
show that \(\operatorname{Var}(u+v)=K_{a,b}L^2\), and also give the displayed mean and the exact negative covariance of the separate line-family counts. Note that the last covariance contains no conditional translation covariance, because the two phase coordinates are independent at fixed angle.

The periodic function \(g\) has the uniformly and absolutely convergent Fourier series
\[
g(t)=\frac16-\frac1{\pi^2}\sum_{k=1}^{\infty}\frac{\cos(2\pi kt)}{k^2}
\]
including at integer arguments (where both sides vanish). The integral identity
\[
J_0(z)=\frac1{2\pi}\int_0^{2\pi}\cos(z\cos\theta)\,d\theta
\]
and invariance of orientation under quarter-turns imply
\[
\mathbb E\cos(2\pi ku)=J_0(2\pi kL/a),\qquad
\mathbb E\cos(2\pi kv)=J_0(2\pi kL/b).
\]
Uniform absolute convergence permits expectation term by term. This proves the exact formula, including the constant \(2(1/6)=1/3\).

For the large-length formula, use the standard uniform real-axis Bessel expansion
\[
J_0(z)=\sqrt{\frac2{\pi z}}\cos(z-\pi/4)+O(z^{-3/2})
\qquad(z\to+\infty).
\]
For each fixed grid spacing, the Bessel arguments \(2\pi kL/a\) and \(2\pi kL/b\) are uniformly large for all integers \(k\ge1\) as \(L\to\infty\). On multiplying by \(k^{-2}\), the errors sum absolutely to \(O_{a,b}(L^{-3/2}\sum_{k\ge1}k^{-7/2})\). The leading terms combine exactly into the two periodic functions \(S(L/a)\) and \(S(L/b)\), establishing the claimed remainder bound.

If \(a=b=1\), then \(S(m)=\zeta(5/2)/\sqrt2\) for integers \(m\), while \(S(m+1/2)=-\eta(5/2)/\sqrt2\). Substitution in the expansion yields the two nonzero limits. Their opposite signs rule out a single nonoscillatory coefficient of order \(L^{-1/2}\). All statements follow.

## Verification
Run the accompanying `check.py` with Python, NumPy and SciPy. The executable independently evaluates the conditional fractional-part variance by splitting the angular integral at every integer projection threshold, compares this quadrature to a truncated Bessel series for seven length/grid configurations, checks the classical short-needle polynomial, and compares four direct endpoint-based Monte Carlo samples of 500,000 needles each with predicted means and variances. It also verifies the phase-sensitive asymptotic at integer and half-integer lengths 10, 50 and 100. The observed completion marker was `LONG_BUFFON_GRID_VARIANCE_OK`.

As an exact cross-check, when \(L\le\min(a,b)\) there are at most two line intersections; the classical short-needle probabilities yield
\[
\operatorname{Var}(N_L)
=\frac{2L}{\pi}\left(\frac1a+\frac1b\right)
+\frac{2L^2}{\pi ab}
-\left[\frac{2L}{\pi}\left(\frac1a+\frac1b\right)\right]^2.
\]
The Bessel identity agrees with this elementary formula on its full validity range. All finite computation is corroboration; the proof is the analytic argument above.

## Relationship to prior work
Classical Buffon–Laplace theory handles the short-needle crossing probabilities. Siniksaran (2009) discusses short-needle estimation on single and multiple grids. Diaconis (1976) derives a crossing-count distribution and approximate large-length moments **for one family of parallel lines**. Mendo and Arkhipov (2022/2023) establish the mean number and maximum tile count on arbitrary rectangular grids, but not their variance. Min, Zhu and Zhao (2024) derive long-needle grid-contact probabilities, an event indicator rather than the total crossing count. Bäsel (2025) derives a multidimensional variance only under the short-needle restriction \(L\le\min(a,b)\). The present result isolates the variance of the unrestricted **two-family total crossing count**, its exact negative cross-family covariance, and its sharp Bessel-induced length-phase correction. These claims are mathematical comparisons, not a guarantee of complete historical priority.

## Limitations
The variance formula applies to a deterministic-length straight needle with uniform orientation and uniform independent phase in an infinite rectangular grid; it does not cover length randomness, nonorthogonal grids, biased orientations, or dependent phase coordinates. The large-length error is for fixed \(a,b\) and is not claimed uniformly as grid spacings degenerate. The exact parallel-line variance and related asymptotics may occur in older literature; Diaconis's full 1976 article and some historical monographs were inaccessible, so historical priority for the two-family phase correction requires independent checking. No independent audit has been performed.

## References
1. E. Siniksaran, "Throwing Buffon's Needle with Mathematica," *The Mathematica Journal*, vol. 11, no. 1, publicly available online 2009-01-12. https://www.mathematica-journal.com/2009/01/12/throwing-buffons-needle-with-mathematica/
2. P. Diaconis, "Buffon's problem with a long needle," *Journal of Applied Probability* **13** (1976), 614–618. https://doi.org/10.2307/3212484
3. L. Mendo and A. Arkhipov, "On the number of tiles visited by a line segment on a rectangular grid," arXiv:2201.03975 (2022); *Mathematika* **69** (2023), 1242–1281. https://arxiv.org/abs/2201.03975
4. Y.-J. Min, D.-Q. Zhu and J.-H. Zhao, "Buffon-Laplace Needle Problem as a geometric probabilistic approach to filtration process," arXiv:2402.06670 (2024). https://arxiv.org/abs/2402.06670
5. U. Bäsel, "The probabilities for the number of intersections in the Buffon-Laplace needle problem in \(\mathbb R^d\)," arXiv:2508.04640 (2025). https://arxiv.org/abs/2508.04640
