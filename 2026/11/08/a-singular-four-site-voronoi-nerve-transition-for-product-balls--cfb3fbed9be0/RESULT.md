# A singular four-site Voronoi-nerve transition for product balls

## Finding
Let \(R,h>0\) and \(1\le p<\infty\). In \(\mathbb R^3=\mathbb R^2\times\mathbb R\), use the centrally symmetric convex unit ball
\[
K_p=\left\{(u,w):\bigl(\|u\|_2^p+|w|^p\bigr)^{1/p}\le1\right\}.
\]
Place three sites at the vertices of a horizontal equilateral triangle of circumradius \(R\), centered at the origin, and a fourth site at height \(h\) above its center:
\[
z_j=\bigl(R\cos(2\pi(j-1)/3),R\sin(2\pi(j-1)/3),0\bigr)\ (j=1,2,3),\qquad z_4=(0,0,h).
\]
Define closed convex-distance Voronoi cells \(V_i^{(p)}=\{x:d_p(x,z_i)\le d_p(x,z_k)\ \text{for every }k\}\), where \(d_p(x,z)=\|x-z\|_{K_p}\); let \(N_p=\{\varnothing\ne J\subseteq\{1,2,3,4\}:\bigcap_{j\in J}V_j^{(p)}\ne\varnothing\}\).

**Exact nerve classification.** For every \(p>1\), \(N_p\) is the complete nonempty simplex on four sites: the four Voronoi cells meet at exactly one point. For \(p=1\), the nerve is complete when \(h\ge R\), whereas when \(0<h<R\), the *only* missing nonempty faces are \(\{1,2,3\}\) and \(\{1,2,3,4\}\).

**Quantified singularity.** If \(0<h<R\) and \(p>1\), the unique fourfold Voronoi point is \((0,0,-t_p)\), where \(t_p>0\) is the unique solution of
\[
(t_p+h)^p-t_p^p=R^p.
\]
With \(Q_p=(R^p/(p h))^{1/(p-1)}\), its exact bounds and endpoint asymptotic are
\[
Q_p-h<t_p<Q_p,\qquad
 t_p\sim\frac{R}{e}\left(\frac Rh\right)^{1/(p-1)}\quad(p\downarrow1).
\]
Thus the fourfold point escapes exponentially to infinity as the strictly convex balls tend to the bicone \(K_1\).

**Exact missing-term and positive defect.** Write \(W_i=z_i-K_1\) and \(U=\bigcup_{i=1}^4W_i\). For \(0<h<R\), the difference between the ordinary union volume and the proposed reduced inclusion-exclusion sum over the Voronoi nerve is exactly
\[
\operatorname{vol}_3(U)-\sum_{J\in N_1}(-1)^{|J|+1}\operatorname{vol}_3\left(\bigcap_{j\in J}W_j\right)
=\operatorname{vol}_3\left((W_1\cap W_2\cap W_3)\setminus W_4\right).
\]
In the nonempty parameter region
\[
\tfrac12<R<1/\sqrt3,\qquad 1-R<h<R,
\]
this difference is **strictly positive**, with the explicit bound
\[
\operatorname{vol}_3\left((W_1\cap W_2\cap W_3)\setminus W_4\right)
\ge\frac{2\pi}{3}\,\delta^3>0,
\quad \delta=\min\{1-\sqrt3R,\ R+h-1\}.
\]
For instance \(R=11/20\), \(h=1/2\) gives \(\delta=1-11\sqrt3/20\), so the deficit is at least \((2\pi/3)(1-11\sqrt3/20)^3\).

## Assumptions and scope
All sites are distinct, with \(h,R>0\); the fourth site lies outside the plane of the first three. The distance is the Minkowski functional of exactly the stated \(K_p\), not a site-dependent metric. Nerve intersections are closed-set intersections, so equidistance ties count. The volume identity concerns all four **unscaled** unit translates of \(K_1\). The specified strict inequalities on \(R,h\) are a sufficient open region for positive error; no necessity outside that region is asserted. All classification and asymptotic assertions are proved for the stated parameter ranges without genericity assumptions.

