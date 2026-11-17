# Reciprocal dynamical symmetry and an exact two-sided rotation-depth law at a shearless collision

## Finding
Let the biquadratic nontwist map be
\[
F_{a,b,\varepsilon}(x,y)=\bigl(x+a(1-Y^2)(1-\varepsilon Y^2)\pmod 1,\,Y\bigr),\qquad Y=y-b\sin(2\pi x).
\]
For every \(a>0\), \(\varepsilon>0\), and real \(b\), the coordinate rescaling \(C_\varepsilon(x,y)=(x,\sqrt\varepsilon\,y)\) obeys the exact conjugacy
\[
C_\varepsilon\circ F_{a,b,\varepsilon}\circ C_\varepsilon^{-1}
=F_{a,\sqrt\varepsilon b,\,1/\varepsilon}.
\]

In the integrable subfamily \(b=0\), fix \(\varepsilon\ne1\). The **negative lifted-rotation band** is the full invariant set
\[
\mathcal N_\varepsilon=\{(x,y):x\in\mathbb R/\mathbb Z,\ \min(1,\varepsilon^{-1/2})<|y|<\max(1,\varepsilon^{-1/2})\}.
\]
It has symplectic area \(\mathcal A_\varepsilon=2|1-\varepsilon^{-1/2}|\). Sample \((X,Y)\) from normalized Lebesgue area on this band, set \(e=\sqrt\varepsilon\), and define the negative lift rotation \(W=-a(1-Y^2)(1-\varepsilon Y^2)>0\), its maximum \(M=a(\varepsilon-1)^2/(4\varepsilon)\), and its normalized depth \(Z=W/M\in(0,1)\).

For every \(0<z<1\), put \(s=\sqrt{1-z}\) and
\[
A_\pm=\frac{1+e^2\pm(1-e^2)s}{2}.
\]
The entire conditional rotation-depth distribution is
\[
\boxed{\Pr_\varepsilon(Z>z)=\frac{(1+e)s}{\sqrt{A_+}+\sqrt{A_-}}.}
\]
It is **exactly reciprocal-invariant**: the law at \(\varepsilon\) equals that at \(1/\varepsilon\). Moreover, if
\[
r=\frac{|1-e|}{1+e}=\tanh\bigl(|\log\varepsilon|/4\bigr),
\]
then \(\Pr_\varepsilon(Z>z)\) is strictly decreasing in \(r\) for every \(0<z<1\). Thus the entire normalized rotation-depth law becomes strictly stochastically larger as \(\varepsilon\) approaches \(1\) from **either** side in logarithmic parameter distance.

At the collision, the negative band itself vanishes, but the normalized laws have the nondegenerate, two-sided limit
\[
\boxed{Z\ \Longrightarrow\ \operatorname{Beta}(1,1/2),\qquad
\Pr(Z>z)\longrightarrow\sqrt{1-z}.}
\]
Their moments are exactly
\[
\mathbb E[Z]=\frac{8(e^2+3e+1)}{15(e+1)^2},\quad
\operatorname{Var}(Z)=\frac{64(3e^4+8e^3+13e^2+8e+3)}{1575(e+1)^4}.
\]
The mean increases strictly and the variance decreases strictly as \(r\downarrow0\), with limiting values \(2/3\) and \(4/45\), respectively.

The total (un-normalized) reverse angular-displacement flux over the band is
\[
\boxed{\mathcal J_\varepsilon=\int_{\mathcal N_\varepsilon}W\,dx\,dy
=\frac{4a|e-1|^3(e^2+3e+1)}{15e^3}
\sim\frac a6|\varepsilon-1|^3.}
\]
Consequently the band area, maximum reverse rotation, and integrated reverse flux vanish with the respective exact critical powers \(1,2,3\).

## Assumptions and scope
The map acts on \((\mathbb R/\mathbb Z)\times\mathbb R\). The conjugacy holds algebraically for any \(a>0\), \(b\in\mathbb R\), and \(\varepsilon>0\); a transformation may carry \(b\) outside a physically restricted parameter interval. The probability law, moments, monotonicity and flux concern **only \(b=0\)** and \(\varepsilon\ne1\), with natural finite normalized area on the full negative-lift band, not a uniquely selected ergodic measure. The rotation is the real lift increment, **not** its residue modulo one. At \(\varepsilon=1\), the band is empty; no probability on it is claimed, only a two-sided limit.

