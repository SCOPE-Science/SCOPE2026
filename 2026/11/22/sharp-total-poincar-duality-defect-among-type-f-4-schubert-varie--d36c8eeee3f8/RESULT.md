# Sharp total Poincaré-duality defect among type-\(F_4\) Schubert varieties

## Finding

Let \(G\) be a simply connected complex algebraic group of type \(F_4\), \(B\) a Borel subgroup and \(W=W(F_4)\) its Weyl group. For \(w\in W\), write \(X_w=\overline{BwB/B}\), \(d=\ell(w)\), and
\[
P_w(q)=\sum_{i=0}^{d}a_i(w)q^i,\qquad
 a_i(w)=\dim_{\mathbb Q}H^{2i}(X_w;\mathbb Q).
\]
Define the *total opposite-Betti defect*
\[
T(w)=\sum_{0\le i<d/2}\bigl(a_{d-i}(w)-a_i(w)\bigr).
\]
The **sharp global maximum** over all \(1,152\) Schubert varieties is
\[
\boxed{\max_{w\in W(F_4)}T(w)=252.}
\]
Exactly **two** group elements attain it. They have length \(18\), are involutions, and are exchanged by the abstract Coxeter diagram automorphism \(s_j\mapsto s_{5-j}\). They may be represented by the reduced words `132132432132343213` and `423423123423212342` (digits give the simple-reflection indices). For either extremizer,
\[
(a_0,a_1,\ldots,a_{18})=(1,4,9,16,25,36,48,60,71,80,87,92,94,89,74,51,26,8,1),
\]
and the lower-half reverse differences are \((0,4,17,35,49,53,46,32,16)\), summing to \(252\). The next-largest value is \(249\). Among the \(1,152\) varieties, exactly \(174\) have palindromic Betti sequences. No statement about other root systems is asserted.

## Assumptions and scope

