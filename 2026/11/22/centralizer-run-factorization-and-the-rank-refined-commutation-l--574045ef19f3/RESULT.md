# Joint rank census and sharp fixed-rank commutation bounds for shift-one partial isometries

## Finding

Let \(N=n-1\) for \(n\ge2\), and let \(B_n\) consist of all partial maps \(\xi_A:a\mapsto a-1\) with domain \(A\subseteq\{2,\ldots,n\}\) on \(\{1,\ldots,n\}\). The empty map is included. For positive rank \(r\le N\), the rank-\(r\) stratum is the family \(F_r\) of shift-one maps used in the minimal ideal generators of Ayık, Ayık and Fernandes [1, §2 and Theorem 7].

**Joint rank census.** Define
\[
C_N(x,y)=\sum_{\substack{\xi_A,\xi_D\in B_n\\\xi_A\xi_D=\xi_D\xi_A}}x^{|A|}y^{|D|},\qquad C_0(x,y)=1,
\qquad Q(z,x,y)=\frac{zx}{1-zx}+\frac{zy}{1-zy}+\frac{zxy}{1-zxy}.
\]
Then the formal power series for ordered commuting pairs is
\[
\sum_{N\ge0}C_N(x,y)z^N=\frac{1+Q(z,x,y)}{1-z-zQ(z,x,y)}.
\]
In particular, the coefficient of \(z^{n-1}x^ry^r\) counts the ordered commuting pairs from \(F_r\). Summing over both ranks gives
\[
C_N(1,1)=\frac{(1+\sqrt3)^{N+1}+(1-\sqrt3)^{N+1}}2,
\qquad
\frac{C_N(1,1)}{4^N}\sim\frac{1+\sqrt3}{2}\left(\frac{1+\sqrt3}{4}\right)^N.
\]

**Sharp fixed-rank bound.** Write \(d=N-r\) for \(1\le r\le N\). The maximum number of partners in \(B_n\) commuting with an element of rank \(r\) is
\[
\begin{cases}
2^{d+1},&0\le d\le r-1,\\
2^d,&d\ge r.
\end{cases}
\]
In the first regime the maximizing support words have \(d+1\) nonempty blocks of ones separated by single zeros, with no boundary zeros. There are exactly \(\binom{r-1}{d}\) such words. In the second regime any contiguous block of \(r\) ones touching a boundary attains the maximum.

## Scope

The rank is domain cardinality. All pairs are ordered. The notation uses ordinary partial function composition; whether it is written left-first or right-first does not alter commutation. The family \(B_n\) is not asserted to be closed under composition, and a partner count in \(B_n\) is not the centralizer size in the full semigroup. The \(N=0\) term expresses the empty-word convention.

## Proof

**Local compatibility.** Let \(a_i=1\) mean \(i+1\in A\), and similarly \(b_i=1\) for \(D\), for \(1\le i\le N\). Both products, wherever defined, shift by minus two. The composites are defined at \(i+1\), for \(2\le i\le N\), exactly when \(a_i b_{i-1}=1\) and \(b_i a_{i-1}=1\), respectively. Thus commutation is equivalent to
\[
a_i b_{i-1}=b_i a_{i-1}\qquad(2\le i\le N).
\]
The condition is vacuous for \(N=1\).

**Pair generating function.** Encode the two bits at each position by \(00,10,01,11\), weighted \(1,x,y,xy\) respectively. Two adjacent nonzero symbols obey the local condition exactly when they are equal: the distinct nonzero binary vectors all have a nonzero determinant in pairs. The symbol \(00\) is compatible with all symbols. Let \(G\) be the length-and-rank generating function. A nonempty admissible word either begins with \(00\), after which the suffix is unrestricted, or begins with a maximal constant nonzero block. The latter is weighted by \(Q\), and is followed by the end of the word or by \(00\) and an unrestricted suffix. These cases are disjoint. Hence \(G=1+zG+Q(1+zG)\), which yields the claimed series. Specializing \(x=y=1\) gives \((1+2z)/(1-2z-2z^2)\). The coefficients have initial values \(1,4\) and recurrence \(c_N=2c_{N-1}+2c_{N-2}\) for \(N\ge2\), giving the stated closed form. The asymptotic follows since \(|1-\sqrt3|<1+\sqrt3\), and the two maps are drawn from \(2^N\) possibilities each.

