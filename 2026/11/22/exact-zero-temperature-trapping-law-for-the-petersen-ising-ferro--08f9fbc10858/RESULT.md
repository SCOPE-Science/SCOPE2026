# Exact zero-temperature trapping law for the Petersen Ising ferromagnet

## Finding
Let \(G\) be the ten-vertex Petersen graph with one binary spin at every vertex. Each vertex has an independent rate-one Poisson clock; when it rings, its spin agrees with the strict majority of its three neighbors. Initially, spins are independent and plus with probability \(p\in[0,1]\). Write \(Q(p)\) for the probability that the process eventually freezes without reaching either all-plus or all-minus consensus. Then
\[
\boxed{Q(p)=\frac{2}{189}[p(1-p)]^3\bigl(924+425p(1-p)\bigr).}
\]
There are exactly fourteen absorbing spin configurations: the two consensuses and twelve nonconstant states, each with five plus and five minus spins. The plus and minus vertices in every nonconstant absorbing state induce complementary five-cycles. The nonconstant final states form one automorphism orbit, so each has final probability exactly \(Q(p)/12\), for every \(p\in[0,1]\).

In particular, the exact infinite-temperature-quench trapping probability is
\[
\boxed{Q(1/2)=\frac{4121}{24192}\approx0.1703455688.}
\]
Since the displayed expression is strictly increasing as a function of \(p(1-p)\) on \([0,1/4]\), the trapping probability has its unique maximum at \(p=1/2\). The eventual consensus probability is \(1-Q(p)\).

## Assumptions and scope
Use the labelled graph \(G=KG(5,2)\), whose vertices are the ten two-element subsets of \(\{0,1,2,3,4\}\) in lexicographic order, with an edge precisely between disjoint subsets. This is the Petersen graph. The coupling is ferromagnetic and identical on all edges; at zero temperature a spin changes exactly when at least two of its three neighbors disagree with it. There are no tied local majorities and no external field, quenched random fields, simultaneous updates, or persistent noise. Each site's attempted updates form an independent Poisson process of rate one. Initial spins are independent Bernoulli variables, including the endpoint values \(p=0,1\). The claim is finite-volume and requires no thermodynamic limit.

## Proof
**1. Finite descent.** Encode a spin configuration by a ten-bit integer \(s\), where a one means plus. Define \(C(s)\) to be the number of graph edges joining opposite spins. A permissible spin flip has either two or three disagreeing neighbors, and consequently decreases \(C\) by exactly one or three, respectively. Therefore every path of actual flips strictly decreases a nonnegative integer. Clock attempts that leave the state unchanged do not affect absorption; the process almost surely reaches an absorbing state after finitely many flips.

**2. Complete absorbing-state geometry.** In an absorbing state, every vertex has at least two same-spin neighbors. If both colors occur, each monochromatic induced subgraph has minimum degree at least two, hence contains a cycle. The Petersen graph has girth five, so each color class contains at least five vertices. They therefore have exactly five each; each induces a five-cycle. The Petersen graph has exactly twelve five-cycles, and each such cycle has a complementary five-cycle. Thus there are exactly twelve nonconstant absorbing states, alongside the two homogeneous states. Their monochromatic induced cycles have five edges each and the five remaining Petersen edges cross the color boundary. Under the natural \(S_5\)-action on the Kneser representation, these twelve nonconstant states form one orbit.

**3. Exact absorption recursion.** For a configuration \(s\), let \(F(s)\) be the set of vertices whose spins disagree with at least two neighbors. Let \(a(s)\) be the probability of eventual nonconstant absorption starting from \(s\). In an absorbing state, set \(a(s)=1\) if it is nonconstant and \(a(s)=0\) otherwise. In a nonabsorbing state, equal rate-one clocks give the embedded-jump recursion
\[
a(s)=\frac{1}{|F(s)|}\sum_{v\in F(s)}a(s\mathbin{\triangle}\{v\}),
\]
where \(s\mathbin{\triangle}\{v\}\) flips exactly the spin at \(v\). Since each successor has smaller \(C\), this uniquely defines rational values on all \(2^{10}=1024\) configurations without a matrix inversion or infinite limiting argument.

**4. Exact finite certificate and Bernoulli averaging.** The coefficient
\[
B_k=\sum_{|s|=k}a(s),\qquad 0\le k\le10,
\]
computed by the displayed finite recursion, is exactly
\[
(B_0,\ldots,B_{10})=\left(0,0,0,\frac{88}{9},\frac{8242}{189},\frac{12788}{189},\frac{8242}{189},\frac{88}{9},0,0,0\right).
\]
This follows from the exhaustive independently checked state recursion in `verify_state_dp.py` and, separately, from the eighteen-row symmetry-quotient recursion in `verify_orbit_dp.py`. The latter generates the complete quotient under all \(120\) permutations of \(\{0,1,2,3,4\}\) and global spin complementation, and tests the outgoing transitions for every member of every orbit. Its complete orbit counts, transitions, cut levels, and absorption fractions appear in `orbit_table.csv`. In particular, these are exact rational certificates, not sampling estimates. Averaging the finite-state absorption probabilities under the independent Bernoulli product law gives
\[
Q(p)=\sum_{k=0}^{10}B_kp^k(1-p)^{10-k}
=\frac{2}{189}[p(1-p)]^3(924+425p(1-p)).
\]
The orbit action of \(S_5\) preserves both the dynamics and the iid initial law, proving equal final probabilities for the twelve nonconstant states.

