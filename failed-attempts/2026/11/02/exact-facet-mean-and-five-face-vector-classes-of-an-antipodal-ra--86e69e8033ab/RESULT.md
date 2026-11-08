# Exact facet mean and five face-vector classes of an antipodal random four-polytope

## Finding
Let \(X_1,\ldots,X_5\) be independent uniform points on the unit sphere \(S^3\subset\mathbb R^4\), and let \(P=\operatorname{conv}\{\pm X_i:1\le i\le5\}\). Almost surely, \(P\) is a simplicial centrally symmetric four-polytope with ten vertices. Its entire face vector has the form
\[
(f_0,f_1,f_2,f_3)=(10,40-2e,60-4e,30-2e),\qquad e\in\{0,1,2,3,4\},
\]
where every one of the five cases occurs with positive probability. In particular the set of possible facet numbers is exactly \(\{22,24,26,28,30\}\). More importantly, the expected facet number has the exact non-rational value
\[
\boxed{\mathbb E f_3(P)=40-\frac{45056}{315\pi^2}=25.507532539\ldots.}
\]
Consequently
\[
\mathbb E(f_0,f_1,f_2,f_3)=\left(10,\;50-\frac{45056}{315\pi^2},\;80-\frac{90112}{315\pi^2},\;40-\frac{45056}{315\pi^2}\right).
\]
These are the face numbers of the ordinary Euclidean convex hull, not a spherical polytope or a Gaussian projection.

## Assumptions and scope
The sphere has radius one, dimension three intrinsically, and is equipped with rotation-invariant probability measure; the five original sphere points are independent. The ten points include their deterministic antipodes. The face vector counts nonempty proper faces by dimensions zero through three. All assertions about exact face classes are almost sure or concern realizations in the open general-position regime; zero-measure degeneracies (linearly dependent quadruples or a five-vertex supporting hyperplane) are excluded. The mean is an unconditional expectation, and all bases of logarithms and orientations are irrelevant.

## Proof
**Step 1: An exact circuit and facets.** With probability one the five vectors span \(\mathbb R^4\) and have a unique linear relation with nonzero coefficients. Each sign of a generating vector can be reversed without changing \(P\); after doing so the relation is \(\sum_{i=1}^5a_iX_i=0\) with \(a_i>0\) and \(\sum_i a_i=1\). Since all vectors have Euclidean norm one, the triangle inequality applied to any term gives \(a_i\le1-a_i\), with strict inequality in the full-rank, noncollinear case. Hence \(0<a_i<1/2\). Almost surely no nontrivial subset of the \(a_i\) sums to \(1/2\). The ten signed points are distinct and are all vertices because each is the unique maximizer of its own Euclidean supporting functional among distinct sphere points. A supporting facet cannot contain an antipodal pair, because \(0\) is interior; generically every facet therefore consists of one signed point from each of four distinct pairs.

Fix the omitted index \(j\) and signs \(\epsilon_i\in\{-1,1\}\) for \(i\ne j\). The four chosen points define a unique normalized supporting affine functional \(u\) with \(\langle u,\epsilon_iX_i\rangle=1\), in general position. It bounds a facet exactly if \(|\langle u,X_j\rangle|<1\). The circuit identity makes this equivalent to
\[
\left|\sum_{i\ne j}a_i\epsilon_i\right|<a_j.\tag{1}
\]
Let a coalition \(T\subseteq\{1,\ldots,5\}\) be *winning* when \(\sum_{i\in T}a_i>1/2\). For a given omitted \(j\), (1) is in bijection with a winning coalition containing \(j\) that becomes losing upon removal of \(j\): take the signs positive on \(T\setminus\{j\}\) and negative outside it. Thus the number of facets equals the number of pivotal (coalition, member) pairs.

