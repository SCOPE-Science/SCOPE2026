# Zariski-chamber spectrum of the one-nodal cubic's minimal resolution

## Finding

Let \(k\) be an algebraically closed field of arbitrary characteristic, and let \(X\) be the blow-up of \(\mathbb P^2_k\) at **any six pairwise distinct points on a smooth conic**. Thus \(X\) is a weak del Pezzo surface of degree three, whose anticanonical model is a cubic surface with one ordinary double point (type \(A_1\)). Let \(z_r(X)\) be the number of Zariski chambers of the big cone whose negative part has exactly \(r\) distinct irreducible components; the nef chamber corresponds to \(r=0\).

The complete support-size enumerator is
\[
\boxed{\sum_{r\ge0}z_r(X)t^r=1+22t+156t^2+490t^3+725t^4+447t^5+57t^6.}
\]
In particular, the **total number of chambers** is \(\boxed{z(X)=1898}\), independent of the positions of the six points along the conic, and there are no chambers with more than six negative components. Exactly \(648\) chambers have the strict transform of the conic in their negative support. For comparison, the classical smooth cubic surface has \(2764\) chambers, so this one-nodal degeneration has \(866\) fewer.

## Assumptions and scope

A Zariski chamber is counted by its distinct negative support in the Zariski decomposition of a big real divisor class, following Bauer–Funke–Neumann (2009, Proposition 1.1). The base field is algebraically closed; no genericity is assumed beyond six distinct points on a smooth conic. The theorem is about the **smooth minimal resolution** \(X\), not the singular cubic itself. Every chamber is counted once, including the nef chamber. Arithmetic on a nonclosed field and volumes of chambers are not asserted.

Write \(H\) for the pullback of a line, \(E_i\) for the six exceptional curves (\(1\le i\le6\)), \(L_{ij}=H-E_i-E_j\) for the strict transform of the line through points \(i,j\), and \(Q=2H-\sum_{i=1}^6 E_i\) for the strict transform of the conic. The intersection form in \((H,E_1,\ldots,E_6)\) is \(\operatorname{diag}(1,-1,-1,-1,-1,-1,-1)\).

## Proof

**1. There are precisely 22 negative curves.** The canonical class is \(K_X=-3H+\sum_iE_i\), so \((-K_X)^2=3\). For every exceptional \(E_i\), \((-K_X)\cdot E_i=1\). For the strict conic \(Q\), \((-K_X)\cdot Q=0\). Any other irreducible nonexceptional curve is the proper transform of a plane curve of degree \(d\ge1\) with multiplicities \(m_i\) at the six points. Bézout with the smooth conic, which is not a component, gives \(\sum_i m_i\le2d\), hence
\[
(-K_X)\cdot C=3d-\sum_i m_i\ge d>0.
\]
Thus \(-K_X\) is nef and big. If an irreducible curve \(C\) satisfies \(C^2<0\), adjunction and \(p_a(C)\ge0\) give
\[
-2\le C^2+K_X\cdot C=C^2-(-K_X\cdot C).
\]
Since \((-K_X)\cdot C\ge0\), this forces either \((C^2,(-K_X)\cdot C)=(-2,0)\) or \((-1,1)\); the other possibilities are excluded by the integer parity in adjunction. For a nonexceptional curve different from \(Q\), the Bézout inequality yields \(1=(-K_X)\cdot C\ge d\), hence \(d=1\) and \(\sum_i m_i=2\). No three distinct points on a smooth conic are collinear, so the curve must be exactly one of the \(15\) lines \(L_{ij}\). The only \((-2)\)-curve is \(Q\), and the other \((-1)\)-curves are the six \(E_i\). This establishes the complete negative-curve list without a generic-position assumption.

**2. Negative-definite support criterion.** The intersection products for distinct curves are
\[
E_i\cdot E_j=0,\qquad E_i\cdot L_{jk}=\begin{cases}1&i\in\{j,k\},\\0&\text{otherwise},\end{cases}\qquad
Q\cdot E_i=1,\qquad Q\cdot L_{jk}=0,
\]
\[
L_{ij}\cdot L_{kl}=\begin{cases}0&|\{i,j\}\cap\{k,l\}|=1,\\1&\{i,j\}\cap\{k,l\}=\varnothing.\end{cases}
\]
All \(21\) curves \(E_i,L_{ij}\) have self-intersection \(-1\), while \(Q^2=-2\). A negative-definite matrix cannot contain two distinct \((-1)\)-curves with positive mutual intersection: the corresponding \(2\times2\) matrix is already nonnegative or indefinite. Conversely, a set of pairwise disjoint \((-1)\)-curves has negative-definite diagonal intersection matrix. If the root \(Q\) is also selected, the Schur complement of the diagonal \((-1)\)-block is \(-2+s\), where \(s\) is the number of selected \(E_i\). Thus the full matrix is negative definite exactly when those \((-1)\)-curves are pairwise disjoint **and** \(s\le1\). By the standard Zariski-chamber correspondence, every such support occurs for a big divisor, and no others do. A direct proof of the existence direction is obtained by choosing an ample divisor \(A\), solving \((A+\sum a_iC_i)\cdot C_j=0\) on a negative-definite support, and adding sufficiently large positive multiples of the \(C_i\) to obtain a big divisor with precisely that negative part.

