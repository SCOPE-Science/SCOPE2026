# Sharp quadratic Steinhaus modulus of the complex two-atom \(\ell_1\) plane

## Finding

**Theorem.** Let \(X=\ell_1^2(\mathbb C)\), equipped with the underlying real norm \(\|(w_1,w_2)\|=|w_1|+|w_2|\). For fixed \(0<d<2\) and \(a>0\), define the uniform Steinhaus modulus by
\[
U_X(d;a)=\inf_{\substack{x,y\in X,\ \|x\|=\|y\|=1\\\|x-y\|\ge d}}\ \sup_{\|z\|\le a}\big|\|x+z\|-\|y+z\|\big|.
\]
Then
\[
\boxed{\lim_{a\downarrow0}\frac{U_X(d;a)}{a^2}=\frac{d}{1-d^2/4}.}\tag{1}
\]
The coefficient is sharp and comes from the positive, coordinate-swapped unit pair
\[
x_d=\left(\frac{2+d}{4},\frac{2-d}{4}\right),\qquad
y_d=\left(\frac{2-d}{4},\frac{2+d}{4}\right),\qquad\|x_d-y_d\|=d.
\]
Furthermore, if \(a_n\downarrow0\), \(x_n,y_n\in S_X\), \(\|x_n-y_n\|\ge d\), and their perturbation supremum divided by \(a_n^2\) converges to the coefficient in (1), then every convergent subsequence of the pairs has, after exchanging the two vectors or two coordinates and rotating individual complex coordinates, the limiting pair \((x_d,y_d)\). This gives the asymptotic rigidity of the worst-separated unit pairs.

## Assumptions and scope

Complex coordinates provide the full perturbation directions, but the normed space and Steinhaus property are regarded over the real field. Every perturbation \(z=(z_1,z_2)\) has complex coordinates with \(|z_1|+|z_2|\le a\); no restriction to real perturbations is made. The pair separation \(d\in(0,2)\) is fixed while \(a\downarrow0\). The endpoint \(d=2\), possible uniformity as \(d\uparrow2\), and the complete finite-radius function are not asserted. The elementary quadratic expansion below is used only where coordinate moduli are bounded away from zero.

Write
\[
B(x,y;a)=\sup_{\|z\|\le a}|\|x+z\|-\|y+z\||.
\]
All limits of pairs are ordinary Euclidean limits in the four-real-dimensional space \(X\).

## Proof

**1. An explicit matching upper bound.** Put \(\delta=d/2\), \(r=(1+\delta)/2\), \(s=(1-\delta)/2\), and \(x=(r,s)\), \(y=(s,r)\). Both norms equal one and \(\|x-y\|=2\delta=d\). For complex \(w\) with \(|w|\le a\), Taylor expansion at a fixed positive radius \(R\) gives uniformly
\[
|R+w|=R+\operatorname{Re}w+\frac{(\operatorname{Im}w)^2}{2R}+O_R(a^3).
\]
For all \(z\in aB_X\) the real-linear terms cancel in the difference of the perturbed norms, leaving
\[
\|x+z\|-\|y+z\|=
\frac12\Big(\frac1r-\frac1s\Big)
\big((\operatorname{Im}z_1)^2-(\operatorname{Im}z_2)^2\big)+O_d(a^3).
\]
Since \((\operatorname{Im}z_1)^2+(\operatorname{Im}z_2)^2\le a^2\), the absolute value is at most \(a^2|1/r-1/s|/2+O_d(a^3)\). The perturbation \(z=(ia,0)\) attains the same leading term. Thus
\[
B(x,y;a)=\frac{a^2}{2}\frac{r-s}{rs}+O_d(a^3)
=\frac{d}{1-d^2/4}a^2+O_d(a^3),
\]
and (1) follows in the upper direction.

**2. Reduction for nearly minimizing sequences.** Fix any \(a_n\downarrow0\). By Step 1 choose unit pairs \(x_n,y_n\) at distance at least \(d\) such that
\[
B_n:=B(x_n,y_n;a_n)\le U_X(d;a_n)+a_n^3\le C_d a_n^2.
\]
Compactness allows passage to a subsequence with \(x_n\to x\), \(y_n\to y\), where \(x,y\in S_X\) and \(\|x-y\|\ge d\). We establish that all four complex numbers \(x_j,y_j\), \(j=1,2\), are nonzero.

