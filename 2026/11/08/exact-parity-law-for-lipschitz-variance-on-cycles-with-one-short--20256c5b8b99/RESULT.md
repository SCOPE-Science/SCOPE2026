# Exact parity law for Lipschitz variance on cycles with one shortened edge

## Finding
Let \(n\ge3\) be an integer and \(0<\lambda\le1\). Form the metric cycle \(C_n(\lambda)\) with \(n-1\) cyclic edges of length \(1\) and one distinguished edge of length \(\lambda\), using shortest-path distances. Give the \(n\) vertices uniform probability. Then the squared norm of the centered real Lipschitz-to-\(L^2\) inclusion is
\[
\boxed{\sup_{\operatorname{Lip}(f)\le1}\operatorname{Var}(f)=
\begin{cases}
\dfrac{(n^2-1)(n^2+3)}{48n^2},&n\text{ odd},\\[5pt]
\dfrac{n^2-4}{48}+\dfrac{\lambda^2}{4},&n\text{ even}.
\end{cases}}
\]
Thus shortening one cycle edge leaves the sharp variance exactly unchanged for odd cycles; for every even cycle the exact loss relative to the unit-edge case is \((1-\lambda^2)/4\), **independent of cycle size**. Explicit maximizing potentials are given in the proof. The statement does not claim a complete classification of all equality cases.

## Assumptions and scope
Vertices are labeled \(0,1,\dots,n-1\) in cyclic order. The exceptional edge joins \(n-1\) to \(0\); every other edge has length one. The edge constraints \(|f(i+1)-f(i)|\le\ell_i\) (indices modulo \(n\)) are equivalent to \(1\)-Lipschitz continuity for the associated shortest-path metric. Functions are real, and the measure assigns probability \(1/n\) to every vertex. The parameter is strictly positive; the limit \(\lambda\downarrow0\) is not asserted to be a metric on \(n\) distinct points. Primary classification: 46B20 (norms of metric Lipschitz function spaces and their centered Hilbert inclusions).

## Proof
**1. Increment polytope and its vertices.** Orient the cycle consecutively and set \(d_i=f(i+1)-f(i)\), with cyclic indexing. Then
\[
\sum_{i=0}^{n-1}d_i=0,\quad |d_i|\le1\ (i<n-1),\quad |d_{n-1}|\le\lambda.
\]
Conversely every such vector integrates to a potential, unique modulo constants. The quadratic objective \(\operatorname{Var}(f)\) is positive definite on the zero-sum increment hyperplane. Hence every maximizing increment vector is a vertex of the section of the coordinate box: if two coordinates are strictly within their bounds, their opposite perturbations preserve the constraint and strict convexity precludes a maximum. Therefore at least \(n-1\) edge bounds are tight.

For odd \(n=2m+1\), at the unit-edge point \(\lambda=1\), the \(2m\) fixed signs sum to an even integer. The remaining increment can lie in \([-1,1]\) only when it is zero. Each vertex therefore has \(m\) increments equal to \(+1\), \(m\) equal to \(-1\), and one zero. For even \(n=2m\) with \(0<\lambda<1\), the short edge cannot be free: fixing the other \(2m-1\) increments to unit signs would make its absolute value an odd positive integer, exceeding \(\lambda\). The short edge therefore equals \(\lambda\) or \(-\lambda\). Of the remaining \(2m-1\) edges, one is free and \(2m-2\) have signs. Their signed sum is even; requiring the remaining free increment to have absolute value at most one forces that sum to be zero. Consequently the full increment multiset is
\[
\{\underbrace{+1,\ldots,+1}_{m-1},\ \lambda,\ -\lambda,\ \underbrace{-1,\ldots,-1}_{m-1}\}.
\]
All permutations of this multiset satisfying the exceptional-coordinate placement are feasible vertices.

