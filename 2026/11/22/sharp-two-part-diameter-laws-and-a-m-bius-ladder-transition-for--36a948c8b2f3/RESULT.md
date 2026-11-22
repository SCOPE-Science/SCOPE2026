# Sharp two-part diameter laws and a Möbius-ladder transition for spherical antiprisms

## Finding
For each integer \(n\ge3\) and real \(0<h<1\), put \(r=\sqrt{1-h^2}\) and take the \(2n\) distinct points on the Euclidean unit sphere
\[
U_j=(r\cos(2\pi j/n),r\sin(2\pi j/n),h),\qquad
L_j=(r\cos((2j+1)\pi/n),r\sin((2j+1)\pi/n),-h),
\quad 0\le j<n.
\]
Write \(V_{n,h}=\{U_j,L_j:0\le j<n\}\), and let the *optimal two-part diameter* be
\[
\Delta_2(V)=\min_{V=V_0\sqcup V_1,\,V_0,V_1\ne\varnothing}
\max\bigl\{\operatorname{diam}(V_0),\operatorname{diam}(V_1)\bigr\},
\]
with ordinary Euclidean chord distance. Set \(s_n=\sin(\pi/(2n))\), \(c_n=\cos(\pi/(2n))\).

**Exact all-order partition law.** For every odd \(n\ge3\),
\[
\boxed{\Delta_2(V_{n,h})=2\sqrt{1-h^2}\,c_n,\qquad \operatorname{diam}(V_{n,h})=2.}
\]
For every even \(n\ge4\), define
\[
 A=4(1-h^2),\qquad B=4\bigl(h^2+(1-h^2)c_n^2\bigr),\qquad
 q_n=\frac{s_n^2}{1+s_n^2}.
\]
Then
\[
\boxed{\Delta_2(V_{n,h})=\sqrt{\min\{A,B\}},\quad
\operatorname{diam}(V_{n,h})=\sqrt{\max\{A,B\}}.}
\]
The Euclidean diameter graph joins pairs at the largest mutual distance. For even \(n\), as \(h^2\) increases across the sharp critical value \(q_n\), this graph changes from \(n\) disjoint edges (the within-ring opposite pairs) to a Möbius ladder \(M_{2n}\) at equality and then to a Hamilton cycle \(C_{2n}\) (the staggered-ring farthest cross-pairs). At the critical height its chromatic number is exactly three, while in the two strict regimes the chromatic number is two. Accordingly, the minimum number \(b(V_{n,h})\) of subsets having diameter *strictly smaller than* \(\operatorname{diam}(V_{n,h})\) is
\[
\boxed{b(V_{n,h})=\begin{cases}3,&n\text{ even and }h^2=q_n,\\2,&\text{otherwise}.\end{cases}}
\]
For odd \(n\), the diameter graph is a perfect matching. Moreover the even-order two-part optimum is uniquely maximized over \(0<h<1\) at \(h^2=q_n\), where
\[
\boxed{\max_{0<h<1}\Delta_2(V_{n,h})=\frac2{\sqrt{1+s_n^2}}.}
\]
For odd \(n\), \(\Delta_2\) strictly decreases with \(h\) and has unattained supremum \(2c_n\) as \(h\downarrow0\).

## Assumptions and scope
The point set is finite, with two equal regular \(n\)-point latitude rings at opposite nonzero heights and relative twist exactly \(\pi/n\). All diameters use **Euclidean chord distance** on points of the unit sphere, not intrinsic spherical geodesics or the diameter of the solid convex hull. A partition consists of exactly two nonempty disjoint subsets and permits arbitrary labeling; an optimal diameter uses a non-strict within-part bound, whereas the Borsuk number \(b(V)\) uses a strict bound relative to the original diameter. The graph \(M_{2n}\) here means the cycle on \(2n\) nodes with chords joining nodes \(n\) cyclic positions apart. The statements quantify over every integer \(n\ge3\) and every real \(0<h<1\).

