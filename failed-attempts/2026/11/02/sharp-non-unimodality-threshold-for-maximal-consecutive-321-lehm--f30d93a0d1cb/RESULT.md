# Sharp non-unimodality threshold for maximal consecutive-\(321\) Lehmer codes

## Finding

For each integer \(n\ge2\), let \(\mathcal M_n\) be the set of coordinatewise-maximal Lehmer codes of permutations avoiding the **consecutive**, not classical, pattern \(321\). For a code \(p=(p_1,\ldots,p_n)\), define the inversion defect \(\delta(p)=\binom{n}{2}-\sum_{i=1}^n p_i\) and the nonnegative-coefficient polynomial
\[
F_n(q)=\sum_{p\in\mathcal M_n}q^{\delta(p)}.
\]

**Theorem (exact spectrum-shape classification).** The coefficients of \(F_n(q)\), read in ascending degree (including zero coefficients if any), are unimodal if and only if
\[
2\le n\le10\quad\text{or}\quad n=12.
\]
In particular, non-unimodality first occurs at \(n=11\), disappears at \(n=12\), and persists for every \(n\ge13\). The inversion enumerator \(q^{\binom{n}{2}}F_n(q^{-1})\) has the same unimodality classification, since its coefficient order is reversed.

The proof also derives the exact defect generating function
\[
\sum_{n\ge2}F_n(q)x^n=\frac{(x+qx^2)^2}{1-qx^2-q^3x^3}.
\]
This generating function is a calculation from the structural characterization of Beveridge--Hu--Liu, **not an independently claimed new classification of maximal codes**. The contribution asserted here is the sharp all-length unimodality/non-unimodality boundary, including the exceptional recovery at \(n=12\).

## Assumptions and scope

The Lehmer code of a permutation \(\pi\in\mathfrak S_n\) is \(p_i=|\{j>i:\pi_j<\pi_i\}|\), so \(0\le p_i\le n-i\). A permutation avoids the consecutive pattern \(321\) when no index \(i\) has \(\pi_i>\pi_{i+1}>\pi_{i+2}\). The coordinate order is \(p\preceq r\) exactly when \(p_i\le r_i\) for every \(i\); maximality is with respect to all *avoiding* codes in this induced poset. The inversion count is \(\sum_i p_i\). No claim is made about all consecutive-pattern-avoiding permutations, only maximal code elements, or about classical \(321\) avoidance.

A finite coefficient string \((a_0,\ldots,a_s)\) is unimodal if some \(k\) satisfies \(a_0\le\cdots\le a_k\ge\cdots\ge a_s\). Leading and trailing zero coefficients do not change this property; the displayed polynomial coefficients use the usual degrees.

## Proof

**1. Previously established block characterization.** Lemma 4.4 of Beveridge--Hu--Liu (arXiv:2609.33137v1, Section 4) identifies the maximal codes bijectively with ordered compositions
\[
(b_1,\ldots,b_\ell)\models n,
\qquad b_1,b_\ell\in\{1,2\},\quad b_i\in\{2,3\}\ (1<i<\ell).
\]
Every composition has at least two blocks for \(n\ge2\). If \(d_j=b_1+\cdots+b_j\) is a block endpoint, the corresponding code is constant with value \(n-d_j\) on that block; the last block carries zero. On a block of length \(b\) the difference between the full code \((n-1,n-2,\ldots,0)\) and this constant code is \(\binom b2\). Therefore
\[
\delta(p)=\sum_{j=1}^\ell\binom{b_j}{2}.
\]
This uses the source's structural lemma and defect calculation, which are credited rather than reproduced as new theorems.

**2. Weighted enumerator.** The first and last blocks have respective length-defect monomials \(x\) or \(qx^2\). Each interior block has monomial \(qx^2\) or \(q^3x^3\). An arbitrary ordered sequence of interior blocks is permitted. Multiplying the two endpoint choices and summing the geometric series of interior choices proves
\[
\sum_{n\ge2}F_n(q)x^n=(x+qx^2)^2\sum_{r\ge0}(qx^2+q^3x^3)^r
=\frac{(x+qx^2)^2}{1-qx^2-q^3x^3}.
\]
In particular \(F_2(q)=1\), \(F_3(q)=2q\), \(F_4(q)=q+q^2\), and for \(n\ge5\),
\[
F_n(q)=qF_{n-2}(q)+q^3F_{n-3}(q).
\]

