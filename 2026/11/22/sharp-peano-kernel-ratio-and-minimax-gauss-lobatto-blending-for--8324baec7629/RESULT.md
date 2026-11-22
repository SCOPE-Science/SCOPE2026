# Sharp Peano-kernel ratio and minimax Gauss–Lobatto blending for sixth-derivative-sign quadrature

## Finding

Let \(G\) denote the three-node Gauss–Legendre rule and \(L\) the four-node Gauss–Lobatto rule on any nondegenerate real interval, both normalized to integrate constants exactly. Define
\[
c_* = \frac{25-6\sqrt{15}}{25-6\sqrt{15}+\sqrt5}
     =0.44072684457373244490\ldots.
\]
For every \(f\in C^6[a,b]\) whose sixth derivative has one sign,
\[
0\le \frac{\int_a^b f-G[f]}{L[f]-G[f]}\le c_*
\]
whenever the denominator is nonzero; if it is zero, all three values agree. Both endpoints of this ratio interval are optimal in the supremum/infimum sense over admissible smooth nonpolynomial functions. The inequalities reverse when \(f^{(6)}\le0\), but the ratio and certificate remain valid after dividing by the common signed gap.

The unique minimax real blending weight is \(q_*=c_*/2\). Specifically, writing \(Q_q=(1-q)G+qL\),
\[
\inf_{q\in\mathbb R}\ \sup_{f:\ f^{(6)}\text{ has one sign},\ L[f]\ne G[f]}
\frac{|\int f-Q_q[f]|}{|L[f]-G[f]|}
=\frac{c_*}{2}=0.22036342228686622245\ldots,
\]
with the infimum attained only at \(q=q_*\). The new positive-weight, degree-five-exact blended rule thus has a sharp, computable a posteriori error certificate
\[
\left|\int_a^b f-Q_{q_*}[f]\right|\le\frac{c_*}{2}|L[f]-G[f]|.
\]
The same inequality applies to the sum of the rules over any fixed finite partition, uniform or nonuniform, provided the sixth derivative has a single sign throughout the full interval. It requires exactly the evaluations already needed by the primitive Gauss and Lobatto rules. Compared with the published \(1/4\) certificate for its \(q=1/4\) blend, the sharp certificate constant improves by \(1-2c_*=0.1185463108525351\ldots\), or about \(11.85\%\).

## Assumptions and scope

The interval endpoints satisfy \(a<b\); the integrand is real-valued, belongs to \(C^6[a,b]\), and either \(f^{(6)}\ge0\) everywhere or \(f^{(6)}\le0\) everywhere. The rules are the classical degree-five-exact rules with nodes and weights, on \([0,1]\),
\[
G: \left(\frac{5-\sqrt{15}}{10},\frac12,\frac{5+\sqrt{15}}{10}\right),\quad
\left(\frac5{18},\frac8{18},\frac5{18}\right);
\]
\[
L:\left(0,\frac{5-\sqrt5}{10},\frac{5+\sqrt5}{10},1\right),\quad
\left(\frac1{12},\frac5{12},\frac5{12},\frac1{12}\right).
\]
Affine rescaling gives arbitrary intervals. The conclusion is a deterministic quadrature guarantee, not a claim about floating-point rounding, unknown derivative sign, or arbitrary noisy evaluations.

## Proof

Normalize to \([0,1]\). Put \(k_t(x)=(x-t)_+^5/120\), \(I[f]=\int_0^1 f(x)\,dx\), and define the sixth-order Peano kernels
\[
A(t)=I[k_t]-G[k_t],\qquad D(t)=L[k_t]-G[k_t].
\]
Exactness on polynomials of degree at most five gives the identities
\[
I[f]-G[f]=\int_0^1 f^{(6)}(t)A(t)\,dt,\qquad
L[f]-G[f]=\int_0^1 f^{(6)}(t)D(t)\,dt.
\]
Both kernels are symmetric about \(t=1/2\): reflection converts a right-truncated fifth power to a left-truncated fifth power, and their difference is a degree-five polynomial annihilated by both quadrature error functionals.

Set \(u=(5-\sqrt{15})/10\), \(v=(5-\sqrt5)/10\), \(R=25-6\sqrt{15}\), and \(T=R+\sqrt5\), so \(c_*=R/T\). For \(t\in[0,1/2]\), each kernel is an explicit degree-at-most-six piecewise polynomial, obtained from
\[
A(t)=\frac{(1-t)^6}{720}-\frac1{120}\sum_{g_j>t}w_j^G(g_j-t)^5,
\quad D(t)=\frac1{120}\left(\sum_{\ell_j>t}w_j^L(\ell_j-t)^5-\sum_{g_j>t}w_j^G(g_j-t)^5\right).
\]
On \([0,u]\), exact simplification yields \(A(t)=t^6/720\), \(D(t)=t^5/1440\), and
\[
T(c_*D(t)-A(t))=\frac{t^5(R-2Tt)}{1440}\ge0,
\]
with strict positivity inside that segment. The inequality follows from the exact bound \(R-2Tu>0\).

