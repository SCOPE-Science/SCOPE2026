# The exact Löwner ellipsoid of a single-class rank-two matroid base polytope

## Finding
For integers \(a,b\ge2\), partition \([a+b]=A\sqcup B\) with \(|A|=a\), \(|B|=b\), and define the clipped rank-two hypersimplex
\[
P_{a,b}=\operatorname{conv}\left(\{e_i+e_j:i\in A,\ j\in B\}\cup\{e_j+e_k:j,k\in B,\ j<k\}\right).
\]
This is the base polytope of the connected rank-two matroid whose sole nonsingleton parallel class is \(A\). Its affine hull is \(H=\{x\in\mathbb R^{a+b}:\sum_i x_i=2\}\), of intrinsic dimension \(d=a+b-1\).

Put \(n=a+b\), \(\kappa=1/a+1/b\), and let \(p\) be the **unique** number in \((0,1)\) satisfying
\[
\frac ap-\frac1{1-p}+\frac{(b-1)(3-b)}{2(b-2)+(3-b)p}=0.
\]
Equivalently, \(p\) is the unique maximizer of
\[
p^a(1-p)\,[2(b-2)+(3-b)p]^{b-1},\qquad 0<p<1.
\]
For \(b=2\), \(p=(a+1)/(a+2)\); for \(b=3\), \(p=a/(a+1)\). For \(b\ge4\), it is the unique root in \((0,1)\) of
\[
(a+b)(b-3)p^2-\big[(a+b-1)(b-3)+2(a+1)(b-2)\big]p+2a(b-2)=0.
\]
Define the center, a unit vector, and positive scalars by
\[
\begin{aligned}
c&=\frac pa\,\mathbf1_A+\frac{2-p}{b}\,\mathbf1_B,\\
u&=\frac{\mathbf1_A/a-\mathbf1_B/b}{\sqrt\kappa},\\
\sigma_A&=\frac pa,\\
\sigma_B&=\frac{2(b-2)+(3-b)p}{b(b-1)},\\
\sigma_T&=p(1-p)\kappa.
\end{aligned}
\]
Here \(\mathbf1_A,\mathbf1_B\) are coordinate indicators. Let \(\Pi_A\) and \(\Pi_B\) be orthogonal projections onto vectors supported respectively on \(A\) and \(B\) with coordinate sum zero. Let
\[
C=\sigma_A\Pi_A+\sigma_B\Pi_B+\sigma_Tuu^{\mathsf T}.
\]
On the tangent space \(H_0=\{z:\sum_i z_i=0\}\), this matrix is positive definite, and its positive-semidefinite extension to \(\mathbb R^n\) has kernel \(\mathbb R\mathbf1\).

**Theorem.** The unique minimum-volume ellipsoid containing \(P_{a,b}\), with intrinsic Euclidean volume measured in \(H\), is
\[
\boxed{\mathcal E_{a,b}=\{x\in H:(x-c)^{\mathsf T}C^+(x-c)\le d\},}
\]
where \(C^+\) is the inverse on \(H_0\) and zero on the constant direction. Its squared semiaxes are \(d\sigma_A\) (multiplicity \(a-1\)), \(d\sigma_B\) (multiplicity \(b-1\)), and \(d\sigma_T\) (multiplicity one), and its intrinsic volume is
\[
\boxed{\frac{\pi^{d/2}d^{d/2}}{\Gamma(1+d/2)}\sqrt{\sigma_A^{a-1}\sigma_B^{b-1}\sigma_T}.}
\]
**The complete contact set comprises exactly the \(ab+\binom b2\) vertices** of the polytope. The theorem is valid uniformly, with no asymptotic or genericity qualifications, for all integers \(a,b\ge2\). For instance, at \(a=2,b=3\), the unique mixing mass is \(p=2/3\) and the intrinsic squared semiaxes are \(4/3\) with multiplicity three and \(20/27\) with multiplicity one: the outer ellipsoid is anisotropic even though every vertex touches it.

## Assumptions and scope
Only bases containing at most one element of \(A\) are permitted. Thus \(P_{a,b}=\Delta_{2,n}\cap\{x:x(A)\le1\}\), the affine dimension is \(n-1\), and the two displayed vertex families are disjoint, complete and nonempty. The dimension assertion also follows directly: differences of suitable cross vertices span within-\(A\) and within-\(B\) sum-zero directions; subtracting a cross vertex from a \(B\)-pair vertex supplies an independent between-block direction. All norms, determinants, and volumes refer to the intrinsic Euclidean structure of \(H\), not the ambient space. The bound \(a,b\ge2\) ensures each of the three orthogonal subspaces has positive dimension.