For a complex scalar \(u\) and perturbation \(w\), define
\[
H(u,w)=|u+w|+|u-w|-2|u|\ge0.
\]
For any coordinate \(j\) and \(|w|\le a_n\), the two perturbed-norm differences obey \(|B_{n,+}|,|B_{n,-}|\le B_n\). Since \(\|x_n\|=\|y_n\|\), their sum equals
\[
H(x_{n,j},w)-H(y_{n,j},w),
\qquad |H(x_{n,j},w)-H(y_{n,j},w)|\le2B_n.\tag{2}
\]
If, for example, \(x_j=0\) but \(y_j\ne0\), choose \(|w|=a_n\) perpendicular to \(x_{n,j}\) in the complex plane (any direction when it is zero). Then
\[
\frac{H(x_{n,j},w)}{a_n^2}
=\frac{2}{\sqrt{|x_{n,j}|^2+a_n^2}+|x_{n,j}|}\longrightarrow+\infty,
\]
whereas \(H(y_{n,j},w)=O(a_n^2)\) since its limiting modulus is positive. This contradicts (2). The reverse one-zero case is identical.

If both \(x_j=y_j=0\), the other coordinates have limiting modulus one. Because \(\|x-y\|\ge d\), their limiting complex phases differ. Perturbing only that other coordinate by a complex vector aligned with the difference of those phases yields
\[
B_n\ge a_n\left|\frac{x_{n,3-j}}{|x_{n,3-j}|}-\frac{y_{n,3-j}}{|y_{n,3-j}|}\right|-O(a_n^2),
\]
contradicting \(B_n=O(a_n^2)\). Therefore all limiting coordinate moduli are positive.

**3. First-order phases agree.** Put \(r_{n,j}=|x_{n,j}|\), \(s_{n,j}=|y_{n,j}|\) and \(\omega_{n,j}=x_{n,j}/r_{n,j}\), \(\eta_{n,j}=y_{n,j}/s_{n,j}\). Since the limiting radii are positive, the scalar modulus has a uniform first-order Taylor expansion, and perturbations concentrated in coordinate \(j\) imply
\[
 a_n|\omega_{n,j}-\eta_{n,j}|\le B_n+O(a_n^2).
\]
Hence \(|\omega_{n,j}-\eta_{n,j}|=O(a_n)\) for each coordinate, and at the limit the phase of \(x_j\) equals that of \(y_j\). Independent coordinate rotations reduce the limiting pair to nonnegative real coordinates.

**4. A compulsory curvature cost in each coordinate.** For fixed \(j\), take \(w_n=ia_n\omega_{n,j}\). For a scalar \(u\) whose modulus is bounded below, the symmetric Taylor formula is
\[
H(u,w)=\frac{|w|^2-[\operatorname{Re}(\overline u w)/|u|]^2}{|u|}+O(|w|^3).
\]
The chosen perturbation is perpendicular to \(x_{n,j}\), and its angle to \(y_{n,j}\) differs from a right angle by \(O(a_n)\), as Step 3 shows. Thus (2) gives, for \(r_j=|x_j|\), \(s_j=|y_j|\),
\[
\liminf_{n\to\infty}\frac{B_n}{a_n^2}
\ge\frac12\left|\frac1{r_j}-\frac1{s_j}\right|
\quad(j=1,2).\tag{3}
\]
The real unit norm conditions yield \(r_1+r_2=s_1+s_2=1\). Since the limiting complex phases agree coordinatewise,
\[
\|x-y\|=|r_1-s_1|+|r_2-s_2|=2\Delta,
\qquad \Delta=|r_1-s_1|\ge d/2.
\]
After swapping vectors if needed, write \(s_1=t\), \(r_1=t+\Delta\), \(r_2=1-t-\Delta\), \(s_2=1-t\), where \(0<t<1-\Delta\). Formula (3) implies
\[
\liminf_{n\to\infty}\frac{B_n}{a_n^2}
\ge\frac\Delta2\max\left\{
\frac1{t(t+\Delta)},\ 
\frac1{(1-t-\Delta)(1-t)}\right\}.\tag{4}
\]
The first denominator increases strictly with \(t\), while the second decreases strictly; their minimum has the unique maximum when \(t=(1-\Delta)/2\), at which each denominator is \((1-\Delta^2)/4\). Consequently the right side of (4) is at least
\[
\frac{2\Delta}{1-\Delta^2}\ge\frac{d}{1-d^2/4},
\]
with equality only if \(\Delta=d/2\) and the coordinate radii are the balanced swapped pair. This proves the lower bound for arbitrary approximate minimizers, hence (1).

