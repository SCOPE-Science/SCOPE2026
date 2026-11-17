# Pappus majority dynamics: 92 recurrent symbols and a sharp three-step clock

## Finding
On the 18-vertex Pappus graph, synchronous binary open-neighbor majority dynamics has **92 fixed configurations** and **4,186 primitive temporal two-cycle orbits**. All \(2^{18}=262144\) labelled initial configurations satisfy
\[
F^5=F^3,\qquad F^4\ne F^2,
\]
so every trajectory enters its periodic orbit within **three** updates and this bound is sharp. The attraction basin of every periodic orbit has more states than the orbit itself.

The complete orbit-level basin census, where each basin includes all initial states eventually reaching that *temporal* orbit, is:

| Period | Basin cardinality per orbit | Number of orbits |
|---:|---:|---:|
|1|4|54|
|1|16|36|
|1|16900|2|
|2|8|1431|
|2|16|1944|
|2|32|630|
|2|520|108|
|2|1040|72|
|2|33800|1|

The period-refined first-entry census is:

| First periodic entry \(t\) | Eventually fixed | Eventually period two |
|---:|---:|---:|
|0|92|8372|
|1|1668|77484|
|2|5760|42048|
|3|27072|99648|

## Assumptions and scope
The Pappus graph here is the **18-vertex cubic bipartite Levi graph**, not the sometimes similarly named nine-vertex collinearity graph. Present its nine point vertices as \((g,i)\) with \(g\in\{0,1,2\}\) and \(i\in\mathbb Z/3\mathbb Z\), and its nine line vertices as \((a,b)\) with \(a,b\in\mathbb Z/3\mathbb Z\). Each line \((a,b)\) is joined to exactly the points \((0,a),(1,b),(2,a+b)\), arithmetic modulo three. This defines 27 edges and degree three at every vertex. Every vertex updates synchronously to 1 iff at least two of its three neighbors have value 1. Temporal rotations of the same cycle count as one orbit. All graph vertices are labelled; graph automorphisms and global bit complementation are **not** identified.

Identify a point-coloring with a nine-bit set \(S\) and line-coloring with a nine-bit set \(T\). Let \(\Phi(S)\) be the nine-bit line set whose line triples contain at least two selected points; let \(\Psi(T)\) be the nine-bit point set whose incident line triples contain at least two selected lines. Then
\[
F(S,T)=(\Psi(T),\Phi(S)),\quad P=\Psi\Phi,\quad Q=\Phi\Psi.
\]

## Proof
**Finite shore certificate (exhaustive and reproducible).** Each of the nine-vertex shores has exactly \(2^9=512\) binary subsets. The standalone standard-library script `check_pappus_projection.py` specifies the nine incidence triples in nine short integer tuples, computes \(\Phi\), \(\Psi\), \(P\), and \(Q\) by direct integer bit tests, and checks every input in the *entire* 512-element domain; no sampling or unbounded extrapolation is involved. The assertions certify:
\[
P^3=P^2,\quad Q^3=Q^2,\quad
|\operatorname{im}P|=|\operatorname{im}Q|=110,\quad
|\operatorname{im}P^2|=|\operatorname{im}Q^2|=92.
\]
The 92-element image \(\mathcal R=\operatorname{im}P^2\) is pointwise fixed by \(P\); the 92-element image \(\mathcal R^*=\operatorname{im}Q^2\) is pointwise fixed by \(Q\). The certificate also checks the stronger, necessary odd-time assertions
\[
\operatorname{im}(\Psi\Phi\Psi)=\mathcal R,\qquad
\operatorname{im}(\Phi\Psi\Phi)=\mathcal R^*.
\]
Since \(F^3(S,T)=(\Psi\Phi\Psi(T),\Phi\Psi\Phi(S))\), every third image lies in \(\mathcal R\times\mathcal R^*\). On that set, \(\Phi:\mathcal R\to\mathcal R^*\) and \(\Psi:\mathcal R^*\to\mathcal R\) are inverse bijections (also checked on every element). Hence the recurrent system is conjugate to the swap \((R,U)\mapsto(U,R)\) on \(\mathcal R^2\). Therefore all third images are periodic, \(F^5=F^3\), and there are precisely \(92\) fixed points and \(\binom{92}{2}=4186\) genuine two-cycles.

The certificate counts \(|\operatorname{im}\Phi|=|\operatorname{im}\Psi|=182\). Thus
\[
|\operatorname{im}F|=182^2=33124,\quad
|\operatorname{im}F^2|=110^2=12100,\quad
|\operatorname{im}F^3|=92^2=8464.
\]
Every third image is already periodic but \(\operatorname{im}F^2\) is strictly larger than the recurrent set; some configurations first enter their orbit at update three. Equivalently \(F^4\ne F^2\). These cardinalities and all phase-map identities are exhaustively certified by the attached source code, which acts as a short complete finite proof for this fixed graph.

