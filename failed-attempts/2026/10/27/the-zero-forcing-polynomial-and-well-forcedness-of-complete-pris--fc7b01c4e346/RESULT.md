# The zero-forcing polynomial and well-forcedness of complete prisms

## Finding
For every integer \(n\ge3\), consider the complete prism \(H_n=K_n\square K_2\). Its vertex set consists of two cliques \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), with the matching edge \(a_ib_i\) for each \(i\in[n]\) and no other cross-layer edges. Under standard zero forcing, an initially blue vertex with exactly one white neighbor may turn that neighbor blue; \(S\) is zero forcing if successive applications color every vertex.

**Theorem.** Let \(u=|A\setminus S|\), \(v=|B\setminus S|\). The set \(S\) is zero forcing exactly in one of the following disjoint regimes:

1. \(u=0\) or \(v=0\).
2. \(u=v=1\).
3. \(u=1\) and \(2\le v\le n-2\), or the version interchanging \(A,B\).
4. \(u=1\), \(v=n-1\), and the sole initially blue vertex in \(B\) has index different from the sole initially white vertex in \(A\); or the interchanged version.

Here the first regime is counted only once when both layers are entirely blue; the third is empty when \(n=3\). Consequently, the complete zero-forcing polynomial is
\[
\boxed{\mathcal Z(H_n;z)=2z^n(1+z)^n-z^{2n}+n^2z^{2n-2}+2n\sum_{v=2}^{n-2}\binom nv z^{2n-1-v}+2n(n-1)z^n.}
\]
The coefficient of \(z^k\) is the number of labeled zero-forcing sets of cardinality \(k\).

Every zero-forcing set contains a zero-forcing subset of cardinality \(n\). Thus \(H_n\) is *well-forced*: all inclusion-minimal zero-forcing sets have the same cardinality, \(n\). The \(2n(n-1)+2\) minimum sets are exactly the two clique layers and the \(2n(n-1)\) sets
\[
(A\setminus\{a_j\})\cup\{b_i\},\qquad (B\setminus\{b_j\})\cup\{a_i\},\qquad i\ne j.
\]
In particular,
\[
\mathcal Z(H_n;1)=2(n+1)2^n-n^2-6n-1
\]
and a uniform random vertex subset is zero forcing with probability
\[
\frac{n+1}{2^{n-1}}-\frac{n^2+6n+1}{4^n}.
\]
The probability tends to zero exponentially with \(n\).

## Assumptions and scope
Graphs are finite, simple, and undirected, with the Cartesian product adjacency defined above. All vertices and initial colorings are labeled, and the standard, not positive-semidefinite or skew, zero-forcing rule is used. Statements hold for every integer \(n\ge3\). The three-layer notation is never used; \(A\) and \(B\) are precisely the two matched cliques. No claim is made for \(n=1,2\).

## Proof
Write \(U=A\setminus S\) and \(V=B\setminus S\), with sizes \(u,v\). An initially blue \(a_i\) sees precisely \(u\) white neighbors inside its clique and, additionally, possibly the white mate \(b_i\); the analogous statement holds for initially blue \(b_i\).

**Necessity and sufficiency of the four regimes.** If \(u\ge2\) and \(v\ge2\), each initially blue vertex has at least two white clique neighbors, so no force is possible. If \(u=0\), every initially white vertex \(b_i\) is the unique white neighbor of its already blue mate \(a_i\), so all white vertices can be forced immediately; likewise when \(v=0\). If \(u=v=1\), with white \(a_j,b_k\), there is an index \(i\notin\{j,k\}\), since \(n\ge3\). Both \(a_i\) and \(b_i\) are blue. Vertex \(a_i\) forces \(a_j\), after which all vertices of \(A\) are blue and they can force any remaining white vertices of \(B\).

Suppose \(u=1\) and \(v\ge2\). Every initially blue vertex of \(B\) has at least two white neighbors in \(B\), so no such vertex forces initially. Writing \(U=\{a_j\}\), a blue \(a_i\) can force \(a_j\) precisely if \(i\ne j\) and its mate \(b_i\) is blue. Once \(a_j\) is forced, all of \(A\) is blue, which subsequently forces the remaining whites in \(B\). Consequently success is equivalent to the existence of an index \(i\ne j\) with \(b_i\notin V\). Such an index exists automatically if \(v\le n-2\), and when \(v=n-1\) exists exactly if the sole blue vertex in \(B\) has index different from \(j\). When \(v=n\), it cannot exist. Interchanging the layers completes all cases. This accounts also for configurations where one layer initially has zero white vertices.

**Counting.** The first regime contributes \(2z^n(1+z)^n-z^{2n}\), by inclusion-exclusion. The \(u=v=1\) regime has \(n^2\) choices, each with \(2n-2\) blue vertices, contributing \(n^2z^{2n-2}\). For each \(v\in\{2,\ldots,n-2\}\) in the third regime, there are \(n\binom nv\) choices with \(2n-1-v\) blue vertices, doubled by layer interchange. For the fourth, each choice of white \(a_j\) allows \(n-1\) blue mates \(b_i\) with \(i\ne j\); doubling yields \(2n(n-1)z^n\). This gives the stated polynomial without overlapping regimes.

