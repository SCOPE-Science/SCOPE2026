# Exact square-subsequence generating function and extremal rotations of permutation powers

## Finding
Let \(q\ge 2\), let \(P=c_1\cdots c_q\) be a word in which each of the \(q\) alphabet letters occurs exactly once, and let \(S_q(k,m)\) count **distinct strings** of the form \(VV\), with \(|V|=m\ge1\), occurring as scattered subsequences of \(P^k\). Different embeddings of the same string are counted once. Put
\[
B=1+(1-t^2)z.
\]
Then the full bivariate generating function (the exponent of \(z\) is the half-length) is
\[
\boxed{\sum_{k\ge1}\sum_{m\ge1} S_q(k,m)\,t^k z^m
=\frac{zt^2\left(\sum_{j=0}^{q-1}B^j+qt B^{q-1}\right)}{1-t^2 B^q}.}
\]
The expression is interpreted as a formal series in \(t,z\) at the origin, and is independent of the ordering of the letters in \(P\). For \(k=1\) there is no nonempty square subsequence. For \(k\ge2\) the maximum possible half-length is \(q\lfloor k/2\rfloor\). If \(k=2r\), there is exactly one square of maximum length, namely \((P^r)^2\). If \(k=2r+1\ge3\), there are exactly \(q\) distinct maximum-length squares, whose roots are the \(q\) cyclic rotations of \(P^r\).

For instance, for \(q=3,k=4\), the six successive values \(S_3(4,m)\), \(m=1,\ldots,6\), are \(3,9,17,15,6,1\). Two useful specializations are \(S_q(2,m)=\binom qm\) for \(1\le m\le q\), and \(S_q(3,m)=q\binom{q-1}{m-1}\) for \(1\le m\le q\); all other positive half-lengths in these cases have count zero.

## Assumptions and scope
The alphabet is finite, with exactly \(q\ge2\) distinct letters. \(P\) is any fixed permutation of those letters; every copy in \(P^k\) has the same order. A scattered subsequence preserves order of selected positions but may skip positions. A square means \(VV\) for a **nonempty** word \(V\). The statistic counts square words, equivalently their unique root strings, never positional embeddings. The power count \(k\) and half-length \(m\) range over positive integers. There is no claim about squares occurring as **contiguous factors**, nor about arbitrary periods with repeated letters.

Order the letters as \(c_1<\cdots<c_q\) in the order they appear in \(P\). This is a relabeling used only in the proof, so the stated count does not depend on an ambient alphabet order. For a root \(V=v_1\cdots v_m\), define
\[
d(V)=\sum_{i=1}^{m-1}[v_i\ge v_{i+1}],\qquad
b(V)=[v_m\ge v_1].
\]
Here \([E]\) denotes the indicator of a proposition \(E\), and equality counts as a weak descent.

## Proof
**1. Exact embedding criterion.** Greedily select each desired letter at its earliest possible occurrence in \(P^k\). Moving from \(v_i\) to \(v_{i+1}\) stays in the current copy of \(P\) precisely when \(v_i<v_{i+1}\), and otherwise advances by one copy. The first letter uses copy one. Thus \(V\) requires exactly \(1+d(V)\) copies, and the concatenation \(VV\) requires exactly
\[
1+2d(V)+b(V)
\]
copies. A greedy match is successful if and only if any match exists, so
\[
S_q(k,m)=\sum_{V\in\{c_1,\ldots,c_q\}^{m}}[1+2d(V)+b(V)\le k]. \tag{1}
\]
Summing over all \(k\) gives the weighted enumeration
\[
F_q(z,t)=\frac{t}{1-t}\sum_{m\ge1}z^m
\sum_{V\in\{c_1,\ldots,c_q\}^{m}}t^{2d(V)+b(V)}. \tag{2}
\]

**2. Transfer-matrix evaluation.** Define the \(q\)-by-\(q\) matrix \(M(u)\) by \(M(u)_{ij}=u\) if \(i\ge j\), and \(M(u)_{ij}=1\) if \(i<j\). Let \(J\) be the all-ones matrix and \(L\) the lower-triangular matrix of ones (including the diagonal). Then \(M(u)=J+(u-1)L\). In (2), all consecutive internal edges of \(V\) have weight \(M(t^2)\), while the closing edge from \(v_m\) back to \(v_1\) has weight \(M(t)\). Therefore
\[
F_q(z,t)=\frac{zt}{1-t}\operatorname{tr}\!\left((I-zM(t^2))^{-1}M(t)\right). \tag{3}
\]
This includes the one-letter case because the diagonal entry of \(M(t)\) is \(t\).

