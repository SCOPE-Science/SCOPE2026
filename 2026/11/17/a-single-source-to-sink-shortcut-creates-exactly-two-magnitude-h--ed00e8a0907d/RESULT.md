# A single source-to-sink shortcut creates exactly two magnitude-homology classes

## Finding
Let \(D=(V,E)\) be any finite layered directed acyclic graph with a unique source \(s\) and a unique sink \(t\), with \(d_D(s,t)=L\ge2\). Assume each vertex lies on a directed \(s\)-to-\(t\) path, and every directed path from any \(u\) to \(v\) has length \(d_D(u,v)\). Let \(D^+\) be obtained by adjoining the single missing arc \(s\to t\). All magnitude homology groups in this note have integral coefficients.

**Shortcut perturbation theorem.** For every pair of integers \(k,\ell\ge0\), there are isomorphisms of abelian groups

\[
\operatorname{MH}_{k,\ell}(D^+;\mathbb Z)\cong
\begin{cases}
\operatorname{MH}_{k,\ell}(D;\mathbb Z)\oplus\mathbb Z,&(k,\ell)=(1,1)\text{ or }(2,L),\\
\operatorname{MH}_{k,\ell}(D;\mathbb Z),&\text{otherwise.}
\end{cases}
\]

More precisely, let \(P=(s,t)\) be the open reachability interval, and \(\Delta(P)\) its order complex. For every \(k\ge2\), the **source-to-sink** summand of \(D^+\) satisfies
\[
\operatorname{MH}_{k,L}^{s,t}(D^+;\mathbb Z)\cong H_{k-2}(\Delta(P);\mathbb Z),
\]
whereas that summand for \(D\) is \(\widetilde H_{k-2}(\Delta(P);\mathbb Z)\). For the new shortcut \(\operatorname{MH}_{1,1}^{s,t}(D^+;\mathbb Z)\cong\mathbb Z\), and all other source-to-sink length summands vanish. Every endpoint summand with endpoints other than \((s,t)\) is unchanged.

In particular, the one-edge addition leaves the reachability relation unchanged, and the shortcut-augmented graph is **magnitude-diagonal precisely when \(L=2\)**. For every \(L\ge3\), it creates a nonzero off-diagonal class at \((2,L)\), arbitrarily far from the diagonal, while leaving every other positive-degree group unchanged except for the new arc class.

## Assumptions and scope
An *unweighted digraph distance* \(d_G(x,y)\) is the minimum number of arcs in a directed walk from \(x\) to \(y\), or infinity if unreachable. Magnitude chains \(\operatorname{MC}_{k,\ell}(G;\mathbb Z)\) are free abelian on \((k+1)\)-tuples of vertices with consecutive vertices distinct and finite total distance \(\ell\). Their differential omits an interior vertex if and only if this omission preserves total distance, with the usual alternating sign; endpoints are never omitted. Magnitude homology is the homology of this bigraded chain complex. A graph is *diagonal* when \(\operatorname{MH}_{k,\ell}=0\) for all \(k\ne\ell\). The graph's reachability relation is the partial order induced by directed paths.

For example, when \(D\) is the coherently directed path with \(L\) arcs, its open source-to-sink interval is a simplex and the original graph has diagonal magnitude homology. Adding only the terminal shortcut creates a nonzero \(\operatorname{MH}_{2,L}\cong\mathbb Z\) for every \(L\ge3\). For noncomplete layered networks the original graph may already have off-diagonal magnitude homology; the formula still identifies precisely the two additional free summands.

The hypotheses imply that \(P\) is nonempty and that \(s\to t\) is not already an arc. Arbitrary intermediate layer widths and missing between-layer arcs are allowed, provided the hypotheses hold; there is no assumption of a complete layered graph, a connected open interval, or torsion-freeness in higher homology. The isomorphisms in the theorem are as **abelian groups**, not asserted canonical as modules over a symmetry group.

## Proof
**1. Localization of metric changes.** Since \(s\) has no incoming arc and \(t\) has no outgoing arc, a directed walk in \(D^+\) that traverses the new arc \(s\to t\) has that arc as its entire walk. Therefore
\(d_{D^+}(x,y)=d_D(x,y)\) for every ordered pair except \((s,t)\), while \(d_D(s,t)=L\) and \(d_{D^+}(s,t)=1\). The reachability relation is unchanged. Magnitude differentials retain the first and last vertex of a chain, so the chain complex splits over ordered endpoint pairs; all pairs other than \((s,t)\) are identical before and after adding the arc. In degree zero, all vertex groups are also unchanged.

**2. Exact support of the changed endpoint chains.** A source-to-sink chain with at least one interior vertex in either graph consists of a strictly increasing sequence in the reachability order: consecutive positive finite distances force comparable distinct vertices, and acyclicity excludes repetitions along the sequence. If the interior vertices are \(v_1<\dots<v_{k-1}\), the grading assumption gives
\[
d(s,v_1)+d(v_1,v_2)+\cdots+d(v_{k-1},t)=L.\]
The shortcut cannot appear in any such chain, so for \(k\ge2\), the source-to-sink chain groups in \(D^+\) are precisely the chains of total length \(L\), in bijection with the ordinary simplicial chains \(C_{k-2}(\Delta(P);\mathbb Z)\). The exceptional chain with no interior vertex, \((s,t)\), has length \(L\) in \(D\) and length \(1\) in \(D^+\). There are no other changed source-to-sink chain groups.

