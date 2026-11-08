# Exact scalar–Hilbert Lipschitz variance on two-distance bipartite metrics

## Finding
Let \(m,n\ge2\), \(N=m+n\), and \(1\le t\le2\). Partition a uniformly weighted finite metric space \(X=A\sqcup B\), with \(|A|=m\) and \(|B|=n\), giving every cross-part pair distance \(1\) and every distinct same-part pair distance \(t\). For a real- or Hilbert-valued 1-Lipschitz function \(f\), write \(\mathcal V(f)=N^{-1}\sum_{x\in X}\|f(x)-\bar f\|^2\).

Put \(C_{a,b}=at+b(2-t)\) and \(z_{k,l}=tk+(2-t)l\), and define
\[
P_{a,b}=ab(t-1)^2+\max_{0\le k\le a,\,0\le l\le b}z_{k,l}(C_{a,b}-z_{k,l}).
\]
The sharp scalar constant is
\[
\boxed{\mathcal V_{\mathbb R}(m,n,t)=\frac{\max\{P_{m,n},P_{n,m}\}}{N^2}.}
\]
Thus the answer is an explicit finite integer-lattice maximization with at most \(2(m+1)(n+1)\) candidates, equivalently a closest-point problem for the set \(\{tk+(2-t)l\}\) around \(C_{a,b}/2\). Every scalar maximizer is, up to an additive constant and exchange of the two parts, a four-level assignment: \(k\) points of the first part at \(0\), its remaining points at \(t\), and \(l\) points of the second part at \(t-1\), its remaining points at \(1\), with a maximizing pair \((k,l)\). Degenerate level collisions are allowed at the endpoints.

For real Hilbert targets of dimension at least \(N-1\), let \(M=\max\{m,n\}\), \(q=\min\{m,n\}\), and set
\[
\alpha=\min\left\{1,\frac{M-1}{2M}t^2\right\},\quad
\beta=\min\left\{1-\alpha,\frac{q-1}{2q}t^2\right\},\quad
\gamma=1-\alpha-\beta.
\]
Then
\[
\boxed{\mathcal V_H(m,n,t)=\frac{M\alpha+q\beta}{N}+\frac{Mq}{N^2}\gamma.}
\]
Every Hilbert maximizer makes **all cross-part distances equal to one**, and maximizers exist using orthogonal centered regular simplices in the parts, with squared radii \(\alpha,\beta\), and centroid separation squared \(\gamma\). In particular there is a rank and variance phase transition at
\[
t_0=\sqrt{\frac{2mn}{2mn-m-n}},
\]
and for unequal part sizes there is a second transition at \(t_1=\sqrt{2M/(M-1)}\). Below \(t_0\), every Hilbert maximizer is an isometric copy of the whole metric, with affine rank \(N-1\); at \(t_0\) its rank drops to \(N-2\). Above \(t_1\), every maximizer collapses the smaller part to one point, while the larger part forms a centered regular simplex of squared radius one. For equal parts, the two post-\(t_0\) regimes have equal objective coefficient, so their optimizers are not restricted by the unequal-part description.

The scalar–Hilbert gap is **strict** for every \(1\le t<2\). At the graph-metric endpoint it is exactly
\[
\boxed{\mathcal V_H(m,n,2)-\mathcal V_{\mathbb R}(m,n,2)=\frac{M\bmod 2}{N^2},}
\]
where \(M\bmod 2\) means zero or one according to parity. Hence equality at \(t=2\) occurs precisely when the larger part size is even. If \(m=n=r\) is even, the formulas reduce to
\[
\mathcal V_{\mathbb R}=\frac{1+(t-1)^2}{4},\qquad
\mathcal V_H=\min\left\{\frac14+\frac{r-1}{4r}t^2,\frac12\right\}.
\]
For these balanced even classes, the gap has a **unique maximum** at \(t=\sqrt{r/(r-1)}\), of value \(t(2-t)/4\), tending to \(1/4\) as \(r\) grows through even integers.

## Assumptions and scope
All measures are uniform; all Lipschitz constants are at most one with respect to the specified metric. The domain size and distances are as above. The Hilbert conclusion holds in every real Hilbert space of dimension at least \(N-1\); the scalar optimization concerns real functions. The variance is centered and uses denominator \(N\), not an unbiased sample-variance convention. The metric triangle inequalities hold precisely in the stated range. The phrase 'all maximizers' is understood modulo addition of a common constant and Hilbert rigid motions.

