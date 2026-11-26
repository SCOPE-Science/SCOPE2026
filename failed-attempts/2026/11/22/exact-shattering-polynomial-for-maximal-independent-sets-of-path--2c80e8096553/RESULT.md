# Exact shattering polynomial for maximal independent sets of paths

## Finding

For every integer \(n\geq1\), let \(P_n\) be the path on the ordered vertices \([n]=\{1,\ldots,n\}\), and let \(\mathcal M_n\) be **all inclusion-maximal independent vertex sets** of \(P_n\). A support \(S\subseteq[n]\) is *shattered* if for every \(T\subseteq S\) some \(I\in\mathcal M_n\) satisfies \(I\cap S=T\). Define \(\Phi_n(z)=\sum_{S\text{ shattered}}z^{|S|}\), with the empty support counted once.

The complete two-variable generating function is
\[
\boxed{\sum_{n\ge0}\Phi_n(z)t^n=\frac{1+2t^2z-t^3z}{1-t-2t^3z+t^4z},}\qquad \Phi_0(z):=1.
\]
For every \(k\ge1\), the number of shattered supports of size \(k\) is zero if \(n<3k-1\), and otherwise equals
\[
\boxed{c_{n,k}=\sum_{r=0}^k\binom{k}{r}\binom{n-3k+1+r}{r}.}
\]
The constant coefficient is \(c_{n,0}=1\). Consequently,
\[
\boxed{\operatorname{VCdim}(\mathcal M_n)=\left\lfloor\frac{n+1}{3}\right\rfloor,\qquad n\ge1,}
\]
and for \(n=3k-1\) exactly \(2^k\) maximum-size shattered supports exist. The associated shattering complex need not be pure: at \(n=5\), the singleton \(\{3\}\) is an inclusion-maximal shattered support, while four shattered supports have size two.

There is also an exact **pairwise reachability test** for every individual support. Form a directed acyclic graph on the vertices \(L,1,\ldots,n,R\), with edges from \(L\) to \(1,2\) when available, from \(i\) to \(i+2,i+3\) when at most \(n\), and from \(n-1,n\) to \(R\) when available. For distinct endpoints \(x,y\), let \(x\leadsto_F y\) mean that some directed \(x\)-to-\(y\) path has no interior vertex in \(F\). Then \(S\) is shattered if and only if all of the following hold:

1. \(L\leadsto_S R\).
2. For each \(a\in S\), both \(L\leadsto_{S\cap[1,a-1]}a\) and \(a\leadsto_{S\cap[a+1,n]}R\).
3. For each pair \(a<b\) in \(S\), \(a\leadsto_{S\cap(a,b)}b\).

This replaces testing exponentially many trace labelings by polynomially many ordinary reachability queries.

## Assumptions and scope

Graphs are simple paths and all maximal independent sets are included, **not just largest or minimum-cardinality independent dominating sets**. The ground set is the set of vertices, queried by Boolean membership. No claim is made about arbitrary graphs, cycles or exact adaptive Littlestone dimensions. For \(n=0\), the unique empty hypothesis and empty support are included only to normalize the generating series.

## Proof

**1. Maximal-independent-set encoding.** An independent set is maximal precisely when it dominates every unselected vertex. In a path, if its selected vertices are \(i_1<\cdots<i_q\), the first selected vertex belongs to \(\{1,2\}\), consecutive selected vertices differ by exactly two or three, and the last belongs to \(\{n-1,n\}\). This is exactly the set of directed \(L\)-to-\(R\) paths in the graph in the Finding, with selected vertices as its interior vertices. For \(n=1\) the same statement holds after omitting nonexistent vertices.

**2. Pairwise test.** If \(S\) is shattered, the all-zero labeling gives condition 1; each single-positive labeling gives the two paths of condition 2; and the labeling positive exactly at \(a,b\) gives condition 3. Conversely, for any labeling with positive queried vertices \(a_1<\cdots<a_j\), concatenate a path from \(L\) to \(a_1\), paths from \(a_i\) to \(a_{i+1}\), and a path from \(a_j\) to \(R\). The tests guarantee that no negatively labeled support vertex occurs internally in these paths. Each connection is strictly forward, so concatenation is a legitimate directed path. When \(j=0\), condition 1 supplies the path. The result is an independently dominating set that has precisely the desired trace. This proves the if-and-only-if statement, with no enumeration assumptions.

**3. Finite automaton that recognizes every shattered support.** The legal selected/unselected words are recognized by the following partial deterministic automaton. Its prefix states are \(q_0\) (start), \(q_1\) (a leading zero), \(q_2\) (last symbol one), \(q_3\) (a zero after a one), and \(q_4\) (two zeros after a one). Undefined transitions reject. The accepting states are \(q_2,q_3\).

| Prefix state | Read 0 | Read 1 |
|:--|:--|:--|
| \(q_0\) | \(q_1\) | \(q_2\) |
| \(q_1\) | undefined | \(q_2\) |
| \(q_2\) | \(q_3\) | undefined |
| \(q_3\) | \(q_4\) | \(q_2\) |
| \(q_4\) | undefined | \(q_2\) |

For an input bit specifying whether a coordinate is queried, keep a **family of possible-prefix state subsets**, one for each labeling of the queried coordinates. Starting with the family containing just \(\{q_0\}\): at an unqueried coordinate replace every subset \(U\) by the union of its valid 0- and 1-successors; at a queried coordinate replace \(U\) by both successor subsets separately. Empty subsets are retained because they witness an impossible labeling. A support is shattered exactly when every final member subset intersects \(\{q_2,q_3\}\).

Exhaustively applying these two explicit finite transition operations produces exactly 28 reachable families. Grouping families with identical acceptance and future behavior gives six classes: \(A,B,E,C,F,D\), listed below in a convenient order. Their complete transition table (where 0 means *unqueried* and 1 means *queried*) is:

