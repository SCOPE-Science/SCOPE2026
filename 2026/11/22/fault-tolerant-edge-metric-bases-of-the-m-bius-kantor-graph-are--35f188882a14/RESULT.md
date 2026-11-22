# Fault-tolerant edge metric bases of the Möbius–Kantor graph are distance-three spheres

## Finding

In the Möbius–Kantor graph \(G=\operatorname{GP}(8,3)\), the fault-tolerant edge metric dimension is exactly \(5\). There are exactly \(16\) minimum fault-tolerant edge-resolving sets, and they are precisely the sixteen radius-exactly-three spheres
\[
S_x=\{y\in V(G):d_G(x,y)=3\},\qquad x\in V(G).
\]
Every \(S_x\) consists of five vertices, all lying in a single side of the bipartition of \(G\). The family of optima has the following pairwise-intersection census: among its \(\binom{16}{2}=120\) unordered pairs, exactly \(64\) intersect in zero elements, \(8\) in two elements, and \(48\) in three elements. Consequently their optimal-set reconfiguration graph under replacement of at most \(k\) landmarks is
\[
\mathcal R_1\cong16K_1,\qquad
\mathcal R_2\cong2(K_8-4K_2),\qquad
\mathcal R_3\cong\mathcal R_4\cong2K_8,\qquad
\mathcal R_5\cong K_{16}.
\]
In particular the sharp simultaneous-replacement connectivity threshold is \(5\): changing one, two, three, or four landmarks at a time cannot connect the two optimal-placement classes. For context, the ordinary edge metric dimension is \(4\), with exactly \(368\) ordinary edge metric bases.

## Assumptions and scope

The graph is undirected, simple, and has the following complete labelled description, with indices in \(\mathbb Z/8\mathbb Z\):
\[
V(G)=\{u_i,v_i:0\le i<8\},\quad
E(G)=\{u_i u_{i+1},\ u_i v_i,\ v_i v_{i+3}:0\le i<8\}.
\]
For a landmark vertex \(z\) and an edge \(e=ab\), its edge distance is \(\delta(z,e)=\min\{d_G(z,a),d_G(z,b)\}\), where \(d_G\) is unweighted shortest-path distance. A set \(T\subseteq V(G)\) is edge resolving if, for every two distinct edges \(e,f\), at least one \(z\in T\) satisfies \(\delta(z,e)\ne\delta(z,f)\). It is one-failure fault-tolerant if \(T\setminus\{z\}\) remains edge resolving for every \(z\in T\). The equivalent test, used below, is **two distinct witnesses in \(T\) for each unordered edge pair**. An optimal fault-tolerant set is one of minimum possible cardinality. In \(\mathcal R_k\), two distinct optimal sets \(S,T\) are adjacent if \(|S\setminus T|=|T\setminus S|\le k\). All counts refer to the labelled graph just defined; no graph quotient is taken.

## Proof

**Finite exhaustive classification, with complete search domain.** There are \(16\) vertices, \(24\) edges, hence exactly \(\binom{24}{2}=276\) unordered edge pairs. For each such pair \((e,f)\), compute its full witness mask
\[
W(e,f)=\{z\in V(G):\delta(z,e)\ne\delta(z,f)\}.
\]
Then a landmark set \(T\) is edge resolving precisely when \(|T\cap W(e,f)|\ge1\) for every pair, and is one-failure fault-tolerant precisely when \(|T\cap W(e,f)|\ge2\) for every pair. These are exact integer conditions, not approximations. The general lower bound that fault-tolerant edge metric dimension is at least ordinary edge metric dimension plus one is already given by Liu et al. [4, Lemma 1.4]; since the ordinary edge metric dimension here is four, that published inequality independently yields the lower bound five.

The attached standalone C++17 program independently builds all \(24\) edges, runs breadth-first search from all \(16\) vertices, constructs all \(276\) witness masks, and iterates every bit mask of Hamming weight four or five. It counts \(368\) ordinary edge-resolving four-sets, zero fault-tolerant four-sets, and exactly \(16\) fault-tolerant five-sets. If a fault-tolerant set of size at most three existed, every four-set extension would be fault-tolerant too (the two-witness property is monotone); therefore no smaller fault-tolerant set exists. The ordinary dimension is also exactly four: the Python checker explicitly rejects all \(\binom{16}{3}=560\) ordinary three-set candidates and certifies 368 ordinary four-set bases. The general published inequality from [4] gives the same robust lower bound \(5\).

For every center \(x\), breadth-first distances have shell cardinalities \((1,3,6,5,1)\) at radii \(0,1,2,3,4\). The checkers construct the sixteen size-five distance-three spheres and verify that the resulting set of masks equals the complete independently enumerated family of sixteen fault-tolerant five-sets, with no duplications. This proves the main characterization and all finite optimality claims.

