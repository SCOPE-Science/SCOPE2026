# A marked Poisson shape law for disappearing three-vertex components in band random graphs

## Finding

Let \(C_n^{m_n}\) be the \(m_n\)-th power of the labeled cycle \(\mathbb Z/n\mathbb Z\). Independently retain each host edge with probability
\[
p_n=1-\exp\!\left[-\frac{\log n+2\log\log n+c}{6m_n}\right],
\qquad c\in\mathbb R,
\]
where \(m_n/\log n\to\infty\) and \(m_n/n\to0\). Write the three vertices of an isolated three-vertex component in their unique short cyclic order as \((i,i+a,i+a+b)\), with \(1\le a,b\le m_n\). For a tree component, mark \(h\in\{L,M,R\}\) according as its unique degree-two vertex is the left, middle, or right member of this ordered triple. Place an atom at \((i/n,a/m_n,b/m_n,h)\).

**Marked Poisson theorem.** The point process of such atoms converges weakly, as a finite point process on \(\mathbb T\times[0,1]^2\times\{L,M,R\}\), to a Poisson point process with intensity
\[
\boxed{\nu(dx\,du\,dv\,dh)=\frac{e^{-c}}{36}\,dx\,du\,dv\,
\bigl[\mathbf1_{\{h=M\}}+\mathbf1_{\{u+v\le1\}}(\mathbf1_{\{h=L\}}+\mathbf1_{\{h=R\}})\bigr].}
\]
Here \(\mathbb T=\mathbb R/\mathbb Z\), and the counting measure on the three marks is implicit. Thus the unmarked number of three-vertex components (including possible three-cycles) tends to \(\operatorname{Poisson}(e^{-c}/18)\). The probability of any three-cycle component tends to zero.

The limiting conditional shape of a randomly selected three-vertex component, given that one exists, has consecutive normalized gap density
\[
\boxed{f(u,v)=\frac12\bigl(1+2\mathbf1_{\{u+v\le1\}}\bigr),\qquad 0<u,v<1.}
\]
In particular, **the three vertices form a host-graph triangle with limiting probability \(3/4\)** even though their retained component is a two-edge tree with probability tending to one. Conditional on the component existing, its spatially middle vertex is the tree's degree-two vertex with probability tending to \(1/2\); the spatially left and right vertices each have limiting probability \(1/4\). Conditionally on \((u,v)\), the center is forced to be \(M\) if \(u+v>1\), and otherwise is uniform among \(L,M,R\).

For every \(n>6m\) and \(0<p<1\) (with \(q=1-p\)), the finite mean of the number \(Z_{n,3}\) of *all* three-vertex components is exactly
\[
\boxed{\mathbb E Z_{n,3}=
\frac{nm(m+1)}2p^2q^{6m-4}
+\frac{nm(m-1)}2(3p^2-2p^3)q^{6m-6}.}
\]
This finite identity is part of the same finding, not a separate claim.

## Assumptions and scope

The graph is undirected, simple, and has exactly \(n\) labeled vertices; \(m=m_n\) is an integer satisfying \(m/\log n\to\infty\) and \(m=o(n)\). The fixed real parameter \(c\) is arbitrary, with \(p_n\in(0,1)\) for sufficiently large \(n\). A three-vertex *component* is a connected component of the retained graph of exactly three vertices, with no retained edges to outside vertices. A *tree component* has exactly two retained edges; a three-cycle has all three. The host-graph triangle event means that all three possible pairs were admissible host edges, not that all three edges were retained. A center mark is assigned only to tree components. The short cyclic representation is unique for all sufficiently large \(n\), since \(n>6m\); its anchor is the vertex immediately after the unique long cyclic gap. Edge cases \(u+v=1\) are null for the limiting Lebesgue measure. Weak convergence of the finite point processes means convergence of all disjoint continuity-set counts to independent Poisson counts with the stated intensity.

## Proof

