# An unbounded adaptive gap at fixed VC dimension for simple cycles of wheels

## Finding

Let \(W_{r+1}=K_1\vee C_r\) be the wheel with \(r\ge3\) rim vertices, and let \(\mathcal C_r\) be the family of **edge sets of all simple cycles** of this wheel. Each binary query asks whether an edge belongs to an unknown member of \(\mathcal C_r\). The following theorem concerns this exact concept class, not the binary cycle space, unions of cycles, or vertex membership.

**Theorem.** The known static dimensions and the new adaptive bounds obey
\[
\operatorname{VCdim}(\mathcal C_r)=
\begin{cases}2,&r=3,\\3,&r\ge4,\end{cases}
\]
\[
\operatorname{Ldim}(\mathcal C_3)=2,\qquad
\operatorname{Ldim}(\mathcal C_4)=3,\qquad
\operatorname{Ldim}(\mathcal C_5)=4,
\]
and, for every \(r\ge5\),
\[
\boxed{\max\{4,\lfloor\log_2(r-1)\rfloor\}
\ \le\ \operatorname{Ldim}(\mathcal C_r)
\ \le\ \lfloor\log_2(1+r(r-1))\rfloor.}
\]
In particular, the six-vertex wheel \(W_6\) is the first wheel with strictly larger Littlestone than VC dimension. Every larger wheel has such a gap, and the gap is unbounded on this **planar** family although the VC dimension remains exactly three. The static wheel VC values were determined by Mofidi and are recalled for comparison; novelty is claimed only for the adaptive assertions and their separation consequence, subject to the literature limitations below.

## Assumptions and scope

The wheel has rim vertices \(v_0,\ldots,v_{r-1}\) in cyclic order and hub \(h\). Label rim edges \(e_i=\{v_i,v_{(i+1)\bmod r}\}\), indexed \(0\le i<r\), and spokes \(s_i=\{h,v_i\}\), indexed \(0\le i<r\). A cycle is a simple undirected cycle, represented by its set of edges. In the standalone certificate, the bit positions \(0,\ldots,r-1\) encode rim edges and positions \(r,\ldots,2r-1\) encode spokes. A concept is a cycle's edge-membership function on this \(2r\)-edge ground set.

A set of \(d\) distinct edges is VC-shattered when all \(2^d\) traces occur. The Littlestone dimension is the largest depth of a complete binary decision tree whose internal nodes are edge queries, with each leaf labeled by an actual cycle realizing all zero/one answers along its path. This adaptive tree need not ask the same edge at the same depth in different branches.

## Proof

**Cycle count and universal online upper bound.** There is one rim-only simple cycle. Every other simple cycle contains the hub, hence exactly two distinct spokes, with a unique proper nonempty rim arc connecting their endpoints. For each unordered spoke pair there are exactly two rim arcs. Consequently
\[
|\mathcal C_r|=1+2\binom r2=1+r(r-1).
\]
The \(2^d\) paths of a realized complete depth-\(d\) binary tree require \(2^d\) distinct cycle witnesses, because two distinct answer paths cannot be realized by the same cycle. Thus \(2^d\le1+r(r-1)\), proving the upper bound.

**Static dimension.** Mofidi, *On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs*, Theorem 3.4(2), proves exactly \(\operatorname{VCdim}(\mathcal C_3)=2\) and \(\operatorname{VCdim}(\mathcal C_r)=3\) for \(r\ge4\). Its proof observes that each cycle is a rim or has exactly two spokes; a shattered set with two spokes contains at most one rim edge, one with one spoke contains at most two rim edges, and no four rim edges are shattered; three rim edges can be shattered for \(r\ge4\). These facts establish the stated static formula and are *not* new contributions.

**Two small wheels.** For \(r=3\) there are seven cycles, so \(\operatorname{Ldim}\le\lfloor\log_2 7\rfloor=2\), matching VC dimension. For \(r=4\) there are thirteen cycles, so \(\operatorname{Ldim}\le\lfloor\log_2 13\rfloor=3\), again matching VC dimension. This rules out any earlier strict separation within wheel graphs.

**The first strict gap, certified exactly.** For \(r=5\), the concept family has twenty-one simple cycles, so \(\operatorname{Ldim}\le\lfloor\log_2 21\rfloor=4\). The included `wheel_r5_tree.json` provides an explicit complete depth-four decision tree: every internal node records a bit-indexed edge query, every leaf an integer bit mask representing an actual simple cycle, and all sixteen root-to-leaf paths have a distinct realizing cycle. The standalone `verify_wheel.py` reconstructs the wheel's simple cycles independently via adjacency-based depth-first enumeration and checks every tree edge and leaf witness. This establishes \(\operatorname{Ldim}(\mathcal C_5)\ge4\) by a finite explicit certificate, hence equality; no search timeout or numerical approximation is involved.

