# A sharp three-leaf bridge-deletion transition for Laplacian spectral-width design

## Finding
For every integer \(m\ge1\), form the balanced double-star tree with two hubs, \(m\) distinct pendant leaves attached to each hub, and a single bridge between the hubs. Assign arbitrary nonnegative conductances independently to the \(2m+1\) edges, with their sum equal to one. Write \(L\) for the resulting unnormalized weighted graph Laplacian, list its \(2m+2\) eigenvalues in nondecreasing order as \(0=\lambda_1\le\lambda_2\le\cdots\le\lambda_{2m+2}\), and set the spectral width \(W=\lambda_{2m+2}-\lambda_2\).

**The globally optimal allocation is unique, even without assuming equal conductances on symmetric edges.** Its common pendant conductance \(a_m\) and its bridge conductance \(b_m\) are
\[
(a_m,b_m)=
\begin{cases}
\left(\dfrac{6m+2}{9m^2+10m+1},\dfrac{-3m^2+6m+1}{9m^2+10m+1}\right),&m=1,2,\\[5pt]
\left(\dfrac1{2m},0\right),&m\ge3.
\end{cases}
\]
The exact minimum is
\[
\min W=
\begin{cases}
\sqrt{4/5},&m=1,\\
\sqrt{32/57},&m=2,\\
\dfrac{m+1}{2m},&m\ge3.
\end{cases}
\]
In particular, with two leaves per hub the optimal bridge has conductance \(1/57\), but with three or more leaves per hub **every minimizer deletes the bridge**. Under the additional requirement that all conductances be strictly positive, the same number is only an unattained infimum for \(m\ge3\).

## Assumptions and scope
The underlying potential graph is the unweighted, undirected balanced double star with \(2m+2\) distinct vertices. Conductances may be zero, so connectivity of the conductance support is *not* imposed. The budget is \(\sum_{e}w_e=1\). The Laplacian is \(L=\sum_{\{u,v\}}w_{uv}(e_u-e_v)(e_u-e_v)^\mathsf{T}\). The objective is the difference of the **largest** and the **second-smallest** eigenvalue, not a condition number, not the largest-to-smallest-positive eigenvalue ratio, and not the spectral width after excluding all zeros. All statements apply for every integer \(m\ge1\), including when the optimizer is disconnected.

## Proof
**1. Global symmetry reduction.** On real symmetric matrices, the largest eigenvalue is convex. Because every Laplacian kills the all-ones vector, its second-smallest eigenvalue equals the minimum of \(x^\mathsf{T}Lx\) over unit vectors \(x\perp\mathbf1\), hence is concave in the edge conductances. Therefore \(W\) is convex in the conductance vector. Average an arbitrary allocation over permutations of the \(m\) leaves at each hub and the interchange of the two hubs. The total conductance and bridge conductance do not change, and the resulting width cannot increase. Thus at least one optimal allocation has all pendant conductances equal to \(a\), bridge conductance \(b\), and \(2ma+b=1\).

**2. All symmetric eigenvalues.** For \(a,b>0\), the leaf-difference subspaces have eigenvalue \(a\), with multiplicity \(2(m-1)\) (empty if \(m=1\)). The hub-symmetric sector has eigenvalues \(0\) and \((m+1)a\). In the hub-antisymmetric sector, writing the common leaf and hub amplitudes as \(\ell,h\) on one side and \(-\ell,-h\) on the other yields the characteristic polynomial
\[
\lambda^2-((m+1)a+2b)\lambda+2ab.
\]
Its roots \(\lambda_-<\lambda_+\) satisfy \(0<\lambda_-<a\) and \(\lambda_+>(m+1)a\): evaluate the polynomial at \(0\), \(a\), and \((m+1)a\), obtaining \(2ab>0\), \(-ma^2<0\), and \(-2mab<0\), respectively. Thus \(\lambda_2=\lambda_-\), \(\lambda_{2m+2}=\lambda_+\), and
\[
W(a,b)=\sqrt{((m+1)a+2b)^2-8ab}.
\]
The formula extends continuously to \(a=0\) or \(b=0\), where the endpoint eigenvalue descriptions are checked directly (including the extra zero eigenvalue when \(b=0\)).

**3. Exact global symmetric optimum.** Substitute \(b=1-2ma\), with \(0\le a\le 1/(2m)\). The squared width is the strictly convex quadratic
\[
W(a,1-2ma)^2=4-(12m+4)a+(9m^2+10m+1)a^2.
\]
Its unconstrained minimizer is \(a_0=(6m+2)/(9m^2+10m+1)\). The corresponding bridge is \(b_0=(-3m^2+6m+1)/(9m^2+10m+1)\). Since \(b_0>0\) holds for integer \(m\ge1\) **exactly when** \(m=1\) or \(m=2\), the unique constrained minimum is \((a_0,b_0)\) for these two cases, and the boundary point \((1/(2m),0)\) for every \(m\ge3\). Substitution gives the three stated exact minimum values.

