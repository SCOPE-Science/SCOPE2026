# Linear local and 2-local derivations on Heisenberg Lie algebras: hierarchy and rank census

## Finding
For every field \(k\) and every integer \(n\ge1\), let \(H=V\oplus kz\) be a Heisenberg Lie algebra with \(\dim_k V=m=2n\) and \([v,w]=\omega(v,w)z\), for a fixed nondegenerate alternating form \(\omega\). A **linear local derivation** is a linear map whose value at each vector agrees with some ordinary derivation (depending on the vector). A **linear 2-local derivation** is a linear map whose values at every ordered pair agree with one ordinary derivation (depending on the pair).

Every linear local derivation, and only such a map, has the unique form
\[
\Delta(v+az)=Bv+\bigl(f(v)+at\bigr)z,
\qquad B\in\operatorname{End}_k(V),\ f\in V^*,\ t\in k.
\]
Such a map is a linear 2-local derivation if and only if
\[
\omega(Bv,w)+\omega(v,Bw)=c\omega(v,w)
\quad\text{for every }v,w\in V
\]
for some \(c\in k\). It is an ordinary derivation if and only if, in addition, \(t=c\). In particular, the three spaces have respective dimensions
\[
\dim\operatorname{LocDer}_{\rm lin}(H)=4n^2+2n+1,\qquad
\dim\operatorname{2LocDer}_{\rm lin}(H)=2n^2+3n+2,\qquad
\dim\operatorname{Der}(H)=2n^2+3n+1.
\]
Thus derivations are strictly contained in linear 2-local derivations in every rank, and linear 2-local derivations equal linear local derivations exactly in Heisenberg dimension three (\(n=1\)).

For every prime power \(q\), the **complete rank census** over \(k=\mathbb F_q\) is
\[
\sum_{\Delta\in\operatorname{LocDer}_{\rm lin}(H)}u^{\operatorname{rank}\Delta}
=\sum_{r=0}^{m}{m\brack r}_q
\left(\prod_{i=0}^{r-1}(q^m-q^i)\right)
\left(q^r u^r+(q^{m+1}-q^r)u^{r+1}\right),
\quad m=2n,
\]
where \({m\brack r}_q\) is the Gaussian binomial coefficient and the empty product is one. It sums to \(q^{m^2+m+1}\) at \(u=1\).

## Assumptions and scope
The field \(k\) is arbitrary, including characteristic two; \(n\ge1\), and \(\omega\) is nondegenerate and alternating. All local and 2-local maps classified here are assumed \(k\)-linear. Witnesses are arbitrary ordinary \(k\)-linear Lie derivations. A nonlinear 2-local map is not included in the assertion. The rank polynomial counts labeled linear maps, not automorphism-conjugacy classes. The conformal-symplectic multiplier \(c\) is unique because \(\omega\ne0\).

## Proof
**Step 1: all ordinary derivations.** The center and derived algebra of \(H\) are both \(kz\), so an ordinary derivation has the form \(D(v+az)=Av+(g(v)+ac)z\). Applying the derivation identity to \([v,w]=\omega(v,w)z\) yields precisely
\[
\omega(Av,w)+\omega(v,Aw)=c\omega(v,w).
\]
Conversely this equation suffices. Therefore \(A\) belongs to the conformal symplectic Lie algebra \(\mathfrak{csp}(V,\omega)\), and \(g\in V^*\) is free. Relative to a symplectic basis, \(A_0=\operatorname{diag}(cI_n,0)\) has multiplier \(c\), so every scalar multiplier exists in every characteristic. Its zero-multiplier kernel \(\mathfrak{sp}(V,\omega)\) has dimension \(n(2n+1)\), by its identification with symmetric bilinear forms through \(S\mapsto\omega(S\cdot,\cdot)\). This argument is valid in characteristic two.

**Step 2: evaluation-surjectivity lemma.** Fix \(0\ne v\in V\) and any \(u\in V\). There exists \(S\in\mathfrak{sp}(V,\omega)\) with \(Sv=u\): prescribe the symmetric bilinear form \(b(v,x)=\omega(u,x)\) and extend it to a symmetric bilinear form on a basis containing \(v\). Nondegeneracy gives \(S\) with \(b(x,y)=\omega(Sx,y)\). Hence, for any prescribed scalar \(c\), a conformal symplectic map of multiplier \(c\) can be chosen with any prescribed value at nonzero \(v\). Every derivation maps \(z\) into \(kz\), so a linear local derivation must preserve the center. Conversely take any center-preserving \(\Delta(v+az)=Bv+(f(v)+at)z\). For \(v\ne0\) use an ordinary derivation with multiplier zero and quotient value \(Bv\), and choose its central functional \(g\) with \(g(v)=f(v)+at\). For \(v=0\), use any derivation of multiplier \(t\). Thus every center-preserving map is local.

**Step 3: necessity for two-locality.** For independent vectors \(v,w\in V\) with \(\omega(v,w)=0\), the ordinary derivation witnessing the two values \(\Delta(v),\Delta(w)\) implies
\[
\beta_B(v,w):=\omega(Bv,w)+\omega(v,Bw)=0.
\]
The alternating form \(\beta_B\) vanishes automatically on dependent pairs. If \(n=1\), any alternating form on \(V\) is proportional to \(\omega\). If \(n\ge2\), choose a hyperbolic symplectic basis \((e_i,f_i)\). Every basis pair except \((e_i,f_i)\) is \(\omega\)-orthogonal, hence has zero \(\beta_B\) value. For \(i\ne j\), the vectors \(e_i+e_j\) and \(f_i-f_j\) are also orthogonal; evaluating \(\beta_B\) shows \(\beta_B(e_i,f_i)=\beta_B(e_j,f_j)\). This remains valid in characteristic two. Thus \(\beta_B=c\omega\) for a unique \(c\), proving \(B\in\mathfrak{csp}(V,\omega)\).