We evaluate (3) explicitly, rather than leaving a determinant. Put \(u=t^2\), \(B=1-z(u-1)\), and \(A=I-zM(u)\). The matrix \(I-z(u-1)L\) has determinant \(B^q\). Solving \((I-z(u-1)L)x=\mathbf1\) by prefix sums gives
\[
\mathbf1^T(I-z(u-1)L)^{-1}\mathbf1
=\frac{B^{-q}-1}{z(u-1)}.
\]
A rank-one determinant identity, applied to the update \(-zJ\), now gives
\[
\det A=\frac{uB^q-1}{u-1},\qquad
\operatorname{tr}(A^{-1}J)=\frac{1-B^q}{z(uB^q-1)}. \tag{4}
\]
Also, differentiating the determinant with respect to \(z\) yields
\[
\operatorname{tr}(A^{-1}M(u))=-\frac{d}{dz}\log\det A
=\frac{qu(u-1)B^{q-1}}{uB^q-1}. \tag{5}
\]
Because \(M(t)=(M(t^2)+tJ)/(1+t)\), substitute (4)–(5) into (3) and use
\[
B^q-1=z(1-t^2)\sum_{j=0}^{q-1}B^j.
\]
Cancellation produces the boxed generating function. Every identity here is an identity of formal series with invertible denominators at the origin.

**3. Sharp maximum and classification.** Each letter occurs exactly \(k\) times in \(P^k\); in any square its total frequency is even. If \(k=2r\), the maximum possible square length is \(2qr\). It is attained by the whole \(P^{2r}\), and the whole word is the sole subsequence of its length, giving exactly one maximizer. If \(k=2r+1\) with \(r\ge1\), the square uses at most \(2r\) occurrences of each letter and hence has half-length at most \(qr\). This bound is attained by \((P^r)^2\).

Let \(V\) be the root of a maximum square in the odd case. It must contain each letter exactly \(r\) times. Let \(c(V)=d(V)+b(V)\) be its number of *cyclic weak descents*, using the comparison of last to first as a closing edge. Each strictly increasing circular run has length at most \(q\); with \(qr\) letters this forces \(c(V)\ge r\). By (1), the embedding inequality \(2d(V)+b(V)\le2r\) gives \(c(V)\le r\): if \(b(V)=0\), then \(d(V)\le r\); if \(b(V)=1\), then \(d(V)\le r-1\). Consequently \(c(V)=r\). All \(r\) strictly increasing circular runs must have length exactly \(q\); each is the full ordered alphabet \(P\). Thus \(V\) is a cyclic rotation of \(P^r\). Conversely, each of those \(q\) rotations has \(c(V)=r\), and the cases \(b(V)=0\) and \(b(V)=1\) both satisfy (1). There are exactly \(q\) different rotations because \(P\) has pairwise distinct letters. This proves the maximum and multiplicity statements.

## Verification
The standalone, standard-library script `verify.py` constructs all subsequences by position-wise dynamic expansion and counts the **distinct** square strings directly. Its independent coefficient engine extracts the series from the proposed rational equation by integer polynomial recurrence. It additionally checks the greedy-period criterion against direct greedy embedding for small instances and verifies the extremal descriptions. Running `python3 verify.py` produced:

```
PASS: 19 complete position-enumerated (q,k) profiles; 85 rational coefficients; 11992 independent greedy/descents decisions.
Examples: q=3, k=4 -> [3, 9, 17, 15, 6, 1]
          q=4, k=3 -> [4, 12, 12, 4]
```

The verifier is a finite consistency test, not an infinite proof. The proof above supplies the all-parameter justification. Counts and comparisons concern words over exactly the stated alphabet and powers of a single fixed permutation.

## Relationship to prior work
Inoue, Inenaga, Hyyrö, Bannai and Takeda (2018) develop general algorithms for **longest common square subsequences** of two strings. Bannai, I and Köppl (2022) treat longest periodic and subperiodic subsequences of one string, including the square case. These are closely related algorithmic problems, but the claims inspected there concern computing an optimum for arbitrary input, not the complete distinct-square census of repeated permutations or this closed bivariate rational function. The present result uses a special periodic structure and counts every root length and every power; generic optimum-length algorithms do not state these counts. Contiguous square-factor enumerations are a different statistic. Previous work on palindromic subsequences also concerns a different symmetry operation. The literature comparison is not a proof of worldwide priority.

## Limitations
The theorem does not count embeddings (which may be numerous), does not characterize squares for arbitrary nonpermutation periods, and does not extend unchanged to abelian squares or contiguous square factors. It is self-reviewed but has not received an independent audit. Literature coverage is incomplete, and an unindexed equivalent enumeration remains possible.

## References
1. H. Bannai, T. I and D. Köppl, *Longest (Sub-)Periodic Subsequence*, arXiv:2202.07189v1, first posted 2022-02-15. https://arxiv.org/abs/2202.07189
2. T. Inoue, S. Inenaga, H. Hyyrö, H. Bannai and M. Takeda, *Computing Longest Common Square Subsequences*, CPM 2018, DOI:10.4230/LIPIcs.CPM.2018.15. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2018.15
