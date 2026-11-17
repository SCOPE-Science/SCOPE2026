# Exact face-vector law and uniform-square exponent for affine sections of regular simplices

## Finding

Let \(n\ge3\) be an integer. Intersect a regular \((n-1)\)-simplex with an affine hyperplane drawn from Euclidean-motion-invariant hyperplane measure, conditional on meeting the simplex. Write \(K_n\) for the number of simplex vertices on one designated side and \(f_j(n)\) for the number of \(j\)-faces of the section. The orientation of the hyperplane is chosen symmetrically; the face vector does not depend on it.

If \(G_1,\ldots,G_n\) are independent standard normal variables, \(G_{(1)}<\cdots<G_{(n)}\) their order statistics, \(M_n=\max_i G_i\), and \(\Phi\) the standard normal distribution function, then for every \(1\le k\le n-1\),
\[
\Pr(K_n=k)=\frac{\mathbb E(G_{(k+1)}-G_{(k)})}{2\mathbb E M_n}
=\frac{\binom nk\int_{-\infty}^{\infty}\Phi(z)^k[1-\Phi(z)]^{n-k}\,dz}{2\mathbb E M_n}.
\]
Almost surely, the section is combinatorially \(\Delta_{k-1}\times\Delta_{n-k-1}\) conditional on \(K_n=k\); hence its complete face-vector distribution is the pushforward of this explicit finite probability mass function under
\[
 f_j(n)=\sum_{a=1}^{j+1}\binom{K_n}{a}\binom{n-K_n}{j+2-a},\qquad 0\le j\le n-2,
\]
where out-of-range binomial coefficients are zero. In particular \(f_0(n)=K_n(n-K_n)\), and
\[
\mathbb E f_0(n)=\frac{n(n-1)}{2\sqrt\pi\,\mathbb E M_n}
\sim\frac{n^2}{2\sqrt{2\pi\log n}}.
\]
There is a nondegenerate limiting law for the **typical** section complexity. Let \(U\) be uniform on \([-1,1]\). For each fixed nonnegative integer \(r\),
\[
\left(\frac{\log f_j(n)}{\log n}\right)_{j=0}^r
\ \xrightarrow{d}\ (j+2-U^2)_{j=0}^r.
\]
In particular, writing \(Y=2-U^2\),
\[
\Pr(Y\le y)=\begin{cases}
0,&y<1,\\
1-\sqrt{2-y},&1\le y\le2,\\
1,&y>2.
\end{cases}
\]
Thus the expected vertex count has exponent tending to \(2\) although the sampled vertex-count exponent has a nonconstant limit taking values between \(1\) and \(2\).

## Assumptions and scope

Work in \(E=\{x\in\mathbb R^n:\sum_i x_i=0\}\), with its inherited Euclidean metric, and take the simplex \(\operatorname{conv}\{e_i-\frac1n\mathbf 1:1\le i\le n\}\subset E\). An oriented hyperplane is \(H(v,t)=\{x\in E:\langle v,x\rangle=t\}\) with \(v\in S(E)\) and \(t\in\mathbb R\). The probability measure is proportional to \(d\sigma(v)\,dt\), restricted to planes intersecting the simplex. In particular, the normal is **not** uniform after conditioning: its density is proportional to the directional width. The choice of orientation has a twofold symmetry, which does not affect section geometry. Hyperplanes containing vertices or entire edges constitute a null set. We consider face dimensions \(0\le j\le n-2\) and fixed \(r\) as \(n\to\infty\). A zero-dimensional section from a supporting plane has probability zero.

## Proof

**1. Face lattice.** In a generic direction the support values at the \(n\) vertices are distinct. If the plane divides them into blocks of sizes \(k\) and \(n-k\), it crosses exactly the edges joining opposite blocks, giving \(k(n-k)\) section vertices. More generally, each face of the section is the transverse intersection with the convex hull of a nonempty subset of each block. Choosing \(a\) vertices from the first block and \(b\) from the second gives a section face of dimension \(a+b-2\). Distinct subsets give distinct faces, and all faces arise this way. This is exactly the face lattice of \(\Delta_{k-1}\times\Delta_{n-k-1}\), proving the stated binomial formula in every dimension, including the cases \(k=1\) and \(k=n-1\).

