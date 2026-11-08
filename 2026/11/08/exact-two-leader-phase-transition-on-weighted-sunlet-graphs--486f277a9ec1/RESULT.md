# Exact two-leader phase transition on weighted sunlet graphs

## Finding

Let \(n\ge3\) be an integer and \(t>0\). Form the weighted sunlet graph \(S_n(t)\) from the cycle \(C_n\) with vertices \(c_0,\ldots,c_{n-1}\), giving every cycle edge conductance \(1\), and attach a leaf \(\ell_i\) to each \(c_i\) with edge conductance \(t\). Exactly two distinct vertices are fixed as noise-free leaders. For a leader set \(A\) define
\[
J(A)=\operatorname{tr}\bigl(L_{V\setminus A,V\setminus A}^{-1}\bigr),
\]
where \(L\) is the unnormalized, weighted combinatorial Laplacian.

Put
\[
R_n=\frac{\lfloor n^2/4\rfloor}{n},\qquad
\tau_n=\frac{3}{1+2(n-3)R_n}.
\]
A pair of distinct core indices is *diametral* when their cyclic distance equals \(\lfloor n/2\rfloor\). The complete classification of global minimizers is:

- If \(0<t<\tau_n\), precisely the core–leaf pairs \(\{c_i,\ell_j\}\) with diametral indices are optimal.
- If \(t>\tau_n\), precisely the core–core pairs \(\{c_i,c_j\}\) with diametral indices are optimal.
- If \(t=\tau_n\), precisely the union of these two classes is optimal.

No leaf–leaf pair, nor a core and its own leaf, is optimal. For odd \(n\), the two types have respectively \(2n\) and \(n\) optimizer sets; for even \(n\), they have respectively \(n\) and \(n/2\) sets. At equality the counts add.

The minimal objective is the lesser of the following explicit values (with \(r=R_n\)):
\[
\begin{aligned}
J_{CC}&=\frac{n}{t}+\frac{n^2-2nr-2}{3},\\
J_{CL}&=\frac{n-1}{t}+\frac{n^2-1}{3}
-\frac{r\bigl[t(2nr+1)/3+1\bigr]}{1+tr}.
\end{aligned}
\]
In particular, \(\tau_3=3\), \(\tau_4=1\), and \(\tau_n\sim6/n^2\) as \(n\to\infty\). At unit leaf conductance the optimum is core–leaf for \(n=3\), tied core–leaf/core–core for \(n=4\), and core–core for \(n\ge5\).

## Assumptions and scope

All \(2n\) graph vertices are eligible; there are exactly two distinct noise-free leaders, not at most two. Every cycle edge has conductance exactly \(1\); every pendant edge has the same prescribed conductance \(t>0\). The leader–follower objective is the unscaled trace of the inverse of the follower principal submatrix of the original graph Laplacian. If the underlying stochastic model uses a one-half variance normalization, all objectives are divided by two and the optimizer sets are unchanged. This is a theorem about the entire integer family \(n\ge3\) and all positive real \(t\), not an inference from finite samples.

## Proof

**1. A cycle Green kernel.** Fix cycle core \(c_0\), ground it, and index the remaining cores \(1,\ldots,n-1\). The inverse \(H\) of the cycle's grounded Laplacian is
\[
H_{ij}=\frac{\min(i,j)[n-\max(i,j)]}{n}.
\]
Directly summing the diagonal, column, and squared column gives, for \(b\in\{1,\ldots,n-1\}\),
\[
\operatorname{tr}H=\frac{n^2-1}{6},\quad
r=H_{bb}=\frac{b(n-b)}n,\quad
\sum_i H_{ib}=\frac{nr}{2},\quad
q=(H^2)_{bb}=\frac{r(2nr+1)}6.
\]
For example, with \(b\) measured from grounded core \(0\), the column-square identity follows by evaluating \(q=(n-b)^2 n^{-2}\sum_{j=1}^{b}j^2+b^2 n^{-2}\sum_{j=1}^{n-b-1}j^2\); the remaining identities use the corresponding sums of first powers. These formulas are exact. The quantities \(r\) and \(q\) depend only on the cyclic distance \(d\) between the two underlying core indices, with \(r=d(n-d)/n\).

**2. Exhaustion of all two-vertex types.** Let CC mean two distinct cores, CL a core and a leaf, and LL two distinct leaves. Every pair belongs to exactly one type. Eliminating an *unselected* leaf by its Schur complement contributes \(1/t\) to the inverse trace and, if its core is retained, adds the core's diagonal inverse entry. An unselected leaf whose core is grounded contributes \(1/t\) and no core variance. A *selected* leaf instead provides a shunt of conductance \(t\) at its retained core.

For CC at cyclic separation \(d\ge1\), the remaining core problem splits into two Dirichlet paths of lengths \(d-1\) and \(n-d-1\), whose total inverse trace is \([d^2+(n-d)^2-2]/6\). Including the leaves yields
\[
J_{CC}(r)=\frac nt+\frac{n^2-2nr-2}{3}.
\]

For CL with distinct underlying indices, ground the selected core \(a\), and let \(b\ne a\) be the core of the selected leaf. The retained-core matrix is \(H^{-1}+t e_b e_b^\top\). The rank-one inversion identity gives
\[
\operatorname{tr}(H^{-1}+te_be_b^\top)^{-1}=\operatorname{tr}H-\frac{tq}{1+tr},\qquad
[(H^{-1}+te_be_b^\top)^{-1}]_{bb}=\frac{r}{1+tr}.
\]
The leaf \(\ell_b\) is absent, so its core variance must be subtracted once. Therefore
\[
J_{CL}(r)=\frac{n-1}{t}+\frac{n^2-1}{3}-\frac{2tq+r}{1+tr}.
\]
A selected core and its *own* leaf yield \(J_{CL}(0)=(n-1)/t+(n^2-1)/3\), strictly larger than \(J_{CL}(r)\) for any \(r>0\).

