# Design-universal endpoint Hodge projection norms for symmetric block incidences

## Finding

Let \(\mathcal D\) be any symmetric \(2\)-\((v,k,\lambda)\) block design: it has \(v\) points, \(v\) distinct blocks of size \(k\), every point lies on \(k\) blocks, and every pair of distinct points lies on exactly \(\lambda\) blocks. Assume \(2\leq k<v\), \(1\leq\lambda<k\), and therefore \(k(k-1)=\lambda(v-1)\). Let \(G_{\mathcal D}\) be its unweighted bipartite point–block incidence graph. Orient all \(vk\) edges from points to blocks, and give \(\mathbb R^{E(G_{\mathcal D})}\) its usual coordinate \(\ell_1\) norm. Let \(Q\) be Euclidean orthogonal projection onto the cut (gradient) space and \(C=I-Q\) the orthogonal projection onto the cycle-flow space.

**Theorem.** Both endpoint operator norms depend on the parameters, not on the incidence isomorphism type:
\[
\boxed{\|Q\|_{1\to1}=1+\frac{2(k-1)}{\lambda v}\left[2(k-\lambda)\left(1-\frac\lambda k\right)+(\lambda-1)\left(2-\frac\lambda k\right)\right],}
\]
\[
\boxed{\|C\|_{1\to1}=1+\|Q\|_{1\to1}-\frac{2(2v-1)}{kv}.}
\]
The same values are the \(\ell_\infty\)-operator norms, because the matrices are symmetric. Uniformly over all such designs, \(\|Q\|_{1\to1}<5\) and \(\|C\|_{1\to1}<6\), and both constants are optimal strict upper bounds over the class. Moreover \(\|Q\|_{1\to1}>\|C\|_{1\to1}\) for \(k\leq3\), whereas \(\|Q\|_{1\to1}<\|C\|_{1\to1}\) for \(k\geq4\).

For the incidence graph of **every projective plane of order** \(q\ge2\), including non-Desarguesian planes whenever they exist, \(v=q^2+q+1\), \(k=q+1\), \(\lambda=1\), and
\[
\boxed{\|Q\|_{1\to1}=1+\frac{4q^3}{(q+1)(q^2+q+1)},\quad \|C\|_{1\to1}=\|Q\|_{1\to1}+1-\frac{2(2q^2+2q+1)}{(q+1)(q^2+q+1)}.}
\]
Thus \(\|Q\|_{1\to1}=5-8/q+O(q^{-2})\), while \(\|C\|_{1\to1}=6-12/q+O(q^{-2})\), along orders for which a plane exists. These are bounds for the specified **canonical orthogonal projections**, not assertions of minimum projection constants.

## Assumptions and scope

No transitivity, field structure, or isomorphism classification of the design is assumed. We use the coordinate \(\ell_1\) norm on unoriented edges after fixing a reference orientation; changing orientations conjugates both operators by a diagonal sign matrix and does not affect the norms. The graph is connected: any two points meet a block, and each block meets points. Set \(D:\mathbb R^E\to\mathbb R^{P\sqcup\mathcal B}\) to have column \(e_x-e_A\) for an incidence edge \(e=(x,A)\). Then \(Q=D^\top(DD^\top)^+D\), and \(C=I-Q\).

## Proof

Let \(N\) be the \(v\times v\) point–block incidence matrix and \(J\) the all-ones matrix. The symmetric design identities are
\[
N\mathbf1=N^\top\mathbf1=k\mathbf1,\qquad NN^\top=N^\top N=(k-\lambda)I+\lambda J.
\]
For the second equality, the first Gram identity and invertibility of \(N\) (since \(k>\lambda\)) give the dual Gram identity. The graph Laplacian is
\[
L=DD^\top=\begin{pmatrix}kI&-N\\-N^\top&kI\end{pmatrix}.
\]
Fix an incidence edge \(e=(p,B)\). Solve \(Lh=e_p-e_B\) modulo constants. Decompose the point and block potentials into their respective means \(a,b\) and zero-sum fluctuations \(X,Y\). Summing the point equations gives \(a-b=1/(kv)\). Eliminating \(Y\) from the zero-sum equations yields
\[
(k^2I-NN^\top)X=ke_p-Ne_B.
\]
On zero-sum vectors the left side equals \((k^2-k+\lambda)I=(\lambda v)I\). The analogous block equation gives
\[
X=\frac{ke_p-Ne_B}{\lambda v},\qquad Y=\frac{N^\top e_p-ke_B}{\lambda v}.
\]
Both right-hand sides have zero sum. Hence, for every edge \(f=(x,A)\), the **exact transfer-current entry** is
\[
\boxed{Q_{f,e}=\frac1{kv}+\frac{k\mathbf1_{x=p}-\mathbf1_{x\in B}-\mathbf1_{p\in A}+k\mathbf1_{A=B}}{\lambda v}.}\tag{1}
\]
Its diagonal is \(R=(2v-1)/(kv)\), using the design parameter relation. If \(f\ne e\) shares one endpoint with \(e\), its entry is \(1/(kv)+(k-2)/(\lambda v)>0\). If \(f\) shares neither endpoint, put \(i=\mathbf1_{x\in B}\), \(j=\mathbf1_{p\in A}\). Then \(Q_{f,e}=(\lambda/k-i-j)/(\lambda v)\), positive for \((i,j)=(0,0)\) and negative otherwise, since \(0<\lambda<k\).

