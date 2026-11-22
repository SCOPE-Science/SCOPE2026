# The first strict pairwise Davenport gap has diameter nine and a unique support

## Finding

Let \(X\subset\mathbb Z\) be finite and contain at least one positive and at least one negative integer. A *minimal zero-sum sequence* is a nonempty finite multiset of elements of \(X\) whose sum is zero and which has no proper nonempty zero-sum submultiset. Define \(D(X)\) to be its maximum possible length; let

\[
\chi(X)=\max_{-a,b\in X,\ a,b>0}\frac{a+b}{\gcd(a,b)},
\qquad \operatorname{diam}(X)=\max X-\min X.
\]

**Sharp first-gap theorem.** The least diameter of a set satisfying \(\chi(X)<D(X)\) is \(9\). Every such set of diameter exactly \(9\), up to global sign reversal, is precisely
\[
X_*=\{-6,-1,2,3\}\quad\text{or}\quad X_*\cup\{0\}.
\]
For both supports, \(\chi(X)=4\), \(D(X)=5\). Among minimal zero-sum sequences of length greater than their support's pairwise bound and span at most \(9\), the only ones are \((-6,-1,2,2,3)\) and its sign reversal.

For completeness the entire list of minimal zero-sum sequences on the four nonzero entries of \(X_*\), written as multiplicity vectors for \((-6,-1,2,3)\), is
\[
(0,2,1,0),\quad (1,0,0,2),\quad (0,3,0,1),\quad
(1,0,3,0),\quad(1,1,2,1).
\]
These have lengths \(3,3,4,4,5\) respectively. If zero is adjoined, the singleton zero is an additional atom.

## Assumptions and scope

All sets are finite subsets of the ordinary additive integers; the empty subsequence is excluded. Repetitions in zero-sum sequences are allowed, while supports are sets. A sign change acts on every member of a support and every term of a sequence. The statement is about *all* finite mixed-sign sets with diameter at most nine, not only integer intervals or sets of fixed cardinality. In an arbitrary mixed-sign support, \(\chi(X)\le D(X)\) follows from the primitive two-value sequence consisting of \(b/\gcd(a,b)\) copies of \(-a\) and \(a/\gcd(a,b)\) copies of \(b\).

## Proof

**1. A finite universal length bound.** For a minimal zero-sum sequence \(S\) with smallest term \(-m<0\) and largest term \(M>0\), arrange its terms greedily: begin with a positive term, and thereafter take a negative term when the current partial sum is positive, and a positive term when it is negative. Minimality excludes a zero partial sum before the end, and the total-sum condition guarantees a term of the needed sign is available. Every partial sum before the final zero lies in the integer interval \([1-m,M]\). The initial zero and the \(|S|-1\) nonfinal partial sums are pairwise distinct: repetition would yield a proper zero-sum submultiset. Since \([1-m,M]\) has exactly \(m+M\) integers, \(|S|\le m+M\le\operatorname{diam}(X)\). In particular, every candidate for strictness at diameter \(d\le9\) has at most \(d\) terms.

**2. Reduction to the support of a witness.** If \(S\) witnesses \(D(X)>\chi(X)\), let \(Y\) be the set of terms occurring in \(S\). Then \(\chi(Y)\le\chi(X)\), so \(|S|>\chi(Y)\), and \(\operatorname{diam}(Y)\le\operatorname{diam}(X)\). Every such nontrivial sequence contains both signs and no zeros. Thus it suffices to enumerate multisets of lengths \(2\le L\le d\), using entries of \(\{1-d,\ldots,-1,1,\ldots,d-1\}\), sorted nondecreasingly, satisfying a zero sum, both signs, \(\max S-\min S\le d\), and \(L>\chi(Y)\). These finite conditions give an exhaustive search, not a heuristic sample.

**3. Exact minimality test.** For any zero-sum multiset \(S=(s_1,\ldots,s_L)\), define the subset-sum set \(R_0=\{0\}\) and recursively \(R_j=R_{j-1}\cup (R_{j-1}+s_j)\) for \(1\le j<L\). The multiset is minimal if and only if \(0\notin R_{j-1}+s_j\) at every step \(j<L\). Indeed, any proper zero-sum subset that contains the last term has a nonempty zero-sum complement not containing the last term; hence testing only nonempty subsets of the first \(L-1\) terms suffices. This recursion enumerates all their subset sums exactly.

