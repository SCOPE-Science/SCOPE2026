# A universal hard-core zero circle and an exponentially escaping root on subdivided stars

## Finding

For every integer \(m\ge1\), let \(S_m\) be the tree with hub \(c\) and \(m\) disjoint length-two arms \(c-u_i-v_i\). For the univariate hard-core partition function \(P_m(z)=\sum_{I\text{ independent in }S_m}z^{|I|}\), the exact polynomial is
\[
P_m(z)=(1+2z)^m+z(1+z)^m.
\]
Define the open disk \(\mathcal D=\{z\in\mathbb C:|z+1/3|<1/3\}\). Exactly \(m\) simple zeros of \(P_m\) belong to \(\mathcal D\); its sole remaining zero is \(-X_m<-1\), where \(X_m\) uniquely satisfies
\[
X_m=\left(2+\frac1{X_m-1}\right)^m,\qquad X_m>2^m.
\]
The zero in \((-1/2,0)\) is unique for all \(m\). For even \(m\) there is precisely one more real zero in \((-2/3,-1/2)\); for odd \(m\) there is none there. All other zeros are nonreal conjugate pairs. Thus there are two real roots if \(m\) is odd and three if \(m\) is even; all roots are simple and the polynomial is real-rooted only for \(m=1,2\).

The exceptional root has the asymptotic expansion
\[
X_m=2^m+\frac m2+O\!\left(\frac{m^2}{2^m}\right).
\]
Moreover, if \(z_{m,1},\ldots,z_{m,m}\) are the roots in \(\mathcal D\), then
\[
\max_{1\le j\le m}\operatorname{dist}\left(z_{m,j},\partial\mathcal D\right)\longrightarrow 0\qquad(m\to\infty).
\]
This last statement concerns radial condensation toward the circle, not a proved angular limiting density.

## Assumptions and scope

The graph is a finite, simple, unweighted once-subdivided star, with \(m\ge1\) two-edge arms and uniform complex fugacity \(z\). The partition function counts all independent vertex sets, including the empty set, without any activity normalization beyond \(P_m(0)=1\). No claim is made for unequal arm fugacities, other arm lengths, or infinite-lattice phase transitions.

## Proof

**Exact polynomial and degree.** If the hub is empty, every arm is one edge and contributes \(1+2z\). If the hub is occupied, its \(m\) neighbours are forbidden, and the \(m\) tips may be independently occupied, yielding \(z(1+z)^m\). Therefore \(P_m\) has degree exactly \(m+1\).

**Sharp disk separation.** On \(\partial\mathcal D\),
\[
|1+2z|^2-|1+z|^2=3|z|^2+2\operatorname{Re}z=0,
\]
and \(|z|\le2/3<1\). Hence \(|z(1+z)^m|<|(1+2z)^m|\) everywhere on the boundary. Rouché's theorem gives exactly \(m\) roots of \(P_m\) inside \(\mathcal D\), counted with multiplicity, because \((1+2z)^m\) has \(m\) roots there. No root lies on the boundary. The disk is strictly in the left half-plane; its only boundary intersection with the imaginary axis is \(z=0\), which is not a zero.

**Complete real-root count.** Write \(z=-x\), where \(x>0\). For \(0<x<1/2\), the equation \(P_m(-x)=0\) is
\[
\left(\frac{1-2x}{1-x}\right)^m=x.
\]
Its left side strictly decreases from \(1\) to \(0\), so there is one root. For \(1/2<x<1\) and odd \(m\), both terms in \(P_m(-x)=(1-2x)^m-x(1-x)^m\) are negative, so there are no roots. For even \(m\), the equation becomes \(((2x-1)/(1-x))^m=x\); the left-to-right ratio is strictly increasing from zero to infinity because its logarithmic derivative is
\[
m\left(\frac2{2x-1}+\frac1{1-x}\right)-\frac1x>0.
\]
At \(x=2/3\), the ratio exceeds one, so this root lies in \((1/2,2/3)\). For \(x>1\), cancellation of the common parity sign gives
\[
\left(2+\frac1{x-1}\right)^m=x.
\]
The left side strictly decreases from infinity to \(2^m\), while the right side increases without bound. Hence there is exactly one such root, at \(x=X_m>2^m\). The endpoints \(x=1/2\) and \(x=1\) are not roots. The disk count identifies \(-X_m\) as the sole exterior root; no nonnegative real root exists because \(P_m\) has positive coefficients.