| Class | 0 | 1 | Accepting? |
|:--|:--|:--|:--|
| \(A\) (initial) | \(B\) | \(E\) | no |
| \(B\) | \(B\) | \(C\) | yes |
| \(E\) | \(C\) | \(F\) | no |
| \(C\) | \(D\) | \(F\) | yes |
| \(F\) | \(F\) | \(F\) | no |
| \(D\) | \(B\) | \(E\) | yes |

The separately supplied `checker.py` reconstructs all 28 families from the five explicitly given prefix transitions, computes their six-class stable quotient, verifies each transition and acceptance bit displayed above, and cross-checks the resulting language against raw MIS traces. The 28-state transition certificate is also included as `automaton_certificate.json`. Thus the finite algebraic step is a completely specified exhaustive **finite proof obligation**, rather than an inference from any finite list of word lengths. All lengths are covered because the transition invariant follows by induction on the length of the scanned prefix.

**4. Transfer calculation.** For each class \(X\), let \(H_X(t,z)\) be the sum of weights \(t^{\ell}z^s\) over accepted suffixes of length \(\ell\) with \(s\) marked coordinates. From the table,
\[
\begin{aligned}
H_A&=t(H_B+zH_E),\\
H_B&=1+t(H_B+zH_C),\\
H_E&=tH_C,\\
H_C&=1+tH_D,\\
H_D&=1+t(H_B+zH_E),\\
H_F&=0.
\end{aligned}
\]
Solving these five linear identities and restoring the empty-path term gives
\[
1+H_A=\frac{1+2t^2z-t^3z}{1-t-2t^3z+t^4z}.
\]
In particular, expanding as a formal power series in \(z\), for every \(k\ge1\) one obtains the exact coefficient generating series
\[
[z^k](1+H_A)=\frac{t^{3k-1}(2-t)^k}{(1-t)^{k+1}}.
\]
Writing \(2-t=1+(1-t)\) and applying the negative-binomial expansion yields the nonnegative binomial sum in the Finding. Its first nonzero power of \(t\) is \(t^{3k-1}\), with coefficient \(2^k\). Hence a \(k\)-element shattered support exists exactly when \(n\ge3k-1\), and the VC formula and extremal count follow. At \(n=5\), the support \(\{3\}\) cannot be extended to a shattered pair, while \(\{1,4\},\{2,4\},\{1,5\},\{2,5\}\) are shattered, proving the nonpurity assertion.

## Verification

Run `python3 checker.py` from a directory containing the delivered code. The checker reconstructs the prefix automaton, its reachable families and quotient, checks the six-state table, compares direct maximal-independent-set traces with the independent pairwise reachability test for **every** support through length 13 (16,382 supports), and checks agreement of the transfer automaton with the closed coefficient formula through length 100. Exact output from that replay is included as `verification_output.txt`.

No finite trace check is used to extrapolate to infinite length. The all-length proof is the finite-state invariant, the completely enumerated quotient certificate, and formal generating-function algebra.

## Relationship to prior work

Hunter R. Johnson's *Binary strings of finite VC dimension* (arXiv:2101.06490, first public 2021-01-16, primary MSC 03C45) investigates the VC behavior of a fixed binary sequence and its translates/substrings; it does not enumerate all coordinate-shattering supports of the family of maximal independent sets of finite paths. Beaton, Brown and Cameron, *Independence Equivalence Classes of Paths and Cycles* (arXiv:1810.05317, first public 2018-10-12), study the ordinary independence polynomial of all independent sets, not the face polynomial of supports shattered by maximal independent sets.

The general result of Liu, Shangguan, Skokan and Xu (SoCG 2024, Lemma 27) gives an induced-matching upper bound on the VC dimension of maximal-independent-set membership systems; its argument does not count path-specific shattered supports. Related records already establish the **same VC dimension** for maximal-independent-set concepts on paths and exhibit an adaptive/static gap, while a separate record derives a full shattering polynomial for cycles. Therefore the numerical VC-dimension identity alone is *not* offered as new. The claim assessed here is the all-length exact path support enumerator, the individual-support criterion, and its finite-state proof; neither follows merely from those known VC values or from closing a path to a cycle.

## Limitations

No statement about exact Littlestone dimension is made. Related indexed path and cycle works had accessible summaries but not their full repository documents, so their appendices could contain an equivalent path enumeration; this is an explicitly unresolved historical-priority risk, not evidence of uniqueness. No independent mathematical audit has been performed. The computational tests cover only stated finite ranges; the formal proof extends the formula to all lengths.

## References

1. Hunter R. Johnson, *Binary strings of finite VC dimension*, arXiv:2101.06490 (v1 2021-01-16), https://arxiv.org/html/2101.06490v2 .
2. Iain Beaton, Jason I. Brown and Ben Cameron, *Independence Equivalence Classes of Paths and Cycles*, arXiv:1810.05317 (v1 2018-10-12), https://arxiv.org/abs/1810.05317 .
3. *Linear static–online shattering separation for maximal independent sets of paths*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-linear-static-online-shattering-separation-for-maximal-independe--1d3f970e51af .
4. *Complete shattering polynomial and forbidden-gap law for maximal independent sets of cycles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-complete-shattering-polynomial-and-forbidden-gap-law-for-maximal--4d0afc364bee .

5. Hong Liu, Chong Shangguan, Jozef Skokan and Zixiang Xu, *Beyond Chromatic Threshold via (p,q)-Theorem, and Blow-Up Phenomenon*, SoCG 2024, Lemma 27, https://doi.org/10.4230/LIPIcs.SoCG.2024.71 .