**Step 2: Count all pivotal pairs.** Let \(e\) be the number of winning two-member coalitions, equivalently the number of edges \(ij\) for which \(a_i+a_j>1/2\). A singleton loses and every four-member coalition wins, because each weight is below one half. Winning two-member coalitions contribute \(2e\) pivotal pairs. The winning triples are exactly the complements of losing pairs, so there are \(10-e\). These triples contribute \(3(10-e)-3e=30-6e\) pivotal pairs: a player in a winning triple ceases to be pivotal exactly when the other two players form a winning pair; each such pair is contained in three triples. Winning four-member coalitions contribute \(2e\) pivotal pairs, indexed by each winning pair and the choice of which of its two members is removed from the corresponding four-member coalition. The full coalition contributes none. Hence
\[
f_3(P)=2e+(30-6e)+2e=30-2e.\tag{2}
\]
Two distinct winning pairs cannot be disjoint, since their four positive weights would sum to more than one. Any pairwise-intersecting family of distinct two-element subsets on five labels is a star (at most four edges) or a triangle (three edges). Consequently \(0\le e\le4\). Every triangle face of a simplicial four-polytope belongs to precisely two tetrahedral facets, so \(f_2=2f_3\). Euler's boundary relation \(f_0-f_1+f_2-f_3=0\) with \(f_0=10\) yields \(f_1=10+f_3\). This proves the asserted five face vectors.

**Step 3: No missing class, with unit-sphere realizations.** Suitable five-tuples of strictly positive rational circuit weights, in order of \(e=0,1,2,3,4\), are
\[
(1/5,1/5,1/5,1/5,1/5),\quad(300,215,180,160,145)/1000,\quad(32,21,19,14,14)/100,
\]
\[
(37,18,17,16,12)/100,\qquad(40,15,15,15,15)/100.
\]
Each tuple has maximum weight below one half, exactly the indicated count of winning pairs, and no subset sum equal to one half. To realize any tuple by unit vectors of rank four, write \(k=a_1/(1-a_1)\), \(\rho=\sqrt{1-k^2}\), and \(t=1/5\). Choose unit vectors \(Y_2,Y_3\in\operatorname{span}(e_1,e_2)\subset\mathbb R^3\) such that \(a_2Y_2+a_3Y_3=te_1\), and \(Y_4,Y_5\in\operatorname{span}(e_1,e_3)\) such that \(a_4Y_4+a_5Y_5=-te_1\). The strict triangle inequalities \(|a_2-a_3|<t<a_2+a_3\) and \(|a_4-a_5|<t<a_4+a_5\) hold for all five tuples; choose transverse components of opposite signs. Put \(X_1=(1,0,0,0)\) and \(X_i=(-k,\rho Y_i)\) for \(2\le i\le5\). Then each \(X_i\) has norm one, \(\sum_i a_iX_i=0\), and the five vectors have rank four. All inequalities are strict, so each of the five cases occurs on an open, positive-measure subset of \((S^3)^5\).

**Step 4: A spherical hyperplane integral.** There are exactly \(5\cdot2^4=80\) distinct *candidate* facets (choose the omitted antipodal pair and signs on four chosen pairs). By sign and permutation invariance each has the same probability. Let \(H\in(0,1)\) be the unsigned distance of the affine hull of four independent uniform points on \(S^3\) from the origin. The spherical Blaschke--Petkantschin formula gives its density
\[
g(h)=\frac{256}{35\pi}(1-h^2)^{7/2},\qquad0<h<1.\tag{3}
\]
The exponent \(7/2\) is the specialization of the standard spherical facet-hyperplane density \((d^2-2d-1)/2\) at ambient dimension \(d=4\); its normalizing constant follows by the beta integral \(\int_0^1(1-h^2)^{7/2}\,dh=35\pi/256\). The fifth independent antipodal pair lies strictly on the inner side of the hyperplane precisely when its projection onto the unit normal has absolute value less than \(H\). A uniform point on \(S^3\) has one-coordinate density \(2\sqrt{1-z^2}/\pi\), so the conditional probability is
\[
q(h)=\frac2\pi\left(\arcsin h+h\sqrt{1-h^2}\right).\tag{4}
\]
Linearity of expectation therefore gives
\[
\mathbb Ef_3(P)=80\int_0^1 g(h)q(h)\,dh
=\frac{40960}{35\pi^2}\int_0^{\pi/2}\cos^8\theta\,(\theta+\sin\theta\cos\theta)\,d\theta.
\]
Here \(h=\sin\theta\). Two exact elementary integrals are
\[
\int_0^{\pi/2}\theta\cos^8\theta\,d\theta=\frac{35\pi^2}{1024}-\frac29,
\qquad\int_0^{\pi/2}\sin\theta\cos^9\theta\,d\theta=\frac1{10}.
\]
Substitution yields \(\mathbb Ef_3(P)=40-45056/(315\pi^2)\). The other expectations follow from the deterministic face-number identities, completing the proof.

