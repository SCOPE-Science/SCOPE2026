# Weighted longest chains determine all minimum-width directions of order polytopes

## Finding
Let \(P\) be a nonempty finite poset and let \(s_p>0\) be a coordinate scale for each \(p\in P\). In the standard Euclidean coordinate space, put
\[
K(P,s)=\operatorname{diag}(s_p)\mathcal O(P),\qquad
H(P,s)=\max_{C\text{ a chain of }P}\sum_{p\in C}s_p^{-2}.
\]
Then the minimum Euclidean directional width of \(K(P,s)\) is exactly
\[
\boxed{\operatorname{width}_{\min}(K(P,s))=H(P,s)^{-1/2}.}
\]
Moreover, **every** minimizing Euclidean unit normal is obtained by choosing a chain \(C=(c_1<\dots<c_k)\) attaining \(H(P,s)\), choosing \(\sigma\in\{-1,1\}\), and setting
\[
\boxed{v_{c_j}=\frac{\sigma(-1)^j}{s_{c_j}\sqrt{H(P,s)}}\quad(1\le j\le k),\qquad v_p=0\quad(p\notin C).}
\]
The two choices of \(\sigma\) give opposite normal orientations, and distinct maximizing chains give distinct support sets. Thus there are exactly twice as many oriented minimizing normals as maximum-weight chains for the positive weights \(s_p^{-2}\). In particular, with all \(s_p=1\), the minimum width is the reciprocal square root of the poset height, and its minimizing unit normals are precisely the alternating-sign indicators of longest chains, normalized by the square root of their length.

## Assumptions and scope
The order polytope uses the convention
\[
\mathcal O(P)=\{x\in\mathbb R^P:0\le x_p\le1\text{ for all }p,\quad x_p\le x_q\text{ whenever }p<q\}.
\]
A filter (upper set) is a subset \(F\subseteq P\) such that \(p\in F\), \(p\le q\) imply \(q\in F\). The vertices of \(\mathcal O(P)\) are the indicators \(\mathbf1_F\) of filters. A chain is a subset of pairwise comparable elements, including singletons. All widths refer to the ambient Euclidean metric after the displayed positive diagonal scaling, and to unit normal vectors \(v\): \(W_K(v)=\max_{y\in K}\langle v,y\rangle-\min_{y\in K}\langle v,y\rangle\). The result applies to every finite poset, without rankedness, connectedness, or any assumption that its longest chains have the same size.

## Proof
**1. Signed antichain cubes inside the difference body.** Fix an arbitrary antichain \(A\subseteq P\) and a sign pattern \(\varepsilon_p\in\{-1,1\}\) on \(A\). Partition it into \(A_+\) and \(A_-\). Let \(U(A)=\{q\in P: a<q\text{ for some }a\in A\}\) be the strict upper closure. Both \(F=U(A)\cup A_+\) and \(G=U(A)\cup A_-\) are filters, and
\[
\mathbf1_F-\mathbf1_G=\sum_{p\in A}\varepsilon_p e_p.
\]
Consequently, for every nonzero linear functional \(u\in\mathbb R^P\), the (unscaled) order-polytope width satisfies
\[
W_{\mathcal O(P)}(u)\ge\max_{A\text{ antichain}}\sum_{p\in A}|u_p|.
\tag{1}
\]
This is a statement about the full difference body, not just a projection onto the antichain coordinates.

**2. The antichain-constraint decomposition.** We use the following elementary consequence of Dilworth's theorem: if \(z_p\ge0\) and \(\sum_{p\in A}z_p\le1\) for every antichain, then \(z\) is a convex combination of indicator vectors of chains, including the empty chain. To see this without a polyhedral integrality assumption, first suppose all \(z_p\) have denominator \(m\). Replace each \(p\) by \(m z_p\) mutually incomparable copies, ordered between different copy blocks exactly as their original elements are ordered. The largest antichain of this blown-up poset has cardinality at most \(m\), since it projects to an antichain of \(P\). Dilworth's theorem partitions its elements into at most \(m\) chains. After adding empty chains if necessary and projecting back, their indicator vectors average to \(z\). For general real \(z\), apply this argument to \(\lfloor m z_p\rfloor/m\) and pass to the limit; the convex hull of the finitely many chain indicators is closed.

**3. Sharp bound.** Let \(v\) be any Euclidean unit normal to \(K(P,s)\), write \(u_p=s_pv_p\), and let \(w=W_{K(P,s)}(v)=W_{\mathcal O(P)}(u)>0\). By (1), \(z_p=|u_p|/w\) satisfies every antichain constraint. Writing \(z=\sum_C\lambda_C\mathbf1_C\) with \(\lambda_C\ge0\), \(\sum_C\lambda_C=1\), and using \(0\le z_p\le1\), gives
\[
1=\sum_p\frac{u_p^2}{s_p^2}
=w^2\sum_p\frac{z_p^2}{s_p^2}
\le w^2\sum_p\frac{z_p}{s_p^2}
=w^2\sum_C\lambda_C\sum_{p\in C}s_p^{-2}
\le w^2 H(P,s).
\tag{2}
\]
Hence \(w\ge H(P,s)^{-1/2}\) for every Euclidean unit normal.

