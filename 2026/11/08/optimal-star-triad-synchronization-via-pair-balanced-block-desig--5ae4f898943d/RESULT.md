# Optimal star–triad synchronization via pair-balanced block designs

## Finding

Consider the mean-degree-normalized two-order synchronization linearization of Zhang, Lucas, and Battiston (2022/2023). For each integer \(n\ge4\), take a pairwise star on \(n\) vertices, and any nonempty simple collection \(\mathcal H\) of three-vertex interactions entirely among its \(m=n-1\) leaves. Write \(g(\alpha,\mathcal H)\) for the smallest positive-order eigenvalue \(\lambda_2\), including zero when the Laplacian is disconnected, for the coupling split \(0\le\alpha\le1\).

**Sharp optimization and all equality cases:**
\[
 g(\alpha,\mathcal H)\le\frac{n}{n-1};\qquad
 g(\alpha,\mathcal H)=\frac{n}{n-1}
 \iff\left\{\begin{array}{l}
 \alpha=(n-2)/n,\\
 \mathcal H\text{ is a nonempty }2\text{-}(n-1,3,\mu)\text{ block design for some }\mu\ge1.
 \end{array}\right.
\]
A block design here means that *every pair of distinct leaves appears in exactly \(\mu\) triples*. The maximum is attainable for every \(n\ge4\), by choosing all triples of leaves. Every pair-balanced design, even a much sparser one, has **the same entire normalized multiorder Laplacian for every \(\alpha\)** as that complete triple system. The nonzero eigenvalues, including their multiplicities, are
\[
 \underbrace{\frac{n}{2(n-1)}(1-\alpha)+\frac{n}{n-2}\alpha}_{n-2\text{ copies}},
 \qquad
 \underbrace{\frac{n^2}{2(n-1)}(1-\alpha)}_{1\text{ copy}}.
\]
Consequently, the spectral gap is the minimum of these expressions and its unique maximizer is \(\alpha=(n-2)/n\). Relative to the pairwise-star-only spectral gap \(n/[2(n-1)]\), the best local relaxation rate is **exactly doubled**; the triples-only model is disconnected.

Every optimal triple collection has cardinality
\[
 |\mathcal H|=\frac{\mu(n-1)(n-2)}6.
\]
The universal lower bound \((n-1)(n-2)/6\) is attained precisely when the leaves admit a Steiner triple system. For \(n=8\), the seven triples
\[
 \{012,034,056,135,146,236,245\}
\]
(on leaves \(0,\ldots,6\); the hub is \(7\)) constitute a Fano-plane system. Each three-digit word denotes the set of its three displayed digits, not an integer. Seven triples therefore give the same full normalized linearization as all \(35\) possible triples, attain \(g=8/7\) at \(\alpha=3/4\), and double the star-only rate \(4/7\).

## Assumptions and scope

Let the vertices be \(V=\{0,\ldots,n-1\}\), with distinguished hub \(h=n-1\) and leaves \(U=V\setminus\{h\}\), \(|U|=m=n-1\). The first-order interactions are exactly the \(m\) unweighted edges \(\{h,u\}\) for \(u\in U\). Let \(\varnothing\ne\mathcal H\subseteq\binom U3\) be the second-order interactions, viewed as **independent hyperedges**, not as simplices requiring their pairwise edges. Each triple is present at most once, and there are no other interactions.

Define the ordinary unweighted star Laplacian \(L_1\). For each leaf \(u\), put \(k_u=|\{e\in\mathcal H:u\in e\}|\). For distinct leaves \(u,v\), let \(c_{uv}=|\{e\in\mathcal H:\{u,v\}\subseteq e\}|\). Define the symmetric triadic Laplacian by \((L_2)_{uu}=k_u\), \((L_2)_{uv}=-c_{uv}/2\) for distinct leaves, and zero in the hub row and column. The two average generalized degrees are
\[
 d_1=\frac{2(n-1)}n,\qquad d_2=\frac{3|\mathcal H|}n.
\]
With unit total coupling, use precisely the source paper's normalization
\[
 L(\alpha)=\frac{1-\alpha}{d_1}L_1+\frac{\alpha}{d_2}L_2,
 \quad 0\le\alpha\le1.
\]
Let \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_n\) denote its eigenvalues, and set \(g(\alpha,\mathcal H)=\lambda_2\). In the identical-natural-frequency phase model of the initiating paper, this equals the magnitude of the first nontrivial transverse linearized decay exponent, whenever \(g>0\). All statements concern this local linearization, not global nonlinear synchronization or heterogeneous natural frequencies.

