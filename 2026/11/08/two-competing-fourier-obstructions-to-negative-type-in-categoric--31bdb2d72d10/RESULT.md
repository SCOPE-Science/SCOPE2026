# Two competing Fourier obstructions to negative type in categorical Hamming double covers

## Finding

Let \(q\ge 3\) and \(d\ge 2\) be integers. Let \(X\) be the vertex set of the graph-theoretic categorical product \(K_2\times K_q^{\times d}\): two vertices are adjacent when they differ in **every** coordinate. Equip \(X\) with its ordinary shortest-path distance \(\rho\). Write
\[
N=q^d,\qquad Q=(q-1)^d,\qquad M=(q-1)^{d-1},
\]
and for \(p\ge0\) define
\[
F_{q,d}(p)=(N-1)2^p-Q-(N-Q)3^p.
\]
Here \(p\)-negative type means \(\sum_{x,y\in X}a_xa_y\rho(x,y)^p\le0\) for every real vector \(a\) satisfying \(\sum_xa_x=0\); at \(p=0\), nonzero distances have zeroth power one and the diagonal is zero.

**Exact spectral and threshold theorem.** The metric has \(p\)-negative type if and only if
\[
M(3^p-1)\le2^p\qquad\text{and}\qquad F_{q,d}(p)\le0.
\]
Let \(b_1\) be the unique positive solution of \(M(3^{b_1}-1)=2^{b_1}\). Let \(b_0\) be the smallest positive zero of \(F_{q,d}\), with \(b_0=+\infty\) if no such zero exists. The supremal negative-type exponent is exactly
\[
\boxed{\beta_{q,d}=\min\{b_0,b_1\}.}
\]
For \(0\le p<\beta_{q,d}\), negative type is strict. At the endpoint, the centered nullspace has dimension \(1\) when \(b_0<b_1\), dimension \(d(q-1)\) when \(b_1<b_0\), and dimension \(1+d(q-1)\) when equality holds. These are respectively the bipartition sign character, the first-order product characters with trivial \(K_2\) factor, or both. Therefore the minimal Euclidean dimension for embedding the snowflaked distance \(\rho^{\beta_{q,d}/2}\) is \(2N-1\) minus that nullspace dimension; for exponents below \(\beta_{q,d}\), it is \(2N-1\).

**Asymptotic phase transition.** Let \(d\to\infty\) and let integers \(q=q_d\ge3\) satisfy \(q_d/d\to\alpha\in(0,\infty)\). Define
\[
\theta=1-\frac{\log 2}{\log3},\qquad
\alpha_c=\frac1{\log(1/\theta)}=1.0032421945\ldots,
\qquad C_\alpha=1-\theta e^{1/\alpha}.
\]
If \(0<\alpha<\alpha_c\), then the first-order Fourier mode is critical for all sufficiently large \(d\), and
\[
\beta_{q_d,d}\sim\frac{1}{M\log3}.
\]
If \(\alpha>\alpha_c\), then the bipartition character is critical for all sufficiently large \(d\), and
\[
\beta_{q_d,d}\sim\frac{1}{(q_d-1)M(\log3)C_\alpha}.
\]
The exact critical regime \(\alpha=\alpha_c\) is not classified by this asymptotic statement.

## Assumptions and scope

The alphabets are arbitrary sets of \(q\) symbols; no field structure or primality is required. For Fourier analysis, independently label each coordinate by the cyclic group \(\mathbb Z/q\mathbb Z\), and the first coordinate by \(\mathbb Z/2\mathbb Z\). Since adjacency is inequivalence in every coordinate, it is precisely the stated graph regardless of labeling. The claim covers all integer \(q\ge3\), \(d\ge2\) and all real \(p\ge0\). Powers of the distance are interpreted on the off-diagonal as usual. This is a classification for the unweighted path metric, not for arbitrary edge weights or unequal alphabets.

## Proof

**1. The distance kernel.** Label a vertex by \((b,x)\in\mathbb Z_2\times(\mathbb Z_q)^d\). The graph is connected and has diameter three. From the origin, the distance is zero at the origin; it is \(2\) at \((0,x)\ne(0,0)\); it is \(1\) at \((1,x)\) when every coordinate of \(x\) is nonzero; and it is \(3\) at all other \((1,x)\). Indeed, a two-step route between any two vertices of equal first-coordinate parity exists because \(q\ge3\) supplies an intermediate symbol different from both endpoints in each coordinate. With different first-coordinate parity, either the endpoints are adjacent or a three-step route exists independently in every factor (also when \(q=3\)).

**2. Every Fourier multiplier.** Every character is indexed by a sign \(\varepsilon\in\{+1,-1\}\) on the binary coordinate and a character on \((\mathbb Z_q)^d\) nontrivial in exactly \(j\) coordinates. The character sum over the completely nonzero \(d\)-tuple set equals
\[
P_j=(-1)^j(q-1)^{d-j}.
\]
Summing the distance powers in the four cases above, the eigenvalues of the full \(p\)-distance matrix are
\[
\lambda_{\varepsilon,0}(p)=(N-1)2^p+\varepsilon\bigl(Q+(N-Q)3^p\bigr),
\]
\[
\lambda_{\varepsilon,j}(p)=-2^p+\varepsilon(1-3^p)(-1)^j(q-1)^{d-j},\quad 1\le j\le d,
\]
with multiplicity \(\binom dj(q-1)^j\) in each \(\varepsilon\)-sector. The \((+,0)\) eigenvector is constant and has a positive eigenvalue. Every other character is perpendicular to constants.

