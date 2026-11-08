# Parity-filtered attractors and exact relaxation spectra for stochastic minority on partially whiskered cycles

## Finding
Let \(n\ge3\) and choose any nonempty subset \(S=\{s_1,\ldots,s_k\}\) of the vertices of the labelled cycle \(C_n\), in cyclic order. Attach one private pendant leaf at every marked vertex, and let \(\ell_i\ge1\) be the number of cycle edges on the arc from \(s_i\) to \(s_{i+1}\) (indices cyclic), so \(\sum_i\ell_i=n\). At each discrete step, one of the \(N=n+k\) vertices, chosen uniformly, changes to the minority bit among its **closed neighborhood**, retaining its current bit in case of equality.

Define an admissible index set \(I\subseteq\{1,\ldots,k\}\) by the two conditions: \(|I|\equiv n\pmod2\), and \(I\) contains no two **distinct cyclically adjacent** indices. For \(k=1\), both the empty and singleton sets satisfy the adjacency condition; for \(k=2\), the two indices are adjacent.

**Theorem.** The terminal recurrent communicating classes are indexed by an admissible \(I\) and a global bit \(\epsilon\in\{0,1\}\). The class has exactly \(\prod_{i\in I}\ell_i\) configurations, with the empty product equal to \(1\). More strongly, its state-transition graph is the Cartesian product of path graphs with \(\ell_i\) vertices, one for each \(i\in I\), with self-loops from inactive updates. Every initial configuration enters one of these classes almost surely. Each class has the uniform stationary distribution.

The total number of recurrent configurations is therefore exactly
\[
R_{n,S}=2\sum_{\substack{I\text{ admissible}}}\prod_{i\in I}\ell_i,
\]
and the number of recurrent communicating classes is
\[
A_{n,k}=2\#\{I:I\text{ admissible}\}.
\]
For \(k\ge2\), the latter number depends only on \(k\) and the parity of \(n\), not on the positions of the leaves:
\[
\boxed{A_{n,k}=L_k+2(-1)^n\cos(k\pi/3),}\qquad k\ge2,
\]
where \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\) are the Lucas numbers. For \(k=1\), \(A_{n,1}=2\).

The full transition spectrum within a class \((I,\epsilon)\) is
\[
\boxed{\left\{1-\frac2N\sum_{i\in I}\left[1-\cos\left(\frac{r_i\pi}{\ell_i}\right)\right]:0\le r_i<\ell_i\right\}.}
\]
All eigenvalues are counted with their multiplicities. If at least one occupied arc has \(\ell_i\ge2\), the class is nontrivial and its spectral gap is
\[
\boxed{\gamma_{I}=\frac2{n+k}\left(1-\cos\frac{\pi}{\max_{i\in I}\ell_i}\right).}
\]
Singleton classes have no nonzero relaxation mode.

For example, \(n=12\) and marked vertices \(S=\{0,2,5,7\}\) give arc lengths \((2,3,2,5)\): exactly six recurrent classes, of sizes \(1,1,4,4,15,15\), including four nonabsorbing classes with two persistent monochromatic cycle edges. Their total recurrent population is \(40\), although the cycle itself is bipartite.

## Assumptions and scope
The graph is simple, undirected, and consists of exactly one labelled cycle with exactly one leaf attached at each marked vertex. Marks are distinct, and adjacent marked vertices are allowed. All bits are binary. Updates choose a vertex uniformly among **all** \(n+k\) vertices, including currently inactive vertices. The minority is computed on the closed neighborhood; tie retention is essential. A recurrent communicating class means a closed irreducible component of the resulting finite Markov chain, not a deterministic period orbit. No statement is made about absorption probabilities from a specified initial configuration or time to reach the recurrent set.

The theorem concerns a graph-indexed stochastic cellular automaton and its recurrent dynamical structure (MSC2020 37B15). The earliest public source used to motivate the problem is the November 23, 2010 arXiv preprint of Rouquier, Regnault, and Thierry.