For \([u,v]\), use the affine coordinate \(s=(t-u)/(v-u)\). The degree-six polynomial \(H(t)=RD(t)-TA(t)\) has all seven Bernstein coefficients strictly positive. For \([v,1/2]\), the exact polynomial \(H(t)\) is divisible by \((1/2-t)^2\); its quotient is degree four and has all five Bernstein coefficients strictly positive in the affine coordinate \(s=(t-v)/(1/2-v)\). Thus \(0\le A(t)\le c_*D(t)\) on the entire interval. Independently, the piecewise kernels \(A,D\) have strictly positive Bernstein coefficients on the last two segments, while their first-segment forms above are positive for \(t>0\). The coefficient assertions are exact algebraic sign statements: the self-contained `verify_peano.py` expands the polynomial formulas in \(\mathbb Q(\sqrt3,\sqrt5,\sqrt{15})\), converts to Bernstein form, and uses rational upper/lower square-root brackets produced by integer square roots at denominator \(10^{70}\). All 39 required algebraic sign intervals have strictly positive rational lower endpoints; the code also proves the factors and divisibility identities, not merely their sampled values.

At the midpoint, direct exact substitution yields \(A(1/2)/D(1/2)=R/T=c_*\). For positive \(t\downarrow0\), the first-segment formulas yield \(A(t)/D(t)=2t\to0\). Hence these are the sharp extreme kernel ratios. For an arbitrary nonnegative, nonzero continuous \(f^{(6)}\), the functional error ratio is a \(D(t)f^{(6)}(t)\)-weighted mean of \(A(t)/D(t)\), and therefore lies in \([0,c_*]\). Choosing continuous nonnegative bump sixth derivatives increasingly concentrated near the midpoint, or near a small positive \(t\), makes the ratio approach the respective extreme. Integrating the bumps six times supplies admissible \(C^6\) test functions. Replacing \(f\) by \(-f\) covers nonpositive sixth derivatives.

For any real \(q\), the normalized blended error is \(|r-q|\) where \(r\) ranges densely up to both ends of \([0,c_*]\). Therefore its sharp supremum is \(\max\{|q|,|c_*-q|\}\), uniquely minimized at \(q_*=c_*/2\). For a finite partition, apply the same Peano inequalities on each cell. Since the local gaps have one common sign, their sums preserve \(0\le (I-G_{\mathcal P})/(L_{\mathcal P}-G_{\mathcal P})\le c_*\). Concentration in a single cell gives sharpness for every fixed finite partition.

## Verification

Run `python verify_peano.py` with Python 3 and SymPy. It reconstructs both sets of nodes and weights, checks twelve exact polynomial moment identities, proves all three piecewise Peano-kernel identities and midpoint equality, verifies 39 exact positive radical-interval certificates, and reports the optimal weight and improvement. The algebraic Bernstein certificates are finite exhaustive checks of explicitly specified polynomial pieces, not sampling arguments. The continuum claim follows from positivity of the Bernstein basis on each subinterval and the Peano integral representation.

## Relationship to prior work

Komisarski and Wąsowicz (2016 preprint; 2017 journal paper) proved the weaker remainder comparison \(0\le I-G\le L-I\), giving the upper ratio bound \(1/2\); their proof uses a nonnegative Peano kernel. Wąsowicz (2026, first public 23 January) used that bound to select \(Q=(3G+L)/4\) and an a posteriori \(1/4\)-gap certificate. The present result uses the *sharp* kernel-ratio supremum \(c_*<1/2\), classifies the minimax coefficient, and proves its optimality for smooth one-signed-sixth-derivative functions. Komisarski and Wąsowicz (2022) optimized different degree-three quadratures on 3-convex functions; this is useful methodological precedent, but their statements do not entail the present specific four-node Lobatto/sixth-order ratio or constant.

## Limitations

The strength is relative to the gap \(|L-G|\), not an absolute a priori error bound when the sixth-derivative sign is unknown. The improvement is in the guaranteed error constant, not an established universal wall-clock speedup or guaranteed reduction in subdivisions at every tolerance. It uses seven distinct quadrature nodes per panel, the same as the pre-existing blend; it does not optimize node placement or the number of function evaluations across all possible rules. Sharpness is in a limit of smooth admissible integrands and need not be attained by a single nonpolynomial \(C^6\) function. No independent audit has been performed.

## References

1. S. Wąsowicz, *Adaptive integration of 5-convex and 5-concave functions*, arXiv:2601.16796v1, first public 2026-01-23, https://arxiv.org/abs/2601.16796; journal version: *Adaptive integration of functions maintaining a constant sign of the sixth derivative*, Aequationes Mathematicae 100 (2026), article 90, https://doi.org/10.1007/s00010-026-01333-2.
2. A. Komisarski and S. Wąsowicz, *Inequalities between remainders of quadratures*, arXiv:1612.08086v1 (2016), https://arxiv.org/abs/1612.08086; Aequationes Mathematicae 91 (2017), 1103–1114, https://doi.org/10.1007/s00010-017-0505-8.
3. A. Komisarski and S. Wąsowicz, *On optimal inequalities between three-point quadratures*, Aequationes Mathematicae 96 (2022), 621–638, https://doi.org/10.1007/s00010-022-00868-4.
