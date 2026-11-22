# Prescribed commutator fibers of rank-one matrix sandwich semigroups

## Finding

Let \(k=\mathbb F_q\) be any finite field; let \(m,n\ge2\), and fix a rank-one matrix \(A\in M_{n\times m}(k)\). Endow \(S=M_{m\times n}(k)\) with the associative sandwich product \(X\star Y=XAY\). For each \(Z\in S\), define the ordered commutator fiber

\[
F_A(Z)=\#\{(X,Y)\in S^2:XAY-YAX=Z\}.
\]

Put \(\alpha=m-1\), \(\beta=n-1\), \(h=\alpha\beta\), \(G_q=|\operatorname{GL}_2(k)|=q(q-1)(q^2-1)\), and \(H_q=|\operatorname{SL}_2(k)|=q(q^2-1)\). The following table is the **complete prescribed-nonzero-target fiber law**. Here \(0\) and \(+\) mean, respectively, that the indicated matrix product vanishes or does not vanish; whenever \(A Z\) and \(Z A\) are both nonzero, the row marked rank two also requires \(A Z A=0\).

| \(\operatorname{rank}Z\) | \(A Z\) | \(Z A\) | Additional requirement | \(q^{-2h}F_A(Z)\) | Number of such nonzero targets |
|---|---|---|---|---|---|
| \(1\) | \(0\) | \(0\) | none | \((q^2-1)(q^\alpha+q^\beta-q)\) | \((q^\alpha-1)(q^\beta-1)/(q-1)\) |
| \(1\) | \(0\) | \(+\) | none | \((q^2-1)q^\alpha\) | \((q^\alpha-1)q^\beta\) |
| \(1\) | \(+\) | \(0\) | none | \((q^2-1)q^\beta\) | \(q^\alpha(q^\beta-1)\) |
| \(2\) | \(0\) | \(0\) | none | \(G_q\) | \((q^\alpha-1)(q^\alpha-q)(q^\beta-1)(q^\beta-q)/G_q\) |
| \(2\) | \(+\) | \(+\) | \(A Z A=0\) | \(H_q\) | \(q^{\alpha+\beta-1}(q^\alpha-1)(q^\beta-1)\) |

**Every other nonzero target has an empty fiber.** The rank-two \((0,0)\) row is absent when \(\min(m,n)=2\). Thus the commutator image and the complete nonzero fiber multiplicities are explicitly determined, with a genuine \(\operatorname{GL}_2/\operatorname{SL}_2\) split of rank-two fibers. The nonzero target values depend only on rank and the two-sided annihilator predicates in the table, not on the individual matrix entries.

For completeness the zero fiber is the earlier established commuting-pair count

\[
F_A(0)=q^{2h}\left[q^{\alpha+\beta+1}+q^{\alpha+\beta+2}-(q+1)(q^\alpha+q^\beta)+q+q^{2\alpha}+q^{2\beta}\right].
\]

That zero-target formula, and the global rank histogram obtained by summing target fibers, were already known and are **not** claimed as new here.

## Assumptions and scope

All matrices are over the same finite field \(k\); no characteristic restriction is imposed, including characteristic two. The product is ordinary rectangular matrix multiplication with fixed middle matrix \(A\). The target \(Z\) is fixed **before** counting ordered pairs, not merely fixed up to rank or similarity. Every matrix, regular or singular, is admitted for \(X\) and \(Y\). All ranks are ordinary linear-map ranks. Changing bases simultaneously on the left and right transports \(A\), \(X\), \(Y\), and \(Z\), and preserves all fiber sizes and predicates; hence one may take \(A=E_{11}\). The source matrix \(A\) need not be an idempotent, since it is generally rectangular.

## Proof

**1. Rank-one reduction and a constrained two-factor product.** Invertible independent changes of the outer vector-space bases reduce \(A\) to the matrix with its only nonzero entry at \((1,1)\). Write each \(X\in S\) with first column \(x\in k^m\) and first row \(r\in k^{1\times n}\), where their first entries agree. For a pair \(X,Y\), put