**Minimum and inclusion-minimality.** No successful configuration has fewer than \(n\) selected vertices, as follows directly from the four regimes. Exactly the two whole layers and fourth-regime sets have \(n\) blue vertices; the \(u=v=1\) regime has \(2n-2\ge n\), with equality only when \(n=2\), outside scope. All third-regime sets have at least \(n+1\) selected vertices. For \(n\ge3\), even when \(n=3\), the \(u=v=1\) regime has \(2n-2=4>3=n\). To prove the stronger assertion, a successful set of the first regime already contains an entire layer. A successful set with \(u=1\) and \(2\le v\le n-2\) has at least two blue vertices in \(B\), one of which is indexed differently from its white \(a_j\); retaining \(A\setminus\{a_j\}\) plus that one blue \(b_i\) gives a successful minimum set. A fourth-regime set is already minimum. In the \(u=v=1\) regime, choose \(b_i\) initially blue with \(i\ne j\) (exists because \(n\ge3\) and the initially white indices are at most two). Then \((A\setminus\{a_j\})\cup\{b_i\}\subseteq S\) is minimum. Every successful set thus contains a successful \(n\)-subset. A minimum-cardinality successful subset is automatically inclusion-minimal, which establishes well-forcedness and the claimed complete minimum-set census.

**Total count and random probability.** Substitute \(z=1\). The third-regime sum is \(2n(2^n-2-2n)\), because \(\sum_{v=2}^{n-2}\binom nv=2^n-2-2n\) for \(n\ge3\). After collecting all terms, \(\mathcal Z(H_n;1)=2(n+1)2^n-n^2-6n-1\). Since there are \(2^{2n}\) equally likely initial subsets, division gives the probability formula. Every displayed equality is exact for all claimed orders.

## Verification
The supplied standalone `verify.py` constructs the two cliques and cross matching directly, applies the standard color-change rule to each of the \(2^{2n}\) initial blue subsets for every \(3\le n\le8\), and independently compares every coefficient with the theorem. It also computes inclusion-minimal successful sets from the original rule, confirms their exclusive size \(n\), and checks the total-set and minimum-set formulas. Execution terminates with `VERIFY_OK`. These finite enumerations are diagnostic checks only; the preceding case analysis proves the result for every \(n\ge3\).

## Relationship to prior work
Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips and Reinhart introduced the zero-forcing polynomial and enumerated several classic graph families, but do not give this matched-clique-prism polynomial. Pelayo and Abara study maximal failed sets for graph products and cite the scalar failed-zero-forcing number \(F(K_n\square K_m)=nm-4\) for \(n\ge4,m\ge2\); that scalar property neither counts every successful set nor proves well-forcedness. Grood, Haas, Jacob, King and Nasserasr define well-forced graphs and characterize trees, whereas complete prisms have many triangles. Cameron et al. study forts, fractional zero forcing and Cartesian products, not this all-cardinality enumeration. An earlier detailed classification of all minimal forts of rook graphs gives a *feasibility obstruction* for each selected set via fort hitting, but its structural fort classification and fort count do not state this closed success-set polynomial, its minimum-set census, or the well-forced conclusion. In particular, no inference of novelty is based merely on a different invariant name; the distinct all-coefficient combinatorial count is what is assessed.

## Limitations
This result treats only the standard zero-forcing rule and complete prisms with \(n\ge3\), not arbitrary rectangular rook graphs. A closed form is obtained for labeled subsets, not for symmetry orbits. The result does not establish new bounds on general zero-forcing parameters. Extensive accessible literature comparisons were conducted, but unindexed or differently expressed prior work could still contain equivalent statements. The finite checks are not substitutes for the proof.

## References
- K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips and C. Reinhart, “The zero forcing polynomial of a graph,” arXiv:1801.08910 (first publicly posted 2018-01-26), https://arxiv.org/pdf/1801.08910.
- P. A. B. Pelayo and M. N. M. Abara, “Maximal failed zero forcing sets for products of two graphs,” arXiv:2202.04997 (first publicly posted 2022-02-10), https://arxiv.org/pdf/2202.04997.
- T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal and H. Schuerger, “Forts, (fractional) zero forcing, and Cartesian products of graphs,” arXiv:2310.17904, https://arxiv.org/pdf/2310.17904.
- C. Grood, R. Haas, B. Jacob, E. King and S. Nasserasr, “Well-forced graphs,” arXiv:2312.14298, https://arxiv.org/pdf/2312.14298.
- K. Menon and A. Singh, “Exploring the influence of graph operations on zero forcing sets,” Discrete Mathematics 348 (2025), 114516, doi:10.1016/j.disc.2025.114516.
