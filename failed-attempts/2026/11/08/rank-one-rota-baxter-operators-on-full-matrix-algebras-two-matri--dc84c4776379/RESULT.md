# Rank-one Rota–Baxter operators on full matrix algebras: two matrix types and an exact finite-field census

## Finding

Let \(k\) be any field and \(n\ge 2\). A linear map \(R:M_n(k)\to M_n(k)\) is a weight-zero Rota–Baxter operator if
\[
R(X)R(Y)=R(R(X)Y+XR(Y))\qquad(X,Y\in M_n(k)).
\]
Among the nonzero maps of vector-space rank one, there are exactly two structural types. Writing uniquely up to reciprocal scaling
\[
R(X)=\operatorname{tr}(BX)A,\qquad A,B\in M_n(k)\setminus\{0\},
\]
these types are:

**Square-zero image type (N).** The conditions are \(A^2=0\) and \(AB=BA=0\).

**Idempotent image-line type (I).** There exists \(\mu\in k^\times\) with \(A^2=\mu A\), and exactly one of the following alternatives holds:
\[
(AB=\mu B,\ BA=0)\quad\text{or}\quad(BA=\mu B,\ AB=0).
\]
Equivalently, in type (I), there is a **unique** idempotent \(e\) spanning the image line, and the operator is \(R(X)=\operatorname{tr}(CX)e\), where \(C\ne0\) belongs to \(eM_n(k)(1-e)\) or \((1-e)M_n(k)e\). Both types satisfy \(R^2=0\).

