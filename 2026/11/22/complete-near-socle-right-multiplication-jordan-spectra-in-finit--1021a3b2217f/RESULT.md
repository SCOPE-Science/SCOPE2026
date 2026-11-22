# Complete near-socle right-multiplication Jordan spectra in finite exterior algebras

## Finding

For every integer \(n\ge5\), every finite field \(k=\mathbb F_q\) (including characteristic two), and the exterior algebra \(E=\bigwedge_k V\) of an \(n\)-dimensional space, write \(J=\bigoplus_{d=1}^{n}\bigwedge^dV\). For every \(z\in J^{n-2}\), let \(R_z:E\to E\) be right multiplication, \(R_z(w)=w\wedge z\). The complete distribution of \(\operatorname{rank}R_z\), together with its Jordan form, is:

\[
\begin{array}{c|c}
\operatorname{rank}R_z & \#\{z\in J^{n-2}:\operatorname{rank}R_z=s\}\\\hline
0&1\\
1&q-1\\
2&q(q^n-1)\\
2+2r& q^{n+1}{n\brack 2r}_q\,q^{r(r-1)}\prod_{j=1}^{r}(q^{2j-1}-1),\quad 1\le r\le\lfloor n/2\rfloor.
\end{array}
\]

Here \({n\brack d}_q=\prod_{i=0}^{d-1}(q^{n-i}-1)/(q^{d-i}-1)\) is the Gaussian binomial coefficient. Every displayed rank occurs and no others do; in particular ranks \(3,5,7,\ldots\) do not occur. Every \(R_z\) is square-zero, with Jordan partition \(2^s1^{2^n-2s}\), where \(s=\operatorname{rank}R_z\); the notation denotes \(s\) blocks of size two and \(2^n-2s\) blocks of size one.

The distribution is invariant under arbitrary changes to the top two graded components when the degree-\(n-2\) component is nonzero. Thus the formula is a census of *all inhomogeneous* near-socle elements, not just homogeneous forms. The total number of counted elements is \(q^{\binom n2+n+1}\).

## Assumptions and scope

The exterior product is alternating even in characteristic two (each basis generator has square zero). The assertion includes all prime-power field sizes \(q\), all \(n\ge5\), all \(z\in J^{n-2}=\bigwedge^{n-2}V\oplus\bigwedge^{n-1}V\oplus\bigwedge^nV\), and the right-regular multiplication operator, not an arbitrary endomorphism. There are no asymptotic or genericity hypotheses.

## Proof

Choose a nonzero linear volume functional \(\varepsilon:\bigwedge^nV\to k\). Write \(z=\alpha+\beta+\gamma\), where \(\alpha\in\bigwedge^{n-2}V\), \(\beta\in\bigwedge^{n-1}V\), and \(\gamma\in\bigwedge^nV\). Since \(2(n-2)>n\) for \(n\ge5\), every product of two elements of \(J^{n-2}\) vanishes. Consequently \(R_z^2=0\). Moreover, \(R_z\) annihilates all terms of exterior degree at least three. With source \(\bigwedge^0V\oplus V\oplus\bigwedge^2V\) and target \(\bigwedge^{n-2}V\oplus\bigwedge^{n-1}V\oplus\bigwedge^nV\), its only nonzero block is exactly

\[
(s,v,w)\longmapsto(s\alpha,\ s\beta+v\wedge\alpha,\ s\gamma+v\wedge\beta+w\wedge\alpha).
\]

If \(\alpha\ne0\), the perfect top-wedge pairing \(\bigwedge^2V\times\bigwedge^{n-2}V\to\bigwedge^nV\) guarantees that \(w\mapsto w\wedge\alpha\) has one-dimensional image. Quotienting by that top-degree image, the displayed matrix has rank \(1+\operatorname{rank}(v\mapsto v\wedge\alpha)\): the first \(1\) is the independent degree-\(n-2\) coordinate \(s\alpha\), while the remaining map has image in degree \(n-1\). Restoring the one-dimensional top image gives

\[
\operatorname{rank}R_z=2+\operatorname{rank}(V\longrightarrow\bigwedge^{n-1}V,\ v\mapsto v\wedge\alpha).
\]

Under the perfect top pairing, the latter map corresponds to the alternating bilinear form \(B_\alpha(u,v)=\varepsilon(u\wedge v\wedge\alpha)\). The linear map \(\alpha\mapsto B_\alpha\) from \(\bigwedge^{n-2}V\) to \(\bigwedge^2V^*\) is an isomorphism: each basis coefficient of \(\alpha\) matches the complementary two-index matrix coefficient. In particular \(B_\alpha\ne0\) for \(\alpha\ne0\), and its possible ranks are precisely \(2r\) for \(1\le r\le\lfloor n/2\rfloor\), even in characteristic two.