\[
U=[x\ y]\in M_{m\times2}(k),\qquad
V=\begin{bmatrix}r\\s\end{bmatrix}\in M_{2\times n}(k),\qquad
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

The first row of \(U\) is \(t=(a,b)\) and the first column of \(V\) is \(t^\mathsf T\), for the same pair \(a=X_{11},b=Y_{11}\). The commutator is exactly \(Z=UJV\), so \(Z_{11}=tJt^\mathsf T=0\). Conversely, every such pair of \(U,V\) with the shared first two scalars determines first rows and columns of \(X,Y\); the two bottom-right \(\alpha\times\beta\) blocks may be freely chosen. Thus each factorization counted below lifts to precisely \(q^{2h}\) ordered matrix pairs. Because \(J\) is invertible, the output has rank at most two in every characteristic.

**2. Rank-two targets whose first row and column both vanish.** These have \(t=0\): since both \(U\) and \(V\) have rank two, a nonzero \(t\) would force the first row \(tJV\) and the first column \(UJt^\mathsf T\) to be nonzero. Therefore the factorization occurs solely in the lower-right \(\alpha\times\beta\) block, as \(U'JV'=Z'\), with \(U'\) and \(V'\) both rank two. Every rank-two matrix has exactly \(G_q\) such full-rank two-factor representations: choose an isomorphism from \(k^2\) to its column space, and the second factor is then unique. This also explains why the row cannot occur when \(\alpha<2\) or \(\beta<2\).

**3. Rank-two targets with both first row and first column nonzero.** The shared row \(t\) must be nonzero. Fix any ordinary full-rank factorization \(Z=U_0V_0\) through \(k^2\). Let \(u\ne0\) be the first row of \(U_0\) and \(v\ne0\) the first column of \(V_0\). Necessarily \(uv=Z_{11}=0\). In dimension two there is a unique \(\delta\in k^\times\) such that \(v=\delta Ju^\mathsf T\). Every factorization \(Z=UJV\) is uniquely of the form

\[
U=U_0T,\qquad V=J^{-1}T^{-1}V_0,\qquad T\in\operatorname{GL}_2(k).
\]

Its first row and column agree in the required sense exactly when

\[
J^{-1}T^{-1}v=(U_0T)_{1,*}^{\mathsf T}
\quad\Longleftrightarrow\quad\det T=\delta,
\]

using the two-dimensional identity \(J^{-1}T^{-1}J=T^{\mathsf T}/\det T\). There are exactly \(H_q\) matrices with that determinant. Thus every rank-two target with \(Z_{11}=0\) and both axes nonzero has exactly \(q^{2h}H_q\) witnesses. If just one axis vanishes, full row and column ranks would force the shared \(t\) to be simultaneously zero and nonzero, so the fiber is empty.

**4. Rank-one targets with both axes zero.** Again \(t=0\). Choose one fixed ordinary factorization \(Z'=uv^\mathsf T\ne0\) of the lower-right block. Count \(Z'=U'W\) with \(U'\in M_{\alpha\times2}(k)\) and \(W\in M_{2\times\beta}(k)\); multiplying \(W\) by \(J^{-1}\) establishes a bijection with the original expression. If \(\operatorname{rank}U'=1\), then \(U'=ua^\mathsf T\) for \(a\in k^2\setminus\{0\}\), and each column of \(W\) satisfies one linear condition, giving \((q^2-1)q^\beta\) possibilities. If \(\operatorname{rank}U'=2\), its image is a two-plane containing \(u\), and there are \({\alpha-1\brack1}_qG_q=(q^2-1)(q^\alpha-q)\) choices of \(U'\); \(W\) is then uniquely determined. Adding the two disjoint cases gives \((q^2-1)(q^\alpha+q^\beta-q)\).

**5. Rank-one targets with exactly one zero axis.** Suppose the first row is zero and the first column is nonzero, and write the target uniquely as \(Z=cw^\mathsf T\) where \(c=Z_{*,1}\ne0\), \(c_1=0\), and \(w_1=1\). Now \(t\ne0\), and \(tJV=0\) forces \(V=t^\mathsf T w^\mathsf T\). The remaining equation \(UJt^\mathsf T=c\) supplies one nontrivial linear condition on each of the \(\alpha\) lower rows of \(U\); its top row is already \(t\). Thus there are \((q^2-1)q^\alpha\) constrained factorizations. Transposing and exchanging the left and right roles gives \((q^2-1)q^\beta\) when the first column, rather than the first row, vanishes. Rank one cannot have nonzero first row and first column while \(Z_{11}=0\).

**6. Counts of targets.** Write every nonzero rank-one target as \(uv^\mathsf T\), dividing the number of nonzero vector-pairs by the scaling factor \(q-1\). Requiring both distinguished coordinates zero yields \((q^\alpha-1)(q^\beta-1)/(q-1)\). Requiring exactly one distinguished coordinate zero yields the two numbers in the table. The rank-two zero-axis count is the ordinary number of rank-two \(\alpha\times\beta\) matrices, namely the displayed quotient by \(G_q\). For the final row count factorizations with nonzero \(t\) and full ranks of \(U,V\): there are \((q^2-1)(q^{2\alpha}-q^\alpha)(q^{2\beta}-q^\beta)\) such pairs. Every resulting target has exactly \(H_q\) such factorizations by Step 3, so dividing gives \(q^{\alpha+\beta-1}(q^\alpha-1)(q^\beta-1)\). This proves the output counts and exhaustiveness of the table.

For completeness, the zero-target formula is a previously published centralizer sum: the rank-one sandwich algebra is (after basis changes) the rectangular-band algebra; its commutator-zero fiber is the full commuting-pair count of that algebra. It also follows directly by setting \(UJV=0\) and separating the possible first-column and first-row vanishings. This known zero fiber is stated to complete the data but plays no role in the novelty claim.

## Verification

`checker.py` constructs finite fields by exact arithmetic, including the degree-two extension \(\mathbb F_4\), enumerates **all** pairs of matrices and directly evaluates each commutator entry from \(XAY-YAX\), and compares **every single target** against the complete predicted fiber function. The eight exhaustive cases \((m,n,q)=(2,2,2),(2,3,2),(3,2,2),(3,3,2),(2,4,2),(2,2,3),(2,3,3),(2,2,4)\) covered up to \(531441\) ordered pairs in one case. Every comparison passed, and the sum of predicted fiber sizes equals \(q^{2mn}\) in each instance. The terminal marker is `SANDWICH_PRESCRIBED_COMMUTATOR_FIBERS_VERIFIED`. These finite checks are corroboration; Steps 1–6 prove the statement in all finite-field sizes and dimensions allowed above.

## Relationship to prior work

Dolinka and East's 2015 study of matrix sandwich semigroups supplies the classical rectangular matrix product and its idempotent structure, not a prescribed **commutator-target** fiber distribution. Dolinka, East and Ruškuc's 2024 study of transformation variants motivates the focus on rank-controlled sandwich products and semigroup invariants, but studies congruences of a different transformation-semigroup variant rather than the present target fibers.

The published 2026 result *Commutator-rank census of finite rectangular-band semigroup algebras* establishes the **global commutator-rank histogram** and all **zero-target centralizer counts** for an isomorphic rank-one matrix sandwich algebra. These existing results are explicitly credited and not re-presented as novel. Its complete mathematical statement and proof do **not** determine how the nonzero rank-one and rank-two outputs split according to the two annihilator predicates. Its stated limitation expressly leaves prescribed nonzero matrix target fibers unresolved. The present classification supplies those finer data. The published *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups* treats only pairs of idempotents commuting at zero target; it does not cover arbitrary ordered matrices with a prescribed nonzero bracket.

For conceptual comparison, the new rank-two factorization depends on a fixed determinant fiber in \(\operatorname{GL}_2(k)\), producing \(|\operatorname{SL}_2(k)|\), whereas outputs annihilated on both sides have the full \(|\operatorname{GL}_2(k)|\) fiber. A rank-only histogram cannot distinguish these two target types. Relevant published works on prescribed brackets for unrelated Lie algebras concern different product laws and do not imply the statement by a known reduction.

## Limitations

The sandwich rank is exactly one, and dimensions \(m,n\ge2\); the theorem makes no claim for higher-rank sandwich matrices. This is an **ordered** finite-field fiber census, not a classification up to algebra automorphism, nor a scheme-theoretic classification of fibers. Independent mathematical validation and exhaustive historical-priority verification have not been performed. Equivalent formulations could exist in older homotope, Munn-ring, or Rees-algebra literature; no claim is made that the displayed formulas are historically first beyond the specifically inspected sources.

## References

1. I. Dolinka and J. East, *Semigroups of rectangular matrices under a sandwich operation*, arXiv:1503.03139, first posted 2015-03-11, especially Sections 5–7. https://arxiv.org/abs/1503.03139
2. I. Dolinka, J. East and N. Ruškuc, *Congruences of maximum regular subsemigroups of variants of finite full transformation semigroups*, arXiv:2403.05191v1, first posted 2024-03-08. https://arxiv.org/abs/2403.05191
3. *Commutator-rank census of finite rectangular-band semigroup algebras*, published 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-commutator-rank-census-of-finite-rectangular-band-semigroup-alge--6f0f9b3726a9
4. *Joint matrix-rank spectrum of commuting idempotents in rectangular sandwich semigroups*, published 2026-10-13, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-joint-matrix-rank-spectrum-of-commuting-idempotents-in-rectangul--85aa4c5711c9
