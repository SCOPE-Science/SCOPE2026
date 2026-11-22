# A Rayleigh-mixed Poisson overlap law for periodic vertices of independent random mappings

## Finding
For any fixed integer \(q\ge2\), take \(q\) independent uniform random functions \(f_i:[n]\to[n]\). Write \(C_i\) for the set of vertices periodic under iteration of \(f_i\), and \(X_{ij}=|C_i\cap C_j|\) for each \(1\le i<j\le q\). Let \(R_1,\ldots,R_q\) be independent Rayleigh random variables with density \(r e^{-r^2/2}\), \(r>0\). Conditional on these variables, let the \(Y_{ij}\), \(i<j\), be independent Poisson random variables of means \(R_iR_j\). Then, jointly over all \(\binom q2\) pairs,
\[
(X_{ij})_{i<j}\ \xrightarrow{d}\ (Y_{ij})_{i<j}.
\]
In particular, for two maps,
\[
\lim_{n\to\infty}\Pr(C_1\cap C_2=\varnothing)=\mathbb E e^{-R_1R_2}=\frac13,
\]
so the probability of at least one common periodic vertex tends to \(2/3\). For any two distinct index pairs, the limiting covariance is \(\pi-\pi^2/4>0\) if they share one map and zero if they have no map in common. The latter overlap counts are exactly independent for every finite \(n\). The mean and variance of one limiting overlap count are respectively \(\pi/2\) and \(4+\pi/2-\pi^2/4\).

## Assumptions and scope
A uniform map on \([n]\) means that all \(n^n\) functions are equiprobable, equivalently its images at distinct vertices are independent and uniform. A vertex is periodic if \(f_i^m(v)=v\) for some integer \(m\ge1\). The number \(q\) of sampled functions is fixed as \(n\to\infty\). All pairs use the same labelled vertex set. The theorem concerns coincident *periodic vertices*, not common directed cycles, common edges or agreement of the maps themselves. All stochastic limits are unconditioned, and the mixing variables \(R_i\) are nondegenerate.

## Proof
**1. Cyclic-core size and exchangeability.** For one uniform mapping let \(K=|C|\). Fixing a set of \(k\) periodic vertices, the map restricts to one of \(k!\) permutations on this set; the other \(n-k\) vertices form a forest rooted at these \(k\) vertices. The rooted-forest count is \(k n^{n-k-1}\), with the \(k=n\) case understood by cancellation. Thus for \(1\le k\le n\),
\[
\Pr(K=k)=\frac{k(n)_k}{n^{k+1}},\qquad
\Pr(K\ge k)=\frac{(n)_k}{n^k},
\]
where \((x)_k=x(x-1)\cdots(x-k+1)\). Conditional on \(K=k\), the set \(C\) is a uniformly distributed \(k\)-subset of \([n]\), by label-exchangeability. In particular, the cyclic sets of independent maps are independent conditional on their sizes. For fixed \(x>0\), taking \(k=\lceil x\sqrt n\rceil\) in the tail formula gives
\[
\Pr(K/\sqrt n\ge x)\longrightarrow e^{-x^2/2}.
\]
The bound \(\Pr(K\ge k)\le\exp[-k(k-1)/(2n)]\) implies uniform integrability of every fixed power of \(K/\sqrt n\). Therefore \(K/\sqrt n\Rightarrow R\), a unit-scale Rayleigh variable, and all fixed positive moments converge. For the independent maps, the rescaled sizes converge jointly to independent \(R_i\).

**2. Deterministic-size overlap lemma.** Suppose independently sampled uniform subsets \(S_i\subset[n]\) have deterministic sizes \(m_i=m_i(n)\), with \(m_i/\sqrt n\to r_i>0\) for every \(i\le q\). For nonnegative fixed integers \(a_{ij}\) write \(d_i=\sum_{j\ne i}a_{\min(i,j),\max(i,j)}\) and \(L=\sum_{i<j}a_{ij}\). Expand the mixed falling factorial moment of the counts \(|S_i\cap S_j|\) by selecting ordered witness vertices for every pair. Terms where all \(L\) witnesses are distinct contribute exactly
\[
(n)_L\prod_{i=1}^q\frac{(m_i)_{d_i}}{(n)_{d_i}}
\ \longrightarrow\ \prod_{i<j}(r_i r_j)^{a_{ij}}.
\]
Every collision between witnesses assigned to *different* index pairs forces one vertex to belong to at least three distinct subsets (or to four for disjoint index pairs). For any fixed collision configuration with \(h<L\) distinct witnesses, the corresponding expectation is bounded by a constant times \(n^{h-\sum_v |I_v|/2}\), where \(I_v\) is the union of map indices demanded at witness \(v\). Since at least one witness has \(|I_v|\ge3\) and all have \(|I_v|\ge2\), this is \(O(n^{-1/2})\). Hence all collisions vanish. The limiting mixed falling factorial moments are precisely those of independent Poisson variables with means \(r_ir_j\). Moreover, each coordinate has bounded exponential moments uniformly when the \(m_i/\sqrt n\) remain bounded, since its factorial moments are at most \((m_im_j/n)^a\). Hölder's inequality bounds the joint exponential moments in a neighborhood of the origin, so these factorial moments determine joint weak convergence.

