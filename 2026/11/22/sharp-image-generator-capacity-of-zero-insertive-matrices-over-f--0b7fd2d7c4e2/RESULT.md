# Sharp image-generator capacity of zero-insertive matrices over finite chain rings

## Finding
Let \(R\) be any nonzero finite commutative chain ring with maximal ideal \(\pi R\), where \(\pi^k=0\) and \(\pi^{k-1}\ne0\), \(k\ge1\). For \(n\ge1\) define the zero-insertive locus
\[
\mathcal Z_n(R)=\{ATB:A,B,T\in M_n(R),\ AB=0\}.
\]
For a matrix \(X\), let \(\mu(X)\) be the minimum number of \(R\)-module generators of \(\operatorname{im}(X:R^n\to R^n)\), with \(\mu(0)=0\).

More precisely, fix \(A\in M_n(R)\) and put
\[
\kappa(A)=\max_{\substack{B,T\in M_n(R)\\AB=0}}\mu(ATB).
\]
Write the Smith diagonal of \(A\) as \(\operatorname{diag}(\pi^{a_1},\dots,\pi^{a_n})\), where \(0\le a_i\le k\) and \(\pi^k=0\). Let \(n_h=|\{i:a_i=h\}|\) for \(0\le h\le k\). Then
\[
\boxed{\kappa(A)=n-\max_{0\le h\le k}n_h.}
\]
Every integer between \(0\) and \(\kappa(A)\) is attained by some pair \((B,T)\) with \(AB=0\). In particular,
\[
\boxed{\max_{X\in\mathcal Z_n(R)}\mu(X)=n-\left\lceil\frac{n}{k+1}\right\rceil.}
\]
For \(n\ge2\), a zero-insertive matrix whose image needs \(n-1\) generators exists exactly when \(k\ge n-1\). The capacity depends only on matrix size and radical length, not on the residue-field order or characteristic.

## Assumptions and scope
All rings are finite, commutative, unital chain rings. Their ideals are exactly \(R,\pi R,\ldots,\pi^kR=0\); a field is the case \(k=1\). Matrix equivalence and Smith diagonals exist over these principal ideal rings. No assumption that \(R\) has equal characteristic or is a truncated polynomial ring is made. The invariant \(\mu(X)\) is the minimal number of generators of the *image module*, not the rank of reduction modulo \(\pi\) or the maximum size of a nonzero minor. In a chain ring these ranks are different.

## Proof
**1. Reduction to Smith levels.** Write \(A=P D_a Q\) with \(P,Q\) invertible and \(D_a=\operatorname{diag}(\pi^{a_i})\). The relation \(AB=0\) is equivalent to \(D_a QB=0\). Since \(\operatorname{Ann}(\pi^{a_i})=\pi^{k-a_i}R\) (also valid for \(a_i=0,k\)), there exists \(H\in M_n(R)\) with \(QB=D_{k-a}H\), where \(D_{k-a}=\operatorname{diag}(\pi^{k-a_i})\). For any middle matrix \(T\), after writing \(S=QTQ^{-1}\),
\[
ATB=P\,YH,\qquad Y=D_a S D_{k-a}.
\]
Consequently
\[
Y_{ij}=\pi^{k+a_i-a_j}S_{ij},
\]
and \(Y_{ij}=0\) whenever \(a_i\ge a_j\). Multiplication by \(P\) does not alter the minimal number of image generators.

**2. Upper bound.** Form a bipartite support graph with a row vertex \(i\), a column vertex \(j\), and an edge only when \(a_i<a_j\). Fix any level \(h\). Every edge meets either a row with \(a_i<h\) or a column with \(a_j>h\). These form a vertex cover of size \((\sum_{u<h}n_u)+(\sum_{u>h}n_u)=n-n_h\). Partition the nonzero entries of \(Y\) into a matrix \(Y_{\mathrm{row}}\) supported on the covered rows and a matrix \(Y_{\mathrm{col}}\) supported on the covered columns. The image of \(Y_{\mathrm{row}}H\) is a submodule of a free module of rank \(\sum_{u<h}n_u\); over a principal ideal ring such a submodule has at most that many generators (Smith normal form). The matrix \(Y_{\mathrm{col}}H\) is a sum of at most \(\sum_{u>h}n_u\) column-vector/row-vector products, so its image needs at most that many generators. Since the image of their sum is contained in the sum of their images, again using the generator bound for submodules over a principal ideal ring, we obtain \(\mu(YH)\le n-n_h\). Choosing \(h\) with largest \(n_h\) gives \(\mu(ATB)\le n-\max_h n_h\).

**3. Sharpness at fixed \(A\).** Let \(m=\max_h n_h\). The support graph has a matching of size \(n-m\). Indeed, for any nonempty set \(S\) of row vertices, let \(h\) be its smallest Smith level. Its neighbor set consists of *all* columns of levels strictly greater than \(h\). Thus \(|S|-|N(S)|\le n_h\le m\). Taking \(S\) to be all rows of levels \(\ge h\) for a level with \(n_h=m\) gives equality. The deficiency form of Hall's matching theorem therefore yields matching number \(n-m\).

