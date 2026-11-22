# An exact type-A permutohedral ridge-angle law and its second-order Gaussian variance

## Finding
For every integer \(n\ge3\) and every strictly decreasing real vector \(x_1>\cdots>x_n\), let \(P_n(x)\) be the convex hull in \(\mathbb R^n\) of all coordinate permutations of \(x\). Equip its \((n-1)\)-dimensional affine hull with the induced Euclidean metric, and select a codimension-two face (ridge) uniformly among distinct faces. Let \(\Theta_n\) be its **interior** dihedral angle.

The complete ridge-angle multiset is indexed, with multiplicity, by positive integer triples \((a,b,c)\) with \(a+b+c=n\):
\[
\theta_{a,b,c}=\pi-\arccos\sqrt{\frac{ac}{(a+b)(b+c)}},\qquad
m_{a,b,c}=\frac{n!}{a!b!c!}.
\]
Consequently, for every bounded function \(\varphi\),
\[
\mathbb E\varphi(\Theta_n)=\frac{1}{3^n-3\cdot2^n+3}
\sum_{\substack{a,b,c\ge1\\a+b+c=n}}
\frac{n!}{a!b!c!}\varphi(\theta_{a,b,c}).
\]
The finite-dimensional mean is exactly \(\mathbb E\Theta_n=2\pi/3\) for all \(n\ge3\), a consequence also implied by previously known aggregate-angle identities. The new quantitative angular concentration calculation gives
\[
\sqrt n\left(\Theta_n-\frac{2\pi}{3}\right)
\ \xrightarrow{\mathrm d}\ \mathcal N\left(0,\frac38\right),\qquad
\operatorname{Var}(\Theta_n)=\frac{3}{8n}+\frac{63}{64n^2}+O(n^{-3}).
\]
All assertions, including the exact distribution, are independent of the particular strictly decreasing generating vector \(x\). The variance is zero at \(n=3\) and positive for \(n\ge4\).

## Assumptions and scope
The parameter \(n\) is an integer at least three. Strict inequalities among all entries of \(x\) are essential: repeated entries collapse the normal fan and change the face distribution. Faces are sampled by **count**, not by Euclidean ridge volume or by exterior angle. Angles are measured intrinsically in the affine hyperplane of coordinate sum \(\sum_i x_i\); an interior dihedral angle is the supplement of the acute angle between its two outward facet normals. The variance expansion is as \(n\to\infty\) through integers, and no uniformity across degenerating non-generic generating vectors is claimed (the normal-fan statement already covers every generic vector exactly).

## Proof
**1. Face parametrization and multiplicities.** The normal fan of a strictly generic type-A permutohedron is the braid arrangement. Its dimension-\((n-3)\) faces are in bijection with ordered partitions \((A,B,C)\) of \([n]\) into three nonempty blocks. This follows directly by sorting a supporting functional into its three equal-coordinate levels: the maximizers permute the corresponding three consecutive groups of distinct entries of \(x\). For fixed block sizes \((a,b,c)\) there are exactly \(n!/(a!b!c!)\) such ordered partitions. Inclusion-exclusion therefore gives \(3^n-3\cdot2^n+3\) ridges. This braid-fan/ordered-partition description is established background, not independently new.

**2. Metric angle.** The two facets incident to the ridge are indexed by the nested proper subsets \(A\subset A\cup B\). In the sum-zero linear space put
\[
 u_A=\mathbf1_A-\frac an\mathbf1,\qquad
 u_{A\cup B}=\mathbf1_{A\cup B}-\frac{a+b}{n}\mathbf1.
\]
They are outward facet normals up to a simultaneous reversal, which does not change their mutual angle. Their inner product and squared norms are
\[
 \langle u_A,u_{A\cup B}\rangle=\frac{ac}{n},\qquad
 \|u_A\|^2=\frac{a(b+c)}n,\qquad
 \|u_{A\cup B}\|^2=\frac{c(a+b)}n.
\]
Hence their cosine is exactly \(\sqrt{ac/((a+b)(b+c))}\), strictly between zero and one, and the interior angle is its supplement. This proves the complete finite multiset.

**3. Exact mean and Gaussian limit.** Write \(\alpha_{a,b,c}=\pi-\theta_{a,b,c}\). The three acute angles for the cyclic triples \((a,b,c),(b,c,a),(c,a,b)\) sum to \(\pi\): their cotangents are, in the same order,
\[
 \sqrt{\frac{ac}{bn}},\quad
 \sqrt{\frac{ab}{cn}},\quad
 \sqrt{\frac{bc}{an}},
\]
whose pairwise products sum to \((a+b+c)/n=1\); the acute-angle cotangent addition identity then gives the asserted sum. The multinomial multiplicities are unchanged by cyclic permutation, so \(\mathbb E\Theta_n=2\pi/3\).

