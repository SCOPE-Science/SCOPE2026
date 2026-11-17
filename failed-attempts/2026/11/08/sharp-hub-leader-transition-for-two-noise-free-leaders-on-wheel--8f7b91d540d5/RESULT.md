# Sharp hub-leader transition for two noise-free leaders on wheel graphs

## Finding

**Theorem.** For each integer \(m\ge3\), let \(W_{m+1}=K_1\vee C_m\) be the unweighted wheel with hub \(h\) and \(m\) rim vertices. A pair \(S\) of noise-free leaders minimizes the grounded-Laplacian inverse trace \(J(S)=\operatorname{tr}(L_{V\setminus S,V\setminus S}^{-1})\) exactly in the following cases:

- \(m=3\): all six pairs, of objective \(3/4\).
- \(4\le m\le6\): the two leaders are rim vertices at maximum cyclic separation \(d=\lfloor m/2\rfloor\), and no other pair is optimal. The numbers of optimal pairs for \(m=4,5,6\) are respectively \(2,5,3\).
- \(m\ge7\): the pair consists of the hub and one rim vertex, and no other pair is optimal; there are exactly \(m\) optimal pairs.

Consequently the globally optimal leader geometry changes sharply at seven rim vertices, despite the hub being the only vertex of degree growing with \(m\). The minimum objective is \(31/30,67/44,2\) at \(m=4,5,6\) and \(954/377\) at \(m=7\), respectively.

## Assumptions and scope

All edges carry unit conductance. There are precisely two distinct noise-free leaders, removed by grounding the corresponding rows and columns of the full combinatorial Laplacian \(L\). Every remaining vertex is a noisy follower of equal noise intensity, with the standard objective taken as the inverse trace (without a factor \(1/2\)). The rim is a simple cycle; for \(m=3\) the wheel is \(K_4\). The result addresses only this fixed graph, exact budget, and unweighted model; no claims about arbitrary leader budgets or adjustable edge weights are made.

Write \(T_\ell\) for the \(\ell\times\ell\) tridiagonal matrix with diagonal \(3\) and adjacent off-diagonals \(-1\). For \(\ell\ge0\) define \(h_\ell=\operatorname{tr}(T_\ell^{-1})\), \(z_\ell=T_\ell^{-1}{\bf1}\), \(f_\ell={\bf1}^{\mathsf T}z_\ell\), and \(g_\ell=z_\ell^{\mathsf T}z_\ell\); all are zero when \(\ell=0\).

## Proof

**Step 1 (complete symmetry reduction).** The wheel automorphisms act transitively on hub–rim pairs and on rim pairs at any fixed smaller cyclic separation \(1\le d\le\lfloor m/2\rfloor\). For a hub–rim pair, the follower set is a path of \(m-1\) rim vertices and the grounded matrix is \(T_{m-1}\); therefore \(J_{hr}=h_{m-1}\).

For two rim leaders at separation \(d\), the two follower rim arcs have \(a=d-1\) and \(b=m-d-1\) vertices, with \(a+b=m-2\). Taking the hub as the final coordinate yields the grounded matrix
\[
M=\begin{pmatrix}T_a&0&-{\bf1}\\0&T_b&-{\bf1}\\-{\bf1}^{\mathsf T}&-{\bf1}^{\mathsf T}&m\end{pmatrix}.
\]
Its Schur pivot \(D=m-f_a-f_b\) is positive, because \(M\) is positive definite. Block inversion (including empty blocks) gives the exact formula
\[
J_{rr}(d)=h_a+h_b+\frac{1+g_a+g_b}{m-f_a-f_b}. \tag{1}
\]
These formulas exhaust all choices of two leaders.

**Step 2 (exact small instances).** Repeated exact tridiagonal inversion in equation (1), or direct exact inversion of the grounded wheel matrices, gives the following complete orbit table. In each row the rim-pair values are ordered by increasing cyclic separation \(d\).

| Rim size \(m\) | Hub–rim | Rim–rim values for \(d=1,2,\ldots,\lfloor m/2\rfloor\) |
|---|---|---|
| \(4\) | \(25/21\) | \(5/4,\ 31/30\) |
| \(5\) | \(18/11\) | \(62/33,\ 67/44\) |
| \(6\) | \(25/12\) | \(453/176,\ 509/240,\ 2\) |
| \(7\) | \(954/377\) | \(383/116,\ 885/319,\ 31/12\) |
| \(8\) | \(2939/987\) | \(4927/1218,\ 1451/420,\ 425/132,\ 221/70\) |

All comparisons in this rational table are strict except within a symmetry orbit. The case \(m=3\) is \(K_4\): its grounded matrix for any two leaders has diagonal \(3\) and off-diagonal \(-1\), giving \(J=3/4\). This settles \(3\le m\le8\).

