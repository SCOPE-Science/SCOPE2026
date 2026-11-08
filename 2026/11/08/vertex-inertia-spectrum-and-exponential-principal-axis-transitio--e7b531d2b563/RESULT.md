# Vertex-inertia spectrum and exponential principal-axis transition of nonempty biclique bond polytopes

## Finding

For integers \(2\le p\le q\), let \(G=K_{p,q}\), and let \(B^+(G)\) be the convex hull of the indicators of all **nonempty** edge cuts whose two induced shores are connected. Choose \(X\in\{0,1\}^{p\times q}\) uniformly from the distinct vertices of \(B^+(G)\). These nonempty cuts are precisely the ordinary connected-shore bonds, and every such indicator is a distinct vertex of \(B^+(G)\). The exclusion of the zero cut is essential: some references define an augmented bond polytope by including zero as an extra vertex.

Set \(P=2^p\), \(Q=2^q\), and
\[
C=(P-2)(Q-2)+2(p+q),\qquad
\alpha=\frac{2(p+q-4)}{C},\quad
b_L=\frac{2(p+q-Q-2)}{C},\quad
b_R=\frac{2(p+q-P-2)}{C},\quad
g=\frac{2(p+q-6)}{C}.
\]
There are exactly \(C/2\) bonds, and every coordinate of \(X\) has expectation \((1-\alpha)/2\). The Euclidean covariance operator \(\Sigma=\operatorname{Cov}(\operatorname{vec}X)\) has the following **complete orthogonal eigenspace decomposition**, including possible coincidences of numerical eigenvalues:

| Eigenspace | Eigenvalue | Dimension |
| --- | --- | ---: |
| Constant matrices | \(\lambda_0=\bigl[1+(q-1)b_R+(p-1)b_L+(p-1)(q-1)g-pq\alpha^2\bigr]/4\) | \(1\) |
| Row contrasts \(u\mathbf1_q^T\), \(\sum_i u_i=0\) | \(\lambda_L=[PQ-2q(P-4)]/(4C)\) | \(p-1\) |
| Column contrasts \(\mathbf1_p v^T\), \(\sum_j v_j=0\) | \(\lambda_R=[PQ-2p(Q-4)]/(4C)\) | \(q-1\) |
| Row-and-column-zero matrices | \(\lambda_T=PQ/(4C)\) | \((p-1)(q-1)\) |

The exact ordering is \(\lambda_0<\lambda_L\le\lambda_T\) and \(0<\lambda_R\le\lambda_L\), where \(\lambda_T=\lambda_L\) exactly when \(p=2\), and \(\lambda_R=\lambda_L\) exactly when \(p=q\). The eigenvalue \(\lambda_0\) is positive unless \((p,q)=(2,2)\), in which case it is zero.

Define the integer threshold
\[
\boxed{\quad q_*(p)=\left\lfloor\frac{2^p-4}{p}-p+6\right\rfloor+1.\quad}
\]
Then, for **every** integer pair \(2\le p\le q\), there is a strict principal-axis transition:
\[
\boxed{\begin{array}{lll}
q<q_*(p)&\Longrightarrow&\lambda_0<\lambda_R\quad\text{(constant-edge mode is least)},\\
q\ge q_*(p)&\Longrightarrow&\lambda_R<\lambda_0\quad\text{(column-contrast mode is least)}.
\end{array}}
\]
There is no equality case, and \(q_*(p)\sim 2^p/p\) as \(p\to\infty\). For example, the first transitions occur at \(q_*(2)=5\), \(q_*(3)=5\), \(q_*(4)=6\), \(q_*(5)=7\), \(q_*(6)=11\), \(q_*(7)=17\), \(q_*(8)=30\). The transition is exponentially displaced from the balanced graph as the smaller shore grows.

## Assumptions and scope

The graph is finite, simple, undirected and exactly complete bipartite, with \(p,q\ge2\). The probability measure is uniform over **distinct nonempty bond-incidence vertices**, excluding the zero vector, not over all cuts, all points of the polytope, maximal cuts, or spanning trees. Covariance is computed in the standard edge-coordinate Euclidean inner product, without rescaling. The theorem makes no claim about other graphs or weighted edge metrics. For \((p,q)=(2,2)\), the nonempty-bond polytope is a 3-dimensional hypersimplex in its affine hull, explaining its single zero covariance eigenvalue.

## Proof

