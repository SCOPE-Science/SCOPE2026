# Sharp logarithmic amplification from one displaced Chebyshev–Lobatto node

## Finding

For each integer \(n\ge2\), the Chebyshev–Lobatto grid is \(x_{j,n}=\cos(j\pi/n)\) for \(0\le j\le n\). Fix \(0<\tau<1\), and choose integers \(k_n\) with \(1\le k_n\le n-1\) and \(k_n/n\to a\in(0,1)\). Replace exactly the sample \(x_{k_n,n}\) by
\[
y_n=\cos((k_n+\tau)\pi/n),
\]
leaving every other sample unchanged. Let \(\widetilde\Lambda_n\) be the operator norm on \(C([-1,1])\), with its uniform norm, of polynomial interpolation of degree at most \(n\) at this displaced grid. Define \(v_\tau\in(0,1/2)\) as the unique solution of
\[
\pi(v_\tau^2+\tau v_\tau)\cos(\pi v_\tau)
=\tau\sin(\pi v_\tau).
\]
Then the **exact asymptotic logarithmic amplification** is
\[
\boxed{\displaystyle
\lim_{n\to\infty}\frac{\widetilde\Lambda_n}{\log n}
=\frac2\pi\sin(\pi v_\tau)
 \left(1+\frac{\tau}{v_\tau}\right).}
\]
The leading coefficient depends on the displacement fraction \(\tau\) but not on the limiting bulk index ratio \(a\). It is strictly increasing in \(\tau\), and exceeds the intact-grid coefficient \(2/\pi\) for every \(\tau>0\).

A fully explicit asymptotically maximizing evaluation point is
\[
z_n=\cos((k_n-v_\tau)\pi/n).
\]
Indeed, the Lebesgue function at \(z_n\), divided by \(\log n\), converges to the boxed constant. If \(z_n^*\in[-1,1]\) is *any* exact maximizing evaluation point and \(z_n^*=\cos(\theta_n^*)\) with \(0\le\theta_n^*\le\pi\), then
\[
\frac{n\theta_n^*}{\pi}-k_n\longrightarrow-v_\tau.
\]
For example, at \(\tau=1/2\), the leading coefficient is \(1.378345665463865\ldots\), instead of the intact-grid value \(2/\pi=0.636619772367581\ldots\).

## Assumptions and scope

All grid points are exact real numbers; they remain distinct because \(0<\tau<1\). The displacement affects exactly one **interior** sample whose index remains a positive proportion of \(n\) away from each endpoint. The statement fixes \(\tau\) as \(n\to\infty\); there is no uniform claim as \(\tau\) approaches the collision value \(1\). The Lebesgue constant is the maximum, over all \(z\in[-1,1]\), of the sum of absolute values of all \(n+1\) Lagrange cardinal polynomials. The logarithm is natural.

## Proof

**1. Exact one-node replacement.** Write \(x_j=x_{j,n}\), \(k=k_n\), \(y=y_n\). Let \(L_j\) denote the unperturbed cardinal polynomial and \(\widetilde L_j\) the displaced-grid cardinal polynomial. Polynomial interpolation at the displaced grid gives the exact identities
\[
\widetilde L_k(z)=\frac{L_k(z)}{L_k(y)},\qquad
\widetilde L_j(z)=L_j(z)-\frac{L_j(y)}{L_k(y)}L_k(z)
\quad(j\ne k).
\tag{1}
\]
Since \(y\ne x_j\) for every original node, \(L_k(y)\ne0\). Equivalently, comparing the nodal-product polynomials gives for \(j\ne k\)
\[
\widetilde L_j(z)=L_j(z)
 \frac{z-y}{z-x_k}\frac{x_j-x_k}{x_j-y},
\tag{2}
\]
with the removable singularity at \(z=x_k\) interpreted by continuity. Both formulas hold identically, not approximately.

**2. Chebyshev cardinal formula.** For \(z=\cos\theta\), use the nodal-product polynomial proportional to \(Q_n(\cos\theta)=-\sin\theta\sin(n\theta)\). Differentiation at the nodes gives \(Q_n'(x_j)=n(-1)^j\) for interior \(j\) and \(Q_n'(x_j)=2n(-1)^j\) for endpoints. Consequently
\[
L_j(\cos\theta)=
\frac{-(-1)^j\sin\theta\sin(n\theta)}
{n c_j[\cos\theta-\cos(j\pi/n)]},
\quad c_j=\begin{cases}2&j\in\{0,n\},\\1&0<j<n.\end{cases}
\tag{3}
\]
In particular, since \(k/n\to a\in(0,1)\),
\[
L_k(y)\longrightarrow\frac{\sin(\pi\tau)}{\pi\tau}>0.
\tag{4}
\]
The classical intact-grid estimate is
\[
\max_z\sum_j|L_j(z)|=\frac2\pi\log n+O(1).
\tag{5}
\]
It is also stated in Equation (1.2) of Wu [1].