**1. Geometric triple classification.** Write \(m=m_n\). In \(C_n^m\), any connected three-vertex host set has a spanning tree with two edges, each of cyclic length at most \(m\). Since \(n>6m\), all its vertices lie in a unique short cyclic arc of total length at most \(2m\). Write them as \((i,i+a,i+a+b)\) with \(1\le a,b\le m\); conversely every such pair produces a connected host triple because its consecutive pairs are adjacent. The pair of extreme vertices is additionally a host edge if and only if \(a+b\le m\). Thus there are \(n m(m-1)/2\) triples whose induced host graph is a triangle, and \(n m(m+1)/2\) whose induced host graph is a path. For the path the only possible spanning tree is centered at \(M\). For the host triangle there are exactly three possible two-edge spanning trees, one centered at each of \(L,M,R\).

**2. Exact probabilities.** A three-vertex host path has exactly \(6m-4\) incident host edges other than its two internal edges. To be an isolated three-vertex component, both must be open and all other incident edges closed, of probability \(p^2q^{6m-4}\). A host triangle has \(6m-6\) external edges; its internal retained graph is connected with probability \(3p^2q+p^3=3p^2-2p^3\). This proves the finite mean identity. In a triangle, the event that a specified spanning tree is the entire component has probability \(p^2q^{6m-5}\); for a host path it has probability \(p^2q^{6m-4}\). Actual three-cycle components have mean
\[
\frac{nm(m-1)}2\,p^3q^{6m-6}.
\tag{1}
\]

**3. Exact centering and first marked intensity.** Put \(L_n=\log n+2\log\log n+c\). Then \(q_n^{6m}=e^{-L_n}=e^{-c}/[n(\log n)^2]\), and the condition \(m/\log n\to\infty\) gives \(p_n\to0\) and \(mp_n/\log n\to1/6\). Hence
\[
nm^2p_n^2q_n^{6m}\longrightarrow \frac{e^{-c}}{36}.
\tag{2}
\]
For every Riemann-integrable test function of \((x,u,v,h)\), summation over anchors \(i\) and the grid \((a/m,b/m)\), using the exact path/triangle tree weights in Step 2, converges to the integral against \(\nu\). Its total mass is \(e^{-c}/18\), since
\[
\int_{[0,1]^2}\!\left(1+2\mathbf1_{\{u+v\le1\}}\right)du\,dv=2.
\tag{3}
\]
By (1)–(2), the expected number of actual triangular components is \(O(p_n)\to0\); they may be discarded for the limit.

**4. Factorial moment measures.** Index candidate tree-component events by a triple of vertices together with a specific two-edge host spanning tree and center mark. Two distinct such events cannot both hold if their vertex sets overlap: distinct connected components are disjoint, and two different tree configurations on the same triple cannot occur simultaneously. There are at most \(3nm^2\) candidate events, and for each fixed event at most \(O(m^2)\) other candidates have intersecting vertex sets (each of its three vertices belongs to only \(O(m^2)\) candidate triples). Consequently, for each fixed \(r\), the fraction of ordered \(r\)-tuples of candidates with any vertex collision is \(O_r(1/n)\).

For an ordered collection of \(r\) vertex-disjoint candidate tree configurations, each event prescribes two internal edges open and all other host edges incident to its triple closed. The prescriptions are compatible. The only duplicated prescriptions are closed host edges crossing between two distinct triples, at most \(9\binom r2\) such edges. Thus the exact joint probability equals the product of the \(r\) individual probabilities multiplied by \(q_n^{-b}\) with \(0\le b\le9\binom r2\). Because \(p_n\to0\), this factor is \(1+o_r(1)\), uniformly over all configurations. Individual event probabilities are uniformly \(p_n^2q_n^{6m}(1+O(p_n))\), and their total sum is bounded by (2)–(3). Their maximal weight tends to zero. It follows that every mixed factorial moment of counts in disjoint continuity sets converges to the product of the corresponding \(\nu\)-masses, i.e. to the mixed factorial moments of independent Poisson variables. The factorial-moment characterization (and bounded total intensity) yields convergence of finite point processes to the stated Poisson process.

