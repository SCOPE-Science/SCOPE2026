# The gcd sphere law for avalanche complexes of two independently firing directed cycles

## Finding
For integers \(a,b\ge3\), write \(N=a+b\) and \(d=\gcd(a,b)\). Two disjoint consistently oriented directed cycles, each initially containing exactly one empty vertex and one chip at every other vertex, have avalanche complex
\[
\mathcal A(\overrightarrow C_a\sqcup\overrightarrow C_b,c_0)\simeq S^{N-d-2}.
\]
The exact firing period is \(\operatorname{lcm}(a,b)\), and the unique nonzero reduced integral homology group is \(\mathbb Z\) in degree \(N-d-2\). The result is about the **simultaneous** firing process; joining or disjointly uniting the two individual avalanche complexes would give an incorrect answer in general.

## Assumptions and scope
Cycles have disjoint labeled vertex sets \(A=\{u_0,\ldots,u_{a-1}\}\) and \(B=\{v_0,\ldots,v_{b-1}\}\). Arcs are \(u_i\to u_{i+1}\) and \(v_j\to v_{j+1}\), indices understood modulo the respective cycle lengths. Initially, \(c_0(u_0)=c_0(v_0)=0\) and every other entry equals one; independent cyclic relabeling covers every choice of empty positions. At each integer time, every vertex whose chip count is at least its outdegree fires once, simultaneously sending one chip along its outgoing arc. Both outdegrees equal one. The avalanche complex is the downward closure of all **nonempty** firing sets, as in Riihimäki–Smith [1]. It uses the combined vertex set \(A\sqcup B\).

## Proof
**Step 1: dynamics and a bipartite omission graph.** At time \(t\), exactly \(u_{t\bmod a}\) and \(v_{t\bmod b}\) have no chip. Every other vertex fires. Under the parallel update, the missing chip advances by one position on each cycle. This follows by induction: each occupied site sends its only chip forward, while the successor of the empty site receives none. Consequently the configuration and firing set have exact period \(T=\operatorname{lcm}(a,b)\).

Let \(H\) be the bipartite graph on \(A\sqcup B\) with edges \(\{u_{t\bmod a},v_{t\bmod b}\}\), for \(0\le t<T\). The Chinese remainder theorem says that a pair \((i,j)\) occurs exactly when \(i\equiv j\pmod d\), where \(d=\gcd(a,b)\). Thus \(H\) is the disjoint union of \(d\) copies of \(K_{a/d,b/d}\). The facets of the avalanche complex \(X\) are exactly \((A\sqcup B)\setminus e\) for edges \(e\) of \(H\), since all omitted pairs have size two and are distinct.

Equivalently, writing \(\operatorname{Ind}(H)\) for the independence complex, \(X=\operatorname{Ind}(H)^*\) under Alexander duality on the full ground set: a subset \(\sigma\) belongs to \(X\) precisely when its complement contains an edge of \(H\).

**Step 2: a graph false-twin suspension lemma.** For a finite simple graph \(J\) with at least one edge, let \(Y(J)=\operatorname{Ind}(J)^*\). Fix a vertex \(u\) of \(J\), and add a new vertex \(x\), adjacent to exactly the neighbors of \(u\), but not to \(u\). Then
\[
Y(J+x)\simeq \Sigma Y(J)
\]
provided the geometric realization \(|Y(J)|\) is nonempty. Indeed, in \(Y(J+x)\), the link of \(x\) is exactly \(Y(J)\), because when a simplex contains \(x\), its complement has an edge if and only if the complementary old vertices contain an edge of \(J\). The deletion of \(x\) is a cone with apex \(u\): for any simplex not containing \(u\), adding \(u\) still leaves an excluded edge. If the original witness edge was \(u\!\text{--}\!w\), the excluded false-twin edge \(x\!\text{--}\!w\) remains instead; every other witness persists. Thus the complex is a union of two contractible subcomplexes (the deletion and the cone from \(x\) over the link), meeting in \(Y(J)\). The simplicial inclusions are cofibrations, and their homotopy pushout is \(\Sigma Y(J)\).

**Step 3: begin with a matching.** Contract each residue-block bipartite component abstractly to a single edge, obtaining a matching \(J_d\) of \(d\) edges. For \(d\ge2\), \(Y(J_d)\) has \(d\) facets, each the complement of one matching edge. Every proper subcollection of these facets has nonempty intersection, but the intersection of all \(d\) is empty. The simplicial nerve theorem therefore gives \(Y(J_d)\simeq\partial\Delta^{d-1}\simeq S^{d-2}\).

For \(d=1\), \(Y(J_1)\) has only the empty simplex. Its first false-twin addition produces exactly two isolated vertices, hence \(S^0\), directly. This avoids invoking a geometric suspension of an empty realization.

**Step 4: expand the bipartite blocks.** Each \(K_{a/d,b/d}\) is obtained from an edge by adding \(a/d-1\) false twins of the vertex on the first side and \(b/d-1\) false twins on the second. Across the \(d\) components there are exactly \(N-2d\) additions. For \(d\ge2\), iterating Step 2 gives a sphere of dimension \((d-2)+(N-2d)=N-d-2\). For \(d=1\), the first addition yields \(S^0\), and the remaining \(N-3\) additions yield \(S^{N-3}\), which is the same dimension formula. Since \(a,b\ge3\), all final spheres have nonnegative dimension, and in fact dimension at least one. The integral reduced homology statement follows. This establishes the theorem for **all** permitted parameters without extrapolating finite tests.

## Verification
The embedded standalone script `verify.py` reconstructs the simultaneous chip-firing orbit from the initial configuration, checks the exact least period and the Chinese-remainder omitted-pair graph for all \(36\) ordered pairs \(3\le a,b\le8\), and independently builds **every simplex** of each resulting avalanche complex for the \(26\) pairs satisfying \(a+b\le12\). It computes all reduced homology ranks over \(\mathbf F_2\) using full boundary matrices, and checks the unique predicted sphere degree and rank in every such case. The saved output ends with `ALL_VERIFY_OK`. These finite checks corroborate, but do not replace, the all-parameter proof above.

## Relationship to prior work
Riihimäki and Smith [1, §2, Corollary 3.20] define the avalanche complex and calculate the sphere for a **single** one-hole directed cycle; their Proposition 3.24 treats a **vertex-glued wedge of two identical cycles**, not a disjoint union with independently advancing holes. Their discussion preceding Proposition 3.24 raises questions about graph operations. The present theorem answers a specific disjoint-union case and reveals that the dimension depends on the greatest common divisor of the component lengths. The Alexander-dual definition and the nerve/homotopy-pushout principles used in the proof are classical tools, not asserted as new discoveries.

## Limitations
The result requires two **disjoint**, consistently oriented directed cycles and exactly one missing chip in each component. It does not classify more than two cycles, changed chip numbers, joined cycles, or other firing conventions. The complete homotopy type is proved but no natural equivariant splitting or new persistence barcode is asserted. Unindexed stronger prior literature may exist; independent mathematical auditing has not been performed.

## References
[1] H. Riihimäki and J. P. Smith, *Avalanche homology of digraphs via sandpile dynamics*, arXiv:2606.26786, first public 2026-06-25, revised 2026-11-02, especially §2 and §§3.2–3.3. https://arxiv.org/abs/2606.26786
[2] Classical simplicial nerve theorem, combinatorial Alexander duality, and homotopy pushout for two contractible simplicial subcomplexes (standard topological tools; no new attribution claimed).