**2. Correct invariant measure and exact rank law.** Let \(a_i(v)=\langle v,e_i-\frac1n\mathbf1\rangle=v_i\) and order these values increasingly. A fixed normal \(v\) permits offsets \(a_{(1)}(v)<t<a_{(n)}(v)\). The offsets with exactly \(k\) vertices below the plane form an interval of length \(a_{(k+1)}(v)-a_{(k)}(v)\). Dividing its orientation-averaged length by the averaged total permitted width gives the invariant measure probability.

Take independent \(G_i\sim N(0,1)\), set \(\bar G=n^{-1}\sum_i G_i\), \(R=\sqrt{\sum_i(G_i-\bar G)^2}\), and \(v_i=(G_i-\bar G)/R\). Gaussian rotational invariance on \(E\) makes \(v\) Haar-uniform on \(S(E)\) and independent of \(R\). Both the order-statistic gap and the total range of the \(G_i\) are \(R\) times their counterparts for the \(v_i\). Thus the common factor \(\mathbb E R\) cancels in the ratio, yielding
\[
\Pr(K_n=k)=\frac{\mathbb E(G_{(k+1)}-G_{(k)})}{\mathbb E(G_{(n)}-G_{(1)})}.
\]
Symmetry gives \(\mathbb E(G_{(n)}-G_{(1)})=2\mathbb E M_n\). Integrating the indicator of the event \(G_{(k)}\le z<G_{(k+1)}\) gives
\[
\mathbb E(G_{(k+1)}-G_{(k)})
=\binom nk\int_{\mathbb R}\Phi(z)^k[1-\Phi(z)]^{n-k}\,dz.
\]
These terms are nonnegative and telescope to the expected range, so they sum to probability one.

**3. Exact expected number of vertices.** For fixed \(v\), the sum of lengths of offset intervals that cross each simplex edge \([e_i,e_j]\) is \(\sum_{i<j}|v_i-v_j|\). Integrate and divide by mean width. Gaussian radial cancellation as above yields
\[
\mathbb E f_0(n)=\frac{\sum_{i<j}\mathbb E|G_i-G_j|}{\mathbb E(G_{(n)}-G_{(1)})}.
\]
Since \(G_i-G_j\sim N(0,2)\), its absolute mean is \(2/\sqrt\pi\), proving the finite formula. Standard Gaussian maximum bounds, obtained for instance from \(\Pr(M_n\le t)=\Phi(t)^n\), give \(\mathbb EM_n\sim\sqrt{2\log n}\) and hence the asserted asymptotic.

