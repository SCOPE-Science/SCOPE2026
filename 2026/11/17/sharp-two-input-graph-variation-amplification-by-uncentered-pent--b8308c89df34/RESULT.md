# Sharp two-input graph-variation amplification by uncentered pentagonal maximal averaging

## Finding

Let \(C_5\) be the simple unweighted cycle on \(V=\mathbb Z/5\mathbb Z\), with edges joining consecutive residues. For nonnegative real functions \(f\in[0,\infty)^V\), define the **uncentered graph-ball maximal average**

\[
(\widetilde M f)(i)=\max_{\substack{c\in V,\ r\in\{0,1,2\}\\ i\in B(c,r)}}\frac{1}{|B(c,r)|}\sum_{j\in B(c,r)}f(j),
\quad B(c,r)=\{j:d_{C_5}(j,c)\le r\}.
\]

For a real function \(h\), set \(\operatorname{TV}(h)=\sum_{i\in V}|h(i)-h(i+1)|\). Then the exact **two-input** graph-variation Lipschitz coefficient is

\[
\boxed{\sup_{\substack{f,g\in[0,\infty)^V\\\operatorname{TV}(f-g)>0}}
\frac{\operatorname{TV}(\widetilde M f-\widetilde M g)}{\operatorname{TV}(f-g)}=\frac75.}
\]

The bound is **attained** by the nonnegative pair

\[
f=(0,3,4,1,4),\qquad g=f+\frac1{100}(0,0,1,1,0).
\]

Thus uncentered graph-ball maximal averaging is expansive for **differences** in edge variation on the smallest noncomplete odd cycle. This is distinct from estimates comparing the variation of one maximal output with the variation of that same input.

## Assumptions and scope

Vertices have counting measure and unit graph distances. Only metric **balls** may be used in the maximum, not arbitrary connected arcs or intervals: each evaluation vertex has precisely five eligible sets, namely its singleton, the three closed radius-one balls containing it, and the full five-vertex ball. The inputs are nonnegative, as in the usual maximal operator with absolute input values. The variation seminorm is evaluated on their possibly signed difference. A zero-variation difference is constant; translation equivariance gives a constant output difference as well.

## Proof

**1. Exact linear-branch reduction.** At each evaluation vertex choose one of the five eligible ball-average rows. Any such independent choice defines a nonnegative row-stochastic \(5\times5\) matrix \(A\). The map \(\widetilde M\) is coordinatewise the maximum of finitely many linear averages, hence is continuous and piecewise linear. Along the segment between any two nonnegative inputs, the derivative of \(\widetilde M\) exists except at finitely many switching parameters and equals \(A\) applied to the segment direction for one of these row selections. It therefore suffices to prove

\[
\operatorname{TV}(Ah)\le\frac75\operatorname{TV}(h)
\quad\text{for every row selection \(A\) and every real \(h\).}
\]

The integration step uses convexity and the triangle inequality of \(\operatorname{TV}\): applying this bound to every constant-branch segment and summing gives the corresponding nonlinear two-input inequality. Ties and endpoints are handled by continuity.

**2. Cut reduction for a constant-preserving matrix.** Every such \(A\) satisfies \(A\mathbf1=\mathbf1\). Write any \(h\) as a constant plus a positive integral of superlevel-cut indicators. The discrete coarea identity gives

\[
\operatorname{TV}(h)=\int\operatorname{TV}(\mathbf1_{\{h>t\}})\,dt.
\]

Applying \(A\), using \(A\mathbf1=\mathbf1\), and invoking the triangle inequality shows

\[
\frac{\operatorname{TV}(Ah)}{\operatorname{TV}(h)}
\le\max_{\varnothing\ne S\subsetneq V}
\frac{\operatorname{TV}(A\mathbf1_S)}{\operatorname{TV}(\mathbf1_S)}.
\]

The reverse inequality for the operator norm follows by substituting a maximizing cut indicator, so this is an exact cut reduction for each fixed \(A\).

**3. Sharp universal row-choice envelope.** For each cut \(S\), the five coordinates of \(A\mathbf1_S\) are **independently** selected from the eligible averages. Write \(\ell_i\) and \(u_i\) for the smallest and largest possible averages at vertex \(i\). Because total variation is convex in the output vector, its maximum on the rectangular box \(\prod_i[\ell_i,u_i]\) occurs at one of its \(2^5\) endpoint vectors. Dihedral symmetry and complementation \(S\leftrightarrow V\setminus S\) reduce the thirty nontrivial cuts to three representatives. The following values are calculated by exact rational evaluation of those thirty-two endpoint vectors in each row:

| Representative cut indicator | Coordinate ranges \([\ell_i,u_i]\) in cyclic order | Maximum output variation | Input variation | Ratio |
| --- | --- | ---: | ---: | ---: |
| \((1,0,0,0,0)\) | \([1/5,1],[0,1/3],[0,1/3],[0,1/3],[0,1/3]\) | \(8/3\) | \(2\) | \(4/3\) |
| \((1,1,0,0,0)\) | \([1/3,1],[1/3,1],[0,2/3],[0,2/5],[0,2/3]\) | \(14/5\) | \(2\) | \(7/5\) |
| \((1,0,1,0,0)\) | \([1/3,1],[0,2/3],[1/3,1],[0,2/5],[0,2/5]\) | \(4\) | \(4\) | \(1\) |

