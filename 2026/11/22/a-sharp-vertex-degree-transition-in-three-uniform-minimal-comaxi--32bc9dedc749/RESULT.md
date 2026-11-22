# A sharp vertex-degree transition in three-uniform minimal comaximal hypergraphs

## Finding

Consider the minimal comaximal hypergraph \(\mathcal H_k(R)\) of a finite commutative ring \(R\), with vertex set consisting of the nonunits outside the Jacobson radical and edges consisting of irredundant \(k\)-element families generating the unit ideal. We determine the degree of **each individual vertex**, including for rings with nonzero Jacobson radical and unequal residue-field sizes. In the Boolean-ring family \(R=\mathbb F_2^n\), the resulting rank-three degree spectrum has a sharp, eventually stable maximum-degree support class.

**Theorem.** Let \(R\) be finite, commutative and unital, with \(n\ge3\) maximal ideals \(M_1,\dots,M_n\), Jacobson radical of cardinality \(j\), and residue-field cardinalities \(q_i=|R/M_i|\). Fix \(2\le k\le n\). For a vertex \(x\) put
\[
C(x)=\{i:x\notin M_i\},\qquad C=C(x),\qquad C^c=[n]\setminus C.
\]
Its incidence degree is exactly
\[
\boxed{\deg_{\mathcal H_k(R)}(x)=
\frac{j^{k-1}}{(k-1)!}
\left(\prod_{i\in C}q_i^{k-1}-\prod_{i\in C}(q_i^{k-1}-1)\right)
\sum_{a=0}^{k-1}(-1)^a\binom{k-1}{a}
\prod_{i\in C^c}\left(q_i^{k-1}-1-a(q_i-1)\right).}
\]
All products over empty index sets are defined to be \(1\). The formula is integral and is zero if \(|C|>n-k+1\). Each vertex in the same co-support class has the same degree.

In particular, for \(R_n=\mathbb F_2^n\) and \(k=3\), a vertex with \(|C(x)|=s\), \(1\le s\le n-1\), has
\[
\boxed{d_n(s)=\frac{(4^s-3^s)(3^{n-s}-2^{n-s+1}+1)}{2}.}
\]
There are precisely \(\binom ns\) vertices of this degree before coincident degree values are merged. The maximum vertex degree \(\Delta_n\) and all of its maximizing vertices are given by
\[
\boxed{
\begin{array}{c|c|c}
\text{range}&\text{unique maximizing support size }s&\Delta_n\\\hline
n=3&1&1\\
n=4&2&7\\
5\le n\le10&n-3&6(4^{n-3}-3^{n-3})\\
n\ge11&n-4&25(4^{n-4}-3^{n-4})
\end{array}}
\]
Thus the mode first moves away from the \(n-2\) support stratum at \(n=5\), and crosses from \(n-3\) to \(n-4\) **exactly at \(n=11\)**. At \(n=10\) the degree maxima are \(85{,}182\) in support \(7\); at \(n=11\) they are \(354{,}925\) in support \(7\), strictly exceeding the \(353{,}850\) at support \(8\). In every case the number of maximizing vertices is \(\binom n{s}\).

## Assumptions and scope

The ring is finite and commutative with identity. Distinct maximal ideals are numbered, but the formula is permutation-invariant. All \(q_i\) are prime powers of size at least two. We take \(2\le k\le n\), and \(x\) is a nonunit outside the Jacobson radical; thus \(\emptyset\ne C(x)\subsetneq[n]\). An edge is a set, not an ordered tuple; \(\deg(x)\) counts edges containing \(x\). The ring \(\mathbb F_2^n\) is the direct product of \(n\) copies of the two-element field; its elements are binary support vectors.

## Proof

**1. Ring-theoretic reduction.** By the Chinese remainder theorem the natural homomorphism \(R\to\prod_i R/M_i\) is surjective with kernel \(J(R)\) of size \(j\). A tuple generates the unit ideal if and only if every residue coordinate has a nonzero entry among its members. Such a family is irredundant precisely if each member has a *private coordinate* where it alone has nonzero residue. Thus any irredundant family has distinct members and distinct nonempty proper co-supports; every compatible tuple of residue vectors lifts to exactly \(j\) elements per unfixed family member.

**2. Fix a vertex.** Fix \(x\) and order its \(k-1\) prospective partners. At every coordinate \(i\in C\) the other members' residues can be arbitrary, giving \(q_i^{k-1}\) possibilities, but \(x\) has a private coordinate if and only if at least one such coordinate has all partner residues zero. The number of choices is therefore
\[
P_C=\prod_{i\in C}q_i^{k-1}-\prod_{i\in C}(q_i^{k-1}-1).
\]
At each coordinate outside \(C\), at least one partner must be nonzero to achieve comaximality; that gives \(q_i^{k-1}-1\) residue choices. Each partner must also have at least one private coordinate outside \(C\). For any designated \(a\) partners prohibited from having a private coordinate, exactly \(a(q_i-1)\) singleton residue patterns must be excluded at coordinate \(i\notin C\). Inclusion–exclusion over the \(k-1\) partners consequently gives
\[
Q_{C^c}=\sum_{a=0}^{k-1}(-1)^a\binom{k-1}{a}
\prod_{i\notin C}(q_i^{k-1}-1-a(q_i-1)).
\]
The \(k-1\) partners each have \(j\) independent lifts, so the ordered count is \(j^{k-1}P_CQ_{C^c}\). Every admissible unordered edge containing fixed \(x\) appears exactly \((k-1)!\) times among those ordered partners. This proves the first formula, including integrality and all boundary cases.