## Proof
**Scalar extremizers.** After fixing one function value, the set of real 1-Lipschitz functions is a compact polytope. Its variance, written as \(N^{-2}\sum_{x<y}(f(x)-f(y))^2\), is strictly convex modulo constants; hence every maximizer is an extreme point. The standard tight-edge criterion says that an extreme point is exactly a feasible function whose graph of pairs satisfying \(|f(x)-f(y)|=d(x,y)\) is connected. Indeed, connected tight edges fix every difference under a convex decomposition; if the tight graph is disconnected, a sufficiently small shift of one component makes a nontrivial convex decomposition.

For \(1<t<2\), if the first part has a tight within-part pair, translate its minimum to zero, and its maximum is \(t\). Every value of the other part belongs to \([t-1,1]\). Any first-part value strictly between \(0\) and \(t\), or second-part value strictly between \(t-1\) and \(1\), would have no tight edge; thus connectivity forces the four specified levels, with both extreme first-part levels represented. The same argument applies with the parts reversed. If neither part has a tight within-part pair, connected tight paths use only cross edges of increment \(\pm1\). Two points in the same part are linked by an even path; their difference is therefore an even integer, whose absolute value is strictly less than \(2\), forcing equality. Thus each part is constant and their values differ by one; this is also included in the four-level families at a degenerate choice of counts. At \(t=1\) every extreme point is a two-level equilateral potential, included in the same families. At \(t=2\), the same connectivity argument yields the stated four-level families with any internal intermediate level excluded, or the two constant parts. This **vertex classification was already established in the published polyhedral work cited below**; it is reused, not independently claimed as a new vertex theorem.

For an assignment with \(k\) first-part zeros and \(l\) second-part values \(t-1\), direct expansion of the pairwise-difference sum gives
\[
N^2\mathcal V=ab(t-1)^2+z_{k,l}(C_{a,b}-z_{k,l}).
\]
Taking the maximum over the two possible orientations and finite integer counts proves the scalar formula and equality description.

**Hilbert optimization.** For any Hilbert-valued map, let \(u\) and \(v\) denote the means over the two parts, and let \(a\), \(b\) be their respective mean squared centered radii; put \(c=\|u-v\|^2\). Summing the squared within-part distances yields
\[
0\le a\le\frac{m-1}{2m}t^2,\quad 0\le b\le\frac{n-1}{2n}t^2.
\]
The exact average of squared cross-part distances is \(a+b+c\), so \(a+b+c\le1\). The total centered variance decomposes as
\[
\mathcal V=\frac{ma+nb}{N}+\frac{mn}{N^2}c.
\]
Its three coefficients are strictly ordered for \(m>n\): \(m/N>n/N>mn/N^2\). Consequently the linear-program maximum first fills the larger part's radius to \(\min\{1,(m-1)t^2/(2m)\}\), then the smaller part's radius to \(\min\{1-a,(n-1)t^2/(2n)\}\), and assigns any remainder to \(c\). When \(m=n\), the two radius coefficients tie and any optimal split between their caps gives the same value; the stated greedy split is one maximizer. This proves the claimed bound.

The bound is attained in Euclidean space by a centered regular simplex of \(m\) vertices of common squared norm \(a\) and a centered regular simplex of \(n\) vertices of common squared norm \(b\) in orthogonal subspaces, with their centers separated in a third perpendicular direction by squared distance \(c=1-a-b\). Their within-part squared pair distances are \(2ma/(m-1)\le t^2\) and \(2nb/(n-1)\le t^2\); all squared cross distances equal \(a+b+c=1\). This construction requires at most \(N-1\) dimensions. Any Hilbert maximizer must have \(a+b+c=1\), for otherwise its centroid-distance variable could be increased and the variance would strictly increase; since the average squared cross distance is one and each such distance is at most one, **every** cross distance must equal one.

