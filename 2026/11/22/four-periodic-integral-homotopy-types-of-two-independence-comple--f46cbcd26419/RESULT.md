# Four-periodic integral homotopy types of two-independence complexes of three-arm theta graphs

## Finding
For an integer \(\ell\ge3\), let \(T_\ell=\Theta_{2,2,\ell}\) consist of two vertices \(u,v\) connected by three internally disjoint paths of edge lengths \(2,2,\ell\). Its two-independence (dissociation, three-path-free) complex \(\operatorname{Ind}_2(T_\ell)\) consists of vertex subsets all of whose induced connected components have at most two vertices. Then, **over the integers and up to homotopy equivalence**, for every \(k\) in the indicated ranges,
\[
\operatorname{Ind}_2(T_\ell)\simeq
\begin{cases}
S^{2k+1},&\ell=4k+3,\quad k\ge0,\\
S^{2k},&\ell=4k,\quad k\ge1,\\
\bigvee^3 S^{2k+1},&\ell=4k+1,\quad k\ge1,\\
\bigvee^5 S^{2k+1},&\ell=4k+2,\quad k\ge1.
\end{cases}
\]
In particular, the sphere multiplicity exhibits the repeating sequence \(1,1,3,5\) (starting at lengths \(3,4,5,6\)), and the result is an all-length classification, not a finite computational conjecture.

## Assumptions and scope
Label the poles \(u=0\), \(v=1\); the internal vertices of the two short arms are \(a=2,b=3\); and the long-arm internal vertices are \(w_1=4,\ldots,w_{\ell-1}=\ell+2\), in path order from \(u\) to \(v\). The edge set is \(ua,av,ub,bv,uw_1,w_1w_2,\ldots,w_{\ell-2}w_{\ell-1},w_{\ell-1}v\). Distinct paths meet only at the poles. The dimension of a nonempty simplex \(F\) is \(|F|-1\). All spheres and wedges refer to ordinary unbased homotopy types of geometric realizations.

## Proof
**1. Connected triples and a fixed-core path model.** A selected set is a face exactly when it contains no three vertices spanning a connected induced subgraph. For three vertices, connectedness means at least two of the three possible graph edges. Fix the selected subset \(B\subseteq\{u,v,a,b\}\). The admissible core subsets are precisely
\(\varnothing,\{u\},\{v\},\{a\},\{b\},\{u,v\},\{a,b\},\{u,a\},\{u,b\},\{v,a\},\{v,b\}\); all other cores contain a connected triple. Put \(m=\ell-1\). Conditional on an admissible core, the selected binary word \(x_1\cdots x_m\), with \(x_i=1\) denoting \(w_i\in F\), has no substring \(111\) and satisfies one left and one right endpoint condition. Write \(F\) for *free*, \(S\) for a *forbidden terminal 1*, and \(D\) for a *forbidden terminal 11*. At the left endpoint, the type is \(S\) if \(u\) and one short-arm vertex are selected, \(D\) if \(u\) alone (among its short-arm neighbors) is selected, and \(F\) otherwise. The right type is the analogous condition at \(v\). Thus the core-to-type table is

| Core | Left type | Right type |
|---|---|---|
| \(\varnothing,\{a\},\{b\},\{a,b\}\) | F | F |
| \(\{u\}\) | D | F |
| \(\{v\}\) | F | D |
| \(\{u,v\}\) | D | D |
| \(\{u,a\},\{u,b\}\) | S | F |
| \(\{v,a\},\{v,b\}\) | F | S |

There are no further restrictions: a selected connected triple not lying entirely in the core must either be three consecutive path vertices or meet a pole and its two incident selected neighbors.

**2. A uniform acyclic matching.** On the **augmented** face poset (including \(\varnothing\)), sequentially toggle the vertices in the fixed order \(w_1,\ldots,w_m,a,b,u,v\). At each vertex \(z\), pair and remove every two still-unmatched faces \(F,F\cup\{z\}\) with \(z\notin F\). By the sequential-element-matching lemma (Deshpande–Singh, Proposition 2.10, cited below), the union of these pairs is acyclic. This is a matching of actual face-cover relations, not a chain-complex heuristic. The faces remaining after the long-arm toggles are calculated separately for each of the eleven cores using its binary-word restrictions.

**3. Exact four-step path reduction.** Fix left type \(L\in\{F,S,D\}\) and right type \(R\in\{F,S,D\}\). Let \(Q_m(L,R)\) be the set of binary words surviving the successive toggles \(w_1,\ldots,w_m\), starting with *all* words avoiding \(111\) and obeying the two endpoint restrictions. For every \(m\ge7\), there is an **equality of sets**, not merely of counts:
\[
Q_m(L,R)=\{p_Lx:x\in Q_{m-4}(L,R)\},\quad
p_F=0110,\quad p_S=0011,\quad p_D=0101.
\]
Here concatenation puts the four displayed bits first. To establish this, process the first vertices, leaving the last two untouched (possible when \(m\ge7\)). In type F, toggling \(w_1\) matches every word permitting \(w_1\); an unmatched word must begin \(011\), since those two selected neighbors make insertion of \(w_1\) illegal. The next bit is forced to 0 by the forbidden \(111\); toggles at positions 2,3,4 cannot match a surviving word. The remaining word is again free on its left. In type S, \(w_1=0\) is forced; applying the same argument starting at \(w_2\) forces \(00110\), whose final 0 is the first bit of a shorter type-S instance, giving the prefix \(0011\). In type D, the first toggle forces \(x_1x_2=01\); because \(x_2=1\), the remaining suffix must begin with a forbidden pair \(11\), i.e. another D instance. Repeating once produces prefix \(0101\) and a shorter D instance. In each case the suffix has exactly the original right restriction, because it refers only to the final one or two coordinates. This proves the recurrence, including the absence of additional surviving words. Each prefix has exactly two selected vertices.

