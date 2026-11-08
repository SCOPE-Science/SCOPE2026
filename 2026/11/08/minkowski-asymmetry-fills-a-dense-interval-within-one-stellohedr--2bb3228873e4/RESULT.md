# Minkowski asymmetry fills a dense interval within one stellohedral combinatorial type

## Finding
Let \(n\ge2\), let \(\mathbf b=(b_1,\ldots,b_n)\) be positive integers, and write \(S_j=\sum_{i=1}^j b_i\), \(B=S_n-1\), and \(T=\sum_{j=1}^n(S_j-1)\). For the full-dimensional generalized parking-function polytope \(K=\mathfrak X_n(\mathbf b)\), its **Minkowski asymmetry** and the **unique minimizing Minkowski center** are
\[
\boxed{\operatorname{asym}(K)=\frac{nB}{T},\qquad c_K=\frac{S_n+\operatorname{asym}(K)}{1+\operatorname{asym}(K)}\mathbf1.}
\]
For the classical parameters \(b_1=\cdots=b_n=1\), asymmetry is identically \(2\), in every dimension \(n\ge2\).

For each fixed \(n\ge2\), restrict to positive integer parameters with \(b_1\ge2\). All these polytopes have **the same stellohedron combinatorial type** (Bayer et al., Corollary 3.14), yet their Minkowski asymmetry values form a dense subset of \((1,n)\). The endpoints are not attained: specific families converge, after affine homotheties, to an \(n\)-cube and an \(n\)-simplex, respectively.

