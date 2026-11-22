# A rank-one exponential dependence kernel for minimal and maximal counts in random graph orders

## Finding

The two boundary-count variables in a dense random graph order are asymptotically independent, but their first nonvanishing joint correction has an explicit **rank-one** structure. Fix \(p\in(0,1)\) and put \(q=1-p\). Define
\[
F_n(z)=z\prod_{k=1}^{n-1}(1-q^k+q^kz),\qquad F(z)=z\prod_{k=1}^{\infty}(1-q^k+q^kz).
\]
Let \(S_n\) and \(T_n\) count minimal and maximal elements. Uniformly for complex \(|z|,|w|\le1\), as \(n\to\infty\),
\[
\mathbb E[z^{S_n}w^{T_n}]-F_n(z)F_n(w)
=nq^{n-1}(1-z)(1-w)F(z)F(w)
+O_p((1+\log n)q^{n-1}). \tag{1}
\]
The error constant depends on fixed \(p\), but not on \(z,w,n\). Write \(\pi_k=[z^k]F(z)\) and \(\pi_0=0\). For each fixed \(r,s\ge1\),
\[
\Pr(S_n=r,T_n=s)-\Pr(S_n=r)\Pr(T_n=s)
=nq^{n-1}(\pi_r-\pi_{r-1})(\pi_s-\pi_{s-1})
+O_p((1+\log n)q^{n-1}). \tag{2}
\]
In particular, with \(\kappa(q)=\prod_{j\ge1}(1-q^j)>0\),
\[
\Pr(S_n=1,T_n=1)-\Pr(S_n=1)^2
=\kappa(q)^2nq^{n-1}+O_p((1+\log n)q^{n-1}). \tag{3}
\]
For every integer \(n\ge2\), there is also an exact positive covariance:
\[
\operatorname{Cov}(S_n,T_n)
=\frac{q^{n-1}(np-1+q^n)}{p}>0. \tag{4}
\]

## Assumptions and scope

For each integer \(n\ge2\), place vertices \(1,\ldots,n\) in their natural linear order and independently retain every ordered edge \(i\to j\), \(i<j\), with probability \(p\). Take transitive closure to obtain a partial order. A vertex is minimal if it has no original incoming edge, and maximal if it has no original outgoing edge; these equivalences hold even after transitive closure. Let \(A_i\) and \(B_j\) be their indicators, so \(S_n=\sum_i A_i\), \(T_n=\sum_j B_j\). Edges entering distinct vertices are disjoint, as are edges leaving distinct vertices. Hence each of the separate probability-generating functions is \(F_n\). The limit \(F\) is absolutely convergent on compact subsets of the complex plane. All asymptotic statements fix \(p\) strictly between zero and one; no uniformity as \(p\) approaches either endpoint is asserted.

## Proof

**Exact covariance.** For \(j<i\), the events \(A_i=1\) and \(B_j=1\) require the same edge \(j\to i\) to be absent. Therefore
\[
\mathbb E[A_iB_j]=q^{(i-1)+(n-j)-1}=q^{n+i-j-2},
\quad \operatorname{Cov}(A_i,B_j)=p q^{n+i-j-2}.
\]
For \(j\ge i\), the two events depend on disjoint edge sets, and their covariance vanishes. Consequently
\[
\operatorname{Cov}(S_n,T_n)=pq\sum_{1\le j<i\le n}q^{n+i-j-3}
=p q^{n-1}\sum_{d=1}^{n-1}(n-d)q^{d-1}
=\frac{q^{n-1}(np-1+q^n)}p.
\]
The sum of positive terms gives strict positivity.

**Bernoulli interpolation.** For each possible edge \(e\), take two Bernoulli-\(p\) edge indicators \((X_e,Y_e)\) which are identical with probability \(t\) and independently resampled otherwise; the pairs are independent over distinct \(e\). For \(0\le t\le1\), write \(H_t(z,w)=\mathbb E_t[z^{S(X)}w^{T(Y)}]\). Then \(H_0=F_n(z)F_n(w)\), while \(H_1\) is the desired joint generating function. Differentiation of the pair law yields the exact product-measure interpolation identity
\[
\frac{dH_t}{dt}
=pq\sum_e\mathbb E_t[\Delta_e z^{S(X)}\,\Delta_e w^{T(Y)}],
\quad \Delta_e f=f(e=1)-f(e=0).
\]
Indeed, for a single coupled pair, the derivative of the four-state probability table is \(pq\begin{psmallmatrix}1&-1\\-1&1\end{psmallmatrix}\), and the formula follows by differentiating one edge-pair at a time.

For \(e=(j,i)\) with \(j<i\), let \(E_i\) be the event that all *other* incoming \(X\)-edges into \(i\) are absent, and \(G_j\) that all *other* outgoing \(Y\)-edges from \(j\) are absent. Thus
\[
\Delta_e z^{S(X)}=(1-z)z^{S(X)-A_i(X)}\mathbf1_{E_i},
\quad \Delta_e w^{T(Y)}=(1-w)w^{T(Y)-B_j(Y)}\mathbf1_{G_j}.
\]
(The exponents are unaffected by changing the selected edge.) The coordinates used by \(E_i\) and \(G_j\) are distinct; their coupled edge-pair indices do not overlap because the only edge both entering \(i\) and leaving \(j\) is \(e\), which was excluded. Hence their events are independent for every \(t\), with
\[
\Pr_t(E_i\cap G_j)=q^{i-2+n-j-1}=q^{n+i-j-3}.
\]
Define
\[
K_{j,i,t}(z,w)=\mathbb E_t[z^{S-A_i}w^{T-B_j}\mid E_i\cap G_j].
\]
It follows exactly that
\[
H_1-H_0=pq(1-z)(1-w)\int_0^1
\sum_{j<i}q^{n+i-j-3}K_{j,i,t}(z,w)\,dt. \tag{5}
\]

