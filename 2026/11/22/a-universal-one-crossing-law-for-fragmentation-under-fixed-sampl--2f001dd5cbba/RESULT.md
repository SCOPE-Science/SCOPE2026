# A universal one-crossing law for fragmentation under fixed-sample occupancy on trees

## Finding

Let \(T\) be **any** finite tree on \(m\ge3\) labeled vertices. Allocate \(n\ge1\) balls independently and uniformly among its vertices. Let \(K_{m,n}\) count occupied vertices, and let \(C_{T,n}\) count connected components of the induced subgraph on the occupied vertices, assigning zero components to the empty set. Write
\[
q_j=\left(1-\frac jm\right)^n,\quad j=1,2,3.
\]
Then the mixed covariance is independent of the structure of \(T\), and its exact value is
\[
\begin{aligned}
J_m(n):=\operatorname{Cov}(K_{m,n},C_{T,n})={}&-(m-2)q_1+(m-1)(4-m)q_2\\
&+(m-1)(m-2)q_3+m(m-2)q_1^2-m(m-1)q_1q_2.
\end{aligned}
\tag{1}
\]
Define the continuous extension \(J_m(t)\) by the right side of (1), with real \(t>0\), interpreting \(0^t=0\). **For every \(m\ge3\), there exists exactly one real \(r_m>2\)** with \(J_m(r_m)=0\). Furthermore, \(J_m(t)>0\) for \(1<t<r_m\), and \(J_m(t)<0\) for \(t>r_m\). In particular, the covariance for integer sample sizes reverses sign once (with at most one zero integer at the transition). Exactly,
\[
J_m(1)=0,\qquad J_m(2)=\frac{(m-1)(m-2)}{m^3}>0.
\]
The real crossing has the sharp two-term asymptotic position
\[
\boxed{r_m=m\log 2+\frac{2-5\log 2+4(\log 2)^2}{2(1-\log 2)}+O(m^{-1}).}
\tag{2}
\]
The additive constant is approximately \(0.743151315515574\). For any sequence with \(n/m\to\lambda\in(0,\infty)\),
\[
\frac{J_m(n)}m\longrightarrow
\underbrace{e^{-\lambda}[1-(1+\lambda)e^{-\lambda}]}_{>0}
(2e^{-\lambda}-1).
\tag{3}
\]
Thus the sign boundary is the universal load \(\lambda=\log 2\), with the finite-size displacement specified by (2).

## Assumptions and scope

The underlying graph is a deterministic, undirected, simple, connected tree with exactly \(m\) vertices; the balls are iid and each lands at each vertex with probability \(1/m\). Both statistics are unconditioned, including samples that occupy one or all vertices. The law is *fixed-sample multinomial occupancy*, not independent site retention. No assumptions about tree degrees, planar embedding, or vertex labeling are needed. The real continuation is used to locate integer transition counts; it is not a probability model for noninteger \(t\). The degenerate two-vertex tree has \(C_{T,n}=1\) for every \(n\ge1\), hence covariance zero, and is excluded from the nontrivial statement.

## Proof

**1. Exact moments for one edge.** For each vertex \(v\), let \(X_v\) indicate positive occupancy. The event that any specified \(j\) vertices are all unoccupied has probability \(q_j\). Hence
\[
\operatorname{Var}(K_{m,n})=m q_1+m(m-1)q_2-m^2q_1^2.\tag{4}
\]
For any edge \(\{u,v\}\), write \(Y_{uv}=X_uX_v\). Its expected value is \(1-2q_1+q_2\). The two endpoint terms in \(\operatorname{Cov}(K,Y_{uv})=\sum_w\operatorname{Cov}(X_w,Y_{uv})\) contribute \(2q_1(1-2q_1+q_2)\). For any third vertex \(w\notin\{u,v\}\), inclusion–exclusion gives
\[
\operatorname{Cov}(X_w,Y_{uv})=2q_2-q_3-2q_1^2+q_1q_2.
\]
Therefore this edge covariance equals
\[
d_{m,n}=2q_1(1-2q_1+q_2)
 +(m-2)(2q_2-q_3-2q_1^2+q_1q_2).\tag{5}
\]

**2. Shape invariance.** Every induced subgraph of a tree is a forest. Thus, sample by sample,
\[
C_{T,n}=\sum_vX_v-\sum_{\{u,v\}\in E(T)}X_uX_v
=K_{m,n}-\sum_{\{u,v\}\in E(T)}Y_{uv}.
\]
Every tree has exactly \(m-1\) edges, and (5) is the same for every edge, regardless of its endpoints. Consequently
\[
J_m(n)=\operatorname{Var}(K_{m,n})-(m-1)d_{m,n}.
\]
Substitution of (4) and (5), followed by collection of terms, gives (1). More generally, for any forest with \(m\) vertices and \(e\) edges, its component-count/occupancy covariance is \(\operatorname{Var}(K_{m,n})-e d_{m,n}\); this extension is not used to claim a unique switching point for arbitrary forests. Direct substitution proves the two exact small-sample identities.

**3. Exactly one sign reversal.** Put
\[
a=1-1/m,\quad b=1-2/m,\quad c=1-3/m.
\]
For \(m\ge5\) the positive bases occur in strict decreasing order \(a>a^2>b>ab>c>0\). In that order the coefficients of \(J_m(t)\) have signs \(-,+,-,-,+\), or precisely three variations. For \(m=4\), the zero coefficient of \(b^t\) is omitted, giving \(-,+,-,+\), again three variations. The generalized Descartes sign-variation rule states that for distinct positive bases the number of distinct real zeros of \(\sum c_i b_i^t\) cannot exceed the number of coefficient sign variations when the bases are ordered. For completeness, substitute \(x=e^t\), order the real exponents increasingly, and divide by the smallest power of \(x\) to obtain \(H(x)=c_1+\sum_{j=2}^k c_jx^{\alpha_j}\) with \(0<\alpha_2<\cdots<\alpha_k\). Its derivative has the coefficient signs of \(c_2,\ldots,c_k\). If \(c_1c_2>0\), then \(H\) initially moves away from zero and Rolle's theorem forces at least as many derivative zeros as positive zeros of \(H\); if \(c_1c_2<0\), at least one fewer derivative zero is forced. Induction on the number of terms bounds the positive zeros by, respectively, the variations in \(c_2,\ldots,c_k\) or that count plus one, exactly the variations in all coefficients. The argument applies to arbitrary real exponents and distinct roots, as needed here.