**2. The circle rearrangement bound.** We use the following finite-circle quadratic rearrangement fact. For a cyclic index set of size \(n\), a nonnegative vector \(x\), and a kernel \(K(r)\) strictly decreasing in cyclic distance \(r=0,\ldots,\lfloor n/2\rfloor\), the energy \(\sum_{i,j}x_ix_j K(\operatorname{dist}_{C_n}(i,j))\) is maximized over all permutations of the entries of \(x\) by putting them in decreasing order at positions \(0,1,-1,2,-2,\ldots\) (or its reflection/rotation). This standard one-dimensional circular polarization fact has a short finite verification: reflect the polygon across an axis through vertices or edge midpoints, pair each point with its mirror, and put the larger of each reflected pair on a chosen semicircle. For two paired orbits with representatives \(p,q\) in that semicircle, the change in the quadratic energy is
\[
[K(\operatorname{dist}(p,q))-K(\operatorname{dist}(p,Rq))]
\bigl(|(x_p-x_{Rp})(x_q-x_{Rq})|-(x_p-x_{Rp})(x_q-x_{Rq})\bigr)\ge0.
\]
Here \(R\) is the reflection, and points in one chosen semicircle are no farther apart than the corresponding crossed pair. The within-orbit terms stay unchanged. For completeness, make the termination argument precise. Number the sites by the preference order \(0,1,-1,2,-2,\ldots\), and give them distinct auxiliary scores \(q_i=-2\operatorname{dist}(i,0)+\epsilon\mathbf1_{\{i\text{ on the positive side}\}}\), where \(0<\epsilon<1\). Among the finitely many permutations that maximize the energy, choose one maximizing \(\sum_iq_ix_i\). For every reflection, choose its semicircle containing site zero; when the axis contains zero, choose the positive side. Every paired site on this semicircle has at least the auxiliary score of its reflected partner (strictly unless the pair is fixed). Thus polarizing cannot lower the energy and cannot lower the auxiliary sum, and improves the latter whenever a preferred site holds a smaller entry than its reflected mate. Now any two sites out of decreasing preference order are interchanged by a regular-polygon reflection; its preferred side contains the earlier site (the side nearer site zero, with the positive tie-break on the axis). An inversion would contradict maximality of the auxiliary sum. Hence the energy maximum has the required circular decreasing arrangement. This is the discrete circle analogue of the classical circular Riesz rearrangement principle. Neither integrality nor an assertion of uniqueness is needed.

To apply it, write \(f\) in terms of its zero-sum increments \(d\). The cycle Laplacian Green matrix is
\[
G_{ij}=\frac{n^2-1}{12n}-\frac{r(n-r)}{2n},\qquad
r=\operatorname{dist}_{C_n}(i,j).
\]
Direct multiplication by the cyclic Laplacian gives \(LG=I-\mathbf1\mathbf1^T/n\) and \(G\mathbf1=0\). On the zero-sum increment space, the variance of the integrated centered potential is exactly
\[
\operatorname{Var}(f)=\frac1n d^T Gd.
\]
Indeed the discrete derivative has Fourier multiplier \(e^{2\pi ik/n}-1\) and \(G\) is the inverse of its squared modulus on nonconstant modes; this identity also follows by integrating the increments and subtracting their mean. The Green kernel is strictly decreasing in cyclic distance. Choose a constant \(C\) sufficiently large that \(K=G+C\) is nonnegative. With \(x=d+\mathbf1\ge0\), one has \(d^TGd=x^TGx\) because \(G\mathbf1=0\). Adding \(C\) to the kernel changes the energy by \(C(\sum_i x_i)^2\), which is permutation invariant. Thus the rearrangement fact applies to any fixed multiset of increments.

**3. Odd cycles.** At \(\lambda=1\), rearrange the vertex increment multiset of step 1. A cyclic maximizer has \(m\) consecutive increments \(+1\), one zero increment, and \(m\) consecutive increments \(-1\) (possibly cyclically rotated). Integrating gives the \(2m+1\) heights \(0,1,\ldots,m,m-1,\ldots,1\), up to rotation and addition of a constant. Their exact variance is
\[
\frac{(n^2-1)(n^2+3)}{48n^2}.
\]
When \(0<\lambda<1\), the feasible Lipschitz set is contained in the unit-edge feasible set, so its spread cannot increase. Rotate the displayed unit-edge maximizer so that the zero increment lies on the short edge. It remains feasible for every positive \(\lambda\), proving the identical sharp value throughout the entire interval.