**3. Random-size mixing.** The conditional lemma applies to every deterministic size sequence whose rescaled vector tends to a point in \((0,\infty)^q\). Conditional expectations of any bounded continuous function of the overlap array therefore converge to the corresponding independent-Poisson expectation, continuously in the limiting size vector. Combining this with the joint Rayleigh convergence and tightness from Step 1 yields the asserted Rayleigh-mixture limit. For each fixed triple of maps, the expected count of vertices belonging to all three cyclic sets is \((\mathbb E K)^3/n^2=O(n^{-1/2})\), so such triple coincidences disappear in probability; nevertheless pair-count dependence survives through the shared Rayleigh size.

**4. Exact empty-intersection probability.** The mixture limit gives \(\Pr(X_{12}=0)\to\mathbb E[e^{-R_1R_2}]\) because the variables are integer-valued (test at \(1/2\)). Using the two Rayleigh densities, the expectation is
\[
\int_0^\infty\!\int_0^\infty rs\,e^{-(r+s)^2/2}\,dr\,ds.
\]
Substitute \(u=r+s\), \(v=r/(r+s)\), whose Jacobian is \(u\). The integral factors as
\[
\left(\int_0^\infty u^3e^{-u^2/2}\,du\right)
\left(\int_0^1v(1-v)\,dv\right)=2\cdot\frac16=\frac13.
\]

**5. Covariance and moments.** Let \(\mu_n=\mathbb E K\) and \(\sigma_n^2=\operatorname{Var}(K)\). Conditional on the cyclic set of map \(i\), the overlaps \(X_{ij}\) and \(X_{ik}\) are independent if \(j\ne k\), and each has conditional mean \(K_i\mu_n/n\). Thus, for distinct \(j,k\),
\[
\operatorname{Cov}(X_{ij},X_{ik})
=\frac{\mu_n^2\sigma_n^2}{n^2}
\ \longrightarrow\ \left(\frac\pi2\right)\left(2-\frac\pi2\right)
=\pi-\frac{\pi^2}4.
\]
For disjoint index pairs the counts depend on disjoint independent maps and are independent exactly. Also \(\mathbb E X_{ij}=\mu_n^2/n\to\pi/2\). Under the limiting mixed-Poisson law, conditional variance equals conditional mean, so \(\operatorname{Var}(Y_{ij})=\mathbb E(R_iR_j)+\operatorname{Var}(R_iR_j)=\pi/2+4-\pi^2/4\), using \(\mathbb ER_i=\sqrt{\pi/2}\) and \(\mathbb ER_i^2=2\).

## Verification
Run `python checker.py` using a standard Python 3 installation. The standalone script exhaustively enumerates all uniform maps for \(1\le n\le5\), checks the exact labelled cyclic-set counts, reconstructs the full pair-intersection distribution in two independent ways using rational arithmetic, and checks the exact three-map covariance identity. It reports 102 assertion groups and additionally prints exact-formula numerical probabilities for selected larger sizes. These finite checks are reproducibility tests, not substitutes for the general proof. The empty-intersection integral and the limiting moments were verified independently by symbolic calculation and the direct calculations displayed above.

## Relationship to prior work
The classical random-mapping cyclic-core law and conditional uniformity are used as inputs. Hansen and Jaworski, *A new random mapping model* (first arXiv version 22 March 2006), study one-map cyclic-point and component statistics, including in-degree variants. Hansen and Jaworski, *Random Mappings with a Given Number of Cyclical Points* (2010), study the typical component and component size partitions conditioned on cyclic-core size. The present assertion concerns intersections of *independently drawn* periodic sets, their full fixed-\(q\) joint law, and a rational empty-intersection probability; these are not statements of the cited sources. No priority claim is made over uninspected or unindexed independent-map literature.

## Limitations
The number of maps must remain fixed as \(n\to\infty\); no uniformity for growing \(q\) is proved. Nothing here identifies common directed cycles, synchronized periodic trajectories, or shared images, and those events need not have the same limit. The theorem gives weak convergence and exact finite covariance identities, not an optimal convergence rate or total-variation estimate. The literature comparison does not exclude older equivalent results under alternative terminology.

## References
1. J. C. Hansen and J. Jaworski, *A new random mapping model*, arXiv:math/0603529, initial version 2006-03-22. https://arxiv.org/abs/math/0603529
2. J. C. Hansen and J. Jaworski, *Random Mappings with a Given Number of Cyclical Points*, Ars Combinatoria **94** (2010), 341–359. https://combinatorialpress.com/ars-articles/volume-094-ars-articles/random-mappings-with-a-given-number-of-cyclical-points/
3. V. F. Kolchin, *Random Mappings*, Optimization Software, 1986 (classical background).