## Proof
**1. Edge particles and strict energy drops.** Call an edge a particle edge when its endpoint bits agree. Let \(E\) be the number of such edges. At a vertex of degree \(d\) with \(t\) incident particle edges, the closed-neighborhood minority rule flips its bit precisely when \(2t\ge d\). A flip changes \(E\) by \(d-2t\). Thus \(E\) never increases. A degree-one leaf with a particle on its edge flips and reduces \(E\) by one. Consequently no recurrent configuration has a particle on a leaf edge. Once all leaf edges are particle-free, each marked vertex has degree three and cannot flip at constant energy: if both incident cycle edges are particles, it flips with a strict energy drop of one; otherwise it stays fixed. Every unmarked cycle vertex has degree two. One incident particle causes a reversible, energy-preserving flip, moving that particle to the other cycle edge; two incident particles cause a strict energy decrease by two.

**2. Exclusion of non-admissible particle patterns.** In a putative recurrent configuration, a leaf particle would yield an immediate strict energy drop. Suppose instead that all leaf edges are particle-free. If one arc between consecutive marks contains at least two particles, select two consecutive particles on that arc and move one toward the other through energy-preserving flips at internal degree-two vertices; when the particles occupy consecutive edges, flipping their shared internal vertex strictly decreases \(E\). If two distinct adjacent arcs both contain particles, first apply the preceding case if either arc contains at least two. Otherwise move the unique particle of each arc along its arc until both are on edges incident to their common marked vertex. Flipping this degree-three vertex strictly reduces \(E\). These finite positive-probability update sequences preclude every such configuration from belonging to a closed communicating class.

**3. Sufficiency and completeness.** Conversely, assume all leaf edges are particle-free; each arc contains zero or one cycle particle; and no distinct adjacent arcs both contain a particle. Degree-one and degree-three vertices cannot change bit, since they see respectively zero and at most one incident particle. A degree-two vertex can only transport the unique particle along its own occupied arc; it never creates another particle or crosses a marked endpoint. Therefore the occupied arcs form an invariant set \(I\), and within each such arc the unique particle can move between all \(\ell_i\) edge positions via reversible positive-probability transitions. Moves on distinct occupied arcs commute, proving that the product of paths is closed and irreducible. Every finite Markov chain enters some closed class almost surely. Steps 1–2 show that no other closed classes exist.

**4. Cyclic consistency and complement.** Along a cycle, the number of disagreeing edges must be even. Hence the number of agreeing (particle) edges has parity \(n\). This is exactly the restriction \(|I|\equiv n\pmod2\). Conversely, choose one cycle-root bit \(\epsilon\), an admissible \(I\), and a particle position independently in each occupied arc. Walk once around the cycle, preserving the bit across particle edges and reversing it across other cycle edges; parity guarantees closure. Assign each leaf the bit opposite its marked parent. This constructs a unique configuration and proves the two choices of \(\epsilon\) yield disjoint classes. Counting all choices proves \(R_{n,S}\) and \(A_{n,k}\).

**5. Position-independent class count.** For \(k\ge2\), let \(F_k(w)=\sum_{I\text{ independent}}w^{|I|}\) be the ordinary independence polynomial of the cycle on \(k\) index positions, treating \(k=2\) as a single adjacency. Then \(A_{n,k}=F_k(1)+(-1)^nF_k(-1)\). The two transfer eigenvalues for the cycle independence polynomial are \((1\pm\sqrt{1+4w})/2\); their \(k\)-th powers sum to \(F_k(w)\) for \(k\ge2\). At \(w=1\) this sum is \(L_k\). At \(w=-1\) it is \(2\cos(k\pi/3)\). For \(k=1\), a single arc can be empty or occupied without violating distinct-index adjacency, giving exactly two complement-related classes of the permitted parity.

