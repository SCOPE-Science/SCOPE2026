# Fixed-point slack, shattering, and the top cycle of involution assignment complexes

## Finding

Let \(\mathcal I_n=\{\pi\in\mathfrak S_n:\pi^2=\mathrm{id}\}\), and represent each \(\pi\) by its Boolean permutation matrix \(G_\pi=\{(i,\pi(i)):i\in[n]\}\). Queries range over **all ordered** cells of \([n]^2\). Let \(\Delta_n\) be the simplicial complex of VC-shattered query supports, with \(\Delta_0=\{\varnothing\}\).

**Exact support criterion.** A support \(S\subseteq[n]^2\) is shattered if and only if it consists of \(f\) distinct diagonal cells and \(e\) off-diagonal cells, each off-diagonal cell representing one oriented edge, such that the underlying loops and undirected edges are pairwise vertex-disjoint and
\[
 f=0\quad\text{or}\quad 2e+f<n.
\]
In particular, a support cannot contain both \((i,j)\) and \((j,i)\) for \(i\neq j\). Thus the only further obstruction after consistency with disjoint involution cycles is a *fully saturated support containing a fixed-point query*.

The complete face polynomial and its exponential generating function are
\[
 \Phi_n(z)=\sum_{\substack{e,f\ge0,\ 2e+f\le n\\ f=0\ \mathrm{or}\ 2e+f<n}}
 \frac{n!}{e!f!(n-2e-f)!}\,z^{e+f},
 \qquad \sum_{n\ge0}\Phi_n(z)\frac{t^n}{n!}
 =e^{zt^2}\left(e^{(1+z)t}-e^{zt}+1\right).
\]
For \(n\ge2\), \(\operatorname{VCdim}(\mathcal I_n)=\operatorname{Ldim}(\mathcal I_n)=n-1\); at \(n=1\), both dimensions are zero.

**Facet spectrum and integral top homology.** For \(n\ge2\), the facets of \(\Delta_n\) are exactly the admissible partial involution query supports occupying \(n-1\) vertices, together with the oriented perfect matchings with no loops when \(n\) is even. Hence all facet cardinalities \(\lfloor n/2\rfloor,\ldots,n-1\) occur (and \(\Delta_n\) is nonpure for \(n\ge4\)). The number of facets using exactly \(e\) off-diagonal cells and one uncovered vertex is \(n!/[e!(n-1-2e)!]\), for \(0\le e\le\lfloor(n-1)/2\rfloor\). When \(n\) is even, add \(n!/(n/2)!\) oriented perfect-matching facets. For every \(n\ge3\),
\[
 \widetilde H_{n-2}(\Delta_n;\mathbb Z)\cong\mathbb Z,
\]
whose generator is the oriented boundary of the simplex on all \(n\) diagonal queries.

**Sampling threshold.** If \(m=m(n)\) distinct ordered cells are chosen uniformly from \([n]^2\), then whenever \(m/\sqrt n\to c\in[0,\infty)\),
\[
 \Pr(\text{sampled support is shattered})\longrightarrow e^{-2c^2}.
\]
The limiting probability tends to one for \(m=o(\sqrt n)\), and to zero if \(m/\sqrt n\to\infty\).

## Assumptions and scope

All permutation matrices are those of unrestricted **self-inverse** permutations, fixed points are allowed, and both orientations of an off-diagonal matrix cell are distinct query coordinates. Supports are sets of distinct queried cells; every assignment of zero/one answers must occur on one of the permitted matrices. An involution consists of disjoint fixed points and two-cycles. Homology is ordinary reduced integral simplicial homology. The binomial/factorial formulas use \(0!=1\) and include the empty support. The limit samples without replacement from all \(n^2\) positions and has no conditioning on off-diagonal positions.

## Proof

**1. Necessity of disjoint oriented cycles.** If \(S\) is shattered, its all-one trace is the restriction of an involution. Two distinct positive queries cannot prescribe incompatible images or conflicting two-cycles/fixed points. The sole exception to naïve vertex-disjointness is the pair \((i,j),(j,i)\): these always have the same answer under every involution, so they cannot both appear in a shattered support because the opposite-answer trace would be missing. Thus every shattered support is as in the first sentence of the criterion.

Suppose such a support occupies all \(n\) vertices and includes at least one diagonal cell \((i,i)\). Prescribe that cell zero and **every other queried cell one**. Those other positives fix or pair every vertex except \(i\), leaving no distinct partner for \(i\); yet the zero answer forbids fixing \(i\). No involution realizes this trace. Hence the saturation condition is necessary.

