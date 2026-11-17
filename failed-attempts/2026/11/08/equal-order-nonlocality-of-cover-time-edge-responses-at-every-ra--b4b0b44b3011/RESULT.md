# Equal-order nonlocality of cover-time edge responses at every radius

## Finding

For every integer \(r\geq1\), there are two connected simple graphs of the **same order**, with three individually marked vertices \(s,u,v\) and a missing edge \(uv\), whose marked, ambient-degree-labelled radius-\(r\) neighborhoods are isomorphic but for which adding \(uv\) has opposite effects on the expected cover time of simple random walk started at \(s\). Both configurations additionally have
\[
\deg(s)=\deg(u)=\deg(v)=1,\quad \deg(c)=5,\quad
\operatorname{dist}(s,\{u,v\})=2,\quad R_{uv}=2.
\]
In particular, **even the graph order, when supplied alongside the bounded local datum and these invariants, does not determine the sign of the fixed-start cover-time response.**

More explicitly, write
\[
\Delta_s(G;uv)=\mathbb E_s\tau_{\mathrm{cov}}(G+uv)-\mathbb E_s\tau_{\mathrm{cov}}(G).
\]
The graphs constructed below satisfy \(\Delta_s(G^-_r;uv)<0<\Delta_s(G^+_r;uv)\), and each has exactly \(17r+20\) vertices.

## Assumptions and scope

All walks here are ordinary discrete-time simple random walks on finite, connected, undirected, unweighted, simple graphs. Cover time counts traversed edges until every vertex has been visited; the initial vertex is already visited. The edge \(uv\) is absent prior to its insertion. Radius neighborhoods mean induced subgraphs on all vertices within distance \(r\) of \(\{s,u,v\}\), retaining the labels of the three marks and **degrees in the entire graph**, not merely in the induced neighborhood.

Fix an arbitrary integer \(r\geq1\). Set \(h=r\), \(M=16(h+1)\), and \(L=h+M-1\). Begin both graphs with the center \(c\), three leaves \(s,u,v\), and an additional leaf \(w\), attached individually to \(c\). In \(G^+_r\), attach one path of \(L\) edges to \(c\). In \(G^-_r\), attach a path \(c,a_1,\ldots,a_h=z\) of \(h\) edges and identify its terminal vertex \(z\) with one vertex of a new \(M\)-vertex complete graph, whose other \(M-1\) vertices are new. There are no further edges. The common order is
\[
|V(G^-_r)|=|V(G^+_r)|=h+M+4=17r+20.
\]
The old edge counts are \(m_-=M(M-1)/2+h+4\) and \(m_+=L+4\), respectively.

Every marked vertex has degree one; the central degree is five. The local balls through radius \(r=h\) see the same three marked leaves, center, possibly the extra leaf \(w\), and the first \(h-1\) path vertices. The last visible path vertex has ambient degree two on each side because the next path vertex is just outside the ball. All unseen clique edges therefore lie beyond the radius. Each path/clique branch is connected to the three marked leaves only through \(c\), so \(\operatorname{dist}(s,\{u,v\})=2\) and \(R_{uv}=2\) in both graphs (two unit-resistance bridges in series).

## Proof

**1. A cut-vertex response identity.** Consider any connected remote graph \(H\) attached to three additional pendant vertices \(s,u,v\) at \(c\), and add \(uv\). Write \(m\) for the old number of edges. For a departure from \(c\), regard the ensuing random-walk excursion through its first return to \(c\) as one mark. At each directed edge from \(c\), run an independent artificial rate-one Poisson process of departure marks. Superposition makes the ordered departure directions independent and uniform, exactly as in the walk. The remote and local marks use disjoint clock families.

Let \(T\) be the artificial-time completion of all remote vertices; let \(J\geq0\) be the conditional mean physical suffix length from the last remote discovery to the next return to \(c\). Let \(A\) and \(B\) be the local completion times of \(u,v\), before and after inserting \(uv\). The independent leaf clocks give
\[
\mathbb P(A>t)=2e^{-t}-e^{-2t},\qquad
\mathbb P(B>t)=2e^{-3t/2}-e^{-2t}.
\]
For the second identity, after the first encountered endpoint, a departure toward the already encountered endpoint has probability \(1/2\) of crossing to the unseen endpoint before return to \(c\). Thus the two transient phase decay rates are \(2\) and \(3/2\).

The expected complete excursion length under the old walk is \(2m/\deg(c)\), by the return-time identity; after insertion it is \(2(m+1)/\deg(c)\), since \(\deg(c)\) is unchanged. Wald's stopped-sum argument applies to the marked excursions, because each completion criterion is decided from the marks revealed through the current departure, never future marks. The mean counts of departures through stopping times \(\max(T,A)\) and \(\max(T,B)\) are \(\deg(c)\) times their respective expected artificial times. Subtract the unused suffix of the terminal excursion. A last-completed old leaf has expected suffix one; the new local triangle has expected suffix two; the remote last-completion suffix is \(J\) in either chain.

