# Four vertices are necessary and sufficient for fourth-norm amplification of the heat square function on an unweighted graph

## Finding

Let \(G\) be any connected, simple, unweighted graph on \(n\) vertices, with combinatorial Laplacian \(L\), heat semigroup \(T_t=e^{-tL}\), and orthogonal projection \(F\) onto constant functions. For a complex signal \(f\), set
\[
G_2(f)(v)=\left(\int_0^\infty |t\partial_tT_tf(v)|^2\,\frac{dt}{t}\right)^{1/2}.
\]
All vertex norms use **counting measure** (the same ratio results from normalized counting measure). For every connected graph with \(n\le3\),
\[
\|G_2(f)\|_4\le \tfrac12\|f-Ff\|_4.
\]
This fails already on the path \(P_4\). For the vertex-ordered signal \(f=(1,1,-1,-1)\),
\[
(G_2(f)(v)^2)_{v=1}^4=(5,3,3,5)/16,\qquad
\frac{\|G_2(f)\|_4^4}{\|f\|_4^4}=\frac{17}{256}>\frac1{16}.
\]
Therefore the **least number of vertices for which the \(L^4\) square-function norm strictly exceeds its universal \(L^2\) value \(1/2\) is four**. This is a sharp *onset statement*, not a determination of the full \(P_4\) operator norm.

## Assumptions and scope

The graphs are finite, connected, simple, and **unweighted**. The generator is the combinatorial graph Laplacian, not a normalized Laplacian or an arbitrary weighted Markov generator. Inputs may be complex; \(G_2\) is the time-derivative square function, not a spatial-gradient square function. The centering operator \(F\) is needed because constants are annihilated by the derivative. For \(n=1\), both sides vanish. Vertex \(L^4\) norms are \((\sum_v |h(v)|^4)^{1/4}\).

## Proof

**Spectral kernel.** Write \(f-Ff=\sum_{j=1}^r f_j\), where \(Lf_j=\lambda_jf_j\) and \(\lambda_j>0\), with multiplicities allowed. Direct integration yields the pointwise identity
\[
G_2(f)(v)^2=\sum_{j,k=1}^r\frac{\lambda_j\lambda_k}{(\lambda_j+\lambda_k)^2}f_j(v)\overline{f_k(v)},\qquad
\int_0^\infty t e^{-at}\,dt=a^{-2}.
\]
The first identity includes every cross term and is valid for arbitrary complex \(f\).

**Up to three vertices.** Every connected graph of order two or three is \(K_2\), \(K_3\), or the path \(P_3\). On either complete graph all positive eigenvalues of \(L\) coincide, so the spectral kernel equals \(1/4\) in every entry and \(G_2(f)(v)=|f(v)-Ff(v)|/2\). For the path \(P_3\), choose its normalized real nonconstant eigenvectors
\[
u=(1,0,-1)/\sqrt2,\quad w=(1,-2,1)/\sqrt6,\quad Lu=u,\quad Lw=3w.
\]
Write \(f-Ff=xu+yw\), with arbitrary complex \(x,y\), and \(R=\operatorname{Re}(x\overline y)\). The spectral-kernel formula gives
\[
G_2(f)(v)^2=\tfrac14(|x|^2u_v^2+|y|^2w_v^2)+\tfrac38R u_vw_v.
\]
An expansion, with no sign assumption, yields the exact deficit identity
\[
\frac{\|f-Ff\|_4^4}{16}-\|G_2(f)\|_4^4
=\frac7{384}R^2\ge0.
\]
It also identifies equality on \(P_3\) precisely when \(\operatorname{Re}(x\overline y)=0\), including pure eigenmodes and their quadrature-phase mixtures.

**Four vertices.** On \(P_4\), let \(f=(1,1,-1,-1)\). It is mean zero. Its two active Laplacian eigenvalues are \(2-\sqrt2\) and \(2+\sqrt2\), with spectral components
\[
f_-=(\tfrac{1+\sqrt2}2,\tfrac12,-\tfrac12,-\tfrac{1+\sqrt2}2),\qquad
f_+=(\tfrac{1-\sqrt2}2,\tfrac12,-\tfrac12,\tfrac{-1+\sqrt2}2).
\]
Their sum equals \(f\), and their cross-kernel coefficient is
\[\frac{(2-\sqrt2)(2+\sqrt2)}{((2-\sqrt2)+(2+\sqrt2))^2}=\frac18.\]
Substituting the two components into the spectral formula gives \(G_2(f)^2=(5,3,3,5)/16\). Consequently \(\|G_2(f)\|_4^4=17/64\) and \(\|f\|_4^4=4\), so the fourth-power ratio is \(17/256\), strictly exceeding \(1/16\). Together with the all-graph result for \(n\le3\), this proves the minimality of four.

## Verification

A standalone exact-arithmetic SymPy checker reproduces the complete \(P_3\) complex-coefficient deficit as a polynomial identity, diagonalizes the \(P_4\) Laplacian with the stated real eigenvalues, checks the two components and pointwise \(G_2^2\) values, and verifies \(17/256>1/16\). No numerical minimization, finite enumeration beyond the elementary graph list, or unverified computation enters the proof. Run `python3 check.py` with SymPy installed.

## Relationship to prior work

Lai, Li, and Li (first posted November 7, 2026) develop dimension-free Hilbert-valued Littlewood–Paley semigroup estimates and identify the universal \(L^2\) normalization \(1/2\); their paper does not present this small-graph onset classification. Earlier general Littlewood–Paley theory provides norm bounds but does not by itself identify the first connected unweighted graph where the \(L^4\) norm exceeds \(1/2\). Search results concerning graph heat variation or gradient norms address different operators. The distinction is the exact minimal **graph order** and complex-input equality identity, not the general existence of \(L^p\) amplification.

## Limitations

The result is restricted to connected, unweighted, undirected graphs and to the heat derivative square function at output/input exponent four and time exponent two. The value \(17/256\) belongs to one explicit \(P_4\) witness; no sharp \(P_4\) operator norm is asserted. The graph size cutoff does not address weighted or directed graphs. The literature search is not a proof of uniqueness against every unindexed equivalent calculation. Independent mathematical validation has not been performed.

## References

1. X. Lai, B. Li, J. Li, *Optimal orders for Hilbert-valued Littlewood–Paley functions of symmetric semigroups*, arXiv:2611.10710 (first posted 2026-11-07), https://arxiv.org/abs/2611.10710.
2. Q. Xue, X. Peng, K. Yabuta, *On the theory of multilinear Littlewood–Paley g-function*, J. Math. Soc. Japan **67** (2015), 535–559, https://doi.org/10.2969/jmsj/06720535. This paper treats multilinear estimates, not the graph-size onset asserted here.
