# A sharp quarter-part transition for Lipschitz-to-variance embeddings on complete multipartite metrics

## Finding

Let \(G=K_{n_1,\ldots,n_r}\), with \(r\ge2\) nonempty parts, \(N=\sum_{i=1}^r n_i\ge2\), and \(m=\max_i n_i\). Equip the vertex set with the unit-edge shortest-path metric and the uniform probability measure \(\mu\). Write \(\operatorname{Lip}_0(G)\) for the real Banach space of functions vanishing at one fixed vertex with norm equal to their Lipschitz constant. The canonical centered inclusion
\[
T_G:\operatorname{Lip}_0(G)\longrightarrow L_2^0(V,\mu),\qquad T_Gf=f-\int f\,d\mu
\]
has the sharp squared operator norm
\[
\boxed{\|T_G\|^2=\operatorname{spr}(G)
=\frac{1}{N^2}\max\left\{\left\lfloor\frac{N^2}{4}\right\rfloor,\;Nm-(m\bmod 2)\right\}.}
\tag{1}
\]
Here \(\operatorname{spr}(G)\) is the maximum vertex variance over all real functions of Lipschitz constant at most one. Formula (1) also specifies all extremizers as follows (up to an additive constant and common sign reversal):

* **Balanced binary type.** A partition of the \(N\) vertices into two groups of sizes \(\lfloor N/2\rfloor\) and \(\lceil N/2\rceil\) is assigned the respective values \(0\) and \(1\). These are maximizing precisely when the first argument in (1) is at least the second.
* **Polarized largest-part type.** Choose a part of maximum cardinality \(m\ge2\). All other parts receive value \(0\). In the selected part, \(\lfloor m/2\rfloor\) vertices receive \(-1\) and \(\lceil m/2\rceil\) receive \(+1\), or vice versa. These are maximizing precisely when the second argument in (1) is at least the first.

No additional maximizers exist. At \(N=2,3\), a numerical tie of the two terms for a singleton largest part does not create a nonexistent polarized configuration: the condition \(m\ge2\) above is essential.

For every \(N\ge4\), the variance is exactly the clique baseline \(\lfloor N^2/4\rfloor/N^2\) if and only if \(m\le\lfloor N/4\rfloor\). For \(m>\lfloor N/4\rfloor\), the polarized term is strictly larger. **Coexistence of both extremizer types** occurs exactly at \(N\equiv0\pmod8\) and \(m=N/4\). For example, the balanced four-partite graph \(K_{s,s,s,s}\) has spread \(1/4\) for every positive integer \(s\), despite missing exactly \(2s(s-1)\) clique edges (an asymptotic quarter of all edges of the complete graph); at even \(s\) it admits the two distinct extremizer types.

## Assumptions and scope

All graphs are finite, connected, simple and unweighted. There are at least two nonempty independent parts, and edges join all vertices in distinct parts. Vertex measure is uniform, all functions are real, and variance is normalized as \(\operatorname{Var}_\mu(f)=N^{-1}\sum_vf(v)^2-(N^{-1}\sum_vf(v))^2\), with no Bessel correction. The norm on \(\operatorname{Lip}_0(G)\) is the full graph-metric Lipschitz norm, equivalently the largest absolute edge difference. The basepoint choice changes neither norm nor variance.

## Proof

**1. Extremal reduction, with full quantifiers.** Fix one basepoint \(o\). The set \(\mathcal L=\{f:V\to\mathbb R:f(o)=0,\ |f(u)-f(v)|\le1\text{ for every edge }uv\}\) is a compact polytope: connectedness bounds all coordinates. For any two distinct anchored functions \(f,g\) and \(0<t<1\),
\[
\operatorname{Var}_\mu(tf+(1-t)g)
=t\operatorname{Var}_\mu(f)+(1-t)\operatorname{Var}_\mu(g)
-t(1-t)\operatorname{Var}_\mu(f-g)
< t\operatorname{Var}_\mu(f)+(1-t)\operatorname{Var}_\mu(g).
\]
The strict inequality follows because \(f-g\) is nonconstant whenever \(f\ne g\) and both vanish at \(o\). Thus every maximum is attained at, and only at, a vertex of \(\mathcal L\).

**2. Integrality and diameter-two range.** For feasible \(f\), let its tight-edge graph \(H_f\) contain precisely edges \(uv\) with \(|f(u)-f(v)|=1\). The active constraint normals are signed edge-incidence vectors. After anchoring, they have full rank \(N-1\) if and only if \(H_f\) is connected. Hence at a polytope vertex there is a spanning tree of tight edges. Starting from \(f(o)=0\), the value of every vertex is an integer, obtained by summing increments \(\pm1\) along this tree. The graph has diameter at most two, since every two vertices in the same part share a neighbor in another part. Therefore the integer-valued \(f\) has range at most two. A nonconstant extremal function has range either one or two.

**3. Binary branch.** If the range is one, translate so the only values are \(0\) and \(1\). If precisely \(t\) vertices have value \(1\), then
\[
\operatorname{Var}_\mu(f)=\frac{t(N-t)}{N^2}
\le\frac{\lfloor N^2/4\rfloor}{N^2}.
\tag{2}
\]
Equality means \(t\in\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\). Every such binary assignment is feasible, so the right side is achievable, independent of the part sizes.

