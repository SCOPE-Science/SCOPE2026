# Sharp thermal-offset boundaries for the irreversibility peak of a polytropic harmonic stroke

## Finding

The harmonic finite-time polytropic-steering formulas have a **complete, sharp parameter classification** of whether their irreversible-entropy-generation curve has an interior maximum. Such a peak need not exist: sufficiently large initial temperature mismatch eliminates it, with different exact boundaries for compression and expansion.

Fix a stiffness endpoint ratio \(u>0\), \(u\ne1\), an initial relative temperature offset \(\delta>-1\), \(\delta\ne0\), and a positive entropy normalization \(\chi\). Assume either **compression** \(u>1,\delta>0\) or **expansion** \(0<u<1,-1<\delta<0\). Let \(x=-\xi\in[0,1]\) be minus the polytropic index. With its continuous value at \(x=0\), the irreversible entropy of the prescribed harmonic stroke is

\[
\mathcal S(x)=\chi(1-x)\left[(1+\delta)\frac{u^x-1}{x}-\log u\right]. \tag{1}
\]

Here \(\chi=1\) for the cited underdamped harmonic formula and \(\chi=1/2\) for its overdamped entropy expression. The first theorem is a mathematical statement about (1), independent of the choice of \(\chi>0\).

**Compression.** Put \(L=\log u>0\). If \(0<L<2\), a unique interior strict global maximum exists **if and only if**

\[
0<\delta<\delta_c(L):=\frac{L}{2-L}. \tag{2}
\]

For \(\delta\ge\delta_c(L)\), \(\mathcal S\) is strictly decreasing on \([0,1]\). If \(L\ge2\), there is a unique interior strict global maximum for every \(\delta>0\). In every peak regime the derivative is positive before the maximizer and negative after it.

**Expansion.** Put \(\ell=-\log u>0\) and \(\eta=-\delta\in(0,1)\). A unique interior strict global maximum exists **if and only if**

\[
0<\eta<\eta_c(\ell):=\frac{\ell}{2+\ell}. \tag{3}
\]

For \(\eta\ge\eta_c(\ell)\), \(\mathcal S\) is strictly decreasing on \([0,1]\). Thus the peak is neither universally present nor multiply attained in these physical sign regimes.

The associated underdamped stroke-duration parametrization from the same harmonic theory is

\[
\tau(x)=\frac{1-x}{\gamma x}\log\left[(1+\delta^{-1})u^x-\delta^{-1}\right],\quad 0<x<1,\ \gamma>0. \tag{4}
\]

It is strictly decreasing in \(x\) in both sign regimes. Consequently the preceding classification and uniqueness apply equally to the interior peak **as a function of duration**. The largest duration along this fixed-offset family is finite:

\[
\lim_{x\downarrow0}\tau(x)=\frac{(1+\delta)|\log u|}{\gamma|\delta|},\qquad \lim_{x\uparrow1}\tau(x)=0. \tag{5}
\]

The peak disappears through the slow-duration endpoint. Its location has a sharp linear onset: as \(\delta\uparrow\delta_c(L)\) at fixed \(0<L<2\),

\[
x_*=\frac{(2-L)^2}{4L(1-L/3)}(\delta_c-\delta)+O((\delta_c-\delta)^2). \tag{6}
\]

As \(\eta\uparrow\eta_c(\ell)\) for expansion,

\[
x_*=\frac{(2+\ell)^2}{4\ell(1+\ell/3)}(\eta_c-\eta)+O((\eta_c-\eta)^2). \tag{7}
\]

In particular, an endpoint ratio \(u=3/2\) has \(L=\log(3/2)\) and critical compression mismatch \(\delta_c=\log(3/2)/(2-\log(3/2))\). Below it the peak is interior; at or above it no interior maximizer remains.

## Assumptions and scope

This is an exact analysis of the explicitly given *harmonic polytropic-steering entropy function* and, for the duration assertion, of the cited underdamped stroke-duration formula. The two parameters \(u\) and \(\delta\) are fixed while \(x\) varies from \(0\) (isothermal-index endpoint) to \(1\) (adiabatic-index endpoint). The classification does not extend to independent arbitrary controls, arbitrary initial distributions, or arbitrary anharmonic potentials. Its thermodynamic application inherits the dynamical assumptions and scale separation under which those harmonic expressions were derived; it is not an all-times theorem for a general Langevin model. At nonzero fixed mismatch the slow-index duration endpoint is **finite**, not literally an infinite-time equilibrium limit.

