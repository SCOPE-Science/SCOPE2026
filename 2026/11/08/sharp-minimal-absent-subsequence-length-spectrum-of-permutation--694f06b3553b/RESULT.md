# Sharp minimal-absent-subsequence length spectrum of permutation powers

## Finding

Let \(q\ge4\) and \(k\ge1\) be integers, and let \(P\) contain each of \(q\) distinct alphabet symbols exactly once. Define \(W=P^k\). A *minimal absent scattered subsequence* of \(W\) is a nonempty word that does not embed as a subsequence of \(W\), although each of its one-letter deletions embeds.

Write \(k-1=(q+1)t+r\), with \(t\ge0\) and \(0\le r\le q\). **The exact set of lengths of minimal absent scattered subsequences** is

\[
\bigl\{k+1,k+2,\ldots,k+1+(q-1)t+\min(r,q-1)\bigr\}.
\]

In particular, the longest length is

\[
\Lambda(q,k)=k+1+(q-1)\left\lfloor\frac{k-1}{q+1}\right\rfloor
+\min\bigl((k-1)\bmod(q+1),q-1\bigr).
\]

This is exact for every \(q\ge4\) and every \(k\ge1\); the bound does not assume a fixed alphabet size or an asymptotic regime. For fixed \(q\), the leading coefficient of \(\Lambda(q,k)\) in \(k\) is \(2q/(q+1)\).

## Assumptions and scope

The alphabet consists of exactly the \(q\) letters of \(P\); no external symbols are allowed in absent words. Relabeling the symbols preserves subsequence containment, so take \(P=01\cdots(q-1)\). For a candidate word \(v=v_1\cdots v_\ell\), put

\[
 d(a,b)={\bf1}_{a\ge b},\qquad
 D(v)=\sum_{i=1}^{\ell-1}d(v_i,v_{i+1}),\qquad
 A(v)=\ell-1-D(v).
\]

The indicators count *weak* descents, including equal neighboring letters. A word with zero letters is embedded, so minimal absent words have length at least two in this full-support setting.

## Proof

**1. Greedy embedding and local minimality.** A greedy subsequence embedding of \(v\) in \(P^k\) moves to the next copy exactly when \(v_i\ge v_{i+1}\). The first symbol always uses the first copy. Therefore

\[
 v\preceq P^k\quad\Longleftrightarrow\quad D(v)\le k-1.
\]

Suppose \(v\) is minimal absent. By deleting either endpoint, the weak-descent count decreases by at most one. Since the resulting word is embedded, \(D(v)=k\), and both the first and last adjacent pairs are weak descents. Deleting an interior letter \(v_i\) decreases \(D\) by

\[
\Delta_i=d(v_{i-1},v_i)+d(v_i,v_{i+1})-d(v_{i-1},v_{i+1}).
\]

Here \(\Delta_i\le1\); minimality requires \(\Delta_i\ge1\), hence \(\Delta_i=1\). Conversely, these endpoint conditions and all the interior equalities ensure that every one-letter deletion embeds, while \(D(v)=k\) ensures that \(v\) does not embed. This gives a necessary and sufficient local criterion.

**2. Two interleaved monotonicity tracks.** Let \(a=A(v)\), so \(v\) has \(k\) descents and \(a\) ascents, hence \(\ell=k+a+1\). The interior equality forbids two adjacent ascents. At every ascent from \(v_i\) to \(v_{i+1}\), it forces the two strict inequalities

\[
 v_{i-1}<v_{i+1}\quad\hbox{and}\quad v_i<v_{i+2},
\]

because the neighboring edges are descents. At every pair of adjacent descents, it instead forces \(v_i\ge v_{i+2}\). Consequently the two step-two paths through the positions of odd parity and even parity each contain exactly \(a\) strict-increase edges. Their other edges are nonincreasing. If these other edge counts are \(h_0,h_1\), then

\[
 h_0+h_1=k-a-1.
\]

A path containing \(h_j\) nonincreasing steps can have at most \(h_j+1\) successive runs of strictly increasing steps; each such run has length at most \(q-1\), because the alphabet has \(q\) values. Thus, for \(a\ge1\),