For \(m\ge4\), (1) yields \(J_m(0)=J_m(1)=0\). Also \(J_m(2)>0\). Because \(a\) is the unique largest base and its coefficient is negative, \(J_m(t)<0\) for all sufficiently large \(t\). Continuity forces some root in \((2,\infty)\). These three distinct real roots exhaust the allowed three variations. Their absence elsewhere, together with the given positive and negative values, proves the signs on \((1,r_m)\) and \((r_m,\infty)\). For \(m=3\), the term \(c^t\) is identically zero for positive \(t\). The remaining bases satisfy \(a>a^2>b>ab\), with coefficient signs \(-,+,+,-\), having only two variations. The zero at \(t=1\) and the root after \(2\) therefore exhaust the possible positive real zeros. This proves the same assertion at \(m=3\).

**4. Load limit and additive displacement.** If \(n/m\to\lambda>0\), use
\[
\left(1-\frac jm\right)^n\to e^{-j\lambda}
\]
and the first-order expansions of these powers in (1). Collecting the terms of order \(m\) gives (3); the expression is positive exactly for \(\lambda<\log 2\), because \(e^\lambda>1+\lambda\). Consequently the unique root satisfies \(r_m/m\to\log 2\).

For the second order, put \(L=\log 2\), \(t=mL+\beta\), with bounded real \(\beta\). Taylor expansion for each \(j\in\{1,2,3\}\) gives
\[
\left(1-\frac jm\right)^t
=e^{-jL}\left[1-\frac{j\beta+j^2L/2}{m}
+\frac{\frac12(j\beta+j^2L/2)^2-j^2\beta/2-j^3L/3}{m^2}+O(m^{-3})\right],
\]
uniformly on bounded \(\beta\)-sets. Substituting in (1), the order-\(m\) term vanishes at \(L\), and the remaining terms reduce to
\[
J_m(mL+\beta)=\frac{2\beta L-2\beta+4L^2-5L+2}{8}+O(m^{-1}).\tag{6}
\]
The coefficient of \(\beta\) is strictly negative. Taking any fixed \(\beta\) on either side of its zero traps the unique root in a bounded additive window; expanding around this simple zero using the uniform error term gives (2), including its \(O(m^{-1})\) error.

## Verification

Run `python verify.py` using Python 3 and only its standard library. The program derives the exact rational covariance in two algebraically distinct forms, then enumerates all labeled trees on three, four, and five vertices through Prüfer sequences and all possible allocations for one through four balls. It checks each enumerated mixed covariance against (1), checks finite sign transitions for tree orders three through twenty-three, and performs additional noncritical-load asymptotic diagnostics. It prints `PASS 1738 exact rational, enumeration and asymptotic assertions` when successful. These finite checks verify algebra and boundaries but cannot replace the all-order sign-variation or asymptotic arguments above.

## Relationship to prior work

Tittmann, Averbouch, and Makowsky introduced the full subgraph-component polynomial \(Q(G;x,y)\), whose coefficients encode induced-subgraph component counts and whose probability specialization treats **independent** site failures. This is an underlying enumeration framework; it does not state the fixed-ball, tree-universal mixed covariance or its exact one-crossing law. Bartroff and Goldstein analyze Berry–Esseen bounds for **frequency counts** in the uniform fixed-ball multinomial model, not spatial adjacency or connected-component covariance. Allard and collaborators address component-size distributions in general random-graph percolation, without the finite-sample multinomial sign transition. Closely related exact results for Bernoulli-retained habitat trees concern either isolated vertices versus total survivors or degree-matched third cumulants; neither implies the present mixed covariance under dependent site occupancies. The contribution is the conjunction of an all-tree exact covariance, one-crossing theorem, and sharp additive threshold constant, not the elementary forest identity or classical occupancy probabilities alone.

## Limitations

The universality and one-crossing theorem require uniform iid ball allocations and a connected tree. Inhomogeneous vertex probabilities, independent Bernoulli retention, graphs with cycles, arbitrary correlated allocations, and unequal sampling rates are not covered. The sign law concerns covariance, not stochastic ordering or concentration. The real-root continuation has no direct probabilistic interpretation. Historical novelty searches cannot rule out equivalently formulated older formulas or a broader theorem with this as an already established corollary. The verification program performs finite experiments only; independent mathematical review has not been performed.

## References

- P. Tittmann, I. Averbouch and J. A. Makowsky, *The Enumeration of Vertex Induced Subgraphs with Respect to the Number of Components*, arXiv:0812.4147, first public preprint 2008-12-22, https://arxiv.org/html/0812.4147v2.
- J. Bartroff and L. Goldstein, *A Berry–Esseen Bound for the Uniform Multinomial Occupancy Model*, arXiv:1202.0909, first public preprint 2012-02-04, https://arxiv.org/pdf/1202.0909.
- A. Allard, L. Hébert-Dufresne, J.-G. Young and L. J. Dubé, *General and Exact Approach to Percolation on Random Graphs*, arXiv:1509.01207, first public preprint 2015-09-03, https://arxiv.org/abs/1509.01207.
