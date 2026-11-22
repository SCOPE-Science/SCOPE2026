# An exact integral barcode for dimension-delayed lower-star filtrations on simplicial cones

## Finding
Let \(L\) be any finite simplicial complex, let \(a\) be a new vertex, and write \(K=a*L\) for its simplicial cone. Let \(w:V(K)\to\mathbb R\) satisfy \(w(a)\le w(v)\) for every \(v\in V(L)\). Let \(h(0)=0\) and let \(h(0)<h(1)<\cdots<h(\dim K)\) be any strictly increasing sequence of real numbers. Filter the nonempty simplices of \(K\) by
\[
F(\tau)=\max_{v\in\tau}w(v)+h(\dim\tau),\qquad
K_t=\{\tau\in K:\tau\ne\varnothing,\ F(\tau)\le t\}.
\]
For ordinary homology with **integer coefficients**, the filtered cellular chain complex admits an explicit filtration-preserving integral decomposition. Its homology persistence module is
\[
H_j(K_\bullet;\mathbb Z)\ \cong\
\begin{cases}
\mathbb Z_{[w(a),\infty)}\ \oplus\ \displaystyle\bigoplus_{\substack{\sigma\in L,\ \sigma\ne\varnothing\\\dim\sigma=0}}
\mathbb Z_{[b_\sigma,d_\sigma)},&j=0,\\[3pt]
\displaystyle\bigoplus_{\substack{\sigma\in L,\ \sigma\ne\varnothing\\\dim\sigma=j}}
\mathbb Z_{[b_\sigma,d_\sigma)},&j\ge1,
\end{cases}
\]
where \(b_\sigma=\max_{v\in\sigma}w(v)+h(\dim\sigma)\) and \(d_\sigma=\max_{v\in\sigma}w(v)+h(\dim\sigma+1)\). Here \(\mathbb Z_I\) denotes the integral interval persistence module supported on \(I\), with identity transition maps inside \(I\) and zero maps otherwise. Every finite interval has strictly positive length \(h(j+1)-h(j)\) in degree \(j\), independent of the weights and of the topology of \(L\).

In particular, the \(\varepsilon\)-lower-star filtration, \(h(j)=j\varepsilon\) for \(\varepsilon>0\), has exactly one interval of length \(\varepsilon\) in degree \(j\) for **every \(j\)-simplex of the base \(L\)**, and one infinite degree-zero interval. If \(L\) is a full simplex on \(m\) vertices, there are \(\binom{m}{j+1}\) degree-\(j\) finite intervals, totaling \(2^m-1\) finite intervals on the contractible cone.

## Assumptions and scope
All complexes are abstract, finite, and have ordinary oriented simplicial chains; the empty simplex is excluded from unreduced chain groups. The base \(L\) can be disconnected, nonpure, or empty. For the empty base, \(K\) consists only of the apex and the formula reduces to its infinite degree-zero class. Vertex weights may tie. The cone apex must be a global minimum of \(w\). Dimension offsets are strictly increasing and normalized by \(h(0)=0\); adding a constant to every offset merely translates all birth and death times. The result concerns the **whole** complex \(K\), not a truncation of its dimension.

## Proof
Fix a total vertex order with \(a\) first. For every nonempty face \(\sigma=[v_0,\ldots,v_j]\) of \(L\), let \(u_\sigma=[a,v_0,\ldots,v_j]\in C_{j+1}(K;\mathbb Z)\) and \(z_\sigma=\partial u_\sigma\in C_j(K;\mathbb Z)\). In degree zero also retain \([a]\). The simplicial boundary formula is
\[
z_\sigma=[v_0,\ldots,v_j]+\sum_{i=0}^{j}(-1)^{i+1}[a,v_0,\ldots,\widehat v_i,\ldots,v_j],
\]
with the singleton convention \(z_{[v]}=[v]-[a]\). Each proper-face cone term has the same dimension as \(\sigma\), so the global-minimum assumption gives
\[
F(\{a\}\cup(\sigma\setminus\{v_i\}))
=\max_{v\in\sigma\setminus\{v_i\}}w(v)+h(j)
\le\max_{v\in\sigma}w(v)+h(j)=F(\sigma).
\]
For a singleton, the same assertion is \(F(\{a\})\le F(\{v\})\). Thus \(z_\sigma\) enters **exactly** at \(b_\sigma=F(\sigma)\): its original face \([v_0,\ldots,v_j]\) has coefficient \(+1\), and all other terms have filtration at most \(b_\sigma\).