**6. Transition spectrum.** For each occupied arc of length \(\ell\), its particle is a reflecting nearest-neighbor walk on the \(\ell\) edge positions; each allowed left or right move has probability exactly \(1/N\) per global update. The corresponding combinatorial path Laplacian has eigenvalues \(2[1-\cos(r\pi/\ell)]\), \(0\le r<\ell\). The class transition matrix is the identity minus \(1/N\) times the sum of these commuting path Laplacians. Their tensor-product eigenbasis yields the displayed complete spectrum. If some \(\ell_i\ge2\), the smallest positive Laplacian eigenvalue occurs on the longest occupied arc, giving the gap formula. Uniform stationarity follows also directly from symmetry of every permitted single-site transition.

## Verification
Two implementations were run from the enclosed source code. The direct-state implementation constructs the actual transition digraph and determines its closed strongly connected components for **all 243 nonempty marked subsets over cycle sizes \(3\le n\le7\)**, jointly involving **335,632 labelled binary states**. It agrees with the predicted multiset of recurrent class sizes in every case. A separate implementation constructs recurrent configurations from occupied-arc positions, checks closure, irreducibility and reversibility for 32 chosen graph instances through \(n=9\), and verifies the reflecting-path spectral formula on path lengths through \(20\). This is finite supporting evidence; steps 1–6 are the all-size proof. See `verification/class_scc.py`, `verification/class_scc_output.txt`, `verification/class_product.py`, and `verification/class_product_output.txt`.

## Relationship to prior work
Rouquier, Regnault, and Thierry, *Stochastic Minority on Graphs* (arXiv:1011.5119, first posted November 23, 2010), supplies exactly the closed-neighborhood asynchronous minority model and the monotone particle-energy method. Their Theorem 4.2 treats paths and cycles without leaves, and Theorem 4.6 classifies attractors on **trees** of maximum degree three via matchings in a reduced tree. Neither theorem covers the present unicyclic graph: cyclic consistency imposes a global parity obstruction; stable higher-energy recurrent classes may coexist with the bipartite ground state; and the complete product-path transition spectrum is new to the present calculation. The matching/independent-set connection is acknowledged as methodological prior art, not asserted to be invented here.

The Lucas-number identity for independence sets on a cycle is classical; see Alexander and Hearding, *A graph-theoretic encoding of Lucas sequences* (arXiv:1501.00061, December 31, 2014), which explicitly cites Prodinger and Tichy. The purely combinatorial identity is **not** a novelty claim. The claim evaluated here concerns the complete recurrent-class realization, parity selection, gap-dependent class populations, and exact relaxation spectra for the stochastic dynamics.

Papp and Wattenhofer, *Stabilization Time in Minority Processes* (arXiv:1907.02131, July 3, 2019), addresses stabilization complexity under differently specified update schedules; its abstract does not determine the present communicating classes. Only its abstract was available for comparison. Other unindexed treatments of zero-temperature antiferromagnetic relaxation may use equivalent language; historical priority has not been independently established.

## Limitations
The theorem establishes exact recurrent structure and within-class relaxation eigenvalues, but not the distribution of which class is reached from arbitrary initial states, nor a bound on time to enter the recurrent union. A spectral gap is not a bound on global mixing across multiple closed classes; no unique global stationary distribution is claimed. The additional Lucas identity is already classical. The published-model comparison is detailed but not an exhaustive historical-priority certification. No independent scientific audit has been performed.

## References
1. J.-B. Rouquier, D. Regnault, and E. Thierry, *Stochastic Minority on Graphs*, arXiv:1011.5119 (first public arXiv version, 2010-11-23); https://arxiv.org/abs/1011.5119. In particular Definition 2, Lemma 1, Theorems 4.2 and 4.6.
2. J. Alexander and P. Hearding, *A graph-theoretic encoding of Lucas sequences*, arXiv:1501.00061 (2014-12-31); https://arxiv.org/abs/1501.00061. See Theorem 1.1 and the citation of Prodinger and Tichy.
3. P. A. Papp and R. Wattenhofer, *Stabilization Time in Minority Processes*, arXiv:1907.02131 (2019-07-03); https://arxiv.org/abs/1907.02131. Contextual reference; only title and abstract inspected.