Every endpoint is understood by continuity; the value at \(x=0\) is \(\chi\delta\log u>0\), and the value at \(x=1\) is zero. The exact equality cases in (2) and (3) have a horizontal tangent at \(x=0\), but strictly negative derivative for all \(x>0\).

## Proof

**1. A strictly monotone duration coordinate.** Set \(K(x)=\log[(1+\delta^{-1})u^x-\delta^{-1}]\). In compression, with \(L=\log u\), it is \(K(x)=\log[1+c(e^{Lx}-1)]\) with \(c=(1+\delta)/\delta>1\). Then \(K(0)=0\), \(K(x)>0\), and

\[
K''(x)=\frac{L^2c(1-c)e^{Lx}}{[1+c(e^{Lx}-1)]^2}<0.
\]

In expansion, \(K(x)=\log[1+c(1-e^{-\ell x})]\) with \(c=(1-\eta)/\eta>0\); it is again positive for \(x>0\), vanishes at zero, and has strictly negative second derivative. Concavity yields \(K(x)/x>0\) strictly decreasing. Equation (4) is the product of this quantity and the positive strictly decreasing factor \(1-x\), so \(\tau\) is strictly decreasing. Its endpoint limits follow by differentiating \(K\) at zero. This proves (5), as well as the equivalence between extrema in \(x\) and extrema in duration.

**2. Expansion has a strictly decreasing derivative.** Write \(g_-(x)=(1-e^{-\ell x})/x=\int_0^\ell e^{-sx}\,ds\). Then