**Step 3 (a uniform strict bound for every \(m\ge9\)).** Set \(r=(3+\sqrt5)/2\), so \(r>1\). The diagonal Green function of \(T_\ell\), derivable by solving the second-order recurrence with zero boundary values, is
\[
(T_\ell^{-1})_{ii}=\frac{(1-r^{-2i})(1-r^{-2(\ell+1-i)})}{\sqrt5(1-r^{-2(\ell+1)})}, \qquad 1\le i\le\ell.
\]
It implies the two-sided trace estimates
\[
\frac{\ell-2/(r^2-1)}{\sqrt5}\le h_\ell\le\frac\ell{\sqrt5}. \tag{2}
\]
Indeed, each diagonal term is at most \(1/\sqrt5\), and is at least \([1-r^{-2i}-r^{-2(\ell+1-i)}]/\sqrt5\); summing the tails gives (2). The solution of \(T_\ell z={\bf1}\) is
\[
z_{\ell,i}=1-\frac{r^i+r^{\ell+1-i}}{r^{\ell+1}+1},
\]
so \(f_\ell\ge\ell-2/(r-1)\), including the empty case. Thus for two rim leaders
\[
f:=f_a+f_b\ge m-2-\frac4{r-1}=m-2\sqrt5, \qquad 0<D=m-f\le2\sqrt5. \tag{3}
\]
By Cauchy–Schwarz on the \(m-2\) rim follower coordinates,
\[
g_a+g_b\ge\frac{f^2}{m-2}\ge\frac{(m-2\sqrt5)^2}{m-2},\qquad(m\ge9). \tag{4}
\]
The second inequality uses \(f\ge m-2\sqrt5>0\). Combining equations (1)–(4) yields
\[
J_{rr}(d)\ge\frac{m-2-4/(r^2-1)}{\sqrt5}+\frac{1+(m-2\sqrt5)^2/(m-2)}{2\sqrt5}. \tag{5}
\]
By (2), \(J_{hr}=h_{m-1}\le(m-1)/\sqrt5\). Hence it suffices that
\[
B(m):=\frac{1+(m-2\sqrt5)^2/(m-2)}{2\sqrt5}>\frac{1+4/(r^2-1)}{\sqrt5}=\frac65-\frac1{\sqrt5}. \tag{6}
\]
The function \((x-2\sqrt5)^2/(x-2)\) is strictly increasing for \(x\ge9\), since its derivative equals \((x-2\sqrt5)(x+2\sqrt5-4)/(x-2)^2>0\). At \(x=9\), the difference between the sides of (6) is \((61\sqrt5-132)/35>0\); the last sign is exact since \(5\cdot61^2>132^2\). Thus (6), and consequently \(J_{rr}(d)>J_{hr}\), hold for every integer \(m\ge9\) and every separation \(d\). Together with the finite table, the theorem follows.

## Verification

Run `python3 verify_wheel.py` with Python 3.9 or later; it uses only the standard library. It constructs the full wheel Laplacian and obtains inverse traces by exact-rational Gauss–Jordan elimination. It exhaustively compares every pair of leader vertices for rim sizes \(4\) through \(10\), checks the independent Schur expression against direct inverses for all rim sizes \(4\) through \(18\), reproduces the exact rational small-instance table, and checks the integer witness in equation (6). The finite computations corroborate the displayed exact formulas; only the symbolic argument of Step 3 proves the unbounded range.

## Relationship to prior work

The stochastically forced consensus leader-selection framework and the inverse-trace objective appear in Lin, Fardad and Jovanović (2013). Fitch and Leonard (2014) provide a general graph-resistance/joint-centrality expression and exact examples for other graph families; Patterson, McGlohon and Dyagilev (2014) treat path and ring formations. None of the inspected relevant parts of those sources gives an exact unweighted-wheel two-leader phase transition or a proof that hub-containing pairs become uniquely optimal at seven rim vertices. A general-purpose evaluation formula for any fixed graph is not, by itself, a comparison of all orbit classes uniformly over an infinite graph family. Related wheel-polytope and graph-domination results address different objectives. This is a literature comparison on inspected evidence, not a claim of exhaustive priority.

## Limitations

The theorem assumes the specified unweighted wheel and exactly two noise-free leaders; no optimality statement is made about noisy leaders, different weights, different noise covariances, or different budgets. The Green-function bounds are intentionally coarse and establish strict hub dominance for \(m\ge9\), with \(m=7,8\) settled separately. Independent mathematical review and an exhaustive bibliographic priority check have not been performed. Potential equivalent results in unindexed literature remain a risk.

## References

1. F. Lin, M. Fardad, and M. R. Jovanović, *Algorithms for leader selection in stochastically forced consensus networks*, arXiv:1302.0450v1, first posted 2013-02-03. https://arxiv.org/abs/1302.0450
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569v1, first posted 2014-07-07. https://arxiv.org/abs/1407.1569
3. S. Patterson, N. McGlohon, and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595v1, first posted 2014-12-20. https://arxiv.org/abs/1412.6595
4. S. Patterson, Y. Yi, and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873v1, first posted 2017-08-23. https://arxiv.org/abs/1708.06873
