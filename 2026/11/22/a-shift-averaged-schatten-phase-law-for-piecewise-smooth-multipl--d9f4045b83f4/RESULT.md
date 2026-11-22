# A shift-averaged Schatten phase law for piecewise-smooth multiplication commutators

## Finding

For the local-averaging orthogonal projection \(P_{N,u}\) on a uniformly shifted \(N\)-cell partition of the circle, let \(M_f\) denote multiplication by a bounded piecewise \(C^1\) complex-valued function \(f\). Write \(h=1/N\) and, for every \(p>0\),

\[
F_p(N)=\frac1h\int_0^h\|[P_{N,u},M_f]\|_{\mathcal S_p}^p\,du.
\]

Then the following three **sharp spectral-mass limits** hold, with \(\Delta_j=f(x_j+)-f(x_j-)\) at the finitely many discontinuities:

\[
\begin{aligned}
\lim_{N\to\infty}h^{1-p}F_p(N)
 &=2\cdot12^{-p/2}\int_{\mathbb T}|f'(x)|^p\,dx,&&0<p<1,\\
\lim_{N\to\infty}F_1(N)
 &=\frac1{\sqrt3}\int_{\mathbb T}|f'(x)|\,dx
   +\frac\pi4\sum_j|\Delta_j|,&&p=1,\\
\lim_{N\to\infty}F_p(N)
 &=2B(1+p/2,1+p/2)\sum_j|\Delta_j|^p,&&p>1.
\end{aligned}
\]

Here \(B\) is Euler's beta function; the first formula includes the case of vanishing derivative, and the last includes the case of no jumps. At finite \(N\), there is a complete exact singular-value description: every cell contributes the nonzero singular value

\[
\sigma_I=\left(\frac1h\int_I|f(x)-h^{-1}\!\int_I f(y)\,dy|^2\,dx\right)^{1/2}
\]

**twice** (omitting zeros). In particular, \(\|[P_{N,u},M_f]\|_{\mathcal S_p}^p=2\sum_I\sigma_I^p\) for all \(p>0\).

## Assumptions and scope

The circle \(\mathbb T\) is \(\mathbb R/\mathbb Z\) with normalized arc length. There is a finite cyclic partition by points \(x_1,\ldots,x_J\) such that \(f\) has a \(C^1\) extension to the closure of each complementary arc and is essentially bounded. Breakpoints at which both one-sided limits agree are allowed and have \(\Delta_j=0\); all derivative integrals use the a.e. derivative on open arcs. When \(J=0\), assume \(f\in C^1(\mathbb T)\). No real-valuedness, monotonicity, or nonvanishing-derivative hypothesis is imposed.

For each integer \(N\ge1\), put \(h=1/N\). For \(0\le u<h\), the arcs \(I_{k,u}=[u+kh,u+(k+1)h)\) modulo \(1\), for \(k=0,\ldots,N-1\), partition the circle. The bounded orthogonal projection \(P_{N,u}\) sends a function to its average on its containing arc. The commutator is \([P_{N,u},M_f]=P_{N,u}M_f-M_fP_{N,u}\). The Schatten expression for \(p<1\) is the \(p\)-th power of the usual quasi-norm. One set of singular-value pairs exists per cell, so the operator has rank at most \(2N\).

## Proof

**1. Exact two-singular-value reduction.** Fix one arc \(I\) of length \(h\), with unit vector \(e=h^{-1/2}1_I\), mean \(m=h^{-1}\int_I f\), and \(w=(f-m)e\). The restriction of the commutator to \(L^2(I)\) is

\[
K_I=|e\rangle\langle \overline w|-|w\rangle\langle e|.
\]

We use the inner-product convention linear in the second argument. Since \(\langle e,w\rangle=\langle e,\overline w\rangle=0\), the normalized vectors \(e,\overline w/\|w\|\) form an orthonormal pair in the input and \(e,w/\|w\|\) an orthonormal pair in the output (when \(w\ne0\)). The restriction maps these input vectors to \(-w\) and \(\|w\|e\), respectively, and vanishes on the input orthogonal complement. Hence its two nonzero singular values both equal \(\|w\|=\sigma_I\). The different arcs are reducing subspaces for \(K\). This proves the finite-rank assertion and the exact formula for every \(p>0\), including complex \(f\).

**2. Smooth-cell contribution.** Mark as exceptional every arc that touches a breakpoint \(x_j\); there are at most \(2J\) such cells, uniformly in \(u\). On the remaining arcs, uniform differentiability of the finitely many \(C^1\) extensions gives the variance expansion

\[
\sigma_{I_{k,u}}=\frac h{\sqrt{12}}|f'(\xi_{k,u})|+o(h),
\]

