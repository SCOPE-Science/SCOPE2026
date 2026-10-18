# Minimum repair triples form exact 2-designs in the new 3-design LRC family
## Finding

Let
\[
q=p^m,
\]
where \(p\) is an odd prime,
\[
m\ge2,\qquad 1\le s<m,
\qquad
\ell=\gcd(m,s).
\]
Let \(C\) be the linear code of Xiong, Wang, Zheng, and Ji with parameters
\[
[q+1,4,q-p^\ell]_{q^2}.
\]
Set
\[
\lambda=p^\ell-2.
\]

For every coordinate \(i\), the **complete collection of minimum-cardinality recovery sets** is
\[
\mathcal R_i
=
\{B\setminus\{i\}:i\in B,\ B\in\mathcal B_4(C^\perp)\},
\]
where \(\mathcal B_4(C^\perp)\) denotes the set of distinct supports of weight-\(4\) dual codewords.

Moreover,
\[
(\{1,\ldots,q+1\}\setminus\{i\},\mathcal R_i)
\]
is a simple
\[
2\text{-}(q,3,\lambda)
\]
design.

Hence every coordinate has exactly
\[
|\mathcal R_i|
=
\frac{\lambda q(q-1)}6
\]
distinct minimum recovery triples. Every other coordinate belongs to exactly
\[
\frac{\lambda(q-1)}2
\]
of these triples, and every pair of helper coordinates occurs together in exactly
\[
\lambda
\]
minimum recovery triples.

The repair design also yields a uniform disjoint-repair guarantee. Every coordinate has at least
\[
\left\lceil
\frac{\lambda q(q-1)}
{9\lambda(q-3)+6}
\right\rceil
\]
pairwise disjoint minimum recovery triples.

Thus the source's all-symbol locality-\(3\) statement admits a sharper structural form: the entire minimum-repair hypergraph at each coordinate is an exact balanced design, and it provides explicit availability.

For the source examples this lower bound gives at least \(2\), \(3\), and \(10\) pairwise disjoint repair triples at
\[
(q,\lambda)=(9,1),\ (25,3),\ (81,7),
\]
respectively.

## Assumptions and scope

The source proves
\[
C^\perp=[q+1,q-3,4]_{q^2}
\]
and proves that the distinct supports of its weight-\(4\) dual codewords form a
\[
3\text{-}(q+1,4,p^\ell-2)
\]
design.

A recovery set for coordinate \(i\) is a set \(R\) of other coordinate positions such that the \(i\)-th symbol of every codeword is determined by the symbols in \(R\).

For a linear code, any such recovery relation can be taken linear. Indeed, if
\[
\pi_R:C\longrightarrow \mathbb F_{q^2}^{R}
\]
is coordinate projection and the \(i\)-th coordinate is determined by \(\pi_R(c)\), then
\[
\ker\pi_R
\subseteq
\ker(c\mapsto c_i).
\]
Therefore the coordinate functional factors linearly through \(\pi_R(C)\) and extends to a linear functional on \(\mathbb F_{q^2}^{R}\). Equivalently, there is a dual codeword supported inside
\[
R\cup\{i\}
\]
whose \(i\)-th entry is nonzero.

Because
\[
d(C^\perp)=4,
\]
no coordinate can have a recovery set of size below \(3\). Thus the triples classified here are exactly the minimum-cardinality recovery sets.

## Proof

The source proves that the distinct weight-\(4\) dual supports form a
\[
3\text{-}(q+1,4,\lambda)
\]
design with
\[
\lambda=p^\ell-2.
\]

First fix a coordinate \(i\). If \(B\) is a weight-\(4\) dual support containing \(i\), choose
\[
h\in C^\perp
\]
with
\[
\operatorname{Supp}(h)=B.
\]
All four entries of \(h\) on \(B\) are nonzero. For every codeword \(c\in C\),
\[
\sum_{j\in B}h_jc_j=0.
\]
Hence
\[
c_i
=
-h_i^{-1}
\sum_{j\in B\setminus\{i\}}h_jc_j,
\]
so
\[
B\setminus\{i\}
\]
is a recovery triple for \(i\).

Conversely, let \(R\) be any recovery triple for \(i\). By the factorization argument in the scope section, there is a nonzero dual codeword supported in
\[
R\cup\{i\}.
\]
Since
\[
d(C^\perp)=4,
\]
that dual word must have weight exactly \(4\). Therefore
\[
R\cup\{i\}
\]
is a weight-\(4\) dual support. This proves the exact equality
\[
\mathcal R_i
=
\{B\setminus\{i\}:i\in B,\ B\in\mathcal B_4(C^\perp)\}.
\]

