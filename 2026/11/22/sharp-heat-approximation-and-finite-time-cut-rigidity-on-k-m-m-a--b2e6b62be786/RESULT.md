# Sharp heat approximation and finite-time cut rigidity on \(K_{m,m}\) and \(K_{m,m+1}\)

## Finding
Fix an integer \(m\ge2\) and any \(t>0\). Let \(G\) be the unit-edge complete bipartite graph with shores \(U,W\) of sizes \((m,m)\) or \((m,m+1)\). Its combinatorial Laplacian is \(L=\deg-\mathrm{adjacency}\), and \(H_t=e^{-tL}\) is the counting-measure symmetric heat operator. For real vertex functions put
\[
\|g\|_{\ell^1(V)}=\sum_{v\in V}|g(v)|,\qquad
\operatorname{TV}_G(f)=\sum_{\{u,v\}\in E(G)}|f(u)-f(v)|.
\]
The exact **attained** quotient-by-constants operator norm of \(I-H_t\) from graph variation to counting \(\ell^1\) is
\[
\boxed{C_{m,m}(t)=\frac{2(1-e^{-mt})}m}.
\]
For \(K_{m,m+1}\), define
\[
X=\frac{1-e^{-(2m+1)t}}{2m+1},\qquad
A=\frac{1-e^{-(m+1)t}-(m+1)X}m,\qquad
B=\frac{1-e^{-mt}-mX}{m+1}.
\]
Then
\[
\boxed{C_{m,m+1}(t)=2\left[X+\frac{(m-1)A+mB}{2m-1}\right]}.
\]
Every nonconstant equality input is, up to additive constant and nonzero scalar multiplication, a cut indicator \(\mathbf1_S\). In \(K_{m,m}\), equality holds precisely when the two shores contain the same number \(k\in\{1,\ldots,m-1\}\) of vertices of \(S\). In \(K_{m,m+1}\), equality holds precisely when the two shore counts are \((1,1)\) or \((m-1,m)\). Thus the balanced graph has a family of optimal cardinalities, but adding one vertex rigidifies the finite-time optimizer to the smallest balanced pair and its complement. Both coefficients increase strictly and are strictly concave in \(t\), with
\[
\lim_{t\to\infty} C_{m,m}(t)=\frac2m,\qquad
\lim_{t\to\infty} C_{m,m+1}(t)=\frac4{2m+1},\qquad
C_{m,m}(t),C_{m,m+1}(t)=2t+O_m(t^2)\ (t\downarrow0).
\]

## Assumptions and scope
All edges have conductance one, the Laplacian is unnormalized, vertex error is the **sum**, not the average, of absolute coordinate errors, and variation sums each undirected bipartite edge once. The assertion concerns all real inputs with nonzero variation, all integers \(m\ge2\), and every finite \(t>0\). Boundary cases \(t=0\), constant functions, \(m=1\), other graph families, and weighted/degree-normalized generators are not part of the equality classification.

## Proof
**1. Strictly positive heat and cut reduction.** On a connected finite graph \(H_t\) is symmetric and strictly positive entrywise for every \(t>0\), and has row and column sums one. For a nonempty proper set \(S\), symmetry and conservation give
\[
\|(I-H_t)\mathbf1_S\|_1=2\sum_{v\in S,\,w\notin S}H_t(v,w).
\]
Every real input is an additive constant plus a positive linear combination of nested strict-superlevel indicators; the identity \(\operatorname{TV}_G(f)=\int_\mathbb R |\partial\{f>s\}|\,ds\) and triangle inequality reduce its norm ratio to the largest nontrivial cut ratio. Hence proving a sharp cut inequality proves the bound for every real input.

