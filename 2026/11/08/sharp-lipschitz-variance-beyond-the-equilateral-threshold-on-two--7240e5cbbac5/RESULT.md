# Sharp Lipschitz variance beyond the equilateral threshold on two-cluster metrics

## Finding

For integers \(m,n\ge2\) and a real number \(1<s<2\), partition a finite metric space \(X=A\sqcup B\) into parts of cardinalities \(m,n\). The distance between distinct points in the same part is \(s\); every cross-part distance is \(1\). Let \(N=m+n\). For a real function \(f\) let \(\bar f=N^{-1}\sum_{x\in X}f(x)\), and define its sharp Lipschitz variance
\[
V_{m,n}(s)=\max_{\operatorname{Lip}(f)\le1}\frac1N\sum_{x\in X}(f(x)-\bar f)^2.
\]
For positive integers \(a,b\) with \(a+b=N\), define the two-integer discrepancy
\[
\Delta_{a,b}(s)=\min_{\substack{k\in\{0,\ldots,a\}\\\ell\in\{0,\ldots,b\}}}\left|sk+(2-s)\ell+b(s-1)-\frac{Ns}{2}\right|,
\]
and put
\[
\Phi_{a,b}(s)=\frac{s^2}{4}-\frac{b(s-1)}N-\frac{\Delta_{a,b}(s)^2}{N^2}.
\]
Then the sharp, attained value is
\[
\boxed{V_{m,n}(s)=\max\{\Phi_{m,n}(s),\Phi_{n,m}(s)\}.}
\]
Every maximizing function, up to a common additive constant, a global sign reversal, and permutations within the parts, has the following form for at least one winning orientation \((a,b)=(m,n)\) or \((n,m)\): in the \(a\)-point part, exactly \(k\) values equal \(s\) and the remaining \(a-k\) equal \(0\); in the \(b\)-point part, exactly \(\ell\) values equal \(1\) and the remaining \(b-\ell\) equal \(s-1\). The pair \((k,\ell)\) must realize \(\Delta_{a,b}(s)\) in a winning orientation, and every such configuration is maximizing. Thus the theorem classifies *all* maximizers, not just one witness.

There is a particularly simple universal law at the arithmetic midpoint \(s=3/2\):
\[
\boxed{V_{m,n}(3/2)=\frac9{16}-\frac{\min\{m,n\}}{2N}-\frac{\mathbf1_{\{N\ \mathrm{odd}\}}}{16N^2}.}
\]
The two endpoints of the metric interpolation are determined by continuity:
\[
V_{m,n}(1)=\frac{\lfloor N^2/4\rfloor}{N^2},\qquad
V_{m,n}(2)=\frac{H}{N}-\frac{\mathbf1_{\{H\ \mathrm{odd}\}}}{N^2},\quad H=\max\{m,n\}.
\]
The optimizer classification above is asserted only for the open interval \(1<s<2\); new degeneracies occur at its endpoints.

## Assumptions and scope

The metric is well-defined because \(s\le2\), and the measure is uniform on all \(N\) points. Functions are real-valued, and \(\operatorname{Lip}(f)\le1\) means \(|f(x)-f(y)|\le d(x,y)\) for every pair. Translation invariance removes one coordinate and leaves a compact convex Lipschitz polytope. The objective is *probability-normalized variance*, not the unnormalized sum of squares. No restriction to integral or rational \(s\) is imposed in the proof.

## Proof

**1. A connected-tight-graph criterion.** Pin one function value to zero. Every boundary inequality of the Lipschitz polytope is of the form \(|f(x)-f(y)|\le d(x,y)\). A feasible potential is a vertex if and only if the undirected graph of pairs with equality is connected. Indeed, the active normals are signed incidence vectors \(e_x-e_y\), whose rank modulo constants is \(N-c\), where \(c\) is the number of connected components of the active graph. In particular, the active graph of a vertex contains a spanning tree. The centered variance is a strictly convex positive-definite quadratic form on the quotient by constants. Hence **every** maximizer is a vertex: a nonvertex can be expressed as a nontrivial convex combination and strict convexity makes its variance smaller than the larger endpoint variance.

**2. Classify the vertices sufficient for maximization.** Suppose the tight graph of a vertex contains no edge within either part. Then its spanning paths use cross-part tight pairs of distance \(1\). Along any even path between two vertices of the same part, the difference of values is an even integer. Since their allowed separation is strictly below \(2\), they have equal values. Thus each entire part is constant, and the connected tight graph forces a cross-part difference exactly \(1\). This is a two-level special case of the proposed configurations.

Otherwise some tight pair lies, say, in the part with \(a\) points. Subtract its smaller value, so the minimum over this part is \(0\) and its maximum is \(s\). (The diameter bound assures these are the exact partwise minimum and maximum.) Every value in the other part lies in the intersection of the distance-one intervals around \(0\) and \(s\), namely \([s-1,1]\). As \(1<s<2\), this other part has width at most \(2-s<s\), so no within-part pair there is tight. Every vertex in the spanning part with value strictly between \(0\) and \(s\) has no tight within-part or cross-part edge: a cross-part value would need to be \(f(x)+1>1\) or \(f(x)-1<s-1\), both impossible. Therefore all values in the spanning part are \(0\) or \(s\). Similarly, any vertex in the other part with a value strictly between \(s-1\) and \(1\) would have no tight edge, so all its values belong to \(\{s-1,1\}\). Both parts cannot have an internal tight pair because the second has width \(2-s<s\). Interchanging the parts covers the remaining case.

