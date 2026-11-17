# Universal extinction clocks for characteristic-two neighbor-sum dynamics on odd-degree trees

## Finding
Let \(T\) be a finite nonempty simple tree containing precisely one vertex \(r\) of even degree (an isolated vertex has degree zero). For states in a finite field \(\mathbb F_q\) with characteristic two, synchronously replace every vertex state by the sum of its neighbors' previous states. If \(h\) is the eccentricity of \(r\), then **the exact global extinction time is \(2h+1\)**: every state is zero by then and some state survives to the preceding update. An impulse at distance \(\ell\) from \(r\) has exact extinction time \(h+\ell+1\).

For \(h\ge1\), writing \(N=|V(T)|\) and \(\tau(x)\) for the first zero time, the complete *last-two-layer* distribution is
\[
\#\{x:\tau(x)=2h+1\}=(q-1)q^{N-1},\quad
\#\{x:\tau(x)=2h\}=(q-1)q^{N-2},\quad
\#\{x:\tau(x)\le2h-1\}=q^{N-2}.
\]
In particular, the probability of maximal extinction time for uniform initial states is \(1-1/q\), unaffected by all branching choices. When \(h=0\), there are \(q-1\) states with extinction time 1 and one already-zero state.

The maximum transient time can exceed diameter by an unbounded amount even when maximum degree is three: an explicit height-\(h\) comb has diameter \(h+1\) and maximal extinction time \(2h+1\).

## Assumptions and scope
The graph is finite, simple, undirected, connected, and acyclic. Its **exactly one** even-degree vertex is the distinguished root \(r\); every other degree is odd. Degrees count graph edges, and the isolated root is allowed. Each nonroot vertex has one parent, so it has an even number of children; the root also has an even number of children. Thus all rooted child counts are even, including zero. Let \(L_j\) denote the vertices of depth \(j=d(r,v)\), let \(L_h\ne\varnothing\) denote the deepest level, and let \(e_v\) be the coordinate-unit state. Iteration is simultaneous in \(\mathbb F_q\), where \(q\) is any power of two. The period of the unique zero state is one; every nonzero state becomes zero and has no other eventual orbit.

