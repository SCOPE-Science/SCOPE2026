# Partition discrepancy governs sharp Lipschitz variance on clique windmills

## Finding

Let \(r\ge 2\), let \(s_1,\ldots,s_r\) be positive integers, and let \(W(\mathbf s)\) consist of cliques of orders \(s_i+1\) all sharing exactly one common hub, with no other inter-clique edges. Give each edge length one and each vertex equal probability. Write
\[
S=\sum_{i=1}^r s_i,\qquad N=S+1,\qquad
D=\min_{\varepsilon_i\in\{-1,1\}}\left|\sum_{i=1}^r\varepsilon_i s_i\right|.
\]
For the centered inclusion from real one-Lipschitz functions modulo constants into \(L^2\) of uniform vertex measure, the exact *squared* operator norm is
\[
\boxed{\operatorname{spr}(W(\mathbf s))=
\frac{N(N-1)-D^2+\left\lfloor ((2D-N)_+)^2/4\right\rfloor}{N^2}.}
\]
Here \((t)_+=\max\{0,t\}\), and \(\operatorname{spr}\) is the maximum variance. Every maximizing function is described explicitly below. In particular,
\[
\operatorname{spr}(W(\mathbf s))=\frac{N-1}{N}\quad\Longleftrightarrow\quad D=0.
\]
A partially zeroed blade can occur in a maximizer only when one blade dominates the outer vertex count: if \(m=\max_i s_i\), the necessary and sufficient condition for the existence of a maximizing configuration with at least one nonhub zero is
\[
\boxed{2D-N\ge1\quad\Longleftrightarrow\quad m>(3N-2)/4.}
\]
There is a strict improvement over the fully polarized configuration precisely when \(2D-N\ge2\).

The equality question for \(\operatorname{spr}=(N-1)/N\), with \(\mathbf s\) encoded in binary, is NP-complete by an exact reduction from PARTITION. This is a statement about succinct size-vector encoding, **not** about an explicitly listed adjacency matrix.

## Assumptions and scope

Every \(s_i\) is a positive integer, \(r\ge2\), and the graph is the vertex union of the indicated cliques, meeting only in the hub. The metric is shortest-path distance for unit-length edges. All functions are real, and vertex probability is uniform. An input function is one-Lipschitz if \(|f(u)-f(v)|\le1\) for each edge. Translating a function does not change its variance, and we anchor the hub at value zero. We use
\[
\operatorname{Var}(f)=N^{-1}\sum_{v} f(v)^2-\left(N^{-1}\sum_v f(v)\right)^2.
\]
The squared embedding norm equals this maximum because scaling reduces every nonconstant Lipschitz function to Lipschitz norm one.

## Proof

**1. The only possible extremal blade profiles.** With the hub anchored at zero, the feasible Lipschitz polytope is compact, and its variance is strictly convex: for every nonzero anchored perturbation \(g\), \(\operatorname{Var}(g)>0\) because the fixed hub has value zero. Consequently every maximizer is a vertex of the polytope. The polytope is the Cartesian product of its individual blade polytopes. Within one blade, form the tight-edge subgraph consisting of edges \(uv\) with \(|f(u)-f(v)|=1\). If it does not connect every leaf to the hub, an unanchored tight component can be shifted by sufficiently small positive and negative amounts while respecting all inequalities. The original function would be the midpoint of two feasible distinct functions, impossible at a vertex. Thus each leaf is joined to the hub along a path of tight edges. Every leaf value is an integer, and the hub constraint forces it into \(\{-1,0,1\}\). A clique forbids simultaneously \(+1\) and \(-1\) among its leaves. Hence every maximizing blade consists of \(k_i\) entries equal to either \(+1\) or \(-1\), with the remaining leaves zero, where \(0\le k_i\le s_i\).

**2. Fix a partition of blade signs.** Assign each blade a putative positive or negative sign, including arbitrary choices for blades with zero nonhub entries. Let \(P\) and \(L\) be the total leaf capacities on the two signs, chosen with \(P\ge L\); thus \(P+L=S\) and \(\Delta=P-L\ge0\). All integer numbers \(0\le k\le P\) of positive leaves and \(0\le l\le L\) of negative leaves are realizable by filling the blades in that sign class. The variance is exactly
\[
F(k,l)=\frac{k+l}{N}-\frac{(k-l)^2}{N^2}.
\]
At its maximum the negative/minority sign capacity is saturated, \(l=L\). Indeed, whenever \(k<l\), increasing \(k\) by one strictly increases \(F\), and is feasible because \(P\ge L\); whenever \(k\ge l\) and \(l<L\), increasing \(l\) by one strictly increases \(F\). Repeating these moves, and increasing both counts together when needed, reaches \(l=L\). With \(l=L\), increasing \(k\) is beneficial until \(k\ge L\), and the remaining strictly concave quadratic has real maximum at \(k=L+N/2\).

Set \(h=P-k\), the number of positive-side leaves changed from \(+1\) to zero. Relative to the fully polarized assignment, an exact calculation gives
\[
F(P-h,L)-F(P,L)=\frac{h(2\Delta-N-h)}{N^2}.
\]
Therefore the maximizing integer \(h\ge0\) is zero if \(2\Delta-N\le0\), and otherwise is any nonnegative integer nearest \((2\Delta-N)/2\). The upper constraint \(h\le P\) is inactive because \(2\Delta-N<2P\). Consequently the maximum for fixed sign partition is
\[
F_*(\Delta)=\frac{N(N-1)-\Delta^2+\lfloor((2\Delta-N)_+)^2/4\rfloor}{N^2}.
\]

