# Sharp ten-vertex collisions of graded one-point types over height-two tree-cover posets

## Finding
Let \(P\) be a finite, nonempty, height-two poset whose undirected Hasse cover graph is a tree. Regard every element as an individually named parameter of the countable universal homogeneous poset. For every realizable nonalgebraic one-type \(p\), let \(L_p\) and \(U_p\) respectively denote the named parameters strictly below and strictly above a realization. Define the bivariate type polynomial
\[
\Phi_P(s,t)=\sum_p s^{|L_p|}t^{|U_p|}.
\]
**Sharp reconstruction theorem.** For \(2\le n\le9\), this polynomial determines every height-two tree-cover poset of order \(n\) up to poset isomorphism. At \(n=10\), among precisely \(203\) isomorphism classes there are \(201\) distinct polynomials and **exactly two nonsingleton fibres, each of size two**. The first fibre consists of a non-self-dual poset and its dual, both with \(332\) types. The second fibre consists of two self-dual posets with nonisomorphic underlying trees, both with \(340\) types. Thus orientation and even undirected tree shape can first be lost at order ten.

Moreover, the polynomial of every such input has the closed form below. Write \(A=\min(P)\), \(B=\max(P)\), \(n=|A|+|B|\), \(N(b)=\{a\in A:a<b\}\), \(d(v)\) for Hasse degree and \(J_P(z)=\sum_{I\text{ ideal of }P}z^{|I|}\). Then
\[
\begin{aligned}
\Phi_P(s,t)={}&J_P(s)+J_{P^{\mathrm{op}}}(t)-1\\
&+s\sum_{a\in A}\big((1+t)^{d(a)}-1\big)
+t\sum_{b\in B}\big((1+s)^{d(b)}-1\big)-(n-1)st,\\
J_P(z)={}&\sum_{S\subseteq A}z^{|S|}(1+z)^{|\{b\in B:N(b)\subseteq S\}|}.
\end{aligned}
\]

## Assumptions and scope
A strict poset of height two has no three-element chain. The Hasse cover graph is connected and acyclic, hence bipartite, with every edge oriented from a minimal to a maximal element. All parameters are individually fixed, and the extension point is new and distinct from them. We count complete types, not types modulo parameter automorphisms. The underlying homogeneous structure realizes every finite induced one-point extension of a finite poset; these types are nonalgebraic. Our first-collision theorem concerns this natural, explicitly bounded class, not arbitrary posets or general oriented cover trees.

## Proof
**1. Type/ideal-filter bijection.** For a new point \(x\), let \(L=\{p:p<x\}\) and \(U=\{p:x<p\}\). The induced old order remains unchanged exactly when \(L\) is an ideal, \(U\) is a filter, and \(l<u\) for every \(l\in L,u\in U\). These conditions suffice: adjoining \(x\) and closing transitively creates no new old-old comparisons. Homogeneity then realizes each admissible profile as a distinct complete nonalgebraic type. Profiles with at least one empty shore contribute \(J_P(s)+J_{P^{\mathrm{op}}}(t)-1\).

**2. The mixed-profile formula.** When both shores are nonempty, the height-two condition forces \(L\subseteq A\) and \(U\subseteq B\). Every edge in \(L\times U\) must occur in the Hasse tree. A simple tree contains no four-cycle, so \(|L|=1\) or \(|U|=1\). For a fixed lower singleton \(\{a\}\), there are \(\binom{d(a)}j\) compatible upper sets of size \(j\); dually for an upper singleton. The two sums count singleton-singleton profiles twice, one per Hasse edge. Subtracting \((n-1)st\) proves the displayed identity, including exact boundary coefficients. An ideal with minimal-vertex intersection \(S\subseteq A\) may contain precisely any subset of the upper vertices whose full lower neighborhoods lie in \(S\), proving the second identity. These identities hold for **all** orders in the stated class.

**3. Exhaustive class enumeration.** Generate free trees recursively from the one-vertex tree by attaching a new leaf to each existing vertex, deduplicating by a canonical code. Every tree on \(n+1\) vertices has a leaf, hence deleting it yields an \(n\)-vertex tree and proves exhaustiveness inductively. The canonical code recursively sorts rooted branches at the center(s) of the tree; with two centers, sort the two half-tree codes. The identical rooted-code construction, with a vertex tag recording its lower/upper shore, canonically classifies each of the two bipartite orientations. Thus codes agree if and only if the corresponding Hasse posets are isomorphic. Evaluate the exact polynomial for each distinct oriented code using integer subset enumeration and the formula above; group exact coefficient tuples, not hashes or numerical evaluations. Independent direct enumeration of the three relations to each named point checks every generated instance through eight vertices and all four ten-vertex collision witnesses. The executable certificate `verify.py` implements this exhaustive argument and checks expected totals.

The resulting closed finite census is:

| \(n\) | Free trees | Height-two oriented poset types | Distinct \(\Phi\) |
|---:|---:|---:|---:|
| 2 | 1 | 1 | 1 |
| 3 | 1 | 2 | 2 |
| 4 | 2 | 3 | 3 |
| 5 | 3 | 6 | 6 |
| 6 | 6 | 10 | 10 |
| 7 | 11 | 22 | 22 |
| 8 | 23 | 42 | 42 |
| 9 | 47 | 94 | 94 |
| 10 | 106 | 203 | 201 |