## Proof
Define linear maps on vertex states: the childward lift \((Ux)_v=x_{p(v)}\) for nonroot \(v\), with \((Ux)_r=0\); and the rootward summation \((Dx)_v=\sum_{w\text{ child of }v}x_w\). Adjacency update is \(F=A=U+D\). For each vertex \(v\),
\[
(DUx)_v=\sum_{w\text{ child of }v}x_v=(\#\text{children of }v)x_v=0
\]
because each child count is even and the characteristic is two. Also \(U^{h+1}=D^{h+1}=0\) by depth. Since any operator word containing adjacent factors \(DU\) vanishes, the only potentially nonzero words in the noncommutative expansion of \((U+D)^k\) consist of a block of \(U\)'s followed by a block of \(D\)'s, each appearing exactly once. Therefore
\[
A^k=\sum_{a+b=k}U^aD^b.
\]
If \(k\ge2h+1\), every term has \(a>h\) or \(b>h\), hence \(A^{2h+1}=0\).

For any \(v\) of depth \(\ell\), \(D^\ell e_v=e_r\) (the unique parent path), while \(D^{\ell+1}e_v=0\). At time \(h+\ell\), in the displayed expansion the only possible nonzero term is \(U^hD^\ell e_v=U^he_r=\mathbf 1_{L_h}\). The deepest level is nonempty, so this state is nonzero, and at time \(h+\ell+1\) all terms vanish. Thus \(\tau(e_v)=h+\ell+1\), giving the claimed maximum \(2h+1\) at deepest impulses.

For arbitrary \(x\), the only term in \(A^{2h}\) is \(U^hD^h\). Therefore
\[
A^{2h}x=\Big(\sum_{v\in L_h}x_v\Big)\mathbf 1_{L_h}.
\]
This has rank one, so the kernel has \(q^{N-1}\) states, proving the first count. When \(h\ge1\),
\[
A^{2h-1}=U^hD^{h-1}+U^{h-1}D^h.
\]
The first summand depends on the sum of depth-\(h-1\) inputs and has output in depth \(h\); the second depends on the sum of depth-\(h\) inputs and has output in depth \(h-1\). The two levels are nonempty and disjoint, so these two rank-one maps have independent inputs and outputs. Hence \(\operatorname{rank}A^{2h-1}=2\). The number with first zero time \(2h\) is \(|\ker A^{2h}|-|\ker A^{2h-1}|=q^{N-1}-q^{N-2}\); the remaining states die earlier. For \(h=0\) the adjacency map is zero, yielding the separate stated counts.

For the claimed degree-three family, begin with root \(u_0\). For \(0\le i<h-1\), give spine vertex \(u_i\) exactly two children, one side leaf and the next spine vertex \(u_{i+1}\). Give final spine vertex \(u_{h-1}\) exactly two leaf children. All nonroot internal vertices have graph degree three, all other nonroot vertices have degree one, and the root has degree two. This tree has \(2h+1\) vertices and height \(h\); its diameter is \(h+1\) (one deepest leaf and the root's side leaf attain it). The proved extinction index is \(2h+1\), so the difference is \(h\). No finite experiment is used to pass from the construction to the arbitrary-\(h\) conclusion.

## Verification
Two independent implementation paths are included. `verify_graph.py` builds **unrooted** trees and applies the binary adjacency map directly to coordinate vectors, checks exact impulse lifetimes, powers/ranks, top-layer form, and exhaustive initial states for small orders. It checked 409 eligible nonisomorphic trees of order at most 15 and 30 comb instances (with explicit dynamic checks through comb height seven). `verify_operators.py` independently builds even-child rooted trees, confirms \(DU=0\), expands each relevant matrix power by words, and checks impulse extinction on 250 independently generated trees of order at most 213. Both scripts passed. To replay, install the declared dependency from `requirements.txt` and run `python3 verify_graph.py` and `python3 verify_operators.py`. Captured standard output is in `verification_graph.txt` and `verification_operators.txt`.

The verification is finite evidence supporting the argument. The universal statement rests on the algebraic proof above. Direct executable tests use binary coefficients; extension to all finite characteristic-two fields is by the proved field-independent identities.

## Relationship to prior work
The algebraic representation of additive cellular automata and finite-field update maps is classical: Wolfram (1983), and Martin, Odlyzko and Wolfram (1984) give broad treatments. The inspected 1984 primary manuscript develops regular one-dimensional and multidimensional lattice additive rules, not the present irregular finite-tree parity criterion, impulse-depth formula, or exact terminal-layer census. A later paper on nilrigidity of infinite tree cellular automata (Salo, 2019) addresses a different setting: infinite trees and cellular-automaton rigidity, rather than sharp finite-graph extinction times. An earlier public mathematical discussion of tree adjacency matrices notes their decomposition into directed nilpotent pieces, but nilpotency of each summand does **not** imply nilpotency of their sum; the vanishing mixed product used here is essential. Existing recorded findings on parity automata on complete multipartite graphs, distance-two Boolean cubes, and a fan graph use different graph families and do not imply this theorem.

## Limitations
This is not a classification of all trees with nilpotent adjacency over characteristic two; the one-even-degree hypothesis is sufficient, not asserted necessary. The remaining early extinction-time layers need not have the simple universal multiplicities above. Nothing is claimed for characteristic other than two. The historical searches, read primary source, and comparisons did not reveal a covering result, but inaccessible or unindexed equivalent results remain a priority risk. Independent validation has not been performed.

## References
1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics **55** (1983), 601–644, DOI: `10.1103/RevModPhys.55.601`, first public date recorded as 1983-07-01.
2. O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258, DOI: `10.1007/BF01223745`; open full text: `https://content.wolfram.com/sw-publications/2020/07/algebraic-properties-cellular-automata.pdf`.
3. V. Salo, *Trees are nilrigid*, arXiv:1905.06093 (2019), `https://arxiv.org/abs/1905.06093`.
4. MathOverflow (2012), *If graph is tree what can be said about its adjacency matrix?* (discussion of nilpotent directed decompositions; not the present cancellation or lifetime theorem).
