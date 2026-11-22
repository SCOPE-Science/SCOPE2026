# Cubic endpoint Sobolev rotations: a two-turning-point angular profile

## Finding
Let \(W^{3,1}(\mathbb R^2;\mathbb R)\) carry the complete, unweighted norm
\[
N_3(f)=\sum_{j=0}^3\sum_{a=0}^j\|\partial_x^{j-a}\partial_y^a f\|_{L^1(\mathbb R^2)}.
\]
For the planar rotation \(R_\theta\), set \(U_\theta f=f\circ R_\theta\) and let \(\phi=\operatorname{dist}(\theta,(\pi/2)\mathbb Z)\in[0,\pi/4]\), \(r=\tan\phi\in[0,1]\). Then its **exact** operator norm is
\[
\boxed{\|U_\theta\|_{N_3\to N_3}=\begin{cases}
\dfrac{1+5r+r^2-r^3}{(1+r^2)^{3/2}},&0\le r\le1/\sqrt2,\\[4pt]
\dfrac{-1+5r+5r^2-r^3}{(1+r^2)^{3/2}},&1/\sqrt2\le r\le1.
\end{cases}}
\]
On \(0<\phi<\pi/4\), this profile rises strictly to a smooth local maximum at \(r=r_*\), falls strictly to a nonsmooth local minimum at \(r=1/\sqrt2\), then rises strictly to its global maximum at \(r=1\). Here \(r_*\) is the unique positive root of
\[
r^3+13r^2+r-5=0,\qquad 0.57<r_*<0.58.
\]
In particular,
\[
\boxed{\sup_{\theta\in\mathbb R}\|U_\theta\|=2\sqrt2,}
\]
attained precisely for \(\theta\in\pi/4+(\pi/2)\mathbb Z\). The operator is an isometry precisely at quarter-turn multiples \(\theta\in(\pi/2)\mathbb Z\). Its norm is not attained by a nonzero Sobolev function at any other angle.

The interior smooth maximum and cusp minimum are distinct: \(\|U_{\arctan r_*}\|\approx2.6161789\), whereas the cusp value is \(\|U_{\arctan(1/\sqrt2)}\|\approx2.5485474\). The global maximum moves to a diagonal rotation at cubic order, unlike the quadratic derivative-sum profile whose diagonal angle is a local minimum.

## Assumptions and scope
All functions are real valued, defined on the whole plane with Lebesgue measure; weak partial derivatives through order three are integrable. Each distinct mixed derivative is counted **once**, without multinomial weights. Angles and rotations are real, and the operator norm is the supremum of \(N_3(U_\theta f)/N_3(f)\) over nonzero functions. The result does not use an Euclidean-tensor norm on the entire third derivative.

A published input is Ornstein's same-order \(L^1\) non-inequality: a scalar homogeneous constant-coefficient differential operator cannot have its \(L^1\) norm controlled by finitely many others of the same homogeneous order unless it is in their linear span. Consequently, for any fixed one of the four cubic monomial derivatives and any \(\varepsilon>0\), there is \(f\in C_c^\infty(\mathbb R^2;\mathbb R)\) for which the sum of the other three cubic derivative \(L^1\) norms is at most \(\varepsilon\) times the selected derivative norm. This is cited prior mathematics, not a new theorem.

## Proof
**1. Symmetry reduction.** Quarter-turns and coordinate reflections permute the derivative slots, hence act isometrically. Their products reduce the norm of any rotation to \(\phi\in[0,\pi/4]\). Put \(c=\cos\phi\ge s=\sin\phi\ge0\), \(r=s/c\). A rotation preserves planar measure, and under composition its derivative operators transform as \(\partial_x\mapsto c\partial_x+s\partial_y\), \(\partial_y\mapsto-s\partial_x+c\partial_y\), with the derivatives on the right evaluated at \(R_\phi(x,y)\).