**Simplicity.** At a multiple zero \(z\), necessarily \(z\ne0,-1/2,-1\). From \(P_m(z)=0\) one gets \((1+2z)^m=-z(1+z)^m\). Substitution into \(P_m'(z)=0\), after dividing by nonzero factors, yields
\[
2z^2+(3-m)z+1=0.
\]
For \(m\ge3\), both roots of this quadratic have nonnegative real parts: their sum is \((m-3)/2\ge0\) and product is \(1/2>0\), with conjugacy or positive-real roots according to the discriminant. This contradicts the strict-left-half-plane disk localization of all roots except the exterior negative root. For \(m=1,2\), the real-root census already gives respectively two and three distinct roots, matching the polynomial degrees. Thus all roots are simple for every \(m\).

**Exponential escape.** Let \(q=2^m\). The exterior equation is \(X_m=q(1+1/(2(X_m-1)))^m\). Since \(X_m>q\), the bound \((1+t)^m\le e^{mt}\) gives \(0<X_m-q\le q(e^{m/(2(q-1))}-1)=O(m)\). Writing \(X_m=q+O(m)\), the uniform binomial expansion now yields
\[
X_m=q+\frac{mq}{2(X_m-1)}+O(m^2/q)=q+\frac m2+O(m^2/q).
\]

**Uniform circle condensation.** Put \(w=(1+2z)/(1+z)\). The map takes \(\mathcal D\) biholomorphically onto \(|w|<1\), with inverse \(z=(w-1)/(2-w)\). For any of the \(m\) interior zeros, \(w^m=-z\), so \(|w|^m=|z|\). Given \(\varepsilon>0\), if \(|w|\le1-\varepsilon\), then \(|z|=|w-1|/|2-w|\ge\varepsilon/3\), while \(|z|=|w|^m\le(1-\varepsilon)^m\), impossible for all sufficiently large \(m\). This holds simultaneously for every interior zero. Since the inverse Möbius map is uniformly Lipschitz on the closed unit disk, the distance of all these zeros to \(\partial\mathcal D\) tends uniformly to zero.

## Verification

The accompanying `verify.py` independently enumerates the independent sets of the graphs with \(1\le m\le7\) and checks their complete coefficients against the closed formula. Exact Sturm real-root counts, polynomial degrees, endpoint exclusions, and square-freeness are additionally tested for \(1\le m\le16\), for 103 successful checks total. These are finite consistency tests. The arbitrary-size claims are proved in the preceding section by Rouché's theorem, monotonicity, elementary algebra and asymptotics.

## Relationship to prior work

Scott and Sokal (first public version 2003) develop the hard-core lattice-gas/independence-polynomial correspondence and general tree recursion, which gives the physical setting and can produce the exact partition expression. Law's 2011 thesis gives a general spider polynomial representation and proves it distinguishes spiders; Wang's 2022 article explicitly studies short-leg spider independence polynomials and their unimodality. Zhang and Tu (2026) prove **strict left-half-plane stability for all spiders**, a stronger result than that particular implication here. Accordingly, left-half-plane stability, the spider conditional-product identity, and coefficient unimodality are **not** asserted as new. The distinct claim assessed here is the sharp two-dimensional disk separation, the sole exponentially escaping zero, the parity-dependent complete real-root census, simplicity, and the uniform zero-circle condensation for the equal-length-two-arm subfamily. The inspected source sections do not state or imply that entire package merely from their theorems without new root-geometry analysis.

## Limitations

This is a classification for a specific natural infinite family of finite trees, not for arbitrary spiders. The uniform-condensation statement does not establish an angular density or any thermodynamic singularity. The elementary polynomial formula and general half-plane stability are preexisting; historical priority for the finer disk and real-root classification is subject to further external inspection. Independent validation has not been performed.

## References

- A. D. Scott and A. D. Sokal, *The repulsive lattice gas, the independent-set polynomial, and the Lovász local lemma*, arXiv:cond-mat/0309352 (first public version 2003-09-15), Sections 3.3–3.5, https://arxiv.org/html/cond-mat/0309352v2 .
- H.-F. Law, *Trees and Graphs: Congestion, Polynomials and Reconstruction*, 2011 thesis, Section 5.1, https://ora.ox.ac.uk/objects/uuid%3A54190b51-cd9d-489e-a79e-82ecdf15b4c5/files/m6d55eeb5c15f488bbcc1f7fff3d56411 .
- K. Wang, *Unimodality of Independence Polynomials of Special Trees*, 2022, Proposition 1 and first two pages, https://nhsjs.com/wp-content/uploads/2022/08/Unimodality-of-Independence-Polynomials-of-Special-Trees.pdf .
- L. Zhang and J. Tu, *Stability of independence polynomials of spiders*, arXiv:2609.04694 (2026), Theorem 4 and equations (6)–(7), https://arxiv.org/abs/2609.04694 .