**Persistence for every larger wheel.** Fix \(r\ge5\). Obtain a rim cycle on \(r\) vertices from the five-vertex rim by subdividing its five edges into five internally vertex-disjoint paths, each with at least one edge. Retain the five original rim vertices and their five spokes to the common hub. Every simple cycle of \(W_6\) maps to a simple cycle of \(W_{r+1}\) by replacing each used original rim edge by its entire subdivided rim path; the hub and original spokes are unchanged. Pick one edge as the representative of each of the five subdivided paths. On these five rim representatives and the five retained spokes, the mapped cycles realize precisely the same membership patterns as the original cycles. Hence the certified complete depth-four tree for \(W_6\) remains realized in \(W_{r+1}\). Therefore \(\operatorname{Ldim}(\mathcal C_r)\ge4\) for every \(r\ge5\).

**An unbounded logarithmic lower bound.** For \(1\le j\le r-1\), take the cycle consisting of spokes \(s_0,s_j\) and the clockwise rim arc from \(v_0\) to \(v_j\), whose rim edges are exactly \(e_0,\ldots,e_{j-1}\). Restrict queries to \(e_1,\ldots,e_{r-2}\). The answer to query \(e_k\) on concept \(j\) is one precisely when \(j>k\). Thus these \(r-1\) concepts induce the complete ordered threshold family on \(r-1\) ordered values. Threshold queries can split a contiguous candidate interval of size \(N\) into two subintervals of sizes at least \(\lfloor N/2\rfloor\); repeatedly splitting the candidate interval yields a full mistake tree of depth \(\lfloor\log_2 N\rfloor\). Taking \(N=r-1\) proves the second lower bound, independently of the finite depth-four certificate. For each \(r\ge5\), VC dimension is three while Littlestone dimension is at least four; as \(r\) grows, the latter diverges. This completes the proof.

## Verification

The standalone `verify_wheel.py` enumerates cycles *from graph adjacency*, not from the counting proof's arc formula. For rim sizes \(3\) through \(8\) it exhaustively evaluates static shattering on every subset through size four and computes the exact adaptive rank by first-query minimax recursion over distinct concept subsets. The resulting pairs \((\operatorname{VCdim},\operatorname{Ldim})\) are \((2,2),(3,3),(3,4),(3,4),(3,5),(3,5)\), respectively. It also independently checks all sixteen cycle witnesses in `wheel_r5_tree.json` against the depth-four tree and verifies they are distinct. Running `python verify_wheel.py wheel_r5_tree.json` prints `WHEEL_CYCLE_SHATTERING_CHECKS_PASS; W6_tree_depth=4; leaf_witnesses=16`. The general claims are proved by the arguments above, not inferred from these finite enumerations. No external proof assistant or independent mathematical audit has been used.

## Relationship to prior work

Mofidi's 2022 *Transactions on Combinatorics* article studies precisely the cycle hypergraph of wheel graphs and establishes the VC-dimension values quoted above, along with their contrast to spanning-tree hypergraph VC dimension. Mofidi's 2022 *Facta Universitatis* article also analyzes the cycle-hypergraph concept and static VC information. Neither inspected article defines or calculates a Littlestone mistake tree for wheel cycle edge membership, nor gives the present four-depth certificate, persistence embedding, or unbounded online-versus-static gap. Guingona, Kolesnikov, Nierwinski and Soucy (2021) discuss VC and Littlestone dimensions for a different class, linear zero sets, and provide terminology and theoretical context, but their equal-dimension theorem has different assumptions. Prior work on cover-free graph families and on wheel graph cycle counts is about different invariants; the cycle-count formula itself is elementary and not new.

## Limitations

This gives exact online dimensions only for rim sizes three, four, and five, and general upper/lower bounds for larger wheels; it does **not** determine a sharp formula for every larger rim size. Although the trace checks extend through rim size eight, finite data do not establish further exact cases generally. The claimed contribution is in adaptive complexity, not the already-known VC dimension, the basic wheel cycle count, or the standard fact that finite concept classes satisfy a cardinality bound on online depth. An equivalent result may exist under alternate online-learning or graph-cycle terminology; the accessible searches and primary-text inspections do not establish absolute priority. The date 2021-09-10 records the earliest precisely verified public source among the cited theoretical background (the arXiv first version); one specific wheel VC paper is indexed as published in March 2022 without a verified day, so that journal month has not been converted to an invented day. Independent mathematical review has not been performed.

## References

1. A. Mofidi, *On the VC-dimension, covering and separating properties of the cycle and spanning tree hypergraphs of graphs*, Transactions on Combinatorics 11 (2022), 29–43, DOI: 10.22108/TOC.2021.127880.1832. Full text: https://toc.ui.ac.ir/article_25746_890e066e8b9dd269c189910e7e780475.pdf, especially Theorem 3.4(2), pages 38–39.
2. A. Mofidi, *On the Number of Cycles of Graphs and VC-Dimension*, Facta Universitatis, Series Mathematics and Informatics 37 (2022), 121–135. DOI: 10.22190/FUMI210301011M. Public date 2022-05-10 as recorded by the MaRDI portal.
3. V. Guingona, A. Kolesnikov, J. Nierwinski and R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1, publicly submitted 2021-09-10. https://arxiv.org/abs/2109.04805.