**5. Rigidity.** For any sequence of admissible pairs whose normalized supremum tends to the sharp coefficient, repeat Steps 2–4: the compactness argument forces positive coordinate radii and matching phases, and equality in the strictly monotone inequalities of Step 4 forces \(\Delta=d/2\), \(t=(1-\Delta)/2\). Thus every limit is equivalent under the stated coordinate phases and exchanges to \((x_d,y_d)\). Conversely, Step 1 exhibits such a sharp family.

## Verification

The upper pair and its exact coordinate separation may be checked by elementary algebra. The curvature coefficient comes from the independently verifiable one-variable expansion of \(|R+w|\) at \(R>0\). In Step 2 the exact transverse identity for \(H\) rules out a vanishing coordinate when its counterpart stays positive; the remaining case uses a nonzero first derivative. Step 4 proves a universal lower bound without assuming finite numerical enumeration is exhaustive. A standalone checker, `check_examples.py`, evaluates the explicit upper-pair transverse perturbation at ten finite parameter/scale combinations and checks its approach to the claimed coefficient. These diagnostics are not a proof of (1).

## Relationship to prior work

Johnson and Kania [1] define exactly this norm-difference Steinhaus modulus and determine it on nonatomic real \(L^1\), where its small-radius behavior is **linear** rather than quadratic; their squared-norm Hilbert calculation is a different quantity. Their complete displayed results and open questions do not state the coefficient (1) for complex two-atom \(L^1\). Kania and Kochanek [2] treat the qualitative local norm-separation property, not the small-radius modulus.

The published qualitative characterization of strictly convex \(\ell_1\)-sums [3] applies to this two-complex-coordinate space (each complex scalar coordinate is a two-dimensional real Euclidean block), but cannot imply the exact coefficient. The sharp quadratic result for \(\mathbb R\oplus_1 H\) [4] concerns one real scalar and a real Hilbert block of dimension at least three and has a *different* coefficient, \(d/(4-2d)\). Real \(\ell_p\), \(p\ge2\), has a linear small-radius profile [5]. These are related models but neither their hypotheses nor their formulas cover (1).

## Limitations

The result is specific to the complex two-atom \(\ell_1\) norm regarded over the real field, for fixed \(0<d<2\). It does not determine \(U_X(d;a)\) at arbitrary finite radius, establish a general formula for more atoms, or address the endpoint \(d=2\). No claim of priority against unindexed older norm-germ curvature literature is made; independent verification has not been performed.

## References

[1] W. B. Johnson and T. Kania, *Uniform Property (S)*, arXiv:2602.09106, first posted 9 February 2026, especially Definition 1.2, Proposition 1.4 and Theorem B. https://arxiv.org/html/2602.09106v2

[2] T. Kania and T. Kochanek, *Steinhaus' lattice-point problem for Banach spaces*, arXiv:1302.6443, first posted 26 February 2013, especially Theorem A and the examples. https://arxiv.org/html/1302.6443v5

[3] *Sharp Steinhaus criterion for \(\ell_1\)-sums of strictly convex spaces*, 2026, public mathematical note. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-steinhaus-criterion-for-ell-1-sums-of-strictly-convex-spac--61990e8279cd

[4] *Sharp quadratic Steinhaus modulus of a scalar–Hilbert one-sum*, 2026, public mathematical note. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-quadratic-steinhaus-modulus-of-a-scalar-hilbert-one-sum--102221e3c81d

[5] *Sharp small-radius Steinhaus modulus of real \(\ell_p\) for \(p\ge2\)*, 2026, public mathematical note. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-small-radius-steinhaus-modulus-of-real-ell-p-for-p-ge2--072a2f172b7d