\[
\frac{\mathcal S(x)}\chi=(1-x)[\ell-(1-\eta)g_-(x)],\quad
\frac{\mathcal S'(x)}\chi=-\ell+(1-\eta)H_-(x),
\]

where \(H_-(x)=g_-(x)-(1-x)g_-'(x)\). Because \(g_-'<0\) and \(g_-''>0\),

\[
H_-'(x)=2g_-'(x)-(1-x)g_-''(x)<0\quad(0\le x\le1).
\]

Moreover \(H_-(0)=\ell+\ell^2/2\) and \(H_-(1)=1-e^{-\ell}<\ell\). Hence \(\mathcal S'(1)<0\) and the derivative has at most one zero; it has an interior zero exactly when \(\mathcal S'(0)>0\). That last inequality is \((1-\eta)(1+\ell/2)>1\), equivalent to (3). At equality the derivative is negative at every positive \(x\); otherwise its sign classification gives strict monotonicity or a unique global maximum.

**3. Compression and the global shape lemma.** Write \(g_+(x)=(e^{Lx}-1)/x=\int_0^L e^{sx}\,ds\) and \(H_+(x)=g_+(x)-(1-x)g_+'(x)\). Then

\[
\frac{\mathcal S'(x)}\chi=L-(1+\delta)H_+(x),\quad
H_+(0)=L-\frac{L^2}{2},\quad H_+(1)=e^L-1>L.
\]

We prove that \(H_+\) is strictly increasing if \(L\le3\), whereas if \(L>3\) it decreases to one minimum and then increases. Let \(F(y)=(e^y-1)/y=\int_0^1e^{yt}\,dt\), analytically continued at zero, and set \(y=Lx\). Direct differentiation gives

\[
H_+'(x)=L^2F''(y)[B(y)-L],\qquad B(y)=y+\frac{2F'(y)}{F''(y)}.
\]

The derivatives \(F',F'',F'''\) are strictly positive for \(y\ge0\). A direct algebraic identity gives, for \(y>0\),

\[
3F''(y)^2-2F'(y)F'''(y)=\frac{e^y}{y^4}\big[e^y(y^2-4y+6)-2y-6\big]>0. \tag{8}
\]

Indeed, the bracket \(q(y)\) has \(q(0)=q'(0)=0\) and \(q''(y)=y^2e^y>0\), so it is strictly positive for \(y>0\). Thus

\[
B'(y)=\frac{3F''(y)^2-2F'(y)F'''(y)}{F''(y)^2}>0,
\quad B(0)=3,
\quad B(L)>L.
\]

If \(L\le3\), this makes \(H_+'(x)>0\) for all \(x\in(0,1)\). If \(L>3\), \(B(y)=L\) has one and only one solution in \((0,L)\); the sign of \(H_+'\) changes there from negative to positive.

For \(0<L<2\), \(H_+(0)>0\) and \(H_+\) increases strictly, so the threshold level \(L/(1+\delta)\) is crossed in the interior exactly when \(H_+(0)<L/(1+\delta)\), equivalent to \(\delta<L/(2-L)\). In the equality and larger-mismatch cases, \(\mathcal S'(x)<0\) for all \(x>0\).

For \(L\ge2\), \(H_+(0)\le0<L/(1+\delta)\), and \(H_+(1)>L/(1+\delta)\). If \(L\le3\), the strict increase gives exactly one crossing. If \(L>3\), the initial decreasing branch lies below the positive threshold, and the strictly increasing second branch crosses exactly once. In every case with a crossing, \(\mathcal S'\) changes from positive to negative. This proves all compression assertions.

**4. Linear coalescence with the endpoint.** For \(0<L<2\), at the compression threshold the first derivative vanishes at zero and its derivative in \(x\) is \(-(1+\delta_c)L^2(1-L/3)<0\). The derivative of \(\mathcal S'(0)/\chi\) with respect to \(\delta\) is \(-L(1-L/2)\). The implicit-function theorem at this nondegenerate boundary root proves (6). For expansion, at \(\eta_c\), \(\partial_x(\mathcal S'/\chi)|_{x=0}=-(1-\eta_c)\ell^2(1+\ell/3)<0\) and \(\partial_\eta(\mathcal S'(0)/\chi)=-\ell(1+\ell/2)\), giving (7). The expansion coefficients are strictly positive.

## Verification

The accompanying `verify.py` checks the derivative identities and (8) symbolically using SymPy, then checks the strict-sign regimes and unique-root locations on ten compression/expansion parameter sets at high precision using mpmath. Four critical-window tests compare the numerically located root with the coefficients in (6) and (7). The checker is run by `python verify.py` with `sympy` and `mpmath` installed. These finite examples are diagnostics only; the preceding proof establishes the universal quantifiers.

## Relationship to prior work

Fu, Lin, Su and Ma introduced the harmonic finite-time polytropic entropy and duration expressions used in (1) and (4), and emphasized a nonmonotone entropy-production peak for illustrated parameter choices. Those **pointwise expressions and the occurrence of a peak in their studied regime are prior results**, not claimed here. The present contribution is a global mathematical classification: the peak can disappear altogether, the exact compression and expansion threshold surfaces and uniqueness hold throughout the specified parameter domains, and the peak collides linearly with the slow-duration endpoint. In particular, the large-\(L\) compression case requires the nontrivial one-minimum lemma in step 3, not just examination of an endpoint derivative.

The cited Brownian-engine and thermodynamic studies address different control protocols and/or optimization objectives; the classification here refers solely to the particular harmonic polytropic stroke. It is not a universal statement about entropy production under arbitrary protocols.

## Limitations

The entropy function (1) is adopted from the cited harmonic theory rather than derived anew from a microscopic stochastic differential equation. Its interpretation as an exact physical entropy for any experimental driving rate inherits that theory's timescale-separation and local-equilibrium assumptions, especially in the underdamped case. Equation (4) is the **underdamped** duration relation; no claim that it is the overdamped duration relation is made. The \(\chi=1/2\) overdamped entropy factor does not affect extrema as a function of the index, but (4) does not justify an overdamped duration reparametrization. The result does not claim novelty of the polytropic construction, entropy formula, or preexisting finite-duration endpoint. Independent validation and publication-priority review have not been performed. A previously unindexed detailed parameter analysis of the same entropy function could reduce or eliminate novelty.

## References

1. C. Fu, Y. Lin, S. Su and Y.-H. Ma, *Finite-time Polytropic Steering Reveals Non-monotonic Irreversibility*, arXiv:2602.13765 (first public version, 2026-02-14; version 2, 2026-10-21), https://arxiv.org/abs/2602.13765 . Relevant source formulas: harmonic stroke duration (Eq. 8) and entropy generation (Eq. 10) of version 2.
2. I. Prieto-Rodríguez, A. Prados and C. A. Plata, *Maximum-Power Stirling-like Heat Engine with a Harmonically Confined Brownian Particle*, Entropy 27 (2025), 72, https://doi.org/10.3390/e27010072 . Context on harmonic-trap heat-engine optimization, not a source of (1)–(3).