The numbers of edges with \((i,j)=(1,0),(0,1),(1,1)\) respectively are
\[
(k-1)(k-\lambda),\quad (k-1)(k-\lambda),\quad (k-1)(\lambda-1).
\]
Indeed, for each of the \(k-1\) other points of \(B\), exactly \(\lambda\) blocks contain both it and \(p\); dually, two distinct blocks meet in \(\lambda\) points. All remaining disjoint-endpoint edges have \((i,j)=(0,0)\); their number is \((k-1)(k-\lambda)^2/\lambda\), by subtracting the known types from the \(vk\) total edges. In particular every column of \(Q\) has the same sign-and-multiplicity profile even when the design has no edge-transitive automorphism group.

Now \(Q\) fixes gradients. Its column sum in the common point-to-block orientation is exactly one: equivalently, the sum of the edge drops \(h_x-h_A\) equals \(k\sum_xh_x-k\sum_Ah_A=kv(a-b)=1\). Therefore its absolute column sum is one plus twice the mass of its negative entries. From the two negative categories we obtain
\[
\sum_f|Q_{f,e}|=1+\frac{2}{\lambda v}\left[2(k-1)(k-\lambda)\left(1-\frac\lambda k\right)+(k-1)(\lambda-1)\left(2-\frac\lambda k\right)\right].
\]
This is independent of \(e\), so it is exactly \(\|Q\|_{1\to1}\). Since \(0<R<1\), replacing \(Q\) by \(I-Q\) changes the absolute value in the diagonal position from \(R\) to \(1-R\) and leaves every other absolute entry unchanged. Thus \(\|C\|_{1\to1}=\|Q\|_{1\to1}+1-2R\).

Finally,
\[
\|Q\|_{1\to1}-\|C\|_{1\to1}=2R-1=\frac{(4-k)v-2}{kv}.
\]
Because \(v>k\ge2\), the numerator is positive for \(k\le3\) and negative for \(k\ge4\). For projective planes, the negative entries consist of exactly \(2q^2\) entries equal to \(-q/((q+1)v)\); the positive entries consist of the diagonal \((2v-1)/((q+1)v)\), exactly \(2q\) shared-endpoint entries equal to \(q^2/((q+1)v)\), and exactly \(q^3\) further entries equal to \(1/((q+1)v)\). This four-value current distribution proves the stated plane formula and its asymptotics by elementary expansion. To establish the uniform bounds, eliminate \(v\) using \(\lambda(v-1)=k(k-1)\) and obtain
\[
5-\|Q\|_{1\to1}=\frac{2\left[2k(k-1)+\lambda(2k^2-k+1)-(k-1)\lambda^2\right]}{k(k^2-k+\lambda)}>0,
\]
where positivity follows from \(1\leq\lambda\leq k-1\). Also \(\|C\|_{1\to1}=\|Q\|_{1\to1}+1-2R<6\). Prime-power projective planes exist in arbitrarily large orders, and the already established two asymptotics approach \(5\) and \(6\), respectively. Thus neither sharp bound can be lowered. \(\square\)

## Verification

Run `python check_design_projections.py` using Python 3 and its standard library. It constructs the Fano plane, the projective plane over the three-element field, a symmetric \(2\)-\((11,5,2)\) biplane, and the complement-of-singletons symmetric design \(2\)-\((5,4,3)\). For each it independently inverts the grounded graph Laplacian **over exact rational numbers**, constructs the full transfer-current matrix, checks all entries against equation (1), checks symmetry and idempotence, and checks the exact cut and cycle operator norms. For both projective planes it also verifies all four current values and multiplicities. The analytic proof, rather than these finite instances, establishes every design covered by the theorem.

## Relationship to prior work

Dilworth, Kutzarova and Ostrovskii [1] supply the cycle/cut projection framework and examine invariant/minimal projections on discrete tori and Hamming graphs. Their discussion distinguishes orthogonal projections from general norm-minimizing projections. Shramchenko and Shramchenko [2] study design incidence and mutual-incidence matrices and their spectral structure; the standard Gram identity is acknowledged. Schild, Rao and Srivastava [3] give general logarithmic-type bounds on entrywise absolute transfer-current matrices, rather than the sharp dimension-free values for incidence designs. The present statement extracts exact absolute **edge-column** masses of the transfer-current projector for all symmetric designs and determines both endpoint projection norms without assuming automorphism transitivity. It includes as a special case the previously evaluated crown graphs (complements of singletons), but its projective-plane and biplane families are not implied by that restricted calculation.

## Limitations

The result does not compute minimum projection constants over all projections, nor projections in intermediate \(\ell_p\) exponents. It does not assert that a design exists for any arbitrary admissible triple \((v,k,\lambda)\): the theorem is conditional on an existing design. The projective-plane asymptotics concern orders for which a projective plane exists. A differently phrased transfer-current computation in earlier design/electrical-network literature cannot be excluded merely by database searches; the precise literature comparison remains subject to independent review.

## References

[1] S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 2023-05-21), Sections 1–2. https://arxiv.org/abs/2305.12582

[2] A. Shramchenko and V. Shramchenko, *Mutual incidence matrix of two balanced incomplete block designs*, arXiv:2312.03937 (2023), Sections 1–3. https://arxiv.org/abs/2312.03937

[3] A. Schild, S. Rao and N. Srivastava, *Localization of electrical flows*, arXiv:1708.01632 (first posted 2017-08-04), Sections 1–2. https://arxiv.org/abs/1708.01632
