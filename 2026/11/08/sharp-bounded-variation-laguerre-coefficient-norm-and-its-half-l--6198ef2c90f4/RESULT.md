# Sharp bounded-variation Laguerre coefficient norm and its half-line localization

## Finding
For the ordinary Laguerre polynomials \(L_n=L_n^{(0)}\), normalized by \(L_n(0)=1\) and orthonormal in \(L^2([0,\infty),e^{-x}\,dx)\), let \(n\ge 1\) and define
\[
F_n(x)=\int_0^x e^{-t}L_n(t)\,dt,\qquad M_n=\sup_{x\ge0}|F_n(x)|.
\]
The *exact* optimal bounded-variation-to-coefficient constant is \(M_n\): for every complex-valued function \(f\) of finite total variation on the half-line,
\[
\left|\int_0^\infty f(x)e^{-x}L_n(x)\,dx\right|\le M_n\,\operatorname{Var}_{[0,\infty)}(f),
\]
and the factor cannot be decreased (single-jump functions attain equality).

There is an explicit finite-degree two-candidate rule. Let \(Z_n\) be the set of the \(n\) positive zeros of \(L_n\), and let \(z_{n,-}\) be the largest zero at most \(1/2\), if any, and \(z_{n,+}\) the smallest zero at least \(1/2\), if any. Then
\[
M_n=\max_{z\in \{z_{n,-},z_{n,+}\}\,\text{defined}}
\left|\frac{z e^{-z}}{n}L_{n-1}^{(1)}(z)\right|.
\]
Finally, the sharp global asymptotic is
\[
\boxed{\displaystyle \lim_{n\to\infty}n^{3/4}M_n=
\frac{e^{-1/4}}{2^{1/4}\sqrt\pi}=0.369482560207115\ldots .}
\]
Every sequence of global maximizing locations \(x_n\in\operatorname{argmax}_{x\ge0}|F_n(x)|\) satisfies \(x_n\to1/2\). These are uniform-in-jump-location results, not merely bounds for each fixed jump position.

## Assumptions and scope
We use the conventional Laguerre normalization \(L_n^{(\alpha)}(0)=\binom{n+\alpha}{n}\), so \(\int_0^\infty e^{-x}L_n(x)L_m(x)\,dx=\delta_{nm}\). The coefficient is defined for bounded finite-variation functions; every such function has finite limits and is integrable against the stated weight. The variation is total variation on \([0,\infty)\). The theorem concerns integer degrees \(n\ge1\) and parameter \(\alpha=0\) only. No common maximizer is required for all degrees.

## Proof
**1. Primitive and normalization.** Classical Laguerre differentiation yields
\[
F_n'(x)=e^{-x}L_n(x),\qquad
F_n(x)=\frac{x e^{-x}}{n}L_{n-1}^{(1)}(x).
\]
The latter follows because differentiating its right side gives \(e^{-x}L_n(x)\) and it vanishes at zero. Both \(F_n(0)\) and \(\lim_{x\to\infty}F_n(x)\) vanish; the latter also follows from orthogonality to \(L_0=1\). Integration by parts in the Stieltjes sense gives
\[
\int_0^\infty f(x)F_n'(x)\,dx=-\int_{[0,\infty)}F_n(x)\,df(x),
\]
so its modulus is at most \(M_n\operatorname{Var}(f)\). For \(f=\mathbf 1_{[z,\infty)}\) with \(|F_n(z)|=M_n\), the coefficient is \(-F_n(z)\) and \(\operatorname{Var}(f)=1\), proving optimality. The harmless choice of the function's value at the jump does not affect either quantity.

