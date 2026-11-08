# Cut-controlled Euclidean inballs and factorized centers of complete directed flow polytopes

## Finding

Let \(n\geq3\). Direct every edge of the complete graph on \([n]\) from the lower to the higher index, equip its \(m=\binom n2\) edge-flow space with the standard Euclidean norm, and let \(B\) be its vertex-by-edge incidence matrix, with column \(e_i-e_j\) at edge \((i,j)\). Let \(b\in\mathbb R^n\) satisfy \(\sum_{i=1}^n b_i=0\), and put \(\beta_k=\sum_{i=1}^k b_i\). Suppose \(\beta_k>0\) for every \(1\leq k<n\). Define
\[
P_n(b)=\{x\in\mathbb R^m:x\geq0,\ Bx=b\},\qquad
\tau=\min_{1\leq k<n}\frac{\beta_k}{k(n-k)}.
\]
Then \(P_n(b)\) has affine dimension \(\binom{n-1}{2}\) and exact **intrinsic** Euclidean inradius
\[
\boxed{r(P_n(b))=\sqrt{\frac n{n-2}}\,\tau.}
\]
Its **entire** set of centers of maximum-radius balls is
\[
\boxed{\mathcal I_n(b)=\{x\in P_n(b):x_{ij}\geq\tau\text{ for all }i<j\}.}
\]
Let \(C=\{k\in[n-1]:\beta_k=k(n-k)\tau\}\), write \(0=c_0<c_1<\cdots<c_s=n\) for the increasing union \(\{0\}\cup C\cup\{n\}\), and write \(d_j=c_j-c_{j-1}\). After subtracting the constant flow \(\tau\mathbf1\), every edge crossing any cut indexed by \(C\) is forced to zero. The remaining nonnegative flows form an affine Cartesian product of independent complete-DAG flow polytopes on the consecutive blocks \([c_{j-1}+1,c_j]\), each full-dimensional in its natural flow affine space. Thus
\[
\boxed{\dim\mathcal I_n(b)=\sum_{j=1}^{s}\frac{(d_j-1)(d_j-2)}2.}
\]

In particular, take \(b=(1,0,\ldots,0,-1)\), the unit-source/unit-sink flow realization of the Chan–Robbins–Yuen polytope. Then
\[
\boxed{r(P_n(b))=\frac{\sqrt{n/(n-2)}}{\lfloor n^2/4\rfloor},\qquad
\dim\mathcal I_n(b)=(\lfloor n/2\rfloor-1)(\lfloor n/2\rfloor-2).}
\]
There is a unique incenter for \(3\leq n\leq5\), whereas the incenter set is positive-dimensional for every \(n\geq6\). Moreover \(n^2r(P_n(b))\to4\), and the ratio of incenter-locus dimension to polytope dimension tends to \(1/2\).

## Assumptions and scope

All distances, balls, and dimensions refer to the Euclidean metric induced by the **edge-coordinate embedding** \(P_n(b)\subset\mathbb R^{\binom n2}\), restricted to its affine hull \(\{x:Bx=b\}\). The classical Chan–Robbins–Yuen realization as a face of a Birkhoff polytope is only integrally equivalent to this realization and need not preserve this Euclidean metric. The theorem makes no metric claim about that alternative realization.

The strict prefix conditions \(\beta_k>0\) guarantee the existence of a flow strictly positive on every edge and are essential for the asserted affine dimension and common projected-normal norm. Real, possibly negative, individual internal netflows \(b_i\) are allowed. No formula is asserted for the lower-dimensional boundary cases where one or more prefix sums vanish. For the complete graph with only two vertices, the flow polytope is a point and intrinsic ball radius is not considered here.

## Proof