**3. Boundary comparison in every degree.** For \(k\ge3\), removing any interior vertex preserves total distance because the two endpoints of the shortened segment are never simultaneously \(s,t\) (there is at least one other interior vertex), and their graded distances add. Consequently, under the correspondence above, the boundary is the ordinary simplicial boundary, up to a harmless uniform sign convention. For \(k=2\), a chain \((s,v,t)\) has length \(L\), but its omitted-interior-vertex target \((s,t)\) has length \(1\) in \(D^+\); hence \(\partial_2=0\). Thus the new endpoint chain complex at length \(L\) is exactly the **unaugmented** simplicial chain complex of \(\Delta(P)\), shifted by two. In \(D\) the length-\(L\) chain \((s,t)\) supplies the augmentation group in degree one and \(\partial_2\) is (up to sign) the simplicial augmentation, reproducing the augmented complex. This proves the two displayed endpoint homology formulas, integrally.

**4. Comparing integral groups.** Since \(P\ne\varnothing\), the augmentation map \(\varepsilon:H_0(\Delta(P);\mathbb Z)\to\mathbb Z\) is surjective and admits an abstract splitting. Therefore \(H_0(\Delta(P);\mathbb Z)\cong\widetilde H_0(\Delta(P);\mathbb Z)\oplus\mathbb Z\). For each \(j>0\), ordinary and reduced integral homology agree. The new degree-one length-one chain is a cycle with no possible length-one two-chain and gives a free \(\mathbb Z\). Combining with the unchanged endpoint pairs proves the theorem. No claim of a canonical group-equivariant splitting is needed.

**5. Diagonality boundary.** If \(L=2\), then every reachable pair in \(D\) is separated by one or two layers; its open interval is empty or discrete. The augmented order-complex model thus has homology only at \((k,\ell)=(1,1)\) or \((2,2)\), so \(D\) is diagonal. The two new positions are also diagonal, hence \(D^+\) is diagonal. If \(L\ge3\), the new nonzero group \(\operatorname{MH}_{2,L}^{s,t}\cong H_0(\Delta(P);\mathbb Z)\) lies strictly off the diagonal, so \(D^+\) is not diagonal. A general layered DAG of height at least three need **not** itself be diagonal; this distinction does not affect the exact perturbation theorem. Complete layered DAGs provide diagonal starting examples for all heights.

## Verification
The accompanying `check_shortcut.py` directly enumerates directed distances, all possible increasing vertex tuples in the magnitude chain groups, and the signed boundary matrices. It compares complete bigraded homology ranks for the original and shortcut-augmented digraphs over \(\mathbb F_2\) and \(\mathbb F_3\) across **58 finite checks**, including noncomplete layered DAGs. All show exactly the predicted two rank increments. Run with `python3 check_shortcut.py`; the recorded output is `check_shortcut.out`. The modular experiment does not prove the integral theorem or rule out torsion; the full integral conclusion is the chain-level argument in the Proof section.

## Relationship to prior work
Huntsman, *Magnitude homology and Euler characteristics of directed acyclic graphs* (arXiv:2607.23357, first posted 2026-07-25), establishes the **augmented** order-complex model for layered DAGs and explicit diagonal formulas for complete layered DAGs. The present result does **not** re-claim that base theorem: it determines the entire integral bigraded response to introducing a single non-geodesic source-to-sink shortcut. The new arc converts the exceptional augmented endpoint complex to its unaugmented analogue and creates an additional length-one class while retaining every other endpoint contribution.

Ivanov and Mukoseev, *On diagonal digraphs, Koszul algebras and triangulations of homology spheres* (arXiv:2405.04748, first posted 2024-05-08; published in 2026), give a general basis for the second magnitude homology of **all** finite digraphs (their Theorem 4.5, Corollary 4.6). This general theory can independently compute the rank of the new degree-two class. It does not state the full two-bidegree perturbation of every homology group or the integral chain comparison for arbitrary layered source-to-sink graphs. In particular, the degree-two calculation **alone** is not treated as a new theorem here. Kaneta and Yoshinaga's 2018 interval-order-complex framework provides earlier general background.

## Limitations
The theorem requires a source and a sink that are global extremal vertices, a layered graph, and a single shortcut directly from source to sink. It does not describe edges between arbitrary internal vertices, multiple simultaneous shortcuts, weighted distances, homotopy types of order complexes, or canonical equivariant splitting. The full bigraded result may be an implicit consequence of earlier general machinery even though no matching explicit statement was identified; this is the main residual originality risk. Independent mathematical audit has not been performed.

## References
1. Steve Huntsman, *Magnitude homology and Euler characteristics of directed acyclic graphs*, arXiv:2607.23357 (2026), especially Theorem 7, Corollary 8, Lemma 4 and Proposition 9. https://arxiv.org/abs/2607.23357
2. Sergei O. Ivanov and Lev A. Mukoseev, *On diagonal digraphs, Koszul algebras and triangulations of homology spheres*, arXiv:2405.04748 (2024; revised 2026), Theorem 4.5 and Corollary 4.6. https://arxiv.org/html/2405.04748v5
3. Ryuki Kaneta and Masahiko Yoshinaga, *Magnitude homology of metric spaces and order complexes*, arXiv:1803.04247 (2018), interval-order-complex description. https://arxiv.org/abs/1803.04247