## Proof
**1. Distances and candidates.** Within either ring, for a cyclic index difference \(k\), squared distance equals \(4r^2\sin^2(\pi k/n)\). Between rings the angular difference is an odd multiple of \(\pi/n\) and squared distance equals \(4h^2+4r^2\sin^2((2k+1)\pi/(2n))\). For even \(n\), the largest within-ring squared distance is \(A=4r^2\), attained precisely by opposite vertices in each ring: a total of \(n\) pairs. The largest cross-ring squared distance is \(B=4(h^2+r^2c_n^2)\), attained at two cross-ring partners for each top vertex: a total of \(2n\) pairs. These cross pairs form one Hamiltonian cycle \(C_{2n}\). Each within-ring opposite pair joins vertices at distance \(n\) along this cycle, so their union is \(M_{2n}\).

**2. Even-order lower bound.** For any two-coloring of the \(2n\) sites, at least one edge in the graph obtained by joining all pairs at squared distance \(\ge\min\{A,B\}\) is monochromatic. Indeed, if \(A\le B\), that graph contains the Hamiltonian cross-ring cycle and the \(n\) opposite chords; this Möbius ladder has an even rim and opposite chords separated by an even number \(n\) of rim edges, so is not bipartite. If \(B<A\), the same conclusion holds because the graph still contains both types of edges. Thus \(\Delta_2^2\ge\min\{A,B\}\). At equality, the very same nonbipartite ladder gives the lower bound; at either strict inequality, edges of the longer class already suffice for a strict-diameter obstruction only at the maximum, but for the two-part optimum the union at \(\min\{A,B\}\) is still needed.

**3. Even-order matching upper bound.** If \(A\le B\), the partition into the two rings has within-class squared diameter exactly \(A\). If \(B\le A\), color the sites so each opposite same-ring pair has different colors (for example color each ring by choosing one representative of each diametral pair, colored zero, and the opposite representatives one). Then every same-color pair within a ring is *not* diametral. Its squared distance is at most \(A_2=4r^2\cos^2(\pi/n)\), whereas
\[
\frac B4=h^2+r^2c_n^2>r^2\cos^2(\pi/n)=\frac{A_2}4.
\]
All cross-ring pair distances are at most \(B\). Thus this partition has maximum squared within-class distance at most \(B\), proving equality in both regimes. The formulas for the full-set diameter follow immediately from the candidate distances.

**4. Diameter-graph transition and exact chromatic threshold.** As \(h^2\) increases, \(A=4(1-h^2)\) decreases strictly while \(B=4(1-(1-h^2)s_n^2)\) increases strictly; equality occurs only at \(h^2=q_n=s_n^2/(1+s_n^2)\). In the strict regimes the diameter graph is respectively a perfect matching or an even cycle, hence is bipartite with an edge. At the equality the diameter graph is the Möbius ladder and is not bipartite. It is three-colorable: index its Hamiltonian rim \(x_0,\dots,x_{2n-1}\) with opposite chords \(x_i x_{i+n}\), write \(n\) even, color the first half alternating zero, one, and color the second half \((x_n,\ldots,x_{2n-1})\) by \(2,0,1,0,1,\ldots,0,1,2\) (where the interior alternates, beginning with zero and ending with one). Adjacent rim sites, the wraparound pair, and every opposite chord have different colors. Any partition into fewer than three strict-smaller-diameter parts would color the diameter graph with fewer than three colors. Three colors suffice by construction. Hence the stated exact Borsuk numbers follow.

**5. Odd-order case.** Write \(n=2m+1\). For every upper site \(U_j\), the lower site \(L_{j+m}\) is precisely its Euclidean antipode; these \(n\) pairs form the whole diameter graph, and \(\operatorname{diam}V=2\). Within one ring the largest distance is \(2r\cos(\pi/(2n))=2rc_n\), attained by index jumps of size \(m\) or \(m+1\). The graph of these within-ring largest-distance pairs is an odd \(n\)-cycle, because \(\gcd(m,n)=1\). Any two-coloring of this ring therefore makes a largest-distance pair monochromatic, forcing the optimal partition diameter to be at least \(2rc_n\). Partitioning by the two latitude rings attains that value, proving equality. Each antipodal pair can be split between two colors, giving \(b(V)=2\).