**4. Three-level branch.** If an extremal function has range two, translate so its values lie in \(\{-1,0,1\}\) with both end values present. Any vertices taking \(-1\) and \(+1\) cannot be adjacent; consequently all such vertices belong to a *single* part \(A_i\). Indeed, choose one \(-1\) vertex in part \(A_i\); all \(+1\) vertices must be in \(A_i\), and then all \(-1\) vertices must also lie there. Every vertex outside \(A_i\) is adjacent to both signs and must have value \(0\). A vertex of \(A_i\) with value \(0\) has no tight edge, contradicting connectivity of \(H_f\); all \(n_i\) vertices of \(A_i\) take one of the signs. If \(k\) of those vertices take \(+1\), with \(1\le k<n_i\), then
\[
\operatorname{Var}_\mu(f)=\frac{n_i}{N}-\frac{(2k-n_i)^2}{N^2}
\le\frac{n_i}{N}-\frac{n_i\bmod2}{N^2}
\le\frac{m}{N}-\frac{m\bmod2}{N^2}.
\tag{3}
\]
Both inequalities are sharp exactly when \(k\) is nearest to \(n_i/2\) and \(n_i=m\). The last inequality is strict for \(n_i<m\), since the integer function \(h(t)=Nt-(t\bmod2)\) is strictly increasing for positive \(t\) when \(N\ge2\). Conversely, choosing a largest part with \(m\ge2\) and its nearly balanced signs, and setting all other vertices to zero, is feasible and achieves (3). Its tight graph is connected: every signed vertex is joined to all outside zeros, and the part contains both signs. This completes the formula and the full equality classification. The \(m=1\) case has no range-two configurations, but (2) dominates the extraneous algebraic second argument except for a harmless equality at \(N=2,3\).

**5. Exact quarter-part boundary.** Put \(q=\lfloor N/4\rfloor\) and \(H=\lfloor N^2/4\rfloor\). For \(N\ge4\), a direct four-residue computation shows \(Nq-(q\bmod2)\le H\), with equality *only* when \(N\) is divisible by eight. It also shows \(N(q+1)-((q+1)\bmod2)>H\). Since \(Nm-(m\bmod2)\) is strictly increasing in \(m\), these two inequalities give the threshold and all ties. To see both inequalities explicitly, write \(N=4q+r\), \(r=0,1,2,3\). For \(m=q\), the difference \(Nm-(m\bmod2)-H\) is, respectively,
\[
-(q\bmod2),\quad-q-(q\bmod2),\quad-2q-1-(q\bmod2),\quad-3q-2-(q\bmod2).
\]
For \(m=q+1\), the corresponding four differences are exactly \(4q+(q\bmod2)-1\), \(3q+(q\bmod2)\), \(2q+(q\bmod2)\), and \(q+(q\bmod2)\). Each is strictly positive for \(q\ge1\). This proves the asserted phase classification. \(\square\)

## Verification

The accompanying `checks/verify_multipartite_spread.py` uses only the Python standard library and exact rational arithmetic. It enumerates all unordered positive part-size profiles through total order eight, every feasible anchored integer-valued one-Lipschitz function on each profile, and every equality shape, then compares the exact results against (1) and the stated classification. It also verifies the quarter-part phase and tie arithmetic for every \(4\le N\le1000\) and every candidate largest-part size \(1\le m<N\). Its successful output includes `EXHAUSTIVE_INTEGER_LIPSCHITZ_PROFILES_AND_EQUALITY_SHAPES_OK 58 13800 968`, `SHARP_QUARTER_PHASE_AND_TIE_CERTIFICATES_OK 499497`, and `ALL_MULTIPARTITE_SPREAD_CHECKS_OK`. The universal proof does not rely on these finite checks; in particular, the finite range of a checker cannot establish all-order uniqueness.

## Relationship to prior work

Addario-Berry, Janson and McDiarmid (arXiv:0902.1156v1, 6 February 2009) set out the graph-spread invariant and general concentration context. Their early sections state that integral extremizers exist and give the complete-graph example, but do not give the multipartite sharp embedding formula or quarter-part boundary. Godefroy and Kalton (2003) establish a foundational Lipschitz-free Banach-space framework; they do not supply this sharp \(\operatorname{Lip}_0\)-to-centered-\(L_2\) constant. Bobkov, Houdré and Tetali (2006) study related subgaussian constants, which are a distinct functional from worst-case variance.

The strongest nearby structural result is Higashitani, Jochemko and Michałek (arXiv:1807.07678v1, Proposition 3.5). Their **complete-multipartite facet classification already supplies the possible extreme potential shapes**, and the present proof neither claims that classification as new nor assumes it requires rediscovery. Optimizing the quadratic centered norm over those shapes gives (1), the equality conditions and the sharp quarter-part transition; the cited proposition does **not itself report** these sharp Lipschitz-to-variance embedding constants or the stability plateau. A later published account of the interior metric interpolation addresses facet counts, not this variance optimization. The difference between **existence/shape of extreme points** and **which shapes maximize an explicit centered quadratic norm** is the substantive additional comparison.

## Limitations

The theorem concerns uniform vertex mass and the unit-edge graph metric of complete multipartite graphs with at least two parts. It does not cover arbitrary weighted masses, unequal cross-part edge lengths, or general joins. The two extreme potential types are established in earlier facet literature; only the sharp norm, optimization/equality selection and phase conclusion are asserted as additional results. This work has not undergone independent mathematical audit, and equivalent calculations in unindexed sources remain possible.

## References

1. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156v1 (first posted 6 February 2009), https://arxiv.org/abs/0902.1156.
2. G. Godefroy and N. J. Kalton, *Lipschitz-free Banach spaces*, Studia Mathematica **159** (2003), 121–141, https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/159/1/90209/lipschitz-free-banach-spaces.
3. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1 (20 July 2018), especially Proposition 3.5, https://arxiv.org/abs/1807.07678.
4. S. G. Bobkov, C. Houdré and P. Tetali, *The subgaussian constant and concentration inequalities*, Israel Journal of Mathematics **156** (2006), 255–283; author-hosted manuscript https://houdre.math.gatech.edu/research/papers/BHT_SUB7.pdf.