## Proof

**1. Normalized trace and positive semidefiniteness.** Every star edge contributes a positive-semidefinite edge Laplacian of trace \(2\). Every triple contributes the positive-semidefinite \(3\)-by-\(3\) matrix having diagonal entries \(1\) and off-diagonal entries \(-1/2\), whose eigenvalues are \(0,3/2,3/2\). Therefore \(L_1,L_2\) and \(L(\alpha)\) are positive semidefinite and annihilate the constant vector. Their traces are \(2m\) and \(3|\mathcal H|\), respectively. Thus \(\operatorname{tr}L(\alpha)=n\) for every \(\alpha\). The other \(n-1\) nonnegative eigenvalues sum to \(n\), so
\[
 \lambda_2\le\frac{\lambda_2+\cdots+\lambda_n}{n-1}
 =\frac{n}{n-1}.
\]
Equality holds if and only if all \(n-1\) nonconstant eigenvalues equal \(n/(n-1)\). Since the null eigenspace then consists exactly of constant vectors, this is equivalent to the matrix identity
\[
 L(\alpha)=\frac{nI-J}{n-1},
\]
where \(J\) is the all-one matrix.

**2. Necessity of tuning and pair balance.** The hub–leaf off-diagonal entry of \(L(\alpha)\) is \(-(1-\alpha)/d_1\). Comparing it with \(-1/(n-1)\) in the displayed identity forces \(1-\alpha=2/n\), so \(\alpha=(n-2)/n\). A leaf–leaf entry equals \(-\alpha c_{uv}/(2d_2)\). At this positive value of \(\alpha\), equality of every off-diagonal entry forces each \(c_{uv}\) to be the same strictly positive integer \(\mu\). This is exactly the asserted pair-design condition.

**3. Sufficiency.** Suppose every leaf pair occurs in \(\mu\ge1\) triples. Each triple contains three leaf pairs, so \(3|\mathcal H|=\mu\binom m2\) and \(d_2=\mu m(m-1)/(2n)\). Hence for every distinct leaf pair
\[
 (L_2/d_2)_{uv}=-\frac{n}{m(m-1)},
\]
independently of \(\mu\) and of the particular design. At \(\alpha=(n-2)/n=(m-1)/(m+1)\), the leaf–leaf entry of \(L(\alpha)\) is \(-1/m\), just as the hub–leaf entry. All row sums are zero, so \(L(\alpha)=(nI-J)/(n-1)\). This proves all equality cases and attainability by the complete triple system.

**4. Full spectrum and unique maximizer.** For a pair-balanced collection the normalized triadic Laplacian has eigenvalue \(n/(n-2)\) on the \((n-2)\)-dimensional space of leaf contrasts and eigenvalue zero on the hub-versus-uniform-leaves vector. The normalized star Laplacian has respective eigenvalues \(n/[2(n-1)]\) and \(n^2/[2(n-1)]\). These spaces are invariant for both matrices, giving the two explicit eigenvalue branches in the finding. The leaf-contrast branch increases strictly with \(\alpha\) while the hub branch decreases strictly. They meet exactly at \(\alpha=(n-2)/n\); their minimum has this unique maximum, \(n/(n-1)\). The star-only gap is half this value; at \(\alpha=1\) the hub is isolated.

**5. Sparse optimal systems.** The block-design pair count yields \(|\mathcal H|=\mu m(m-1)/6\); since \(\mu\ge1\), the least possible size among optimal designs is at least \(m(m-1)/6\), with equality precisely for \(\mu=1\), a Steiner triple system. Such systems exist for \(m\equiv1,3\pmod6\). The seven listed Fano triples cover each pair of the seven leaves exactly once; this can be checked directly. The complete triple hypergraph instead contains \(\binom m3\) blocks. Whenever a Steiner triple system exists, it therefore uses exactly a \(1/(m-2)\) fraction of the complete triple interactions while giving the *identical normalized matrix for every coupling split*.

