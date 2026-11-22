# Sharp bounded-variation norms of every Bernstein–Durrmeyer power

## Finding
Let \(n\geq1\) and \(r\geq1\) be integers. For the classical Bernstein–Durrmeyer operator \(D_n\), the **exact operator norm on real bounded variation modulo constants** is
\[
\kappa_{n,r}:=\sup_{\operatorname{TV}(f)>0}
\frac{\operatorname{TV}(D_n^r f)}{\operatorname{TV}(f)}
=\sum_{0\le q\le\lfloor(n-1)/2\rfloor}
(-1)^q(c_q+c_{q+1})\lambda_{n,2q+1}^{\,r},
\quad c_q=4^{-q}\binom{2q}{q},\quad
\lambda_{n,j}=\prod_{s=0}^{j-1}\frac{n-s}{n+2+s}.
\]
The same number is the sharp oscillation-seminorm coefficient of \(D_n^r\). For every \(n,r\), the only nonconstant real bounded-variation extremizers, modulo constants, nonzero scaling, and almost-everywhere equivalence, are steps jumping at \(1/2\). The first power is the previously known special value \(\kappa_{n,1}=1-2^{-n}\); the new exact formula addresses **every power**, including all \(r\geq2\).

For each fixed \(n\), the sharp long-power equivalent is
\[
\kappa_{n,r}\sim\frac32\left(\frac{n}{n+2}\right)^r\quad(r\to\infty).
\]
For \(n\geq3\), the first spectral correction is \(-\frac78\lambda_{n,3}^{\,r}\), with an exact finite alternating expansion. In particular, for \(n\geq3\) and all \(r\geq1\),
\[
\frac32\lambda_{n,1}^{\,r}-\frac78\lambda_{n,3}^{\,r}
\leq\kappa_{n,r}<\frac32\lambda_{n,1}^{\,r},
\]
with equality on the left for \(n=3,4\). At \(n=1,2\), the leading expression is already exact. Finally, for every \(n\geq1\) and positive integers \(r,s\),
\[
\kappa_{n,r+s}<\kappa_{n,r}\kappa_{n,s}.
\]
This demonstrates a gap between multiplication of the one-step sharp constant and the much faster exact long-run variation decay.

