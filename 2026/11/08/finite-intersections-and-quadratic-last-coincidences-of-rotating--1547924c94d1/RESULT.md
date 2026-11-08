# Finite intersections and quadratic last coincidences of rotating-memory Fibonacci sequences

## Finding
For every pair of distinct integers \(2\le k<\ell\), let \(V_s=\{R_n^{(s)}:n\ge1\}\) denote the **positive-value set** of the rotating-memory Fibonacci recurrence. The intersection \(V_k\cap V_\ell\) is finite, and its cardinality admits a complete exact formula. Its individual values are synchronized by their indices: an equality at indices at least two cannot occur at different indices.

For the general family \(4\le k<\ell\), set
\[
d=\ell-k,\qquad Q=\left\lfloor\frac{k-1}{d}\right\rfloor.
\]
Then
\[
\boxed{|V_k\cap V_\ell|=k-2+kQ-\frac{dQ(Q+1)}2.}
\]
All its positive common values are \(R_n^{(k)}=R_n^{(\ell)}\), with exactly the indices
\[
2\le n\le k-1,\quad\text{or}\quad q\ell\le n\le(q+1)k-1\quad(1\le q\le Q).
\]
For \(k=2\), the cardinalities are \(2,4,3,2\) for \(\ell=3,4,5,\ell\ge6\), respectively. For \(k=3\), they are \(13,8,7,6,5,4\) for \(\ell=4,5,6,7,8,\ell\ge9\), respectively.

For fixed \(k\ge4\), the intersection size is nonincreasing as \(\ell\) grows; the largest occurs at the neighboring memory period \(\ell=k+1\) and has size \(k(k-1)/2+k-2\). Its largest common positive value occurs at the exactly determined index \(n=k^2-1\). When \(\ell\ge2k\), only the \(k-2\) values from the initial powers of two survive.

## Assumptions and scope
For every integer \(s\ge2\), define
\[
R_0^{(s)}=0,\qquad R_1^{(s)}=1,\qquad
R_n^{(s)}=\sum_{j=1}^{2+(n\bmod s)}R_{n-j}^{(s)}\quad(n\ge2),
\]
with \(R_t^{(s)}=0\) for \(t<0\). Only **positive** sequence values are counted, without multiplicity: \(R_1^{(s)}=R_2^{(s)}=1\) is one value, and the common zero at index zero is excluded. We make no claim for \(s=1\), which gives the classical Fibonacci sequence.

For \(s\ge2\) and \(n\ge2\), write
\[
c_s(n)=\max\!\left(0,\left\lfloor\frac ns\right\rfloor-\mathbf 1_{s\in\{2,3\}}\right).
\]

## Proof
**Closed form.** The one-step recurrence reduces to multiplication by \(2\) at non-reset indices \(n\ge3\) and by \(3/2\) at reset indices \(n\ge4\), as proved in the cited source. At \(n=2\) the value is \(1\), and at \(n=3\) it is \(2\). Counting reset positions gives
\[
R_n^{(s)}=2^{n-2-2c_s(n)}3^{c_s(n)}\quad(s\ge2,\ n\ge2).
\]
The exponent of \(2\) is nonnegative; the formula includes periods \(s=2,3\) and all initial terms. Equivalently it follows by direct induction from the defining recurrence. For all \(s\ge2\), the values strictly increase for \(n\ge2\), because all subsequent ratios are either \(2\) or \(3/2\).

**Index rigidity.** Suppose \(R_n^{(k)}=R_m^{(\ell)}>0\) with \(n,m\ge2\). Unique factorization in \(2\) and \(3\) gives \(c_k(n)=c_\ell(m)\) and \(n-2-2c_k(n)=m-2-2c_\ell(m)\), hence \(n=m\). Values at index one add no new positive value, since the same value \(1\) already occurs at index two. Thus intersections are counted by the single-index condition \(c_k(n)=c_\ell(n)\), for integers \(n\ge2\).