**3. Exact local logarithmic profile.** For a real angular offset \(u\), set \(z_n(u)=\cos((k+u)\pi/n)\). Fix \(R>0\). Uniformly for \(|u|\le R\), the displaced Lebesgue function satisfies
\[
\widetilde\lambda_n(z_n(u))
=\frac2\pi\,|\sin(\pi u)|
 \left|1-\frac{\tau}{u}\right|\log n+O_{R,\tau,a}(1),
\tag{6}
\]
where the product at \(u=0\) is assigned its continuous value \(\pi\tau\).

Here is the error justification. In (3), put \(j=k+m\). For fixed sufficiently large \(M>2(R+1)\) and \(M<|m|\le\epsilon n\), where \(\epsilon>0\) is fixed sufficiently small compared with \(a\) and \(1-a\), Taylor expansion of cosine differences about the interior angle \(k\pi/n\), followed by the exact product identity (2), gives
\[
\left|\widetilde L_{k+m}(z_n(u))\right|
=\frac{|\sin(\pi u)|\,|u-\tau|}{\pi|u|}
 \frac1{|m|}+O_{R,\tau,a}\!\left(\frac1{m^2}+\frac1n\right).
\tag{7}
\]
The error is uniform over \(|u|\le R\), including \(u=0\), because \(\sin(\pi u)/u\) extends smoothly there. More explicitly, before extracting the harmonic coefficient, the leading term is
\[
\frac{|\sin(\pi u)|\,|u-\tau|}{\pi|u|}
 \frac{|m|}{|u-m|\,|m-\tau|};
\]
its difference from the \(1/|m|\) term in (7) is \(O_R(m^{-2})\), and the relative error of the trigonometric-to-linear approximations is \(O_{R,\tau,a}(|m|/n)\), hence contributes \(O(1/n)\). The finitely many \(|m|\le M\), together with the displaced index \(j=k\), contribute only \(O_{R,\tau,a,M}(1)\), including at their removable poles. For \(|m|>\epsilon n\), the exact formula (2) and bulk location give \(|\widetilde L_{k+m}(z_n(u))|\le C_{R,\tau,a,\epsilon}/n\); their total is \(O(1)\). Summing (7) over the positive and negative offsets uses \(\sum_{1\le m\le\epsilon n}m^{-1}=\log n+O_\epsilon(1)\) on each side. This proves (6), uniformly on the entire compact \(u\)-interval.

**4. Localization of every global maximum.** The exact basis-replacement identity (1) and the triangle inequality yield
\[
\widetilde\lambda_n(z)
\le \sum_j|L_j(z)|+
 \frac{|L_k(z)|}{|L_k(y)|}
 \left(1+\sum_{j\ne k}|L_j(y)|\right).
\tag{8}
\]
By (4) and (5), the final parenthesis is \(O_\tau(\log n)\). For \(z=\cos\theta\), put \(u=n\theta/\pi-k\). Formula (3) and the bulk separation of \(k\) from both endpoints give \(|L_k(z)|\le C_a/|u|\) when \(|u|\ge1\). Therefore, for every fixed \(R\ge1\), the region \(|u|\ge R\) obeys
\[
\limsup_{n\to\infty}\sup_{|u|\ge R}
\frac{\widetilde\lambda_n(z_n(u))}{\log n}
\le\frac2\pi+\frac{C_{a,\tau}}R.
\tag{9}
\]
Since the profile in (6) takes values strictly greater than \(2/\pi\), we may choose \(R\) large enough that this exterior bound lies below its global maximum. Thus all maximizing offsets remain in a fixed compact interval, and (6) controls the global limit and their subsequential limits.

