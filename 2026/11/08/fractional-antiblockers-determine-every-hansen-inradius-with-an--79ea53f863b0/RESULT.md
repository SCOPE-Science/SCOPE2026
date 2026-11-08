# Fractional antiblockers determine every Hansen inradius, with an unbounded failure of the clique law

## Finding
Let \(G\) be any finite nonempty simple graph with vertex set \(V\) of order \(n\). In its **canonical Euclidean realization**, the Hansen polytope is the twisted stable-set prism
\[
\mathcal H(G)=\operatorname{conv}\{(1,\mathbf1_S),(-1,-\mathbf1_S):S\subseteq V\text{ stable in }G\}\subset\mathbb R^{n+1}.
\]
For any graph \(F\), define the *clique-constrained fractional stable-set polytope*
\[
Q(F)=\{p\in\mathbb R_{\ge0}^{V(F)}:\sum_{i\in C}p_i\le1\text{ for every clique }C\text{ of }F\},
\qquad \mu(F)=\max_{p\in Q(F)}\sum_{i\in V(F)}p_i^2.
\]
Then the **exact Euclidean inradius** of \(\mathcal H(G)\) is
\[
\boxed{r(\mathcal H(G))=(1+4\mu(\overline G))^{-1/2}.}
\tag{1}
\]
The origin is an incenter. Moreover, all facets tangent to its largest inscribed ball have outward polar normals **exactly**
\[
\boxed{\pm(1,-2p),\qquad p\in\operatorname*{argmax}_{q\in Q(\overline G)}\|q\|_2^2.}
\tag{2}
\]
These maximizers are vertices of \(Q(\overline G)\). In particular, no polar point with first coordinate strictly between \(-1\) and \(1\) is farthest from the origin.

For perfect \(G\), formula (1) specializes to the previously established \(r=(1+4\omega(G))^{-1/2}\), since \(Q(\overline G)=\operatorname{STAB}(\overline G)\) and \(\mu(\overline G)=\omega(G)\). In sharp contrast, the clique-number formula can fail by an **unbounded multiplicative factor** over nonperfect graphs: there exists a sequence \(G_j\) with \(|V(G_j)|\to\infty\) for which
\[
\frac{(1+4\omega(G_j))^{-1/2}}{r(\mathcal H(G_j))}\longrightarrow\infty.
\tag{3}
\]
A finite witness is furnished by the complement \(G\) of the \(35\)-vertex Ramsey \((3,9)\) graph: it has \(\omega(G)=8\), but
\[
\boxed{r(\mathcal H(G))\le1/6<1/\sqrt{33}=(1+4\omega(G))^{-1/2}.}
\tag{4}
\]
The displayed \(1/6\) is a rigorously valid upper bound, **not** a claim that this particular inradius equals \(1/6\).

## Assumptions and scope
All graphs are finite, simple and nonempty. The complement \(\overline G\) is on the same labelled vertex set. Stable sets include the empty set. Cliques include singletons; the empty clique is harmless. A polytope is given the standard Euclidean metric in the stated \((n+1)\)-dimensional coordinates, rather than in an arbitrary affine image. Its inradius maximizes over **all** possible centers. The compactness of \(Q(F)\) follows from the singleton clique inequalities \(0\le p_i\le1\); its maximum in the definition of \(\mu(F)\) is therefore attained.

For any graph \(F\), \(Q(F)\) is a standard polyhedral relaxation of its stable-set polytope. The exact inradius reduction (1), tangent-normal classification (2), and sequence (3) apply to arbitrary graphs, not merely perfect graphs. The theorem does not assert an elementary closed form for the nonlinear invariant \(\mu(F)\) on all graph classes.

## Proof
**1. The centered ball is optimal.** The polytope \(\mathcal H(G)\) is centrally symmetric and full dimensional: the vertices corresponding to the empty stable set and all singleton stable sets affinely span the ambient space, and their negatives give the other side. It contains the origin in its interior. If a ball of radius \(r\) centered at \(c\) lies in \(\mathcal H(G)\), so does its reflection centered at \(-c\). Convexity then puts the same-radius ball centered at the origin in \(\mathcal H(G)\). Hence
\[
r(\mathcal H(G))^{-1}=\max_{y\in\mathcal H(G)^\circ}\|y\|_2.
\tag{5}
\]

