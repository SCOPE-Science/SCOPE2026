# Italian-domination weight polynomials distinguish the Shrikhande and rook graphs

## Finding
Let \(R=K_4\square K_4\) be the sixteen-vertex rook graph and \(S\) the Shrikhande graph on \(\mathbb Z_4^2\), with respective adjacency relations specified below. For \(G\in\{R,S\}\), let \(I_G(z)=\sum_f z^{\sum_v f(v)}\) sum over all Italian (Roman \(\{2\}\)) dominating functions \(f:V(G)\to\{0,1,2\}\). Then
\[
\boxed{I_R(z)-I_S(z)=8z^4+224z^5+1184z^6+1408z^7+1176z^8+832z^9+640z^{10}+256z^{11}.}
\]
Every coefficient of degree \(12\) through \(32\) is identical. Both Italian-domination numbers are \(4\), but exactly \(24\) optimal functions occur on \(R\), versus \(16\) on \(S\). Each optimum uses four labels \(1\) and twelve labels \(0\); its positive support is a maximum independent set. On \(R\) these are the \(4!\) permutation transversals. On \(S\) these are exactly the sixteen cosets of four specified order-four subgroups, four cosets for each subgroup.

## Assumptions and scope
Both graphs are labelled on \(\mathbb Z_4^2\). In \(R\), distinct pairs \((a,b)\) and \((c,d)\) are adjacent exactly when \(a=c\) or \(b=d\). In \(S\), adjacency means that \((c-a,d-b)\), modulo \(4\), belongs to \(\{(1,0),(3,0),(0,1),(0,3),(1,1),(3,3)\}\). Both are simple connected six-regular graphs of order sixteen with strongly regular parameters \((16,6,2,2)\). An Italian dominating function imposes \(\sum_{u\in N(v)}f(u)\ge2\) **only when** \(f(v)=0\); it does not impose exact equality, total domination, or a condition at nonzero vertices. Each labelled function is counted exactly once.

## Proof
**1. Exact positive-support enumeration identity.** For a finite graph \(G=(V,E)\) and any nonempty support \(A\subseteq V\), define \(U(A)\) as the selected vertices which are the *unique* selected neighbor of at least one unselected vertex:
\[
U(A)=\{u\in A:\exists v\notin A,\ N(v)\cap A=\{u\}\}.
\]
If some \(v\notin A\) has no neighbor in \(A\), no Italian function can have support \(A\). Otherwise, every zero vertex with at least two positive neighbors is automatically defended (each positive label is at least one), and a zero with exactly one positive neighbor is defended precisely when that neighbor has label \(2\). Consequently every vertex in \(U(A)\) is forced to receive label \(2\), while all other selected vertices freely receive either \(1\) or \(2\). Therefore the following finite identity is exact for *every* finite graph:
\[
I_G(z)=\sum_{\substack{A\subseteq V\\N(v)\cap A\ne\varnothing\ \forall v\notin A}}
 z^{2|U(A)|}(z+z^2)^{|A|-|U(A)|}.
\tag{1}
\]
It is not a sampled expansion. For a sixteen-vertex graph, it has exactly \(2^{16}\) candidate supports, and each term contributes integer binomial coefficients. The self-contained `verify_support.py` enumerates the sixteen-bit masks in ascending order, computes \(U(A)\) from the displayed adjacency rules and accumulates \(\binom{|A|-|U(A)|}{t}\) at weight \(|A|+|U(A)|+t\), for \(0\le t\le |A|-|U(A)|\). This deterministic, finite calculation gives the following complete coefficient vectors in degrees \(0,1,\ldots,32\):

```
R: [0,0,0,0,24,528,4552,23680,96966,296432,707160,1379472,2285712,3305520,4252296,4926912,5180931,4964688,4342280,3465744,2520336,1665456,996216,536640,258570,110448,41328,13328,3620,800,136,16,1]
S: [0,0,0,0,16,304,3368,22272,95790,295600,706520,1379216,2285712,3305520,4252296,4926912,5180931,4964688,4342280,3465744,2520336,1665456,996216,536640,258570,110448,41328,13328,3620,800,136,16,1]
```

Subtracting the two exact vectors yields the boxed formula, including the degree-twelve tail equality. The complete enumeration identity (1), the explicit graphs and the terminating 65,536-mask algorithm determine every coefficient without invoking an unproved analytic identity. The script assertions certify these exact integers, while `verify_ternary.cpp` independently enumerates all \(3^{16}=43{,}046{,}721\) labelings for each graph and checks the original neighbor condition directly.

**2. A structural minimum-weight bound.** Write \(p\) for the number of positive vertices, and \(w\) for the sum of their labels. Every unselected vertex has total positive neighbor weight at least two. Since each graph is six-regular, counting the positive-to-zero incident label weight in two ways gives
\[
2(16-p)\le 6w,
\qquad 16\le p+3w\le4w.
\]
Thus \(w\ge4\). If \(w=4\), both inequalities must be equalities: \(p=4\), so all selected labels are \(1\); the four positive vertices have no edges among themselves; and every zero vertex has exactly two positive neighbors. Conversely, every four-vertex independent set in either graph has exactly two neighbors at every outside vertex (as proved directly below), and so gives a valid weight-four function. The two counts in Part 1 establish that such functions exist, hence the bound is attained.