**Partner factorization (a prior structural specialization).** Fix \(a\). On each maximal one-run the equation makes the \(b\)-bits all equal; a zero next to any one forces its \(b\)-bit to vanish, and every other zero is free. With one-run lengths \(\ell_1,\ldots,\ell_s\) and \(h\) zeros not adjacent to a one, the rank polynomial of the restricted partners is therefore
\[
P_A(y)=\sum_{D:\,\xi_A\xi_D=\xi_D\xi_A}y^{|D|}=(1+y)^h\prod_{j=1}^{s}(1+y^{\ell_j}),
\]
where the sum is over \(\xi_D\in B_n\). This also follows directly from the established initial-chain/terminal-chain characterization of commuting partial injections [2, Proposition 2.2; 3, proof §§1–2]. The chains of \(\xi_A\) are the descending intervals of length \(\ell_j+1\) coming from one-runs, with the remaining vertices viewed as singleton chains. Within a chain of length \(L\ge2\), the only nonempty initial-to-terminal segment map with shift minus one uses \(L-1\) arrows. Between different chains, a shift-minus-one arrow must cross between consecutive intervals. Its source must be the minimum of its own chain but also the first (largest) vertex of its source segment, forcing a singleton source chain. Its image must be both the maximum of the next chain and the terminal vertex of the one-point image, forcing a singleton target chain. These are precisely the free zeros. The allowed segment maps never conflict for source or target, because nontrivial chains only pair with themselves and each singleton has at most one immediately lower target and at most one immediately higher source. The elementary local proof above is included for completeness; the individual factorization is not claimed as a separate new result.

**Fixed-rank extremum.** For rank \(r\ge1\), let \(f=d-h\) count the zeros adjacent to a one. The factorization gives \(P_A(1)=2^{s+d-f}\). Every one of the \(s-1\) internal gaps contributes at least one neighboring zero; a gap of length at least two contributes two, and a nonempty boundary gap contributes one. Thus \(s+d-f\le d+1\), with equality exactly for single internal zeros and no boundary zeros. This requires \(s=d+1\le r\), and distributing the \(r\) ones into \(s\) nonempty runs gives \(\binom{r-1}{d}\) attaining words when \(d<r\). When \(d\ge r\), equality is impossible, so the integer exponent is at most \(d\). A single boundary-touching one-run has \(f=s=1\) and attains it. Full rank (\(d=0\)) belongs to the first case, giving two partners.

## Verification

For a finite reproduction, `python3 verify.py` uses the standard library. Its direct comparison of composite domains, individual run polynomials, and four-state bivariate dynamic program agree for \(1\le N\le8\). Its extremal check uses \(1\le N\le10\) and also tests the number of dense-regime maximizers. `verification_output.txt` is the recorded replay. The finite tests do not prove the formal power series or the sharp bounds for arbitrary lengths; those follow from the arguments above.

## Relationship to prior work and limitations

The generator theorem [1] supplies the interpretation of the rank coefficients. The general symmetric-inverse-monoid centralizer theorem [2] and its matching-polynomial application [3] supply the individual factorization by the specialization explained above. They classify partners of a given map, without summing in both ranks over the linearly arranged supports or optimizing the restricted neighborhood at fixed rank. The joint calculation uses a run language of *pairs* of support words; the extremal one needs the number and types of zero gaps. The exact full centralizers of powers of the canonical shift [4] concern a prescribed consecutive or residue-chain support and use a larger partner family; the full-support restriction agrees with \(P_A(y)=1+y^N\). Aggregate product-rank counts for unrestricted translations [5] do not record commutation, and the commuting-pair census for interval-supported translations [6] does not permit arbitrary support holes or give this joint refinement. The underlying order-decreasing isometry semigroup is studied in [7].

The conclusions are restricted to pairs of displacement minus one with arbitrary supports. No classification of all maximizers in the second regime is asserted, and no historical-priority claim is made for the unweighted recurrence in other settings. A differently indexed derivation of the joint or extremal formulas may exist.

## References

1. G. Ayık, H. Ayık and V. H. Fernandes, *On semigroups of order-decreasing partial isometries: presentations and ranks of certain ideals*, [arXiv:2611.12150v1](https://arxiv.org/abs/2611.12150v1), §2, Theorem 7.
2. J. Araújo, W. Bentz and J. Konieczny, *The commuting graph of the symmetric inverse semigroup*, [arXiv:1205.1664](https://arxiv.org/abs/1205.1664), Proposition 2.2.
3. *Nilpotent partial-permutation conjugacy is determined by its centralizer rank spectrum*, [published record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-nilpotent-partial-permutation-conjugacy-is-determined-by-its-cen--8be29dd91c24).
4. *Rank-refined centralizers of canonical shifts in order-decreasing partial-isometry monoids*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-rank-refined-centralizers-of-canonical-shifts-in-order-decreasin--548536412e8b).
5. *The product-rank law of finite-chain partial translations*, [published record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-the-product-rank-law-of-finite-chain-partial-translations--849553a20428).
6. *Exact nonzero-product commuting pairs in interval-translation rook monoids*, [published record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-nonzero-product-commuting-pairs-in-interval-translation-ro--12e310078e35).
7. R. Kehinde, S. O. Makanjuola and A. Umar, *On the semigroup of order-decreasing partial isometries of a finite chain*, [arXiv:1101.2558v1](https://arxiv.org/abs/1101.2558v1).
