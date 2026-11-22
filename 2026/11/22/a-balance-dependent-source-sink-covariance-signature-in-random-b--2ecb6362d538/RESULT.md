# A balance-dependent source–sink covariance signature in random bipartite spanning trees

## Finding

Let \(a,b\ge2\). Sample a uniformly random spanning tree of the labeled complete bipartite graph \(K_{a,b}\), and independently orient every selected edge with probability \(1/2\) in either direction. Let \(S_A,S_B\) count sources in the two vertex classes, and let \(K_A,K_B\) count sinks. Write
\[
C_{a,b}=\begin{pmatrix}\operatorname{Cov}(S_A,K_A)&\operatorname{Cov}(S_A,K_B)\\\operatorname{Cov}(S_B,K_A)&\operatorname{Cov}(S_B,K_B)\end{pmatrix}.
\]
Define
\[
 c_A=\left(1-\frac1{2a}\right)^{b-1},\quad
 c_B=\left(1-\frac1{2b}\right)^{a-1},\quad
 q_A=\left(1-\frac1a\right)^{b-1},\quad
 q_B=\left(1-\frac1b\right)^{a-1},
\]
\[
 r=\frac{c_Ac_B}{4}\left(\frac1{2a-1}+\frac1{2b-1}-\frac1{(2a-1)(2b-1)}\right).
\]
Then the **exact mixed-covariance matrix** is
\[
\boxed{C_{a,b}=\begin{pmatrix}
\frac{a(a-1)}4q_A-\frac{a^2}4c_A^2&ab r\\
ab r&\frac{b(b-1)}4q_B-\frac{b^2}4c_B^2
\end{pmatrix}.}
\]
Both diagonal entries are strictly negative; both off-diagonal entries are strictly positive. More sharply:

1. For every balanced graph \(K_{m,m}\) with \(m\ge3\), \(C_{m,m}\) is **negative definite**. Hence for every nonzero real vector \(w=(w_A,w_B)\), the mixed covariance \(\operatorname{Cov}(w_A S_A+w_B S_B,w_A K_A+w_B K_B)\) is strictly negative.
2. For every fixed integer \(a\ge2\), the matrix \(C_{a,b}\) is **indefinite** for every sufficiently large \(b\). More precisely,
\[
\boxed{\lim_{b\to\infty}\frac{\det C_{a,b}}{b^2(1-1/(2a))^{2(b-1)}}=-\frac{a^2}{16(2a-1)^2}<0.}
\]
Thus sufficiently unequal bipartition sizes admit a weighted source count and corresponding weighted sink count with strictly *positive* covariance, even though each within-class covariance is negative.

The change occurs at small sizes: for \(K_{2,4}\),
\[
C_{2,4}=\begin{pmatrix}-473/4096&81/256\\81/256&-13/16\end{pmatrix},\qquad
\operatorname{Cov}(3S_A+S_B,3K_A+K_B)=\frac{191}{4096}>0.
\]
This is not a claim of a unique transition threshold at every fixed \(a\).

## Assumptions and scope

Both parts contain at least two labeled vertices. Spanning trees are equiprobable (not random minimum spanning trees); conditional on the tree, orientations of different edges are independent and fair. A source has indegree zero and a sink has outdegree zero. All covariances include randomness from **both** the tree and its orientation. Vectors of class weights are deterministic and can be any real numbers. The claim concerns source–sink *mixed* covariances, not the covariance matrix of source counts alone.

## Proof