**Uniform localization.** Take \(L=\lceil 3\log n/|\log q|\rceil\) for sufficiently large \(n\), so \(L<n/4\) and \(q^L\le n^{-3}\). Call a pair \((j,i)\) central if \(j>L\), \(i\le n-L\), and \(1\le i-j\le L\). Under \(E_i\cap G_j\), the first \(L\) minimal indicators and the last \(L\) maximal indicators involve mutually disjoint sets of coupled edge-pair coordinates, also disjoint from all coordinates fixed by the conditioning. Their combined generating function is therefore exactly \(F_L(z)F_L(w)\), uniformly in \(t\).

For any other minimal indicator \(A_k\) with \(k>L\), \(k\ne i\), at most one of its incoming edge variables is coupled to an edge fixed by the conditioning. All other \(k-2\) necessary edges remain independent Bernoulli-\(p\), so \(\Pr_t(A_k=1\mid E_i\cap G_j)\le q^{k-2}\). Analogously, for every additional maximal indicator \(B_l\) with \(l\le n-L\), \(l\ne j\), its conditional probability is at most \(q^{n-l-2}\). By summing these bounds and using \(|z|,|w|\le1\),
\[
\sup_{t,z,w}\big|K_{j,i,t}(z,w)-F_L(z)F_L(w)\big|
\le \frac{4q^{L-1}}p.
\]
The products converge geometrically: \(\sup_{|z|\le1}|F_L(z)-F(z)|\le2q^L/p\). Thus for central pairs, \(K_{j,i,t}=F(z)F(w)+O_p(q^{L-1})\), uniformly. For noncentral pairs use \(|K|\le1\). At each gap \(d=i-j\), at most \(2L\) pairs violate the two endpoint conditions, and the total weight of all gaps \(d>L\) is \(O_p(nq^{n-2}q^L)\). Summing geometric weights gives a total localization error \(O_p((L+nq^L)q^{n-2})\).

Finally, the full geometric sum is explicit:
\[
\sum_{1\le j<i\le n}q^{n+i-j-3}
=\frac{q^{n-2}(np-1+q^n)}{p^2}
=\frac{nq^{n-2}}p+O_p(q^{n-2}).
\]
Insert this and the localization estimate in (5). Since \(L=O_p(\log n)\) and \(nq^L=O(n^{-2})\), this proves (1). Note that the bound is **uniform on the closed unit bidisk**, not merely pointwise for real arguments.

**Coefficient extraction.** Apply Cauchy's two-dimensional coefficient formula on \(|z|=|w|=1\) to (1). Its uniform error remains \(O_p((1+\log n)q^{n-1})\) for each fixed coefficient. The coefficient of \(z^r\) in \((1-z)F(z)\) is \(\pi_r-\pi_{r-1}\), giving (2). Since \(\pi_1=\kappa(q)\), equation (3) follows.

## Verification

Run `python3 verify.py` with the Python standard library. The program exhaustively enumerates all forward-edge configurations for \(2\le n\le6\) and both \(p=1/2\) and \(p=2/3\), computing the joint count law using exact rational arithmetic. It checks marginal probability generating polynomials, positive finite covariance, and the exact expression (4). It also verifies the finite algebraic identity for the geometric weighted sum. This tests finite consequences only; the proof of the infinite generating-function expansion is analytic and does not depend on the enumeration.

## Relationship to prior work

Albert and Frieze (1989) introduced this same random graph order model and computed the individual minimal/maximal count distribution at \(p=1/2\); their Section 3 explicitly gives independent indicators and the limiting one-minimum probability. These one-variable laws are **not new**. Bombelli, Seggev and Watson (2008) study the number of posts and Euler-product bounds in the general \(p\) model, a different statistic. The additional result here is the explicit first-order **joint-to-product** correction at scale \(nq^{n-1}\), its rank-one kernel, and its fixed-coefficient consequences. Related literature on source–sink counts of sparse ordered acyclic digraphs concerns \(p=c/n\), where counts fluctuate at a different scale, and does not imply the fixed-\(p\) expansion. The exact elementary covariance (4) is provided as a supporting identity, not relied on alone to establish research value.

## Limitations

The asserted remainder is for each fixed \(0<p<1\); the result does not address sparse density \(p=p_n\), endpoint-uniform errors, or whether the stated logarithmic remainder is sharp. The source comparison is bounded by accessible primary materials; priority relative to inaccessible or unindexed older work remains uncertain. The finite checker does not establish the asymptotic theorem. No independent mathematical validation is claimed.

## References

- M. H. Albert and A. M. Frieze, *Random Graph Orders*, Order **6** (1989), 19–30. https://doi.org/10.1007/BF00341633 ; lawful author manuscript https://www.math.cmu.edu/~af1p/Texfiles/RANDGRAPHORD.pdf
- L. Bombelli, I. Seggev and S. Watson, *A Computation of the Expected Number of Posts in a Finite Random Graph Order*, arXiv:0809.2258, first publicly submitted 2008-09-12. https://arxiv.org/abs/0809.2258
- G. Brightwell, *Random graph orders do not satisfy a 0–1 law*, Random Structures & Algorithms **6** (1995). https://doi.org/10.1002/rsa.3240060211
- B. Bollobás and G. Brightwell, *The structure of random graph orders*, SIAM Journal on Discrete Mathematics **10** (1997). https://doi.org/10.1137/S0895480194281215