The first threshold is the equality \((m-1)t^2/(2m)+(n-1)t^2/(2n)=1\), giving \(t_0\). Below it, equality forces both within-part squared means to saturate their caps, hence every within-part pair distance equals \(t\) and every cross distance equals one: the embedding is isometric. The centered Gram matrix of an exact finite distance matrix is uniquely determined by double centering; the explicit simplex construction has affine rank \(N-1\) if \(c>0\), and \(N-2\) if \(c=0\). For \(m>n\), above \(t_0\), the larger radius remains at cap until it reaches one at \(t_1\), where the smaller radius and separation vanish. Above \(t_1\) the smaller part collapses. This proves the phase and rigidity assertions, with equal-part coefficient ties handled as stated.

**Gap and balanced case.** For \(t<2\), a scalar function with all cross distances equal to one must be constant on both parts: for each fixed point on one side, values on the other would otherwise differ by two, violating its within-part bound \(t<2\). Its variance would then be \(mn/N^2\); the displayed Hilbert optimum is strictly larger because the nonzero within-part radii have objective coefficient greater than that for centroid separation. Thus no scalar optimizer can reach the Hilbert optimum. At \(t=2\), the Hilbert formula reduces to \(M/N\). The scalar lattice formula reduces to \(M/N-(M\bmod2)/N^2\) (the optimal two-point split in the larger part has sizes as balanced as parity permits), yielding the endpoint difference. For \(m=n=r\) even, the lattice center is attained by \(k=l=r/2\), so \(\mathcal V_{\mathbb R}= [1+(t-1)^2]/4\). The Hilbert formula simplifies as displayed; differentiating the two branchwise gap formulas shows strict increase until \(t=\sqrt{r/(r-1)}\) and strict decrease thereafter, giving the unique maximum and limit. \(\square\)

## Verification
The accompanying standard-library Python program independently reconstructs real Lipschitz-polytope vertices by signed tight-constraint intersection with exact rational arithmetic, compares the scalar formula for two small part-size pairs, and checks the Hilbert linear program by enumeration of its boundary intersections. It additionally tests exact parity and balanced even formulas over several parameter sets. Running `python bipartite_variance_checker.py` prints `ALL_BIPARTITE_VARIANCE_DIAGNOSTICS_PASSED`. These finite diagnostics corroborate, but do not establish, the universal formulas, whose proof above is analytical.

## Relationship to prior work
Addario-Berry, Janson and McDiarmid (2009) use the scalar Lipschitz spread invariant in random graph theory, but the inspected discussion is not this sharp two-distance, scalar-versus-Hilbert optimization. The published result *Sharp facet-count transitions for snowflaked complete bipartite metrics* gives the relevant four-level real Lipschitz-polytope vertex classification: hence that classification is credited, not claimed new. Its facet counts do not give the new Hilbert sharp variance, dimension-collapse regimes, or the sharp scalar–Hilbert comparison. Robertson (2023, Section 4.1) establishes the underlying negative-type/isometric Hilbert embedding threshold for complete bipartite graph snowflakes; the threshold by itself is known and is not claimed as new. The present theorem determines the maximum **one-sided Lipschitz variance beyond the isometry threshold**, the second transition for unequal parts, and a scalar comparison with sharp parity and balanced-even maximum. A previous complete-multipartite graph-spread result already gives the scalar endpoint at \(t=2\), which is explicitly credited as covered; the new continuum curve and Hilbert comparison do not follow from that endpoint alone.

## Limitations
The formulas concern only uniform measures, two-part complete-bipartite distance families with \(1\le t\le2\), real scalar maps, and real Hilbert maps with sufficient target dimension. The Hilbert theorem does not determine restricted small-dimensional optimal variances away from the isometric regime. Part sizes one, arbitrary complete multipartite metrics, nonuniform measures and Banach targets are not addressed. The vertex classification, the known isometric Hilbert threshold and the \(t=2\) scalar endpoint are credited prior knowledge, not independent novelty claims. An equivalent complete variance-phase result in incompletely indexed literature is a residual bibliographic risk.

## References
1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1, first publicly posted 2009-02-06, https://arxiv.org/abs/0902.1156.
2. *Sharp facet-count transitions for snowflaked complete bipartite metrics* (2026), publicly posted mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-facet-count-transitions-for-snowflaked-complete-bipartite--e855a74da4ce.
3. G. Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space*, arXiv:2309.16070v1 (2023-09-27), especially Section 4.1, https://arxiv.org/abs/2309.16070.
4. *Complete multipartite graph-metric scalar spread* (previously established result for the endpoint; not reproduced here).
