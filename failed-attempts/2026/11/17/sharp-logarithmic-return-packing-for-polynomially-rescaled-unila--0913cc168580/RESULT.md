# Sharp logarithmic return packing for polynomially rescaled unilateral shifts

## Finding
Let \(X\) be either the complex sequence space \(\ell^p(\mathbb N_0)\), \(1\le p<\infty\), or \(c_0(\mathbb N_0)\). Let \(B(x_0,x_1,\dots)=(x_1,x_2,\dots)\), and let \(e_0=(1,0,\dots)\). For real \(\alpha\) and integer \(n\ge1\), put \(A_n=n^\alpha B^n\). Set
\[
U_\varepsilon=\{z\in X:\|z-e_0\|_X<\varepsilon\},\qquad
R_{\alpha,\varepsilon}=\left(\frac{1-\varepsilon}{\varepsilon}\right)^{1/\alpha}.
\]
For every \(\alpha>0\) and \(0<\varepsilon<1/2\):

1. The operator sequence \((A_n)\) is topologically mixing, and some \(x\in X\) has dense orbit \(\{A_nx:n\ge1\}\). In contrast, no such vector exists for \(\alpha\le0\).
2. For **every** \(x\in X\), successive return times \(n<m\) in \(E_x(\varepsilon)=\{k\ge1:A_kx\in U_\varepsilon\}\) satisfy \(m>R_{\alpha,\varepsilon}n\). In particular, for every integer \(M\ge0\) and \(N\ge1\),
\[
\#\big(E_x(\varepsilon)\cap[M,M+N]\big)
\le 1+\frac{\log(N+1)}{\log R_{\alpha,\varepsilon}}.
\]
Thus every such return set has zero upper Banach density and hence zero upper and lower natural density.
3. For the natural maximal logarithmic recurrence invariant
\[
\mathcal C_{X,\alpha}(\varepsilon)
=\sup_{x\in X}\limsup_{N\to\infty}
\frac{\#\big(E_x(\varepsilon)\cap[1,N]\big)}{\log N},
\]
there is a **sharp exact constant** on \(c_0\):
\[
\boxed{\mathcal C_{c_0,\alpha}(\varepsilon)
=\frac{\alpha}{\log((1-\varepsilon)/\varepsilon)}.}
\]
For every finite \(p\ge1\), sharp-order quantitative brackets hold:
\[
\boxed{\frac{\alpha p}{\log(1+\varepsilon^{-p})}
\le\mathcal C_{\ell^p,\alpha}(\varepsilon)
\le\frac{\alpha}{\log((1-\varepsilon)/\varepsilon)}.}
\]
Consequently, for every listed \(X\),
\[
\boxed{\lim_{\varepsilon\downarrow0}
\mathcal C_{X,\alpha}(\varepsilon)\log(1/\varepsilon)=\alpha.}
\]
In particular the logarithmic return-growth order is optimal: suitable fixed vectors have \(\Theta(\log N)\) visits to this ball.

## Assumptions and scope
The scalar field is complex, the shift is the ordinary **unweighted** unilateral backward shift, and the polynomial factor \(n^\alpha\) scales the \(n\)-th operator rather than being a product of internal shift weights. Norms are the standard \(\ell^p\) or supremum norm. Open balls use strict inequality. The exact finite-radius formula is asserted for \(c_0\); for finite \(p\), only the displayed two-sided bounds and sharp small-radius limit are asserted, **not** an exact finite-radius coefficient. Topological mixing of an operator sequence means that for any two nonempty open sets \(V,W\subset X\), one has \(A_n(V)\cap W\ne\varnothing\) for all sufficiently large \(n\).

## Proof
**Mixing and universal orbits.** Denote by \(F\) the ordinary forward shift. Given nonempty open \(V,W\), choose finitely supported \(u\in V\), \(v\in W\). For all sufficiently large \(n\), the vector \(u+n^{-\alpha}F^nv\) lies in \(V\) and satisfies
\[
A_n(u+n^{-\alpha}F^nv)=v,
\]
proving mixing. To construct a single universal vector, choose a dense sequence \((v_j)_{j\ge1}\) of finitely supported vectors with every basic open set met infinitely often. Recursively choose integers \(n_j\) so the supports of \(F^{n_j}v_j\) are disjoint and
\[
\|v_j\|/n_j^\alpha<2^{-j},\qquad
n_i^\alpha\|v_j\|/n_j^\alpha<2^{-j}\quad(i<j).
\]
This is possible because \(\alpha>0\). The norm-convergent series \(x=\sum_{j\ge1}n_j^{-\alpha}F^{n_j}v_j\) satisfies
\[
\|A_{n_i}x-v_i\|\le\sum_{j>i}2^{-j}\le2^{-i},
\]
since earlier inserted blocks have disappeared under \(B^{n_i}\). Hence the orbit is dense. If \(\alpha\le0\), then \(\|A_nx\|\le\|B^nx\|\to0\) for every \(x\in X\), precluding density.

**Multiplicative separation and packing.** Suppose \(n<m\) both lie in \(E_x(\varepsilon)\). The zeroth coordinate of \(A_mx\) gives
\[
m^\alpha|x_m|>1-\varepsilon.
\]
The coordinate numbered \(m-n\ge1\) of \(A_nx-e_0\) gives \(n^\alpha|x_m|<\varepsilon\). Dividing yields
\[
\frac mn>\left(\frac{1-\varepsilon}{\varepsilon}\right)^{1/\alpha}=R_{\alpha,\varepsilon}>1.
\]
For \(X=\ell^p\), adding all later return-coordinate contributions to the \(p\)-th power of the norm also yields the stronger packing constraint, for every \(n\in E_x(\varepsilon)\):
\[
\sum_{\substack{m\in E_x(\varepsilon)\\m>n}}
\left(\frac nm\right)^{\alpha p}
<\left(\frac{\varepsilon}{1-\varepsilon}\right)^p.
\]
A finite increasing chain of return times in \([M,M+N]\) has consecutive ratios greater than \(R_{\alpha,\varepsilon}\), whereas the last-to-first ratio is at most \(N+1\): the first positive time is at least \(\max(1,M)\). Taking logarithms proves the uniform counting estimate and the density conclusions. It also gives
\[
\mathcal C_{X,\alpha}(\varepsilon)
\le\frac{1}{\log R_{\alpha,\varepsilon}}
=\frac{\alpha}{\log((1-\varepsilon)/\varepsilon)}.
\]

**Matching lower bounds.** Fix any real \(q>1\), let \(n_j=\lceil q^j\rceil\) for all sufficiently large \(j\), and set all coordinates of \(x\) to zero except \(x_{n_j}=a n_j^{-\alpha}\). These vectors lie in all spaces under discussion because the nonzero coordinates decrease geometrically. At the selected times the zeroth coordinate of \(A_{n_j}x\) equals \(a\), and the later coordinates are exactly \(a(n_j/n_k)^\alpha\) for \(k>j\). On \(\ell^p\), choosing \(a=1\) gives the exact limiting error
\[
\lim_{j\to\infty}\|A_{n_j}x-e_0\|_p
=\left(\sum_{h=1}^\infty q^{-\alpha ph}\right)^{1/p}
=(q^{\alpha p}-1)^{-1/p}.
\]
Thus every \(q>(1+\varepsilon^{-p})^{1/(\alpha p)}\) ensures all sufficiently late selected times are returns. Since \(\#\{j:n_j\le N\}\sim (\log N)/(\log q)\), taking \(q\) down to the indicated threshold proves the finite-\(p\) lower bound.

On \(c_0\), let \(q>R_{\alpha,\varepsilon}\) and choose
\[
1-\varepsilon<a<\min\{1+\varepsilon,\varepsilon q^\alpha\}.
\]
Then the limiting supremum-norm error is
\[
\max\{1-a,a q^{-\alpha}\}<\varepsilon.
\]
Hence \(\mathcal C_{c_0,\alpha}(\varepsilon)\ge1/\log q\). Letting \(q\downarrow R_{\alpha,\varepsilon}\) matches the universal upper bound, proving the exact formula. Finally multiply the two-sided logarithmic-frequency bounds by \(\log(1/\varepsilon)\) and send \(\varepsilon\downarrow0\). Both ends tend to \(\alpha\), proving the common small-ball law.

## Verification
Every result above follows from the explicit shift coordinates, the geometric-series identity, and a norm-convergent separated-block construction. The finite-grid supplementary diagnostic program in `diagnostics.py` tests the sharp constructions at sample parameters and does **not** replace the infinite-dimensional proof. The proof's only nontrivial limiting claims use the facts that \(\lceil q^j\rceil/q^j\to1\), a geometric sequence has logarithmic counting function, and geometric-series tails converge uniformly under fixed \(q>1\).

## Relationship to prior work
Li, Ruan and Yang [1] establish general weighted-orbit inclusion criteria and construct an unbounded-weight counterexample on the product space of all scalar sequences. Their proof gives a disjoint-block construction, but not the norm-controlled sharp logarithmic return-frequency law in the stated Banach spaces. Costakis and Parissis [2] prove a qualitative recurrence obstruction for frequently universal scalar-weighted operator sequences when successive weight ratios tend to one; applied to this strongly stable shift, that already excludes frequent universality. Thus **absence of frequent universality is not independently claimed as new**. The quantitative uniform logarithmic packing, the exact \(c_0\) supremum, and the universal sharp small-ball coefficient are the claimed refinements.

## Limitations
The finite-radius value \(\mathcal C_{\ell^p,\alpha}(\varepsilon)\) is not determined exactly for finite \(p\). The theorem does not classify arbitrary scalar weights or arbitrary shifts and makes no priority claim over possible equivalent return-frequency formulations. The quantitative estimates are not claims about positive-frequency return to every open set; a single fixed ball suffices to obstruct density-based universality. The supplementary numerical checks verify only sampled finite parameters.

## References
[1] J. Li, Y. Ruan, Y. Yang, *Weighted orbits of hypercyclic vectors on F-spaces*, arXiv:2611.04629v1 (first public November 3, 2026), https://arxiv.org/html/2611.04629v1.

[2] G. Costakis, I. Parissis, *Szemerédi's theorem, frequent hypercyclicity and multiple recurrence*, Mathematica Scandinavica 110 (2012), 251–272, https://doi.org/10.7146/math.scand.a-15207.