**2. Polar inequalities and positive/negative parts.** Write \(y=(t,x)\) with \(t\in\mathbb R\) and \(x\in\mathbb R^V\). From the exact vertex description, the polar is
\[
\mathcal H(G)^\circ
=\{(t,x):|t+\sum_{i\in S}x_i|\le1\text{ for every stable }S\subseteq V\}.
\tag{6}
\]
The empty stable set forces \(-1\le t\le1\). Let \(x^+\) and \(x^-\) be the disjoint nonnegative positive and negative coordinate parts of \(x\). For any stable \(S\), the subsets \(S\cap\{i:x_i>0\}\) and \(S\cap\{i:x_i<0\}\) are stable, so (6) implies
\[
\sum_{i\in S}x_i^+\le1-t,\qquad
\sum_{i\in S}x_i^-\le1+t.
\tag{7}
\]
The stable sets of \(G\) are exactly the cliques of \(\overline G\). Thus whenever the respective denominator is positive,
\[
\frac{x^+}{1-t}\in Q(\overline G),\qquad
\frac{x^-}{1+t}\in Q(\overline G).
\tag{8}
\]
At an endpoint where a denominator vanishes, (7), applied to singleton stable sets, forces the corresponding numerator to vanish. Consequently (8) yields the bounds \(\|x^+\|_2^2\le(1-t)^2\mu\) and \(\|x^-\|_2^2\le(1+t)^2\mu\) also at endpoints, where \(\mu=\mu(\overline G)\).

Since the two coordinate parts are disjoint,
\[
\|(t,x)\|_2^2
=t^2+\|x^+\|_2^2+\|x^-\|_2^2
\le t^2+2(1+t^2)\mu\le1+4\mu.
\tag{9}
\]
Here \(\mu\ge1\), because each singleton coordinate vector belongs to \(Q(\overline G)\); the last inequality is strict whenever \(|t|<1\).

**3. Sharpness and complete contact classification.** Let \(p\) maximize \(\mu\) in \(Q(\overline G)\). Because every stable set \(S\) of \(G\) is a clique of \(\overline G\), one has \(0\le\sum_{i\in S}p_i\le1\). Thus \((1,-2p)\) satisfies (6), and its squared norm is \(1+4\mu\). Its antipode is also feasible. This attains (9) and establishes (1) using (5).

Conversely, equality in (9) forces \(|t|=1\). If \(t=1\), (7) forces \(x^+=0\), while (6) becomes precisely \(p=-x/2\in Q(\overline G)\). Equality of the norm forces \(\|p\|_2^2=\mu\); the case \(t=-1\) follows by symmetry. Since squared norm is strictly convex, every maximizer over the convex polytope \(Q(\overline G)\) is a vertex. Polar vertices correspond to facet normals of \(\mathcal H(G)\), and their support hyperplanes lie at distance \(1/\|y\|_2\) from the origin. Therefore precisely the vectors (2) correspond to tangencies with the centered maximal ball.

**4. Perfect graphs and an explicit finite departure.** For perfect \(G\), its complement is perfect and \(Q(\overline G)=\operatorname{STAB}(\overline G)\). The vertices of this stable-set polytope are the independent-set indicator vectors. Strict convexity shows \(\mu(\overline G)=\alpha(\overline G)=\omega(G)\), giving the previously established perfect-graph formula.

Let \(F\) be the published \(35\)-vertex Ramsey \((3,9)\) graph, so \(F\) is triangle-free and has independence number \(8\). With \(G=\overline F\), the graph \(G\) has clique number \(8\). Since \(F\) is triangle-free, every clique of \(F\) has at most two vertices; hence \(p=\mathbf1/2\in Q(F)\), with \(\|p\|_2^2=35/4>8\). Substitution into (1) gives (4), establishing a strict and explicitly quantified failure of the perfect-graph rule.

**5. An unbounded separation.** We give an elementary probabilistic existence argument, with no computational hypothesis. For an integer \(N\to\infty\), draw an Erdős–Rényi graph \(F_0\sim G(N,N^{-3/4})\). The expected number of triangles is at most \(N^{3/4}/6\), so with probability tending to one it is at most \(N^{7/8}\) by Markov's inequality. Take \(k=\lceil4N^{3/4}\log N\rceil\). A union bound gives
\[
\Pr(\alpha(F_0)\ge k)
\le {N\choose k}(1-N^{-3/4})^{\binom{k}{2}}
\le\exp\left(k\log\frac{eN}{k}-\frac{N^{-3/4}k(k-1)}2\right)
\longrightarrow0.
\tag{10}
\]
Indeed, the exponent's leading term is bounded above by \((-7+o(1))N^{3/4}(\log N)^2\). Thus there exist graphs \(F_0\) satisfying both properties. Delete one vertex from each remaining triangle until none remain, using at most \(N^{7/8}\) deletions. The resulting triangle-free graph \(F\) has \(n\ge N-N^{7/8}\) vertices and \(\alpha(F)<k=o(n)\). For \(G=\overline F\), we have \(\omega(G)=\alpha(F)=o(n)\) and \(\mu(F)\ge n/4\), witnessed again by \(p=\mathbf1/2\). Therefore
\[
\frac{(1+4\omega(G))^{-1/2}}{r(\mathcal H(G))}
=\sqrt{\frac{1+4\mu(F)}{1+4\omega(G)}}
\ge\sqrt{\frac{n+1}{1+4\alpha(F)}}\longrightarrow\infty,
\]
proving (3).