Writing \(a=\mathbb E e^{-T}\), \(b=\mathbb E e^{-3T/2}\), the tail-integral identity \(\mathbb E\max(T,X)=\mathbb ET+\int_0^\infty\mathbb P(X>t)\mathbb P(T\leq t)dt\) and the two local tails yield, after cancellation of all \(\mathbb E e^{-2T}\) terms,
\[
\boxed{\frac{\Delta_s(G;uv)}2=\mathbb ET-(2m-1)\left(a-\frac23b\right)
-\mathbb E\left[J(e^{-T}-e^{-3T/2})\right].}\tag{1}
\]
The formula can also be derived directly from the exact stopped-excursion identity in Si (2026, Theorem 3.2). The argument above specifies its normalization and the terminal correction. In particular, \(b\leq a\), and the final expectation in (1) is nonnegative.

**2. Negative response of the distant-clique graph.** Work in \(G^-_r\). On first arrival at \(z\), run the walk until it either visits all \(M\) clique vertices or reaches \(c\). Its probability \(p_0\) of covering the clique before \(c\) is at least \(1/2\). Here is an explicit proof.

First suppress the stem and consider ordinary simple random walk on \(K_M\), observed in successive excursions from \(z\) back to \(z\). For any fixed other clique vertex \(q\), the chance that one such excursion encounters \(q\) is
\[
\frac1{M-1}+\frac{M-2}{M-1}\cdot\frac12
=\frac{M}{2(M-1)}\geq\frac12.
\]
The \(1/2\) is the symmetric chance to encounter \(q\) before \(z\) starting from another clique vertex. If \(K\) is the number of complete clique excursions needed to see all clique vertices, independence of excursions and a union bound give \(\mathbb P(K>k)\leq (M-1)2^{-k}\). Consequently
\[
\mathbb EK\leq\lceil\log_2(M-1)\rceil+2\leq(M-1)/2\quad(M\geq32).
\]
The final elementary bound follows by checking the initial interval and the monotonic gaps between successive powers of two.

When the stem is restored, each return to \(z\) precedes a decision: leave into a genuine clique excursion, or be killed by reaching \(c\) along the stem. A departure from \(z\) into the stem has probability \(1/M\), and conditional on it, gambler's ruin on the \(h\)-edge stem gives probability \(1/h\) of hitting \(c\) before \(z\). Failed stem attempts return to \(z\). Thus the chance of reaching \(c\) before the **next genuine clique excursion** is exactly
\[
\frac1{h(M-1)+1}.
\]
Couple the genuine clique excursions with the unrestricted \(K_M\) sequence; an expected-count union bound gives
\[
1-p_0\leq\frac{\mathbb EK}{h(M-1)+1}
\leq\frac{M-1}{2[h(M-1)+1]}<\frac12.
\]

A remote excursion from \(c\) down the stem hits \(z\) before returning to \(c\) with probability \(1/h\). Therefore a departure mark that visits **every** clique vertex before returning to \(c\) has probability at least \(1/(2h)\); its Poisson thinned arrival time \(S\) is exponential of rate \(\kappa\geq1/(2h)\). The first mark visiting \(w\) has independent time \(W\sim\operatorname{Exp}(1)\). The remote completion time satisfies \(T\leq\max(S,W)\). Hence
\[
\mathbb ET\leq2h+1,\qquad
 a\geq\mathbb E e^{-(S+W)}
=\frac{\kappa}{2(1+\kappa)}\geq\frac1{4h+2}.
\]
Since \(a-2b/3\geq a/3\), (1) gives
\[
\frac{\Delta_s(G^-_r;uv)}2\leq
2h+1-\frac{M(M-1)+2h+7}{3(4h+2)}<0.
\]
The strict inequality holds for \(M=16(h+1)\): indeed \(M(M-1)>3(4h+2)(2h+1)\) for all \(h\geq1\), with considerable slack.

