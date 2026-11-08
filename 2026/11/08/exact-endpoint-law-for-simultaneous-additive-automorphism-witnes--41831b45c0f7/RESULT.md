# Exact endpoint law for simultaneous additive automorphism witnesses in finite abelian \(p\)-groups

## Finding

Let \(p\) be any prime and let \(A\ne0\) be a finite abelian \(p\)-group with its distinct elementary-divisor exponents displayed as
\[
 A=\bigoplus_{j=1}^{s}(\mathbb Z/p^{e_j}\mathbb Z)^{m_j},\qquad
 1\le e_1<\cdots<e_s,\quad m_j\ge1.
\]
Write \(r=|\{j:m_j=1\}|\) and \(k=p-1\). Independently sample \(k\) automorphisms \(\beta_1,\ldots,\beta_k\) uniformly from \(\operatorname{Aut}(A)\). Say that this tuple has an *additive automorphism witness* if there is an \(\alpha\in\operatorname{Aut}(A)\) such that \(\alpha+\beta_i\in\operatorname{Aut}(A)\) for every \(i\). (Addition is pointwise addition of homomorphisms.) Then the exact probability is
\[
 \boxed{\Pr(\text{a witness exists})=
 \left(1-\frac{(p-1)!}{(p-1)^{p-1}}\right)^r.}
\]
The expression with exponent zero is interpreted as one. In particular, **every** \(k\)-tuple has an additive automorphism witness if and only if **each elementary-divisor exponent occurs with multiplicity at least two**, that is, \(r=0\). For any smaller positive \(k'<p-1\), every \(k'\)-tuple has such a witness regardless of the multiplicities.

More precisely, let \(\pi:\operatorname{End}(A)\to\prod_{j=1}^s M_{m_j}(\mathbb F_p)\) be reduction to the diagonal elementary-divisor blocks. For any tuple of \(k\) automorphisms, set \(A_{ij}=\pi_j(\beta_i)\) and
\[
 N_m(B_1,\ldots,B_k)=
 |\{U\in\operatorname{GL}_m(\mathbb F_p):
       \det(U+B_i)\ne0\text{ for all }i\}|.
\]
The **exact number** of additive automorphism witnesses is
\[
 \boxed{p^{E-\sum_jm_j^2}
       \prod_{j=1}^{s}N_{m_j}(A_{1j},\ldots,A_{kj}),\qquad
 E=\sum_{j,\ell=1}^{s}m_jm_\ell\min(e_j,e_\ell).}
\]
For every \(m\ge2\) and every \(k\le p-1\), the factor \(N_m\) is strictly positive. For \(m=1\), it is \(p-1-|\{A_{11},\ldots,A_{k1}\}|\), with the corresponding block indices understood. Thus the endpoint probability depends only on the count \(r\) of singleton multiplicities, **not** on the exponents or the higher multiplicities.

## Assumptions and scope

All groups are finite, nontrivial and abelian; \(p\) is prime, with characteristic two included. Automorphism tuples are ordered and sampled independently with replacement. The word "witness" means a group automorphism, **not** an arbitrary permutation. The original simultaneous complete-mapping property allowing arbitrary bijections is a different, weaker requirement and is not settled here for groups with \(r>0\).

## Proof

**1. The reduction and its fibers.** For cyclic summands of exponents \(e_j,e_\ell\), the number of homomorphisms between them is \(p^{\min(e_j,e_\ell)}\). Consequently, \(|\operatorname{End}(A)|=p^E\). Order the summands by exponent. Endomorphism matrices reduced modulo \(p\) are block triangular: maps from a shorter cyclic summand to a longer one have the forced divisibility \(p^{e_\ell-e_j}\) in the longer target. Their diagonal blocks give a surjective ring homomorphism
\[
 \pi:\operatorname{End}(A)\twoheadrightarrow
 \prod_{j=1}^{s}M_{m_j}(\mathbb F_p).
\]
Surjectivity follows by lifting each prescribed diagonal matrix to a block diagonal endomorphism. An endomorphism is invertible if and only if every diagonal block of its reduction is invertible: a block-triangular matrix is invertible on \(A/pA\) precisely in that case, and surjectivity on \(A/pA\) lifts to surjectivity on the finite \(p\)-group \(A\) (equivalently, apply Nakayama's lemma). Every fiber of \(\pi\) has \(p^{E-\sum_jm_j^2}\) members. Restricted to automorphisms, the induced map onto \(\prod_j\operatorname{GL}_{m_j}(\mathbb F_p)\) has the same constant fiber cardinality.

For a proposed \(\alpha\), all \(\alpha+\beta_i\) are automorphisms if and only if the independent diagonal choices \(U_j=\pi_j(\alpha)\) lie in the sets counted by \(N_{m_j}\). Multiplying these cardinalities and the constant lift count proves the exact witness-number formula.

**2. Noncyclic blocks never obstruct at the endpoint.** Fix \(m\ge2\) and \(B_1,\ldots,B_k\in\operatorname{GL}_m(\mathbb F_p)\) with \(k\le p-1\). For a fixed \(B_i\), the bad matrices \(U\in\operatorname{GL}_m\) for which \(U+B_i\) is singular are equinumerous with the matrices \(C\in\operatorname{GL}_m\) having eigenvalue one, by \(C=-UB_i^{-1}\). Let \(H=|\operatorname{GL}_m(\mathbb F_p)|\), and let \(b\) be the number of such \(C\). Count pairs \((C,v)\) with \(0\ne v\in\mathbb F_p^m\) and \(Cv=v\). Transitivity on nonzero vectors shows there are exactly \(H\) pairs. Each of the \(b\) matrices contributes at least \(p-1\) pairs, while the identity contributes an additional \(p^m-p\). Hence
\[
 H\ge (p-1)b+p^m-p>(p-1)b.
\]
Therefore fewer than \(H/(p-1)\) possible \(U\)'s are excluded by any one \(B_i\). The union of at most \(p-1\) bad sets is still smaller than \(H\), and \(N_m(B_1,\ldots,B_k)>0\).

**3. Singleton blocks are occupancy problems.** For \(m=1\), the diagonal choices are \(U\in\mathbb F_p^\times\). The \(i\)-th translate is invertible exactly when \(U\ne-B_i\); hence \(N_1=p-1-|\{B_1,\ldots,B_k\}|\). At \(k=p-1\), this is positive unless the \(B_i\)'s enumerate the entire multiplicative group \(\mathbb F_p^\times\). Because the surjection \(\operatorname{Aut}(A)\twoheadrightarrow\prod_j\operatorname{GL}_{m_j}(\mathbb F_p)\) has equal-sized fibers, the singleton diagonal coordinates of independently uniform automorphisms are independent uniform samples in \(\mathbb F_p^\times\). For each singleton block the probability that all \(p-1\) sampled values are distinct is \((p-1)!/(p-1)^{p-1}\). These obstructions are independent across the \(r\) singleton blocks. Noncyclic blocks never obstruct by Step 2, proving the probability formula. When \(k'<p-1\), no singleton block can be exhausted, proving universal existence below the endpoint.