Let \((A_n,B_n,C_n)\) have the multinomial distribution with \(n\) trials and equal probabilities \(1/3\), conditioned on all three counts being positive. This is exactly the random size triple. Conditioning changes probabilities by at most a constant times \((2/3)^n\). In a neighborhood of \((1/3,1/3)\) define
\[
 f(p,q)=\pi-\arccos\sqrt{\frac{p(1-p-q)}{(p+q)(1-p)}}.
\]
Then \(f(1/3,1/3)=2\pi/3\) and
\[
 \nabla f(1/3,1/3)=\left(0,-\frac{3\sqrt3}{4}\right).
\]
The two-dimensional multinomial central limit theorem has covariance matrix
\[
 \Sigma=\frac19\begin{pmatrix}2&-1\\-1&2\end{pmatrix}.
\]
The delta method therefore gives variance \((0,-3\sqrt3/4)\Sigma(0,-3\sqrt3/4)^{\mathsf T}=3/8\), as claimed.

**4. The second variance coefficient.** Put \(s=A_n/n-1/3\) and \(t=B_n/n-1/3\) temporarily without conditioning; the negligible probability of zero counts is handled at the end. Taylor-expand \(f\) at the balanced point as \(2\pi/3+L+Q+C+\text{terms of degree at least four}\), where
\[
 L=-\frac{3\sqrt3}{4}t,\qquad
 Q=-\frac{9\sqrt3}{8}s^2-\frac{9\sqrt3}{8}st+\frac{9\sqrt3}{16}t^2,
\]
\[
 C=-\frac{27\sqrt3}{16}(s^2t+st^2+t^3).
\]
Exact mixed centered multinomial moments (obtainable by factorial-moment expansion) yield
\[
 \mathbb E[L^2]=\frac{3}{8n},\quad
 \mathbb E[2LQ]=-\frac{9}{16n^2},\quad
 \mathbb E[Q^2+2LC]=\frac{99(2n-1)}{128n^3}.
\]
Here the constant expectation of the angle is exactly \(2\pi/3\), not merely asymptotic, so variance is the expectation of the squared centered angle. Combining the displayed identities yields \(3/(8n)+63/(64n^2)+O(n^{-3})\).

For rigor of the error: on the event that both proportions are within a fixed sufficiently small distance of \(1/3\), the function has bounded derivatives through order five. Terms omitted from its square have total degree at least five; centered multinomial moments of monomials of degree five are \(O(n^{-3})\), and absolute moments of order six are \(O(n^{-3})\). Taylor's remainder and higher products are therefore \(O(n^{-3})\) in expectation. The complementary event has exponentially small probability by standard multinomial concentration; the angle is bounded between \(\pi/2\) and \(\pi\) and the Taylor polynomials are bounded for proportions in the probability simplex. Conditioning on three positive counts contributes only an exponentially small correction. This completes the asymptotic proof.

## Verification
The included standalone `checker.py` reconstructs the two normal-vector formulas, the number and finite multinomial distribution of ridges, and their exact mean for small dimensions; it independently differentiates the angular function symbolically and checks the three multinomial-moment identities. It also compares direct finite angular variance sums with the asymptotic prediction at growing dimensions. Run from this package's extracted directory using `python checker.py`; Python 3 and SymPy are required. These finite and symbolic checks supplement the fully quantified analytic argument above and do not replace it.

## Relationship to prior work
Godland and Kabluchko, *Projections and Angle Sums of Belt Polytopes and Permutohedra*, arXiv:2009.04186, prove the braid normal-fan characterization (Theorem 4.3) and generalized aggregate angle sums (Theorem 4.11). The normal fan, face indexing, and aggregate-angle information are **prior results**, and the present proof explicitly uses them; in particular, the exact mean \(2\pi/3\) is not claimed to be a new standalone fact. The distinction is the size-resolved **unweighted-by-ridge-area** Euclidean angle multiset, its random-ridge Gaussian limit, and the exact second-order variance coefficient \(63/64\). Generalized-permutohedral face enumerations by Postnikov, Reiner and Williams also supply known combinatorial background, but not these metric second-moment formulas. Results on full type-B and type-D Coxeter ridge-angle spectra and cycle-graphical zonotopes provide related comparisons: their normal fans, face multiplicities or limiting distributions differ, so their statements do not imply this type-A variance expansion.

## Limitations
The assessment of research priority is provisional: an unindexed equivalent analysis of type-A ridge angles might exist. The result is not an independent audit or external certification. It does not treat nongeneric permutohedra, ridge-volume-weighted sampling, or other Coxeter types, and the asymptotic is for unweighted uniformly sampled ridges only. The classic angle-mean and face-count ingredients remain credited antecedents.

## References
1. T. Godland and Z. Kabluchko, *Projections and Angle Sums of Belt Polytopes and Permutohedra*, arXiv:2009.04186 (initial public version September 9, 2020); *Results in Mathematics* 78 (2023), article 140. https://arxiv.org/abs/2009.04186 ; https://doi.org/10.1007/s00025-023-01918-2 .
2. A. Postnikov, V. Reiner and L. Williams, *Faces of generalized permutohedra*, Documenta Mathematica 13 (2008), 207–273. https://doi.org/10.4171/DM/248 .