**1. Independent degree arrays and two-point moments.** For positive vertex variables \(x_i\), \(i\in A\), and \(y_j\), \(j\in B\), the weighted spanning-tree enumerator is
\[
Z(x,y)=\sum_T\prod_{i\in A}x_i^{d_T(i)}\prod_{j\in B}y_j^{d_T(j)}
=\left(\prod_i x_i\right)\left(\prod_j y_j\right)
\left(\sum_i x_i\right)^{b-1}\left(\sum_j y_j\right)^{a-1}.
\]
It follows from the weighted matrix-tree theorem, or its standard complete-bipartite Schur-complement calculation. Dividing by \(Z(\mathbf1,\mathbf1)=a^{b-1}b^{a-1}\) shows that \((d_T(i)-1)_{i\in A}\) and \((d_T(j)-1)_{j\in B}\) are independent multinomial vectors, with respective totals \(b-1\) and \(a-1\) and uniform probabilities \(1/a\) and \(1/b\). Consequently
\[
\mathbb E[2^{-d_T(i)}]=c_A/2,\quad
\mathbb E[2^{-d_T(j)}]=c_B/2,
\]
\[
\mathbb E[2^{-d_T(i)-d_T(i')}]=q_A/4\ (i\ne i'\in A),\quad
\mathbb E[2^{-d_T(j)-d_T(j')}]=q_B/4\ (j\ne j'\in B),
\]
and for \(i\in A,j\in B\) the corresponding expectation is \(c_Ac_B/4\).

**2. Edge-marked moment.** Let \(I_{ij}\) indicate whether the edge \(ij\) belongs to the sampled tree. Under the weighted spanning-tree law with edge conductances \(w_{uv}=x_u y_v\), put \(X=\sum_{u\in A}x_u\), \(Y=\sum_{v\in B}y_v\). Kirchhoff's edge-inclusion identity \(\mathbb P_w(I_{ij}=1)=w_{ij}R_{ij}\), where \(R_{ij}\) is effective resistance, gives
\[
\mathbb P_w(I_{ij}=1)=\frac{x_i}{X}+\frac{y_j}{Y}-\frac{x_iy_j}{XY}.
\]
For clarity, to verify the resistance formula inject one unit of current at \(i\) and extract it at \(j\). The vertex voltage equations imply \(V_{A,u}=\bar V_B+\mathbf1_{u=i}/(x_iY)\) and \(V_{B,v}=\bar V_A-\mathbf1_{v=j}/(y_jX)\), with \(\bar V_A-\bar V_B=1/(XY)\). Their difference at \(i,j\) is \(R_{ij}=1/(x_iY)+1/(y_jX)-1/(XY)\), as required.

Set \(x_i=y_j=1/2\) and all other variables to one. The ratio of weighted tree partition functions is \(c_Ac_B/4\), while the weighted inclusion probability is the parenthesized expression in the definition of \(r\). Therefore
\[
\mathbb E[I_{ij}2^{-d_T(i)-d_T(j)}]=r.
\]

**3. Pair covariances and matrix.** Given the tree, the source event at \(u\) and the sink event at \(v\) each have probability \(2^{-d_T(u)}\) and \(2^{-d_T(v)}\). For \(u=v\) they are mutually exclusive because degrees are positive. For distinct nonadjacent vertices their incident orientation sets are disjoint, so the joint conditional probability is \(2^{-d_T(u)-d_T(v)}\). For distinct adjacent vertices, their common edge is forced to a consistent orientation by both events, giving **twice** this quantity. Hence for \(u\ne v\),
\[
\mathbb P(u\text{ source},v\text{ sink})
=\mathbb E[2^{-d_T(u)-d_T(v)}]+\mathbb E[I_{uv}2^{-d_T(u)-d_T(v)}].
\]
Within class \(A\), no pair is adjacent: a distinct pair has covariance \((q_A-c_A^2)/4\), while a repeated vertex has covariance \(-c_A^2/4\). The corresponding formulas hold in class \(B\). Across the classes, degree independence and Step 2 give covariance exactly \(r\), positive. Summing over marked vertices gives the displayed \(2\)-by-\(2\) matrix. Since
\[
\frac{q_A}{c_A^2}=\left(1-\frac1{(2a-1)^2}\right)^{b-1}<1,
\]
and similarly for \(B\), the diagonal entries are strictly negative.

**4. Balanced negative definiteness.** Put \(a=b=m\), \(t=(2m-1)^{-2}\), \(c=c_A=c_B\). The matrix has diagonal \(-D\) and off-diagonal \(H>0\), where
\[
D=\frac m4c^2\{m-(m-1)(1-t)^{m-1}\},\qquad
H=\frac m4c^2\{1+(m-1)t\}.
\]
Thus
\[
D-H=\frac{m(m-1)c^2}{4}\left[1-t-(1-t)^{m-1}\right]>0\quad(m\ge3),
\]
since \(0<t<1\) and \(m-1\ge2\). The two eigenvalues \(-D+H\) and \(-D-H\) are both strictly negative. For \(m=2\), the first eigenvalue is zero, consistent with the claim's boundary.

**5. Fixed-side imbalance.** Fix \(a\ge2\) and let \(b\to\infty\). Write \(c_A=(1-1/(2a))^{b-1}\). As \(q_A/c_A^2=(1-(2a-1)^{-2})^{b-1}\to0\),
\[
C_{AA}=-\frac{a^2}4c_A^2(1+o(1)).
\]
Elementary binomial expansions give \(C_{BB}=-b/4+O(1)\), and \(c_B\to1\) yields
\[
C_{AB}=\frac{ab}{4(2a-1)}c_A(1+o(1)).
\]
The product of the diagonal entries, divided by \(b^2 c_A^2\), tends to zero; the squared off-diagonal entry, similarly divided, tends to \(a^2/[16(2a-1)^2]\). The determinant limit follows. A real symmetric \(2\)-by-\(2\) matrix with negative determinant has one positive and one negative eigenvalue. Finally, direct substitution \((a,b)=(2,4)\) gives the claimed matrix and strictly positive weighted covariance.

## Verification

`verify.py` (Python 3 standard library) enumerates every spanning tree of nine complete bipartite graphs from \(K_{1,1}\) through \(K_{4,4}\) and all of their independent fair edge orientations. It checks the exact mixed covariance matrix and two-point source–sink probabilities using rational arithmetic. The largest case evaluates \(524288\) tree/orientation outcomes. It separately checks the balanced determinant signs for \(3\le m\le17\) and obtains negative-determinant examples for fixed \(2\le a\le8\). The checker reports `PASS 92 assertion groups`. The all-size proof relies on Steps 1–5, not on finite enumeration.

Run: `python3 verify.py`.

## Relationship to prior work

The weighted matrix-tree theorem and classical bipartite spanning-tree enumerator are established tools. Burman and Shapiro (2005/2006) give a broad treatment of matrix-tree identities and orientations without sources or sinks of a **fixed graph**; their Section 5 does not give the present two-stage random-tree source/sink covariance matrix. Dong and Ge (2021/2022) count spanning trees of a complete bipartite graph containing prescribed forests; that provides related edge-enumeration information but neither separately randomizes edge orientations nor analyzes this signed covariance spectrum. Known fixed-tree path–star bounds for source/sink covariance and known complete-bipartite degree and edge-covariance identities address related but different statistics. None of those results alone states or implies the balance-to-imbalance change of inertia without the marked edge calculation and the determinant argument provided here.

## Limitations

This is an exact result for complete bipartite graphs and fair, conditionally independent orientations; it does not address arbitrary graphs, weighted tree sampling, other orientation biases, or nonlinear statistics of source/sink counts. The fixed-side asymptotic proves eventual indefiniteness, not an exact or unique threshold for every \(a\). The finite checker is a consistency check rather than proof at all sizes. Historical priority is not settled by search coverage, and independent mathematical validation has not been performed.

## References

- Y. Burman and B. Shapiro, *Around matrix-tree theorem*, arXiv:math/0512164v1, first public 2005-12-07, https://arxiv.org/abs/math/0512164.
- F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294v1, first public 2021-03-09, https://arxiv.org/abs/2103.05294; *Journal of Graph Theory* 101 (2022), 79–94.
- R. Burton and R. Pemantle, *Local characteristics, entropy and limit theorems for spanning trees and domino tilings via transfer-impedances*, *Annals of Probability* 21 (1993), 1329–1371; https://arxiv.org/abs/math/0404048 (later open preprint).
