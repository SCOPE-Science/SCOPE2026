# A sharp logarithmic Lebesgue coefficient after shifting one central Chebyshev–Lobatto node

## Finding

For every fixed real \(0<\alpha<1\), every even integer \(n\ge4\), and the interpolation grid formed by replacing only the central Chebyshev–Lobatto node
\[
 x_{n/2}=0\quad\hbox{with}\quad y_n=\cos\bigl(\pi/2+\alpha\pi/n\bigr)=-\sin(\alpha\pi/n),
\]
while retaining all other nodes \(x_i=\cos(i\pi/n)\), let \(\Lambda_n(\alpha)\) denote the norm of the degree-at-most-\(n\) Lagrange interpolation projector from continuous functions on \([-1,1]\) to polynomials with the uniform norm. Then
\[
 \boxed{\displaystyle \lim_{\substack{n\to\infty\\ n\ \mathrm{even}}}\frac{\Lambda_n(\alpha)}{\log n}
 = C(\alpha):=\frac2\pi\max_{0<u<1/2}\sin(\pi u)\left(1+\frac\alpha u\right).}
\]
The maximum is achieved at exactly one \(u_\alpha\in(0,1/2)\). Equivalently it is the unique solution of
\[
 \alpha=\frac{\pi u_\alpha^2\cos(\pi u_\alpha)}
 {\sin(\pi u_\alpha)-\pi u_\alpha\cos(\pi u_\alpha)}.
\]
In particular, \(C(\alpha)>(2/\pi)(1+2\alpha)>2/\pi\), so a single fixed-fraction mesh perturbation leaves the Lebesgue growth logarithmic but strictly increases its sharp leading coefficient. A sequence of near-norming evaluation points is \(-\sin(-\pi u_\alpha/n)=\sin(\pi u_\alpha/n)\), on the side *opposite* to the displaced node.

## Assumptions and scope

The node shift is an angular displacement of \(\alpha\pi/n\) to the right in angular coordinate, with \(\alpha\) fixed independently of even \(n\) and strictly less than one. The perturbed node stays strictly between its two unchanged neighbors. No other node moves. The Lebesgue function is the sum of absolute values of all \(n+1\) fundamental Lagrange polynomials, maximized on the whole closed interval \([-1,1]\). All statements are for real interpolation; no asymptotics uniform as \(\alpha\uparrow1\) are asserted. The degree is \(n\), not the number of nodes.

## Proof

