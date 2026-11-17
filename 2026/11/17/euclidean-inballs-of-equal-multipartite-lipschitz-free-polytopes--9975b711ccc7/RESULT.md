# Euclidean inballs of equal multipartite Lipschitz-free polytopes: a tripartite transition and arithmetic contact resonances

## Finding
For every integer \(k\ge3\), every positive even integer \(m\), and every \(1<t<2\), consider a finite metric space partitioned into \(k\) parts of size \(m\). Distinct points in the same part have distance \(t\), and points in different parts have distance \(1\). Let \(K\) be its real Lipschitz-free unit ball in the canonical Euclidean zero-sum subspace. Its global Euclidean inradius is
\[
 r(K)=\left[\frac m4\max\{k,\ t^2+(k-1)(2-t)^2\}\right]^{-1/2}.
\]
The origin is the **unique** center of a maximum-radius Euclidean ball. For \(k\ge4\) the inradius is independent of \(t\). For \(k=3\), the radius changes formula precisely at \(t=5/3\), from \((3m/4)^{-1/2}\) below and at the threshold to \(\bigl(m[t^2+2(2-t)^2]/4\bigr)^{-1/2}\) above it.

Set \(N=km\) and \(B=\binom{N}{N/2}\). For \(k=3\), define the integer
\[
 A_m(t)=3\sum_{q=1}^{m-1}\sum_{s=0}^{2m}
 \mathbf 1_{\{\,t(q-m/2)+(t-2)(s-m)=0\,\}}
 \binom mq\binom{2m}s.
\]
The number of *distinct facets* tangent to the origin-centered maximum ball equals \(B\) if \(k\ge4\), equals \(B\) for \(k=3,t<5/3\), equals \(B+A_m(t)\) for \(k=3,t=5/3\), and equals \(A_m(t)\) for \(k=3,t>5/3\). For irrational \(t>5/3\), this last count simplifies to \(3\binom{m}{m/2}\binom{2m}{m}\); at certain rational parameters extra tangent facets occur. All contact formulas concern distinct supporting facets, not multiplicity of equivalent descriptions.

## Assumptions and scope
The metric is defined on \(N=km\) labeled points, with \(k\ge3\), \(m\in2\mathbb Z_{>0}\), \(1<t<2\). Its triangle inequalities follow from \(t<2\). Write \(H=\{x\in\mathbb R^N:\sum_i x_i=0\}\) with the inherited, unscaled Euclidean norm and
\[
 K=\operatorname{conv}\left\{\frac{e_i-e_j}{d(i,j)}:i\ne j\right\}\subset H.
\]
The polar in \(H\) is \(P=\{f\in H:|f_i-f_j|\le d(i,j)\ \forall i,j\}\). Every vertex of \(P\) corresponds to a unique facet of \(K\); the latter lies at Euclidean distance \(1/\|f\|_2\) from the origin. The all-parameter claims above concern the *global* inball, not merely a ball centered at zero.

## Proof
**Extremal centered variance.** Let \(f\) be a real \(1\)-Lipschitz potential and write \(\bar f=N^{-1}\sum_i f_i\). The origin-centered radius is reciprocal to the maximum of \(V(f)=\sum_i(f_i-\bar f)^2\). If the range of \(f\) is at most \(1\), Popoviciu's variance inequality gives \(V(f)\le N/4\). Equality occurs for a binary potential taking the two endpoint values on exactly \(N/2\) points each; such balanced assignments are feasible because every distance between distinct points is at least \(1\).

Suppose the range is \(r>1\). A minimum and a maximum must occur in the same part, because points in different parts have distance at most \(1\). Translate the minimum to \(0\), choose a part containing both extrema, and hence \(1<r\le t\). All \(m\) coordinates of that part lie in \([0,r]\), while the remaining \(L=(k-1)m\) coordinates lie in \([r-1,1]\). Variance is strictly convex as a function of any one coordinate with the others fixed: its quadratic coefficient is \(1-1/N>0\). Its maximum on this enclosing coordinate box must therefore occur with every coordinate at an interval endpoint. Such assignments are themselves feasible: across-part differences are at most \(1\), and within-part differences are at most \(t\).

Let \(q\) of the active-part coordinates equal \(r\), with the other \(m-q\) equal to zero. Let \(s\) of the \(L\) outside coordinates equal \(r-1\), the others equal \(1\). Direct expansion and completion of a square give
\[
 V(f)=\frac m4\bigl[r^2+(k-1)(2-r)^2\bigr]
 -\frac{[r(q-m/2)+(r-2)(s-L/2)]^2}{N}.
\]
Therefore \(V(f)\le F(r)=m[r^2+(k-1)(2-r)^2]/4\). The function \(F\) is strictly convex, so its largest value over \(1\le r\le t\) is attained at \(r=1\) or \(r=t\). We have \(F(1)=N/4\). Since \(m\) and \(L\) are even, choosing \(q=m/2,s=L/2\) makes the square vanish, yielding equality at \(r=t\). Thus \(\max_{f\in P}V(f)=\max\{N/4,F(t)\}\), establishing the exact inradius. Algebraically,
\[
 F(t)-N/4=\frac m4(t-1)(kt-3k+4).
\]
This is negative throughout \(1<t<2\) when \(k\ge4\); when \(k=3\) it changes sign at \(t=5/3\).

