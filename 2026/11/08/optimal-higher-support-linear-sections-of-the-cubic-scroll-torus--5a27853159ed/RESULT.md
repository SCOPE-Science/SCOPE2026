# Optimal higher-support linear sections of the cubic scroll torus

## Finding
Let \(q\ge5\) be a prime power, \(k=\mathbb F_q\), and \(t=q-1\). Consider the rational point set
\[
T_q=\{[1:u:u^2:v:uv]:u,v\in k^\times\}\subset\mathbb P^4(k),
\]
which is the dense-torus point set of the smooth cubic rational normal scroll \(S(1,2)\). Let \(V=\langle1,u,u^2,v,uv\rangle_k\) and \(C_q\) be its evaluation code on \((k^\times)^2\). For each \(1\le r\le5\), let \(z_r\) be the greatest number of common torus zeros of an \(r\)-dimensional subspace \(W\subset V\), and let \(N_r\) be the number of distinct \(r\)-dimensional subspaces attaining that greatest number. Then
\[
(z_1,z_2,z_3,z_4,z_5)=(2t,t+1,t,1,0)
\]
and
\[
\boxed{(N_1,N_2,N_3,N_4,N_5)=\left(\binom t2,\ t^2(t-1),\ t,\ t^2,\ 1\right).}
\]
In particular, the complete generalized Hamming-weight hierarchy is
\[
(d_1,d_2,d_3,d_4,d_5)=(t^2-2t,t^2-t-1,t^2-t,t^2-1,t^2).
\]
The **newly determined data** are the geometric classification and exact numbers of optimizing subspaces, especially dimensions two and three; the first-weight value and its word multiplicity are already accessible from earlier work.

For \(r=2\), every optimal \(W\) consists precisely of sections vanishing on a full ruling fiber \(u=a\) and on one additional torus point \((b,c)\) with \(b\ne a\), and every such choice gives a unique \(W\). Thus exactly \(t^2(t-1)\) projective planes in \(\mathbb P^4(k)\) contain the maximum \(t+1\) points of \(T_q\). For \(r=3\), the only optimal subspaces are \((u-a)\langle1,u,v\rangle\) for \(a\in k^\times\). Their projective annihilators are precisely the \(t\) ruling lines containing \(t\) torus points each. These classifications apply to all finite fields in the specified range, not only prime fields.

## Assumptions and scope
The field has \(q\ge5\) elements, so \(t=q-1\ge4\). Only the dense rational torus points are counted; toric-boundary points, geometric points over extension fields, and scheme-theoretic intersection lengths are not included. Projective linear subspaces are defined over \(k\). Evaluation is injective: a section \(f(u)+vg(u)\) vanishing for all \(u,v\in k^\times\) first has \(g(u)=f(u)=0\) for each \(u\), and degrees \(\deg f\le2<t\), \(\deg g\le1<t\) force \(f=g=0\). Thus \(\dim_k C_q=5\). The code's block length is \(t^2\); its generalized Hamming weight satisfies \(d_r=t^2-z_r\).

## Proof
Every section has the unique form
\[
F(u,v)=f(u)+vg(u),\qquad\deg f\le2,\quad\deg g\le1.
\]
Fix \(a\in k^\times\). Call the fiber \(u=a\) **full** for \(W\) if every section of \(W\) vanishes identically there. Equivalently,
\[
W\subset V_a:=(u-a)\langle1,u,v\rangle_k,
\]
a three-dimensional space. Outside a full fiber, at most one point of that fiber is a common zero, because at least one specialized section is a nonzero affine-linear polynomial in \(v\). Two different full fibers force every section to be a multiple of \((u-a)(u-b)\): its \(v\)-coefficient, of degree at most one, must vanish, and its \(u\)-coefficient is a scalar multiple of this quadratic. Thus a subspace of dimension at least two has at most one full fiber.

**Dimension one.** If \(g=0\), a nonzero \(f\) has at most two roots in \(k^\times\), yielding at most \(2t\) zeros. If \(g\ne0\), at most one fiber can be full and all other fibers contribute at most one zero, hence at most \(t+(t-1)=2t-1\). Equality \(z_1=2t\) holds exactly for the one-dimensional spaces spanned by \((u-a)(u-b)\) with distinct \(a,b\in k^\times\). Hence \(N_1=\binom t2\).