**Step 4: sufficiency for two-locality.** Suppose \(B\) has conformal multiplier \(c\), but allow the central scalar \(t\) to differ from \(c\). For arbitrary \(x=v+az\) and \(y=w+bz\): if \(v,w\) are independent, use the ordinary derivation with quotient \(A=B\), multiplier \(c\), and a linear central functional \(g\) prescribed by \(g(v)=f(v)+a(t-c)\) and \(g(w)=f(w)+b(t-c)\). If \(x,y\) are independent but their projections \(v,w\) are dependent, their span contains \(z\). Choose a derivation of multiplier \(t\) whose quotient takes the nonzero projection \(v\) to \(Bv\), using Step 2; prescribe \(g(v)=f(v)\). It then agrees with \(\Delta\) on their span. When \(x,y\) are dependent, the local witness for a nonzero member suffices by linearity. Therefore the stated criterion is sufficient. Step 1 identifies the additional ordinary-derivation condition \(t=c\).

**Step 5: dimensions.** There are \(m^2+m+1=4n^2+2n+1\) free parameters in an arbitrary center-preserving linear map. The conformal symplectic quotient has dimension \(n(2n+1)+1\); adding \(m\) free central-functional parameters and an independent \(t\) gives \(2n^2+3n+2\). Equating \(t\) to the conformal multiplier reduces the latter dimension by one. Their difference is \(2n^2-n-1=(2n+1)(n-1)\), hence vanishes exactly when \(n=1\).

**Step 6: finite-field rank enumeration.** For a fixed \(m\times m\) matrix \(B\) of rank \(r\), the full block matrix of \(\Delta\) is \(\begin{psmallmatrix}B&0\\f&t\end{psmallmatrix}\). Its rank is \(r\) if and only if \(t=0\) and \(f\) lies in the row space of \(B\), yielding exactly \(q^r\) pairs \((f,t)\). The remaining \(q^{m+1}-q^r\) pairs give rank \(r+1\). The number of matrices \(B\) of rank \(r\) is \({m\brack r}_q\prod_{i=0}^{r-1}(q^m-q^i)\), by choosing their image and a surjection onto it. Multiplication of these independent counts proves the displayed rank polynomial.

## Verification
The accompanying standalone `verify.py` uses only the Python standard library and directly checks the Lie-derivation equations and pairwise witnesses on small fields. It exhausts all linear maps on the three-dimensional Heisenberg algebra over \(\mathbb F_2\), tests 350 reproducibly generated maps over \(\mathbb F_3\), checks all conformal-symplectic quotient matrices in dimension four over \(\mathbb F_2\), and independently enumerates the full rank population of local maps in dimension three over \(\mathbb F_2\) and \(\mathbb F_3\). The output is in `verify_output.txt` and ends `ALL_CHECKS_PASS`. The proof, not the finite checks, establishes the arbitrary-field statement.

## Relationship to prior work
Ayupov and Kudaybergenov (arXiv:1508.03939, first public 2015-08-17) establish that filiform Lie algebras, including the three-dimensional Heisenberg example, have local derivations that are not derivations; their Section 4 constructs witnesses rather than the present uniform classification of all linear local and linear 2-local maps, their dimensions and rank distribution. Ayupov, Kudaybergenov and Rakhimov (2015, DOI below) establish general existence of nonglobal 2-local derivations for nilpotent Lie algebras, but their full text was not accessible for a decisive comparison; no claim of full-document noncoverage is made. Later work by Khudoyberdiyev and Jumaniyozov on local half-derivations (arXiv:2405.04209), and related recent studies, provide context but do not supply the stated joint characteristic-free classification in the portions inspected. The matrix-counting formula uses the standard Gaussian rank count, not claimed new. A possibly broader, unidentified classification of reflexive hulls of conformal symplectic operator spaces would be a priority risk.

## Limitations
Only **linear** local and 2-local derivations are classified, not nonlinear 2-local maps. The polynomial enumerates ranks of all linear local derivations rather than ranks separately within the linear 2-local subspace. It does not determine automorphism orbits, group schemes, or the operator rank census for arbitrary nilpotent Lie algebras. A plausible 2015 primary source was available only through its abstract; the historical-priority comparison is therefore not exhaustive.

## References
1. S. Ayupov and K. Kudaybergenov, *Local derivations on finite-dimensional Lie algebras*, arXiv:1508.03939 (first submitted 2015-08-17), https://arxiv.org/abs/1508.03939; later journal DOI 10.1016/j.laa.2015.11.034.
2. S. Ayupov, K. Kudaybergenov, and I. Rakhimov, *2-Local derivations on finite-dimensional Lie algebras*, Linear Algebra and its Applications 474 (2015), 1–11, DOI 10.1016/j.laa.2015.01.016.
3. A. Khudoyberdiyev and D. Jumaniyozov, *Local and 2-local half-derivations on finite-dimensional Lie algebras*, arXiv:2405.04209, https://arxiv.org/abs/2405.04209 (later supporting context; distinct half-derivation problem).
4. Relevant current Lie-algebra local-derivation literature, arXiv:2610.40348, https://arxiv.org/abs/2610.40348 (supporting context, not archival ownership).
