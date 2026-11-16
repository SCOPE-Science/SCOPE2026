# Sharp lacunarity cutoff for a one-jump close-to-convex family

## Finding
For integers \(p,N\ge1\), let
\[
F_{p,N}(z)=\int_0^z\frac{1+t^{pN}}{1-t^p}\,dt,\qquad |z|<1.
\]
Then \(F_{p,N}\) is close-to-convex on the unit disk **if and only if** \(p\le2\) or \(N=1\). The first coefficient jump, already at \(N=2\), obstructs close-to-convexity for every \(p\ge3\).

## Assumptions and scope
Here \(p\) and \(N\) are positive integers; close-to-convexity means the standard analytic geometric property, equivalent for locally univalent disk maps to Kaplan's boundary-turn condition. The Taylor series is
\[
F_{p,N}(z)=z+\sum_{k=1}^{N-1}\frac{z^{pk+1}}{pk+1}
+2\sum_{k=N}^{\infty}\frac{z^{pk+1}}{pk+1}.
\]
Thus the normalized lacunary derivative coefficients are \(c_0=1\), \(c_k=1\) for \(1\le k<N\), and \(c_k=2\) for \(k\ge N\): they are nondecreasing, nonnegative, and tend to two. This is an analytic subfamily (zero coanalytic part) of the coefficient setting in Prajapat's 2026 monotonicity theorem. No assertion about failure of univalence is made on the non-close-to-convex side.

## Proof
**Positive cases.** If \(N=1\), then \(F_{p,1}'(z)=(1+z^p)/(1-z^p)\) has positive real part for every \(|z|<1\). Hence \(F_{p,1}\) is close-to-convex relative to the identity map.

For \(p=1\) or \(p=2\), put \(\phi_p(z)=\int_0^z(1-t^p)^{-1}\,dt\). This map is convex because
\[
\operatorname{Re}\!\left(1+\frac{z\phi_p''(z)}{\phi_p'(z)}\right)
=\operatorname{Re}\!\left(1+\frac{p z^p}{1-z^p}\right)>0
\]
for \(p\in\{1,2\}\) and \(|z|<1\). Also
\[
\operatorname{Re}\frac{F_{p,N}'(z)}{\phi_p'(z)}
=\operatorname{Re}(1+z^{pN})>0.
\]
This proves close-to-convexity by its standard convex-comparison criterion, independently of the quoted coefficient theorem.

**Negative cases.** Fix \(p\ge3\) and \(N\ge2\). The derivative \(F_{p,N}'\) is nonzero throughout the open unit disk. On the open boundary sector \(0<\theta<2\pi/p\), away from zeros of the numerator, direct factorization gives
\[
e^{i\theta}F_{p,N}'(e^{i\theta})
=i\,e^{iL\theta}\frac{\cos(pN\theta/2)}{\sin(p\theta/2)},
\qquad L=1+\frac{p(N-1)}2.
\]
The denominator sine is positive throughout that sector. The first two simple numerator zero angles are \(\alpha=\pi/(pN)\) and \(\beta=3\pi/(pN)\), both strictly inside the sector. For radii \(r\uparrow1\), the continuously unwrapped argument of \(re^{i\theta}F_{p,N}'(re^{i\theta})\) loses \(\pi\) at each of these two crossings, while its smooth angular slope between crossings tends to \(L\). This sign of the jump follows directly from \(1+r^{pN}e^{ipN\theta}\), whose argument crosses from nearly \(+\pi/2\) to nearly \(-\pi/2\) as each boundary zero is crossed; the denominator has no zero on the selected arc.

Choose
\[
\eta=\frac{(1-2/p)\pi}{4NL}>0,\qquad
\theta_1=\alpha-\eta,\quad\theta_2=\beta+\eta.
\]
These angles remain in \((0,2\pi/p)\), and \(\theta_2-\theta_1<2\pi\). The limiting angular turn along this arc is
\[
\lim_{r\uparrow1}\int_{\theta_1}^{\theta_2}
\operatorname{Re}\!\left(1+\frac{zF_{p,N}''(z)}{F_{p,N}'(z)}\right)_{z=re^{i\theta}}\,d\theta
=L\left(\frac{2\pi}{pN}+2\eta\right)-2\pi
=-\pi-\frac{(1-2/p)\pi}{2N}<-\pi.
\]
The equality is justified by continuous boundary convergence at the two endpoints and by unwrapping the argument along the arc; the zeros occur only on the boundary, not for \(r<1\). Thus for all sufficiently large \(r<1\) the turn is less than \(-\pi\). Kaplan's necessary close-to-convexity criterion forbids this, proving that \(F_{p,N}\) is not close-to-convex. Together the positive and negative cases complete the classification.

## Verification
The accompanying standalone `CHECK.py` checks the exact coefficient expansion, the sector endpoints, and the negative finite-radius turn for a grid of integer \(p,N\). These numerical checks are illustrative; the all-parameter assertion follows from the preceding analytic argument. Reproduce with `python CHECK.py` using Python 3 and NumPy.

## Relationship to prior work
Prajapat, *Monotonicity and bounded variation for harmonic mappings with applications to special functions* (arXiv:2611.02290v1, November 1, 2026), Theorem 2.1, proves a monotone-coefficient sufficient condition for lacunarity \(p=1\) or \(2\). The positive half of the present classification is an explicit specialization; it is not new by itself. The new conclusion is the exact obstruction for every \(p\ge3\) already in a one-jump analytic family, together with the exceptional \(N=1\) case. Kaplan's angular-turning characterization is classical. The coefficient-monotonicity precursors of MacGregor (1969) and Sahoo–Wankhede (2025/2026) provide context; no contrary higher-lacunarity theorem was located in accessible material.

## Limitations
Failure of close-to-convexity does **not** imply failure of injectivity. This theorem does not classify univalence of \(F_{p,N}\), nor all coefficient-monotone lacunary analytic functions. A related older paper by Sahoo and Wankhede was available only in metadata and abstract; full-text comparison could not be completed. The result has not received independent audit.

## References
1. J. K. Prajapat, *Monotonicity and bounded variation for harmonic mappings with applications to special functions*, arXiv:2611.02290v1 (2026-11-01), Theorem 2.1, https://arxiv.org/pdf/2611.02290.
2. V. V. Goryainov, O. S. Kudryavtseva, A. P. Solodov, *Iterates of holomorphic maps, fixed points, and domains of univalence*, Russian Math. Surveys **77** (2022), Theorem 15 (Kaplan's criterion), https://doi.org/10.4213/rm10072e.
3. T. H. MacGregor, *Univalent power series whose coefficients have monotonic properties*, Math. Z. **112** (1969), 222–228, https://doi.org/10.1007/BF01110223.
4. S. K. Sahoo and S. Wankhede, *Monotone coefficients of univalent harmonic functions with applications to special functions*, J. Math. Anal. Appl. **554** (2026), 129898, https://doi.org/10.1016/j.jmaa.2025.129898.