Take \(H=I\), \(B=Q^{-1}D_{k-a}\), and let \(S\) have entry \(1\) precisely at the matched positions and zero elsewhere, setting \(T=Q^{-1}SQ\). Then \(AB=0\), and \(Y\) has exactly \(n-m\) nonzero entries in pairwise distinct rows and columns. Each is \(\pi^{k+a_i-a_j}\ne0\). Its image is a direct sum of \(n-m\) nonzero principal ideals supported on distinct coordinate axes. By the local-module generator theorem (or Smith normal form), its minimal number of generators is exactly \(n-m\). Deleting any number of matching edges realizes every smaller nonnegative number.

**4. Global optimum and threshold.** Since the \(k+1\) Smith-level multiplicities sum to \(n\), their maximum is at least \(\lceil n/(k+1)\rceil\). Conversely, choosing a diagonal matrix whose levels are as balanced as possible makes the largest multiplicity exactly that ceiling. Applying the fixed-\(A\) formula proves the global result. For \(n\ge2\), the bound equals \(n-1\) precisely when \(\lceil n/(k+1)\rceil=1\), i.e. \(k+1\ge n\), or \(k\ge n-1\).

## Verification
A standalone executable \(verify.py\) uses independent bit-polynomial arithmetic in \(\mathbb F_2[t]/(t^k)\). It computes the number of image-module generators from the \(\mathbb F_2\)-dimensions of \(\operatorname{im}X\) and \(t\operatorname{im}X\), rather than implementing the proof's Smith matching reduction. It exhausts 393,216 zero-product sandwich products at matrix size \(2\), ring length \(2\), across all possible Smith-level profiles and all middle/right matrices. It checks the matching formula on 2,989 profiles with \(1\le n\le7\), \(1\le k\le5\), and 7,920 sampled sandwich products in dimensions up to four and lengths up to three. A further 1,830 deterministic checks over mixed-characteristic rings \(\mathbb Z/2^k\mathbb Z\) confirmed the same upper bounds using direct finite-module image enumeration. All checks produced `VERIFY_OK`.

A concrete depth-two example is \(A=\operatorname{diag}(1,\pi,0)\), \(B=\operatorname{diag}(0,\pi,1)\), and \(T=E_{12}+E_{23}\). They satisfy \(AB=0\) and \(ATB=\pi E_{12}+\pi E_{23}\), whose image needs two generators. For the same matrix size over a field, the sharp capacity is only one.

## Relationship to prior work
Subba and Subedi (arXiv:2609.24439v1, first posted September 21, 2026) defined zero-insertivity in this setting and proved that all singular two-by-two matrices over a field are zero-insertive (Corollary 2.7). Their text also gives a one-entry construction for matrices over general coefficient rings (Remark 2.19). Their 2025 precursor arXiv:2508.01333v1 concerns ZINC and nil-cleanness rather than the generator-rank capacity of zero-insertive matrices. A published mathematical finding, *Zero-insertive matrices are exactly the half-rank locus* (October 4, 2026), classifies all matrix sizes over division rings; its theorem is the \(k=1\) boundary of the present formula and does not treat nonfield chain rings. Nóbrega, Feng, Silva, and Uchôa-Filho (arXiv:1311.4861v1) develop Smith shapes for finite-chain-ring matrix channels, without imposing the zero-product condition \(AB=0\). This finding combines the chain-ring filtration with a sharp Ferrers-graph matching argument.

## Limitations
The theorem determines the *maximum minimal image-generator number*, including the value conditioned on Smith levels of the first factor, and its attained interval. It does not describe all zero-insertive matrices, count individual Smith shapes, or claim any probability law. The exhaustive computations are confined to the stated small rings; arbitrary sizes and arbitrary finite commutative chain rings are covered by the proof, not computational extrapolation. Historical-priority search cannot exclude a differently worded older factorization theorem.

## References
1. S. Subba and T. Subedi, *Semicommutativity via Zero-Insertive Elements: Insights from Path and Leavitt Path Algebras*, arXiv:2609.24439v1, September 21, 2026, https://arxiv.org/abs/2609.24439.
2. S. Subba and T. Subedi, *Zero Insertive Nil Clean Rings*, arXiv:2508.01333v1, August 2, 2025, https://arxiv.org/abs/2508.01333.
3. *Zero-insertive matrices are exactly the half-rank locus*, published mathematical finding, October 4, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-zero-insertive-matrices-are-exactly-the-half-rank-locus--8052759fe4ed.
4. R. W. Nóbrega, C. Feng, D. Silva, and B. F. Uchôa-Filho, *On Multiplicative Matrix Channels over Finite Chain Rings*, arXiv:1311.4861v1, 2013, https://arxiv.org/abs/1311.4861.