**1. Classifying and counting all bonds.** A nonempty vertex set in \(K_{p,q}\) induces a connected subgraph exactly when it is a singleton or contains a vertex in each color class. Consequently, if each vertex receives a sign \(\pm1\) to specify a shore, the two shores form a bond precisely in one of two disjoint cases: either the signs are nonconstant within **both** color classes; or precisely one graph vertex has sign opposite to all others. There are \((2^p-2)(2^q-2)\) assignments of the first kind and \(2(p+q)\) of the second. Complementary signs represent the same bond and no other assignments do. Thus the number of bonds is \(C/2\). A \(0/1\) point of a finite set of \(0/1\) points cannot be a nontrivial convex combination of the other points, so every listed indicator is a vertex.

**2. Exact pair moments.** Write the shore signs as \(s_i\) for the left color class and \(t_j\) for the right. The edge indicator is \(X_{ij}=(1-s_it_j)/2\). Under the uniform distribution on the \(C\) signed bond assignments, the mixed-sign assignments on each color class independently have zero one-spin expectation. For two distinct left indices the mean sign product among nonconstant left-sign strings is \(-2/(2^p-2)\); the analogous right value is \(-2/(2^q-2)\). In the singleton assignments, summing over the exceptional vertex gives \(2(p+q-4)\) for \(\sum s_it_j\), \(2(p+q-4)\) for each same-color pair sum before adding the mixed-sign contribution, and \(2(p+q-8)\) for the distinct-four-sign sum. The mixed-sign contribution to that four-sign sum is \(4\). It follows exactly that
\[
\mathbb E(s_it_j)=\alpha,\quad
\mathbb E(s_is_k)=b_L\ (i\ne k),\quad
\mathbb E(t_jt_l)=b_R\ (j\ne l),\quad
\mathbb E(s_is_kt_jt_l)=g\ (i\ne k,\ j\ne l).
\]
In particular, writing \(D\) for a diagonal covariance entry, \(U\) for entries sharing a left index, \(V\) for those sharing a right index, and \(W\) for disjoint edge indices, one has
\[
4(D,U,V,W)=(1-\alpha^2,\ b_R-\alpha^2,\ b_L-\alpha^2,\ g-\alpha^2).
\]
This completely fixes the covariance without any independence assumption between bond edges.

**3. Diagonalization.** The four mutually orthogonal spaces specified in the table partition \(\mathbb R^{p\times q}\). Evaluating the constant/row/column/interaction matrix actions gives, respectively,
\[
D+(q-1)U+(p-1)V+(p-1)(q-1)W,\quad
D+(q-1)U-V-(q-1)W,\quad
D-U+(p-1)V-(p-1)W,\quad
D-U-V+W.
\]
Inserting the exact moments yields the displayed eigenvalues and multiplicities. Since \((2^n-4)/n\) strictly increases over integers \(n\ge2\), their differences imply \(\lambda_T\ge\lambda_L\ge\lambda_R>0\). The difference \(\lambda_0-\lambda_L\) equals
\[
\frac{p}{2C^2}\left(\left[q(p+q-6)-2^q+4\right]C-2q(p+q-4)^2\right).
\]
It is negative because \(p\le q\) and \(2^q>2q(q-3)+4\) for every integer \(q\ge2\) (check \(q=2,3,4\) directly and double inductively for larger \(q\)). The constant-vector variance is \(\operatorname{Var}(\sum_{i,j}X_{ij})/(pq)\). All bonds of \(K_{2,2}\) have size \(2\), whereas every other permitted \(K_{p,q}\) has singleton bonds of sizes \(p,q\) and a bond from a mixed \((1,1)\)-shore of size \(p+q-2>p\). This proves the stated zero-eigenvalue exception.

**4. Exact phase boundary.** A direct subtraction gives
\[
\lambda_0-\lambda_R=\frac{q}{2C^2}
\left(\left[p(p+q-6)-2^p+4\right]C-2p(p+q-4)^2\right).
\]
Set \(r_p=(2^p-4)/p-p+6\). The first factor in brackets is \(p(q-r_p)\). The elementary inequality \(2^p-4\ge 2p(p-3)\) for \(p\ge2\) (directly for \(2\le p\le4\), then induction) gives \(r_p\ge p\). Hence when integer \(q\le r_p\), the displayed difference is strictly negative.