## Assumptions and scope
A \(\mathbf b\)-parking function is a vector of positive integers whose sorted coordinates \(\beta'_1\le\cdots\le\beta'_n\) obey \(\beta'_j\le S_j\) for every \(j\). Its polytope \(K\) is the convex hull of all such vectors in \(\mathbb R^n\), with the ordinary affine structure. For any full-dimensional convex body \(P\), define
\[
\operatorname{asym}(P)=\min_{c\in\operatorname{int}P}\inf\{\lambda\ge1:c-P\subseteq\lambda(P-c)\}.
\]
This is an affine-invariant coefficient, **not** the Euclidean inradius or a measure of graph-theoretic asymmetry. The statement concerns \(n\ge2\), all positive integral parameters, and uses no generic-position assumption. The dense-range and fixed-combinatorial-type assertions require \(b_1\ge2\); the exact formula does not. The degenerate case \(n=b_1=1\) is excluded.

## Proof
**1. Complete supporting inequalities.** The minimal inequality theorem of Bayer et al. (Theorem 2.3) describes \(K\) using \(x_i\ge1\) and, for every nonempty \(I\subseteq[n]\) with \(k=|I|\),
\[
\sum_{i\in I}x_i\le U_k,\qquad U_k=\sum_{j=n-k+1}^{n}S_j.
\]
When \(b_1=1\), the cardinality \(n-1\) inequalities are redundant but remain valid. Coordinate maxima are \(S_n\), attained at vertices with one coordinate \(S_n\); coordinate minima are \(1\). Every nonempty subset sum has minimum \(k\), attained by the all-one vertex. The maximum of the total coordinate sum is \(U_n=T+n\), attained at a permutation of \((S_1,\ldots,S_n)\). These extremal values follow directly from the published vertex/inequality description and are sharp.

**2. One-sided inclusion and a lower bound.** For an arbitrary \(\lambda\ge1\) and center \(c\), inclusion \(c-K\subseteq\lambda(K-c)\) is equivalent to the affine reflection
\[
F_{\lambda,c}(x)=\frac{\lambda+1}{\lambda}c-\frac{x}{\lambda}\in K\quad\text{for every }x\in K.
\]
Write \(y=(\lambda+1)c\). Applying the sharp coordinate maxima to the lower inequalities of \(K\) forces
\[y_i\ge S_n+\lambda\quad(1\le i\le n).\]
Applying the sharp subset minima to the upper inequalities forces
\[\sum_{i\in I}y_i\le\lambda U_k+k\qquad(I\ne\varnothing).\]
In particular, summing the coordinate inequalities and comparing with the full-set upper inequality yields
\[
n(S_n+\lambda)\le\sum_i y_i\le\lambda U_n+n=\lambda(T+n)+n,
\]
which simplifies to \(\lambda T\ge nB\). Therefore \(\operatorname{asym}(K)\ge nB/T\).

**3. An exact realizing center.** Let \(s=nB/T\ge1\), set \(y_i=S_n+s\), and define \(c_i=y_i/(1+s)\). All lower conditions are equalities. The subset condition becomes
\[
k(S_n+s)\le sU_k+k\quad\Longleftrightarrow\quad\frac1k\sum_{j=n-k+1}^n(S_j-1)\ge\frac Tn.
\]
The last inequality says the average of the largest \(k\) terms of the strictly increasing sequence \(S_j-1\) is at least its overall average. It holds for every \(1\le k\le n\), strictly for \(k<n\). Thus all reflected points remain in \(K\); the candidate realizes \(s\). Since \(S_n>1\) and \(s>0\), every \(c_i>1\); the strict proper-subset conditions and the full-set slack for \(c\) show \(c\in\operatorname{int}K\).

**4. Uniqueness.** At the optimal \(\lambda=s\), the upper and lower bounds for \(\sum_i y_i\) in step 2 coincide. Hence each of the \(n\) coordinate lower bounds must be an equality, forcing \(y_i=S_n+s\). The minimizing center is unique and is exactly the claimed \(c_K\).

**5. A fixed face lattice with dense affine asymmetry spectrum.** If \(b_1\ge2\), strict increase of \(S_j\) gives \(B<T<nB\); hence \(1<s<n\). The cited Corollary 3.14 makes every such \(K\) combinatorially equivalent to the \(n\)-dimensional stellohedron. For any target \(v\in(1,n)\), set \(r=n(v-1)/(n-v)>0\), and for increasing integers \(h\) choose
\[
\mathbf b(h)=(h+1,\underbrace{1,\ldots,1}_{n-2\text{ entries}},\lfloor rh\rfloor+1).
\]
Then \(B/h\to1+r\) and \(T/h\to n+r\), giving \(s(\mathbf b(h))\to n(1+r)/(n+r)=v\). Consequently asymmetry values in this single combinatorial type are dense in the entire interval \((1,n)\).

The families \(\mathbf b^{\mathrm{cube}}(h)=(h,1,\ldots,1)\) and \(\mathbf b^{\mathrm{simplex}}(h)=(2,1,\ldots,1,h)\) stay in that same combinatorial type. Bayer et al.'s vertex description says all vertices are permutations of \((1,\ldots,1,S_{k+1},\ldots,S_n)\) for \(0\le k\le n\). Therefore, translating by \(-\mathbf1\) and dividing by \(h-1\) makes the cube family's vertices converge collectively to all \(\{0,1\}^n\). Translating by \(-\mathbf1\) and dividing by \(S_n-1\) makes the simplex family's vertices converge collectively to \(\{0,e_1,\ldots,e_n\}\). The convex hulls consequently converge in the Hausdorff metric to \([0,1]^n\) and \(\operatorname{conv}(0,e_1,\ldots,e_n)\), respectively. Their asymmetry coefficients tend to \(1\) and \(n\), in agreement with the exact formula. Neither endpoint occurs at finite integral parameters with \(b_1\ge2\). \(\square\)

## Verification
A standalone reproducibility script `checker/check_minkowski.py` verifies the exact halfspace reflection constraints and independently solves the corresponding linear program for 360 positive-integer vectors in dimensions \(2\) to \(5\), plus seven classical cases (dimensions \(2\) to \(8\)) and 30 endpoint-family checks. It uses Python 3, exact rational arithmetic, and SciPy's HiGHS linear optimizer. To replay from this package run `python checker/check_minkowski.py` with SciPy installed. The finite checks are not the proof of the claims for all dimensions; steps 1–5 are.

## Relationship to prior work
Hanada, Lentfer, and Vindas-Meléndez (arXiv:2212.06885, first public 2022-12-13) developed the classical and two-parameter parking-function polytope framework, especially face structure and volumes. Bayer et al. (arXiv:2403.07387, first public 2024-03-12) proved the arbitrary-parameter facet/vertex description and stellohedron combinatorial equivalence used here. Those theorems are premises and **not** claimed as new. Beck and Schymura (arXiv:2301.12182) formulate the coefficient of asymmetry in a different setting (lattice zonotopes); the invariant itself is classical. The present claim concerns the complete arbitrary-parameter asymmetry **value and unique optimizing center**, together with the dense interval of values inside a fixed face lattice. Other exact asymmetry results for a simplex-sum stellohedron realization concern a different coordinate realization: combinatorial equivalence alone cannot fix an affine invariant.

## Limitations
Historical priority is provisional: a formula equivalent under submodular-polymatroid or stellohedron terminology may exist outside the materially inspected sources. The similarity-based public-record search does not prove absence. This result does not classify all affine equivalence classes, all values attained exactly by integer vectors, or any Euclidean inradius or ellipsoid.

## References
1. M. Hanada, J. Lentfer, and A. R. Vindas-Meléndez, *Generalized parking function polytopes*, arXiv:2212.06885 (first version 2022-12-13), https://arxiv.org/abs/2212.06885.
2. M. M. Bayer et al., *Combinatorics of generalized parking-function polytopes*, arXiv:2403.07387 (first version 2024-03-12), especially Theorem 2.3 and Corollary 3.14, https://arxiv.org/abs/2403.07387.
3. M. Beck and M. Schymura, *Deep lattice points in zonotopes, lonely runners, and lonely rabbits*, arXiv:2301.12182 (first version 2023-01-28), https://arxiv.org/abs/2301.12182.