These finite maxima can be checked by the attached self-contained, exact-fraction checker; it also independently evaluates every cut for **all \(5^5=3125\) row-choice matrices**. The box method is a valid upper bound even when a selected combination of rows could not occur as a single nonlinear branch. The largest quotient in the table is \(7/5\), proving the universal bound.

**4. Exact attainment by a genuine nonlinear branch.** Let \(f=(0,3,4,1,4)\), \(v=(0,0,1,1,0)\), and \(g=f+v/100\). For **both** inputs, the uniquely active averaging sets at vertices \(0,1,2,3,4\) are, respectively,

\[
V,\quad\{1\},\quad\{2\},\quad\{2,3,4\},\quad\{4\}.
\]

Hence

\[
\widetilde Mf=(12/5,3,4,3,4),\qquad
\widetilde Mg=(601/250,3,401/100,451/150,4).
\]

Subtracting these outputs gives \((1/250,0,1/100,1/150,0)\), whose graph variation is \(7/250\). The input difference has variation \(1/50\). The quotient is therefore \((7/250)/(1/50)=7/5\). This is an exact finite pair, not a limiting or merely infinitesimal witness.

## Verification

Run `python3 check_c5_two_input_variation.py` with a standard Python 3 interpreter and no third-party packages. The program reconstructs all graph metric balls, verifies the complete three-orbit box table with \(96\) exact rational endpoint evaluations, independently checks all \(93,750\) matrix/cut combinations, and verifies the strict active-ball choices and output values of the explicit pair. Its complete success marker is `ALL_C5_UNCENTERED_BV_STABILITY_CHECKS_PASSED`. The analytical coarea and piecewise-affine integration steps prove the universal inequality; the finite exact checks resolve the bounded arithmetic cases.

## Relationship to prior work

Bober–Carneiro–Hughes–Pierce [1] prove one-input variation contraction for the uncentered discrete maximal function on the **infinite line**, rather than two-input difference stability on a finite cycle. Aldaz–Colzani–Pérez Lázaro [2] determine *spatial* moduli of continuity of a maximal output in terms of its input; those are not seminorm Lipschitz estimates **between two inputs**. Madrid [3] establishes sharp one-input derivative/variation estimates for discrete lattice maximal functions. González-Riquelme–Kovač–Madrid [4] study *centered*, one-input graph variation and a census of small graphs; it is not the present uncentered two-input problem. A separate finite five-cycle uncentered result [5] finds a sharp **strong \(\ell^2\) input-to-output norm and its extremizers**, not the edge-variation perturbation modulus. The published finite-path morphology result [6] studies sliding **minimum/maximum coordinate selectors**, rather than maxima of **ball averages**. These implication comparisons do not establish historical uniqueness; unindexed or equivalent work may exist.

## Limitations

The exact coefficient concerns nonnegative real signals and graph-metric balls on the unit five-cycle only. For arbitrary signed inputs with the conventional absolute-value maximal operator, translation equivariance fails and a variation-of-differences seminorm inequality need not be finite. No claim is made for longer cycles, vertex weights, graph intervals that are not balls, other variation exponents, or an arbitrary graph. The coefficient is a fixed-graph finite invariant, not an infinite-family asymptotic. Independent external validation and publication-priority review have not been performed.

## References

[1] J. Bober, E. Carneiro, K. Hughes and L. B. Pierce, *On a discrete version of Tanaka's theorem for maximal functions*, arXiv:1005.3030, first publicly posted 2010-05-17, https://arxiv.org/abs/1005.3030.

[2] J. M. Aldaz, L. Colzani and J. Pérez Lázaro, *Optimal bounds on the modulus of continuity of the uncentered Hardy-Littlewood maximal function*, arXiv:1009.1359, 2010-09-07, https://arxiv.org/abs/1009.1359.

[3] J. Madrid, *Sharp inequalities for the variation of the discrete maximal function*, arXiv:1512.04112v1, 2015-12-13, https://arxiv.org/html/1512.04112v1.

[4] C. González-Riquelme, V. Kovač and J. Madrid, *Sharp variational inequalities for the Hardy-Littlewood maximal operator on finite undirected graphs*, arXiv:2603.12462, 2026-03-12, https://arxiv.org/abs/2603.12462.

[5] *Exact uncentered Hilbert maximal norm on the five-cycle*, research record, 2026-11-02, publicly available with a complete scientific result in the published-finding corpus mathematical research repository.

[6] *Finite-window morphology: sharp two-input variation and a boundary-weight transition*, research record, 2026-11-01, publicly available with a complete scientific result in the published-finding corpus mathematical research repository.
