# Corner-product area-loss law and two-moment reconstruction of triangles

## Finding

Let \(Q\subset\mathbb R^2\) be a fixed nondegenerate convex polygon with \(m\ge3\) genuine vertices, perimeter \(P>0\), side lengths \(\ell_j>0\), and interior angles \(\alpha_i\in(0,\pi)\). Independently choose \(N\ge3\) points uniformly by arclength from its entire boundary. Let \(H_N\) be their convex hull and define the area deficit \(\Delta_N=\operatorname{area}(Q)-\operatorname{area}(H_N)\).

With all \(2m\) variables \(E_i^-,E_i^+\) independent and standard exponential, the following limit holds in distribution **and in every fixed positive integer moment**:

\[
N^2\Delta_N\ \xrightarrow{\mathrm d}\ Z_Q
=\frac{P^2}{2}\sum_{i=1}^{m}\sin\alpha_i\,E_i^-E_i^+.
\]

The limiting law depends only on \(P\) and the multiset \(\{\sin\alpha_i\}\); individual side lengths do not appear. Its Laplace transform and first two cumulants are

\[
\mathbb E e^{-tZ_Q}=\prod_{i=1}^{m}\int_0^\infty
\frac{e^{-x}}{1+tP^2\sin\alpha_i\,x/2}\,dx\quad(t\ge0),
\]
\[
\mu_Q:=\mathbb E Z_Q=\frac{P^2}{2}\sum_i\sin\alpha_i,
\qquad
v_Q:=\operatorname{Var}(Z_Q)=\frac{3P^4}{4}\sum_i\sin^2\alpha_i.
\]

There is also a universal finite-sample mean correction: for \(\delta=\min_j\ell_j/P>0\),

\[
\mathbb E\Delta_N=\frac{\mu_Q}{(N+1)(N+2)}+O_Q\!\left(N e^{-\delta N}\right)
\quad(N\to\infty).
\]

**Inverse theorem (triangles).** If \(m=3\), the perimeter \(P\) and the two numbers \(\mu_Q,v_Q\) uniquely determine the three side lengths, hence the Euclidean triangle up to congruence. Specifically put

\[
R=\frac{P^3}{4\mu_Q},\qquad
S_2=\frac{P^2v_Q}{3\mu_Q^2},\qquad
e_2=\frac{P^2-S_2}{2},
\]
\[
e_3=\sqrt{16P^2R^4+R^2(4P^2e_2-P^4)}-4PR^2.
\]

The side lengths are the three positive real roots, counted with multiplicity, of
\[
z^3-Pz^2+e_2z-e_3=0.
\]

Two initial moments are **minimal**: a single limiting mean, even with known \(P\), cannot distinguish all noncongruent triangles. Moreover, for every triangle,
\[
\frac{v_Q}{\mu_Q^2}=\frac{3(a^2+b^2+c^2)}{P^2}\ge1,
\]
with equality precisely for an equilateral triangle. More generally, \(v_Q/\mu_Q^2\ge3/m\) for every such polygon, with equality exactly when all interior-angle sines are equal.

## Assumptions and scope

All polygons here are fixed as \(N\to\infty\), planar, strictly convex at each genuine vertex (consecutive edges are noncollinear), and sampled with the **entire physical perimeter** as a single uniform probability measure. The point samples are independent. The triangle inverse uses known perimeter and exact moments of the **limiting** scaled loss, not raw finite-sample moments. No claim is made for interior-uniform sampling or for varying/degenerating polygons.

## Proof

**1. Deterministic corner decomposition.** Let \(G_N\) be the event that every side of \(Q\) contains at least two sampled points. For vertex \(i\), let \(U_i\) and \(V_i\) be distances from that vertex to the nearest sampled points on the incident sides; on an empty side temporarily set the corresponding distance to the whole side length. For the next step write \(U_i^-=U_i\) and \(U_i^+=V_i\). On \(G_N\), the boundary of \(H_N\) contains the segment between the two nearest sampled points flanking each original vertex, and all remaining exposed sampled segments lie on original sides. The removed regions are disjoint triangles, yielding the **exact finite-sample identity**
\[
\Delta_N=\frac12\sum_{i=1}^{m}\sin\alpha_i\,U_iV_i
\qquad\text{on }G_N.
\]
Each side has sample probability \(p_j=\ell_j/P>0\). By the binomial formula,
\[
\mathbb P(G_N^c)\le\sum_j\bigl((1-p_j)^N+Np_j(1-p_j)^{N-1}\bigr)
=O_Q(Ne^{-\delta N}).
\]