**2. Cubic jet columns.** In the order \((f_{xxx},f_{xxy},f_{xyy},f_{yyy})\), the column of transformed cubic derivatives sourced by \(f_{xxy}\) has coefficients
\[
(3c^2s,\ c(c^2-2s^2),\ s(s^2-2c^2),\ 3cs^2).
\]
The \(f_{xyy}\) column has the same absolute column sum by symmetry. Their common absolute sum is
\[
L_3=3c^2s+c|c^2-2s^2|+s(2c^2-s^2)+3cs^2.
\]
The pure-cubic columns have absolute sum \(c^3+c^2s+cs^2+s^3=c+s\). At order two, the largest absolute column sum is \(L_2=c^2-s^2+4cs\) (from the mixed derivative), and order one has column sum \(L_1=c+s\). Order zero has sum \(1\). By the chain rule and triangle inequality,
\[
N_3(U_\phi f)\le \max\{1,L_1,L_2,L_3\}N_3(f).
\]
The cubic mixed sum dominates all lower orders. Indeed, \(L_2\ge L_1\ge1\), and, after substituting \(c=(1+r^2)^{-1/2}\), the difference of squared numerators for \(L_3\) and \(L_2\) equals respectively
\[
\begin{cases}
2r(3r^4-12r^3+4r^2+6r+1),&0\le r\le1/\sqrt2,\\
-2r(r^4-26r^2+9),&1/\sqrt2\le r\le1.
\end{cases}
\]
Both are nonnegative, and positive if \(r>0\): in the first polynomial, \(6r-12r^3\ge0\) and all remaining displayed terms are nonnegative; in the second, \(r^4-26r^2+9\le1-13+9<0\). Similarly \(L_2^2-L_1^2=-2r(5r^2-6r-3)/(1+r^2)^2\ge0\). The two mixed cubic columns beat the pure ones: on the first interval their numerator difference is \(2r(2-r^2)\ge0\), and on the second it is \(-2(r+1)(r^2-3r+1)\ge0\). Hence \(\|U_\phi\|\le L_3\), and resolving the one absolute value in \(L_3\) gives the asserted two-branch formula.

**3. Sharpness in the genuine Sobolev space.** Apply Ornstein's non-inequality to the cubic monomial \(f_{xxy}\) versus the other three third derivatives to choose \(g_n\in C_c^\infty\) satisfying
\[
\|g_{n,xxx}\|_1+\|g_{n,xyy}\|_1+\|g_{n,yyy}\|_1\le n^{-1}\|g_{n,xxy}\|_1.
\]
For each \(n\), dilate \(h_n(x,y)=g_n(x/\delta_n,y/\delta_n)\) with sufficiently small \(\delta_n\) that the sum of its zeroth-, first- and second-derivative \(L^1\) norms is at most \(n^{-1}\|h_{n,xxy}\|_1\); this is possible since an order-\(j\) derivative scales as \(\delta_n^{2-j}\). For each output cubic derivative, the reverse triangle inequality removes an error bounded by a fixed multiple of the other three cubic norms. Summing yields
\[
\liminf_{n\to\infty}\frac{N_3(U_\phi h_n)}{N_3(h_n)}\ge L_3.
\]
Thus equality with the chain-rule bound is exact for every real angle. No false independence assumption about prescribing jet coordinates is made; the unbounded ratio required for concentration comes from the cited Ornstein theorem.

**4. Angular profile and sharp maximum.** On the first branch, differentiation gives derivative sign proportional to
\(5-r-13r^2-r^3\), a strictly decreasing function with exactly one zero \(r_*\) in \((57/100,29/50)\). On the second branch the derivative sign is that of \((1-r)(5r^2+18r+5)\), positive on \([1/\sqrt2,1)\). Hence \(1/\sqrt2\) is a strict cusp minimum and \(r_*\) a strict smooth local maximum. The first branch's maximum is smaller than \(8/3\): its numerator increases in the interval, and
\[
\frac{1+5(29/50)+(29/50)^2-(29/50)^3}{(1+(57/100)^2)^{3/2}}<\frac83.
\]
This last inequality follows after squaring positive rational quantities and is also checked in the companion exact-arithmetic script. Since \(8/3<2\sqrt2\), the global maximum is the second branch's value \(2\sqrt2\) at \(r=1\), and nowhere else modulo quarter-turns. Isometry requires \(L_3=1\), which occurs only at \(r=0\).