uniformly in \(u,k\), where \(\xi_{k,u}\in I_{k,u}\) is any point, and the error does not depend on the shift. Indeed, writing \(f(x)=f(\xi)+f'(\xi)(x-\xi)+r(x)\), uniform continuity of the derivatives yields \(\sup_{x\in I}|r(x)|=o(h)\); centered linear functions on a length-\(h\) arc have standard deviation \(h/\sqrt{12}\). Using the uniform continuity of \(t\mapsto|t|^p\) on bounded sets and shifted Riemann sums, for fixed \(p>0\),

\[
2\sum_{I\text{ smooth}}\sigma_I^p
 =2\cdot 12^{-p/2}h^{p-1}\int_{\mathbb T}|f'|^p+o(h^{p-1}),
\]

uniformly in \(u\). The finitely many omitted cells would contribute only \(O(h^p)\) if they were not discontinuous, and their deletion does not change this leading expression.

**3. Jump-cell contribution.** Once \(h\) is smaller than the minimum separation between distinct breakpoints, each true jump is met by exactly one partition arc except on a null set of shifts. If the jump lies a fraction \(\theta_j\in[0,1]\) of the way from the left endpoint, replacing \(f\) on that cell by its two one-sided constants incurs an \(L^\infty\) error \(O(h)\), uniformly over \(u\). The standard deviation of the two-level function is exactly \(|\Delta_j|\sqrt{\theta_j(1-\theta_j)}\). The standard-deviation map is Lipschitz in \(L^2(I,h^{-1}dx)\), so

\[
\sigma_{I(j,u)}=|\Delta_j|\sqrt{\theta_j(1-\theta_j)}+O(h)
\]

uniformly. By uniform continuity of \(t\mapsto t^p\) on compact nonnegative intervals for every \(p>0\), its \(p\)-th powers converge uniformly to the corresponding two-level expression. As the shift ranges uniformly through \([0,h)\), each \(\theta_j\) is individually uniform on \([0,1]\), regardless of correlations between different jumps. Therefore

\[
\frac2h\int_0^h\sum_j\sigma_{I(j,u)}^p\,du
 \longrightarrow 2\sum_j|\Delta_j|^p\int_0^1[\theta(1-\theta)]^{p/2}d\theta
 =2B(1+p/2,1+p/2)\sum_j|\Delta_j|^p.
\]

Continuous non-\(C^1\) breakpoints contribute \(O(h^p)\) and vanish. This establishes a finite nonzero jump contribution for every \(p>0\).

**4. Balance of scales.** The smooth-cell contribution is \(O(h^{p-1})\), while the jump contribution is \(O(1)\). For \(p>1\), only jumps remain in the unscaled limit. For \(0<p<1\), multiplying by \(h^{1-p}\) preserves the derivative integral and annihilates jumps. At \(p=1\), both survive with \(2/\sqrt{12}=1/\sqrt3\) and \(2B(3/2,3/2)=\pi/4\). This proves all three formulas.

## Verification

An independent finite-dimensional matrix computation in `verify.py` constructs complex-valued multiplication and rank-one averaging matrices and compares both nonzero singular values with the cell variance. Further quadrature checks use the periodic sawtooth \(f(x)=x\) for \(0\le x<1\), with one unit jump and a.e. derivative one. For this example, when the jump has relative phase \(\theta\), its crossing-cell variance is **exactly**

\[
\sigma_{\mathrm{cross}}^2=\frac{h^2}{12}+(1-h)\theta(1-\theta),
\]

and the remaining \(N-1\) cells have \(\sigma=h/\sqrt{12}\). Thus the averaged squared Hilbert–Schmidt mass is the exact finite-grid identity \(F_2(N)=1/3-h/6\), consistent with the limit \(1/3\). The same example gives \(F_1(N)\to 1/\sqrt3+\pi/4\) and the stated subtrace normalization. Numerical tests check rather than replace the infinite-dimensional proof.

## Relationship to prior work

Wei and Zhang's 2024 study develops Schatten properties of martingale paraproducts and singular-integral commutators using Besov spaces and dyadic representation. Chao and Peng (1996) investigate Schatten classes and commutators in the simple-martingale framework. Both are relevant to localization, averaging, and commutators; neither of the inspected primary texts states the present exact finite-cell two-singular-value identity together with the *shift-averaged, three-regime, jump-versus-derivative asymptotics and constants*. The variance identity itself is a basic rank-one calculation and is **not** claimed to be historically new in isolation. The present contribution is the complete quantitative asymptotic partition of spectral mass across the trace threshold, with a canonical offset average eliminating grid-alignment artifacts.

A nearby published computation for the commutator of *two* displaced histogram projections determines endpoint operator norms, not the Schatten mass of a *single* histogram projection against multiplication; see the relevant result in the references. These objects and norms are different, and no implication of the stated coefficients is evident. Absence of a matching search hit is not a novelty proof; potential equivalent older signal-processing or variation formulas remain an explicit priority risk.

## Limitations

The theorem is proved only for bounded complex symbols that are piecewise \(C^1\) with finitely many breakpoints. It does not assert a formula for arbitrary bounded-variation functions, infinitely many jumps, nonuniform partitions, multidimensional meshes, or a deterministic offset-independent trace law. In particular, a grid whose boundaries coincide with every jump may suppress all jump-cell contributions, which is why averaging the offset is essential. This work has only self-review; independent validation and exhaustive historical-priority review have not been performed.

## References

- Z. Wei and H. Zhang, *On the boundedness and Schatten class property of noncommutative martingale paraproducts and operator-valued commutators*, initial public arXiv posting 20 July 2024, https://arxiv.org/abs/2407.14988 . See especially Theorems 1.1, 1.2 and Section 6 on martingale paraproduct commutators.
- J.-A. Chao and L. Peng, *Schatten classes and commutators on simple martingales*, *Colloquium Mathematicum* 71 (1996), https://bibliotekanauki.pl/articles/966877.pdf .
- *Sharp endpoint commutator instability for translated histogram projections*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-endpoint-commutator-instability-for-translated-histogram-p--491d3bae8ceb .
