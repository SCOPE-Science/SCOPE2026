# Complete natural-basis Cheeger spectra of a rank-two evolution-algebra family

## Finding
For each integer \(n\ge3\), let \(E_n\) be the real evolution algebra with natural basis \(B=(e_1,\ldots,e_n)\), pairwise mixed products \(e_i e_j=0\) for \(i\ne j\), and squares
\[
 e_1^2=z+e_1,\qquad e_i^2=z\ (2\le i\le n),\qquad z=\sum_{j=1}^n e_j.
\]
Its square \(E_n^2\) has dimension exactly two and \(\operatorname{Ann}(E_n)=0\). For any natural basis \(F\), let \(\Gamma(E_n,F)\) be the simple undirected graph joining distinct indices whenever at least one of the corresponding two off-diagonal structure coefficients is nonzero. Set \(m=\lfloor n/2\rfloor\). **The complete list, up to graph isomorphism, of graphs over all real natural bases** is
\[
  \left\{K_s\vee\overline K_{n-s}:2\le s\le n\right\}.
\]
Here \(\vee\) denotes graph join, so the graph has a clique of \(s\) vertices adjacent to all others and an independent set of \(n-s\) vertices. Every listed graph occurs. Moreover, the full set of attainable edge Cheeger constants is
\[
 \left\{\left\lceil\frac n2\right\rceil-
   \frac{\left\lfloor (n-s)^2/4\right\rfloor}{\left\lfloor n/2\right\rfloor}
   :2\le s\le n\right\},
\]
where \(h(\Gamma)=\min_{\varnothing\ne W\subseteq V,\ |W|\le n/2}|\partial W|/|W|\). Thus the exact basis-independent extrema are
\[
 \inf_F h(E_n,F)=\begin{cases}2&n\text{ odd},\\2-2/n&n\text{ even},\end{cases}
 \qquad \sup_F h(E_n,F)=\left\lceil\frac n2\right\rceil.
\]
For \(n\ge4\) the Cheeger constant depends on the natural basis, despite the algebra having trivial annihilator. The ratio of largest to smallest attainable Cheeger constants is unbounded with \(n\).

## Assumptions and scope
The field is \(\mathbb R\) and the graph convention and unnormalized edge Cheeger constant are exactly those of Giacomelli, Definition 3.1 and Equation (1) (arXiv:2605.12672v2). Loops are discarded; opposite arcs are collapsed to one undirected edge. The strict positive-definiteness of the standard Euclidean dot product is essential to the classification of natural bases. The algebra is not assumed associative or perfect.

## Proof
**Algebraic rank and natural bases.** On the coordinate space of \(B\), the multiplication is
\[
 uv=\langle u,v\rangle z+u_1v_1e_1.
\]
Because \(z\) and \(e_1\) are linearly independent, \(E_n^2=\operatorname{span}(z,e_1)\) has dimension two. Every \(e_i^2\) is nonzero, so if \(xE_n=0\), then \(xe_i=x_i e_i^2=0\) for all \(i\), implying \(x=0\).

Let \(F=(f_1,\ldots,f_n)\) be any natural basis, relabeled if necessary. For distinct \(i,j\), the equality \(f_i f_j=0\) is equivalent to both \(\langle f_i,f_j\rangle=0\) and \((f_i)_1(f_j)_1=0\). At most one vector of \(F\) has nonzero first coordinate. Invertibility forces exactly one; call it \(f_1\). Every other \(f_i\) lies in \(H=\operatorname{span}(e_2,\ldots,e_n)\) and together these \(n-1\) vectors form a basis of \(H\). Orthogonality then forces \(f_1\in H^\perp=\mathbb Re_1\); hence \(f_1=a e_1\) for nonzero \(a\), and \((f_2,\ldots,f_n)\) is an arbitrary nonzero pairwise-orthogonal real basis of \(H\).

Write \(w=\sum_{i=2}^ne_i=\sum_{i=2}^n c_i f_i\). At least one \(c_i\) is nonzero. With \(b_i=\langle f_i,f_i\rangle>0\), the squares are
\[
 f_1^2=a^2(2a^{-1}f_1+w),\qquad f_i^2=b_i(a^{-1}f_1+w)\quad (i\ge2).
\]
Thus vertex \(1\) is adjacent to every other vertex, and two distinct vertices \(i,j\ge2\) are adjacent exactly when \(c_i\ne0\) or \(c_j\ne0\). If \(k\) of the \(c_i\) are nonzero, the graph is \(K_{k+1}\vee\overline K_{n-k-1}\), with \(1\le k\le n-1\).

Conversely, for each \(k\) in that interval, take an orthogonal basis of the Euclidean space \(H\) in which the fixed nonzero vector \(w\) has precisely \(k\) nonzero coordinates. Such a basis exists because the real orthogonal group acts transitively on the sphere: an orthogonal transformation can carry \(w\) to a vector with exactly \(k\) equal nonzero components and the same norm. Adjoin \(e_1\). The resulting natural basis realizes \(K_{k+1}\vee\overline K_{n-k-1}\).