This proves that **every** maximizer is one of the stated two-integer configurations. Conversely, *every* stated configuration is feasible: within-part differences are at most \(s\), and each of \(0,s\) differs by at most \(1\) from each of \(s-1,1\). We may therefore optimize over these configurations even if a degenerate count choice does not give a vertex.

**3. Exact variance completion.** For an \((a,b,k,\ell)\)-configuration, the sum of values and their squared sum are
\[
S=sk+b(s-1)+(2-s)\ell,\qquad
Q=s^2k+(b-\ell)(s-1)^2+\ell.
\]
The elementary identity \(Q=sS-b(s-1)\) gives
\[
\frac QN-\frac{S^2}{N^2}
=\frac{s^2}4-\frac{b(s-1)}N-\frac{(S-Ns/2)^2}{N^2}.
\]
Minimizing the last square over the complete integer rectangle produces \(\Phi_{a,b}(s)\); maximizing over the two orientations gives exactly the displayed value. Strict convexity and this equality also give all equality cases, subject to translation, reflection and permutations. The pair \((k,\ell)\) can be located with \(a+1\) nearest-integer tests: for each fixed \(k\), choose \(\ell\) nearest to \((Ns/2-b(s-1)-sk)/(2-s)\), clipped to the integer interval \([0,b]\), checking both neighbors in a tie. Thus the formula is effectively evaluable in \(O(N)\) arithmetic operations rather than a search through exponentially many potentials.

**4. Arithmetic midpoint.** For \(s=3/2\),
\[
S-\frac{3N}4=\frac12\left(3k+\ell-\frac{3a+b}{2}\right).
\]
The integer intervals \(\{3k,3k+1,\ldots,3k+b\}\), as \(k\) ranges over \(0,\ldots,a\), cover **every integer** from \(0\) to \(3a+b\) because \(b\ge2\) leaves no gap between consecutive intervals. Hence the minimum absolute difference from \((3a+b)/2\) is \(0\) if \(a+b\) is even and \(1/2\) if it is odd. Therefore \(\Delta_{a,b}(3/2)=0\) or \(1/4\) according to the parity of \(N\), independently of the orientation. The branch with smaller \(b\) has the larger value, proving the universal midpoint formula.

**5. Boundary checks.** As \(s\downarrow1\), every proposed configuration becomes a two-level \(0,1\) partition. Its maximal variance is \(\lfloor N^2/4\rfloor/N^2\). As \(s\uparrow2\), the discrepancy in orientation \((a,b)\) reduces to \(\min_{0\le k\le a}|2k-a|=\mathbf1_{\{a\ \mathrm{odd}\}}\), so the branch is \(a/N-\mathbf1_{\{a\ \mathrm{odd}\}}/N^2\). This is maximized by \(a=H\) because increasing \(a\) by at least one gives a larger first term than any parity correction. The formula extends continuously to both endpoints, proving the stated endpoint values without asserting the same equality classification there.

## Verification

The accompanying standard-library Python program `verify_two_cluster_metric.py` independently enumerates every spanning tree through Pruefer sequences and every choice of tight-edge signs for all tested spaces of total cardinality at most six. It checks feasibility and computes variance in exact rational arithmetic, then compares the exhaustive extreme-point optimum with the two-integer formula for 18 combinations of part sizes and metric lengths. Further exact-rational comparisons verify the midpoint formula on 1,089 pairs of part sizes and the two endpoint laws on 529 pairs. These tests are finite corroboration; the universal assertion follows from the preceding analytic proof.

## Relationship to prior work

Alon, Boppana and Spencer (1998) introduced Lipschitz spread and its relation to metric isoperimetry; Addario-Berry, Janson and McDiarmid (arXiv first posted February 6, 2009) analyze the invariant for random graphs and include a separate lemma on random edge lengths in complete bipartite graphs. That lemma does **not** solve the deterministic two-cluster metric variance optimization: its subject is existence of a sparse edge selection with probabilistic length tails. Existing literature on the dual Lipschitz polytope for snowflaked complete bipartite metrics determines facet counts and classifies some extreme potentials; counting facets by itself does **not** evaluate the centered quadratic form on them. The present theorem supplies the exact variance and optimizer counts in the previously untreated interval \(1<s<2\), together with the closed midpoint law. The different regime \(0<s\le1\) has a distinct, one-integer formula and is not claimed here. An equivalent formula in less readily indexed work is not ruled out.

## Limitations

The theorem requires two homogeneous classes of size at least two, equal within-class distance \(s\), fixed cross-class distance one and uniform weights. It does not classify unequal within-class radii, nonuniform measures, more than two classes or all higher moments. The general sharp value is expressed by a bounded two-integer discrepancy, not as a single piecewise polynomial valid without arithmetic cases; the midpoint and endpoints do admit closed expressions. Independent review and exhaustive literature coverage remain outstanding.

## References

1. N. Alon, R. Boppana and J. Spencer, *An asymptotic isoperimetric inequality*, Geometric and Functional Analysis 8 (1998), 411–436, DOI 10.1007/s000390050062.
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first posted February 6, 2009; later Combinatorics, Probability and Computing 23 (2014), 477–504, DOI 10.1017/S0963548314000248.
3. *Sharp facet-count transitions for snowflaked complete bipartite metrics* (publicly indexed mathematical finding, 2026; complete text not inspected). Its facet-count invariant differs from centered Lipschitz variance.