**1. Exact one-node replacement.** Set \(j=n/2\). The unshifted node polynomial, up to a nonzero constant, is
\[
 W_n(x)=(x^2-1)U_{n-1}(x),\qquad W_n(\cos\theta)=-\sin\theta\sin(n\theta),
\]
and its derivative at the unshifted interpolation nodes is \(W_n'(x_i)=n(-1)^i\) for interior indices, and \(2n(-1)^i\) at the endpoints. Write \(\ell_i\) for its cardinal functions, \(\widetilde\ell_i\) for those of the shifted grid, and \(y=y_n\). Since the new node polynomial is \((x-y)W_n(x)/x\), direct differentiation at each unchanged node gives
\[
 \widetilde\ell_i(x)=\ell_i(x)\frac{x-y}{x}\frac{x_i}{x_i-y}\quad(i\ne j),
 \qquad \widetilde\ell_j(x)=\frac{\ell_j(x)}{\ell_j(y)}.
\]
The removable singularities at \(x=0\) are filled by continuity. Direct substitution shows
\[
 \ell_j(y)=\frac{\cos(\alpha\pi/n)\sin(\pi\alpha)}{n\sin(\alpha\pi/n)}
 \longrightarrow\frac{\sin(\pi\alpha)}{\pi\alpha}>0.
\]
Moreover \(|\ell_j(x)|\le\pi/2\) on \([-1,1]\), by \(|\sin(n(\theta-\pi/2))|\le n|\theta-\pi/2|\) and \(|\cos\theta|\ge2|\theta-\pi/2|/\pi\). Thus \(\sup_x|\widetilde\ell_j(x)|=O_\alpha(1)\).

**2. Localized logarithmic profile.** Parameterize positions near the moved node by \(x_n(t)=-\sin(\pi t/n)\), where \(t\) ranges in any fixed compact real interval. For \(k\ne0\), let \(i=j+k\). Applying step 1 and \(x_i=-\sin(\pi k/n)\) yields the exact absolute-value expression (interior nodes)
\[
 |\widetilde\ell_{j+k}(x_n(t))|=\frac{\cos(\pi t/n)|\sin(\pi t)|}{n|\sin(\pi t/n)-\sin(\pi k/n)|}
 \left|\frac{\sin(\pi t/n)-\sin(\alpha\pi/n)}{\sin(\pi t/n)}\right|
 \left|\frac{\sin(\pi k/n)}{\sin(\pi k/n)-\sin(\alpha\pi/n)}\right|.
\]
At removable points this means the continuous limit; the two endpoint terms have an additional factor \(1/2\). For any fixed \(T>0\), uniformly for \(|t|\le T\) and \(K_T\le|k|\le n/4\), Taylor expansion of the divided differences (with the cancellations at \(t=0\) made before expansion) gives
\[
 |\widetilde\ell_{j+k}(x_n(t))|
 =\frac{A_\alpha(t)}{|k|}+O_{T,\alpha}\left(k^{-2}+\frac{|k|}{n^2}+\frac1n\right),\qquad
 A_\alpha(t)=\frac{|\sin(\pi t)|}{\pi}\left|1-\frac\alpha t\right|.
\]
Define \(A_\alpha(0)=\alpha\) by continuity. The finitely many smaller \(k\) terms are uniformly \(O_{T,\alpha}(1)\) in total: each fixed-index cardinal is a continuous ratio of sine divided differences, with the shifted nodes separated by a fixed positive fraction of the angular gap. The large-index tail \(n/4<|k|\le n/2\) also sums to \(O_{T,\alpha}(1)\), since each such cardinal is \(O_{T,\alpha}(1/n)\). Summing the two harmonic tails and using \(\sum_{1\le k\le n/4}1/k=\log n+O(1)\) proves, uniformly for \(t\) on compact sets,
\[
 \sum_{i=0}^n|\widetilde\ell_i(x_n(t))|
 =f_\alpha(t)\log n+O_{T,\alpha}(1),\qquad
 f_\alpha(t)=\frac2\pi|\sin(\pi t)|\left|1-\frac\alpha t\right|.
\]
The continuous values are \(f_\alpha(0)=2\alpha\) and \(f_\alpha(\alpha)=0\).

**3. No larger bulk logarithmic coefficient.** Consider any sequence \(x_n\in[-1,1]\) with \(n|x_n|\to\infty\). The replacement formulas and the bound for the moved cardinal imply
\[
 \widetilde\lambda_n(x_n)
 \le\left|1-\frac{y_n}{x_n}\right|\left(\lambda_n^{(0)}(x_n)+E_n(x_n)\right)+O_\alpha(1),
 \qquad
 E_n(x)=\sum_{i\ne j}|\ell_i(x)|\frac{|y_n|}{|x_i-y_n|}.
\]
Here \(\lambda_n^{(0)}\) is the ordinary Chebyshev–Lobatto Lebesgue function. The geometry of the cosine nodes gives \(|y_n|/|x_{j+k}-y_n|\le B_\alpha/(1+|k|)\) for every nonzero integer \(k\) in the index range. For each fixed \(K\), \(|\ell_{j+k}(x_n)|\to0\) uniformly over \(0<|k|\le K\): \(|W_n(x_n)|\le1\), the interior derivative has magnitude \(n\), and \(n|x_n-x_{j+k}|\to\infty\). For the remaining \(|k|>K\),
\[
 E_n(x_n)\le o(1)+\frac{B_\alpha}{K}\lambda_n^{(0)}(x_n).
\]
The established unperturbed asymptotic \(\max_x\lambda_n^{(0)}(x)=(2/\pi)\log n+O(1)\), together with \(y_n/x_n\to0\), first gives \(\limsup E_n(x_n)/\log n\le 2B_\alpha/(\pi K)\), and then zero upon letting \(K\to\infty\). Therefore
\[
 \limsup\frac{\widetilde\lambda_n(x_n)}{\log n}\le\frac2\pi.
\]
For a maximizing sequence of evaluation points, either a subsequence has bounded \(n|x_n|\) and the compact local expansion of step 2 applies, or a subsequence has \(n|x_n|\to\infty\) and the bulk bound applies. Thus the sharp global coefficient is \(\max\{2/\pi,\sup_{t\in\mathbb R}f_\alpha(t)\}\). Taking the local point \(t=-u_\alpha\) supplies the matching lower bound.

**4. Exact maximization and uniqueness.** On \(t\ge\alpha\), \(f_\alpha(t)\le2/\pi\). For \(0<t<\alpha\), \(f_\alpha(t)\le2\alpha\), while \(f_\alpha(-u)>2\alpha\) for some sufficiently small \(u>0\). For \(t=-u<0\), the relevant function is \(2\sin(\pi u)(1+\alpha/u)/\pi\) after taking periodic absolute values. The region \(u\ge1\) gives at most \((2/\pi)(1+\alpha)\); the region \(1/2\le u\le1\) is strictly decreasing; and at \(u=1/2\) the value is \((2/\pi)(1+2\alpha)\). Therefore the global maximizer lies in \(0<u<1/2\).

The derivative of \(H(u)=\sin(\pi u)(1+\alpha/u)\) vanishes exactly when \(\alpha=G(u)\), with
\[
 G(u)=\frac{\pi u^2\cos(\pi u)}{\sin(\pi u)-\pi u\cos(\pi u)}.
\]
Writing \(z=\pi u\), the sign of \(G'(u)\) is the sign of
\[
 2\sin z\cos z-z(1+\cos^2z)<0,\qquad 0<z<\pi/2,
\]
because \(\sin z<z\) and \(2\cos z\le1+\cos^2z\). Also \(G(u)\to\infty\) as \(u\downarrow0\) and \(G(u)\to0\) as \(u\uparrow1/2\). Hence the critical point is unique and is the strict global maximum. At the endpoint \(u=1/2\) the value is \((2/\pi)(1+2\alpha)\), and the interior maximum is strictly larger. This completes the proof.

## Verification

The standalone `verify.py` uses ordinary Python standard-library arithmetic to compare the exact rank-one cardinal replacement identities with independent product-form Lagrange cardinals on small grids. It also checks the unique-root equation numerically and the predicted leading logarithmic slope at three fixed displacement fractions with degrees through \(16384\). Execute `python3 verify.py` alongside this file. The checks are finite diagnostics only; the all-even-degree asymptotic and uniqueness are proved above, not inferred from computation.

## Relationship to prior work

Hao-Ning Wu, *When do perturbed Chebyshev–Lobatto points remain Chebyshev?*, arXiv:2606.23409, first public version June 22, 2026, considers arbitrary angular perturbations, provides a sufficient \(n\sigma_n\log n\)-scale stability bound, and gives a two-node near-collision obstruction at the angular mesh scale. The present fixed-fraction, **single-node** configuration lies outside that sufficient regime and is distinct from the two-node collision obstruction: its exact leading coefficient is calculated rather than estimated by a uniform worst-case theorem.

Austin and Trefethen study perturbed *periodic trigonometric* interpolation grids, not the one-node polynomial Chebyshev–Lobatto coefficient. Piazzon and Vianello provide general small-perturbation stability inequalities, not the sharp coefficient for a fixed mesh-fraction shift. Previously documented single-node **erasure** removes a sample and has a different dimensionality and linear Lebesgue growth; it does not cover relocation at fixed cardinality. These are statement-level comparisons, not a claim that all literature is indexed.

## Limitations

The coefficient is for one centrally relocated interpolation node on even grids, one-sided displacement, fixed \(\alpha\in(0,1)\), and the uniform norm. It does not classify arbitrary distributed perturbations, all perturbation patterns at the mesh scale, odd-degree central-node conventions, the nearly colliding regime \(\alpha\uparrow1\) simultaneously with increasing degree, or finite-precision error. The historical priority of this exact formula is subject to the usual limitations of accessible literature and indexing; no independent audit has been conducted.

## References

1. Hao-Ning Wu, *When do perturbed Chebyshev--Lobatto points remain Chebyshev?*, arXiv:2606.23409 (2026), https://arxiv.org/abs/2606.23409.
2. A. P. Austin and L. N. Trefethen, *Trigonometric Interpolation and Quadrature in Perturbed Points*, arXiv:1612.04018 (2016), https://arxiv.org/abs/1612.04018.
3. F. Piazzon and M. Vianello, *Stability inequalities for Lebesgue constants via Markov-like inequalities*, Dolomites Research Notes on Approximation 11 (2018), 1–9, https://drna.padovauniversitypress.it/system/files/papers/PiazzonVianello_2018_SIL.pdf.
4. Classical Chebyshev–Lobatto Lebesgue estimate, \(\Lambda_n^{(0)}=(2/\pi)\log n+O(1)\), as recalled in Wu, Theorem 3.2.
