# Rank-indexed components and exact point counts for square-zero matrices over finite dual numbers

## Finding

Fix an integer \(n\ge 2\) and a field \(k\), and put \(R=k[\varepsilon]/(\varepsilon^2)\). Every matrix over \(R\) has a unique expansion \(T=A+\varepsilon B\), where \(A,B\in M_n(k)\). Consider the **square-zero lift locus**
\[
\mathcal J_n(k)=\{(A,B)\in M_n(k)^2:(A+\varepsilon B)^2=0\}.
\]
For each \(0\le r\le\lfloor n/2\rfloor\), let \(\mathcal S_r\subset\mathcal J_n\) consist of pairs with \(\operatorname{rank}A=r\). The reduced geometric locus \(\mathcal J_{n,\mathrm{red}}\) has **exactly \(\lfloor n/2\rfloor+1\) geometrically irreducible components**, namely the distinct closures \(\overline{\mathcal S_r}\) over an algebraic closure. Each component has dimension \(n^2\). More precisely, \(\mathcal S_r\) is a vector bundle of rank \(n^2-2r(n-r)\) over the rank-\(r\) square-zero conjugacy orbit of dimension \(2r(n-r)\).

For every prime power \(q\), the exact number of square-zero matrices in \(M_n(\mathbb F_q[\varepsilon]/(\varepsilon^2))\) is
\[
\boxed{\#\mathcal J_n(\mathbb F_q)=
\sum_{r=0}^{\lfloor n/2\rfloor}
{n\brack r}_q\,{n-r\brack r}_q
\Bigl(\prod_{j=0}^{r-1}(q^r-q^j)\Bigr)
q^{n^2-2r(n-r)}.}
\]
Here \({a\brack b}_q\) denotes the Gaussian binomial coefficient, and the empty product is \(1\). The displayed summands separately count all pairs with \(\operatorname{rank}A=r\). The statement holds in every characteristic, including characteristic two.

## Assumptions and scope

All matrices are **full** \(n\)-by-\(n\) matrices, not upper-triangular matrices. Geometric components are taken after extending \(k\) to an algebraic closure and then giving the solution set its reduced variety structure. No assertion that the polynomial-equation scheme of pairs \((A,B)\) is reduced is made. The finite-field formula counts labeled matrices, not isomorphism or conjugacy classes. The component description holds for arbitrary fields \(k\) after geometric base change; the point count requires a finite field. The integer \(n\) is any integer at least two. For \(n=1\), the same formulas reduce to one affine-line component with \(q\) points, but that degenerate case is not the focus.

The natural source problem is the representation scheme of the algebra \(k[t]/(t^2)\): its ordinary \(n\)-dimensional representations are matrices \(A\) with \(A^2=0\). The pairs above classify *all first-order lifts of these representations* to the base ring \(k[\varepsilon]/(\varepsilon^2)\), before quotienting by change of basis. This is the first jet of the relation-defined **scheme** \(A^2=0\), not automatically the jet of its reduced underlying variety.

## Proof

**Step 1: Linearization.** Since \(\varepsilon^2=0\), the defining equation is equivalent, with no characteristic restriction, to
\[
A^2=0,\qquad AB+BA=0.
\]
For fixed \(A\), the possible \(B\)'s form the kernel of the \(k\)-linear endomorphism \(L_A:M_n(k)\to M_n(k)\) defined by \(L_A(B)=AB+BA\).

**Step 2: All possible reductions.** The condition \(A^2=0\) implies \(\operatorname{im} A\subseteq\ker A\), hence \(r=\operatorname{rank}A\le\lfloor n/2\rfloor\). Its Jordan form consists of exactly \(r\) blocks of size two and \(s=n-2r\) blocks of size one (all of eigenvalue zero), over any field. Consequently all rank-\(r\) square-zero matrices form one smooth, irreducible \(\mathrm{GL}_n\)-orbit \(\mathcal O_r\).

**Step 3: Dimension of the anticommuting fiber.** On every size-two block \(\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\), conjugation by \(\operatorname{diag}(1,-1)\) sends the block to its negative. On every size-one block, use the identity. Thus \(A\) and \(-A\) are conjugate in every characteristic. If \(S\) is invertible with \(AS=-SA\), then \(L_A(B)=0\) if and only if \(BS\) commutes with \(A\). Therefore \(\dim\ker L_A=\dim C_{M_n(k)}(A)\). The centralizer is \(\operatorname{End}_{k[t]}\big((k[t]/(t^2))^r\oplus k^s\big)\). The elementary dimensions of module homomorphisms between length-two and length-one blocks yield
\[
\dim C_{M_n(k)}(A)=2r^2+2rs+s^2=n^2-2r(n-r).
\]
The centralizer in \(\mathrm{GL}_n\) is the open unit subset of this linear space, so its dimension is the same. Hence
\[
\dim\mathcal O_r=n^2-\dim C_{M_n(k)}(A)=2r(n-r).
\]

