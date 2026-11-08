# Exact dense-range congruences between two positive Hilbert-space operators

## Finding

Let \(H=\ell^2(\mathbb N)\oplus\ell^2(\mathbb N)\), with orthonormal basis \((u_m)_{m\ge1}\cup(v_n)_{n\ge1}\), and let \(K=\bigoplus_{j=0}^{\infty}\ell^2(\mathbb N)\), with orthonormal basis \((w_{j,k})_{j\ge0,k\ge1}\). Define positive frame operators by
\[
 P u_m=u_m,\qquad P v_n=n^{-1}v_n,\qquad Qw_{j,k}=2^{-j}w_{j,k}.
\]
There exist **bounded, injective, dense-range contractions** \(W:K\to H\) and \(V:H\to K\) satisfying the *exact* pullback identities
\[
 W^*PW=Q,\qquad V^*QV=P.
\]
Consequently, Bessel families with these frame operators are equivalent under the two-sided dense-range comparison relation. They are **not** equivalent under invertible comparison. In particular, dense-range comparison is strictly coarser than invertible comparison even on injective, nonclosed-range, noncompact Bessel frame operators. This resolves the specific pair and the strictness question posed in Example 1.1 and Problem 11.9 of El Idrissi's *Coarse comparison of Bessel families*.

## Assumptions and scope

All Hilbert spaces are complex or real, separable, with the displayed orthonormal bases. The positive operators \(P,Q\) are bounded, injective, noncompact and not bounded below, so they are legitimate frame operators of Bessel families: choose the columns of \(P^{1/2}\) and \(Q^{1/2}\) as families in the corresponding spaces. Dense-range comparison here requires maps in **both directions** whose ranges are dense and whose pullback frame forms are comparable; we prove equality of forms and both maps also have zero kernel. The theorem treats the two specified spectral configurations, not a classification of all dense-range comparison classes.

## Proof

**Construction from \(Q\) to \(P\).** For an integer \(n\ge1\), let \(j(n)\) be the unique least integer \(j\ge0\) satisfying \(n\le2^j\). Call \((j(n),n)\) a *special* index. The special indices are pairwise distinct, and their complement in \(\{(j,k):j\ge0,k\ge1\}\) is countably infinite (indeed, every row contains infinitely many nonspecial indices). Fix any bijection \(\mu\) from this complement onto \(\mathbb N\). Set
\[
 Ww_{j(n),n}=\sqrt{n\,2^{-j(n)}}\,v_n,
 \qquad Ww_{j,k}=2^{-j/2}u_{\mu(j,k)}\quad\text{for nonspecial }(j,k).
\]
The vectors on the right have pairwise different coordinates; every coordinate of \(H\) occurs once, with a strictly positive scalar at most one. Therefore \(W\) extends uniquely to an injective contraction with dense range. For special indices, the squared scalar times the target \(P\)-eigenvalue is \((n2^{-j(n)})(1/n)=2^{-j(n)}\). For nonspecial indices it is \(2^{-j}\cdot1=2^{-j}\). Orthogonality of the target coordinates proves \(W^*PW=Q\).

**Construction from \(P\) to \(Q\).** Every \(n\ge1\) is uniquely \(n=2^j(2k-1)\), with integers \(j\ge0\), \(k\ge1\). Define
\[
 Vu_m=w_{0,2m-1},\qquad
 Vv_{2k-1}=(2k-1)^{-1/2}w_{0,2k},
\]
\[
 Vv_{2^j(2k-1)}=(2k-1)^{-1/2}w_{j,k}
 \quad(j\ge1,k\ge1).
\]
The images occupy all coordinates of \(K\) exactly once: the odd and even positions in the zeroth row are covered by the \(u_m\) and odd-indexed \(v_n\) respectively, while the row \(j\ge1\) is covered by those \(v_n\) with exact \(2\)-adic valuation \(j\). All positive coefficients are at most one, so \(V\) is an injective contraction with dense range. For any \(n=2^j(2k-1)\), the squared scalar times the target \(Q\)-eigenvalue is \((2k-1)^{-1}2^{-j}=1/n\). On each \(u_m\) the value is one. Orthogonality gives \(V^*QV=P\).

**Failure of invertible comparison.** The operator \(P\) is a compact perturbation of the orthogonal projection \(E\) onto the first summand of \(H\). Suppose for contradiction there were a bounded invertible \(U:K\to H\) and constants \(0<c\le C<\infty\) with \(cQ\le U^*PU\le C Q\). Passing to the Calkin algebra identifies \(U^*PU\) with \(U^*EU\). This positive quotient element has zero isolated from its strictly positive spectrum: writing \(T=EU\), we have \(TT^*=EUU^*E\ge \|U^{-1}\|^{-2}E\), and the nonzero spectra of \(T^*T\) and \(TT^*\) coincide. Let \(p\) be the spectral support projection of the quotient of \(U^*PU\), and let \(\delta>0\) be its positive spectral gap. The order inequalities force the quotient \(q\) of \(Q\) to satisfy \(q=pqp\) and \(q\ge (\delta/C)p\). Thus \(q\) must also have a gap between zero and its positive spectrum. But \(Q\) has, for each \(j\ge0\), the eigenvalue \(2^{-j}\) with infinite multiplicity, so its Calkin spectrum contains all these values, which tend to zero. Contradiction. Therefore no such invertible \(U\) exists.

## Verification

The included standalone Python script `check_dense_range.py` uses only exact integers and rational arithmetic. It verifies 74,089 finite assertions about the two index assignments, scale factors, and pullback identities on representative ranges. Its outcome is `DENSE_RANGE_EXACT_CHECK_OK 74089`. The proof above, not a finite enumeration, establishes the claims for every index and the infinite-dimensional density and Calkin arguments.

To reproduce, run `python3 check_dense_range.py` in the extracted package directory; it has no external dependencies.

## Relationship to prior work

El Idrissi, *Coarse comparison of Bessel families*, arXiv:2610.39002v1, defines the comparison relations, supplies the exact pair \(P,Q\) as Example 1.1, and leaves its dense-range status as Example 8.15 and Problem 11.9. The paper establishes the failure of invertible comparison using spectral multiplicity results; the proof above also gives a direct essential-spectrum obstruction. Unlike the paper's general results about bounded, injective, isometric, Fredholm, and invertible comparison, this explicit two-way dense-range factorization answers the specific unresolved question. Douglas' classical range-inclusion lemma gives relevant general factorization context but does not by itself construct dense-range pullbacks for this pair.

## Limitations

This result does not classify arbitrary dense-range comparison classes, does not determine the category's higher invariants, and does not assert a general equivalence between dense-range and injective comparison. Earlier operator-range theory may encode an equivalent argument in a more general language; publication priority is not independently established. Independent validation has not been performed.

## References

1. N. El Idrissi, *Coarse comparison of Bessel families*, arXiv:2610.39002v1 (first posted 2026-10-28), especially Example 1.1, Theorem 6.5, Proposition 8.13, Example 8.15, and Problem 11.9. https://arxiv.org/abs/2610.39002
2. R. G. Douglas, *On majorization, factorization, and range inclusion of operators on Hilbert space*, Proc. Amer. Math. Soc. **17** (1966), 413–415. https://doi.org/10.2307/2035178
3. P. A. Fillmore and J. P. Williams, *On operator ranges*, Adv. Math. **7** (1971), 254–281. (General historical context; not used as a premise.)