At order ten the two coefficient fibres have size distribution \((2,2)\); all remaining \(199\) fibres are singletons. Because each class is represented exactly once and all class polynomials are evaluated exactly, the census proves the sharp first collision, rather than extrapolating from sampled trees.

**4. Explicit nonisomorphic witnesses.** Vertices are numbered \(0,\ldots,9\). List lower-to-upper Hasse pairs (all other distinct pairs are incomparable):

- \(A:\) `(0,1),(0,2),(0,3),(4,1),(5,1),(6,2),(7,3),(4,8),(6,9)`.
- \(A^{\mathrm{op}}:\) `(1,0),(2,0),(3,0),(1,4),(1,5),(2,6),(3,7),(8,4),(9,6)`.
- \(B:\) `(0,1),(0,2),(0,3),(4,1),(5,1),(6,2),(4,7),(6,8),(9,7)`.
- \(C:\) `(0,1),(0,2),(0,3),(4,1),(5,2),(4,6),(7,6),(8,6),(7,9)`.

The canonical shore-coloured codes of the four witnesses are pairwise different. The first two reverse each other's orders. The last two have different uncoloured canonical tree codes and each is self-dual. Their full polynomials, not only their totals, are
\[
\begin{aligned}
H_0(z)={}&1+5z+12z^2+20z^3+26z^4+28z^5+26z^6+20z^7+12z^8+5z^9+z^{10},\\
H_1(z)={}&H_0(z)+z^4+2z^5+z^6,\\
M(s,t)={}&9st+5(st^2+s^2t)+(st^3+s^3t),\\
\Phi_A(s,t)={}&\Phi_{A^{\mathrm{op}}}(s,t)=H_0(s)+H_0(t)-1+M(s,t),\\
\Phi_B(s,t)={}&\Phi_C(s,t)=H_1(s)+H_1(t)-1+M(s,t).
\end{aligned}
\]
Evaluation at \((1,1)\) gives respectively \(332\) and \(340\). Exact coefficient enumeration confirms these formulas and identifies the two fibres as precisely the displayed witnesses.

## Verification
Run `python3 verify.py` (standard-library only) in the directory containing the included artifact. It generates all free trees up to ten vertices, both oriented bipartitions, exact ideal/filter coefficient tuples, and tests the complete fibre census. Independently, it enumerates all \(3^n\) assignments of lower, upper, or incomparable status for all oriented types through eight vertices and for all four ten-vertex witnesses, testing the transitivity and old-order constraints directly. Its output is in `verification_output.txt`; the witness edge lists are also in `witnesses.json`. This is a finite exhaustive classification proof supported by a generator completeness argument; it asserts nothing about larger orders.

## Relationship to prior work
The ideal/filter characterization is classical. Dolinka and Mašulović (2012) establish the homogeneous-poset extension setting. The existing all-orientation **scalar** one-type formula for Hasse tree covers (`SCOPE-linear-arithmetic-exact-one-type-counting-on-oriented-tree-cover--23742e530543`) counts \(\Phi_P(1,1)\) but does not imply the multivariate coefficients or the sharp reconstruction fibres. The published finite counting-logic classification for height-two permutation orders (`SCOPE-counting-logic-identification-of-all-height-two-permutation-pose--39e17b148bc6`) uses the distinct, generally stronger directed counting-refinement fingerprint and does not imply reconstruction from a one-point polynomial. General eight-vertex poset collisions likewise do not establish the minimal ambiguity in this constrained tree-cover family. Pretzel's 1980 insertion-position work is potentially related, but its full text was not obtainable; this remains a specific historical-priority risk.

## Limitations
The reconstruction cutoff is exhaustive **through** ten vertices, not an assertion about all larger sizes. The formula and proof cover height-two Hasse trees, not general cover graphs with cycles. Independent priority review and external mathematical audit have not been performed. A relevant 1980 source could be compared only at abstract level. The proof depends on the stated complete, exact finite-generation and canonical-isomorphism arguments, which are included for reproduction.

## References
1. I. Dolinka and D. Mašulović, *Countable homogeneous linearly ordered posets*, European Journal of Combinatorics, DOI: 10.1016/j.ejc.2012.06.006; publicly available online 2012-07-15.
2. O. Pretzel, *A construction for partially ordered sets*, Discrete Mathematics 32 (1980), 59–68, DOI: 10.1016/0012-365X(80)90100-4 (abstract inspected, full text inaccessible).
3. *Linear-arithmetic exact one-type counting on oriented tree-cover posets*, published proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/25/SCOPE-linear-arithmetic-exact-one-type-counting-on-oriented-tree-cover--23742e530543/RESULT.md.
4. *Counting-logic identification of height-two permutation posets through ten points*, published proof: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-counting-logic-identification-of-all-height-two-permutation-pose--39e17b148bc6/RESULT.md.
5. R. Otter, *The number of trees*, Annals of Mathematics 49 (1948), 583–599; see the classical free-tree census OEIS A000055.