**4. Typical logarithmic face laws.** First draw an **unweighted** Gaussian sample \(G_1,\ldots,G_n\) and an independent \(U\sim\mathrm{Unif}[-1,1]\), and set
\[
T_n=\tfrac12(1-U)G_{(1)}+\tfrac12(1+U)G_{(n)}.
\]
Use the threshold to form the rank \(\widetilde K_n=\#\{i:G_i<T_n\}\). In the exact invariant section model the Gaussian direction must instead be weighted by
\[
 h_n(G)=\frac{G_{(n)}-G_{(1)}}{\sqrt{\sum_i(G_i-\bar G)^2}}.
\]
This is the directional width, and the corresponding probability density relative to Gaussian measure is \(h_n/\mathbb Eh_n\). The Gaussian maximum/minimum laws and the chi-square law of the centered norm imply
\[
\frac{h_n}{2\sqrt{2\log n}/\sqrt n}\longrightarrow1
\quad\text{in probability},\qquad
\frac{\mathbb Eh_n}{2\sqrt{2\log n}/\sqrt n}\longrightarrow1.
\]
The second limit follows also from \(\mathbb E(G_{(n)}-G_{(1)})=(\mathbb ER)(\mathbb Eh_n)\) and \(\mathbb ER\sim\sqrt n\). Since \(h_n/\mathbb Eh_n\) is nonnegative, has mean one, and converges in probability to one, it converges to one in \(L^1\). Therefore the correct width-biased and the unweighted Gaussian constructions have total variation distance tending to zero for every statistic of the sample and \(U\).

Under the unweighted construction, \(G_{(1)}/\sqrt{2\log n}\to-1\) and \(G_{(n)}/\sqrt{2\log n}\to1\) in probability. Consequently \(T_n/\sqrt{2\log n}-U\to0\) in probability. For any fixed \(u\in(-1,1)\), Gaussian tail bounds and binomial concentration at the bracketing deterministic levels \((u\pm\varepsilon)\sqrt{2\log n}\) show that the smaller of the counts below and above \(T_n\) has logarithmic exponent \(1-u^2\). This remains valid when the random threshold depends on the sample, because the counts are sandwiched between counts at the two deterministic bracketing levels. At \(u=0\) the exponent is \(1\), and the endpoints \(u=\pm1\) have probability zero. Conditioning on \(U\) and then removing a set of arbitrarily small \(U\)-measure around the endpoints gives
\[
\frac{\log\min(\widetilde K_n,n-\widetilde K_n)}{\log n}
-(1-U^2)\longrightarrow0
\quad\text{in probability}.
\]
For every fixed \(j\ge0\), writing \(s=\min(\widetilde K_n,n-\widetilde K_n)\) and \(\ell=n-s\), the exact product face formula implies, for \(\ell\ge j+1\),
\[
 s\binom{\ell}{j+1}\le f_j(n)
\le C_j s n^{j+1},
\]
where \(C_j<\infty\) depends only on \(j\). The lower bound chooses a vertex of the smaller simplex factor and a \(j\)-face of the larger; the upper bound sums at most \(j+1\) terms, each at most a constant times \(s n^{j+1}\). Since \(\ell/n\to1\) except on a null set of limiting \(U\), these bounds show \(\log f_j(n)/\log n-(j+2-U^2)\to0\) in probability. Joint convergence for finitely many \(j\) follows by the same coupling. Total variation asymptotic equivalence transfers the law to the original invariant hyperplane measure.

## Verification

The standalone program `check_affine_simplex_section.py` evaluates the one-dimensional normal integrals for \(n=3,4,6,8\); tests the exact mean identity and symmetry; independently enumerates crossed faces to confirm the product formula for all side splits; and compares the finite probabilities against randomly oriented hyperplanes with the **necessary width-weight correction**. For dimensions \(300,1200,4800\), it checks the progression toward the simultaneous logarithmic face-exponent laws for face dimensions zero, one, and two. The program completed with `AFFINE_SIMPLEX_SECTION_FACE_VECTOR_CHECKS_PASSED`. These checks are finite corroboration; all-dimensional and limit claims rest on the preceding proof.

## Relationship to prior work

Brandenburg, De Loera, and Meroni [1] establish fixed-edge-set chambers for affine polytope sections (notably their Theorem 1.1 and Lemma 2.6). Their chamber descriptions explain where section combinatorics change but do not give the Crofton-probability law and its high-dimensional logarithmic limit. König [2] treats maximal non-central **volumes and perimeters** of sections of the same simplex, rather than the invariant distribution of face vectors. Gaussian simplex-width and maximum calculations [3] provide a normalization that appears in the mean formula, not the full section law. Baryshnikov and Vitale [4] address rotated simplex **projections**, not offset-uniform affine hyperplane intersections. Central hyperplane-section fluctuations in related work impose a fixed offset and therefore involve a different probability law. A general Crofton identity can recover the mean number of intersected edges; the nonconstant typical polynomial exponent and its joint face-vector law are the primary new assertions, rather than Crofton linearity alone.

## Limitations

The normalization uses invariant affine-hyperplane measure **conditioned on hitting the simplex**. Sampling a uniform normal first and then a uniform hitting offset without width bias defines a different finite-dimensional law. The theorem concerns a regular simplex and fixed face dimensions as its number of vertices grows; it does not give a joint limit when the face dimension increases with \(n\), quantitative convergence rates, or face volumes. Novelty is assessed against the inspected primary literature and indexed records; equivalent older stochastic-geometry formulations have not been ruled out by exhaustive human review.

## References

[1] M.-C. Brandenburg, J. A. De Loera, and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first public version 2023-04-27, https://arxiv.org/abs/2304.14239.

[2] H. König, *Non-central sections of the simplex, the cross-polytope and the cube*, arXiv:2002.10743, first public version 2020-02-25, https://arxiv.org/pdf/2002.10743.

[3] Z. Kabluchko, A. E. Litvak, and D. Zaporozhets, *Mean Width of Regular Polytopes and Expected Maxima of Correlated Gaussian Variables*, arXiv:1511.08479, first public version 2015-11-26, https://arxiv.org/abs/1511.08479.

[4] Y. M. Baryshnikov and R. A. Vitale, *Regular simplices and Gaussian samples*, Discrete & Computational Geometry 11 (1994), 141–147, https://doi.org/10.1007/BF02574000.