The number of alternating bilinear forms of rank \(2r\) on \(V\) is

\[
A_{n,r}(q)={n\brack 2r}_q\frac{|\operatorname{GL}_{2r}(\mathbb F_q)|}{|\operatorname{Sp}_{2r}(\mathbb F_q)|}={n\brack 2r}_q\,q^{r(r-1)}\prod_{j=1}^r(q^{2j-1}-1).
\]

Indeed, choose the \((n-2r)\)-dimensional radical and then a nondegenerate alternating form on its \(2r\)-dimensional quotient; the latter forms form one \(\operatorname{GL}_{2r}\) orbit with stabilizer \(\operatorname{Sp}_{2r}\). There are independently \(q^n\) choices of \(\beta\) and \(q\) of \(\gamma\), yielding the \(2+2r\) fiber sizes.

If \(\alpha=0\) but \(\beta\ne0\), the scalar-input image \(k\beta\subset\bigwedge^{n-1}V\) and the top-degree image \(V\wedge\beta=\bigwedge^nV\) are independently one-dimensional by perfect pairing, and \(R_z\) has rank two. There are \((q^n-1)q\) such elements. If \(\alpha=\beta=0\), \(\gamma\ne0\), multiplication has rank one and there are \(q-1\) choices; the remaining zero element has rank zero. These cases are disjoint and exhaust \(q^{\binom n2+n+1}\) elements. A square-zero operator of rank \(s\) on dimension \(2^n\) has exactly \(s\) Jordan blocks of size two and all remaining blocks of size one, proving the partition statement.

## Verification

The attached standalone scripts `near_socle_checker.py` and `exterior_cubic_checker.py` independently form exterior-basis multiplication matrices and compute ranks over prime fields. `near_socle_checker.py` tested every asserted possible rank with forced alternating-form representatives and 120 seeded cases for each of \(n=5,6,7\) and \(q=2,3,5\), plus the exact combinatorial total identities. `exterior_cubic_checker.py` exhaustively counted all \(2^{16}=65{,}536\) elements of \(J^3\) for \(n=5,q=2\), exhaustively checked all \(3^{10}=59{,}049\) homogeneous cubic elements for \(n=5,q=3\), and compared 400 seeded direct multiplication matrices for each of \(q=2,3,5,7\). Both passed; the captured outputs are included. The experiments are finite corroboration, not a substitute for the all-dimensional proof.

For \(n=5\) the rank-count vector in increasing rank order \((0,1,2,4,6)\) is
\[
\bigl(1,\ q-1,\ q(q^5-1),\ q^6(q^5-1)(q^2+1),\ q^8(q^5-1)(q^3-1)\bigr).
\]

## Relationship to prior work

The classical alternating-form orbit enumeration and finite-field rank distribution are credited to established linear-algebra theory; for an explicit published account compare Fulman–Goldstein (2012), particularly Section 5, which does not classify multiplication in exterior algebras. Draisma–Shaw (2009), Sections 1–2, treats alternating forms and the Grassmann algebra, but its assertions concern singular subspaces, not the near-socle right-multiplication census.

A published complete rank census for the five-generator elementary-abelian 2-group algebra already yields the exact specialization \(n=5\) in characteristic two, including all the near-socle ranks. That covered subcase is not claimed as new. The extension to all \(n\ge6\) in characteristic two, and to all \(n\ge5\) in odd characteristic, plus the inhomogeneous filtered-rigidity theorem, are the substantive scope here.

Related existing results concern multiplication by homogeneous bivectors, the full regular-multiplication Jordan distribution for four generators, and homogeneous near-socle operators of degree \(n-3\) in characteristic two. Those do not by themselves determine the all-field, all-dimensional distribution for arbitrary inhomogeneous elements in \(J^{n-2}\). The statement is a structured near-socle application of classical alternating-form counts, not a claim to a new alternating-form enumeration. Priority against all possible earlier implicit corollaries has not been independently established.

## Limitations

The theorem makes no claim for \(n<5\), for multiplication by elements outside \(J^{n-2}\), or for the classification of individual multiplication operators up to conjugacy beyond their Jordan forms. It is an exact self-contained rank census and does not imply new results about general Grassmann algebra modules. Exhaustive numerical checks were limited to the configurations listed above. Historical novelty is subject to fuller comparison with related previous literature.

## References

1. J. Draisma and R. Shaw, *Singular lines of trilinear forms*, arXiv:0909.5676 (first public September 30, 2009), https://arxiv.org/html/0909.5676v1 .
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504 (first public November 2, 2012), Section 5, https://arxiv.org/html/1211.0504v4 .