**4. Exhaustive bounded result.** The attached complete standalone \(\texttt{verify.py}\) implements steps 2 and 3 by exact integer enumeration. The numbers of zero-sum candidates after the sign/span filter for diameters \(2\) through \(9\) are \(1,3,9,25,79,245,809,2703\). The corresponding numbers that additionally pass strictness and minimality are \(0,0,0,0,0,0,0,2\). At \(9\), the two multisets are exactly \((-6,-1,2,2,3)\) and \((-3,-2,-2,1,6)\). As the loops range over *every* eligible sorted multiset, these checks are exhaustive finite proofs of the cutoff and of the witness classification.

**5. Exact support and Davenport value.** The opposite-sign pairs of \(X_*\) have primitive lengths \(4,3,3,4\), hence \(\chi(X_*)=4\). The five-term witness sums to zero; its positive subset sums lie in \(\{0,2,3,4,5,7\}\) and the absolute negative subset sums in \(\{0,1,6,7\}\), intersecting only at zero and at the full-sum value. Hence it is minimal. Every extra nonzero member of the containing interval \([-6,3]\) outside \(X_*\) makes some opposite-sign primitive pair longer than four (checked individually by an exact loop in the certificate). As a strict witness at diameter nine must have one of the classified supports, the only possible full sets are \(\pm X_*\) and the same sets with zero adjoined. Finally the verifier enumerates every nonzero multiplicity vector of total length at most nine over \(X_*\), and gives exactly the five vectors in the theorem, proving \(D(X_*)=5\). Adding zero only adds a singleton minimal zero-sum sequence and cannot alter the maximum.

## Verification

Run \(\texttt{python3 verify.py}\) with a standard Python 3 interpreter; no packages, input files or external databases are required. It prints every checked diameter, the number of zero-sum candidate multisets, the number of strict witnesses, and concludes \(\texttt{ALL CHECKS PASSED}\). All loops are finite, with lengths bounded by the independently proved diameter bound, and compare exact integers; no random trials, numerical tolerance or timeouts are involved.

## Relationship to prior work

Plagne and Tringali introduced the lower invariant \(\chi\) and proved \(\chi(X)\le D(X)\le\operatorname{diam}(X)\); their 2015 paper explicitly acknowledges an earlier example of strictness supplied by W. Schmid. Thus **the existence of a strict gap is not claimed as new**. Their paper's statements and inspected proofs concern the general bound and extremal interval/box sequences, not the exact *smallest possible diameter*, uniqueness of the minimizing support, or exhaustive atom list at that support. Sissokho's 2014 work gives broad minimal zero-sum bounds and a derivation partial order, rather than the sharp first-gap cutoff. The present theorem is an exact finite inverse classification of the first strict disparity, not a new general Davenport bound.

## Limitations

The classification ends at diameter nine and does not claim values for larger finite supports. The completeness argument relies on the finite exhaustive algorithm as presented and reproduced in the attached standalone code; it does not offer a short hand classification of all bounded multisets. The example acknowledged by Plagne and Tringali is not specified in their publication and may coincide with the four-point support here. Consequently existence is prior art, and a broader historical enumeration or an unpublished example could affect priority for the sharp first-diameter statement. No extension to higher diameters is claimed.

## References

- A. Plagne and S. Tringali, *The Davenport constant of a box*, arXiv:1405.4363, first submitted 2014-05-17; *Acta Arith.* **171** (2015), 197–219, DOI: 10.4064/aa171-3-1. https://arxiv.org/abs/1405.4363 ; https://doi.org/10.4064/aa171-3-1
- P. A. Sissokho, *A note on minimal zero-sum sequences over Z*, arXiv:1401.0715 (2014). https://arxiv.org/abs/1401.0715
- M. L. Sahs, P. A. Sissokho and J. N. Torf, *A zero-sum theorem over Z*, *Integers* **13** (2013), paper A71, cited in Plagne–Tringali.