**Exact Cheeger constant of every occurring graph.** Put \(s=k+1\), \(t=n-s\), and \(G=K_s\vee\overline K_t\). If a nonempty vertex subset \(W\) has size \(w\le m\) and contains \(a\) clique vertices and \(b\) independent vertices (so \(w=a+b\)), then
\[
 |\partial W|=a(n-w)+b(s-a)=w(n-w)-b(t-b).
\]
There is always a subset of size \(m\) whose boundary-to-size ratio is no larger than that of \(W\). To see this, if an independent vertex lies outside \(W\), add it. The boundary increases by \(s-2a\), whereas the old ratio satisfies
\[
  \frac{|\partial W|}{w}-(s-2a)=\frac{a(t+a)}w\ge0.
\]
Therefore adding that vertex does not increase the ratio. If all independent vertices already belong to \(W\), add an outside clique vertex. In this case \(|\partial W|/w=n-w\), and the boundary increases by \(n-1-2w\le n-w\), so the ratio again does not increase. Repeat until the size is \(m\).

For \(w=m\), minimizing the boundary is equivalent to maximizing \(b(t-b)\) over integers with \(\max(0,m-s)\le b\le\min(m,t)\). Because \(s\ge2\), this interval contains an integer nearest to \(t/2\). Consequently its maximum is \(\lfloor t^2/4\rfloor\), giving
\[
 h(G)=n-m-\frac{\lfloor t^2/4\rfloor}{m}
 =\left\lceil\frac n2\right\rceil-\frac{\lfloor(n-s)^2/4\rfloor}{\lfloor n/2\rfloor}.
\]
The expression is nondecreasing as \(s\) increases. At \(s=n\) it equals \(\lceil n/2\rceil\). At \(s=2\), substituting \(n=2m\) or \(n=2m+1\) yields respectively \(2-1/m=2-2/n\) or \(2\), completing the proof.

**Explicit integral witnesses for the extrema.** The original basis \(B\) has graph \(K_n\). For the lower endpoint, take \(f_1=e_1\), \(f_2=w=\sum_{j=2}^n e_j\), and for \(2\le r\le n-1\) take
\[
 f_{r+1}=\sum_{j=2}^{r}e_j-(r-1)e_{r+1}.
\]
These \(n-1\) vectors in \(H\) are pairwise orthogonal, and \(w=f_2\); the graph is \(K_2\vee\overline K_{n-2}\). The exact Cheeger formula therefore realizes both endpoints even over \(\mathbb Q\) (though the full intermediate-spectrum realization is asserted only over \(\mathbb R\)).

## Verification
The standalone standard-library Python checker `checks/verify.py` constructs both integer natural bases for every \(3\le n\le10\), checks exact multiplication and orthogonality, reconstructs their structure-matrix graph supports, exhausts every nontrivial cut for those graphs and all intermediate complete-split graphs, and checks the closed Cheeger formula and both extrema. Run `python3 checks/verify.py`. Recorded output is `checks/output.txt`. The proof above, not the bounded calculation, supplies the claims for all dimensions and all real natural bases.

## Relationship to prior work
Giacomelli (2026), arXiv:2605.12672v2, Definition 3.1 and Theorem 3.8 defines precisely this Cheeger invariant and proves natural-basis independence for nonsingular evolution algebras. Problem 8.3 explicitly asks what happens for singular evolution algebras. The present theorem gives a rank-two, annihilator-zero infinite family with a complete graph spectrum and an exact basis-optimization invariant, rather than a single isolated example. Elduque and Labra (2013, 2015) already show in Examples 2.4–2.5 that singular evolution algebra graphs can depend on the basis, and establish basis-independent connectedness when the annihilator is zero. They do not give the rank-two complete-split graph realization or quantitative Cheeger spectrum claimed here. The 2026 evolution-algebra survey (Question 14) similarly discusses nonmonomial changes of natural basis and the broader classification problem. The previously known rank-one graph-support classifications do not entail this rank-two theorem.

## Limitations
The theorem is specifically about the displayed rank-two family over the real field, not all rank-two evolution algebras or arbitrary fields. Full intermediate graph realization may fail over smaller fields. Its quantitative invariant is unnormalized edge Cheeger expansion, not conductance or normalized Laplacian gap. Searches cannot establish historical uniqueness; an earlier equivalent treatment within graph-theoretic studies of natural bases remains a priority risk. Independent validation has not been performed.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v2 (first public version 2026-05-12), Definition 3.1, Theorem 3.8 and Problem 8.3. https://arxiv.org/pdf/2605.12672
2. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685 (first public 2013-12-17), Examples 2.4–2.5 and Proposition 2.8. https://arxiv.org/html/1312.4685v1
3. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248 (first public 2026-10-15), Question 14 and Section 1. https://arxiv.org/abs/2610.22248