**3. Closed-form combinatorial enumeration.** Choose \(s\) exceptional curves among the six, and exclude their labels from all allowable line pairs. On the remaining \(r=6-s\) labels, the selected curves \(L_{ij}\) are pairwise disjoint if and only if the corresponding edges of the complete graph \(K_r\) are pairwise intersecting. For \(r\ge2\), let
\[
F_r(t)=1+\binom r2t+r\sum_{j=2}^{r-1}\binom{r-1}j t^j+\binom r3t^3,
\]
and set \(F_0(t)=F_1(t)=1\). This counts all intersecting edge families: a singleton has \(\binom r2\) choices; a family of at least two edges either forms a star with a unique center, or is the three edges of a triangle. Stars and triangles are disjoint cases, so no overcount occurs.

By the support criterion of Step 2, the complete generating polynomial is
\[
Z_X(t)=\underbrace{\sum_{s=0}^{6}\binom6s t^sF_{6-s}(t)}_{\text{supports omitting }Q}
+\underbrace{tF_6(t)+6t^2F_5(t)}_{\text{supports containing }Q}.
\]
The first summand expands to
\[
1+21t+135t^2+370t^3+465t^4+237t^5+21t^6,
\]
and the second to
\[
t+21t^2+120t^3+260t^4+210t^5+36t^6.
\]
Adding them gives the asserted seven coefficients, their total \(1898\), and the \(Q\)-support subtotal \(648\). The exponent is bounded by six because the Picard intersection form has signature \((1,6)\), and the explicit polynomial attains that bound. The known count \(2764\) for six points in general position is Theorem 1 of Bauer–Funke–Neumann (2009), not part of the priority claim here.

## Verification

The self-contained program `verify_chambers.py` builds the \(22\) curve classes as integral vectors in the \((1,6)\)-signature Picard lattice. It exhaustively checks every principal subset of cardinality at most six, using exact integer fraction-free determinants and Sylvester's criterion, and independently compares the result with the graph-theoretic generating-function formula. The output is stored in `verification_output.txt`, with final marker `NEGATIVE_DEFINITE_ENUMERATION_OK`. In particular the exact algorithm obtains \((1,22,156,490,725,447,57)\) and subtotal \(648\). Enumerating only sizes at most six is **exhaustive** by the Hodge index theorem, not an arbitrary experimental cutoff. The stand-alone program checks the lattice arithmetic and counting; the argument for the complete negative-curve list and its independence of point positions is the mathematical proof in Steps 1–3.

## Relationship to prior work

Bauer, Funke and Neumann (2009) establish the chamber/support correspondence and the total \(2764\) for an ordinary smooth cubic surface (six *general-position* blowup points). Their source does not treat the case when all six points lie on a conic. Bauer and Schmitz (2012) give an improved general negative-principal-minor algorithm and calculate a different high-Picard-number example, the Segre–Schur quartic; no one-nodal cubic chamber spectrum is stated there. Derenthal, Joyce and Teitler (2007) classify the relevant generalized del Pezzo geometry and compute **nef-cone volumes**, which are a distinct invariant; their results imply that the one-nodal case fits the usual weak del Pezzo framework, but do not supply its chamber counts. Later work of Brodie and Constantin (2024) develops Zariski/cohomology chambers for generalized del Pezzo surfaces as a class and reports numbers for toric and ordinary del Pezzo examples, without listing the exact polynomial above for the non-toric \(A_1\) degree-three type.

The contribution is the exact, characteristic-independent support-size spectrum for this natural singular cubic degeneration, including the explicit star/triangle classification and the \((-2)\)-root contribution. It is not a new definition of Zariski chambers or a replacement for the existing general enumeration algorithms.

## Limitations

The result counts chambers but does not compute their volumes, the full walls or generators of every chamber, or analogous spectra for other ADE types. A successful exact enumeration is not a proof of historical novelty. Specialist tables or unpublished classifications of weak del Pezzo chamber numbers may provide an equivalent result; historical priority warrants independent review. No independent scientific audit was performed.

## References

1. U. Derenthal, M. Joyce, Z. Teitler, *The nef cone volume of generalized Del Pezzo surfaces*, arXiv:math/0703202 (first public 2007-03-07), §§1,3–5. https://arxiv.org/html/math/0703202v2
2. T. Bauer, M. Funke, S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958 (first public 2009-12-04), Proposition 1.1, Theorem and §3. https://arxiv.org/html/0912.0958v1
3. T. Bauer, D. Schmitz, *Zariski chambers on surfaces of high Picard number*, arXiv:1204.4373 (first public 2012-04-19), Proposition 1.1 and §§1–3. https://arxiv.org/abs/1204.4373
4. C. R. Brodie, A. Constantin, *Cohomology Chambers on Complex Surfaces and Elliptically Fibered Calabi–Yau Three-Folds* (2024), §4.3, especially the generalized del Pezzo classification. https://doi.org/10.1007/s00220-024-05055-x
