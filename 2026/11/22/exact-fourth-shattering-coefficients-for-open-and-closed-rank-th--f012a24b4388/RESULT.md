# Exact fourth shattering coefficients for open and closed rank-three Kneser neighborhoods

## Finding

Let \(n\ge3\) be an integer, and let \(G_n=\operatorname{KG}(n,3)\) be the graph whose vertices are the three-element subsets of \([n]\), adjacent exactly when they are disjoint. For \(\tau\in\{\circ,\bullet\}\), let \(s_4^\tau(n)\) denote the number of **unordered** sets of four distinct vertices shattered by the open (\(\circ\)) or closed (\(\bullet\)) vertex-neighborhood concept family. Define \(\binom{n}{u}=0\) for \(u>n\).

**Theorem.** For every \(n\ge3\), both exact fourth coefficients are
\[
s_4^\tau(n)=\sum_{(u,e)\in B_\tau}c_{u,e}^\tau\binom{n}{u}\,\mathbf1_{\{n\ge u+e\}},
\]
with the following complete coefficient tables. A row \((u,e,c)\) contributes \(c\binom{n}{u}\) precisely when \(n\ge u+e\).

| \(u\) | Minimum unused elements \(e\) | Open coefficient \(c_{u,e}^{\circ}\) |
|---:|---:|---:|
| 6 | 3 | 15 |
| 7 | 3 | 2310 |
| 8 | 3 | 32060 |
| 9 | 3 | 105525 |
| 10 | 3 | 129150 |
| 11 | 3 | 69300 |

| \(u\) | Minimum unused elements \(e\) | Closed coefficient \(c_{u,e}^{\bullet}\) |
|---:|---:|---:|
| 6 | 3 | 15 |
| 7 | 3 | 4830 |
| 8 | 2 | 560 |
| 8 | 3 | 66780 |
| 9 | 2 | 25200 |
| 9 | 3 | 87885 |
| 10 | 1 | 100800 |
| 10 | 3 | 28350 |
| 11 | 1 | 69300 |

In particular, \(s_4^{\circ}(n)=s_4^{\bullet}(n)=0\) through \(n=8\), and both equal \(1260\) at \(n=9\). At that first order, **every** shattered four-support in either family has the unique form
\[
\bigl\{\{a,b,x_1\},\{a,b,x_2\},\{a,b,x_3\},\{a,b,x_4\}\bigr\},
\]
where the six displayed ground points are distinct. There are exactly \(\binom92\binom74=1260\) such supports. At \(n=10\), the exact counts separate: \(s_4^{\circ}(10)=280350\) and \(s_4^{\bullet}(10)=607950\).

For \(n\ge14\), both formulas become ordinary binomial polynomials; their difference simplifies to
\[
s_4^{\bullet}(n)-s_4^{\circ}(n)
=2520\binom n7+35280\binom n8+7560\binom n9.
\]
Both fourth coefficients have the same leading term \(69300\binom n{11}\), so their relative discrepancy tends to zero. These are coefficients counting shattered supports, **not** the usual maximum-trace shatter function.

## Assumptions and scope

The underlying set has exactly \(n\) distinguishable elements. The graph is finite, simple and undirected. A queried graph vertex is a three-element subset. A neighborhood center ranges over **all** graph vertices, including centers that happen to be queried. The open neighborhood excludes the center itself; the closed neighborhood includes it. A support is shattered only when all \(16\) possible labelings on its four different vertices are realized. The theorem concerns exactly the degree-four support counts; it does not claim to determine the entire all-order shattering polynomials or any higher-degree coefficients.

## Proof

**Step 1: Exhaustive finite shape reduction.** Order four distinct queried triples as \(F_1,F_2,F_3,F_4\), and write \(U=\bigcup_iF_i\), \(u=|U|\le12\). Each point \(x\in U\) has its nonempty Venn signature \(\sigma(x)=\{i:x\in F_i\}\subseteq[4]\). Let \(a_\sigma\) count points of signature \(\sigma\). Then
\[
a_\sigma\ge0,\qquad \sum_{\sigma\ni i}a_\sigma=3\ (i=1,2,3,4).
\]
The four query vertices are distinct exactly when their four membership rows are pairwise different. Every tuple satisfying these integer constraints and distinctness is realizable, uniquely up to relabeling the \(u\) used ground points, and every ordered four-support produces such a tuple. The recursion in `verify_kneser_rank_four.py` exhaustively enumerates **666** valid ordered-signature profiles; it discards **196** additional profiles with repeated query vertices. The reduction is exhaustive for every \(n\), not an enumeration of only small ambient orders.

**Step 2: Exact trace test for each profile.** Given a center triple \(C\), the open trace is
\[
T_\circ(C)=[4]\setminus\bigcup_{x\in C\cap U}\sigma(x),
\]
and the closed trace is
\[
T_\bullet(C)=T_\circ(C)\cup\{i:C=F_i\}.
\]
Only the **number**, not the names, of points outside \(U\) matters. A center has three elements, so using more than three external points creates no new traces. For each valid profile, the verifier constructs the four actual triple vertices from its Venn cells, and tests all center triples for \(e=0,1,2,3\) external points. It records the least \(e\) realizing all sixteen traces, if any. The trace sets grow monotonically with \(e\), so a profile whose minimum is \(e\) is shattered on \([n]\) exactly when \(n\ge u+e\). This proves that the finite test classifies all ambient sizes.

