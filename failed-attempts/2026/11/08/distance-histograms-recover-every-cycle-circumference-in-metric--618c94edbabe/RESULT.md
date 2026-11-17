# Distance histograms recover every cycle circumference in metric cactus graphs

## Finding

Let \(G\) be any finite connected metric cactus graph with strictly positive edge lengths and positive total arclength \(L>0\). Select points \(X,Y\) independently according to normalized arclength on \(G\), and set \(D=d_G(X,Y)\), the intrinsic shortest-path distance. Write \(F(r)=\Pr(D\le r)\), and use the continuous (on each side) density representative \(f=F'\) away from its finitely many breakpoints.

**Cycle-spectrum recovery theorem.** For each \(c>0\), let \(m(c)\) be the number of distinct cycle blocks of \(G\) with total circumference \(c\), counting coincident circumferences with multiplicity. Then
\[
 f(0+)=\frac{2}{L},\qquad
 f(c/2+)-f(c/2-)=-\frac{2c\,m(c)}{L^2}.
\]
There are no other jump discontinuities of \(f\) at positive radii; every jump is strictly negative. Consequently the *single unlabeled two-point distance distribution* determines \(L=2/f(0+)\), the full multiset of cycle circumferences, and the first Betti number \(\beta_1(G)=\sum_{c>0}m(c)\). A cactus is a tree if and only if \(f\) has no positive-radius jumps. The assertion includes bridges of arbitrary lengths, cycles meeting at articulation vertices, unequal or equal cycle circumferences, and any finite cactus block tree.

A complete finite expression for \(F\) and \(f\) is given below. It establishes the jump theorem without a generic-position assumption.

## Assumptions and scope

A metric cactus is the intrinsic path-metric realization of a finite connected undirected graph with strictly positive edge lengths and at least one edge, in which every edge belongs to at most one simple cycle. Subdivision of an edge does not change the object; a cycle block is a maximal cycle viewed as one metric circle. Decompose the graph into its **blocks** \(B_1,\dots,B_s\): all simple cycles, each regarded as one block, and each bridge regarded as one interval block. Different blocks meet, if at all, only at vertices, which have zero arclength measure. Let \(\ell_i\) be the arclength of block \(B_i\), and put
\[
 h_i=\begin{cases}\ell_i/2,&B_i\text{ is a circle},\\ \ell_i,&B_i\text{ is a bridge}.
 \end{cases}
\]
The bipartite block–vertex incidence graph is a tree after omitting isolated degree-two subdivision vertices. For every pair \(i<j\), the unique route between blocks defines an *exit* vertex \(v_{ij}\in B_i\) and an *entry* vertex \(w_{ij}\in B_j\); let \(\delta_{ij}=d_G(v_{ij},w_{ij})\ge0\). The intervening route may pass through further blocks, but is independent of the two sampled positions within the endpoint blocks.

For real \(z\), use \(z_+=\max\{z,0\}\). For \(a,b>0\), define
\[
 T_{a,b}(z)=\frac{z_+^2-(z-a)_+^2-(z-b)_+^2+(z-a-b)_+^2}{2ab},
\]
\[
 t_{a,b}(z)=\frac{z_+-(z-a)_+-(z-b)_++(z-a-b)_+}{ab}.
\]
These are respectively the CDF and density (away from knots) of the sum of independent \(\operatorname{Uniform}[0,a]\) and \(\operatorname{Uniform}[0,b]\) variables.

## Proof

**1. Distances between different blocks.** The cactus condition implies that the block–cut incidence structure is a tree. Therefore every path from an interior point \(x\in B_i\) to an interior point \(y\in B_j\), for \(i\ne j\), must exit \(B_i\) at \(v_{ij}\) and enter \(B_j\) at \(w_{ij}\). A detour outside a cycle that connects two distinct vertices of that cycle would create an additional simple cycle sharing one of its edges, contrary to the cactus condition. Thus every shortest path has length
\[
 d_G(x,y)=d_{B_i}(x,v_{ij})+\delta_{ij}+d_{B_j}(w_{ij},y).
\]
For an interval of length \(b\), distance from an endpoint to an arclength-uniform point is uniform on \([0,b]\). For a circle of circumference \(c\), distance from a fixed vertex to an arclength-uniform point is uniform on \([0,c/2]\), because every distance in the open interval has two equidistant source positions. Hence, conditional on \(X\in B_i,Y\in B_j\), the distance is \(\delta_{ij}+U_i+U_j\), with independent \(U_k\sim\operatorname{Uniform}[0,h_k]\). Both assignments of the two independent labeled points occur with combined probability \(2\ell_i\ell_j/L^2\). The cross-block CDF contribution is therefore
\[
 \frac{2\ell_i\ell_j}{L^2}\,T_{h_i,h_j}(r-\delta_{ij}).
\]
As \(t_{a,b}\) is continuous on all of \(\mathbb R\) and piecewise linear, no cross-block contribution can create or cancel a density jump.

**2. Distances within one block.** Within a circle block of circumference \(c\), no external path can shorten either circular arc between two of its points; such a path would contradict the cactus condition as above. The intrinsic distance of two independent arclength-uniform circle points is uniform on \([0,c/2]\), so the unconditional circle-block CDF and density contributions are respectively \(c^2\min\{1,2r/c\}/L^2\) and \((2c/L^2)\mathbf1_{(0,c/2)}(r)\). Within a bridge block of length \(b\), shortest paths are the direct interval paths, and the absolute difference of two independent uniform positions has CDF \(1-(1-r/b)_+^2\) and density \(2(b-r)_+/b^2\). The corresponding weighted contributions are \([b^2-(b-r)_+^2]/L^2\) and \(2(b-r)_+/L^2\).

**3. Exact global CDF.** Let \(\mathcal C\) denote the circle blocks and \(\mathcal E\) the bridge blocks. Summing the mutually exclusive within-block and cross-block events gives, for every \(r\ge0\),
\[
\boxed{
L^2F(r)=\sum_{C\in\mathcal C} c_C^2\min\{1,2r/c_C\}
+\sum_{e\in\mathcal E}[b_e^2-(b_e-r)_+^2]
+2\sum_{1\le i<j\le s}\ell_i\ell_j\,T_{h_i,h_j}(r-\delta_{ij}).}
\]
Here \(c_C\) is the circumference of cycle \(C\), and \(b_e\) is the length of bridge \(e\). Differentiating on open intervals avoiding finitely many knots yields
\[
\boxed{
L^2f(r)=2\sum_{C\in\mathcal C} c_C\mathbf1_{(0,c_C/2)}(r)
+2\sum_{e\in\mathcal E}(b_e-r)_+
+2\sum_{1\le i<j\le s}\ell_i\ell_j\,t_{h_i,h_j}(r-\delta_{ij}).}
\]
It follows directly that \(F\) is continuous and absolutely continuous, and \(f\) is piecewise affine with a finite number of breakpoints and jump discontinuities. Formulae are independent of the values assigned to \(f\) *at* individual knots.

**4. One-sided limits and inverse statement.** Let \(r\downarrow0\). Every circle contributes \(2c_C\), every bridge contributes \(2b_e\), and every cross-block contribution tends to zero (even when \(\delta_{ij}=0\), because \(t_{a,b}(0)=0\)). Hence \(L^2f(0+)=2(\sum_Cc_C+\sum_eb_e)=2L\). At a strictly positive radius, the bridge and cross-block terms in the density are continuous; a circle of circumference \(c\) contributes a single downward jump of height \(2c/L^2\) at exactly \(r=c/2\). Thus for any \(r>0\),
\[
 f(r+)-f(r-)=-\frac{4r\,m(2r)}{L^2}.
\]
No cancellation is possible. Recovering the multiplicities from jump sizes, and summing the one independent homology generator per cactus cycle, proves the theorem. When there are no cycles the graph is a tree, and conversely, completing the tree criterion. \(\square\)

## Verification

The reproducible standalone script `verify.py` uses Python's standard library only. Execute `python3 verify.py`. It implements the displayed formulas with exact `fractions.Fraction` rational arithmetic and an independent shortest-path sampler over original weighted graph edges. The four test geometries are: one bridge; one three-edge cycle; that cycle with a bridge; and a multiply-connected cactus with three cycles including two of circumference five, together with two bridges. Checks include exact total CDF mass, 316 exact density/CDF derivative comparisons away from knots, exact rational recovery of four distinct cycle-threshold groups (counted across examples), a near-zero derivative identity, and 140,000 independent sampled point pairs. The last run reported a maximum CDF sampling error 0.004476 over the compared thresholds. This sampling error is not a rigorous probabilistic error bound. The all-graph statement rests on the displayed blockwise proof, not on finite tests.

## Relationship to prior work

Bose, De Carufel, Grimm, Maheshwari, and Smid (CCCG 2013; detailed paper 2015) study continuous shortest-path metric geometry and farthest-point queries on cactus networks, including cycle/bridge decomposition. The present inverse theorem asks a different question: what the unlabeled two-point geodesic-distance law determines.

Garijo, Márquez, and Silveira (first preprint 2021; published 2023), especially Lemma 4.1 and Proposition 4.2, give a cut-vertex decomposition and linear-time computation of **mean distance** of weighted cactus graphs. An expectation alone does not furnish the full law or identify its density discontinuities; the present distributional formulas and cycle-spectrum reconstruction are not their stated result. The same authors' full-text section 4 was inspected for this implication.

Mémoli and Needham (2018 preprint; published 2022) study distance-distribution inverse problems for metric measure spaces and prove a local injectivity statement for metric graphs. Their accessible abstract does not state the exact cactus cycle-jump law. Their complete article was not accessible during the literature check, so potential overlap remains a historical-priority limitation rather than a claim of comprehensive exclusion.

## Limitations

Only the multiset of *cycle circumferences*, total length, and first Betti number are asserted recoverable. The theorem does not claim that the entire weighted graph or the attachment locations are determined, nor that a finite noisy sample uniquely resolves nearby jumps. The sampling measure is normalized **arclength on the continuous metric graph**, not uniform counting measure on vertices. The cactus condition is essential to the proof and is not replaced by a restriction merely on cycle rank. Some pertinent historical sources were inaccessible in full; independent priority and mathematical validation are unperformed.

## References

1. P. Bose, J.-L. De Carufel, C. Grimm, A. Maheshwari, and M. Smid, *Optimal Data Structures for Farthest-Point Queries in Cactus Networks*, 25th Canadian Conference on Computational Geometry, August 8–10, 2013. https://cccg.ca/proceedings/2013/papers/paper_23.pdf
2. P. Bose et al., *Optimal Data Structures for Farthest-Point Queries in Cactus Networks*, Journal of Graph Algorithms and Applications **19** (2015), 11–41. https://doi.org/10.7155/jgaa.00345
3. D. Garijo, A. Márquez, and R. I. Silveira, *Continuous Mean Distance of a Weighted Graph*, Results in Mathematics **78** (2023), 139. https://arxiv.org/abs/2103.11676 ; https://doi.org/10.1007/s00025-023-01902-w
4. F. Mémoli and T. Needham, *Distance Distributions and Inverse Problems for Metric Measure Spaces*, Studies in Applied Mathematics **149** (2022), 943–1001. https://arxiv.org/abs/1810.09646 ; https://doi.org/10.1111/sapm.12526
5. D. Baptista, J. B. Kennedy, and D. Mugnolo, *Mean Distance on Metric Graphs*, Journal of Geometric Analysis **34** (2024). https://arxiv.org/abs/2312.04952