**3. Positive response of the long-path graph.** In \(G^+_r\), the remote branch consists of \(w\) and a path of length \(L=h+M-1\). The first successful path-completing departure mark appears at \(X\sim\operatorname{Exp}(1/L)\), independently of the first \(w\)-mark \(Y\sim\operatorname{Exp}(1)\), by gambler's ruin and Poisson thinning. Thus \(T=\max(X,Y)\). If the path completes last, the last discovery is at its endpoint and its conditional expected return to \(c\) is \(L^2\); if \(w\) completes last, this suffix is one. For \(t>0\), put
\[
A_L(t)=\frac1{1+tL}-\frac1{L+1+tL},\qquad
B_L(t)=\frac1{1+t}-\frac{L}{L+1+tL}.
\]
Direct integration of the two competing exponential densities gives \(A_L(t)=\mathbb E[e^{-tT}\mathbf1_{\{X>Y\}}]\) and \(B_L(t)=\mathbb E[e^{-tT}\mathbf1_{\{Y>X\}}]\). Hence \(a=A_L(1)+B_L(1)\), \(b=A_L(3/2)+B_L(3/2)\),
\[
\mathbb ET=L+\frac1{L+1},\quad
\mathbb E[J(e^{-T}-e^{-3T/2})]
=L^2[A_L(1)-A_L(3/2)]+B_L(1)-B_L(3/2).
\]
Substituting into (1) with \(m=L+4\), rational simplification yields the exact expression
\[
\boxed{\Delta_s(G^+_r;uv)=\frac{2\bigl(345L^5+676L^4-489L^3-887L^2-336L-44\bigr)}{15(L+1)(2L+1)(3L+2)(5L+2)}.}\tag{2}
\]
It is strictly positive for every integer \(L\geq2\): putting \(z=L-2\geq0\), its numerator polynomial becomes
\[
345z^5+4126z^4+18719z^3+40003z^2+39480z+13680>0.
\]
Our \(L=h+M-1\) is at least \(32\). This proves the opposite signs together with the exact same-order neighborhood correspondence, for every \(r\geq1\). \(\square\)

## Verification

The self-contained Python file `verify.py` checks the graph construction, the local ambient-degree-labelled neighborhoods and matched scalars for a range of radii, the strict sign inequalities as integer identities, and an independent exact-rational visited-set Markov-chain recurrence at a smaller same-order witness. The smaller witness has \(h=1\), \(M=3\), and \(L=3\), and is used only as a finite regression test, not as a proof for arbitrary radius.

To replay without external packages, run `python3 verify.py` in the directory containing this result and the checker. The infinite proof is the analytical reasoning above; finite tests do not replace it.

## Relationship to prior work

Si, *Nonlocality of Cover-Time Changes Under Edge Addition* (2026), arXiv:2608.27474, proves opposite signs at every radius and matches marked degrees, marked distance, and endpoint resistance, but the two graphs have **different** orders (Theorem 1.1). The article specifically lists equal-order nonlocality as an open problem (Section 7, item 2). Its Theorem 3.2 provides the cut-vertex marked-excursion framework; equation (1) reproduces this framework with its local completion and unused-suffix terms rather than presenting it as a new identity. The new ingredient is an equal-order **clique-versus-path remote-branch construction** with a uniform small-killing bound for a clique excursion, and the exact positive-path response (2).

Barlow, Ding, Nachmias and Peres (2011) establish broad consequences of adding edges for cover times, including a universal factor bound, but not this identical-order, arbitrarily prescribed-radius sign separation. Ding, Lee and Peres (2012) study cover times up to universal multiplicative factors through Gaussian free fields; such coarse comparisons do not specify the sign of a single-edge additive response. The 2026 source's general perturbation formula can, in principle, be evaluated on our graphs, but does not itself establish the opposite signs or matching order for this construction.

## Limitations

The result concerns **fixed-start expected cover time**; it does not establish an analogous sign separation for the worst-start cover time. The two graphs have different total edge counts, degree sequences outside the visible ball, and internal structures. They match order, the full marked radius-\(r\) degree-labelled datum, marked degrees/distance, and endpoint resistance; no equality of other global invariants is claimed. The construction is not optimized for minimum graph order. The proof depends on elementary finite-state return/excursion identities and on the full mathematical content (not merely the abstract) of the cited marked-excursion framework. A prior theorem using a different formulation of equal-order local indistinguishability could affect historical priority; independent validation has not been performed.

## References

1. I. M. Si, *Nonlocality of Cover-Time Changes Under Edge Addition*, arXiv:2608.27474 (first public version, 2026-08-19), https://arxiv.org/abs/2608.27474. Relevant: Theorems 1.1, 3.2, Sections 3 and 7.
2. M. T. Barlow, J. Ding, A. Nachmias and Y. Peres, *The Evolution of the Cover Time*, Combinatorics, Probability and Computing 20 (2011), 331–345, https://doi.org/10.1017/S0963548310000489.
3. J. Ding, J. R. Lee and Y. Peres, *Cover times, blanket times, and majorizing measures*, Annals of Mathematics 175 (2012), 1409–1471, https://doi.org/10.4007/annals.2012.175.3.8.