**6. Sharp even-height stability point.** With \(u=h^2\), the two squared-distance branches \(A(u)\) and \(B(u)\) are respectively strictly decreasing and strictly increasing. Their minimum is therefore uniquely maximized at their only intersection \(u=q_n\); substitution gives \(\Delta_2=2/\sqrt{1+s_n^2}\). For odd \(n\), the displayed expression is strictly decreasing on \(0<h<1\), proving the limiting supremum claim.

## Verification
The standalone `verify_antiprism.py` directly builds all Cartesian coordinates, independently evaluates every pairwise Euclidean squared distance, computes the threshold graphs and independently checks graph bipartiteness by breadth-first search. It covers even integers \(4\le n\le40\) at seven heights including the analytic threshold and odd integers \(3\le n\le41\) at six heights, totaling 253 cases and 303,178 pair checks. Its output is embedded in `verification_output.txt`. The finite checks corroborate, rather than prove, the infinite quantified theorem. The analytical distance comparison, nonbipartiteness, and two explicit partitions above supply the proof at all parameters. Reproduce with the Python 3 standard library: `python3 verify_antiprism.py`.

## Relationship to prior work
Tolmachev (2026) studies Borsuk numbers, spherical partitions, contact points, and related quantitative partition questions, providing the motivation and general setting; the inspected full text does not classify the finite antiprism family or its diameter graph. A previously published exact two-ring spherical *covering* theorem gives a different height optimization for these same staggered point configurations, with optimal squared height \(\cos(\pi/n)/(1+\cos(\pi/n))\). That covering theorem does **not** imply the present two-class within-diameter minimax formula or the nonbipartite diameter-graph transition. A published twelve-point hexagonal-antiprism Vietoris–Rips study tabulates all six Euclidean pair-distance classes for the particular case \(n=6\), which is recognized as an antecedent of the elementary pair-distance calculation above; the work concerns a varying-radius simplicial homology filtration and does not supply this all-\(n\) two-part optimum or graph chromatic transition. Standard results on Möbius-ladder coloring are classical and are not claimed as original. The present contribution is the unified exact diameter partition law, sharp exceptional-height Borsuk threshold and geometric diameter-graph classification for every ring size. Historical priority remains provisional.

## Limitations
This is not a theorem for arbitrary twisted rings, arbitrary finite spherical configurations, or the continuous solid polytope. The classification of Möbius ladders as abstract graphs and their chromatic behavior are prior knowledge; the new feature is their exact geometric realization at the unique critical height and the corresponding all-order minimax law. The finite exhaustive checks cover only the stated finite sample of parameters, while the proof covers all parameters. No independent mathematical audit has been conducted. Unindexed literature under two-clustering, diameter-graph or antiprism terminology remains a priority risk.

## References
1. A. Tolmachev, *Novel upper bounds for Borsuk numbers from contact points and spherical partitions*, arXiv:2611.16775v1, first public November 12, 2026. https://arxiv.org/abs/2611.16775.
2. *Sharp spherical covering by two twisted regular latitude rings*, published published-finding corpus mathematical record (October 18, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-spherical-covering-by-two-twisted-regular-latitude-rings--d6c704c1d311.
3. *Integral persistence phase diagram for height-deformed hexagonal antiprisms*, published published-finding corpus mathematical record (November 1, 2026). https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-integral-persistence-phase-diagram-for-height-deformed-hexagonal--679c3e42e50f.
4. *Antiprism graph*, Wolfram MathWorld, https://mathworld.wolfram.com/AntiprismGraph.html (the skeletal edge graph is distinct from the Euclidean diameter graph).