## Proof
**1. A two-orbit probability design.** Assign probability \(p/(ab)\) to each cross vertex \(e_i+e_j\) (\(i\in A,j\in B\)), and probability \((1-p)/\binom b2\) to each \(B\)-pair vertex \(e_j+e_k\). This is a probability distribution for any \(p\in(0,1)\). If \(X\) is the random vertex, direct symmetry gives
\[
\mathbb EX=c=\frac pa\mathbf1_A+\frac{2-p}{b}\mathbf1_B.
\]
The tangent space splits orthogonally into the within-\(A\) differences, within-\(B\) differences, and the one-dimensional between-block direction \(u\). On the first space the covariance eigenvalue is \(p/a\), since an \(A\)-coordinate is uniformly selected with total probability \(p\). On the second space a uniform singleton contributes \(p/b\); a uniform unordered two-subset of \(B\) contributes \((1-p)2(b-2)/(b(b-1))\). Their sum is \(\sigma_B\). Along \(u\), the two vertex families have \(A\)-coordinate totals one and zero, so their centered scalar scores differ by \(\sqrt\kappa\); their variance is \(p(1-p)\kappa\). Consequently
\[
\operatorname{Cov}(X)=C.
\]
The eigenvalues \(\sigma_A,\sigma_B,\sigma_T\) are strictly positive on \((0,1)\), so \(C\) is nonsingular on \(H_0\).

**2. The strictly optimal mass.** The determinant on \(H_0\) is
\[
\det_{H_0}C=\frac{\kappa}{a^{a-1}[b(b-1)]^{b-1}}\,p^a(1-p)[2(b-2)+(3-b)p]^{b-1}.
\]
Its logarithm has strictly negative second derivative on \((0,1)\): the terms \(a\log p\) and \(\log(1-p)\) are strictly concave and \(\log\bigl(2(b-2)+(3-b)p\bigr)\) is concave with a positive affine argument. The determinant tends to zero at both endpoints. Therefore a unique interior maximizer exists, and differentiating its log gives precisely the defining equation. Multiplying out yields the stated rational cases and quadratic case.

**3. All vertices have equal ellipsoidal gauge.** Write
\[
Q(x)=(x-c)^{\mathsf T}C^+(x-c).
\]
Every cross vertex has the same \(Q\)-value, say \(L_X\), and every \(B\)-pair vertex has the same value, say \(L_Y\). Orthogonal projection onto the three summands gives the explicit expressions
\[
\begin{aligned}
L_X&=\frac{a-1}{a\sigma_A}+\frac{b-1}{b\sigma_B}+\frac{(1-p)^2\kappa}{\sigma_T},\\
L_Y&=\frac{2(b-2)}{b\sigma_B}+\frac{p^2\kappa}{\sigma_T}.
\end{aligned}
\]
Since \(C=\operatorname{Cov}(X)\), \(pL_X+(1-p)L_Y=\operatorname{tr}_{H_0}(C^{-1}C)=d\). To prove equality of the two gauges, differentiate \(\log\det C(p)\). The covariance derivative identity
\[
\frac{d}{dp}\log\det C(p)=L_X-L_Y
\]
follows by differentiating \(C(p)=\mathbb E_p[XX^{\mathsf T}]-c(p)c(p)^{\mathsf T}\), taking the trace against \(C(p)^{-1}\), and using \(\mathbb E_p(X-c(p))=0\) to cancel the mean-derivative terms. At the unique optimum the derivative vanishes, hence \(L_X=L_Y=d\). Every vertex lies on \(\partial\mathcal E_{a,b}\); convexity shows that the entire polytope lies inside \(\mathcal E_{a,b}\). Since the quadratic gauge is strictly convex on the affine hull, any nontrivial convex combination of distinct vertices has strictly smaller gauge than \(d\). Thus no nonvertex point of the polytope contacts the sphere.

