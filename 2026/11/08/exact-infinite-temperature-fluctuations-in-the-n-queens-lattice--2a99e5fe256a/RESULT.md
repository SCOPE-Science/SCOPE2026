# Exact infinite-temperature fluctuations in the \(N\)-queens lattice gas

## Finding

For every integer \(N\geq2\), choose exactly \(N\) occupied sites uniformly from an \(N\times N\) square board with open boundaries. Let \(H_N\) be the number of unordered pairs of occupied sites that attack one another horizontally, vertically, or along either diagonal (each pair counted once). Then \(\mathbb E H_N=(5N-1)(N-1)/(3(N+1))\), and its **exact variance** is

\[
\operatorname{Var}(H_N)=
\begin{cases}
\displaystyle\frac{(N-2)(N-1)(31N^5-75N^4+32N^3+24N^2-24N-6)}{18(N+1)^2(N^2-3)(N^2-2)},&N\text{ even},\\[6pt]
\displaystyle\frac{(N-2)(N-1)^2(31N^4-44N^3-12N^2+12N-3)}{18(N+1)^2(N^2-3)(N^2-2)},&N\text{ odd}.
\end{cases}
\]

In particular,
\[
\lim_{N\to\infty}\frac{\operatorname{Var}(H_N)}{N}=\frac{31}{18}.
\]

For the canonical Gibbs model with physical energy \(E_N=JH_N\), coupling \(J>0\), temperature \(T>0\), and \(k_B=1\), writing \(C_N(T)=\partial_T\langle E_N\rangle_T\), this yields the rigorously ordered limit
\[
\boxed{\lim_{N\to\infty}\lim_{T\to\infty}\frac{T^2 C_N(T)}{NJ^2}=\frac{31}{18}.}
\]
For each fixed \(N\), the inner limit equals \(\operatorname{Var}(H_N)/N\). The order of the two limits is part of the statement; no uniform-in-\(N\) finite-temperature expansion is asserted.

## Assumptions and scope

The board consists of \(\{0,\ldots,N-1\}^2\), with no identification of opposite edges. Every \(N\)-element subset is allowed and equally weighted **only at infinite temperature**; there is no requirement of one queen per row or column. Attacks are counted per unordered pair, not per line containing more than one queen as a single penalty. A pair cannot attack along two distinct directions. In the Gibbs ensemble, each configuration has probability proportional to \(\exp(-JH_N/T)\); the occupation number remains exactly \(N\).

The result is an equilibrium energy-fluctuation and high-temperature specific-heat result, not a claim about phase transitions, finite-temperature limits at fixed \(T\), or the alternative permutation ensemble.

## Proof

Write \(M=N^2\). Form the *queen-attack graph* \(G_N\): its vertices are board squares, with an edge for every attacking pair. Denote its number of edges by \(S_N\), and its number of unordered incident edge pairs (two distinct graph edges meeting at a vertex) by \(W_N\). Let \(X_e\) indicate that both endpoints of edge \(e\) are occupied. Then \(H_N=\sum_{e\in E(G_N)}X_e\).

**Step 1: geometric incidence identities.** At the square \((i,j)\), put \(a_{ij}=|i-j|\) and \(b_{ij}=|i+j-(N-1)|\). Its attack-graph degree is exactly
\[
d_{ij}=4(N-1)-a_{ij}-b_{ij}.
\]
Indeed, the two row/column contributions are each \(N-1\), and the lengths of its two diagonals are \(N-a_{ij}\) and \(N-b_{ij}\). Counting degrees gives the already-known attack-pair total
\[
S_N=\frac12\sum_{i,j}d_{ij}=\frac{N(N-1)(5N-1)}{3}.
\]
To determine the previously needed second incidence count, use
\[
\sum_{i,j}a_{ij}=\frac{N(N^2-1)}3,\qquad
\sum_{i,j}a_{ij}^2=\frac{N^2(N^2-1)}6.
\]
Reflection makes the corresponding two sums for \(b\) identical. The mixed term has the parity-sensitive exact form
\[
\sum_{i,j}a_{ij}b_{ij}=
\begin{cases}
N^2(N^2-4)/12,&N\text{ even},\\
(N^2-1)(N^2-3)/12,&N\text{ odd}.
\end{cases}
\]
For completeness, set \(u=i-(N-1)/2\) and \(v=j-(N-1)/2\). Then \(a_{ij}b_{ij}=|u^2-v^2|\). If \(N=2m+1\), grouping coordinates by their absolute values gives
\[
4\sum_{r=1}^{m}r^2+8\sum_{1\leq s<r\leq m}(r^2-s^2)
=\frac{(N^2-1)(N^2-3)}{12}.
\]
If \(N=2m\), the same grouping over half-integer absolute values gives
\[
8\sum_{1\leq s<r\leq m}\bigl((r-\tfrac12)^2-(s-\tfrac12)^2\bigr)
=\frac{N^2(N^2-4)}{12}.
\]
Both evaluations use only \(\sum r\), \(\sum r^2\), and \(\sum r^3\). Substituting these sums into \(W_N=\tfrac12(\sum d_{ij}^2-\sum d_{ij})\) yields
\[
W_N=
\begin{cases}
N(67N^3-180N^2+146N-36)/12,&N\text{ even},\\
(N-1)(67N^3-113N^2+33N-3)/12,&N\text{ odd}.
\end{cases}
\]

