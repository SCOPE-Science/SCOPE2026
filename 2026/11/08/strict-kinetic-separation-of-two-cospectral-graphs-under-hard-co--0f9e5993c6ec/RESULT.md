# Strict kinetic separation of two cospectral graphs under hard-core monomer adsorption

## Finding
Let \(R\) be the \(4\times4\) rook graph and \(S\) the Shrikhande graph, both with strongly regular parameters \((16,6,2,2)\). Give every vertex one independent rate-one exponential adsorption-attempt time. The vertex becomes permanently occupied if it has no previously occupied neighbor; otherwise its attempt fails. Let \(X_G(t)\) be the number occupied by time \(t\ge0\), and \(X_G(\infty)\) the terminal occupancy.

**Exact terminal law.** On \(R\), \(X_R(\infty)=4\) with probability one, and each of its 24 terminal labeled four-sets has probability \(1/24\). On \(S\),
\[
\Pr[X_S(\infty)=3]=\frac13,\qquad
\Pr[X_S(\infty)=4]=\frac23.
\]
More precisely, its 32 terminal labeled three-sets each have probability \(1/96\), and its 16 terminal labeled four-sets each have probability \(1/24\). Thus the terminal means are \(4\) and \(11/3\) respectively.

**Strict separation at every positive time.** Write \(p=1-e^{-t}\), and let \(a_k(G)=\sum_{|U|=k}F_G(U)\), where \(F_G(U)\) denotes the expected final greedy-independent-set size in the induced graph \(G[U]\) when its vertices arrive in uniformly random order. Then
\[
\mathbb E[X_R(t)]-\mathbb E[X_S(t)]
=\sum_{k=4}^{16}\delta_k p^k(1-p)^{16-k}>0
\qquad (0<t<\infty),
\]
where \(\delta_k=a_k(R)-a_k(S)\) is specified exactly below, and the inequality also holds at \(t=\infty\) with value \(1/3\). In particular, the first distinction in the low-attempt-probability expansion is
\[
\mathbb E[X_R(t)]-\mathbb E[X_S(t)]=8p^4+O(p^5)\qquad(p\downarrow0).
\]
The finite-time assertion is about expectations, not stochastic domination of the complete occupancy distributions.

## Assumptions and scope
The graphs are the following explicitly labeled simple graphs on \(V=(\mathbb Z/4\mathbb Z)^2\), with coordinates \((a,b)\) represented by \(4a+b\). In \(R\), distinct vertices are adjacent exactly when they share their first or second coordinate. In \(S\), distinct vertices are adjacent exactly when their difference belongs modulo four to
\[
\{(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1)\}.
\]
Each vertex has a single independent rate-one exponential first attempt; later attempts, if allowed, cannot reverse a rejection because occupied sites never desorb. This is the standard irreversible nearest-neighbor exclusion rule. Continuous independent times eliminate ties. Labels distinguish physical sites, not graph-isomorphism classes. Both graphs have 16 vertices, degree six, and two common neighbors for any two distinct vertices.

## Proof
**1. Reduction to the first accepted sites.** The first successful arrival is uniformly distributed among the 16 vertices. After it occupies \(v\), exactly nine nonneighbors remain available. The next successful arrival is uniformly distributed among those nine. Since any nonadjacent pair has exactly two common neighbors, removing both closed neighborhoods leaves exactly four available sites:
\[
16-(7+7-2)=4.
\]
By vertex transitivity, take the first site to be \((0,0)\). Directly testing the coordinate adjacency rules, the four remaining sites induce \(C_4\) for each of the nine possible second choices on \(R\). On \(S\), exactly three second choices, namely \((0,2),(2,0),(2,2)\), leave \(C_4\), and the other six leave \(K_4\) with one edge deleted (a diamond). The two graph constructions, nine residual choices, and their induced degrees are exhaustively rechecked by `verify_terminal.py`.

**2. Final occupancy.** Random greedy adsorption on \(C_4\) accepts two opposite vertices, regardless of which is first. On a diamond, with probability \(2/4\) the first occupied residual vertex has degree three and blocks the other three, while with probability \(2/4\) it is a degree-two vertex and its nonadjacent counterpart is forced to occupy next. Therefore after the first two occupied sites the process adds either two (always on \(R\), and on a \(C_4\) branch of \(S\)) or one (on half the diamond branches of \(S\)). Thus
\[
\Pr[X_S(\infty)=3]=\frac69\frac24=\frac13.
\]

**3. Probabilities of individual terminal sets.** For any ordered accepted triple, the first, second, and third choices occur with probability \(1/(16\cdot9\cdot4)=1/576\), because after two occupied nonneighbors exactly four choices remain. A terminal independent three-set can occur in all six orders of its vertices, yielding probability \(6/576=1/96\). Since the total probability for size three is \(1/3\), there are exactly 32 such sets. Similarly, every terminal four-set can occur in all 24 accepted orders: after the third accepted site the fourth member of the set is the unique available candidate. Hence each has probability \(24/576=1/24\). The respective total masses imply 24 terminal four-sets on \(R\) and 16 on \(S\). This also proves every terminal probability without assuming static independence-polynomial counts.