**4. The finite endpoint table, and passage to all lengths.** For \(2\le m\le10\), the eleven admissible cores and the stated one/two-bit endpoint conditions give the following exhaustive result after *all* remaining core toggles. The table reports the cores of the critical faces, and the (unique) dimension of each. These entries follow by enumerating binary words of length at most ten with the explicitly listed constraints and applying the deterministic toggles; the accompanying verifier reconstructs them independently from the original graph.

| \(m\) | Critical cores | Critical dimension |
|---|---|---|
| 2 | \(\{u\}\) | 1 |
| 3 | \(\{u,v\}\) | 2 |
| 4 | \(\{u,a\},\{u,b\},\{v,b\}\) | 3 |
| 5 | \(\{u,v\},\{u,a\},\{u,b\},\{v,a\},\{v,b\}\) | 3 |
| 6 | \(\{v\}\) | 3 |
| 7 | \(\{u,v\}\) | 4 |
| 8 | \(\{u,a\},\{u,b\},\{v,b\}\) | 5 |
| 9 | \(\{u,v\},\{u,a\},\{u,b\},\{v,a\},\{v,b\}\) | 5 |
| 10 | \(\{v\}\) | 5 |

For \(m\ge11\), the four-step reduction holds on each core. The three prefixes \(0110,0011,0101\) are pairwise distinct. Hence two surviving faces with different left types can never be matched during the remaining core toggles; within any common left type, prepending the *same* prefix preserves exactly which pairs have identical path words. Consequently the final critical faces at \(m\) are in bijection with those at \(m-4\), each with **two more vertices**. This is a full induction: the base table covers \(m=2,\ldots,10\), and the recurrence proves the critical-cell counts and dimensions for every \(m\ge11\). The isolated difference in critical core at \(m=2\) versus \(m=6\) does not affect count or dimension. Translating \(m=\ell-1\) yields exactly the four cases in the Finding.

**5. From critical cells to homotopy.** In each case all surviving critical simplices have the *same positive dimension*, with multiplicity 1, 1, 3 or 5. The augmented empty-face pairing can be replaced by one ordinary critical vertex without changing any other critical face. Forman's discrete Morse theorem therefore produces a CW complex with one zero-cell and only the stated positive-dimensional cells. All attaching maps are trivial because there are no intervening cells (and all cell dimensions are positive); hence the CW complex is the indicated wedge of spheres over \(\mathbb Z\). No extension from finite experiments is used in this deduction. \(\square\)

## Verification
Run `python3 verify.py` in the directory containing this report. The standard-library-only verifier independently constructs connected triples from graph edges, enumerates the entire two-independence face poset for \(3\le\ell\le14\), matches all faces in the stated order, and checks the critical-cell dimensions and multiplicities. It directly checks that the directed Hasse graph is acyclic for \(3\le\ell\le11\), compares against a second connected-component face test for \(3\le\ell\le10\), and checks ninety exact four-step recurrence identities (all nine endpoint-type pairs at ten path lengths). The recorded `expected_output.txt` is from a completed run. These finite checks corroborate the symbolic recurrence and all-length discrete-Morse proof; they do not substitute for it.

## Relationship to prior work
The earliest motivating public source is Sawant, arXiv:2605.25150v1 (May 24, 2026), which proves vertex decomposability of higher-independence complexes of **trees**, not this family of theta graphs, each of which contains two cycles. Deshpande and Singh, arXiv:2001.05448, give homotopy types for paths, cycles, complete multipartite graphs, fully whiskered graphs and perfect rooted trees; none includes this partially shared-cycle theta family. Their Proposition 2.10 supplies the general acyclicity principle used here, but not the new endpoint critical-cell classification. Abdelmalek et al., arXiv:2106.10863, concern chordal and tree families and likewise do not imply the present nonchordal theta classification for \(\ell\ge3\).

A previously published result for the **same six-vertex graph** \(\Theta_{2,2,3}\) instead computes the *directed multipath complex* whose vertices are directed arcs and whose faces are directed linear forests. Its reported \(\bigvee^5S^2\vee\bigvee^6S^3\) has a different face definition from the vertex-subset complex here and therefore does not imply the new \(S^1\) starting case. A separate prior multitheta classification concerns **ordinary independence** (threshold one) and symmetry representations, not threshold two. The comparison is by objects and implications, not titles alone.

## Limitations
The theorem is for exactly two length-two arms and one length-\(\ell\) arm, with threshold exactly two and \(\ell\ge3\). It does not classify arbitrary unequal three-arm theta graphs, higher thresholds, graph configuration spaces, or directed multipath complexes. The proof is a self-review; independent mathematical review has not been performed. No absence of unindexed equivalent work is claimed.

## References
1. R. Sawant, *On the Vertex Decomposability of r-Independence Complexes of Trees*, arXiv:2605.25150v1, first public May 24, 2026, https://arxiv.org/abs/2605.25150.
2. P. Deshpande and A. Singh, *Higher Independence Complexes of graphs and their homotopy types*, arXiv:2001.05448v2, https://arxiv.org/html/2001.05448v2, especially Proposition 2.10 and Theorem 4.6.
3. F. M. Abdelmalek, P. Deshpande, S. Goyal, A. Roy and A. Singh, *Chordal graphs, higher independence and vertex decomposable complexes*, arXiv:2106.10863v3, https://arxiv.org/html/2106.10863v3.
4. *The bidirected uneven-theta multipath complex is a mixed-dimensional sphere wedge*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-bidirected-uneven-theta-multipath-complex-is-a-mixed-dimensi--dcb824ea52f8.
5. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics **134** (1998), 90–145.