**Step 2: exact occupation covariance.** For any fixed \(k\) distinct board squares, their joint occupation probability is \(p_k=(N)_k/(N^2)_k\), where \((x)_k\) is the descending factorial, with \(p_k=0\) if \(k>N\). Each graph edge uses two sites; two distinct incident edges use three sites; two disjoint edges use four. Therefore, with \(D_N=\binom{S_N}{2}-W_N\),
\[
\begin{aligned}
\mathbb E H_N &=S_Np_2,\\
\mathbb E H_N^2&=S_Np_2+2W_Np_3+2D_Np_4,\\
\operatorname{Var}(H_N)&=S_Np_2+2W_Np_3+2D_Np_4-(S_Np_2)^2.
\end{aligned}
\]
These identities are exact at every finite \(N\), including \(N=2,3\) with the zero falling-factorial convention. Insert \(p_k\), \(S_N\), and the two expressions for \(W_N\), clear denominators, and factor. The results are exactly the two rational variance formulas in the finding; this is an elementary polynomial identity after the incidence computations above.

**Step 3: limiting coefficient and thermodynamic interpretation.** In the covariance decomposition
\[
\operatorname{Var}(H_N)=S_Np_2(1-p_2)+2W_N(p_3-p_2^2)+2D_N(p_4-p_2^2),
\]
the three terms divided by \(N\) converge respectively to \(5/3\), \(67/6\), and \(-100/9\). The nontrivial cancellation produces \(5/3+67/6-100/9=31/18\). Equivalently, take the rational-function limit of either parity formula.

At each fixed finite \(N\), the canonical identity \(C_N(T)=\operatorname{Var}_T(E_N)/T^2\) follows by differentiating the finite partition sum. As \(T\to\infty\), this finite canonical law converges to uniform occupation, and its variance converges to \(J^2\operatorname{Var}(H_N)\). The claimed iterated limit follows immediately.

## Verification

Execute `python3 check.py`. This self-contained checker uses exact rational arithmetic: it compares the degree sums, mixed diagonal identity, wedge count, and covariance-based variance with their explicit formulas for \(2\leq N\leq80\), and independently enumerates **every** \(N\)-site subset for \(N=2,3,4,5\) directly from attack edges. It reports 491 exact equalities. Representative enumerated variances are \(0\), \(26/63\), \(2479/2275\), and \(4544/2277\) for these four board sizes, respectively. The all-size argument is the algebraic proof above; finite checks do not establish it by themselves.

## Relationship to prior work

Liu, Liao and Wang (arXiv:2605.10326, first submitted 2026-05-11) introduce this unrestricted fixed-occupation lattice-gas ensemble, derive \(\langle E_N\rangle_{T=\infty}\) and estimate its finite-temperature specific heat numerically. Their analytic high-temperature calculation is the mean \(S_Np_2\); their specific-heat section uses measured energy variance, but gives neither an all-size variance formula nor the exact high-temperature coefficient \(31/18\). The present computation supplies that coefficient, with the even/odd finite-board corrections. It does not challenge their energy formula or assert new general covariance principles.

Zhang and Ma (2009) instead simulate a *constrained rook/permutation ensemble* with a different diagonal penalty and thus do not calculate this canonical all-subset variance. Polson and Sokolov (arXiv:2407.08830) discuss Monte Carlo rare-event and energy-level methods, not this variance. The elementary general variance decomposition for edge counts in a uniformly chosen vertex subset is used as a tool rather than claimed as original; the geometry-specific diagonal-intersection count and resulting physical coefficient are the subject of the finding.

## Limitations

The result proves the variance at exactly infinite temperature and the high-temperature coefficient for each finite board; it does not prove a uniform expansion in \(T^{-1}\) as \(N\to\infty\) or an analytic finite-temperature thermodynamic specific heat. It uses the unrestricted fixed-\(N\) all-subsets ensemble, not an independent occupancy process or a one-queen-per-row ensemble. A more general, unindexed theorem for the queen-attack graph's degree moments could indirectly imply these formulas; no independent publication-priority certification is claimed.

## References

1. Z.-Y. Liu, H.-J. Liao, and L. Wang, *Statistical mechanics of the \(N\)-queens problem*, arXiv:2605.10326 (first public version 2026-05-11), https://arxiv.org/abs/2605.10326; Phys. Rev. E **114**, 034125 (2026), DOI: 10.1103/cx7m-n3d5.
2. C. Zhang and J. Ma, *Counting solutions for the \(N\)-queens and Latin-square problems by Monte Carlo simulations*, Phys. Rev. E **79**, 016703 (2009), https://pmc.ncbi.nlm.nih.gov/articles/PMC2682695/.
3. N. Polson and V. Sokolov, *Counting \(N\) Queens*, arXiv:2407.08830 (2024), https://arxiv.org/abs/2407.08830.
