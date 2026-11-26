# Exact long-gap spectrum for three consecutive triangular generators

## Finding

Let \(T_k=k(k+1)/2\). For every integer \(n\ge3\), put \(a=T_n\), \(b=T_{n+1}\), \(c=T_{n+2}\), and \(S_n=\langle a,b,c\rangle\). A gap block is a maximal nonempty interval of consecutive positive integers disjoint from \(S_n\). Put \(K=\lfloor(n+1)/4\rfloor\). The gap blocks of length strictly greater than \(b-a=n+1\) are exactly
\[
 I_q=[qc+1,(q+1)a-1]\cap\mathbb Z,\qquad 0\le q<K.
\]
Their lengths are \(a-1-q(2n+3)\). In particular, there are exactly \(K\) such blocks, and each of these lengths occurs once.

## Assumptions and scope

Representations use nonnegative integral multiplicities of the three generators. The complement is finite: \(\gcd(a,b)\) is \(n+1\) for even \(n\), \((n+1)/2\) for odd \(n\), and \(c\equiv1\) modulo that gcd. The cutoff is strict. This result classifies neither the lengths nor the starts of shorter blocks.

## Proof

Write \(u=b-a=n+1\), \(v=c-a=2u+1\). With exactly \(q\) generators, including repetitions, the represented elements are
\[
 E_q=\{qa+iu+jv:i,j\ge0,\ i+j\le q\}.
\]
Both endpoints of its span \([qa,qc]\) are present. For fixed \(j\), the points form a progression of step \(u\) from \(qa+jv\) up to \(qa+jv+(q-j)u\). Its upper endpoint increases by \(v-u=u+1\) when \(j\) increases by one. The next progression's lower endpoint minus the preceding upper endpoint is \(v-(q-j)u\le u+1\) for \(j<q\). Thus as each progression is added, it either overlaps the span of the preceding union or starts at distance at most \(u+1\) from its upper endpoint. In an overlap, the preceding upper endpoint is within the new progression's span, so the first point of the new progression above it is at distance at most \(u\). Induction shows that successive elements of \(E_q\) differ by at most \(u+1\). The statement is vacuous for \(E_0=\{0\}\).

Any gap block intersecting a span \([qa,qc]\) lies inside that span because its endpoints belong to \(S_n\); its length is therefore at most \(u\). A block longer than \(u\) must instead lie between spans. Their left and right endpoints increase strictly with \(q\). The uncovered intervals are exactly the nonempty intervals between \(qc\) and \((q+1)a\) because successive spans eventually overlap, as \(qc-(q+1)a=qv-a\) tends to infinity. Such an uncovered interval is a maximal gap block: every layer with index at most \(q\) ends at or before \(qc\), every later layer starts at or after \((q+1)a\), and both bounding values are represented. Its length is \(a-1-qv\).

Write \(u=4K+r\) with \(0\le r\le3\). Since \(a=u(u-1)/2\),
\[
 a-1-u-Kv=\frac{u(r-3)}2-K-1<0,\qquad
 a-1-u-(K-1)v=\frac{u(r+1)}2-K>0.
\]
Here \(u\ge4\) and \(K\le u/4\). As the lengths decrease strictly with \(q\), precisely \(q=0,\ldots,K-1\) yield a length greater than \(u\).

## Verification

Run `python3 verify.py`. The checker uses direct reachability with the three generators. A streak of \(a\) consecutive represented values certifies that all later values are represented, by adding \(a\). It compares the starts and ends of all observed blocks longer than \(n+1\) against the formula for \(3\le n\le40\). The proof establishes the infinite range.

## Relationship to prior work

Robles-Pérez and Rosales, [*The Frobenius number for sequences of triangular and tetrahedral numbers*](https://arxiv.org/abs/1706.04378), Corollary 28, give the Apéry rectangle for this family. Komatsu, [*The Frobenius number for sequences of triangular numbers associated with number of solutions*](https://arxiv.org/abs/2206.13054), Theorem 1, treats generalized Frobenius thresholds. The prior [isolated-gap classification](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-isolated-gaps-in-semigroups-of-three-consecutive-triangular-numb--42c2c6edcb7c/RESULT.md) already computes both neighbor bounds for a gap; retaining only the left bound and counting its positive integer lifts recovers all starts. None of those results classifies the blocks longer than \(n+1\) in the passages compared here. The separation at \(n+1\) follows from the fixed-number-of-generators layers, not from the one-sided neighbor bounds alone.