**Geometric organization of the 92 symbols.** The 512-subset certificate also checks that the complete list \(\mathcal R\) has exactly the following point-class occupancy vectors, up to permuting the three classes: the empty and full sets (one each); 18 selected three-sets with occupancies \((1,1,1)\); their 18 complementary six-sets with occupancies \((2,2,2)\); 27 four-sets with occupancies \((2,1,1)\); and their 27 complementary five-sets with occupancies \((2,2,1)\). This is a complete classification, not a random subset of recurrent states.

**Exact basins.** Define \(w(r)=|\{S:P^2(S)=r\}|\), for \(r\in\mathcal R\). Complete enumeration of all nine-bit point subsets establishes the same fiber histogram for \(P^2\) and \(Q^2\): 54 symbols have fiber 2, 36 have fiber 4, and 2 have fiber 130. These sum to \(54(2)+36(4)+2(130)=512\). Under the recurrent-core swap, a fixed orbit with symbol \(r\) attracts exactly \(w(r)^2\) configurations. A two-cycle represented by two distinct core symbols \(r,s\) attracts exactly \(2w(r)w(s)\). Pairing these three fiber sizes yields every orbit count and basin cardinality in the first table. In particular the total basins are 34,592 states at fixed points and 227,552 at two-cycles, summing to 262,144. Because the smallest fiber is two, no recurrent orbit is isolated from transient initial states.

**First-entry refinement.** The image cardinalities above imply the unrefined entry layer sizes \((8464,3636,21024,229020)\) for \(t=0,1,2,3\). The separate, independent 18-bit graph-level checker `check_pappus_full.cpp` constructs the Pappus graph from an 18-cycle plus nine explicitly given chords; it evaluates all 262,144 transitions, peels the indegree-zero trees, and counts exact entry depths and least orbit periods. It checks every period-refined entry in the displayed table and checks \(F^5=F^3\) for every state. The Python script separately verifies an explicit isomorphism between the graph constructions, so this is genuinely the same graph with independent implementations.

## Verification
With Python 3 standard library available, run `python3 check_pappus_projection.py`. With a C++17 compiler, compile `g++ -std=c++17 -O2 -Wall -Wextra -pedantic check_pappus_full.cpp -o check_pappus_full` and run `./check_pappus_full`. The expected outputs are stored in the matching `.out` files. Both programs were executed on the exact packaged sources and their assertions passed. The Python computation is a mathematically exhaustive 512-subset certificate for the reduction; the independently coded C++ exhaustive 262,144-state check verifies the whole-system census, exact basins, and the sharp entry bound. Neither a failed computation nor a partial search is invoked as a proof.

## Relationship to prior work
For any finite cross-coupled synchronous system, a published periodic-core normal form reduces orbit counts to a swap on recurrent symbols. This general mechanism applies here but does not establish the **Pappus-specific 92-element shore core, its 54/36/2 fiber partition, three-step sharp entrance time or exact attraction basins**. On the Heawood graph, a different published incidence majority calculation gives 58 core symbols, a two-step cutoff, and a fiber distribution with 56 unit fibers and two fibers of 36; neither census determines the Pappus values. General results of Goles–Olivos and Benjamini and collaborators bound possible periods but do not supply the present graph-specific enumeration. Cannings studies several regular-network majority models, but an accessible abstract does not permit a full-document noncoverage conclusion.

## Limitations
The assertion concerns the specified synchronous deterministic binary open-neighbor majority rule on this **one** labelled graph. It is not an infinite-family theorem, nor a classification of different tie conventions, asynchronous updates, or other cubic graphs. The 512-subset finite proof relies on completely specified executable enumeration; it is not a symbolic closed-form classification for arbitrary incidence structures. Independent external review has not been performed; historical priority remains uncertain because a potentially relevant historical paper was not accessible in full. An unsuccessful literature search does not demonstrate uniqueness.

## References
1. C. Cannings, *The majority and minority models on regular and random graphs*, Proceedings of GAMENETS 2009, first published 2009-06-26, DOI: 10.1109/GAMENETS.2009.5137464, https://eudl.eu/doi/10.1109/gamenets.2009.5137464 .
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/abs/1405.2486 .
3. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, https://doi.org/10.1016/0012-365X(80)90121-1 .
4. *Pappus Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/PappusGraph.html (graph definition and standard identification, not a majority-dynamics enumeration).
5. *A two-step majority projection and exact attraction basins on the Heawood graph*, published research record 2026-11-02, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-step-majority-projection-and-exact-attraction-basins-on-th--8cd2964a9d93 (comparator; different graph).
6. *Periodic-core swap normal form for bipartite synchronous updates*, published research record 2026-11-08, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-periodic-core-swap-normal-form-for-bipartite-synchronous-updates--70827d4856b3 (general swap mechanism; does not give Pappus core counts).