## Verification
`verify.py` constructs the fractional clique-constrained polytope and the full Hansen polar independently for six low-order graphs, enumerates their vertices through halfspace intersection, compares their maximum squared norms against identity (1), and checks that all maximizers of the polar lie in its two endpoint sections. It reports `HANSEN_FRACTIONAL_ANTIBLOCKER_CHECKS_PASSED`. The same standalone program decodes the documented \(35\)-vertex Ramsey graph from its graph6 representation, checks triangle-freeness and \(140\) edges, and **exhaustively enumerates maximal independent sets**, finding independence number \(8\) and \(3365\) maximal independent sets. It reports `RAMSEY35_EXACT_CHECK_PASSED`. The finite calculations are independent corroboration; steps 1–5 provide the mathematical proof for all graphs and all asymptotic sizes.

To replay: run `python verify.py` in a Python environment with NumPy and SciPy. The graph6 data are embedded in the file, attributed to Brendan McKay's published graph collection, so no network access is required.

## Relationship to prior work
Freij, Henze, Schmitt, and Ziegler (2013, Section 2, Definition 4 and Lemma 5) define Hansen polytopes for arbitrary graphs and state the complete clique-indexed facet description **only for perfect graphs**; their paper studies face numbers, Hanner structures, and Mahler products. Aprile, Cevallos, and Faenza (first arXiv public version 2017-02-10; full text 2017) study perfect-graph Hansen polytopes and vertex–facet inequalities, not Euclidean inradii. The perfect-graph Euclidean formula \(r=(1+4\omega(G))^{-1/2}\) and maximum-clique tangencies are also established in the prior public study *Clique and stability numbers as exact Euclidean radii of perfect-graph Hansen polytopes* (2026); these are not claimed as new.

The present contribution is the **arbitrary-graph** quadratic-antiblocker identity, proof that every farthest polar normal lies on an endpoint section, classification by all quadratic maximizers of the fractional stable-set polytope, and finite/asymptotically unbounded counterexamples to extension of the perfect-graph clique law. Goedgebeur and Radziszowski's Ramsey-graph work and McKay's public graph dataset supply a pre-existing graph witness, not a new graph construction. The exact inradius of that particular \(35\)-vertex Hansen polytope is **not** determined; only the certified strict bound is asserted.

## Limitations
Formula (1) reduces metric inradius determination to a maximization of a convex quadratic over a standard bounded fractional stable-set polytope; this optimization can remain difficult for arbitrary graphs. The theorem does not claim a polynomial-time algorithm, a closed graph-invariant formula in terms of clique number for all graphs, an exact \(35\)-vertex radius, or novelty of the classical random-graph/Ramsey existence statements. Results are metric in the explicit canonical coordinates and need not survive affine transformations. The primary Hansen paper from 1977 was not examined in full; hidden historical equivalences under antiprism, antiblocker, or norm-maximization terminology remain possible.

## References
1. Ragnar Freij, Matthias Henze, Moritz W. Schmitt, and Günter M. Ziegler, *Face Numbers of Centrally Symmetric Polytopes Produced from Split Graphs*, Electronic Journal of Combinatorics 20(2) (2013), #P32, DOI 10.37236/3315, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i2p32/pdf/.
2. Manuel Aprile, Alfonso Cevallos, and Yuri Faenza, *On 2-level polytopes arising in combinatorial settings*, arXiv:1702.03187 (first public version 2017-02-10), https://arxiv.org/html/1702.03187v2.
3. Jan Goedgebeur and Stanisław P. Radziszowski, *New computational upper bounds for Ramsey numbers R(3,k)*, Electronic Journal of Combinatorics 20(1) (2013), P30; see also https://users.cecs.anu.edu.au/~bdm/data/ramsey.html.
4. *Clique and stability numbers as exact Euclidean radii of perfect-graph Hansen polytopes*, public research record (2026-10-11), stable bibliographic identifier 5c60f4f604ef.
5. Branko Kohl, McCabe Olsen, and Raman Sanyal, *Unconditional Reflexive Polytopes*, Discrete & Computational Geometry 64 (2020), 427–452, DOI 10.1007/s00454-020-00199-8.