## Proof
For \(x=(u,w)\), the distances to the three horizontal vertices are
\[
d_p(x,z_j)=\bigl(\|u-Rv_j\|_2^p+|w|^p\bigr)^{1/p},
\]
where \(v_j\in\mathbb R^2\) are the three equilateral unit directions. Since the scalar map \(r\mapsto(r^p+|w|^p)^{1/p}\) is strictly increasing for nonnegative \(r\), equality among those three distances is equivalent to \(\|u-Rv_1\|_2=\|u-Rv_2\|_2=\|u-Rv_3\|_2\), hence to \(u=0\). The four distances along this vertical line therefore reduce to
\[
D_p(w)=(R^p+|w|^p)^{1/p}\quad\text{(each of the first three)},\qquad H(w)=|w-h|\quad\text{(fourth)}.
\]

Suppose \(p>1\). If \(h<R\), at \(w=0\) one has \(D_p(0)>H(0)\), while for \(w=-t\), \(t\to\infty\), one has \(D_p(-t)-H(-t)\to-h<0\). The equation for the unique crossing is \((t+h)^p-t^p=R^p\), whose left side strictly increases from \(h^p\) to infinity for \(t\ge0\). If \(h=R\), the unique crossing is \(w=0\). If \(h>R\), the unique crossing is in \(0<w<h\), because \(D_p(w)\) increases and \(H(w)=h-w\) decreases there. On the two outer rays the strict triangle inequality excludes any additional crossing. At every crossing all four sites tie, establishing the complete nerve for \(p>1\) and uniqueness of the fourfold point.

Suppose \(p=1\). Now \(D_1(w)=R+|w|\). If \(h<R\), the triangle inequality \(|w-h|\le|w|+h<R+|w|\) holds for all \(w\), so \(V_1^{(1)}\cap V_2^{(1)}\cap V_3^{(1)}=\varnothing\). If \(h=R\), every \(w\le0\) gives a fourfold tie; if \(h>R\), a fourfold tie occurs at \(w=(h-R)/2\). These latter cases have complete nerve.

To prove that **no other faces are missing** when \(0<h<R\), rotate the configuration so the first three sites are \((R,0,0)\), \((-R/2,\sqrt3R/2,0)\), and \((-R/2,-\sqrt3R/2,0)\). Set
\[
a=\frac{h^2-R^2}{R+2h}<0,\qquad y=(a,0,-1).
\]
The distances satisfy
\[
d_1(y)=R-a+1,\qquad
 d_2(y)=d_3(y)=\sqrt{a^2+aR+R^2}+1=h-a+1=d_4(y).
\]
The square-root equality follows by squaring and the displayed value of \(a\); all terms have the required nonnegative signs. Since \(R>h\), \(d_1(y)>d_2(y)\). Therefore \(y\in V_2^{(1)}\cap V_3^{(1)}\cap V_4^{(1)}\). Rotations by \(120\) degrees give the other two triples containing site 4. By closure under subsets, the nerve contains all nonempty subsets except the triple \(123\) and its four-element superset.

For the escape estimate, with \(0<h<R\), apply the mean-value theorem to \(s\mapsto s^p\) on \([t_p,t_p+h]\). There is \(\xi_p\in(t_p,t_p+h)\) such that \(R^p=p h\xi_p^{p-1}\), whence \(\xi_p=Q_p\) and \(Q_p-h<t_p<Q_p\). As \(p\downarrow1\), \(Q_p\to\infty\), and
\[
\log Q_p=\frac{p\log R-\log p-\log h}{p-1}
=\frac{\log(R/h)}{p-1}+\log R-1+o(1).
\]
Exponentiating and using \(t_p/Q_p\to1\) gives the stated asymptotic.