**1. Nonempty full-dimensional flow space.** Put \(q_k=k(n-k)\). For each proper prefix \([k]\), cancellation of internal directed edges in the conservation equation gives the exact cut identity
\[
\sum_{1\leq i\leq k<j\leq n}x_{ij}=\beta_k.
\]
In particular the adjacent-edge flow \(x_{k,k+1}=\beta_k\), with other edge entries zero, is feasible. For sufficiently small \(\varepsilon>0\), assign \(\varepsilon\) to every edge and add \(\beta_k-\varepsilon q_k>0\) to adjacent edge \((k,k+1)\). This gives a strictly positive feasible flow. Since the incidence matrix of a connected graph has rank \(n-1\), the full affine hull is \(Bx=b\), of dimension \(\binom n2-(n-1)=\binom{n-1}{2}\).

**2. A common intrinsic Euclidean coordinate-normal length.** The tangent space is \(T=\ker B\). For edge \((i,j)\), let \(u_{ij}\) be its coordinate unit vector in \(\mathbb R^m\). The graph Laplacian of the complete graph is \(BB^{\mathsf T}=nI-J\), with pseudoinverse \((BB^{\mathsf T})^+=\tfrac1n(I-J/n)\). Orthogonal projection \(\Pi_T\) therefore satisfies
\[
\begin{aligned}
\|\Pi_Tu_{ij}\|^2
&=1-(e_i-e_j)^{\mathsf T}(BB^{\mathsf T})^+(e_i-e_j)\\
&=1-\frac2n=\frac{n-2}{n}.
\end{aligned}
\]
This also proves that no coordinate inequality is constant along the affine hull when \(n\geq3\).

For any center \(x\in P_n(b)\), the intrinsic closed ball of radius \(\rho\) centered at \(x\) lies in \(P_n(b)\) if and only if every edge coordinate remains nonnegative throughout the ball. Minimizing the linear coordinate functional over that ball shows this is equivalent to
\[
 x_{ij}\geq\rho\sqrt{(n-2)/n}\qquad\text{for every edge }(i,j).
\]
Hence its maximum admissible radius is exactly \(\sqrt{n/(n-2)}\min_{i<j}x_{ij}\).

**3. Sharp cut obstruction and attainment.** If \(x_{ij}\geq t\) for all edges, the cut identity gives \(\beta_k\geq q_kt\) for each \(k\), whence \(t\leq\tau\). Conversely set
\[
 x_{ij}=\tau+\mathbf1_{\{j=i+1\}}(\beta_i-q_i\tau).
\]
All the added adjacent-edge values are nonnegative by definition of \(\tau\). Across cut \([k]\) the constant part contributes \(q_k\tau\) and the sole additional crossing adjacent-edge value contributes \(\beta_k-q_k\tau\), so all cut sums equal \(\beta_k\); consecutive differences then give \(Bx=b\). Thus \(\min x_{ij}=\tau\), achieving the bound in Step 2. Step 2 also gives precisely the claimed inequalities describing **every** maximum-ball center.

**4. Product structure and dimension of the incenter locus.** Write \(y=x-\tau\mathbf1\) and \(b'=b-\tau B\mathbf1\). Then \(y\geq0\) and \(By=b'\). Its prefix netflows are
\[
\beta'_k=\beta_k-\tau k(n-k)\geq0,
\]
vanishing exactly at the critical cuts \(k\in C\). On any such cut, the sum of its nonnegative crossing values \(y_{ij}\) equals zero, so every crossing value is zero. The surviving edges are exactly those internal to consecutive blocks \([c_{j-1}+1,c_j]\), and conservation equations separate blockwise, proving the Cartesian product claim.