**2. Independent exponential corner gaps.** For any fixed nonnegative thresholds \(t_{i,\pm}\), the \(2m\) subarcs of lengths \(Pt_{i,\pm}/N\) adjacent to vertices are disjoint for all sufficiently large \(N\). Hence
\[
\mathbb P\!\left(\bigcap_{i,\pm}\left\{\frac{NU_i^\pm}{P}>t_{i,\pm}\right\}\right)
=\left(1-\frac{\sum_{i,\pm}t_{i,\pm}}N\right)^N
\longrightarrow\exp\left(-\sum_{i,\pm}t_{i,\pm}\right).
\]
This is the joint survival function of independent rate-one exponentials. Together with the exact identity and the vanishing probability of \(G_N^c\), it proves the distributional limit.

**3. Moment convergence.** For each incident side gap \(U\), and \(0\le x\le\ell_j\),
\[
\mathbb P\left(\frac{NU}{P}>\frac{Nx}{P}\right)=(1-x/P)^N\le e^{-Nx/P}.
\]
Thus all fixed moments of \(NU/P\) are bounded uniformly in \(N\). The elementary inequality \(2UV\le U^2+V^2\) bounds every fixed moment of the corner sum on \(G_N\). On \(G_N^c\), \(0\le N^2\Delta_N\le N^2\operatorname{area}(Q)\), and this event has exponentially small probability. Consequently the scaled deficits are uniformly integrable in every fixed integer power. Moment convergence follows. Since \(\mathbb E(E^-E^+)=1\) and \(\operatorname{Var}(E^-E^+)=4-1=3\), the mean and variance formulas follow. Conditioning on one exponential factor gives the displayed Laplace product.

**4. Sharper expectation.** For incident side lengths \(L,R\), the truncated gaps satisfy for \(0\le u\le L\), \(0\le v\le R\)
\[
\mathbb P(U>u,V>v)=(1-(u+v)/P)^N.
\]
Integrating this joint survival function yields
\[
\mathbb E[UV]=\frac{P^2}{(N+1)(N+2)}\Bigl[1-(1-L/P)^{N+2}-(1-R/P)^{N+2}
+(1-(L+R)/P)^{N+2}\Bigr].
\]
Every bracket differs from one by \(O_Q(e^{-\delta N})\). The deterministic corner formula fails only on \(G_N^c\), where both the true area loss and the sum of triangle areas are bounded by fixed constants depending on \(Q\). Summing and using the bound in Step 1 gives the asserted \(O_Q(Ne^{-\delta N})\) expectation error.

**5. Triangle inversion.** Write the triangle side lengths as \(a,b,c\), with circumradius \(R\) and area \(A\). The sine law gives \(\sin\alpha_i=a_i/(2R)\), so
\[
\mu_Q=\frac{P^3}{4R},\qquad
v_Q=\frac{3P^4}{16R^2}(a^2+b^2+c^2).
\]
Therefore \(R,S_2\), and \(e_2=ab+bc+ca\) are recovered as displayed. Let \(e_3=abc>0\). Heron's identity in elementary symmetric quantities is
\[
16A^2=-P^4+4P^2e_2-8Pe_3.
\]
The circumradius identity \(e_3=4RA\) implies
\[
e_3^2+8PR^2e_3-R^2(4P^2e_2-P^4)=0.
\]
For positive \(e_3\) its left-hand side is strictly increasing, so there is at most one positive root; the displayed root equals the actual \(abc\). Vieta's formulas uniquely recover the unordered side lengths.