For a finite field \(\mathbb F_q\), denote by \({a\brack b}_q\) the Gaussian binomial coefficient and by \(|\mathrm{GL}_r(q)|=\prod_{i=0}^{r-1}(q^r-q^i)\) the number of invertible \(r\)-by-\(r\) matrices. The **exact** numbers of nonzero rank-one Rota–Baxter maps of types (N) and (I) are
\[
\begin{aligned}
\mathcal N_{n,q}&=\sum_{r=1}^{\lfloor n/2\rfloor}
{n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(q)|
\frac{q^{(n-r)^2}-1}{q-1},\\
\mathcal I_{n,q}&=2\sum_{r=1}^{n-1}{n\brack r}_q
q^{r(n-r)}(q^{r(n-r)}-1).
\end{aligned}
\]
There are \(\mathcal N_{n,q}+\mathcal I_{n,q}\) nonzero maps, and one additional zero map. These formulas hold in *every characteristic*, including characteristic two.

The first values are \((\mathcal N,\mathcal I)=(3,12)\) for \(n=2,q=2\), \((8,48)\) for \(n=2,q=3\), and \((315,336)\) for \(n=3,q=2\).

## Assumptions and scope

The matrix algebra is the associative unital algebra \(M_n(k)\) with ordinary multiplication; the operator rank refers to its rank as a linear transformation on the \(n^2\)-dimensional vector space \(M_n(k)\). No algebraic-closedness or characteristic assumption is made. The finite-field count is for **labeled maps**, not orbits under matrix conjugation. The rank-one restriction is essential; higher-rank Rota–Baxter operators are not classified here.

## Proof

**Step 1: factorization and the scalar identity.** Every rank-one linear map has the form \(R(X)=\phi(X)A\), with \(\phi\ne0\), \(A\ne0\). Nondegeneracy of the trace pairing yields a unique \(B\ne0\) with \(\phi(X)=\operatorname{tr}(BX)\). Any two such pairs differ by \((A,B)\mapsto(tA,t^{-1}B)\), \(t\in k^\times\).

Choose \(X,Y\) with \(\phi(X)=\phi(Y)=1\). The Rota–Baxter equation puts \(A^2\) in the line \(kA\); write \(A^2=\mu A\). The equation for arbitrary \(X,Y\) is now equivalent to
\[
\mu\phi(X)\phi(Y)=\phi(X)\phi(AY)+\phi(Y)\phi(XA).
\]
Setting \(\phi(X)=0\) and choosing \(\phi(Y)=1\), then reversing the roles, shows that there are scalars \(c,d\in k\) with
\[
\phi(XA)=c\phi(X),\qquad \phi(AY)=d\phi(Y),\qquad c+d=\mu.
\]
The nondegenerate trace pairing makes these identities exactly
\[
AB=cB,\qquad BA=dB,\qquad c+d=\mu.
\]
Since \(A^2=\mu A\), associating \(A(AB)=(A^2)B\) and \((BA)A=B(A^2)\) yields \(c^2=\mu c\) and \(d^2=\mu d\). If \(\mu=0\), then \(c=d=0\). If \(\mu\ne0\), then \(c,d\in\{0,\mu\}\), and \(c+d=\mu\) forces exactly one of them to equal \(\mu\). This proves the necessity of the two types without dividing by the characteristic. Substitution in the scalar identity proves sufficiency.

**Step 2: nilpotence.** In type (N), \(BA=0\). In type (I), either \(BA=0\) or \(AB=0\). Thus in both cases \(\operatorname{tr}(BA)=0\), because trace is cyclic. Hence \(R^2(X)=\operatorname{tr}(BX)\operatorname{tr}(BA)A=0\).

**Step 3: square-zero type count.** Fix the matrix rank \(r\) of a nonzero square-zero matrix \(A\). Then \(1\le r\le\lfloor n/2\rfloor\). Choosing \(\operatorname{im} A=W\), \(\ker A=K\supseteq W\), and the induced isomorphism \(k^n/K\to W\) yields precisely
\[
\#\{A:A^2=0,\operatorname{rank}A=r\}
={n\brack r}_q{n-r\brack r}_q|\mathrm{GL}_r(q)|.
\]
For fixed \(A\), the conditions \(AB=0\) and \(BA=0\) mean that \(B\) factors as an arbitrary map \(k^n/\operatorname{im}A\to\ker A\). This is a vector space of dimension \((n-r)^2\), with \(q^{(n-r)^2}-1\) nonzero members. Reciprocal scaling of \((A,B)\) acts freely with orbit size \(q-1\), so division by \(q-1\) counts the distinct rank-one operators.

**Step 4: idempotent-image type count.** Normalize \(A=\mu e\) to the unique nonzero idempotent \(e\) on its image line. For \(\operatorname{rank}e=r\), choose an image \(r\)-space and a complementary kernel. There are
\[
{n\brack r}_q q^{r(n-r)}
\]
such idempotents. For each, the two exclusive choices \(eB=B,\ Be=0\) and \(Be=B,\ eB=0\) define the disjoint spaces \(eM_n(k)(1-e)\) and \((1-e)M_n(k)e\), each of dimension \(r(n-r)\). Each has \(q^{r(n-r)}-1\) nonzero choices. Summing over \(1\le r<n\) gives the second formula. Uniqueness of the idempotent normalization shows that no additional scalar division is needed.

The two types cannot overlap, because the image line cannot contain both a nonzero idempotent and a nonzero square-zero element. This completes the classification and counting proof.

## Verification

A standalone checker evaluates all nonzero rank-one tensor representations \(R(X)=\operatorname{tr}(BX)A\), using the first-nonzero-coordinate normalization for \(A\). For \(M_2(\mathbb F_2)\) and \(M_2(\mathbb F_3)\), it evaluates the **original Rota–Baxter identity on every pair of matrix units for every representative** and compares with the structural classification. For \(M_3(\mathbb F_2)\), it exhausts all matrix-tensor representatives using the structural conditions, and directly checks the original equation on 100 sampled representatives. It also evaluates, but does not exhaustively verify, the formula at \((n,q)=(3,3),(4,2)\).

Run `python3 verify_rank_one_rb.py`. The expected final marker is `RANK_ONE_MATRIX_ROTA_BAXTER_EXACT_COUNTS_OK`, with detailed counts in `verification_output.txt`. Finite checks corroborate; the proof above establishes the all-dimensional result.

## Relationship to prior work

Guo, Rosenkranz, and Zheng's 2014 preprint establishes the Rota–Baxter identity and solves finite-dimensional semigroup-algebra examples by polynomial equations; those are **not** full matrix algebras of arbitrary order. Tang, Zhang, and Sun's 2014 complex \(2\)-by-\(2\) classification, reproduced with proof as Theorem 6 in Benito, Gubarev, and Pozhidaev (2018), already covers the rank-one \(n=2\) conjugacy types (M1) and (M2). They are credited as the low-dimensional predecessors, not rebranded as new. Gubarev (2024), Theorem 3, classifies an \(n=3\) subfamily over quadratically closed fields of characteristic not two or three, assuming \(R(1)\ne0\), up to equivalence; it does not enumerate all finite-field labeled rank-one maps.

The present statement concerns the **entire rank-one locus for all matrix orders and all fields**, with its two intrinsic matrix types and an exact finite-field counting formula. It is weaker than a classification of all Rota–Baxter operators, and its low-dimensional special cases overlap existing work. No claim of independent priority certification is made.

## Limitations

Only rank-one operators are classified. The finite-field formula counts individual maps rather than conjugation classes; it does not describe scheme-theoretic nilpotents or higher-rank operators. The literature comparison is not an exhaustive priority proof; in particular, a more general all-dimensional rank-one or associative Yang–Baxter tensor theorem could subsume the result. No independent mathematical audit has been performed.

## References

1. L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, first arXiv submission 2014-02-15, arXiv:1402.3702, especially Sections 1–2 and Theorem 2.1. https://arxiv.org/abs/1402.3702
2. X. Tang, Y. Zhang, Q. Sun, *Rota-Baxter operators on 4-dimensional complex simple associative algebras*, Applied Mathematics and Computation 229 (2014), 173–186, DOI:10.1016/j.amc.2013.12.032.
3. P. Benito, V. Gubarev, A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037v1 (2018-01-22), Section 5.1, Theorem 6 and its proof. https://arxiv.org/pdf/1801.07037
4. V. Gubarev, *Rota–Baxter operators of weight zero on the matrix algebra of order three without unit in kernel*, arXiv:2412.00825v1 (2024-12-01), Sections 1–2 and Theorem 3. https://arxiv.org/pdf/2412.00825