Each block has total netflow zero because its two boundary prefix values \(\beta'\) vanish. Every internal proper prefix cut has *strictly* positive residual value since otherwise its position would also belong to \(C\). The same all-edges-\(\varepsilon\) construction as in Step 1 therefore supplies a flow strictly positive on every internal edge of each block. The incidence rank of a complete directed block of size \(d\) is \(d-1\); its full-dimensional flow-space dimension is \(\binom d2-d+1=(d-1)(d-2)/2\). Summing the independent block dimensions proves the asserted center-locus formula, including singleton blocks, which contribute zero.

**5. Unit-source/unit-sink specialization.** Here every \(\beta_k=1\), so \(\tau=1/\max_{1\leq k<n}k(n-k)=1/\lfloor n^2/4\rfloor\). If \(n=2h\), the unique maximizing cut is \(h\), leaving two blocks of size \(h\). If \(n=2h+1\), the two maximizing cuts are \(h,h+1\), leaving blocks of sizes \(h,1,h\). In either case Step 4 gives \((h-1)(h-2)\) dimensions. The uniqueness threshold, positive-dimensionality, and asymptotic statements follow directly. \(\square\)

## Verification

The accompanying standalone script `check_flow_inball.py` independently computes orthogonal projections of coordinate normals from numerical singular-value decompositions, optimizes the maximal common edge-flow lower bound via an LP solver, checks exact rational construction certificates and critical cuts, and calculates the ranks of free-edge incidence submatrices. It covers \(3\leq n\leq11\) with seven choices of prefix data per size (63 LP instances) and separately checks all unit-source/unit-sink parity formulas through \(n=17\). Its verified completion marker is `COMPLETE_FLOW_INBALL_CUT_AND_LOCUS_CHECKS_PASSED 63`.

These finite tests corroborate, but do not logically replace, the all-parameter cut, projection, and rank proofs above. Execute with `python check_flow_inball.py`; Python 3, NumPy, and SciPy are required.

## Relationship to prior work

Corteel, Kim, and Mészáros (arXiv:1612.00102, publicly available December 1, 2016) treat the complete-graph flow realization of Chan–Robbins–Yuen and normalized volume formulas. Mészáros, Morales, and Rhoades (arXiv:1409.8566) identify the coordinate-permutation equivalence to Tesler polytopes and study face structure and volume. Lee and Liu (arXiv:2212.11423) classify deformation cones and the relationship between Tesler and more general flow polytopes. Dugan (arXiv:2409.15519; later published in 2025) gives enumerative formulas for face vectors. Those inspected statements concern different invariants and do not provide the intrinsic Euclidean inradius formula or optimal-center product/dimension description here.

The feasibility of flow lower bounds, basic linear programming, and complete-graph effective resistance are classical ingredients; they are not claimed new. The stated contribution is their exact combined geometric consequence for the complete-DAG flow family, particularly the complete incenter stratification and its middle-cut factorization for the unit-source/unit-sink family. The metric is explicitly distinguished from a merely affinely equivalent polytope. A search for equivalent formulations under Chebyshev-center, network max-min fairness, flow inball, and Tesler terminology found no covering theorem, but mathematical priority cannot be certified from the searched sources alone.

## Limitations

The result does not apply directly to arbitrary directed graphs, alternative inner products, vanishing-prefix boundary cases, or the Birkhoff-face metric. The theorem does not classify ellipsoids, higher intrinsic volumes, or the face numbers of its incenter polytope. Generic network max-min fairness and related optimization literature might contain an equivalent formulation of parts of the radius computation; this remains an originality risk. No independent mathematical audit has been performed.

## References

1. S. Corteel, J. S. Kim, and K. Mészáros, *Flow polytopes with Catalan volumes*, arXiv:1612.00102 (first public version 2016-12-01), https://arxiv.org/abs/1612.00102.
2. Y. Lee and F. Liu, *Deformation cones of Tesler polytopes*, arXiv:2212.11423 (first public version 2022-12-22), https://arxiv.org/abs/2212.11423.
3. W. T. Dugan, *On the f-vectors of flow polytopes for the complete graph*, arXiv:2409.15519 (first public version 2024-09-23), https://arxiv.org/abs/2409.15519.
4. K. Mészáros, A. H. Morales, and B. Rhoades, *The polytope of Tesler matrices*, arXiv:1409.8566 (2014), https://arxiv.org/abs/1409.8566 (supporting earlier literature).
