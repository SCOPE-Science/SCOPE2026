# Exact multiplicity spectrum of vertex-to-center diameter disks of regular polygons

## Finding
Let \(P_n\) be the regular \(n\)-gon of circumradius one centered at the origin, \(n\ge3\), with vertices \(v_j=(\cos(2\pi j/n),\sin(2\pi j/n))\). Let \(D_j\) be the *closed disk with diameter* \([0,v_j]\). For uniformly distributed \(X\) in \(P_n\), write \(N_n(X)=\#\{j:X\in D_j\}\). The complete multiplicity distribution has the exact tail formula below. Let \(\delta=\pi/n\). Define \(T_{n,1}=1\), \(T_{n,k}=0\) for \(k>\lceil n/2\rceil\), and for integers \(2\le k\le\lceil n/2\rceil\), put \(a_k=2\lfloor k/2\rfloor\delta\), \(s_k=(-1)^{k+1}\), and
\[
(\ell_k,u_k)=\begin{cases}
(\max\{0,a_k-\pi/2\},\delta),&k\text{ even},\\
(0,\min\{\delta,\pi/2-a_k\}),&k\text{ odd}.
\end{cases}
\]
If \(u_k\le\ell_k\), put \(T_{n,k}=0\). Otherwise
\[
T_{n,k}=\frac{1}{\sin(2\delta)}\left[u_k-\ell_k+\frac{\sin(2a_k+2s_ku_k)-\sin(2a_k+2s_k\ell_k)}{2s_k}\right].
\]
Then for every integer \(k\ge1\), \(\mathbb P(N_n(X)\ge k)=T_{n,k}\), so \(\mathbb P(N_n(X)=k)=T_{n,k}-T_{n,k+1}\). Every multiplicity \(1,\ldots,\lceil n/2\rceil\) occurs on positive area; the maximum multiplicity at a generic point is \(\lceil n/2\rceil\), while the origin belongs to all \(n\) disks (a measure-zero exception). In particular, for \(n\ge4\), the exact singly covered area fraction is
\[
\mathbb P(N_n(X)=1)=\frac32-\cos(2\pi/n)-\frac{\pi/n}{\sin(2\pi/n)}.
\]
For \(n=3\), the general expression gives \(T_{3,2}=\frac{\pi}{3\sqrt3}-\frac12\), and the singly covered fraction is \(1-T_{3,2}\).

## Assumptions and scope
Areas are ordinary planar Lebesgue areas; boundary and disk-tie sets have area zero. The polygon is regular, centered at the shared diameter endpoint, and disks have exactly their vertex-to-center segments as diameters. No claim is made for unequal radial vertex distances, arbitrary interior diameter endpoints, or higher-dimensional regular polytopes. Values at the center are pointwise exceptional and do not affect probability. All angles are measured in radians.

## Proof
A point \(x=r(\cos\theta,\sin\theta)\) lies in \(D_j\) precisely when \(r^2\le r\cos(\theta-2\pi j/n)\), i.e. \(0\le r\le[\cos(\theta-2\pi j/n)]_+\). The origin is contained in every disk. By \(n\)-fold and reflection symmetry it suffices to take \(0\le\theta\le\delta\). The polygon's radial boundary on this chamber is
\[
r_{P}(\theta)=\frac{\cos\delta}{\cos(\delta-\theta)}.
\]
The nearest angular vertex is at distance \(\theta\); the second nearest is at distance \(2\delta-\theta\), and subsequent distances alternate \(2m\delta+\theta\) for odd ranks \(2m+1\), and \(2m\delta-\theta\) for even ranks \(2m\). Their nonnegative cosine thresholds are exactly the rank-ordered disk radial cutoffs; for ranks exceeding \(\lceil n/2\rceil\), all such cosines are nonpositive at almost every point in the chamber.

The decisive twofold-coverage containment is
\[
\cos(2\delta-\theta)\le \frac{\cos\delta}{\cos(\delta-\theta)}=r_P(\theta)
\]
whenever the cosine on the left is positive. Indeed, writing \(t=\delta-\theta\in[0,\delta]\),
\[
\cos t\cos(t+\delta)=\tfrac12[\cos\delta+\cos(2t+\delta)]\le\cos\delta,
\]
because \(0<\delta\le\pi/3\) and \(2t+\delta\in[\delta,3\delta]\subseteq[\delta,\pi]\). Every rank \(k\ge2\) threshold is at most the second threshold; therefore every point covered by at least two disks already lies in \(P_n\). This is a genuine set containment (including boundaries).

For each \(k\ge2\), its \(k\)-covered area is consequently the whole radial subgraph of the corresponding nonnegative cosine threshold, not a clipped subgraph. Integrating polar area and accounting for all \(2n\) reflected chambers gives
\[
\operatorname{area}\{x\in P_n:N_n(x)\ge k\}=n\int_0^\delta [\cos(a_k+s_k\theta)]_+^2\,d\theta.
\]
(The positive-part cosine is understood to be zero when the ordered angular separation is at least \(\pi/2\), rather than for angles approaching a full revolution.) The positivity interval is exactly \([\ell_k,u_k]\), and an elementary antiderivative of \(\cos^2\) yields the stated formula after division by \(\operatorname{area}(P_n)=\frac n2\sin(2\delta)\). The covering theorem (or the first radial threshold inequality) gives \(T_{n,1}=1\). The half-circle vertex count gives the maximum generic multiplicity. For every lower rank the positivity interval is nondegenerate, so each area stratum has positive measure. For \(n\ge4\), the second-rank integral evaluates to \(T_{n,2}=\delta/\sin(2\delta)+\cos(3\delta)/(2\cos\delta)\); rewriting \(1-T_{n,2}\) gives the singled-coverage formula.

## Verification
The accompanying standalone script `verify.py` directly numerically integrates the radial distribution obtained by sorting all \(n\) original disk inequalities, without relying on the rank formula. It compares this independent computation with every claimed tail for all \(3\le n\le30\), checks monotonicity and normalization, and reports the 462 comparisons. The proof, not numerical quadrature, establishes the all-\(n\) identity.

## Relationship to prior work
Pavlík, *Thales's theorem in higher dimensions* (2026), Theorem 5.1, proves that every polytope is covered by the disks or balls with diameter joining its vertices to an arbitrary point; Corollary 5.3 identifies a subordinate power-diagram tiling. Neither theorem determines the areas occupied by each number of overlapping balls. The present result specifies their full planar distribution for every regular polygon with the center as distinguished point. Huemer and Pérez-Lantero (2014) and Herrera and Pérez-Lantero (2018) study intersection graphs of disks whose **polygon sides**, rather than vertex-to-center segments, are diameters; these are different geometric families and do not determine the distribution above. Exact multiplicity area spectra differ from existence of a cover, from a pairwise intersection graph, and from a partition into nonoverlapping power cells.

## Limitations
No assertion is made about arbitrary convex polygons or other center placements, or about the topology of each individual stratum. Numerical checks are finite and not a substitute for the analytical proof. A historical equivalent outside searched literature cannot be ruled out; no independent mathematical audit has been performed.

## References
- J. Pavlík, *Thales's theorem in higher dimensions*, arXiv:2611.14277 (first version posted 2026-11-10), https://arxiv.org/abs/2611.14277, especially Theorem 5.1 and Corollary 5.3.
- C. Huemer and P. Pérez-Lantero, *The intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1410.4126 (2014), https://arxiv.org/abs/1410.4126.
- L. H. Herrera and P. Pérez-Lantero, *On the intersection graph of the disks with diameters the sides of a convex n-gon*, arXiv:1805.10847 (2018), https://arxiv.org/abs/1805.10847.
