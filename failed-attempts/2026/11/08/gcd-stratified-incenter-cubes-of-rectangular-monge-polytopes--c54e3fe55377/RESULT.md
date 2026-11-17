# GCD-stratified incenter cubes of rectangular Monge polytopes

## Finding
Let \(p,q\ge2\) be unequal integers and let \(\mathcal M_{p,q}\) be the polytope of nonnegative \(p\)-by-\(q\) real matrices of total entry sum one satisfying the adjacent Monge inequalities. Endow its affine hyperplane with the inherited Frobenius metric. Write \(g=\gcd(p,q)\) and \(\alpha=\sqrt{1-1/(pq)}\).

Its exact intrinsic Euclidean inradius is
\[
\boxed{\rho_{p,q}=\left[pq\sqrt{1-\frac1{pq}}+\frac{p^2q^2-p^2-q^2+g^2}{6}\right]^{-1}.}
\]
**The complete set of centers of largest inscribed balls is an affine \((g-1)\)-cube.** In particular it is a singleton precisely when \(p\) and \(q\) are coprime, and otherwise has \(2^{g-1}\) extreme points. All \((p-1)(q-1)\) adjacent-Monge facets touch every optimal ball. At an incenter with cube coordinates \(t_1,\dots,t_{g-1}\in[0,1]\), exactly
\[
\boxed{(p-1)(q-1)+p+q-g+\#\{k:t_k\in\{0,1\}\}}
\]
facets touch the ball (the remaining touching facets are coordinate nonnegativity facets). These formulas remain algebraically valid at \(p=q\), but that diagonal case was established previously and is *not* claimed as a new discovery.

The centers are explicit. Put \(\theta_j=\lceil pj/q\rceil\) whenever \(pj/q\notin\mathbb Z\); for the \(g-1\) indices \(j=kq/g\) where \(pj/q=kp/g\) is integral, put \(\theta_{kq/g}=kp/g+t_k\). Define \(b_1=0\), \(b_{j+1}=b_j+\theta_j\), and \(a_i=\max_{1\le h\le q}(ih-b_h)\). Every incenter, and no other, is
\[
\boxed{c_{ij}=\rho_{p,q}\left[\alpha+2(a_i+b_j-ij)\right],\quad 1\le i\le p,\ 1\le j\le q.}
\]
For example, the coprime \(2\)-by-\(3\) case has radius \(1/(4+\sqrt{30})\) and a unique incenter; the \(4\)-by-\(6\) case has radius \(1/(88+\sqrt{552})\) and a one-dimensional interval of incenters.

## Assumptions and scope
The Monge convention is \(c_{ij}+c_{i+1,j+1}\le c_{i,j+1}+c_{i+1,j}\) for \(1\le i<p\) and \(1\le j<q\). These adjacent inequalities are equivalent to the full nonadjacent Monge family. The ambient affine span is \(H=\{C:\sum_{i,j}c_{ij}=1\}\), of dimension \(pq-1\), with the Euclidean/Frobenius metric inherited from \(\mathbb R^{p\times q}\). This is not a claim about row-stochastic or fixed-margin transportation polytopes, symmetric matrices, other normalizations, or linear-affine metric equivalence. The 2023 facet classification cited below guarantees that precisely the coordinate nonnegativity inequalities and the adjacent Monge inequalities are facets.

## Proof
**Step 1: Exact ball-containment inequalities.** On the tangent space to \(H\), a coordinate normal has projection norm \(\alpha=\sqrt{1-1/(pq)}\). Every four-entry adjacent Monge normal has coordinate sum zero and Frobenius norm \(2\). Hence a Frobenius radius-\(r\) ball with center \(C\in H\) lies in \(\mathcal M_{p,q}\) if and only if, for every valid index,
\[
c_{ij}\ge\alpha r,\qquad
\delta_{ij}(C):=c_{i,j+1}+c_{i+1,j}-c_{ij}-c_{i+1,j+1}\ge2r.
\]

**Step 2: A sharp coupling identity.** Let \(U\) be uniform on \((0,1)\) and \(I=\lceil pU\rceil,\ J=\lceil qU\rceil\). Put
\[
\pi_{ij}=\operatorname{Leb}\left(((i-1)/p,i/p)\cap((j-1)/q,j/q)\right).
\]
This coupling has row marginals \(1/p\), column marginals \(1/q\), and \(\sum\pi_{ij}=1\). For every real array \(C\), an exact discrete summation-by-parts identity is
\[
\boxed{\sum_{ij}c_{ij}=pq\sum_{ij}\pi_{ij}c_{ij}+\sum_{a=1}^{p-1}\sum_{b=1}^{q-1}w_{ab}\delta_{ab}(C),\qquad w_{ab}=\min(aq,bp)-ab.}
\]
One proves it first for arrays constant on rows or columns (both sides agree by the matching marginals), and then for step arrays supported on northeast rectangles; these arrays together span all matrices. On a northeast rectangle, the cumulative distribution difference of the comonotone and independent couplings is \(\min(a/p,b/q)-ab/(pq)\), giving precisely \(w_{ab}\). Crucially \(w_{ab}>0\) for all interior indices.

**Step 3: Evaluate the coefficient sum exactly.** Indicator expansions of \(I\) and \(J\) give
\[
\sum_{a,b}w_{ab}=pq\operatorname{Cov}(I,J).
\]
For completeness, writing \(B_1(u)=u-1/2\) for \(0\le u<1\), we have \(I=pU+1/2-B_1(\{pU\})\) and similarly for \(J\). Elementary integration gives \(\operatorname{Cov}(U,B_1(\{kU\}))=1/(12k)\). The Fourier series of the centered sawtooth, interpreted in \(L^2\), gives
\[
\int_0^1 B_1(\{pu\})B_1(\{qu\})\,du=\frac{g^2}{12pq},\quad g=\gcd(p,q):
\]
indeed only Fourier frequencies satisfying \(mp+nq=0\) survive, and their reciprocal-square series sums to \(g^2/(12pq)\). Consequently
\[
\operatorname{Cov}(I,J)=\frac{p^2q^2-p^2-q^2+g^2}{12pq},\qquad
\boxed{\sum_{a,b}w_{ab}=\frac{p^2q^2-p^2-q^2+g^2}{12}.}
\]
Applying Step 2 to any radius-\(r\) center and using Step 1 yields
\[
1=\sum c_{ij}\ge pq\alpha r+2r\sum w_{ab};
\]
thus \(r\le\rho_{p,q}\).

**Step 4: Construct every maximizing center.** For arbitrary \(t_k\in[0,1]\), define \(a_i,b_j\) as in the finding and put \(d_{ij}=a_i+b_j-ij\). Then \(d_{ij}\ge0\) by its maximizing definition and \(\delta_{ij}(D)=1\) by direct cancellation. To see that \(d\) vanishes whenever \(\pi_{ij}>0\), note that the differences of \(h_i(j)=ij-b_j\) are \(h_i(j+1)-h_i(j)=i-\theta_j\). Thus \(h_i\) increases, is constant, and decreases as the column subintervals pass the row subinterval; every column with **positive** overlap is a maximizer. At a common partition boundary the free parameter \(t_k\in[0,1]\) preserves that property. Thus \(\sum\pi_{ij}d_{ij}=0\), and Step 2 gives \(\sum d_{ij}=\sum w_{ab}\). Consequently \(C=\rho_{p,q}(\alpha\mathbf1+2D)\) has sum one and satisfies every containment inequality with equality at all Monge facets, attaining \(r=\rho_{p,q}\).

Conversely, equality in Step 3 forces **every** positive-weight Monge slack to be exactly \(2\rho_{p,q}\) and every coordinate with \(\pi_{ij}>0\) to be exactly \(\alpha\rho_{p,q}\). Thus \(D=(C/\rho_{p,q}-\alpha\mathbf1)/2\) obeys \(D\ge0\), \(\delta_{ij}(D)=1\), and \(d_{ij}=0\) on every positive-overlap cell. The zero mixed differences of \(d_{ij}+ij\) imply \(d_{ij}=a_i+b_j-ij\). Write \(\theta_j=b_{j+1}-b_j\). If \(j/q\) lies **inside** a row interval, the two adjacent positive-overlap equalities force \(\theta_j=\lceil pj/q\rceil\). If \(j/q=i/p\) is a common endpoint, the nearest two off-support nonnegativity constraints force \(i\le\theta_j\le i+1\). These are precisely the independent parameters in the displayed construction; all other nonnegativity constraints hold automatically by the maximizing argument.

**Step 5: Affine-cube dimension and facet contacts.** The two uniform partitions of \((0,1)\) have exactly \(g-1\) shared interior endpoints, at \(k/g\). Therefore exactly \(g-1\) independent slope parameters \(t_k\) remain. At every cell of positive overlap, the formula for \(a_i\) may use a fixed maximizing column, so \(C\) depends affinely on \(t\); the slopes \(b_{j+1}-b_j\) recover the parameters injectively. Hence the incenter locus is affinely isomorphic to \([0,1]^{g-1}\). There are \(p+q-g\) positive-overlap cells, each providing a tangent coordinate facet. By the strict increase/decrease of the maximizing sequences outside their overlap blocks, no other coordinate is tangent except exactly one additional neighboring cell at each common boundary for which \(t_k\) equals \(0\) or \(1\). Adding the always tangent \((p-1)(q-1)\) Monge facets proves the contact formula.

## Verification
The standalone standard-library exact checker `artifacts/verify.py` evaluates the coupling-weight identity and constructs valid optimal centers for all \(576\) parameter pairs with \(2\le p,q\le25\), including zero patterns and tangent-contact counts; it additionally checks \(4390\) cube-corner profiles through dimension \(11\) (\(2\le p,q\le12\)). When SciPy is installed, it also independently solves the original radius-maximizing linear program for all \(64\) pairs with \(2\le p,q\le9\), using the true projected Frobenius facet norms. The exact construction and symbolic proof apply for **all** permitted integers; these finite checks are not a substitute for the infinite proof.

## Relationship to prior work
Erickson and Kretschmann (2023), in Theorem 5.3, prove the full irredundant facet description of generic rectangular Monge polytopes and compute volumes for two-row instances, not their Frobenius inradii or incenter strata. The published 2026 theorem *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes* gives exactly the diagonal \(p=q=n\) specialization; the present **unequal-size** theorem is not implied by it: the shared-breakpoint arithmetic changes the optimal-face dimension from \(n-1\) to \(\gcd(p,q)-1\), and the radius has the genuine arithmetic correction \(\gcd(p,q)^2\). The 2026 lattice-path volume/Ehrhart paper on the same Monge family has a distinct stated focus; its full text was not available for direct inspection and therefore remains an explicit historical-priority limitation.

## Limitations
The novelty claim concerns unequal rectangular sizes, not the known square formula. The theorem uses the sum-one normalization, nonnegative entries, and the inherited Frobenius metric. No assertion is made for other metrics, fixed-margin transportation sets, or maximum-volume ellipsoids. The full text of a 2026 article on the Monge family was inaccessible, so hidden equivalent results cannot be categorically excluded. Historical priority has not been independently established.

## References
- W. Q. Erickson and J. Kretschmann, *The structure and normalized volume of Monge polytopes*, arXiv:2311.07522, first public version 2023-11-13; especially Theorem 5.3 and Section 5.2. https://arxiv.org/html/2311.07522v2
- *An affine \((n-1)\)-cube of Euclidean incenters for square Monge polytopes*, publicly available 2026-10-11; original claim and proof inspected in full. https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-an-affine-n-1-cube-of-euclidean-incenters-for-square-monge-polyt--b3dc6b94166a/RESULT.md
- W. Q. Erickson and N. B. Jones, *A lattice path model for the volume of the Monge polytope*, arXiv:2609.09508, first posted 2026-09-08; abstract checked, full text not accessible. https://arxiv.org/abs/2609.09508