For \(j\ge1\), the largest eigenvalue at fixed \(j\), varying the binary sign, is \(-2^p+(3^p-1)(q-1)^{d-j}\). For \(p>0\), the largest among these occurs precisely at \(j=1\), with sign \(\varepsilon=+1\), and has multiplicity \(d(q-1)\). The only remaining nonconstant eigenvalue is \(\lambda_{-,0}=F_{q,d}\), of multiplicity one. Conditional negative semidefiniteness is therefore equivalent to the two stated inequalities; it is strict when both are strict. Since \((3^p-1)/2^p=(3/2)^p-(1/2)^p\) increases strictly from zero to infinity, the first inequality has one unique positive boundary \(b_1\). Also \(F_{q,d}(0)=-1\), and \(F'_{q,d}(p)=(N-1)\log2\,2^p-(N-Q)\log3\,3^p\); this derivative changes sign at most once, from positive to negative. Thus the earliest zero of \(F\), if any, is the first obstruction of that sector. Continuity of the eigenvalues (and the interval property for negative type) establishes the stated \(\beta_{q,d}\).

At the endpoint the only possible zero eigenvalues are in the identified sectors, with their exact multiplicities. The centered squared-distance Gram matrix is \(-\frac12 H D_p H\), with \(H\) the projection off constants. Its rank equals the minimal Euclidean embedding dimension, establishing the final finite-size assertion.

**3. Phase boundary.** Let \(q/d\to\alpha>0\). Set \(r=\log2/\log3\) and \(E_d=(q/(q-1))^d\); then \(E_d\to e^{1/\alpha}\). Since \(M\to\infty\), the unique first-sector root satisfies \(b_1\sim1/(M\log3)\). The derivative at zero obeys the **exact** relation
\[
\frac{F'_{q,d}(0)}{(q-1)M\log3}
=rE_d\bigl(1-N^{-1}\bigr)-(E_d-1),
\]
which tends to \(C_\alpha\). Uniformly for \(0\le p\le b_1\), Taylor's theorem gives
\[
F_{q,d}(p)=-1+pF'_{q,d}(0)+O(Nb_1^2),
\]
and \(Nb_1^2\to0\) because \(q\) is asymptotically proportional to \(d\). If \(C_\alpha<0\), then \(F'(0)<0\) eventually; the displayed derivative shows \(F'(p)<0\) at every positive \(p\). Hence \(b_1\) is the first obstruction. If \(C_\alpha>0\), then \(F'(0)\sim(q-1)M(\log3)C_\alpha>0\), \(F(b_1)>0\) eventually, and the unique first root \(b_0\in(0,b_1)\) obeys \(b_0\sim1/F'(0)\). This yields both regimes and the explicit critical ratio.

## Verification

The independent finite-graph checker in `check.py` constructs the actual categorical-product graph, computes shortest-path distances by breadth-first search, and independently evaluates all group characters against the claimed eigenvalues. It covers \((q,d)=(3,1),(4,1),(5,1),(3,2),(4,2),(5,2),(3,3)\) at four powered-distance exponents each (28 complete cases); the one-dimensional products serve as auxiliary boundary tests, outside the main theorem. Additional checks locate and classify endpoint spectral zeros for \((3,2),(4,2),(5,2),(4,3),(5,3)\). They confirm a switch from a degree-one mode (e.g. \((q,d)=(4,2)\), threshold \(0.31593122265\ldots\), nullity six) to a bipartition mode (\((5,2)\), threshold \(0.14745001406\ldots\), nullity one). Numerical checking does not prove an infinite-family theorem; the argument above does.

## Relationship to prior work

Sánchez (2011) gives a general distance-matrix criterion for the supremal negative type of a finite metric space and explicitly solves complete bipartite graph metrics. Murugan (2011) develops a determinant and equality-space criterion for vertex-transitive graph metrics. Their principles apply here, but their inspected statements do not compute the present three-distance categorical-product Fourier spectrum, identify its two competing null sectors, or obtain the alphabet-to-dimension asymptotic transition. The graph-theoretic categorical product itself and character diagonalization are standard; neither is claimed as novel. The contribution is the joint exact classification and its asymptotic phase boundary.

## Limitations

Historical priority is not established conclusively: some graph-spectrum or distance-regularity treatments may implicitly contain special cases (notably the single-factor crown graph), and an uncatalogued general theorem could cover the complete classification. The asymptotic classification excludes the critical ratio \(q/d\to\alpha_c\), where subleading terms matter. The result does not treat heterogeneous alphabets, multiple binary factors, weighted edges, or graph metrics of greater diameter.

## References

1. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first posted 2011-08-02. In particular, Section 2 and Theorem 3.1.
2. Mathav Kishore Murugan, *Generalized roundness of vertex transitive graphs*, arXiv:1112.5657, first posted 2011-12-23. In particular, Theorem 3.1.
3. Standard categorical-product definition and adjacency tensor factorization; see the established graph-product literature. No claim of priority over these definitions is made.