## Verification
With Python 3, run `python verify_state_dp.py` and `python verify_orbit_dp.py`; neither needs external packages or downloads. The first uses the outer-pentagon/inner-star/spoke presentation of the Petersen graph and exact `fractions.Fraction` recursion over all 1024 masks. The second independently constructs \(KG(5,2)\), enumerates its 18 orbits under \(S_5\) and complementation, confirms that its orbit transition counts are constant within orbits, and evaluates the quotient recursion. The programs independently agree on the full list of Bernstein-basis coefficients, the 14 absorbing states, and the unbiased probability \(4121/24192\). The first program also checks that every possible move lowers the cut by one or three. The quotient's printed rows can be compared with `orbit_table.csv`.

For uniformly selected configurations with exactly \(k\) plus spins, the nonconstant absorption probability is zero when \(k\in\{0,1,2,8,9,10\}\); it is \(11/135\) at \(k=3,7\), \(4121/19845\) at \(k=4,6\), and \(3197/11907\) at \(k=5\). These are conditional initial-seed laws, not the probabilities of particular terminal states.

## Relationship to prior work
Spirin, Krapivsky, and Redner [1,2] introduced and analyzed zero-temperature Ising freezing on finite regular lattices, including metastable stripe states, but did not determine a Petersen-graph absorption polynomial. Baek, Ha, and Jeong [3] investigated zero-temperature absorbing-state distributions of random networks numerically; their setup and active-link observable provide direct physical motivation, but their numerical random-network distributions do not imply this exact labelled ten-spin law. Damron and Sen [4] study the infinite three-regular tree, whose local geometry resembles the Petersen graph while its global state space and absorbing-state law differ.

The fixed-state count of fourteen for \(GP(5,2)\) is separately known from an all-size generalized-Petersen majority equilibrium census [5]. A synchronous Petersen-majority study [6] also identifies fourteen fixed configurations, alongside many two-cycles; it uses simultaneous rather than independent-clock updates. Those existing fixed-point results are **not** claimed as new. Neither fixed-point census nor synchronous basins determines the stochastic probability of reaching a nonconstant absorber under asynchronous rate-one updates. A 2026 study [7] considers a random-field Ising model on generalized Petersen networks and field-driven responses; its abstract does not establish the present zero-field quench law.

## Limitations
This is an exact theorem only for the ten-vertex Petersen graph, strict zero-temperature ferromagnetic majority flips with equal site rates, and independent Bernoulli initial spins. It does not assert analogous trapping probabilities for larger generalized Petersen graphs, other update-rate profiles, nonzero temperature, random fields, or synchronous dynamics. The explicit rational probabilities are proved by finite exhaustive recurrence, not by a general symbolic formula for arbitrary graphs. The literature comparison is not a guarantee against an unindexed earlier equivalent computation.

## References
[1] V. Spirin, P. L. Krapivsky, S. Redner, *Fate of Zero-Temperature Ising Ferromagnets*, arXiv:cond-mat/0008019, first public 2000-08-01. https://arxiv.org/abs/cond-mat/0008019

[2] V. Spirin, P. L. Krapivsky, S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037, first public 2001-05-02. https://arxiv.org/abs/cond-mat/0105037

[3] Y. Baek, M. Ha, H. Jeong, *Absorbing states of zero-temperature Glauber dynamics in random networks*, arXiv:1112.5927, first public 2011-12-27. https://arxiv.org/abs/1112.5927

[4] M. Damron, A. Sen, *Zero-temperature Glauber dynamics on the 3-regular tree and the median process*, arXiv:1904.11625. https://arxiv.org/abs/1904.11625

[5] *Ninth-degree spin sectors and an entropy gap in majority dynamics on generalized Petersen graphs*, published mathematical finding, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-ninth-degree-spin-sectors-and-an-entropy-gap-in-majority-dynamic--81296e8da636

[6] *A four-step Petersen majority projection and the Desargues double-cover basin spectrum*, published mathematical finding, 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-four-step-petersen-majority-projection-and-the-desargues-doubl--b8bcbb0b4dff

[7] A. Daimari, S. Borah, D. Thongjaomayum, *Exploring the role of connectivity in disordered system*, arXiv:2603.17447, first public 2026-03-18. https://arxiv.org/abs/2603.17447