## Assumptions and scope
For \(x,t\in[0,1]\), put \(p_{n,j}(x)=\binom njx^j(1-x)^{n-j}\). Define
\[
(D_nf)(x)=(n+1)\sum_{j=0}^np_{n,j}(x)\int_0^1p_{n,j}(t)f(t)\,dt.
\]
The input is a **real** function of bounded Jordan variation on \([0,1]\). As a Lebesgue-integral operator, \(D_n\) ignores changes on null sets; equality classification is therefore modulo almost-everywhere equivalence and uses representatives of minimal Jordan variation. The total variation of its smooth polynomial output is \(\operatorname{TV}(g)=\int_0^1|g'(x)|\,dx\). The oscillation norm is \(\operatorname{osc}(f)=\sup f-\inf f\) for bounded real functions. All formulas hold for every indicated integer pair; the long-power equivalent fixes \(n\) before letting \(r\to\infty\).

## Proof
**1. Strict total positivity and reflection.** The kernel of \(D_n\) is
\[
K_n(x,t)=(n+1)\sum_{j=0}^np_{n,j}(x)p_{n,j}(t).
\]
For \(x_1<x_2\) and \(t_1<t_2\), every two-column determinant of the Bernstein system is nonnegative and at least one is strictly positive. Expanding the kernel determinant over pairs of indices yields a strictly positive determinant for \(K_n\) (including endpoint arguments by continuity and the same direct minor formula). Compositions preserve strict \(2\times2\) positivity: for kernels \(A,B\), the two-point determinant of \(AB\) is the integral over \(u<v\) of the product of the two corresponding determinants, which is strictly positive. Hence each kernel \(K_n^{(r)}\) for \(D_n^r\) is strictly TP2 and positive. In addition it is Markov (unit row integrals) and reflection-symmetric, so \(K_n^{(r)}(1,t)=K_n^{(r)}(0,1-t)\).

For \(y\in(0,1)\), take \(H_y(t)=\mathbf1_{[y,1]}(t)\). Strict TP2 and stochastic ordering imply \(x\mapsto D_n^rH_y(x)\) is strictly increasing. Consequently,
\[
\operatorname{TV}(D_n^rH_y)
=(D_n^rH_y)(1)-(D_n^rH_y)(0)
=\int_y^1 h_{n,r}(t)\,dt,
\quad h_{n,r}(t)=K_n^{(r)}(1,t)-K_n^{(r)}(0,t).
\]
Strict TP2 makes the ratio \(K_n^{(r)}(1,t)/K_n^{(r)}(0,t)\) strictly increasing in \(t\). Reflection forces this ratio to equal one at \(t=1/2\). Thus \(h_{n,r}(t)<0\) for \(t<1/2\) and \(h_{n,r}(t)>0\) for \(t>1/2\). The displayed step variation is uniquely maximized at \(y=1/2\).

**2. Reduction of all variation inputs to jumps.** Distributionally, every real BV function admits a finite signed derivative measure \(\mu\) with \(|\mu|([0,1])\le\operatorname{TV}(f)\) and a representation \(f(t)=c+\int H_y(t)\,d\mu(y)\) almost everywhere. Linearity, Fubini, and the triangle inequality for the \(L^1\)-norm of the output derivative yield
\[
\operatorname{TV}(D_n^rf)
\le\int\operatorname{TV}(D_n^rH_y)\,d|\mu|(y)
\le\operatorname{TV}(D_n^rH_{1/2})\operatorname{TV}(f).
\]
The midpoint step attains this bound. Strict uniqueness of the maximizing location forces the variation measure of any nonconstant extremizer to be concentrated at \(1/2\), proving the stated equality classification. For the oscillation seminorm, stochastic ordering reduces the maximum kernel-row distance to the endpoint pair, and the same one-crossing calculation gives precisely the integral of the positive part of \(h_{n,r}\), equal to the displayed BV norm.

**3. Diagonalization and exact coefficient.** The kernel is symmetric and \(D_n\) preserves polynomial degree. Its action on degree \(j\) has leading coefficient \(\lambda_{n,j}\): integrate a monomial against \(p_{n,k}\) to get a beta rising factorial, then take the leading term in the binomial-index polynomial. Therefore the normalized shifted Legendre polynomials \(\sqrt{2j+1}P_j(2x-1)\), \(0\le j\le n\), are orthonormal eigenfunctions with eigenvalues \(\lambda_{n,j}\). For every positive integer \(r\),
\[
K_n^{(r)}(x,t)=\sum_{j=0}^n(2j+1)\lambda_{n,j}^{\,r}P_j(2x-1)P_j(2t-1).
\]
Subtracting the endpoint rows retains the odd indices only. Integrating against \(H_{1/2}\) gives
\[
\kappa_{n,r}=\sum_{\substack{1\le j\le n\\j\text{ odd}}}
\lambda_{n,j}^{\,r}\big(P_{j-1}(0)-P_{j+1}(0)\big).
\]
The standard identity \(P_{2q}(0)=(-1)^q4^{-q}\binom{2q}{q}\) yields the formula in the Finding. At the first power, the endpoint kernel rows have beta densities \((n+1)(1-t)^n\) and \((n+1)t^n\). Their positive-part integral from \(1/2\) to \(1\) is \(1-2^{-n}\).

**4. Sharp long-run law and strictness.** The eigenvalues are strictly decreasing in \(j\), so the \(j=1\) term dominates as \(r\to\infty\) at fixed \(n\). The remaining coefficients alternate, with strictly decreasing absolute magnitudes \(c_q+c_{q+1}\), and the positive eigenvalue factors decrease with \(q\). The alternating-series estimate proves the displayed two-mode bounds and identifies the negative first correction. Finally, the only BV extremizers for each power are midpoint steps, whereas \(D_n^sH_{1/2}\) is smooth and nonconstant for \(s\ge1\). Applying the strict inequality for the \(r\)-th power to that smooth function, and then the sharp \(s\)-th power estimate, proves \(\kappa_{n,r+s}<\kappa_{n,r}\kappa_{n,s}\).

## Verification
A standalone exact-rational checker, `check_iterated_durrmeyer.py`, independently evaluates \(D_n^rH_{1/2}\) by finite Bernstein Gram-matrix multiplication and compares it with the Legendre spectral formula for every \(1\le n\le12\) and \(1\le r\le8\). It also checks stochasticity, matrix symmetry, adjacent strict TP2 minors, the one-step identity, the spectral bounds, and strict submultiplicativity on that grid. It uses only the Python standard library: `python check_iterated_durrmeyer.py`. These 96 exact comparisons are independent finite consistency tests; they do **not** replace the analytical proof for all integer pairs.

For illustration, at three degrees the first and second norms are \(7/8\) and \(151/280\), respectively; in particular \(151/280<(7/8)^2\). At four degrees they are \(15/16\) and \(445/672\). The latter can be checked from the first two odd Legendre modes alone.

## Relationship to prior work
Öksüzer, Karsli, and Taşdelen Yeşildal (arXiv:1605.03976, first public 2016-04-30) prove a variation-diminishing bound and approximation-in-variation results for this classical integral operator. They do not state a sharp operator norm for its powers or the midpoint equality classification. The Jacobi-weighted one-step oscillation result in the indexed 2026 finding `ff055fe1e2d7` gives the unweighted \(r=1\) constant \(1-2^{-n}\), and explicitly leaves arbitrary iterates unresolved. Hence **the one-step identity is prior work**, not claimed original here.

Derriennic's 1981 Legendre eigenstructure, described in Abel–Acu–Heilmann–Raşa (arXiv:2506.23579, 2025), is a known input to step 3. That later paper supplies all-power kernel expansions and compositions, but does not obtain the sharp BV/oscillation coefficient, prove its unique midpoint extremizers for every power, or derive the strict seminorm submultiplicativity. Heilmann and Raşa (2016) analyze eigenstructure, Kantorovich modifications, and convergence of iterates; their displayed derivative contraction controls a different seminorm. The new contribution here is the **exact sharp all-power BV coefficient and optimizer**, not the eigenvalues or a generic spectral convergence assertion.

## Limitations
This result covers the classical **unweighted** Bernstein–Durrmeyer operator, real BV on a single interval, and positive integer powers. It does not establish the analogous universal midpoint optimizer for asymmetric Jacobi weights, mixed degrees, or multivariate domains. General published spectral decompositions make the coefficient calculable once the new unique-crossing argument is supplied; historical unindexed equivalent statements remain a priority risk. No independent mathematical audit has been performed.

## References
1. Ö. Öksüzer, H. Karsli, and F. Taşdelen Yeşildal, *Convergence of the Bernstein-Durrmeyer operators in variation seminorm*, arXiv:1605.03976 (first posted 2016-04-30), https://arxiv.org/abs/1605.03976.
2. U. Abel, A. M. Acu, M. Heilmann, and I. Raşa, *Kernels for composition of positive linear operators*, arXiv:2506.23579 (first posted 2025-06-30), https://arxiv.org/abs/2506.23579.
3. M. Heilmann and I. Raşa, *Eigenstructure and iterates for uniquely ergodic Kantorovich modifications of operators*, *Positivity* (first published online 2016-08-23), https://doi.org/10.1007/s11117-016-0441-1.
4. *Sharp oscillation contraction of Jacobi-weighted Bernstein–Durrmeyer kernels*, published mathematical finding (2026-10-18), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-oscillation-contraction-of-jacobi-weighted-bernstein-durrm--ff055fe1e2d7.