**4. Universal criterion and sharpness.** If \(r=0\), all blocks have dimension at least two and Step 2 supplies a witness for every tuple. If \(r\ge1\), choose \(p-1\) automorphisms whose corresponding scalar components on one singleton block run through \(\mathbb F_p^\times\), lifting arbitrary diagonal blocks on other components. No \(\alpha\) works. This proves the if-and-only-if statement.

**5. Threshold consequences.** Set \(\delta_p=(p-1)!/(p-1)^{p-1}\). For fixed \(p\), the success probability tends to zero as \(r\to\infty\). Stirling's formula gives \(\delta_p\sim\sqrt{2\pi(p-1)}e^{-(p-1)}\) as \(p\to\infty\); consequently, for any family with \(r\delta_p\to\lambda\in[0,\infty)\), the success probability tends to \(e^{-\lambda}\). These are consequences of the exact law, not independent claims.

## Verification

The included standalone Python program enumerates all ordered pairs of matrices in \(\operatorname{GL}_2(\mathbb F_3)\) (2,304 tuples) and all six singleton tuples over \(\mathbb F_2\), confirming that each admits a witness. It also samples 125 four-tuples in \(\operatorname{GL}_2(\mathbb F_5)\), exhaustively counts scalar occupancy for \(p=2,3,5,7\) and \(r=1,2\), and enumerates all 11,664 ordered automorphism pairs of \(C_3\oplus C_9\). In that mixed-exponent example exactly 2,916 pairs have an automorphism witness and each such pair has exactly 27 witnesses; the remaining 8,748 pairs have none. The output ends in `VERIFY_OK`. These tests are finite corroboration; Steps 1–4 prove the general theorem.

## Relationship to prior work

Loukaki's *A simultaneous variant of the Hall-Paige theorem and applications* (first public October 15, 2026; arXiv:2610.21600v1, revised October 22, 2026) introduces the simultaneous property and proves automorphism-witness existence below the threshold and at the endpoint on noncyclic homocyclic groups (Theorem 2 and Proposition 2). Its block-matrix decomposition and its finite-field avoidance lemma are important precursors, **not new contributions here**. It explicitly leaves the arbitrary-bijection endpoint question open for general noncyclic abelian \(p\)-groups. The new contribution is the **complete quantitative endpoint law** for uniformly random automorphism inputs on every finite abelian \(p\)-group, including exact witness counts by diagonal factors and the singleton-multiplicity obstruction. The random Hall–Paige theorem of Müyesser and Pokrovskiy concerns randomlike subsets and arbitrary bijections, rather than this random-tuple automorphism-witness distribution. Earlier fixed-point-free automorphism counts concern a single difference map rather than a \(p-1\)-tuple. In characteristic two, the universal automorphism-witness criterion specializes to the already known Gross fixed-point-free-automorphism criterion; this specialization is not claimed as a new result. No independently verified priority guarantee is asserted.

## Limitations

No conclusion is made about the existence of a nonlinear permutation witness in cases where the automorphism witness is obstructed. The block-factor formula is explicit but retains finite matrix-avoidance factors \(N_m\) for \(m\ge2\); it is not a closed formula for every individual witness count. The stated probability assumes independent uniform automorphism inputs, and may fail for other input measures. Computational checks are not the proof. Historical priority under different terminology cannot be completely excluded.

## References

1. M. Loukaki, *A simultaneous variant of the Hall-Paige theorem and applications*, arXiv:2610.21600v1 (October 15, 2026), v2 (October 22, 2026); especially Theorem 2, Proposition 2, and the block-matrix argument.
2. C. J. Hillar and D. L. Rhea, *Automorphisms of finite abelian groups*, American Mathematical Monthly 114 (2007), 917–923.
3. A. Müyesser and A. Pokrovskiy, *A random Hall-Paige conjecture*, Inventiones Mathematicae 240 (2025), 779–867.
4. *Exact counts of fixed-point-free automorphisms of finite abelian groups*, published research record, September 21, 2026 (comparison of related but distinct single-automorphism counts).