For \(p=1\), the ordinary inclusion-exclusion sum includes precisely two terms absent from the nerve sum, associated with \(\{1,2,3\}\) and \(\{1,2,3,4\}\), with opposite signs. Their difference is exactly \(\operatorname{vol}_3((W_1\cap W_2\cap W_3)\setminus W_4)\). In the stated open parameter region take \(x=z_1\). Its gauge-distances to the other two triangle sites are both \(\sqrt3R<1\), while its distance to \(z_4\) is \(R+h>1\). The triangle inequality shows that every point in the open \(K_1\)-ball of radius \(\delta\) about \(z_1\) belongs to \(W_1\cap W_2\cap W_3\) and not to \(W_4\). Finally
\[
\operatorname{vol}_3(K_1)=\int_{-1}^{1}\pi(1-|w|)^2\,dw=\frac{2\pi}{3},
\]
which proves the positive lower bound.

## Verification
The included standard-library Python script `check.py` independently recomputes the triple Voronoi witness and the fourfold equation for sampled positive parameters. It passes 4,500 cases in the bicone phase and 4,000 cases for \(p>1\), plus four limiting-rate checks; it reports `FOUR_SITE_BICONE_VERIFIER_OK 8504`. In the explicit example, it evaluates the analytical volume lower bound as approximately \(0.0002226513389433433\). This finite numerical evidence is supplementary: the claims for all real parameters and the escape asymptotic follow from the preceding identities, inequalities, and mean-value theorem.

## Relationship to prior work
Shelley and Tartakovsky (arXiv:2610.25841, first submitted October 19, 2026) study Voronoi-nerve inclusion-exclusion for translates of strictly convex bodies. Their Theorem 1.1 establishes universal reduction in dimension at most two, and their Section 5 uses **five** sites with a smooth bicone-like body to demonstrate failure in dimension three. Their proof also identifies the nonsmooth limiting bicone \(\{(u,w):\|u\|_2+|w|\le1\}\), and its relationship to the present example is direct and acknowledged. The present statement instead classifies the full four-site Voronoi nerve for an entire product-\(p\) family, gives a four-site nonstrict counterexample, and quantifies exponential escape of a fourfold Voronoi point as \(p\downarrow1\). These parameterwise and limiting assertions are not stated by that paper.

The classical inclusion-exclusion reduction for Euclidean balls (as cited there from Naiman--Wynn, 1992) is consistent with \(p=2\), where our four-site nerve is complete. Prior work on Voronoi cells of lattices for arbitrary norms (Blömer--Kohn, arXiv:1512.00720) concerns a different infinite-site setting. The present comparison does not establish priority against all older generalized Voronoi literature.

## Limitations
The explicit four-site failure is for a **nonstrictly convex** bicone and does not contradict the strictly convex hypotheses in Shelley--Tartakovsky. The quantified positive deficit is established on a sufficient open parameter set only. A complete characterization of when this deficit is positive outside that set is not attempted. The nerve classification relies on the equilateral horizontal three-site symmetry and a single axial fourth site. The formula does not assert that fewer than four sites can never fail for other nonsmooth norms, nor that four sites can never fail for other strictly convex norms. No independent external mathematical audit has been performed.

## References
1. A. Shelley and D. Tartakovsky, *Union of Translates of a Convex Body*, arXiv:2610.25841 (first public submission October 19, 2026), https://arxiv.org/abs/2610.25841. Relevant material: introduction, Theorems 1.1--1.2, and Section 5 (five-site smooth bicone construction).
2. D. Q. Naiman and H. P. Wynn, *Inclusion-exclusion-Bonferroni identities and inequalities for discrete tube-like problems via Euler characteristics* (1992), cited and discussed in Reference 1 for the Euclidean-ball special case.
3. J. Blömer and K. Kohn, *Voronoi Cells of Lattices with Respect to Arbitrary Norms*, arXiv:1512.00720 (first submitted November 27, 2015), https://arxiv.org/abs/1512.00720 (background on non-Euclidean Voronoi geometry of lattices).