**3. Explicit coefficient extraction.** Let \(E\in\{0,1,2\}\) count the endpoint blocks of length two, \(h\) count interior blocks of length two, and \(t\) count interior blocks of length three. Then
\[
n=2+E+2h+3t,\quad \delta=E+h+3t,
\quad\#\text{such block words}=\binom{2}{E}\binom{h+t}{t}.
\]
Write \(n=2m\). Setting \(j=m-1-h\) gives \(\delta=m-1+j\) and \(E+3t=2j\), hence for \(0\le j\le m-1\)
\[
[q^{m-1+j}]F_{2m}(q)=
\sum_{\substack{t\ge0,\ E\in\{0,1,2\}\\ E+3t=2j}}
\binom{2}{E}\binom{m-1-j+t}{t}.
\]
Similarly, when \(n=2m+1\), \(\delta=m+j\) and \(E+3t=2j+1\), giving
\[
[q^{m+j}]F_{2m+1}(q)=
\sum_{\substack{t\ge0,\ E\in\{0,1,2\}\\ E+3t=2j+1}}
\binom{2}{E}\binom{m-1-j+t}{t},\qquad 0\le j\le m-1.
\]
As usual a binomial coefficient with nonnegative upper index smaller than its lower index is zero. The ranges above are complete because \(h\ge0\), and every legal composition has precisely one quadruple \((E,h,t,\text{interior order})\).

**4. Permanent odd-length valley.** For every \(m\ge5\), the coefficients of \(F_{2m+1}(q)\) in consecutive degrees \(m+1,m+2,m+3\) are, using the displayed coefficient formula,
\[
(m-1),\qquad(m-2),\qquad (m-2)(m-3).
\]
Because \(m-1>m-2<(m-2)(m-3)\) for all \(m\ge5\), the coefficient string has a strict valley. Thus every odd \(n\ge11\) is non-unimodal.

**5. Permanent even-length valley.** For every \(m\ge7\), the coefficients of \(F_{2m}(q)\) in consecutive degrees \(m+2,m+3,m+4\) are
\[
\binom{m-2}{2},\qquad\binom{m-3}{2},\qquad2\binom{m-3}{3}.
\]
The first strictly exceeds the second; the last exceeds the second because their ratio is \(2(m-5)/3>1\) for \(m\ge7\). Therefore all even \(n\ge14\) are non-unimodal.

**6. Exhaustion of exceptions without extrapolation.** The recurrence yields the complete coefficient strings in increasing defect, starting at the least nonzero exponent:

| \(n\) | Coefficients of \(F_n(q)\) |
|---:|---|
| 2 | \(1\) |
| 3 | \(2\) |
| 4 | \(1,1\) |
| 5 | \(2,1\) |
| 6 | \(1,1,2\) |
| 7 | \(2,2,1\) |
| 8 | \(1,1,4,1\) |
| 9 | \(2,3,2,2\) |
| 10 | \(1,1,6,3,1\) |
| 11 | \(2,4,3,6,1\) |
| 12 | \(1,1,8,6,3,2\) |

All listed strings except that for \(n=11\) are unimodal. Together with Steps 4--5, this exhausts every \(n\ge2\) and proves the if-and-only-if theorem. \(\square\)

## Verification

Run the standalone Python 3 program `verify.py`. It independently enumerates consecutive-pattern-avoiding permutations and tests coordinatewise maximality directly for \(2\le n\le7\), compares three separate polynomial computations for \(2\le n\le27\), and checks the sharp coefficient-valley formulas and the shape classification through length \(160\). Expected final line: `VERIFY_OK`. These finite checks are diagnostic only; Steps 1--6 provide the infinite proof.

## Relationship to prior work

Beveridge, Hu, and Liu (2026, arXiv:2609.33137v1) prove the precise maximal-code composition structure (Lemma 4.4), Padovan counts (Theorem 1.4), and extremal inversion-number values (Theorem 1.5), including the same block-defect calculation used here. Their inspected entire relevant Section 4 does not state the full defect coefficient polynomial or a unimodality classification. The polynomial here is an algebraic consequence of their structure; the asserted additional result is the **sharp coefficient-shape theorem**, whose proof requires selecting and comparing three coefficients uniformly in both parities. The earlier Beveridge--Hu--Liu (2026, arXiv:2607.26900) studies the different vincular patterns \(32\!\text{-}1\) and \(3\!\text{-}21\); its Fibonacci maximum-code counts do not give this defect shape theorem. The literature on independent domination polynomials of paths is related through maximal independent descent sets, but cardinality grading does not coincide with the present inversion defect grading. No covering equivalent statement was identified in targeted searches; historical priority is not independently certified.

## Limitations

The result is an exact all-length theorem conditional only on the established, cited composition characterization. It does not address average inversions, asymptotic central-limit behavior, classical \(321\)-avoidance, or nonmaximal elements. Earlier work already proves the underlying block model, so neither that classification nor the unweighted Padovan recurrence is claimed as new. The shape theorem has undergone a self-review only; an independent mathematical audit and exhaustive historical-priority check have not been performed.

## References

1. A. Beveridge, Y. Hu, and Y. Liu, *Maximal Lehmer Codes for Permutations with Classical and Consecutive 321-Avoidance*, arXiv:2609.33137v1, initially posted 2026-09-27, especially Lemma 4.4 and Theorems 1.4--1.5. https://arxiv.org/abs/2609.33137
2. A. Beveridge, Y. Hu, and Y. Liu, *Lehmer Codes and the Reverse-Complement Mapping from (32-1)-Avoiding Permutations to (3-21)-Avoiding Permutations*, arXiv:2607.26900, initially posted 2026-07-29. https://arxiv.org/abs/2607.26900