**3. Counting all optimum configurations.** In \(R\), a four-vertex independent set cannot contain two vertices in one row or column, and therefore consists of one position in each row and each column. These are the \(4!=24\) permutation transversals. Every outside cell shares a row with one selected cell and a column with a distinct selected cell, hence is defended twice.

For \(S\), translations act transitively on vertices. The nine nonneighbors of \((0,0)\) are
\[
(0,2),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3),(3,1),(3,2).
\]
Among their \(\binom93=84\) triples, the only pairwise nonadjacent triples are
\[
\begin{aligned}
&\{(0,2),(2,0),(2,2)\},\quad \{(0,2),(2,1),(2,3)\},\\
&\{(1,2),(2,0),(3,2)\},\quad \{(1,3),(2,2),(3,1)\}.
\end{aligned}
\]
This is checked by the explicit six-difference adjacency criterion (and reproduced by the subset verifier). Adjoin \((0,0)\) to each triple. These four configurations are order-four additive subgroups of \(\mathbb Z_4^2\), each with exactly four cosets. Every four-coclique contains a vertex, and translating it to the origin puts it in this list; hence exactly \(4\cdot4=16\) independent four-sets exist. Each has exactly two selected neighbors at every unselected vertex. To see this without a computer, write \(t_v=|N(v)\cap A|\) for each of the twelve outsiders. Six-regularity gives \(\sum_v t_v=24\); the strongly regular parameter \(\mu=2\) and the six unordered pairs from the independent four-set give \(\sum_v\binom{t_v}{2}=12\). Consequently \(\sum_v(t_v-2)^2=\sum_v[t_v+2\binom{t_v}{2}]-4\cdot24+4\cdot12=0\), so every \(t_v=2\). The finite verifier independently checks this assertion for all sixteen sets. Thus all sixteen produce optimal functions and no others exist. \(\square\)

## Verification
Run `python3 verify_support.py` and compile/run `verify_ternary.cpp` with a C++17 compiler, for example `c++ -O3 -std=c++17 verify_ternary.cpp -o verify_ternary && ./verify_ternary`. Both use only standard libraries. The first visits all \(2^{16}\) supports per graph using identity (1), separately visits all \(\binom{16}{4}\) possible four-sets, checks minimum counts and exact tail cancellation, and prints `SUPPORT_ENUMERATION_OK`. The second recursively visits exactly \(3^{16}\) labelings per graph and verifies the Italian condition by direct neighbor sums; its full coefficient output is compared with the first program. These are exhaustive finite proofs for the two specified graphs; no infinite-family extrapolation is asserted.

## Relationship to prior work
Varghese, Anu and Aparna (first publicly available 2 November 2022) study Italian domination and its variants on generalized Sierpiński graphs; this supplies the focal invariant and graph-family motivation but no enumerator for either strongly regular graph studied here. Almulhim, Al Subaiei and Mondal (2024) survey Roman \(\{2\}\)-domination under its Italian-domination alias and variants. The publicly available minimum-Italian-domination theorem for rook graphs determines the ordinary minimum and all rook optimizers, including the count \(24\) on \(K_4\square K_4\); those facts are explicitly credited, not presented as novel. Other published work distinguishes Shrikhande and rook graphs using paired domination and establishes an equality of their total-domination polynomials; these distinct vertex-set invariants neither determine Italian label weights nor imply the displayed coefficient identity. The new claim is the complete **Italian weight polynomial separation**, including the Shrikhande optimum enumeration and sharp tail agreement.

## Limitations
The result is an exact, finite classification of two sixteen-vertex graphs, not a universal strongly regular graph theorem. The equality of coefficients at degrees twelve and above is established through the fully specified complete finite support sum, not by a graph-uniform structural tail theorem. Earlier unindexed exact tables or equivalent enumerations remain possible; literature search cannot prove absolute historical novelty. No independent external mathematical audit is claimed.

## References
1. J. Varghese, V. Anu and L. S. Aparna, *Domination parameters of generalized Sierpiński graphs*, published online 2022-11-02, DOI: 10.1080/09728600.2022.2138630. https://doi.org/10.1080/09728600.2022.2138630
2. A. Almulhim, B. Al Subaiei and S. R. Mondal, *Survey on Roman \(\{2\}\)-Domination*, *Mathematics* **12** (2024), 2771. https://doi.org/10.3390/math12172771
3. *Minimum Italian domination on rook graphs: exact optimizers and a sharp transition*, public mathematical research record, 2026-10-18. https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-minimum-italian-domination-on-rook-graphs-exact-optimizers-and-a--73393dbef1b4
4. *Paired-domination distinguishes two graphs with identical total-domination polynomials*, public mathematical research record, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-paired-domination-distinguishes-two-graphs-with-identical-total--0d16d6786052