\[
 a\le(q-1)(h_j+1)\quad(j=0,1).
\]

Adding the resulting integer lower bounds on \(h_0,h_1\) yields

\[
 k\ge a+1+2\left(\left\lceil\frac{a}{q-1}\right\rceil-1\right)
=a+1+2\left\lfloor\frac{a-1}{q-1}\right\rfloor.
\]

For \(a=0\), only \(k\ge1\) is needed. Inverting this monotone inequality using \(k-1=(q+1)t+r\) gives

\[
 0\le a\le(q-1)t+\min(r,q-1).
\]

To check the inversion explicitly: set \(a-1=(q-1)u+s\), \(0\le s<q-1\). The lower bound for \(k\) becomes \(k\ge(q+1)u+s+2\), which allows exactly the above maximal integer \(a\).

**3. Attaining every length.** For \(2\le h\le q\), define the doubled staircase

\[
 T_h=00\,11\,22\cdots(h-1)(h-1).
\]

For any target ascent count \(a\ge1\), write \(a-1=(q-1)u+s\), \(0\le s\le q-2\), and form

\[
 V_a=(T_q)^u T_{s+2}.
\]

The word \(V_a\) has precisely \(a\) ascents and \(a+1+2u\) weak descents. Every internal triple satisfies the local criterion from Step 1, including triples crossing the boundary between staircases, and both endpoint pairs are weak descents. Therefore \(V_a\) is minimal absent from \(P^{a+1+2u}\). If \(k\ge a+1+2u\), insert \(k-a-1-2u\) further zeros into the initial zero run. This increases the descent count to \(k\), preserves all local equalities, and yields a minimal absent word of \(P^k\) with length \(k+a+1\). For \(a=0\), the word consisting of \(k+1\) zeros has the same property.

Every integer \(a\) allowed by Step 2 meets the construction's inequality, so all and only the asserted lengths occur. This proves the claim.

## Verification

Run `python verify.py` from the directory containing this document and the standalone verifier. The verifier independently checks literal subsequence containment and every deletion for \(14\) finite host configurations, including \(65{,}958\) candidate words. It also computes the maximum via a separate finite-state recurrence for \(136\) configurations. The observed maxima and local characterization agree with the theorem. The finite tests are corroborative; the preceding argument supplies the proof for unbounded parameters.

## Relationship to prior work

Kosche, Koß, Manea and Siemer [1] introduced and systematically studied minimal absent scattered subsequences, including precisely the family \(B_k=P^k\). Their Proposition 3.8 proves that this family supports exponentially many minimal absent subsequences, and supplies an explicit subfamily. Their paper does not state the full sharp maximum-length function or the interval of all feasible lengths derived here. Their general characterization of minimal absence is compatible with Step 1 but does not itself yield the new parity-track extremal bound and attainment.

Manea, Ringleb, Siemer and Winkler [2] subsequently gave a general efficient algorithm for finding a longest minimal absent subsequence. Their algorithm can determine the value on any fixed input; it does not state the present symbolic formula for all \(q,k\) or the complete length-support classification. Previously recorded exact special-alphabet results for two and three symbols are treated as already covered; novelty is restricted to this uniform \(q\ge4\) theorem.

## Limitations

The theorem counts possible *lengths*, not the number of distinct minimal absent words of each length. It assumes the host is an exact power of a single permutation; it does not cover arbitrary periodic blocks, missing alphabet symbols, or arbitrary host strings. Exhaustive computations alone cannot certify an infinite-parameter theorem. Bibliographic searches and inspection of the closest primary sources do not rule out an equivalent result in unindexed or differently named literature. No independent scientific audit has been performed.

## References

1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968, first publicly posted 2021-08-31, https://arxiv.org/abs/2108.13968 . In particular, Section 3 and Proposition 3.8.
2. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471, first publicly posted 2025-04-30, https://arxiv.org/abs/2504.21471 . In particular, its longest-minimal-absent-subsequence algorithm.