**Why the maximizing potentials are facets.** Because \(V\) is strictly convex on \(H\), all its maximizers are extreme points of \(P\). Equivalently their tight-distance equalities span \(H\). A balanced binary configuration has connected tight cross-part edges: each color appears in at least two parts because \(N/2>m\); its bipartite tight-edge graph is connected. For an active assignment with \(1<r=t\), variance-maximization forces both extremes to occur in its active part, so \(1\le q\le m-1\). The tight edges inside the active part join its zero and \(t\) groups; all outside vertices connect by tight cross-part edges to one of those two groups. Thus the tight-edge graph is connected. For the active endpoint family, equality to \(F(t)\) is equivalent to the single displayed integer relation defining \(A_m(t)\). Each active configuration has a uniquely determined active part (the only part containing the global minimum and maximum), hence there is no overcount between the three choices of active part for \(k=3\). The balanced binary configurations are distinct from the active ones when \(t>1\). Strict convexity of \(F\) also excludes any additional maximizers with \(1<r<t\). Counting the independent assignments yields \(B\) or \(A_m(t)\) as applicable. At an irrational \(t\), the equality becomes \(t(q+s-3m/2)=2(s-m)\), forcing \(s=m\) and \(q=m/2\); this gives the simplified count.

**Global optimality and uniqueness of the center.** Since \(K=-K\), any feasible Euclidean ball of radius \(\rho\) centered at \(c\) implies the ball centered at \(-c\) is feasible, so convexity of \(K\) implies the centered ball of radius \(\rho\) is feasible. Thus the centered bound is the global inradius. Suppose another center \(c\in H\) attains the same radius. For every centered contact normal \(f\) and its opposite \(-f\), its two supporting inequalities force \(\langle c,f\rangle=0\).

When balanced binary contacts maximize variance, their centered normals span \(H\): swapping one selected and one unselected vertex produces every coordinate difference \(e_i-e_j\), and these span \(H\). When active contacts maximize, use only the central profiles \(q=m/2,s=L/2\). For any fixed active part, swapping a high and a low vertex in that part or in its complement produces all zero-sum directions internal to those two blocks. Those directions span the codimension-one subspace of \(H\) whose coordinate sum on the active part is zero. Choosing two distinct active parts generates all of \(H\). Hence contact normals span \(H\) in every parameter range; \(c=0\) is the unique incenter.

## Verification
The companion standalone checker uses rational arithmetic throughout and has no external dependencies. For the smallest case \(k=3,m=2\), it constructs all possible rooted spanning-tree tight-edge potentials from Prüfer tree codes and signed edge differences, filters them against **every** pairwise metric inequality, and independently computes maximal centered variance, exact contact multiplicities and contact-normal ranks at seven rational parameters straddling the threshold. Larger exact profiles use independent endpoint-state enumeration and contact-span witnesses, including \((k,m)=(3,4),(3,6),(4,2),(4,4),(5,2)\). All checks pass. The finite enumeration corroborates the proof; it does not establish the infinite family on its own. Run `python3 checker.py` from an extraction containing this file and `checker.py`.

For a concrete arithmetic resonance, \(k=3,m=6,t=12/7\) gives \(55530\) tangent facets, compared with the generic nonresonant count \(55440\). At \(t=5/3\) the same size has \(105140\) contacts.

## Relationship to prior work
The fundamental KR and Lipschitz polar definitions and graph-metric facet theory predate this result. Higashitani–Jochemko–Michałek (2018) give tight-edge characterizations and multipartite **graph-metric endpoint** results. D'Alì–Delucchi–Michałek (2019) describe symmetric edge and Lipschitz polytopes and combinatorial face structure. Previously published work on interpolated multipartite metrics classifies their facet **counts**, not, as far as verified here, the Euclidean variance maximum, incenter and arithmetic tangent-facet strata. The present formulas are for the strict metric interpolation \(1<t<2\), not the known graph-distance endpoint \(t=2\). Graph spread is the closely related maximum Lipschitz variance, so historically equivalent formulations must also be considered.

## Limitations
The equal part sizes and even part size are essential hypotheses for the exact balancing step. No formula for odd part size or general unequal parts is claimed. The canonical intrinsic Euclidean normalization is fixed; arbitrary linear re-embeddings need not preserve these radii. An existing result expressed via graph spread or variance on multipartite metrics could imply the radius formula; the literature comparison cannot eliminate that residual priority risk. The related existing facet-count work was accessible only by an abstract/summary, not a complete inspection. No independent audit has been performed.

## References
1. A. Higashitani, K. Jochemko, M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678 (first version 2018-07-20), especially the facet and complete multipartite discussions.
2. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (2019), §2.3 and combinatorial applications.
3. R. J. Aliaga, *Extreme points in Lipschitz-free spaces over compact metric spaces*, arXiv:2102.01219 (2021), for the surrounding Lipschitz-free geometry.
4. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156 (2009), for the maximum-variance viewpoint.