**5. Nonattainment.** For \(r>0\), the degree-zero mass \(\|f\|_1\) has coefficient \(1<L_3\). The separately bounded homogeneous degrees satisfy \(N_3(U_\phi f)\le\sum_{j=0}^3L_jN^{\mathrm{hom}}_j(f)\), with \(L_0=1\) and \(L_j\le L_3\). Since \(N^{\mathrm{hom}}_0(f)>0\) for nonzero \(f\), strict inequality holds in the full norm estimate. For \(r=0\), each quarter-turn is an isometry and every nonzero \(f\) attains norm one.

## Verification
Run `python check_rotation3.py` (standard library only). The exact-rational checker constructs the derivative-coefficient matrices for 1,201 rational Pythagorean rotations, confirms all absolute column sums and degree dominance, checks both piecewise formulas and the upper bound \(L_3^2\le8\), and independently confirms the strict rational enclosure and bound used to compare the local and global maxima. Expected printed marker: `CUBIC_ROTATION_EXACT_DIAGNOSTICS_OK 1201`. These finite checks only verify algebraic instances; the complete proof above supplies the universal inequalities, spectral shape and infinite-dimensional sharpness via the cited Ornstein theorem.

## Relationship to prior work
Hamad's recent isometry classification establishes the real complete derivative-sum Sobolev norm and its rigid isometries, but not the norm distortion of nonisometric rotations. The earlier exact quadratic-jet rotation result gives \(\|U_\theta\|=2|\sin2\theta|+|\cos2\theta|\) and an oblique global maximizing angle, with a cusp minimum at diagonal angles. The present cubic-jet result has a **different global maximizer at diagonal angles**, plus a new interior smooth local maximum and an interior cusp minimum. Neither statement implies the other across derivative orders. Another earlier exact theorem concerns *shear*, rather than rotational, coordinate changes at all orders; factoring a rotation into shears only yields submultiplicative estimates, not the present equality or turning points. The essential top-order concentration mechanism is Ornstein's classical non-inequality and is not asserted to be new. Claims of priority remain subject to less-indexed general composition-operator literature.

## Limitations
The sharp formula concerns only the real planar order-three, each-derivative-once \(L^1\) norm and linear rotations. It does not claim a general all-order phase diagram, nonlinear diffeomorphism estimates or norm-attaining extremizers at nontrivial angles. The Ornstein concentration gives extremizing sequences, not a finite construction. The exact rational program is supplementary and cannot certify the infinite-dimensional theorem. A more general, not-yet-identified formula for changes of variables may implicitly contain this special case.

## References
1. S. Hamad, *Isometric Classification of Sobolev Spaces*, arXiv:2611.09577v1, publicly submitted 2026-11-06, https://arxiv.org/abs/2611.09577.
2. D. S. Ornstein, *A non-inequality for differential operators in the \(L^1\) norm*, Arch. Rational Mech. Anal. (1962), DOI:10.1007/BF00253928.
3. K. Kazaniecki, D. M. Stolyarov and M. Wojciechowski, *Anisotropic Ornstein noninequalities*, Anal. PDE 10 (2017), 351–366, DOI:10.2140/apde.2017.10.351, https://msp.org/apde/2017/10-2/apde-v10-n2-p04-p.pdf.
4. *Sharp rotation distortion of the planar endpoint second-jet Sobolev norm*, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-rotation-distortion-of-the-planar-endpoint-second-jet-sobo--c088c35512e6.
5. *Exact shear distortion and two endpoint-Sobolev norm transitions*, 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-shear-distortion-and-two-endpoint-sobolev-norm-transitions--c0bb26d3cb4a.