**4. The full-time expected occupancy.** For any induced vertex subset \(U\), let \(N_G[v]\) denote a closed neighborhood in \(G\) and set \(F_G(\varnothing)=0\). Conditioning on the first accepted site gives, for nonempty \(U\), the exact finite recursion
\[
F_G(U)=1+\frac1{|U|}\sum_{v\in U}F_G(U\setminus N_G[v]).
\]
At time \(t\), each site has attempted independently with probability \(p=1-e^{-t}\). Conditional on the set \(U\) of sites that attempted, their order is uniform. Thus
\[
\mathbb E[X_G(t)]=\sum_{k=0}^{16}a_k(G)p^k(1-p)^{16-k}.
\]
The following exact coefficient differences result by the recurrence over all \(2^{16}\) labeled subsets; no statistical estimation is used:

| \(k\) | \(\delta_k=a_k(R)-a_k(S)\) |
|---:|---:|
| 0,1,2,3 | \(0\) |
| 4 | \(8\) |
| 5 | \(64\) |
| 6 | \(3688/15\) |
| 7 | \(20736/35\) |
| 8 | \(990\) |
| 9 | \(3608/3\) |
| 10 | \(3256/3\) |
| 11 | \(3656/5\) |
| 12 | \(5464/15\) |
| 13 | \(392/3\) |
| 14 | \(32\) |
| 15 | \(24/5\) |
| 16 | \(1/3\) |

Every coefficient for \(k\ge4\) is positive. For \(0<p<1\), every Bernstein weight \(p^k(1-p)^{16-k}\) is positive, so the expected-occupancy gap is strictly positive. At \(p=1\), the gap equals \(\delta_{16}=1/3\). The leading small-\(p\) coefficient is \(\delta_4=8\), while lower coefficients vanish, establishing the stated expansion. This proof covers all real \(t\ge0\), not just sample times.

## Verification
Run `python3 verify_terminal.py` and `python3 verify_kinetics.py` from the directory containing these files, using Python 3 and no third-party dependencies. The terminal verifier independently computes exact probabilities of every labeled terminal set by a subset-distribution recursion, checks the graph parameters, and classifies the nine four-vertex residual graphs. The kinetics verifier sums exact rational means over every one of the \(2^{16}\) induced subsets, checks all seventeen coefficient differences, and independently checks the first differing coefficient by evaluating all \(\binom{16}{4}\) four-site sets in each of their \(24\) possible arrival orders. The exact coefficients are also provided in `KINETICS_COEFFICIENTS.csv`. The two required terminal markers are `SHRIKHANDE_ROOK_TERMINAL_OK` and `SHRIKHANDE_ROOK_KINETICS_OK`.

## Relationship to prior work
Pippenger (1989) established a foundational analysis of random sequential adsorption on graphs, especially large-girth regular graphs; his accessible abstract does not claim this short-cycle strongly regular pair, but the complete text was not available for comparison. Dhara, van Leeuwaarden and Mukherjee (arXiv:1604.03918v1, 2016) treat asymptotic adsorption and variants on Erdős–Rényi graphs, not the exact sixteen-site laws here. Krivelevich and collaborators (2023) develop general locally convergent graph tools and analyze random greedy independent sets, without an evaluated comparison of this pair. The published independent-complex comparison of the same two graphs supplies exact static independence polynomials \(1+16z+72z^2+96z^3+24z^4\) for \(R\) and \(1+16z+72z^2+96z^3+16z^4\) for \(S\). Those static counts and known graph-theoretic distinctions are not claimed as new. They do not determine the random-order probabilities or the exact finite-time expected-coverage comparison, which are the contributions stated here.

## Limitations
This is an exact result for a specific pair of 16-vertex graphs, not a universal theorem for all cospectral or strongly regular graphs. It establishes strict expected-coverage ordering, not pathwise coupling or stochastic ordering. Rates are independent and uniform; nonuniform attempt rates are not covered. The results are finite-site dynamics, not a thermodynamic limit. The complete text of Pippenger (1989) was inaccessible; its abstract was available, so hidden historical equivalences cannot be excluded. There has been no independent external mathematical audit.

## References
1. S. Dhara, J. S. H. van Leeuwaarden, D. Mukherjee, *Generalized random sequential adsorption on Erdős–Rényi random graphs*, arXiv:1604.03918v1 (first public 2016-04-13), https://arxiv.org/abs/1604.03918.
2. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2(3) (1989), 393–401, https://doi.org/10.1137/0402034.
3. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, Random Structures & Algorithms (first online 2023-12-18), https://doi.org/10.1002/rsa.21200.
4. *Independence complexes of the Shrikhande and \(4\times4\) rook graphs have different sphere-wedge homotopy types*, published result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-independence-complexes-of-the-shrikhande-and-4-times4-rook-graph--41bf4d1d3187.
5. MSC2020, code 82C20, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=82C20.