To prove minimality, set the circumradius to one and consider isosceles triangles with apex angle \(2\arcsin t\), \(0<t<1\). Their perimeter is \(P(t)=4(1+t)\sqrt{1-t^2}\). It increases strictly from \(4\) to \(3\sqrt3\) on \((0,1/2)\), then decreases strictly to zero on \((1/2,1)\). Hence \(P(t)=5\) has two distinct roots on opposite sides of \(1/2\). The resulting noncongruent triangles have the same circumradius \(1\), perimeter \(5\), and limiting mean \(P^3/4\).

**6. Sharp moment ratios.** The Cauchy–Schwarz inequality gives \(m\sum_i\sin^2\alpha_i\ge(\sum_i\sin\alpha_i)^2\), with equality exactly when the angle sines coincide. In a triangle the sine law turns the equality into equality of all three sides. These observations prove the ratio bounds and their equality cases. In particular, the lower bound \(3/m\) is attained for each \(m\) by regular polygons; non-equiangular polygons can also attain it (for example, nonrectangular parallelograms).

## Verification

The accompanying standalone `VERIFY.py` requires Python 3, NumPy and SciPy; run it as `python3 VERIFY.py`. It checks exact corner-loss versus convex-hull area across random finite polygon samples, reconstructs five different triangles from limiting moments, checks the angle bounds, and compares sample scaled losses with predicted limiting means and variances. Its deterministic seed is set in the file. The script reports `VERIFY_OK triangle_inversions=5 exact_cap_hull_identities= 480 scaled_area_trials= 6400`. Numerical experiments are only supplementary: Steps 1–6 provide the infinite-sample proof.

## Relationship to prior work

Richardson, Vu and Wu (2004) study random inscribed polytopes with smooth boundaries and volume moments. Böröczky, Fodor and Hug (arXiv v1, 2011) develop intrinsic-volume expectation asymptotics under a rolling-ball condition, which a polygon with genuine vertices fails. Reitzner, Schütt and Werner (arXiv v1, 2019; journal 2023) treat random boundary samples from simple polytopes and establish leading **expected** volume-deficit asymptotics. Their cited main results do not give the finite-dimensional product-exponential area-loss law or a two-moment triangle inverse. Prior work on interior-uniform random polygons concerns a different sampling measure.

The closest related perimeter-loss fluctuation result for polygonal boundary sampling has an order-\(N^{-1}\) limit whose corner contributions are sums of homogeneous distance defects. It does **not** imply the order-\(N^{-2}\) area-product law or the explicit reconstruction from its first two moments. The expected area-deficit scale is previously motivated; the distributional and minimal inverse assertions are the distinguishing claims.

## Limitations

The result is asymptotic for each fixed polygon; the exponential error constant depends on its shortest side. It does not provide uniform bounds as side lengths shrink, nor does it establish statistical estimation guarantees from a finite number of independent hull realizations. The inverse theorem needs known perimeter. General polygons with identical interior-angle sine multisets have the same limiting area-loss law, so no full general-polygon congruence reconstruction is claimed. Searches cannot certify absolute historical priority; unindexed or inaccessible specialized literature remains a residual risk.

## References

1. R. M. Richardson, V. H. Vu, L. Wu, *Random Inscribing Polytopes*, Discrete Mathematics & Theoretical Computer Science Proceedings, public date listed 2004-12-31. DOI: 10.46298/dmtcs.3459. https://dmtcs.episciences.org/en/articles/3459
2. K. J. Böröczky, F. Fodor, D. Hug, *Intrinsic volumes of random polytopes with vertices on the boundary of a convex body*, arXiv:1103.4978v1, posted 2011-03-25. https://arxiv.org/abs/1103.4978
3. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917v1, posted 2019-11-14; later published in Discrete & Computational Geometry 69 (2023), 453–504. https://arxiv.org/abs/1911.05917
4. J. Pardon, *Central limit theorems for random polygons in an arbitrary convex set*, Annals of Probability 39 (2011), 881–903, arXiv:1003.4209. https://arxiv.org/abs/1003.4209 (interior-uniform sampling).