**4. Even cycles.** For \(0<\lambda<1\), step 1 gives the same increment multiset at every extremal vertex. Circular rearrangement maximizes its Green energy by the cyclic ordering
\[
\underbrace{+1,\ldots,+1}_{m-1},\ \lambda,\
\underbrace{-1,\ldots,-1}_{m-1},\ -\lambda.
\]
Rotate so that the last increment \(-\lambda\) is precisely the distinguished short edge. The resulting feasible heights are
\[
0,1,\ldots,m-1,\ m-1+\lambda,\ m-2+\lambda,\ldots,\lambda.
\]
Their mean is \((m-1+\lambda)/2\). Summing their squares and subtracting the squared mean gives
\[
\operatorname{Var}(f)=\frac{m^2-1}{12}+\frac{\lambda^2}{4}=
\frac{n^2-4}{48}+\frac{\lambda^2}{4}.
\]
Because the rearrangement dominates every extremal increment multiset permutation, this is the global maximum. At \(\lambda=1\), continuity of the feasible polytopes and of their maxima, or the same rearrangement applied to \(m\) positive and \(m\) negative unit increments, yields the same endpoint formula. The loss relative to \(\lambda=1\) is therefore \((1-\lambda^2)/4\), completing the proof.

## Verification
A standalone Python 3 exact-arithmetic checker (`verify.py`) enumerates all increment-polytope vertices by choosing one free coordinate and setting the other edge coordinates to their prescribed bounds, with the sum-zero constraint determining the free coordinate. It checks the complete formula and the explicit maximizing profile for all \(3\le n\le10\) at four rational parameter values \(1/5,1/2,4/5,1\). It also checks the distance-kernel inequalities used in reflection comparisons for orders \(3\) through \(30\). Run `python3 verify.py` in the same directory. The finite computations corroborate the proof; they do not establish its universal rearrangement step.

## Relationship to prior work
Addario-Berry, Janson, and McDiarmid's 2009 preprint studies graph Lipschitz spread, including graphs with random edge lengths, but does not supply the deterministic one-short-edge cycle formulas. The known exact uniform-cycle spread, also expressed as the centered facet-normal norm of the symmetric edge polytope, agrees with our specialization \(\lambda=1\); that endpoint is acknowledged as prior work. A published one-short-edge weighted-cycle result establishes an exact **Euclidean Banach--Mazur distortion** of the associated Lipschitz-free space. The distortion is an infimum over Euclidean structures, not the norm of the particular centered Lipschitz-to-uniform-vertex-\(L^2\) inclusion, and its parity laws do not imply the present variance formula. Another published weighted-cycle result determines when the **numerical index** equals one; it concerns a different extremal operator invariant. The new quantitative assertion is that under every positive shortening the odd-cycle spread is rigid while the even-cycle spread loses precisely \((1-\lambda^2)/4\), independently of its order.

## Limitations
The result assumes uniform vertex mass, precisely one shortened edge, real functions, and strictly positive edge lengths. It does not classify all maximizers, arbitrary weighted cycles, higher moments, or nonuniform vertex masses. The finite-circle rearrangement is the critical universal lemma; the verification code checks examples and finite polarization geometry rather than certifying the lemma for all sizes. Equivalent formulations in unindexed literature cannot be excluded by bibliographic searches alone.

## References
1. L. Addario-Berry, S. Janson, C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first public 2009-02-06; introduction and Sections 2–5.
2. *Cycle symmetric edge polytopes have a parity-split exact Euclidean inradius*, publicly accessible research result (2026), especially its explicit facet-normal variance extremizers for unweighted cycles and the complete endpoint formulas.
3. *Opposite parity laws for exact Hilbert distortion of one-edge weighted cycles*, publicly accessible research result (2026), Sections 1–5; exact Banach–Mazur distance for the same weighted-cycle metric family.
4. *Numerical-index-one rigidity for weighted cycles and positive cube sections*, publicly accessible research result (2026), especially its cycle-increment cube section and numerical-index criterion.
5. A. Baernstein II, *Convolution and rearrangement on circle*, Complex Variables, Theory and Application 12 (1989), 33–37, DOI 10.1080/17476938908814351 (classical circular rearrangement background; the exact discrete step is detailed above).