## Verification
The standalone `check.py` independently enumerates all \(80\) sign patterns for each of five exact-rational circuit examples, constructs five actual inscribed four-polytopes, compares the facets with `scipy.spatial.ConvexHull`, and checks the symbolic integral identities with SymPy. A seeded experiment with \(8000\) independent five-pair random samples checks the circuit-versus-hull formula samplewise and compares the empirical facet mean with its analytic expectation. Run with `python check.py` using Python 3, NumPy, SciPy, and SymPy. Its actual final output is `ALL_CHECKS_PASSED`. The universal proof is the analytic argument above, not the finite simulation.

## Relationship to prior work
Novik's survey of centrally symmetric polytopes (arXiv:1711.09310v1, 2017) discusses neighborliness and face-number restrictions of centrally symmetric four-polytopes, including established ten-vertex neighborly examples; such existence statements are not claimed new. Bonnet--O'Reilly, *Facets of spherical random polytopes* (arXiv:1908.04033v1, 2019), give the classical spherical facet-height integral for **independent individual vertices**; the spherical hyperplane density in (3) is a credited input, while the antipodal-pair containment event (4) is a different sampling mechanism. Akopyan--Edelsbrunner--Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere* (arXiv:2007.07783v1, 2020), discuss random polytopes and antipodal variants in three-dimensional ambient space, whereas the random four-dimensional five-pair face-vector mean is addressed here. Older centrally symmetric Gale-diagram literature (notably McMullen--Shephard, 1968) may subsume the deterministic circuit classification; the exact stochastic integral is the main claim and is compared separately. Random linear projections of crosspolytopes with Gaussian, nonconstant column lengths must not be identified with uniform points on the sphere.

## Limitations
This result is for exactly five independent antipodal pairs on \(S^3\); it does not give a full probability distribution over the five face vectors, general sample-size formulas, or a higher-dimensional universality law. The deterministic part may be obtainable from older Gale-diagram theory. Priority of the exact expectation remains provisional pending exhaustive historical access; the older McMullen--Shephard full text was not accessible in this check. No independent external audit has been performed.

## References
1. I. Novik, *A tale of centrally symmetric polytopes and spheres*, arXiv:1711.09310v1 (first posted 2017-11-25), https://arxiv.org/html/1711.09310v1 .
2. G. Bonnet and E. O'Reilly, *Facets of spherical random polytopes*, arXiv:1908.04033v1 (first posted 2019-08-12), https://onlinelibrary.wiley.com/doi/full/10.1002/mana.202000314 .
3. A. Akopyan, H. Edelsbrunner, and A. Nikitenko, *The Beauty of Random Polytopes Inscribed in the 2-sphere*, arXiv:2007.07783v1 (first posted 2020-07-15), https://arxiv.org/html/2007.07783v1 .
4. P. McMullen and G. C. Shephard, *Diagrams for centrally symmetric polytopes* (1968), DOI:10.1112/S0025579300002473 (full text not inspected).
