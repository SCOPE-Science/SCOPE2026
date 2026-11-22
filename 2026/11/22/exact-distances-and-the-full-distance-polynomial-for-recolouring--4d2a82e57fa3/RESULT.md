# Exact distances and the full distance polynomial for recolouring stars at the sharp palette threshold

## Finding

Let \(S_n=K_{1,n}\) be the star with one center and \(n\) labelled leaves. Let \(\mathcal R_k(S_n)\) have as its vertices all proper assignments of \(k\) **named** colors to the \(n+1\) vertices, and an edge between assignments differing on exactly one vertex. For **every** pair \(n\ge2\) and \(k\ge n+1\), every distance in this graph has the following exact form.

Write \(\alpha=(x;a_1,\ldots,a_n)\), \(\beta=(y;b_1,\ldots,b_n)\); centers have colors \(x,y\) and leaf \(i\) has colors \(a_i,b_i\). Define \(h=\#\{i:a_i\ne b_i\}\) and \(w=\#\{i:a_i=y\ \text{and}\ b_i=x\}\). Then

\[
d_{\mathcal R_k(S_n)}(\alpha,\beta)=
\begin{cases}
h,&x=y,\\
h+1,&x\ne y,\ w=0,\\
h+2,&x\ne y,\ w>0.
\end{cases}
\]

Thus all vertices have eccentricity \(n+2\), and the radius and diameter are both \(n+2\). Define

\[
T=k^2-3k+3,\qquad F(z)=(k-1)(1+(k-2)z),\qquad
G(z)=(k-2)+Tz,\qquad H(z)=(k-2)+(T-1)z.
\]

The complete ordered-pair distance enumerator, **including** diagonal pairs, is

\[
\boxed{D_{n,k}(z)=\sum_{\alpha,\beta\in V(\mathcal R_k(S_n))} z^{d(\alpha,\beta)}
=kF(z)^n+k(k-1)z\bigl[H(z)^n+z(G(z)^n-H(z)^n)\bigr].}
\]

In particular, the number of **unordered distinct pairs** at the maximum distance is

\[
\boxed{\frac{k(k-1)}2\bigl[T^n-(T-1)^n\bigr].}
\]

For example, at \(n=3,k=4\), the complete ordered-pair distance distribution is \((108,744,2160,3600,3528,1524)\), so there are \(762\) unordered diametral pairs.

## Assumptions and scope

All \(n\) leaves are distinguished, all \(k\) colours are named, and colorings need not use every colour. The center is the unique degree-\(n\) vertex, and all steps recolor **exactly one** vertex while remaining proper. The formulas hold for every integer \(n\ge2\) and \(k\ge n+1\), including the borderline palette size \(k=n+1=\Delta(S_n)+1\). The distance polynomial counts ordered pairs, while the stated diametral count divides by two. No formula is asserted for a general tree or for fewer colors.

## Proof

**1. Lower bounds.** Each of the \(h\) differently colored leaves must be recolored at least once. If \(x\ne y\), the center must also be recolored at least once. If moreover \(w>0\), select a leaf initially colored \(y\) whose final color is \(x\). A one-step center change from \(x\) to \(y\) cannot coexist with a single recoloring of this leaf: before that change it cannot take color \(x\), and after that change it cannot retain color \(y\). Hence any valid sequence needs an extra step beyond \(h+1\), proving \(h+2\) as the lower bound in the swap case.

**2. Upper bounds without a swap.** If \(x=y\), recolor each differing leaf directly to its target, in arbitrary order, using \(h\) steps. If \(x\ne y\) and \(w=0\), first recolor every leaf presently colored \(y\) to its target, which is neither \(x\) (because \(w=0\)) nor \(y\) (because the final center is \(y\)). Recolor the center \(x\to y\), then recolor every remaining disagreeing leaf directly to its target. This uses exactly \(h+1\) steps.

**3. Upper bound with one swapped leaf.** Suppose \(x\ne y\) and \(w=1\). Recolor the unique swapped leaf from \(y\) to any temporary color other than \(x,y\). Recolor every other leaf initially \(y\) directly to its target; these targets are neither \(x\) nor \(y\). Change center \(x\to y\). Recolor the swapped leaf to \(x\), and recolor all remaining disagreeing leaves to targets. Each differing leaf is handled once except the swapped leaf, which is handled twice: total \(h+2\).

**4. Upper bound with two or more swapped leaves.** Suppose \(x\ne y\) and \(w\ge2\). Let \(m\) be the number of leaves initially colored \(y\). Among the \(k-2\) colors different from \(x,y\), at most \(n-m\) appear on initial leaves, so at least \(k-2-(n-m)\ge m-1\) are unused. Of these, at most \(m-w\) occur as target colors of initially-\(y\) leaves, because at least \(w\ge2\) such targets equal \(x\). Select a spare color \(z\) absent from all initial leaves and absent from all targets of initially-\(y\) leaves. Recolor the center \(x\to z\). Now recolor every initially-\(y\) leaf directly to its target; these targets are not \(z\), and no resulting leaf has color \(y\). Also recolor any other disagreeing leaf whose target is not \(z\) directly to that target; the center remains \(z\). Recolor center \(z\to y\), which is legal because every leaf formerly colored \(y\) has moved and no other leaf initially had color \(y\). Finally recolor any remaining disagreeing leaf to its target \(z\). This changes each disagreeing leaf exactly once and the center twice, costing \(h+2\).

**5. Counting distances.** For equal center colors, there are \(k\) center choices. On a given leaf there are \(k-1\) equal-color ordered choices and \((k-1)(k-2)\) unequal ones. Their weighted factor is \(F(z)\), giving \(kF(z)^n\).

For distinct centers there are \(k(k-1)\) choices. On each leaf, the initial and final colors are drawn from sets of size \(k-1\) that overlap in \(k-2\) colors; therefore there are \(k-2\) equal-color pairs and \(T=(k-1)^2-(k-2)\) unequal pairs, giving \(G(z)\). Exactly one unequal ordered pair, \((a_i,b_i)=(y,x)\), is a swap. Excluding that option leaves factor \(H(z)\). Non-swap pairs of colorings contribute \(zH(z)^n\), and those containing at least one swap contribute \(z^2(G(z)^n-H(z)^n)\). Summing proves the polynomial.

**6. Extremal distances.** Since \(h\le n\), all distances are at most \(n+2\). Given any initial coloring, choose a color \(y\) occurring at some leaf and let the target center be \(y\) and all target leaves be \(x\), the initial center color. Then \(h=n\), \(w\ge1\), so the distance is exactly \(n+2\). Consequently every coloring has eccentricity \(n+2\). A pair is diametral exactly if the center colors differ, all \(n\) leaf colors differ, and at least one leaf is a swap. For each ordered center pair there are \(T^n-(T-1)^n\) such leaf transitions, yielding the unordered count.

**7. Sharp palette boundary.** For each \(n\ge3\), take only \(k=n\) colors \(x,y,z_1,\ldots,z_{n-2}\), with all leaves initially colored \(y\) and center \(x\), and target center \(y\), target leaves \(x,x,z_1,\ldots,z_{n-2}\). Every leaf must change and at least two swaps occur. If the center changes only once, both swapped leaves must change twice, requiring at least \(n+3\) total recolorings. If the center changes twice, it must visit one of the colors \(z_j\) (every noncenter initial color except \(y\) is a target leaf color), so the leaf targeted to \(z_j\) cannot get its final color before the second center change, even though it must vacate \(y\) beforehand; this again forces at least \(n+3\) recolorings. Three center changes also force \(n+3\). Conversely choose \(z_1\) as an intermediate center color, recolor every leaf from \(y\) directly to its final color except the leaf targeted to \(z_1\), which goes temporarily to \(x\); change center to \(y\), then change the temporary leaf from \(x\) to \(z_1\). The center has changed twice, leaves \(n+1\) times, for distance exactly \(n+3\). Thus the \(k=n+1\) threshold for this distance law cannot be reduced. At \(n=2,k=2\), the reconfiguration graph is disconnected.

## Verification

The standalone script `verify.py` uses only the Python standard library. For every \(n\in\{2,3,4,5\}\) and both \(k=n+1\) and \(k=n+2\), it constructs the entire proper-colouring reconfiguration graph, runs breadth-first search from a complete set of symmetry-orbit representatives, checks every ordered pair distance against the formula, and compares the independently enumerated full distance counts with the polynomial coefficients. It also checks the sharpness witness by breadth-first search for \(3\le n\le6\) at \(k=n\). The script returns `VERIFY_OK`; these finite tests support but do not replace the preceding unbounded proof.

## Relationship to prior work

The coloring-reconfiguration framework and exact **diameter** of certain tree and complete-multipartite recoloring graphs are established in Cambie, Cames van Batenburg and Cranston, and in De Meyer. Cames van Batenburg's 2026 paper cites the known diameter \(n(G)+\mu(G)\) for trees at \(k\ge\Delta(G)+2\), which specializes to \(n+2\) here. This diameter equality is not claimed as new at that larger palette threshold. The contribution here is the pairwise distance rule, its **sharply smaller** palette threshold \(k=n+1\), the full ordered-pair distance distribution, self-centeredness at that threshold, and the explicit count of diametral pairs. The 2025 three-colouring tree-diameter study concerns a fixed three-colour palette and the extremal diameter among different trees, not the present all-pair formula for \(k\ge n+1\). No claim of established historical priority is made from failure to locate an equivalent formula.

## Limitations

This classification concerns single-vertex recolorings of a star and uses named colors; it does not cover arbitrary trees or list colorings, and the exact distance rule is false in general for \(k=n\). The finite verifier covers small orders only. The originality comparison is based on the accessible sources cited here and mathematical-record searches; unindexed formulations and older results under alternate terminology remain possible. There has been no independent mathematical audit.

## References

1. W. Cames van Batenburg, *Large diameter for \((\Delta+2)\)-colouring reconfiguration*, arXiv:2611.17022, first public 2026-11-12. https://arxiv.org/abs/2611.17022
2. L. De Meyer, *Optimal List Recoloring of Subcubic Graphs and Complete Multipartite Graphs*, arXiv:2501.03748, first public 2025-01-07. https://arxiv.org/abs/2501.03748
3. S. Cambie, W. Cames van Batenburg, D. W. Cranston, *Optimally Reconfiguring List and Correspondence Colourings*, arXiv:2204.07928, first public 2022-04-17. https://arxiv.org/abs/2204.07928
4. S. Asgarli, S. Krehbiel, S. MacLean, G. Zaimi, *Extremal diameters of 3-coloring graphs of trees*, arXiv:2512.03789, first public 2025-12-03. https://arxiv.org/abs/2512.03789