**2. Exact global envelope.** The identity \(L_n'=-L_{n-1}^{(1)}\) gives
\[
F_n''(x)+F_n'(x)+\frac{n}{x}F_n(x)=0,\qquad x>0.
\]
Define the nonnegative Sonin-type envelope
\[
S_n(x)=F_n(x)^2+\frac{x}{n}F_n'(x)^2.
\]
A direct derivative, using the preceding equation, proves the **exact identity**
\[
\boxed{S_n'(x)=\frac{1-2x}{n}F_n'(x)^2.}
\]
Thus \(S_n\) is strictly increasing on \((0,1/2)\) and strictly decreasing on \((1/2,\infty)\), with a unique global envelope maximum at \(1/2\). In particular \(F_n(x)^2\le S_n(x)\le S_n(1/2)\) for all \(x\ge0\).

Any global maximum of \(|F_n|\) occurs at some positive zero of \(F_n'=e^{-x}L_n\), since \(F_n\) vanishes at both endpoints and is not zero identically. At every such zero \(z\), one has \(S_n(z)=F_n(z)^2\). On each side of \(1/2\), the envelope order is monotone, so no zero other than the closest zero to \(1/2\) on that side can give the largest value. This proves the two-candidate formula, including the case in which one side contains no zero.

**3. Uniform asymptotic.** On each fixed compact interval \(K\subset(0,\infty)\), the classical Plancherel--Rotach formulas for \(L_n\) and \(L_{n-1}^{(1)}\) (DLMF §18.15(iv), equations 18.15.14--16) give, uniformly for \(x\in K\),
\[
\begin{aligned}
n^{3/4}F_n(x)
 &=\frac{e^{-x/2}x^{1/4}}{\sqrt\pi}
 \left[\cos\left(2\sqrt{(n-1)x}-\frac{3\pi}{4}\right)+O_K(n^{-1/2})\right],\\
n^{1/4}F_n'(x)
 &=\frac{e^{-x/2}x^{-1/4}}{\sqrt\pi}
 \left[\cos\left(2\sqrt{nx}-\frac{\pi}{4}\right)+O_K(n^{-1/2})\right].
\end{aligned}
\]
The two cosine phases differ by \(\pi/2+O_K(n^{-1/2})\). Therefore their squared contributions add to one up to an error \(O_K(n^{-1/2})\), and
\[
\boxed{n^{3/2}S_n(x)=\frac{e^{-x}\sqrt x}{\pi}+O_K(n^{-1/2}).}
\]
Since \(M_n^2\le S_n(1/2)\), this proves the desired asymptotic upper bound. For the reverse inequality, choose \(y_n\to1/2\), with \(|y_n-1/2|=O(n^{-1/2})\), such that
\(2\sqrt{(n-1)y_n}-3\pi/4\) is an integral multiple of \(\pi\). Such a point exists for every sufficiently large \(n\), because the phase increases continuously with local derivative of order \(\sqrt n\). The first uniform formula gives
\[
\liminf_{n\to\infty}n^{3/4}M_n\ge
\frac{e^{-1/4}(1/2)^{1/4}}{\sqrt\pi}.
\]
The upper bound has exactly the same value, proving the sharp limit.

**4. Localization of all maximizers.** The positive function \(x\mapsto e^{-x}\sqrt x\) has a unique global maximum at \(x=1/2\). Fix \(\varepsilon\in(0,1/2)\). If a maximizing point satisfied \(x_n\le 1/2-\varepsilon\), envelope monotonicity would imply
\(M_n^2\le S_n(1/2-\varepsilon)\). If \(x_n\ge1/2+\varepsilon\), it would imply \(M_n^2\le S_n(1/2+\varepsilon)\). Both contradict the established asymptotic for \(M_n\) and the strictly smaller limits of the scaled envelope at the two points. Hence all maximizing locations converge to \(1/2\).

## Verification
The accompanying standalone `CHECK.py` derives the primitive, oscillator equation, and Sonin identity symbolically for the first twelve degrees. It computes all Laguerre roots for the first hundred degrees and confirms that only the nearest-to-\(1/2\) root(s) are needed, and that the upper envelope dominates the observed maximum. For four larger degrees it checks the predicted limiting envelope numerically. These finite tests are corroborative and do not replace the universal differential identity or compact-uniform classical asymptotic invoked above. Run `python CHECK.py` with Python, SymPy, NumPy, and SciPy installed.

## Relationship to prior work
Kakharman and Tokmagambetov, arXiv:2610.08167 (first public 2026-10-06), establish modulus-of-smoothness and weighted-sequence estimates for Laguerre coefficients; their statements do not evaluate the exact optimal bounded-variation coefficient norm for every degree or the sharp global asymptotic. Zhang, Liu, and Xiang, arXiv:2604.17752, study fixed algebraic/logarithmic singularities and spectral truncation errors; optimizing over the location of a varying jump is not included. The classical Laguerre and Plancherel--Rotach formulas themselves are established, not claimed new. Sluchak, arXiv:2611.04067 (first public 2026-11-02), already states the general sharp primitive method and the ordinary-Laguerre primitive formula, but its Section 8 expressly does not establish a global \(O(n^{-3/4})\) bound; it is cited here as an additional overlapping comparison, not as the motivating source. Zhang, Xiang, and Kong (2023) obtain fixed-jump Laguerre coefficient rates; its full text was not accessible for a complete comparison, leaving a specific residual priority risk.

## Limitations
No uniform estimate for generalized Laguerre parameters \(\alpha\ne0\) is claimed. The coefficient norm is the sharp variation-only norm, not an improvement under additional smoothness assumptions. The full text of the 2023 piecewise-Laguerre paper was unavailable, and an equivalent calculation in older orthogonal-polynomial extremum literature remains possible. There is no independent mathematical audit or publication-priority certification.

## References
1. N. Kakharman and N. Tokmagambetov, *Moduli of smoothness and growth of the Laguerre transform: two-sided estimates*, arXiv:2610.08167 (2026), https://arxiv.org/abs/2610.08167.
2. Y. Zhang, G. Liu, and S. Xiang, *Optimal asymptotic analyses on Laguerre and Hermite orthogonal approximation for functions of algebraic and logarithmic regularities*, arXiv:2604.17752 (2026), https://arxiv.org/html/2604.17752v1.
3. NIST Digital Library of Mathematical Functions, §18.15(iv), especially equations 18.15.14--16, https://dlmf.nist.gov/18.15.iv.
4. V. Sluchak, *Bounds for Orthogonal Expansion Coefficients via Weighted Primitives*, arXiv:2611.04067 (2026), especially §8, https://arxiv.org/html/2611.04067v1.
5. Y. Zhang, S. Xiang, and D. Kong, *On optimal convergence rates of Laguerre polynomial expansions for piecewise functions*, Journal of Computational and Applied Mathematics 425 (2023), 115053, DOI:10.1016/j.cam.2022.115053 (full text unavailable in the present comparison).