**2. Explicit witness for every permitted trace.** Let \(S\) satisfy the criterion and prescribe any labeling. Install every positive queried two-cycle and every positive queried fixed point. All these consume disjoint vertices. Let \(K\) be the set of vertices whose **diagonal** queries are labeled zero. No vertex of \(K\) belongs to any queried two-cycle, and distinct vertices in \(K\) do not belong to positive fixed-point queries. If \(|K|\) is even, pair its vertices arbitrarily into two-cycles. If \(|K|\) is odd, then \(f>0\), so the criterion guarantees a vertex \(u\) that is not incident to **any** cell of \(S\). Pair one vertex of \(K\) with \(u\), and pair the remaining elements of \(K\) arbitrarily. Fix every vertex still unused. The prescribed positive answers are realized. Every negative diagonal is in a constructed two-cycle. Every negative off-diagonal query has both endpoints distinct from those of the constructed cycles and is therefore false. This constructs a valid involution for every labeling. When \(f=0\), the odd case does not arise. Necessity and sufficiency prove the criterion for all \(n\), including the empty universe.

**3. Exact enumeration.** Choose \(e\) disjoint *unordered* pairs and \(f\) additional singletons, leaving \(r=n-2e-f\) unqueried vertices. Their count is \(n!/(2^ee!f!r!)\). Choosing one of the two ordered query orientations on each pair contributes \(2^e\), hence \(n!/(e!f!r!)\). Retain all choices except \(r=0,f>0\), obtaining \(\Phi_n(z)\). Exponential enumeration of unqueried vertices, queried singletons and oriented queried pairs gives \(e^{(1+z)t+zt^2}\). Subtract the forbidden saturated configurations with at least one queried singleton, enumerated by \((e^{zt}-1)e^{zt^2}\). This gives the stated exponential generating function. In particular,
\[
 \Phi_2(z)=1+4z,\quad\Phi_3(z)=1+9z+3z^2,\quad
 \Phi_4(z)=1+16z+42z^2+4z^3,
\]
\[
 \Phi_5(z)=1+25z+130z^2+70z^3+5z^4.
\]
There are \(n\) shattered supports of size \(n-1\), consisting of all but one of the diagonal queries; there is no shattered support of size \(n\). Therefore \(\operatorname{VCdim}=n-1\) for \(n\ge2\).

**4. Adaptive dimension.** For any positive answer at the root of a query tree, the remaining involutions, after removing its forced vertices, form a copy of \(\mathcal I_{n-1}\) for a diagonal query and \(\mathcal I_{n-2}\) for an off-diagonal query. Inductively, the positive branch has Littlestone dimension at most \(n-2\), so a full depth-\(n\) tree is impossible. The base family \(\mathcal I_1\) has one concept and dimension zero, and the empty family of vertices also has dimension zero. Thus \(\operatorname{Ldim}\le n-1\). Static shattering supplies a full adaptive tree of the same depth, proving equality.

**5. Facets and the top integral class.** A valid support leaving at least two vertices unoccupied can be extended by a diagonal query on one unused vertex, still leaving at least one unused vertex. A valid support leaving exactly one unused vertex cannot be extended: adding its diagonal would create a saturated positive-loop support, while any off-diagonal cell would conflict with a used vertex. A valid support occupying all vertices necessarily has no loops and is an oriented perfect matching; it cannot be extended. This proves the full facet characterization and the size/count formulas. At size \(n-1\), for \(n\ge3\), the only faces are the \(n\) codimension-one faces of the simplex spanned by the diagonal queries. Their boundary matrix is exactly that of a simplex boundary; it has a rank-one kernel over \(\mathbb Z\), generated by the signed sum of those facets. No higher-dimensional faces exist, so that cycle is not a boundary and \(\widetilde H_{n-2}\cong\mathbb Z\).