**5. Unique scalar maximizer.** Let
\[
g_\tau(u)=|\sin(\pi u)|\left|1-\frac\tau u\right|,
\qquad g_\tau(0)=\pi\tau.
\]
For \(u\ge\tau\), we have \(g_\tau(u)\le1\). For \(0\le u\le\tau\), \(g_\tau(u)\le\pi\tau\). On the negative axis, putting \(u=-v\) gives \(g_\tau(-v)=|\sin(\pi v)|(1+\tau/v)\). Values with \(v\ge1\) are at most \(1+\tau\), strictly below the value \(1+2\tau\) at \(v=1/2\). For \(1/2<v<1\), reflection to \(1-v\) strictly increases this expression. Therefore its unique global maximum is on \(0<v\le1/2\), where
\[
h_\tau(v)=\sin(\pi v)+\tau\frac{\sin(\pi v)}v.
\]
The function is strictly concave on \((0,1/2)\): \(\sin(\pi v)\) is strictly concave, while the identity
\[
\frac{\sin(\pi v)}v=\pi\int_0^1\cos(\pi vt)\,dt
\]
shows that its second derivative is strictly negative there. Moreover, \(h_\tau'(0+)=\pi>0\) and \(h_\tau'(1/2)=-4\tau<0\). Thus its derivative vanishes at exactly one \(v_\tau\in(0,1/2)\); differentiation yields the equation in the statement. This maximum exceeds \(h_\tau(1/2)=1+2\tau>1\) and exceeds \(\pi\tau\), so it dominates every positive-offset value. The coefficient is strictly increasing in \(\tau\) because, for each fixed \(v\in(0,1/2)\), \(h_\tau(v)\) increases strictly with \(\tau\). Substituting this unique maximizer into (6) and using (9) proves the limit, the witness points, and convergence of *every* exact maximizing offset.

## Verification

The accompanying standard-library `checker.py` computes finite-degree Lagrange cardinals directly from (3), compares independently the two exact replacement identities (1) and (2), checks their partition of unity, and numerically solves the unique scalar critical-point equation. Running `python3 checker.py` passed **195 finite diagnostic assertions**. It reports the asymptotic coefficients approximately \(0.984120116280\), \(1.378345665464\), and \(1.804427925536\) for \(\tau=1/4,1/2,3/4\), respectively. Finite computations are consistency checks only; they do not establish the asymptotic limit, global extremality, or priority. All such infinite statements are proved above by exact identities, uniform estimates, and strict concavity.

## Relationship to prior work

Wu [1, Sections 3 and 6] proves a worst-case sufficient condition \(n\sigma_n(1+\log n)=O(1)\), with a small constant, for perturbed Chebyshev–Lobatto grids to retain logarithmic Lebesgue growth, and gives a superlogarithmic near-collision example when **two** nodes move. That theorem's sufficient condition does not cover the fixed mesh fraction \(\tau\in(0,1)\) considered here. The new formula determines the precise \(\log n\) coefficient for a single moved interior node, independent of its bulk location. The single-erasure result [2] concerns **deletion** and a reduction in interpolation degree and has linear rather than logarithmic growth; it does not imply the claimed displaced-node coefficient. The cyclic robust-interpolation certificate [3] optimizes different periodic sampling functionals; it likewise does not imply the present sharp Lebesgue norm. Classical barycentric formulas [4] supply the algebraic coordinates used in the derivation, but do not themselves state the asymptotic optimization.

## Limitations

This is a single deterministic interior-node perturbation, not a uniform theorem for arbitrary correlated perturbations, endpoints, multiple moved nodes, or a displacement fraction depending on \(n\). The pointwise error term in (6) is uniform on bounded angular-offset intervals only; exterior control is sufficient for global maximization but is weaker. Computation of the coefficient requires solving one strictly concave scalar maximization, not a finite algebraic radical. Existing literature may contain a mathematically equivalent single-defect result using a different representation; absolute publication priority has not been established. All source comparisons concern accessible text and statements, not exhaustive historical indexing.

## References

1. H.-N. Wu, *When do perturbed Chebyshev–Lobatto points remain Chebyshev?*, arXiv:2606.23409 (first public 2026-06-22), especially Sections 3 and 6. https://arxiv.org/abs/2606.23409
2. *Single-erasure boundary layers for Chebyshev–Lobatto interpolation*, published research record (2026-10-18). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-single-erasure-boundary-layers-for-chebyshev-lobatto-interpolati--a3c5beff381f
3. *Optimal shifted cyclic certificates for robust Chebyshev interpolation*, published research record (2026-09-19). https://github.com/published-finding corpus/2026/tree/main/2026/9/19/SCOPE-cyclic-chebyshev-obstruction-euler-prefactor--528d46ae115f
4. J.-P. Berrut and L. N. Trefethen, *Barycentric Lagrange interpolation*, SIAM Review 46 (2004), 501–517, DOI: 10.1137/S0036144502417715.
5. A. P. Austin and L. N. Trefethen, *Trigonometric interpolation and quadrature in perturbed points*, SIAM J. Numer. Anal. 55 (2017), 2113–2122, DOI: 10.1137/16M1107760. (A periodic trigonometric, rather than the present algebraic one-defect, setting.)