**5. Conditional geometry.** Marginalizing over center marks gives intensity proportional to \(1+2\mathbf1_{\{u+v\le1\}}\). The triangle subregion has area \(1/2\) and weight three; its share of total mass two is \(3/4\). The middle-center mark has unit weight on the whole square, hence probability \(1/2\); each end-center mark has unit weight on the area-\(1/2\) triangle, hence probability \(1/4\). The Poisson process has almost surely finite count, and conditional on a positive count, its atoms are iid with normalized intensity; this establishes the claimed random-component conditional law.

## Verification

Run `python verify_band_triples.py` with Python 3.9+ (standard library only). The code independently enumerates the admissible triple sets and all their internal retained-edge subsets for finite \(n,m\), checks exact boundary counts and the finite expectation and center decomposition with rational arithmetic, checks the cross-edge correction for disjoint pairs of candidate component events, and tests numerical finite-parameter centering and discrete shape weights. The checker passed **59,808 assertions**. Those tests validate finite identities and the implementation; the infinitary marked Poisson convergence follows from Steps 3–5, not from finite enumeration.

## Relationship to prior work

Chakraborty, Luh, and Singh (2026), *Band Random Graphs: Connectivity, Geometry, and Transport* (arXiv:2610.42107v1), define this precise cycle-power percolation model and establish connectivity and isolated-vertex Poisson limits at a *different*, higher retention scale. Their Sections 1.2, 4.1, 4.4, and 7 discuss these results and connectivity questions; the present calculation concerns the rare spatial arrangements of components of *exactly three* vertices at an earlier extinction scale. See https://arxiv.org/abs/2610.42107.

The previously published *Universal Poisson extinction windows for fixed-size components of high-degree regular percolation* proves, for any growing-degree regular host, the scalar \(k=3\) count limit \(\operatorname{Poisson}(e^{-c}/18)\) at exactly the same extinction scale. **That scalar limit is prior work and is not presented here as new.** Its theorem and proof do not provide a joint limiting distribution for cyclic position, both internal gap lengths, and degree-two center. The genuinely distinguishing claim here is the joint marked intensity and its \(3/4,1/2,1/4\) shape/topology consequences. See https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-universal-poisson-extinction-windows-for-fixed-size-components-o--e4e16ddb2b60/RESULT.md.

Penrose (2015/2018), *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, studies fixed-order components in a **random-point connection model**, not the specified deterministic cycle-power host with these geometric marks. Penrose and Yang (2022), *On \(k\)-clusters of high-intensity random geometric graphs*, study random-position geometric clusters, which are not the same bond-percolated fixed lattice/cycle model. Those works are relevant context for general cluster Poisson approximations; no claim of a wholly new Poisson methodology is made.

## Limitations

The marks and constants require uniform edge retention and \(m/\log n\to\infty\), \(m=o(n)\). They are not asserted for fixed bandwidth, higher-dimensional tori, growing component sizes, or position-dependent retention. This is a finite-cluster spatial limit, not a connectivity or giant-component theorem. An independently performed mathematical audit and a comprehensive historical-priority certification have not occurred. The main 2026 motivating paper's relevant original sections and the published regular-host scalar theorem were examined, but older geometric cluster literature may contain a reducible marked result; random-point and deterministic-host models should not be conflated.

## References

1. S. Chakraborty, K. Luh, R. P. Singh, *Band Random Graphs: Connectivity, Geometry, and Transport*, arXiv:2610.42107v1, first public 2026-10-30, https://arxiv.org/abs/2610.42107.
2. *Universal Poisson extinction windows for fixed-size components of high-degree regular percolation*, 2026, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-universal-poisson-extinction-windows-for-fixed-size-components-o--e4e16ddb2b60/RESULT.md.
3. M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132 (2015), *Journal of Applied Probability* 55 (2018), 112–136, https://arxiv.org/abs/1507.07132.
4. M. D. Penrose, X. Yang, *On \(k\)-clusters of high-intensity random geometric graphs*, arXiv:2209.14758 (2022), https://arxiv.org/abs/2209.14758.