**3. Boolean rank three.** Now \(j=1\), all \(q_i=2\) and \(k=3\). On the \(s\) coordinates of \(C\) the private-coordinate factor is \(4^s-3^s\). On its \(t=n-s\) complementary coordinates, inclusion–exclusion gives
\[
(4-1)^t-2(4-1-(2-1))^t+(4-1-2(2-1))^t
=3^t-2^{t+1}+1.
\]
Division by two proves \(d_n(s)\). At \(t=1\) the latter factor is zero, matching the isolated-support boundary.

**4. Sharp maximum.** Write \(A_s=4^s-3^s\) for \(s\ge1\), and \(B_t=3^t-2^{t+1}+1\) for \(t\ge2\). Then \(d_n(n-t)=A_{n-t}B_t/2\). For every \(s\ge1\),
\[
\frac{A_{s+1}}{A_s}=4+\frac{1}{(4/3)^s-1}>4.
\]
For \(t\ge5\),
\[
B_t-4B_{t-1}=2^{t+1}-3^{t-1}-3<0.
\]
Hence \(d_n(n-(t-1))>d_n(n-t)\) whenever \(t\ge5\); only the three possible codimensions \(t=2,3,4\) can maximize.

The values \(B_2=2\), \(B_3=12\), \(B_4=50\) give the remaining comparisons. For \(n\ge5\), \(A_{n-2}/A_{n-3}<6\), so codimension \(3\) strictly dominates codimension \(2\). For \(n\ge5\), codimension \(4\) strictly beats codimension \(3\) precisely if
\[
\frac{A_{n-3}}{A_{n-4}}<\frac{25}{6}
\quad\Longleftrightarrow\quad
(4/3)^{n-4}>7.
\]
The last inequality first holds when \(n=11\) and remains true thereafter; it is never an equality for an integer \(n\). For \(n=3\) only codimension two is admissible, and for \(n=4\) its degree \(7\) strictly exceeds the codimension-three degree \(6\). All cases and uniqueness follow.

## Verification

The included dependency-free `verify.py` independently enumerates all vertices and all irredundant edges, using literal residue-unit conditions instead of evaluating the closed formula to decide edge membership. It checks the exact degree of each individual vertex, for \(\mathbb F_2^n\) through \(n=8\), three heterogeneous finite products for \(k=2,3\), and the nonreduced ring \((\mathbb Z/4\mathbb Z)\times\mathbb F_3\times\mathbb F_2\) for \(k=2,3\). Its separate arithmetic mode check covers \(3\le n\le30\); the proof in Step 4, not this finite range, establishes the all-dimensional transition. The recorded command is `python3 verify.py` and the output is `verification_output.txt`; success ends with `VERIFY_OK`. These tests are checks, not substitutes for the general proof.

## Relationship to prior work

Mehdi-Nezhad (2026), first public November 5, proves the co-support covering/blow-up correspondence and reconstructs automorphism and isomorphism information for these minimal comaximal hypergraphs. That correspondence is used as known context, not claimed new. Selvakumar and Amritha (2020) study the same \(k\)-maximal edge notion, including an \(n\)-uniform regularity criterion; their result does not classify the individual degrees in rank three for arbitrary \(n\). The classical minimal-cover enumeration (Hearne–Wagner, Royle, and OEIS A035348) counts **total** minimal coverings, which does not determine vertex-degree strata or maximum-degree support classes. An exact total-edge formula for finite commutative rings is also previously available and is not part of the novelty claim here. The contribution assessed is the all-residue-profile *fixed-vertex* degree formula and particularly the sharp \(n=11\) degree-mode transition.

## Limitations

This is an exact enumeration and optimization for the specified hypergraphs; it does not assert broader extremal theorems for arbitrary hypergraphs or classify maxima for all \(k\) and heterogeneous residue profiles. While the sources examined do not state the fixed-vertex formula or the \(n=11\) transition, independently archived counting results using different terminology may exist. This work has undergone self-review, not independent validation.

## References

1. E. Mehdi-Nezhad, *Isomorphisms and automorphisms of minimal comaximal hypergraphs of commutative rings*, arXiv:2611.07992v1 (first public November 5, 2026). https://arxiv.org/abs/2611.07992
2. K. Selvakumar and V. C. Amritha, *The k-maximal hypergraph of commutative rings*, Beiträge zur Algebra und Geometrie 61 (2020), DOI:10.1007/s13366-020-00505-8. https://doi.org/10.1007/s13366-020-00505-8
3. E. W. Weisstein, *Minimal Cover*, MathWorld, https://mathworld.wolfram.com/MinimalCover.html (including references to T. Hearne–C. Wagner and G. Royle and OEIS A035348).