The base field is \(\mathbb C\) and the flag variety is the **full** flag variety \(G/B\), not a partial flag variety. The Cartan matrix is
\[
C=\begin{pmatrix}
2&-1&0&0\\
-1&2&-2&0\\
0&-1&2&-1\\
0&0&-1&2
\end{pmatrix}.
\]
Simple reflection \(s_k\) acts in the integral simple-root basis by \(s_k(e_j)=e_j-C_{jk}e_k\), for \(1\le j,k\le4\). The Coxeter diagram reversal is an automorphism of the *abstract Coxeter group*; it need not preserve the long/short root labels in this particular root representation. Schubert affine paving identifies \(a_i(w)\) with \(\#\{x\le w:\ell(x)=i\}\) for the strong Bruhat order. Thus the statement is independent of any singular-cohomology normalization ambiguity.

## Proof

**1. Exhaustive faithful Weyl-group construction.** Implement the four matrices \(s_k\) from \(C\) as integer \(4\)-by-\(4\) matrices. Starting with the identity, breadth-first traversal under right multiplication by the four generators yields exactly \(1,152\) distinct matrices, and records the shortest word for each. The maximum recorded word length is \(24\), attained uniquely. Independently, close the four simple roots under these matrices to obtain exactly \(48\) roots, of which exactly \(24\) are positive. For each of the \(1,152\) matrices, the number of positive roots sent to negative equals its recorded word length. This checks both faithfulness and reducedness of every enumerated expression.

**2. Exhaustive Bruhat intervals without numerical approximation.** By the Coxeter subword theorem, \(x\le w\) exactly when \(x\) is the product of a subexpression of any fixed reduced expression of \(w\). For a reduced word \(s_{i_1}\cdots s_{i_d}\), begin with the singleton mask \(M_0=\{e\}\) and iterate
\[
M_{k+1}=M_k\cup\{xs_{i_{k+1}}:x\in M_k\},\qquad 0\le k<d.
\]
Induction on \(k\) proves that \(M_d\) contains *every and only* subexpression product, not just reduced subexpressions. Deduplication is exact by integer matrix identity. Counting \(\ell(x)\) for each \(x\in M_d\) yields the entire vector \((a_0,\ldots,a_d)\) for every one of the \(1,152\) elements. As a global independent numerical consistency check, the polynomial for the unique longest element equals
\[
P_{w_0}(q)=[2]_q[6]_q[8]_q[12]_q,\qquad [r]_q=1+q+\cdots+q^{r-1},
\]
where the factors arise from the exponents \(1,5,7,11\) of \(F_4\).

**3. Optimization and equality.** Compute the exact integer \(T(w)\) from each fully enumerated vector. The attached dependency-free program `verify_f4.py` enumerates all \(1,152\) elements with *no early stopping* and asserts: all reverse-minus-forward differences on the lower half are nonnegative; the maximal \(T\) is \(252\); its equality set has cardinality two and consists entirely of length-\(18\) elements; and the next-largest value is \(249\). It reconstructs the matrix of `132132432132343213` and of its diagram reversal, verifies that they are the two distinct maximizers, verifies that both square to the identity, and checks their complete Betti vectors above. Finally it counts exactly \(174\) palindromic polynomials. Every loop range is finite and exhaustively traversed, so the computation is a proof of this finite classification, not merely sampling.

## Verification

Run `python3 verify_f4.py` using Python 3 standard library only. The script asserts the full Weyl enumeration, independent root-length counts, full Bruhat interval construction, longest-element exponent-product identity, the two extremizers, involutivity, diagram reversal, and the exact coefficient vector and maximum. All arithmetic is integral. The accompanying checker is a complete executable specification of the finite enumeration and uses no downloaded data or external computation package. In the checked environment it finished and printed five `PASS`-or-witness lines. A separately implemented library-level Bruhat enumeration is not claimed; the root-length and longest-element checks are independent sanity checks on a single enumeration implementation.

## Relationship to prior work

Li, Rietsch and Yang (arXiv:2506.18388, 23 June 2025, primary MSC 14M15) relate degree-one and codimension-one Betti numbers to \(\mathbb Q\)-factoriality in Schubert varieties, especially distinguishing simply-laced from nonsimply-laced types. Their criteria do not determine the full Betti-vector reversal distance or its extremizers in type \(F_4\). Sentinelli and Zatti (arXiv:2509.20981, first submitted September 2025, section 4) construct weak Lehmer codes producing *any individual* lower-Bruhat-interval rank-generating polynomial in type \(F_4\), and classify its palindromic polynomials. Their algorithm is a more general computational framework for the component data, so the new result does **not** claim an algorithm for individual Betti vectors or the palindromic classification. Their full text does not report the sharp global total defect, its two-element equality set, or involutive rigidity. The exact new assertion concerns a motivated extremal invariant across all Schubert varieties, not the existence of Bruhat ranks. Burrull, Li, Zeng and Zhang (arXiv:2611.24751, 18 November 2026) separately introduce asymmetry polynomials and obtain bounds in selected type-\(A\)/\(B\) Kazhdan–Lusztig strata; this related study concerns different Weyl types and is not used as an originating source for this finding. The present global extremum over all type-\(F_4\) elements is not stated there.

## Limitations

The classification uses a finite exact exhaustive computation rather than a short conceptual explanation of why these two involutions maximize the defect. The result is limited to full-flag type \(F_4\) over \(\mathbb C\). Published algorithms for individual interval rank counts imply that the requisite data are computable; the new contribution is the sharp optimized value and equality classification, not a new Bruhat algorithm or smoothness criterion. An equivalent unindexed table or computation cannot be ruled out. There has been no independent audit beyond this reproducible exact checker and the documented scientific comparison.

## References

- C. Li, K. Rietsch and M. Yang, *An anticanonical perspective on \(G/P\) Schubert varieties*, arXiv:2506.18388v1 (23 June 2025), https://arxiv.org/html/2506.18388v1.
- P. Sentinelli and A. Zatti, *A weak Lehmer code for type \(F_4\)*, arXiv:2509.20981v2, https://arxiv.org/html/2509.20981v2.
- G. Burrull, Z. A. Li, S. Zeng and X. Zhang, *On the asymmetry polynomial of Schubert varieties*, arXiv:2611.24751 (18 November 2026), https://arxiv.org/html/2611.24751v1 (related comparison).
- Standard Bruhat subword theorem and \(F_4\) Coxeter exponent formula, as recalled in Sentinelli–Zatti, section 2.