**6. Sharp sampling asymptotics.** Let \(Q_n(m)\) be the probability that \(m\) uniformly sampled distinct cells are all off-diagonal and use pairwise disjoint underlying vertices. For \(0\le m\le\lfloor n/2\rfloor\), conditioning successively on \(j\) disjoint oriented off-diagonal queries yields
\[
 Q_n(m)=\prod_{j=0}^{m-1}\frac{(n-2j)(n-2j-1)}{n^2-j}.
\]
Every such support is shattered. Conversely, if a shattered support is not of this form, it includes at least one diagonal cell. The probability of that event is at most \(m/n\), so the shattering probability differs from \(Q_n(m)\) by at most \(m/n\). For \(m=O(\sqrt n)\), a uniform logarithmic expansion gives \(\log Q_n(m)=-2m(m-1)/n+o(1)\), proving the displayed limit. Subcritical convergence follows from this expression. For any supercritical sequence, monotonicity of the shattering event under adding sampled coordinates bounds its probability by that of a sample of size \(\lfloor C\sqrt n\rfloor\), for every fixed \(C>0\). Sending \(n\to\infty\) and then \(C\to\infty\) proves the supercritical limit.

## Verification

The standalone `check_involution_shattering.py` independently enumerates every involution and every subset of the **ordered** query board for \(1\le n\le5\), directly compares realized Boolean traces against the proposed criterion, and independently computes all finite coefficients. It further lists all inclusion-maximal shattered supports and compares their size counts to the facet formula. The program checks every support up to size \(n\), which is sufficient because a support of greater size cannot be shattered when \(n\ge2\) (and all larger supports contain a size-\(n\) subset). The actual program output is included as `CHECK_OUTPUT.txt`. Finite checking corroborates, but does not establish, the all-parameter theorem; Steps 1–6 supply that proof.

## Relationship to prior work

Fang, Hamaker and Troyka (arXiv:2009.00079, first publicly posted August 31, 2020) develop structural pattern-containment and enumeration results for involutions and fixed-point-free involutions. Their full text gives the foundational decomposition into fixed points and two-cycles and the exponential combinatorial enumeration of these, but does not supply Boolean **ordered assignment-cell** shattering or the saturated-diagonal obstruction. Bucić, Devlin, Hendon, Horne and Lund (arXiv:1906.05908) study intersections and relative counts of permutations, derangements and perfect matchings in graphs; their theorems concern counts/ratios, not the present query-support complex. Johnson and Wickes (arXiv:2112.01946) use permutation shattering to mean realizing all relative orders on chosen labels, a different instance domain and trace condition.

The published result *Perfect-matching trace universality and the shattering polynomial of derangements* (published-finding corpus, November 2026) studies unrestricted fixed-point-free **permutations** on the off-diagonal bipartite board. Its shattered supports are partial bipartite matchings with at most \(n-2\) cells and its square-root sampling limit is \(e^{-c^2}\). This neither implies the present self-inverse/involution classification, which identifies \((i,j)\) with \((j,i)\) as logically identical responses, nor gives the role of fixed-point queries, the loop-saturation exception, facet spectrum, top integral class, or \(e^{-2c^2}\) threshold. Earlier full general permutation online bounds may be used to obtain \(\operatorname{Ldim}\le n-1\); the independent short induction above is included for completeness. The originality assessment applies to the **combined involution shattering complex and its consequences**, not to the classical enumeration of involutions, factorial counting or elementary simplex-boundary homology separately.

## Limitations

This classification requires all involutions and the complete ordered assignment board; restrictions on cycle type, parity, forbidden edges, or permitted fixed points may change it. The top-homology statement identifies only the highest reduced homology group, not the full homotopy type or all lower homology groups. The sampling limit uses uniform supports and does not describe adversarial support distributions. The proof and computations were reviewed in one research pass; no independent mathematical audit or complete historical-priority certification has occurred. Equivalent results could be indexed under looped matching complexes, symmetric permutation matrices or monomer-dimer set systems.

## References

1. J. J. Fang, Z. Hamaker, J. M. Troyka, *On pattern avoidance in matchings and involutions*, arXiv:2009.00079 (first version 2020-08-31), Electron. J. Combin. 29 (2022), P1.39. https://arxiv.org/abs/2009.00079
2. M. Bucić, P. Devlin, M. Hendon, D. Horne, B. Lund, *Perfect matchings and derangements on graphs*, arXiv:1906.05908 (first version 2019-06-13). https://arxiv.org/abs/1906.05908
3. J. R. Johnson, B. Wickes, *Shattering \(k\)-sets with Permutations*, arXiv:2112.01946 (first version 2021-12-03). https://arxiv.org/abs/2112.01946
4. *Perfect-matching trace universality and the shattering polynomial of derangements*, published-finding corpus, 2026-11-08, https://github.com/published-finding corpus/2026/blob/main/2026/11/8/SCOPE-perfect-matching-trace-universality-and-the-shattering-polynomia--d84d57a040aa/RESULT.md