For each degree, replace every basis simplex \([\sigma]\) not containing \(a\) with \(z_\sigma\), while keeping all simplices \(u_\tau\) containing \(a\) (including \([a]\)). This is a triangular integral matrix with diagonal entries \(+1\), hence a unimodular change of basis. It is filtration preserving in **both directions**: the extra cone terms in \(z_\sigma\) are no later than \(\sigma\), and conversely \(\sigma=z_\sigma-\sum \text{(those cone terms)}\) also uses nothing later than \(F(\sigma)\). Every \(u_\sigma\) has grade
\[
F(u_\sigma)=\max_{v\in\sigma}w(v)+h(j+1)=d_\sigma,
\]
since \(w(a)\le w(v)\). The new boundary matrix has only the blocks \(\partial u_\sigma=z_\sigma\), \(\partial z_\sigma=0\), and \(\partial[a]=0\). This is a **direct sum of free, two-term integral filtered complexes** (one per nonempty face of \(L\)) and the one-term essential apex complex. At every parameter \(t\), the summand for \(\sigma\) has either no generators, only the cycle \(z_\sigma\), or both \(z_\sigma\) and its integral primitive filling \(u_\sigma\). Their nontrivial homology therefore persists precisely on \([b_\sigma,d_\sigma)\), and all inclusion maps preserve this splitting. No extension, hidden integral torsion, or higher differential remains. This proves the formula over \(\mathbb Z\), and therefore over every coefficient field.

## Verification
An independent ordinary simplicial boundary-matrix reduction in `verify_cone.py` constructs random finite simplicial bases, their cones, arbitrary tied vertex weights with a minimum apex, and independently chosen strictly increasing dimension delays. Across 315 weighted cones on 2 to 8 vertices and coefficient primes \(2,3,5\), it recomputed **945 full persistence barcodes**, each agreeing exactly with the predicted multiset of intervals. The checker does not use the chain-basis construction in the proof. This finite testing is a consistency check, not the proof of the all-complex integral statement.

A sharp boundary is the apex-minimum hypothesis. For the single edge \(K=a*\{v\}\) with \(w(a)=5\), \(w(v)=0\), and \(h(1)=1\), the actual degree-zero persistence has the essential bar born at zero and a finite bar \([5,6)\), rather than the minimum-apex prediction of essential birth at five and finite interval \([0,1)\).

## Relationship to prior work
Abaa and Islambekov introduced the \(\varepsilon\)-lower-star filtration as \(F(\sigma)=\max_{v\in\sigma}w(v)+\varepsilon\dim\sigma\), proved its monotonicity and stability properties, and illustrated transient cycles in individual graph examples. Their publicly accessible exposition does not provide this all-weight, all-dimension **integral barcode of every simplicial cone**, nor the arbitrary increasing-delay extension. The earliest verified public release of that paper is the Preprints.org posting dated 16 September 2026; the later arXiv submission of 6 November 2026 is not used as the first-public date.

Chachólski, Giunti, Jin, and Landi developed general interval-sphere decompositions and algorithms for filtered chain complexes. Those generic algorithms explain why filtered reductions are possible, but they do not state the explicit, base-face-indexed formula for the newly proposed delayed lower-star filtration. In this result, the explicit integral change of basis provides the full calculation without barcode reduction.

For example, when all weights vanish, the cone over a four-cycle plus an isolated vertex and the cone over a five-vertex path have identical delayed lower-star barcodes (five degree-zero finite bars and four degree-one finite bars), although the former base has a nonzero first homology class and the latter base is a tree. Both bases are flag complexes, so these are also concrete clique-complex examples with a dominating vertex.

## Limitations
The exact formula requires a globally minimum cone apex and a genuine full simplicial cone, and it does not assert the same barcode for a merely contractible or conelike-looking complex. It classifies ordinary homology persistence, not the homotopy persistence system or filtrations based on \(L_p\) or softmax. The matched interval decomposition over integers is an explicit special property of this family, not a general assertion that arbitrary integral persistence modules split into intervals. The literature search cannot exclude all unindexed equivalents; independent mathematical audit has not been performed.

## References
1. I. Abaa and U. Islambekov, *Beyond the Lower-Star Filtration: Alternative Filtration Methods for Persistent Homology*. First public preprint 16 September 2026, https://www.preprints.org/manuscript/202609.1332 . Later arXiv version: https://arxiv.org/abs/2611.08833 .
2. W. Chachólski, B. Giunti, A. Jin, and C. Landi, *Decomposing filtered chain complexes: Geometry behind barcoding algorithms*, Computational Geometry 109 (2023), article 101938; https://doi.org/10.1016/j.comgeo.2022.101938 ; open preprint https://arxiv.org/abs/2012.01033 .
3. J. Leygonie and G. Henselman-Petrusek, *Algorithmic Reconstruction of the Fiber of Persistent Homology on Cell Complexes*, https://arxiv.org/abs/2110.14676 (general filtration inverse-problem context).