**3. Partition discrepancy chooses the signs.** The integer numerator \(N^2F_*(\Delta)\) is strictly decreasing in nonnegative integer \(\Delta\). For \(2\Delta\le N\) it equals \(N(N-1)-\Delta^2\). For \(2\Delta\ge N\) it equals \(N(N-1)-N\Delta+\lfloor N^2/4\rfloor\). Both pieces strictly decrease, with consistent values at the transition (and strict decrease across the adjacent integer transition when \(N\) is odd). As every sign partition has discrepancy at least \(D\), the maximum is obtained exactly by partitions with discrepancy \(D\). Substitution proves the boxed formula.

**4. Every maximizer and the dominant-blade transition.** Every maximizing function, modulo addition of a constant, has hub value zero. Choose a sign partition attaining \(D\), relabel its larger-capacity side positive, and put \(-1\) on *all* leaves of the smaller side. Put \(+1\) on all except \(h\) leaves of the larger side; put zero on precisely those \(h\) leaves. Here \(h\) maximizes \(h(2D-N-h)\) among nonnegative integers: \(h=0\) if \(2D-N\le0\), both \(h=0,1\) if \(2D-N=1\), and the integer(s) nearest \((2D-N)/2\) if \(2D-N\ge2\). The choices of the \(h\) leaves are arbitrary, and reversing every sign gives the remaining extremizers. Every such assignment is one-Lipschitz and attains the optimum; Steps 1–3 exclude every other maximizing function.

If \(D>N/2\), then some blade must contain more than half the leaves: otherwise a greedy balancing of the integer blade sizes yields a sign partition with discrepancy at most the largest size \(m\le S/2<N/2\). In that dominant-blade case the unique minimum-discrepancy partition, up to global sign, isolates the largest blade and puts all the other blades opposite. Thus \(D=2m-S\) and \(2D-N>0\) is equivalent to \(m>(3N-2)/4\). All nonhub zeros in the above maximizers then lie in this uniquely dominant blade. The tie and strict-improvement criteria follow from the maximizing quadratic in \(h\).

**5. Binary-encoded complexity.** The universally valid upper bound \(\operatorname{Var}(f)\le S/N\) follows from the above extremal form, since \(\sum_v f(v)^2\le S\) and \(\operatorname{Var}(f)\le N^{-1}\sum_v f(v)^2\). Equality holds exactly when every leaf has magnitude one and their signed sum is zero, which is precisely \(D=0\). Given an instance of PARTITION with positive binary integers \(s_i\), form the same succinct windmill size vector. The equality predicate has a polynomially checkable sign-partition certificate and is equivalent to PARTITION, proving NP-completeness of that succinct predicate. No claim of NP-hardness for explicit-vertex input is made.

## Verification

The accompanying standard-library program `check.py` computes the discrepancy by signed-sum dynamic programming, evaluates the formula with exact rational arithmetic, independently enumerates every anchored integer-valued feasible leaf assignment in small graphs, and compares its exact maximum against the formula. It also independently enumerates signed capacities for larger small parameter tuples, checks every two-blade size pair up to 99, and tests strict monotonicity of the discrepancy envelope for dimensions up to 399. Run `python check.py` from the directory containing this document. These finite checks corroborate but do not replace the proof for all positive integer size vectors.

## Relationship to prior work

Alon, Boppana and Spencer introduced the maximum-variance spread of a finite metric space and proved the general integer extremizer structure; their structural theorem by itself does not compute the sharp constant of a heterogeneous clique windmill. Addario-Berry, Janson and McDiarmid explain its concentration role and compute complete-graph and path benchmarks, while studying random-graph families rather than the present clique-sum/partition-discrepancy law. Yancey's analysis of variance- and subgaussian-optimal Lipschitz functions covers other graph structures and does not provide the stated windmill optimization.

The nearest separately indexed results on generalized windmills concern dissociation polynomials, not Lipschitz variance. The available preceding bridge-connected two-clique spread result treats two *disjoint* cliques connected by an edge, not arbitrary cliques identified at one vertex; neither its graph nor its expression implies the present all-size-vector discrepancy theorem. Literature equivalence outside the inspected sources cannot be excluded.

## Limitations

Only unit-edge graphs whose maximal cliques all meet at one hub, uniform vertex probabilities, and real Lipschitz variance are covered. The formula is not a universal result for all block graphs, weighted probabilities, arbitrary clique-attachment trees, or the spread of explicit adjacency matrices under succinct complexity assumptions. The NP-completeness statement applies **only** when blade sizes are input in binary; the dynamic-programming algorithm is pseudopolynomial in their total sum. Independent mathematical validation has not been performed.

## References

1. N. Alon, R. Boppana and J. Spencer, *An Asymptotic Isoperimetric Inequality* (1998), https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf, especially §2.
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (first posted 2009-02-06), https://arxiv.org/abs/0902.1156, §1.1.
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725 (2017), https://arxiv.org/abs/1705.09725, §§1–2.