**Dimension two.** With no full fiber there are at most \(t\) common zeros. With a full fiber \(u=a\), divide an independent basis by \(u-a\). The resulting two independent affine-linear forms in \((u,v)\) have at most one common affine point off that fiber, so there are at most \(t+1\) common torus zeros. Equality holds exactly if their intersection is a torus point \((b,c)\) with \(b\ne a\). Conversely, for each triple \((a,b,c)\in(k^\times)^3\) with \(a\ne b\), the two-dimensional subspace
\[
W_{a,b,c}=(u-a)\langle u-b,v-c\rangle_k
\]
has precisely the full fiber \(u=a\) and the off-fiber point \((b,c)\) as its common zeros. These zero sets determine the triples uniquely, so their spaces are distinct. There are \(t\cdot(t-1)\cdot t=t^2(t-1)\) of them.

**Dimension three.** If a full fiber occurs then \(W=V_a\), so its common zeros are exactly that fiber, and there are \(t\) such spaces. To prove there is no other optimizing space, suppose \(W\) has no full fiber but at least \(t\) common zeros. Each fiber then has at most one common zero; hence every \(a\in k^\times\) has a common zero \((a,v_a)\). Write an independent basis \(F_i=f_i(u)+vg_i(u)\), \(1\le i\le3\). The determinants
\[
\Delta_{ij}(u)=f_i(u)g_j(u)-f_j(u)g_i(u)
\]
vanish at all \(t\ge4\) distinct nonzero field elements, yet have degree at most three. Thus each \(\Delta_{ij}\) vanishes identically. If all \(g_i=0\), then \(W=k[u]_{\le2}\), which contains \(1\) and has no common zero: contradiction. Otherwise, after choosing coprime \(A,B\in k[u]\) for the common rational ratio \(f_i/g_i=A/B\), polynomial divisibility yields \(f_i=A h_i\) and \(g_i=B h_i\) for each \(i\). Since \(\deg g_i\le1\), all \(h_i\) lie in a polynomial space of dimension at most two. Hence the \(F_i\) are dependent, another contradiction. Therefore \(z_3=t\) and the \(t\) subspaces \(V_a\) are all the optimizers.

**Dimensions four and five.** The evaluation functionals at distinct torus points are linearly independent, since the subspace \(\langle1,u,v\rangle\subset V\) separates any two distinct points. A space of sections vanishing at two distinct points consequently has dimension at most three. For each torus point \(P\), the kernel of evaluation at \(P\) has dimension four, has exactly one common zero, and is unique for \(P\); this yields \(z_4=1\), \(N_4=t^2\). The only five-dimensional subspace is \(V\), which contains the constant section \(1\); therefore \(z_5=0\), \(N_5=1\). This proves the formulas.

## Verification
Run `python3 scripts/check.py` with Python 3 and its standard library. It enumerates **every** reduced-row-echelon \(r\)-subspace of \(k^5\) for all \(1\le r\le5\), tests zero sets using the five independent monomials, and asserts the complete lists of maxima and optimizer counts over prime fields \(\mathbb F_5\) and \(\mathbb F_7\). The exhaustive subspace totals for the two middle ranks are respectively \(20306\) and \(140050\); the exact results are in `checks/output.txt`. The finite checks are corroborative, not a proof for all prime powers.

## Relationship to prior work
Gauthier Umaña and Velasco (arXiv:1404.4063, Theorem 3.4) compute length, dimension and **minimum distance** for degree-one toric polytopes, including the Lawrence prism of type \((1,2)\), but do not count higher-rank optimizing linear systems. González Sarabia, Camps, Sarmiento and Villarreal (arXiv:1611.06405, Theorem 18 and Example 19) determine second generalized Hamming weights for the **complete** degree-bounded torus codes; their Example 19 lists a full six-dimensional quadratic-code hierarchy over \(\mathbb F_5\). The cubic scroll code here is a proper five-dimensional subcode, and their numerical bounds do not classify or count its optimal two- or three-dimensional subcodes. Existing exact one-word weight spectra for the cubic-scroll torus and weight hierarchies for a **different** quartic scroll also do not imply these optimizer multiplicities. The substantive refinement is the sharp classification of all optimum higher-rank linear sections and its uniform count for every prime power \(q\ge5\).

## Limitations
The formula does not enumerate nonoptimal higher-dimensional subcodes or a complete generalized support enumerator. Its incidence counts concern rational points on the dense torus, not the entire projective scroll. The novelty assessment is based on inspected literature and mathematical-record searches; undiscovered specialized priority is possible. Independent mathematical validation has not been conducted.

## References
1. V. Gauthier Umaña and M. Velasco, *Dual toric codes and polytopes of degree one*, arXiv:1404.4063 (first version publicly submitted 2014-04-15), especially Theorem 3.4.
2. M. González Sarabia, E. Camps, E. Sarmiento and R. H. Villarreal, *The second generalized Hamming weight of some evaluation codes arising from a projective torus*, arXiv:1611.06405 (first submitted 2016-11-19), Theorem 18 and Example 19.