**4. Attainment.** Choose a chain \(C=(c_1<\dots<c_k)\) maximizing \(\sum_{p\in C}s_p^{-2}=H(P,s)\). Put \(u_{c_j}=\sigma(-1)^j/\sqrt{H(P,s)}\), and \(u_p=0\) off \(C\), then set \(v_p=u_p/s_p\). This normal is Euclidean unit by definition of \(H(P,s)\). Every filter meets \(C\) in a suffix, and every suffix of \(C\) is realized by some filter (take the upward closure of its least element, with the empty filter for the empty suffix). The alternating signs make all suffix sums lie in a two-point set at distance \(H(P,s)^{-1/2}\). Therefore \(W_{K(P,s)}(v)=H(P,s)^{-1/2}\).

**5. All equality cases.** If \(v\) is any minimizing unit normal, equality holds throughout (2). Positivity of the scale factors and equality of \(\sum z_p^2/s_p^2\le\sum z_p/s_p^2\) force \(z_p\in\{0,1\}\) for every \(p\). The antichain constraints then say that \(\{p:z_p=1\}\) is a chain \(C\). Equality at the last step of (2) forces \(\sum_{p\in C}s_p^{-2}=H(P,s)\). Thus \(|u_p|=w\) at every element of that chain and \(u_p=0\) elsewhere. Since the attainable filter restrictions to \(C\) are all suffixes, the signed unit-step suffix-sum walk must have range exactly one. This occurs if and only if consecutive signs alternate; any two consecutive equal signs would give two consecutive steps in the same direction and range at least two. The displayed normals are therefore exhaustive.

## Verification
The accompanying standalone `verify.py` uses exact integer arithmetic, with no dependencies outside Python's standard library. It enumerates all transitively closed relations on labeled ground sets of up to five elements that are consistent with one fixed linear extension, all upper filters, all chains, and all normals with entries in \(\{-1,0,1\}\), for three positive integer inverse-square weight profiles. It checks (2) after squaring, constructs every predicted normal, and checks that every grid equality case is one of the predicted alternating-chain normals. The execution completed successfully with `POSET_WEIGHTED_WIDTH_CHECKS_PASSED poset_weight_profiles= 1221 filter_sets= 15690 heaviest_chains= 1789`. Finite enumeration is not the proof of the result for arbitrary posets, positive real scales, or real normal vectors; the preceding argument supplies those quantifiers.

## Relationship to prior work
Stanley's order-polytope vertex characterization and Dilworth's chain-partition theorem are used as established foundations. Freij-Hollanti and Lundström (2023) and Ahmad, Fourier, and Joswig (2023) study face vectors and combinatorial comparisons for order and chain polytopes, rather than their minimum Euclidean directional width. Mori (2023) treats simplicial faces of these polytopes. Har-Peled and Robson (2023) calculate the minimum width of regular simplices, which is not directly applicable to generally nonregular order polytopes or to positive coordinate dilations. A prior exact minimum-width result for stable-set polytopes in graphs with equal clique and chromatic numbers gives a superficially similar unweighted value for comparability graphs, but it concerns a different canonical polytope and constant-sign clique normals; the order-polytope minimizers here alternate along chains. No isometric identification that would imply this theorem is established by those works. The support bound (1), weighted chain selection, and complete alternating-normal equality classification are the present assertions.

## Limitations
The theorem is restricted to finite posets and strictly positive diagonal coordinate scales, not arbitrary oblique affine images. It identifies the minimum width and all minimum-width normals but not the entire width distribution. Novelty is assessed from accessible literature and specified prior-record comparisons; historical priority beyond that corpus is not independently certified. The finite exact tests do not constitute exhaustive verification of all real scales or arbitrary poset sizes.

## References
1. R. P. Stanley, *Two poset polytopes*, Discrete & Computational Geometry **1** (1986), 9–23. DOI: 10.1007/BF02187680.
2. R. P. Dilworth, *A decomposition theorem for partially ordered sets*, Annals of Mathematics **51** (1950), 161–166.
3. R. Freij-Hollanti and T. Lundström, *f-vector inequalities for order and chain polytopes*, arXiv:2312.13890 (first posted 2023-12-21).
4. I. Ahmad, G. Fourier, and M. Joswig, *Order and chain polytopes of maximal ranked posets*, arXiv:2309.01626 (first posted 2023-09-04).
5. A. Mori, *Simplex faces of order and chain polytopes*, arXiv:2307.08447 (first posted 2023-07-17).
6. S. Har-Peled and E. W. Robson, *On the Width of the Regular n-Simplex*, arXiv:2301.02616 (first posted 2023-01-06).