**4. Global optimality, including nonsymmetric competitors.** Let any enclosing intrinsic ellipsoid have center \(m\in H\) and positive-definite squared-semiaxis matrix \(R\) on \(H_0\). The random vertex from Step 1 satisfies \((X-m)^{\mathsf T}R^{-1}(X-m)\le1\) almost surely. Averaging gives
\[
1\ge \operatorname{tr}_{H_0}(R^{-1}C)+(c-m)^{\mathsf T}R^{-1}(c-m).
\]
The arithmetic–geometric mean inequality for eigenvalues of \(R^{-1/2}CR^{-1/2}\) implies
\[
\left(\frac{\det C}{\det R}\right)^{1/d}\le\frac1d\operatorname{tr}(R^{-1}C)\le\frac1d.
\]
Therefore \(\det R\ge d^d\det C\), proving that no enclosing ellipsoid has less volume than \(\mathcal E_{a,b}\). Equality forces \(m=c\) and \(R=dC\). This establishes uniqueness among all positive-definite intrinsic ellipsoids. The eigenvalue multiplicities in the theorem then yield the asserted volume formula.

## Verification
Run the standalone Python 3 standard-library program `verify.py`, using `python3 verify.py` in the directory containing this file. It uses 70-digit decimal arithmetic and independently checks all closed scalar gauge identities and the polynomial parameter equation for every \(2\le a,b\le20\) (361 configurations). For every \(2\le a,b\le8\) (49 configurations), it independently constructs all vertices and their probability weights, recomputes the entire covariance matrix from first principles, and checks the full contact gauge of **each** vertex. A successful run prints `CLIPPED_RANK2_LOEWNER_PASS scalar=361 full_covariance_and_contacts=49`. These finite checks detect algebraic and implementation errors but are not the justification for the theorem for all \(a,b\); Steps 1–4 are the complete proof.

## Relationship to prior work
Ferroni and Schröter (arXiv:2310.05487, first posted 2023-10-09) give the one-split hypersimplex representation of Schubert elementary split matroid polytopes in their equation (1), and discuss complete-multipartite edge polytopes and face enumeration of rank-two matroids in Section 2.6. Their theorem concerns face counts, not minimum-volume enclosing ellipsoids. Ohsugi and Hibi study combinatorial and toric properties of complete-multipartite edge polytopes; the bibliographic abstract does not state the ellipsoid law, though the complete article was not material inspected.

The published exact inradius theorem for connected rank-two matroid base polytopes measures distances to facets and determines centers of inscribed **balls**, not minimum-volume outer ellipsoids. A published exact Gaussian angular spectrum theorem for the same rank-two matroid family determines probabilities of vertex exposure under random objectives; these are normal-cone measures and do not determine the optimally weighted vertex covariance or its Löwner contact geometry. A published Löwner theorem for second partial permutohedra concerns a different full-dimensional polytope with vertices at the origin and two distinct positive coordinate levels; it is not a specialization of the present one-split hypersimplex.

The general covariance-contact criterion used in Step 4 is classical and is not claimed to be new. The substantive geometric assertion is the exact optimal probability design, all-vertex contact, eigenvalue spectrum, and volume for the natural clipped matroid base-polytope family.

## Limitations
The result treats exactly one nontrivial parallel class of size at least two and at least two singleton classes. It does not assert a comparable formula for arbitrary multipartite rank-two matroids, higher rank, arbitrary affine images, or inballs. Historical priority has not been independently certified: a thematically related early complete-multipartite edge-polytope paper was available only through bibliographic description/abstract, and unindexed equivalent ellipsoid formulas cannot be excluded. The numerical tests are finite and do not independently certify the infinite theorem.

## References
1. L. Ferroni and B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, first posted 2023-10-09. https://arxiv.org/html/2310.05487v2
2. H. Ohsugi and T. Hibi, *Compressed polytopes, initial ideals and complete multipartite graphs*, Illinois Journal of Mathematics 44 (2000), 391–406. https://doi.org/10.1215/ijm/1255984847
3. *Exact Euclidean inradius of connected rank-two matroid base polytopes*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-euclidean-inradius-of-connected-rank-two-matroid-base-poly--04d0301093d4
4. *Gaussian angular spectra and a sharp balance law for rank-two matroid base polytopes*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-gaussian-angular-spectra-and-a-sharp-balance-law-for-rank-two-ma--1c76a22f265f
5. *A sharp Löwner contact-orbit transition for second partial permutohedra*, published research record (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-sharp-l-wner-contact-orbit-transition-for-second-partial-permu--dc2610ed29db