It remains to show strict positivity as soon as integer \(q>r_p\). In this range \(p(q-r_p)\) is a **positive integer**, hence at least \(1\). We establish the uniform bound
\[
C>2p(p+q-4)^2
\qquad(2\le p\le q,\ q\ge\lfloor r_p\rfloor+1).
\]
To prove it, note that for \(p\ge2\), \(q\ge3\),
\[
9C(p,q+1)-16C(p,q)
=2(2^p-2)(2^q+7)-14(p+q)+18>0.
\]
The last expression is increasing in each integer argument and is already positive at \((p,q)=(2,3)\). Whenever \(p+q-4\ge3\), the ratio of consecutive squares \((p+q-3)^2/(p+q-4)^2\) is at most \(16/9\). Therefore \(C/[2p(p+q-4)^2]\) increases strictly as \(q\) increases, starting at the relevant bases. These bases are \(C(2,5)=74>36\), \(C(3,4)=98>54\), and \(C(p,p)>2p(2p-4)^2\) for every \(p\ge4\). For the last bound, \(2^p-2\ge p(p-1)\) and \(p(p-1)^2\ge8(p-2)^2\) for integers \(p\ge4\), by elementary induction, suffice. Because \(\lfloor r_p\rfloor+1\ge p+1\), these bases cover the required entire domain. The positive integer factor times \(C\) therefore exceeds the negative term, proving the exact sharp threshold and the absence of ties. Finally \(\lfloor r_p\rfloor+1=2^p/p-p+O(1)\), yielding the stated asymptotics.

## Verification

A standalone Python 3 checker in `artifacts/verify.py` independently enumerates signed bond assignments up to eleven graph vertices, computes exact rational covariance entries, tests the four invariant eigenspaces, and checks the phase signs on additional large parameter pairs. It successfully reports:

`BICLIQUE_BOND_INERTIA_CHECKS_PASSED cases=19 vertices=5133 entries=6144 phases=102`

The enumerations cover **19** small parameter pairs, **5,133** distinct bond vertices in aggregate, and **6,144** covariance entries, plus **102** large-parameter sign checks; these finite calculations are corroborative, not a replacement for the proof for all integers.

## Relationship to prior work

Chimani, Juhnke-Kubitzke and Nover studied the bond polytope, its facet relations, graph modifications, and structural descriptions. Their 2020 preprint employs a convention that can include the zero incidence vector, whereas \(B^+(G)\) here uses only the nonempty connected-shore cuts. The present theorem concerns a different invariant: exact equal-vertex covariance and its smallest-eigenspace phase boundary. The connected-cut algorithmic literature likewise studies optimization rather than vertex inertia. Work on complete-bipartite spanning-tree, graphical-zonotope, stable-set, and other edge polytopes concerns different convex hulls: their vertex sets and probability measures do not imply the formulas here. We do not claim novelty of the definition of bonds, elementary two-shore counting, or the standard tensor decomposition; the contribution is their combined exact spectral classification and exponential transition.

## Limitations

Only the uniform distribution over nonempty bond vertices is treated. In particular, adjoining the zero vector to form an augmented bond polytope changes the sampling measure and requires different covariance formulas. The threshold involves the ambient edge-coordinate covariance and may differ under affine or weighted metric changes. The result does not determine the John ellipsoid, volume centroid, or Euclidean inradius, and does not extend to arbitrary graph classes. Historical priority is based on inspected accessible material and targeted searches, not an exhaustive global literature audit; an equivalent earlier second-moment calculation under connected-bipartition terminology remains a residual risk. Independent mathematical validation has not been performed.

## References

1. M. Chimani, M. Juhnke-Kubitzke and A. Nover, *On the Bond Polytope*, arXiv:2012.06288v1 (first public version 2020-12-11), https://arxiv.org/abs/2012.06288. Later published in *Advances in Geometry* (2023), DOI:10.1515/advgeom-2023-0014.
2. G. L. Duarte et al., *Computing the Largest Bond and the Maximum Connected Cut of a Graph*, arXiv:2007.04513 (2020), https://arxiv.org/abs/2007.04513.
3. R. Grappe and M. Lacroix, *The st-bond polytope on series-parallel graphs*, RAIRO Operations Research 52 (2018), 923–934, DOI:10.1051/ro/2018035 (a related but distinct rooted-bond construction).
4. P. Kolman and H. R. Tiwary, *Bond Polytope under Vertex- and Edge-sums*, arXiv:2601.11119 (2026), https://arxiv.org/abs/2601.11119 (later structural comparison; not the dated lead source).