**Step 4: Components.** Over an algebraic closure, the kernel of \(L_A\) has the constant dimension \(n^2-2r(n-r)\) as \(A\) ranges over the smooth orbit \(\mathcal O_r\). It is the kernel vector bundle of a constant-rank morphism of trivial vector bundles on \(\mathcal O_r\). Its total space is \(\mathcal S_r\), which is irreducible and has dimension
\[
2r(n-r)+n^2-2r(n-r)=n^2.
\]
The entire locus is the finite union of these locally closed strata. Therefore it is the union of their irreducible closures. The closures are pairwise distinct: rank of the projection \((A,B)\mapsto A\) cannot increase upon specialization, and two different strata cannot both be dense open subsets of one irreducible closure. Because every closure has the same dimension, none can properly contain another. Thus the closures are exactly the irreducible components, in number \(\lfloor n/2\rfloor+1\), each of dimension \(n^2\). The strata and their closures are all defined over the prime field, so the components remain geometrically irreducible in every characteristic.

**Step 5: Finite-field enumeration.** Let \(V=\mathbb F_q^n\). For a rank-\(r\) square-zero operator \(A\), choose its image \(I\subset V\) of dimension \(r\), choose its kernel \(K\supseteq I\) of dimension \(n-r\), then choose the induced isomorphism \(V/K\overset{\sim}{\to} I\). These choices are in bijection with rank-\(r\) square-zero matrices. Their numbers are respectively \({n\brack r}_q\), \({n-r\brack r}_q\), and \(|\mathrm{GL}_r(\mathbb F_q)|=\prod_{j=0}^{r-1}(q^r-q^j)\). For each such \(A\), Step 3 gives exactly \(q^{n^2-2r(n-r)}\) admissible \(B\)'s. Multiply and sum over all ranks to obtain the formula. Every term is an exact count; no asymptotic approximation is used.

## Verification

A standalone checker, `verify.py`, evaluates matrix multiplication directly over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) (the last via its quadratic polynomial basis). It exhaustively enumerates all square-zero reductions for \((q,n)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)\), computes the rank of the explicit linear map \(L_A\), and checks both the Gaussian-binomial rank counts and the total-lift formula. It separately exhausts **all pairs \((A,B)\)** for \((q,n)=(2,2),(3,2),(4,2),(2,3)\), without using the predicted kernel dimension in the pair test.

The verified total counts for \((q,n)=(2,2),(3,2),(4,2),(2,3),(3,3),(2,4)\) are respectively \(28,153,496,1184,44955,226816\). These computations are finite cross-checks only. The uniform claims for arbitrary \(n\), all prime powers, and arbitrary algebraically closed fields rest on the proof above.

Run `python verify.py` using Python 3 with no external dependencies; success ends with `VERIFY_OK`.

## Relationship to prior work

Bleher, Chinburg and Huisgen-Zimmermann (2014, arXiv:1407.3045, especially the local one-loop discussion preceding their Theorem 3.12) establish that the *ordinary* representation variety of \(k[t]/(t^2)\), namely the reduced locus \(A^2=0\) over a field, is irreducible. The present first-order lift locus is different: it retains first-order data from the original quadratic relations, and every possible reduction rank becomes a component of the same dimension. Thus the new component count is **not** a rephrasing of the cited base-variety component count.

Huisgen-Zimmermann (2014, arXiv:1410.3166) likewise treats representation varieties of local truncated path algebras over a field, not all lifts over a nonreduced coefficient ring. Moreau and Yu (2015, arXiv:1411.6427) study jets of *reduced nilpotent orbit closures* over characteristic zero. The reduced variety of square-zero matrices and the relation-defined (usually nonreduced) scheme \(A^2=0\) need not have the same first jet: for instance, all \(B\in M_n(k)\) appear over the zero reduction in the latter. Their general results do not state the all-rank component count or the finite-field lift enumerator here.

Related published mathematical records for dual-number matrices address the nilpotency index of lifts of an individual regular Jordan block and the census of strongly nil-clean matrices. A fixed regular Jordan reduction (typically not square-zero when \(n>2\)) and a different decomposition property do not determine the complete first-order square-zero locus. No stronger theorem was located in the checked material, but an unindexed full classification may exist.

## Limitations

The theorem classifies the **reduced support** of the first-order-lift scheme and its labeled rational points, not its scheme-theoretic multiplicities, local equations for each minimal prime, full singular loci, or conjugacy orbits of pairs. The component closures are characterized intrinsically as closures of rank strata, rather than supplied with explicit generating ideals. The proof is mathematical; the enumerations for small fields do not certify the general result. Novelty is assessed against the identified literature and records, not asserted as globally proven uniqueness.

## References

1. F. M. Bleher, T. Chinburg, B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045 (first public version 2014-07-11), especially Section 3 and Theorem 3.12. https://arxiv.org/abs/1407.3045
2. B. Huisgen-Zimmermann, *Irreducible components of varieties of representations I. The local case*, arXiv:1410.3166 (first public version 2014-10-12), introduction and local one-loop discussion. https://arxiv.org/abs/1410.3166
3. A. Moreau and R. W. T. Yu, *Jet schemes of the closure of nilpotent orbits*, arXiv:1411.6427 (first public version 2014-11-24), introduction and jet-scheme definitions. https://arxiv.org/abs/1411.6427