**2. Heat kernel and cut orbit.** More generally write the shore sizes as \(a\le b\), with \(N=a+b\). The graph Laplacian has eigenvalues \(b\) on the mean-zero \(a\)-shore subspace, \(a\) on the mean-zero \(b\)-shore subspace, \(a+b\) on the between-shore mean-difference subspace, and zero on constants. Therefore every distinct same-shore kernel entry is
\[
A=\frac{1-e^{-bt}-bX}a,\quad B=\frac{1-e^{-at}-aX}b,\quad X=\frac{1-e^{-(a+b)t}}{a+b},
\]
where \(X\) is every across-shore entry. These are strictly positive when \(a,b\ge2,t>0\). For a cut containing \(p\) vertices from the \(a\)-shore and \(q\) from the \(b\)-shore, put
\[
D=bp+aq-2pq>0,\quad U=p(a-p),\quad V=q(b-q).
\]
Its exact error-to-variation ratio is
\[
R_t(p,q)=2\left[X+\frac{AU+BV}D\right]. \tag{1}
\]

**3. Balanced case.** If \(a=b=m\), then
\[
A=B=\frac{(1-e^{-mt})^2}{2m},\quad X=\frac{1-e^{-2mt}}{2m},\quad D-U-V=(p-q)^2.
\]
Thus \(R_t(p,q)\le2(X+A)=2(1-e^{-mt})/m\), with equality exactly when \(p=q\). Nontrivial such cuts require \(1\le p=q\le m-1\).

**4. One-vertex imbalance.** Let \(a=m\), \(b=m+1\). Since
\[
ab(A-B)=e^{-(a+b)t}-b e^{-bt}+a e^{-at},
\]
multiplying by \(e^{(a+b)t}\) gives \(1-be^{at}+ae^{bt}\), which vanishes at zero and has derivative \(ab(e^{bt}-e^{at})>0\). Consequently \(A>B\). On the other hand,
\[
bB-aA=2e^{-(a+b)t/2}\left[\frac{b-a}{a+b}\sinh\frac{(a+b)t}2-\sinh\frac{(b-a)t}2\right]>0
\]
because \(\sinh s/s\) increases strictly for positive \(s\). Hence \(1<A/B<b/a\) for all \(t>0\).

For any cut write \(d=q-p\). At the first endpoint weight ratio \(A/B=1\), the integer identity
\[
D-U-V=d(d-1)\ge0
\]
proves \((U+V)/D\le1\), with equality for \(d=0\) or \(d=1\). At the other endpoint weight ratio \(A/B=b/a\), put
\[
M=\frac{(b/a)(a-1)+a}{2a-1},\quad
F=a(2a-1)\left[MD-\frac ba U-V\right].
\]
Direct expansion gives the exact polynomial identity
\[
F=p(p-1)+d(a-1)(a-2p)+a(2a-1)d(d-1). \tag{2}
\]
For integer \(d=0\), this is \(p(p-1)\ge0\); for \(d=1\), it is \((a-p)(a-p-1)\ge0\). If \(d\le-1\), then
\[
F(d)-F(0)=d\left[(a-1)(a-2p)+a(2a-1)(d-1)\right]>0
\]
for \(0\le p\le a\), \(a\ge2\). If \(d\ge2\), similarly
\[
F(d)-F(1)=(d-1)\left[(a-1)(a-2p)+a(2a-1)d\right]>0.
\]
Thus \((bU/a+V)/D\le M\), with equality among nontrivial cuts only at \((p,q)=(1,1)\) and \((p,q)=(a-1,a)\). The actual ratio \(A/B\) lies strictly between the two endpoint ratios. Taking their positive convex combination proves
\[
\frac{AU+BV}D\le\frac{A(a-1)+Ba}{2a-1},
\]
with exactly the same two equality patterns. Substitution into (1) proves the claimed sharp coefficient and cut uniqueness.