For LL, select \(\ell_a,\ell_b\) with \(a\ne b\). All cores remain, with core precision \(K=L_{C_n}+t e_a e_a^\top+t e_b e_b^\top\). Write their potential vector as \(x_i=y_i+z\), where \(y_a=0\) and \(z=x_a\). The core quadratic form, including the two leaf shunts, becomes
\[
y^\top H^{-1}y+t z^2+t(z+y_b)^2
=y^\top(H^{-1}+\tfrac t2e_be_b^\top)y+2t(z+y_b/2)^2.
\]
Thus the reduced covariance of \(y\) is \(K_y=(H^{-1}+\tfrac t2e_be_b^\top)^{-1}\), and conditional variance of \(z\) is \(1/(2t)\). It follows that
\[
\begin{aligned}
\operatorname{tr}K^{-1}&=\operatorname{tr}K_y-\sum_i(K_y)_{ib}+\frac n4(K_y)_{bb}+\frac{n}{2t},\\
(K^{-1})_{aa}+(K^{-1})_{bb}&=\frac1t+\frac12(K_y)_{bb}.
\end{aligned}
\]
The same rank-one identity, together with the three finite sums above, gives
\[
J_{LL}(r)=\frac{2n-3}{t}+\frac{n^2-1}{3}-\frac{2tq+(n+1)r}{2+tr}.
\]
This accounts for the unselected \(n-2\) leaves and subtracts the two selected leaves' missing core-variance contributions; no cases are omitted.

**3. All types prefer maximum cyclic separation.** On \(0<r\le R_n\), \(J_{CC}\) is strictly decreasing in \(r\). Since \(q=r(2nr+1)/6\), the subtracted terms in both \(J_{CL}\) and \(J_{LL}\) have the form \((Ar^2+Br)/(c+tr)\), where \(A=2nt/3>0\), \(B>0\), and \(c\in\{1,2\}\). Their derivative is
\[
\frac{At r^2+2Ac r+Bc}{(c+tr)^2}>0.
\]
Hence both objectives are strictly decreasing in \(r\). Since \(r=d(n-d)/n\) is strictly increasing for integer \(1\le d\le\lfloor n/2\rfloor\), each type, separately, is optimized exactly at diametral indices.

**4. Exclude LL and locate the exact phase threshold.** Subtraction of the full rational expressions at a common \(r>0\) gives
\[
J_{LL}(r)-J_{CL}(r)
=\frac{[(2n-6)r^2+r]t^2+(6n-15)rt+6n-12}{3t(1+tr)(2+tr)}>0
\]
for all \(n\ge3\), \(r,t>0\). Every coefficient in the numerator is strictly positive except the harmless \((2n-6)r^2\) term at \(n=3\). LL therefore cannot minimize the global objective. Similarly,
\[
J_{CL}(r)-J_{CC}(r)=\frac{t[1+2(n-3)r]-3}{3t(1+tr)}.
\]
At \(r=R_n\) this expression changes sign *once*, at the strictly positive \(\tau_n\) displayed in the Finding. Strict decrease with distance in each type and the strict LL comparison establish every equality case, type and optimizer count, completing the proof.

## Verification

The included `verify.py` is complete and self-contained apart from its stated Python 3 and SymPy dependency. Running `python verify.py` checks the two rational comparison identities symbolically and, independently of those formulas, inverts every grounded Laplacian for all possible two-leader sets for \(3\le n\le8\), at several positive rational conductances including the exact phase boundaries. It compares every inverse trace to the claimed formula and checks the complete optimizer type, maximal distance and multiplicity. The run reports 1,797 exact rational grounded-matrix comparisons and 29 exhaustive finite parameter classifications. The universal assertions are established by the displayed analytical proof, not by this finite replay.

## Relationship to prior work

Lin, Fardad and Jovanović [1] formulate the noise-free leader objective and general convex-relaxation/greedy algorithms; their inspected formulation and examples do not provide this weighted sunlet classification. Fitch and Leonard [2] develop joint centrality and explicitly treat paths and cycles; the inspected graph-specific results are not on cycles with one weighted pendant edge at *every* core. Patterson, McGlohon and Dyagilev [3] solve weighted paths and rings algorithmically; those graph classes are not sunlets. Patterson, Yi and Zhang [4] provide general resistance-distance formulas and evaluate certain cycles, paths and trees, but their inspected graph-family evaluations do not state the core–leaf/core–core transition on weighted sunlets. Their general methods can be used as alternative starting points for independent derivations, but do not by themselves provide the evaluated phase boundary or optimizer multiplicities. The sunlet identity \(C_n\circ K_1\) and its alternate nomenclature are standard [5]. The present claim concerns the exact weighted phase boundary and exhaustive optimizer sets, not the general selection framework, general resistance formula, or the fact that diametral leaders are optimal on an unadorned cycle.

## Limitations

This result does not cover nonuniform pendant weights, variable cycle conductances, more than two leaders, finite-gain or noisy leaders, continuous-time mixing, or other objective normalizations without explicit rescaling. No statement is made about computational complexity for arbitrary weighted graphs. The mathematical proof has not received independent audit. Literature indexing may omit an equivalent earlier specialization; absence of a search hit does not establish publication priority.

## References

[1] F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first publicly posted 2013-02-03, https://arxiv.org/abs/1302.0450.

[2] K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, https://arxiv.org/abs/1407.1569.

[3] S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, https://arxiv.org/abs/1412.6595.

[4] S. Patterson, Y. Yi, Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, https://arxiv.org/abs/1708.06873.

[5] *Sunlet Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/SunletGraph.html.