**4. Uniqueness without symmetry.** Let an arbitrary allocation be globally minimizing and average it over the full automorphism group. The averaged allocation must be the unique symmetric optimum from step 3. For \(m\ge3\), the bridge is unchanged by averaging; hence its conductance in the original allocation is zero. Let \(S_1,S_2\) be the total pendant conductances in the two disconnected stars. The vector with hub entry \(m\) and every leaf entry \(-1\) gives the Rayleigh lower bound \(\lambda_{\max}\ge(m+1)S_j/m\) separately on each star. Since \(S_1+S_2=1\), any optimizer must have \(S_1=S_2=1/2\). Equality in the bound forces that vector to be an eigenvector on each star; the leaf eigenvector equations then force every leaf conductance to be identical. Thus the boundary optimizer is unique.

For \(m=1,2\), write \(L_0\) for the averaged optimal Laplacian and \(L\) for an original optimal Laplacian. Symmetry averaging and the separate convexity/concavity inequalities imply \(\lambda_{\max}(L)=\lambda_{\max}(L_0)\). The simple top eigenvector of \(L_0\) has equal nonzero leaf coordinates \(\ell\) on each hub's side, opposite signs between sides, and hub coordinates \(h\) and \(-h\), with \(\ell\ne h\). The squared edge differences of this vector are constant within each pendant orbit and it changes only by sign under swapping the hubs. Therefore its Rayleigh quotient is the same for \(L\) and \(L_0\), equal to their common top eigenvalue; it must also be a top eigenvector of \(L\). Each original leaf equation now reads \(w_j(\ell-h)=\lambda_{\max}\ell\) (up to a common sign), forcing every pendant conductance \(w_j\) to have the same value. The bridge is already fixed by averaging. This proves full uniqueness.

## Verification
Run `python verify.py` after installing the dependencies in `requirements.txt`. The script checks the exact rational minimizers and all integer dimension formulas for \(1\le m\le28\), symbolically verifies the squared-width identity, compares the closed-form spectrum to direct full-matrix numerical diagonalization, and tests random asymmetric allocations and symmetry averages. A recorded replay passed 1550 assertions. These finite tests are diagnostics; the proof above covers every integer \(m\ge1\) and every admissible real conductance vector.

## Relationship to prior work
Göring, Helmberg and Reiss (2011 preprint, 2013 journal article) introduced the general weighted-Laplacian spectral-width optimization and showed that its optimal conductance support can be disconnected, including a different example in their Example 27. That general disconnection phenomenon is not new. Boyd's graph-Laplacian eigenvalue optimization overview supplies broader convex-design context. Fan, Xu, Wang and Liang (2008) treat Laplacian spread of unweighted trees and give the characteristic-polynomial structure of unweighted double stars, but do not solve the independent-conductance, fixed-budget optimization here. The claimed contribution is the **complete closed-form optimal design and uniqueness** on the balanced double-star family, with the sharp first bridge-deletion threshold at three leaves per hub. The general convex or unweighted structural results do not state these quantitative conclusions.

## Limitations
The theorem is about balanced double stars with a sum-of-conductances budget. It does not determine all unequal-arm double stars, edge-price variants, other eigenvalue objectives, or floating-point performance. Allowing zero conductances is essential for the claimed attained optimum when \(m\ge3\). This is not a claim of exhaustive bibliographic uniqueness; equivalent results may exist in unindexed literature.

## References
1. F. Göring, C. Helmberg and S. Reiss, *On Minimizing the Spectral Width of Graph Laplacians and Associated Graph Realizations*, TU Chemnitz Preprint 2011-4 (publicly catalogued February 2011), especially introduction, Observations 9 and 22 and Example 27. https://www.tu-chemnitz.de/mathematik/preprint/2011/PREPRINT_04.pdf ; journal DOI: https://doi.org/10.1137/110859658
2. Y.-Z. Fan, J. Xu, Y. Wang and D. Liang, *The Laplacian Spread of a Tree*, Discrete Mathematics and Theoretical Computer Science 10(1), 79–86 (2008), especially Sections 2–3. https://dmtcs.episciences.org/volumes-full/83/83.pdf
3. S. Boyd, *Convex Optimization of Graph Laplacian Eigenvalues*, International Congress of Mathematicians lecture/chapter, EMS Press, published online May 15, 2007, DOI https://doi.org/10.4171/022-3/63 . https://ems.press/books/standalone/24/555