**5. Arbitrary-input equality and time dependence.** For every proper nonempty cut and each vertex \(v\), strict kernel positivity implies \(((I-H_t)\mathbf1_S)(v)>0\) when \(v\in S\), and is negative when \(v\notin S\). If a real input has three or more distinct levels, choose a vertex at an intermediate level: its layer-cake sum contains strictly positive and strictly negative contributions at that coordinate, so the triangle inequality is strict. Hence every nonconstant norm extremizer is two-valued and its unique proper superlevel cut must be one of the classifications above. For a fixed nonconstant cut, its symmetric heat error is
\[
2\langle\mathbf1_S,(I-H_t)\mathbf1_S\rangle
=2\sum_{\lambda>0}(1-e^{-\lambda t})\|P_\lambda\mathbf1_S\|_2^2,
\]
so the cut ratio is strictly increasing and strictly concave in \(t>0\). Since one maximizing cut is fixed for every \(t>0\) in each graph family, the sharp coefficient has both properties. The limits follow by setting the decaying exponentials to zero; the derivative at zero equals twice the cut-boundary size divided by the same boundary size, giving \(2t+O_m(t^2)\).

## Verification
Run `python3 verify_near_biclique.py` using the Python standard library. It exhausts all cut cardinalities with exact rational heat factors \(e^{-t}\in\{1/2,2/3,3/4,9/10\}\) for every \(2\le m\le12\), independently integrates a finite heat ODE, and checks 5,760 randomized real-signal inequalities. Exact-rational cut tests are finite diagnostics; the proof above establishes the arbitrary-size and all-positive-time statements.

## Relationship to prior work
The classical \(L^1\) Poincaré/coarea cut reduction is established in prior literature [2]; it is not claimed as new. A publicly indexed exact Poincaré theorem for complete bipartite graphs [4] calculates the **stationary** real \(L^1\) cut quotient \(\sum_{i<j}|f_i-f_j|/\operatorname{TV}_G(f)\), whose equality family for \(K_{m,m+1}\) contains every cut with shore-count difference zero or one. That result does not state finite-time \(\|f-H_tf\|_1\), the two nonstationary intrashore kernel coefficients, or the strict finite-time collapse to two cut patterns. Another published result [5] computes \(\operatorname{TV}_G(H_tf)/\operatorname{TV}_G(f)\), with variation on both sides; it does not imply an \(\ell^1\) identity-defect estimate. A published normalized-heat Gini contraction result [6] uses a different Laplacian and all-pair variation, not the present graph-edge variation. The general graph heat spectral framework [1,3] supplies context but no claimed exact near-balanced cut inequality. Best-knowledge originality is qualified by the possibility of unindexed equivalent heat-content identities.

## Limitations
The theorem is restricted to real vertex functions, unweighted near-balanced complete bipartite graphs, positive finite times, counting \(\ell^1\) error, and the unnormalized Laplacian. Its \(t\to\infty\) values are already implied by stationary cut-Poincaré theory and are included for comparison rather than presented as separate new results. It does not classify \(K_{a,b}\) for shore-size differences at least two, or weighted, normalized, or directed dynamics. No independent mathematical validation or historical-priority certification is asserted.

## References
[1] J. S. Dowker, *Heat-kernels on the discrete circle and interval*, arXiv:1207.2096v1, first publicly submitted 2012-07-09, https://arxiv.org/abs/1207.2096.
[2] S. Steinerberger, *Sharp \(L^1\) Poincaré inequalities correspond to optimal hypersurface cuts*, arXiv:1309.6211v1, first publicly submitted 2013-09-24, https://arxiv.org/html/1309.6211v7.
[3] H. ElGhawalby and E. R. Hancock, *Heat Kernel Embeddings, Differential Geometry and Graph Structure*, Axioms 4 (2015), 275–293, published 2015-07-21, https://doi.org/10.3390/axioms4030275.
[4] *Sharp metric and real \(L^1\) Poincaré constants of complete bipartite graphs*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-metric-and-real-l-1-poincar-constants-of-complete-bipartit--08309ec3cd7e.
[5] *Sharp edge-variation heat amplification on complete bipartite graphs*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-edge-variation-heat-amplification-on-complete-bipartite-gr--86f601cc5033.
[6] *A sharp uniform Gini-decay envelope for normalized heat on complete bipartite graphs*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-a-sharp-uniform-gini-decay-envelope-for-normalized-heat-on-compl--2ed513aa7e24.