**General case.** If \(4\le k<\ell\), the condition becomes \(\lfloor n/k\rfloor=\lfloor n/\ell\rfloor\). The common quotient \(q=0\) gives exactly \(n=2,\ldots,k-1\), or \(k-2\) positive values. Every quotient \(q\ge1\) gives the integer interval
\[
q\ell\le n\le(q+1)k-1,
\]
whose length is \(k-q(\ell-k)=k-qd\). It is nonempty exactly when \(1\le q\le Q=\lfloor(k-1)/d\rfloor\). Summing these disjoint lengths yields the formula. Since \(\sum_{q\ge1}\max(0,k-qd)\) decreases with \(d\), the cardinality is nonincreasing in \(\ell\); substituting \(d=1\) and \(d\ge k\) yields the two extremal formulas. For \(d=1\), \(Q=k-1\), and the final interval ends at \((Q+1)k-1=k^2-1\).

**Small-period exceptions.** For \(k=2\), \(c_2(n)=\max(0,\lfloor n/2\rfloor-1)\). Comparing this with \(c_3\) gives the shared indices \(2,3\). Comparing it with \(\lfloor n/\ell\rfloor\) for \(\ell\ge4\) gives indices \(2,3,4,5\) when \(\ell=4\), indices \(2,3,5\) when \(\ell=5\), and only \(2,3\) when \(\ell\ge6\). For \(k=3\), the initial zero-quotient indices are \(2,\ldots,\min(5,\ell-1)\). For each \(q\ge1\), the remaining matching integers lie in
\[
[3(q+1),3(q+2)-1]\cap[q\ell,(q+1)\ell-1].
\]
For \(\ell=4\) the nonempty positive-\(q\) interval lengths are \(2,3,3,2,1\); for \(\ell=5\) they are \(3,2\); for \(\ell=6,7,8\) they are respectively \(3\), \(2\), \(1\); for \(\ell\ge9\) there are none. Adding the initial intervals gives \(13,8,7,6,5,4\), as stated. In every case, the intervals have a finite endpoint, completing the proof.

## Verification
The standalone script `verify.py` generates the defining recurrence using arbitrary-precision integers, independently computes the closed form, compares every pair of positive-value sets for \(2\le k<\ell\le42\), checks that all nontrivial common values occur at equal indices, and verifies every claimed cardinality. Exact arithmetic is used throughout. Run `python verify.py`. Finite testing is corroborative; the proof above is unrestricted.

## Relationship to prior work
Abdelaidoum, Mehiri and Belbachir (first public September 11, 2026, arXiv:2609.12569) introduced the rotating-memory recurrence, proved one-period collapse, individual closed forms, \(2\)- and \(3\)-adic valuation formulas, and growth laws, and supplied tiling interpretations. The present finding **depends on those individual-term results**, and does not reassert them as new. Its separate contribution is the two-parameter *value-set intersection problem*: index synchronization, an exact all-pairs finite intersection count including exceptions, and the sharp quadratic largest-common-index law. The source does not report cross-period common-value counts. The cited OEIS records list individual low-period sequences, not their general two-parameter intersection spectrum.

## Limitations
The result is for the specified cyclic memory lengths \(2,3,\ldots,s+1\) and \(s\ge2\). It does not classify intersections with the classical \(s=1\) sequence, nor other variable-order recurrences. It does not assert historical priority: the source's complete individual closed forms make this arithmetic comparison possible, and an earlier equivalent pairwise-count formula could exist. Search-based originality evidence is not a proof of uniqueness. No independent audit has been conducted.

## References
- W. Abdelaidoum, E.-M. Mehiri, H. Belbachir, *Rotating-Memory Fibonacci Numbers and Periodic Tilings*, arXiv:2609.12569v1 (first public September 11, 2026), https://arxiv.org/abs/2609.12569.
- OEIS Foundation, sequence A038754, https://oeis.org/A038754 (period \(2\) shifted sequence).
- OEIS Foundation, sequence A354541, https://oeis.org/A354541 (period \(3\) shifted sequence).