**Step 3: Exact multiplicities.** For a fixed ordered profile with \(u\) used vertices, the number of placements on a prescribed \(u\)-element ground subset is
\[
\frac{u!}{\prod_{\varnothing\ne\sigma\subseteq[4]}a_\sigma!}.
\]
There are \(\binom n u\) choices of this ground subset. Each unordered support corresponds to exactly \(4!=24\) ordered ones, since its queried triples are distinct. Thus summing the displayed factorial weights over all profiles with a given \((u,e)\), and dividing by \(24\), yields the coefficients in the two tables. Every division and comparison is integer exact. The verifier checks both tables directly and also checks the identity \(\sum_{u\le9}\binom9u\sum_{a:|U|=u}u!/\prod a_\sigma!=84\cdot83\cdot82\cdot81\), covering all ordered four-supports at ambient order nine.

**Step 4: First-order rigidity and consequences.** At \(n=9\), the only possible successful profile in either table has \((u,e)=(6,3)\); the exhaustive profile inspection has exactly one such ordered signature profile, consisting of two points of signature \(\{1,2,3,4\}\) and four private points of singleton signatures. This gives precisely the common-two-core supports stated above. Conversely, any such support is shattered: for every trace containing at least one positive query, a center avoids the shared core and contains exactly the private petals of the negative queries, padded by the three external elements; the empty trace can be realized by a center containing the common core and one external point. The same centers work for open and closed neighborhoods because none is a queried triple. Counting chooses the core and then its four distinct petals. The formulas at \(n=10\), the stable difference, and the matching leading terms follow by substitution and collection of binomial terms.

## Verification

Run `python3 verify_kneser_rank_four.py`. Its standard-library-only routine enumerates all nonempty signatures with four row sums equal to three, rejects duplicate queried vertices, builds each query family, checks all possible three-element centers for each needed external-point count, and sums the exact factorial multiplicities. It checks 666 admissible profiles, both entire coefficient tables, the ordered-support checksum at order nine, and small-order evaluations through twelve.

As a second, algorithmically different check, run `c++ -O3 -std=c++17 direct_kg9.cpp -o direct_kg9` followed by `./direct_kg9`. This iterates every four-support among the \(84\) graph vertices of \(\operatorname{KG}(9,3)\), along with all smaller supports, and directly computes open and closed trace sets without Venn reduction. It returns \(1,84,3486,26460,1260\) and \(1,84,3486,56700,1260\), respectively, for support cardinalities zero through four. The profile reduction is the justification for extrapolating the exact finite certificate to *all* ground orders; these small-order checks alone would not establish an infinite theorem.

## Relationship to prior work

Adler, Benediktsson, and Macpherson (first public 2020) analyze the neighborhood relation of Johnson and Hamming graphs. Their Johnson adjacency on triples means overlap in **two** ground elements, not disjointness, so their results do not determine these Kneser coefficients. Coudert, Csikós, Ducoffe and Viennot (2024) give a general graph VC-dimension algorithm; their work does not state the two all-order fourth-coefficient formulas. A previously published exact rank-three Kneser **VC-dimension** classification gives the first order with a shattered four-support and its existence witness, not the number or the closed-neighborhood coefficient. A separate published rigidity result determines *six*-support types in the smallest graph reaching dimension six, not the intermediate fourth coefficients for every ambient size. These comparisons concern the substantive implications of the results, not similarity of terminology.

## Limitations

The proof uses an executable exhaustive integer certificate for 666 reduced incidence profiles rather than a handwritten list of every profile. The independent direct small-order enumeration corroborates but does not replace this complete profile reduction. The result is restricted to rank-three Kneser graphs and support size exactly four. Priority is assessed against the accessible literature and indexed research records, not claimed globally; an unindexed equivalent all-order census remains possible. An independent scientific audit has not been performed.

## References

1. I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, first public 2020-07-31, https://arxiv.org/html/2007.16042v1.
2. D. Coudert, M. Csikós, G. Ducoffe, L. Viennot, *Practical Computation of Graph VC-Dimension*, arXiv:2405.07588v1, first public 2024-05-13, https://arxiv.org/html/2405.07588v1.
3. A. Bhattacharya, S. Chakraborty, A. Ghosh, G. Mishra, M. Paraashar, *Disjointness through the Lens of Vapnik–Chervonenkis Dimension: Sparsity and Beyond*, arXiv:2006.13712v1, first public 2020-06-24, https://arxiv.org/html/2006.13712v1.
4. *Exact open-neighborhood VC dimension of Kneser graphs on triples*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-open-neighborhood-vc-dimension-of-kneser-graphs-on-triples--38f8cf862323.
5. *Rigidity and exact count of six-point shattering supports in the smallest rank-three Kneser graph*, published mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rigidity-and-exact-count-of-six-point-shattering-supports-in-the--473a9e5037c3.