There is no multiplicity ambiguity at the support level. If two nonproportional weight-\(4\) dual codewords had the same support, scale one so that one chosen coordinate agrees with the other and subtract. The result is a nonzero dual word of weight at most \(3\), contradicting
\[
d(C^\perp)=4.
\]
Thus each support carries exactly one projective dual check.

Now derive the design at coordinate \(i\). In a
\[
3\text{-}(q+1,4,\lambda)
\]
design, the blocks through a fixed point, with that point deleted, form a
\[
2\text{-}(q,3,\lambda)
\]
design. Hence \(\mathcal R_i\) has exactly
\[
b_i
=
\lambda
\frac{\binom q2}{\binom32}
=
\frac{\lambda q(q-1)}6
\]
blocks. Its point degree is
\[
r_i
=
\lambda
\frac{\binom{q-1}1}{\binom21}
=
\frac{\lambda(q-1)}2,
\]
and every pair has codegree exactly
\[
\lambda.
\]

For availability, regard \(\mathcal R_i\) as a \(3\)-uniform hypergraph. Fix one recovery triple
\[
E=\{a,b,c\}.
\]
The number of repair triples that intersect \(E\), including \(E\) itself, is
\[
|{\cal R}(a)\cup{\cal R}(b)\cup{\cal R}(c)|.
\]
By inclusion-exclusion and the design parameters this is
\[
3r_i-3\lambda+1
=
\frac{3\lambda(q-3)}2+1.
\]
A greedy matching algorithm therefore selects at least
\[
\left\lceil
\frac{b_i}
{\frac{3\lambda(q-3)}2+1}
\right\rceil
=
\left\lceil
\frac{\lambda q(q-1)}
{9\lambda(q-3)+6}
\right\rceil
\]
pairwise disjoint recovery triples.

This holds uniformly for every coordinate.

## Verification

`artifacts/verify.py` uses only the Python standard library.

It reconstructs the source's smallest example
\[
p=3,\qquad m=2,\qquad s=1,\qquad q=9,\qquad \ell=1.
\]
The code is over
\[
\mathbb F_{81}.
\]
The verifier builds \(\mathbb F_{81}\) from an irreducible quartic over \(\mathbb F_3\), selects an element of order \(q+1=10\), and reconstructs the source's \(4\times10\) generator matrix.

It exhausts all
\[
\binom{10}{4}=210
\]
four-coordinate subsets and finds exactly \(30\) dependent subsets. It verifies directly that every three-coordinate subset is contained in exactly one of these four-subsets, recovering the source
\[
3\text{-}(10,4,1)
\]
design.

For each of the ten coordinates it deletes that coordinate from the incident four-blocks and checks that the resulting twelve triples form a
\[
2\text{-}(9,3,1)
\]
design: every helper coordinate occurs four times and every helper pair occurs exactly once.

The script also checks the general design-count and greedy-availability formulas for the three source examples
\[
(q,\lambda)=(9,1),\ (25,3),\ (81,7).
\]

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Xiong, Wang, Zheng, and Ji determine the parameters of \(C\) and \(C^\perp\), prove that the minimum dual supports form a
\[
3\text{-}(q+1,4,p^\ell-2)
\]
design, and use that fact to conclude that \(C\) has all-symbol locality \(3\). Their locality proof only needs that every coordinate lies in at least one minimum dual support.

The result here uses the full design information rather than only its covering property. It shows that **every** minimum recovery triple arises from that design, identifies the complete recovery hypergraph as the derived
\[
2\text{-}(q,3,p^\ell-2)
\]
design, computes all local incidence multiplicities, and derives an explicit disjoint-repair guarantee.

Availability and multiple disjoint recovery sets are standard refinements of locality in distributed storage. General availability literature gives bounds and constructions, but the inspected sources do not identify the minimum-repair hypergraph or the availability of this September 2026 code family.

Focused searches under the article identifier, design parameters, locality, availability, disjoint repair groups, and minimum dual supports found no prior statement of the complete repair-design theorem above.

## Limitations

The availability formula is a guaranteed lower bound obtained from greedy matching in the exact repair design. It need not equal the maximum possible number of pairwise disjoint repair triples.

The result concerns minimum-cardinality recovery sets. Larger recovery sets may exist in additional forms and are not classified.

No claim is made that the derived repair designs are resolvable in general.

The design-derivation step is classical. The new content is its use to classify every minimum repair set of this specific recent code family and to extract the exact local incidence profile and disjoint-repair guarantee.

## References

1. Shiyan Xiong, Xiaoqiang Wang, Dabin Zheng, and Qinqin Ji, *Infinite families of 3-designs from linear and nonlinear codes*, arXiv:2609.15525v1, first public 14 September 2026.
2. Ankit Singh Rawat, Dimitris S. Papailiopoulos, Alexandros G. Dimakis, and Sriram Vishwanath, *Locality and availability in distributed storage*, IEEE Transactions on Information Theory 62 (2016), 4481--4493.