## Verification

The standalone script `verify_star_triad.py` constructs all matrices directly from edges and triples using exact rational arithmetic, with independent floating-point symmetric-eigenvalue checks. Run it with `python verify_star_triad.py` (NumPy required). It checks \(13\) balanced-design cases, \(7{,}273\) small-network/coupling comparisons obtained by exhaustively enumerating every nonempty triple subset on \(4,5,6\) vertices at seven rational coupling values, and the exact Fano/complete-collection matrix identity for five coupling values. Its output confirms \(g=8/7\) and \(g(0)=4/7\) at \(n=8\). Finite checks illustrate and guard the explicit general proof; they do not establish its universal quantifiers.

## Relationship to prior work

The 2022 preprint of Zhang, Lucas and Battiston (published in 2023) defines the precise mean-degree-normalized two-order Laplacian and the transverse Lyapunov metric, gives degree-based spectral-gap bounds, and observes nonmonotonic optimization with the coupling split on random hypergraphs. In particular, its known minimum-degree inequality already yields a universal trace-type upper bound for fixed total normalized degree. **That upper bound is not claimed as new.** The finding instead supplies its exact attainability and *complete equality topology* for star-first-order/leaf-triadic networks, a unique optimizing split, and a sparse, full-spectrum-equivalent design construction.

Lucas, Cencetti and Battiston (2020) analyze a different star–clique network consisting of two nearly disconnected pieces linked by one edge, with no triads in the star piece. Their first nontrivial mode is unaffected by the higher-order clique; this is not the star-with-all-leaves-eligible-for-triples construction here. Skardal and coauthors (2021) optimize a synchrony-alignment objective on clique complexes, in which a triple must carry its constituent dyadic edges; that restriction excludes the independent-layer star-plus-leaf-triples construction. Wang, Ji and Lü (2025) optimize a largest-eigenvalue criterion for heterogeneous-frequency alignment, not the present smallest-positive-eigenvalue criterion. The use of Steiner systems and the Fano-plane existence theorem is classical; **neither the design nor the general trace bound is claimed to be newly discovered**.

## Limitations

The result applies to symmetric unweighted pairwise stars and simple uniform three-person hyperedges, normalized separately by the mean generalized degree as in the initiating model. It optimizes local decay near full synchrony for identical natural frequencies; it does not establish global nonlinear attraction, noise robustness, a universal optimum for other pairwise graphs, or the minimization of raw interaction costs before degree normalization. Sparse equality requires a suitable combinatorial design; complete triples always give equality but can be dense. Literature comparison cannot rule out an unindexed equivalent formulation.

## References

1. Y. Zhang, M. Lucas and F. Battiston, *Higher-order interactions shape collective dynamics differently in hypergraphs and simplicial complexes*, arXiv:2203.03060 (first public release 2022-03-06), subsequently *Nature Communications* **14**, 1605 (2023), https://arxiv.org/abs/2203.03060 and https://doi.org/10.1038/s41467-023-37190-9.
2. M. Lucas, G. Cencetti and F. Battiston, *Multiorder Laplacian for synchronization in higher-order networks*, *Physical Review Research* **2**, 033410 (2020), https://doi.org/10.1103/PhysRevResearch.2.033410.
3. P. S. Skardal, L. Arola-Fernández, D. Taylor and A. Arenas, *Higher-order interactions can better optimize network synchronization*, *Physical Review Research* **3**, 043193 (2021), https://doi.org/10.1103/PhysRevResearch.3.043193.
4. C.-Y. Wang, B.-Y. Ji and L. Lü, *Optimal synchronization of higher-order Kuramoto model on hypergraphs*, *Chinese Physics B* **34**, 070502 (2025), https://doi.org/10.1088/1674-1056/adcded.
5. E. W. Weisstein, *Steiner Triple System*, MathWorld, https://mathworld.wolfram.com/SteinerTripleSystem.html (classical existence and Fano-plane background).