**Geometric consequences.** The graph is cubic, bipartite and has girth six. The distance-three sphere \(S_x\) is the set of five non-neighbours of \(x\) in the side opposite to \(x\), because the opposite side has eight vertices, three of which are adjacent to \(x\). Thus \(S_x=B_x\setminus N(x)\), where \(B_x\) is the side opposite \(x\). For centers in opposite sides the two spheres occupy disjoint sides, giving \(8\cdot8=64\) zero-intersection pairs. For two distinct centers \(x,y\) on the same side, the two spheres satisfy
\[
|S_x\cap S_y|=8-|N(x)\cup N(y)|=2+|N(x)\cap N(y)|.
\]
The absence of four-cycles ensures at most one common neighbour. A direct check of the eight-vertex same-side distance partition gives exactly six other centers at distance two and one at distance four from every center: for the six distance-two centers there is exactly one common neighbor, whereas the distance-four center has none. Therefore each of the two sides contributes \(8\cdot6/2=24\) pairs of intersection three and \(8\cdot1/2=4\) pairs of intersection two. The pair with intersection two defines a perfect matching in each eight-center class. This establishes the stated intersection census and immediately gives every \(\mathcal R_k\) decomposition. In particular a change of fewer than five selected vertices cannot move from an all-one-side optimum to an all-other-side optimum, while changing all five can.

## Verification

Two independently implemented executable certificates are included: `check_py.py` and `check_cpp.cpp`. Use `python3 check_py.py`; separately compile with `g++ -std=c++17 -O2 check_cpp.cpp -o check_cpp` and execute `./check_cpp`. The Python program constructs edge-distance signatures and directly deletes each chosen vertex to test fault tolerance; C++ independently constructs pair-witness bitmasks and counts witnesses by bit operations. Both enumerate every candidate of sizes four and five, not a sample. The Python certificate also verifies all three-set ordinary resolution candidates and counts exchange components for all replacement budgets. The two programs agree on \(368\), \(0\), \(16\), the sphere classification, the \((64,8,48)\) intersection census, and the \((0,48,56,56,120)\) exchange-edge sequence. These finite checks, with the explicit mask equivalence and shell argument, form the proof certificate.

## Relationship to prior work

Kelenc, Tratnik and Yero introduced the ordinary edge metric dimension in January 2016, including the exact vertex-to-edge distance definition [1]. Filipović, Kartelj and Kratica analyzed ordinary edge metric dimension for generalized Petersen graph families in 2018 [2]. Wang, Wang and Zhang later constructed ordinary edge-resolving sets in the step-three generalized Petersen family and used the Möbius–Kantor graph as an example [3]. Liu, Ahsan, Zahid and Ren formulated one-landmark-failure edge resolution, proved the general lower bound \(\operatorname{fedim}(G)\ge\operatorname{edim}(G)+1\), and computed it for paths, cycles, complete graphs and selected joined-cycle families [4]. Their concluding discussion asks for a broader account of where this one-landmark gap occurs; the present graph supplies a sharp natural example but not such a general classification. None of the inspected relevant statements supplies the sixteen-set fault-tolerant edge-metric classification or its exact exchange geometry on \(\operatorname{GP}(8,3)\). The ordinary edge metric value and graph construction are not claimed as new.

## Limitations

The theorem concerns this one named sixteen-vertex graph, not all generalized Petersen graphs. The minimum and optimizer classification rely on small, fully exhaustive computations; no unaided human enumeration of all \(\binom{16}{5}=4368\) candidate sets is claimed. The structural reconfiguration argument is analytic conditional on that complete classification. Searches of the indexed literature cannot exclude every unindexed or otherwise inaccessible earlier calculation. Independent expert audit has not been performed.

## References

[1] A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291 (first public 31 January 2016). https://arxiv.org/abs/1602.00291

[2] V. Filipović, A. Kartelj, J. Kratica, *Edge metric dimension of some generalized Petersen graphs*, arXiv:1807.00580 (2018). https://arxiv.org/abs/1807.00580

[3] D. G. L. Wang, M. M. Y. Wang, S. Zhang, *The edge metric dimension of the generalized Petersen graph P(n,3) is 4*, arXiv:2005.08038 (first public 16 May 2020); subsequent journal version. https://arxiv.org/abs/2005.08038

[4] X. Liu, M. Ahsan, Z. Zahid, S. Ren, *Fault-tolerant edge metric dimension of certain families of graphs*, AIMS Mathematics 6 (2021), 1140–1152, published online 11 November 2020, doi:10.3934/math.2021069. https://doi.org/10.3934/math.2021069