## Proof
**1. Conjugacy.** Write \(e=\sqrt\varepsilon\) and \(v=e y\). Under \(C_\varepsilon\), the kick becomes \(v'=v-eb\sin(2\pi x)\), while
\[
a(1-(v'/e)^2)(1-e^2(v'/e)^2)=a(1-v'^2/e^2)(1-v'^2).
\]
This is precisely the reciprocal-parameter map, with unchanged angular coordinate. The map is an exact diffeomorphism conjugacy for every positive \(e\), without treating \(C_\varepsilon\) as area-preserving.

**2. Band and density.** For \(b=0\), each \(y\) is invariant and the lift rotation equals \(\omega(y)=a(1-y^2)(1-e^2y^2)\). Its negative set is exactly \(\mathcal N_\varepsilon\), and its unique magnitude maximum on each component occurs at \(y^2=(1+e^2)/(2e^2)\), giving \(M\). After conditioning on the band, \(T=e|Y|\) is uniform on the interval with endpoints \(e\) and \(1\). The variable
\[
U=\frac{T^2-e^2}{1-e^2},\qquad 0<U<1,
\]
has density
\[
f_e(u)=\frac{e+1}{2\sqrt{e^2+(1-e^2)u}},\qquad 0<u<1.
\]
The map's exact factorization implies \(Z=4U(1-U)\). For \(s=\sqrt{1-z}\), the event \(Z>z\) is \((1-s)/2<U<(1+s)/2\). Integrating \(f_e\) between those endpoints gives the displayed survival probability, including the correct absolute endpoint orientation when \(e>1\).

**3. Reciprocal symmetry and strict order.** Replacing \(e\) by \(1/e\) sends \(f_e(u)\) to \(f_e(1-u)\). Since \(4u(1-u)\) is unchanged under \(u\mapsto1-u\), all normalized rotation-depth distributions coincide under reciprocal parameters. To prove strict stochastic ordering without guessing from moments, put \(r=|1-e|/(1+e)\) and \(s=\sqrt{1-z}\). Direct algebra yields
\[
\left(\frac{\Pr_\varepsilon(Z>z)}s\right)^2
=\frac{2}{1+r^2+\sqrt{(1+r^2)^2-4r^2s^2}}.
\]
The denominator is strictly increasing for \(0<r<1\), \(0<s<1\), since its derivative is
\[
2r\left(1+\frac{1+r^2-2s^2}{\sqrt{(1+r^2)^2-4r^2s^2}}\right)>0,
\]
and the square of the radical minus \((1+r^2-2s^2)^2\) equals \(4s^2(1-s^2)>0\). Thus every interior survival probability increases strictly as \(r\downarrow0\). In this limit \(f_e\to1\) uniformly on \([0,1]\), and \(4U(1-U)\) with \(U\) uniform has survival \(\sqrt{1-z}\), proving the beta limit.

**4. Moments and critical exponents.** Uniformity of \(T\) gives
\[
\mathbb E[Z^k]=\frac1{|1-e|}\int_{\min(e,1)}^{\max(e,1)}
\left[\frac{4(t^2-e^2)(1-t^2)}{(1-e^2)^2}\right]^kdt,
\quad k=1,2.
\]
Polynomial integration yields the quoted mean and variance. Their derivatives with respect to \(e\) are
\[
\frac{d}{de}\mathbb E[Z]=\frac{-8(e-1)}{15(e+1)^3},\qquad
\frac{d}{de}\operatorname{Var}(Z)=\frac{128(e-1)(2e^2+e+2)}{1575(e+1)^5},
\]
which establish the asserted monotonicities on each side. The band area and \(M\) are explicit, and \(\mathcal J_\varepsilon=\mathcal A_\varepsilon M\mathbb E[Z]\) simplifies to the flux expression. As \(\varepsilon\to1\), \(|e-1|\sim|\varepsilon-1|/2\); hence the area has power one, \(M\) power two, and flux power three with coefficient \(a/6\).

## Verification
The standalone `verify.py` checks the reciprocal polynomial identity, the exact quadratic depth reduction, first and second moments, both derivative formulas, the flux identity and its limiting coefficient, and the reciprocal moment symmetry in exact SymPy algebra. It also evaluates independent high-precision quadratures for seven parameters on both sides of \(\varepsilon=1\), with three interior tail thresholds per parameter. All checks pass. The strict stochastic ordering and global quantifiers rest on the displayed analytic derivative argument, not on the sampled computations.

## Relationship to prior work
Grime, Roberto, Viana, Elskens and Caldas introduce the biquadratic nontwist map and analyze shearless curves, rotation profiles, primary periodic orbits and reconnections. Their public preprint first appeared on 2022-09-15. Their 2023 continuation analyzes breakup and transport barriers; the 2024 preprint by Grime and collaborators analyzes effective transport in perturbed maps. These results motivate the \(\varepsilon=1\) collision and the negative-frequency band but do not state the conditional area-weighted frequency distribution, strict two-sided stochastic order or exact integrated reverse-flux law proved here. Separately, a publicly indexed fixed-point-winding classification for the same map addresses integer-winding orbit counts and elliptic thresholds, not these continuous measure-distribution assertions. Parameter rescaling and the underlying quartic profile alone are elementary; the differentiated contribution is the complete natural-area law together with ordering, limiting distribution and flux exponents.

## Limitations
The nonintegrable map with \(b\ne0\) need not preserve the negative-lift band and the conditional distribution formula is not asserted there; only the reciprocal conjugacy extends to it. Uniform Liouville area on the integrable band is a particular natural invariant ensemble; individual invariant circles carry their own rotation and no mixing is claimed. There is no stationary ensemble on the collapsed band at \(\varepsilon=1\). Rotation frequencies are real lift values, not circle rotation numbers modulo integers. An inaccessible full text of one closely related publicly indexed fixed-point-winding result and possible unindexed equivalent integral formulas are residual publication-priority risks. Independent audit is not asserted.

## References
1. G. C. Grime, M. Roberto, R. L. Viana, Y. Elskens, I. L. Caldas, *Biquadratic Nontwist Map: a model for shearless bifurcations*, arXiv:2209.07408v1 (first posted 2022-09-15); published in *Chaos, Solitons & Fractals* 169 (2023), article 113231. https://arxiv.org/abs/2209.07408 ; https://doi.org/10.1016/j.chaos.2023.113231.
2. G. C. Grime et al., *Shearless curve breakup in the biquadratic nontwist map*, arXiv:2305.17538v1 (2023-05-27). https://arxiv.org/abs/2305.17538.
3. G. C. Grime et al., *Effective transport barriers in the biquadratic nontwist map*, arXiv:2409.00785v1 (2024-09-01). https://arxiv.org/abs/2409.00785.
4. *Global integer-winding fixed-point spectrum and sharp elliptic staircase of the biquadratic nontwist map*, publicly indexed mathematical result (2026-11-02); https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-global-integer-winding-fixed-point-spectrum-and-sharp-elliptic-s--f0775f13bc35 (full text not retrieved).
