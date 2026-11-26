# Exact intermediate matching-deletion stability for two-way additive least squares

## Finding

For an integer \(n\ge3\), let \(E_{n,r}=\{1,\ldots,n\}^2\setminus\{(s,s):1\le s\le r\}\), with \(0\le r\le n\). Let \(P_{n,r}\) be the real orthogonal projector, for the uniform counting inner product on observed cells, onto the restrictions of arrays \(a_i+b_j\). Put \(T_r=n(n-2)+r\).

The intermediate matching-deletion law, for \(2\le r<n\), is
\[
 \|P_{n,r}\|_{\ell^\infty\to\ell^\infty}=3-\frac4n+\frac{2(n-2)}{nT_r}.
\]
Exactly the observed cells with **both** indices outside \(\{1,\ldots,r\}\) maximize the absolute kernel row sum. The same formula for \(r=0,1\) gives the known intact and one-deletion results [1]; for the full crown \(r=n\), the known norm is \(3-4/n\) and all rows maximize [2,3]. These cases are recalled for comparison, not claimed as discoveries.

Together the formulas give a strictly decreasing profile. The decrement before the final deletion, for any step \(r\to r+1\) with \(0\le r\le n-2\), is \(2(n-2)/[nT_r(T_r+1)]\); the first such step is the square specialization of [1]. The last step has decrement \(2(n-2)/[n(n^2-n-1)]\), exactly \((n+1)(n-2)\) times the preceding step. Thus the disappearance of the last cell with neither index marked accounts for an exceptional final improvement.

Norming real data are obtained by choosing any maximizing row and assigning one overall sign times the signs of its nonzero entries, with arbitrary values in \([-1,1]\) at zeros. The minimum possible fitted value for input data in \([0,1]\), over all observed target cells, is \(-\big(\|P_{n,r}\|-1\big)/2\).

## Scope

Any matching of size \(r\) can be put in the displayed form by independent row and column label permutations. The table is square, the observed cells have equal weight, and the norm concerns only those cells, not extrapolation. The bipartite observation graph is connected for \(n\ge3\): any two vertices in the same part have a common neighbor, and every vertex has an edge. Thus the additive design has rank \(2n-1\); the projector and the fitted cell values are unique even though the unrestrained two-factor parametrization has one redundancy. The result is for the fixed orthogonal projector, not the best norm among arbitrary projections.

## Proof

Write \(T=T_r\), \(D=\{(s,s):1\le s\le r\}\). The intact-table projector has kernel \(H^0_{(i,j),(k,l)}=(\mathbf1_{i=k}+\mathbf1_{j=l})/n-1/n^2\). For the full-rank additive design, deletion subtracts the deleted rows' Gram matrix contribution. Woodbury gives the resulting observed kernel \(H=H^0_{EE}+H^0_{ED}(I-H^0_{DD})^{-1}H^0_{DE}\), where \(H^0_{DD}=2I_r/n-J_r/n^2\) and \((I-H^0_{DD})^{-1}=nI_r/(n-2)-nJ_r/((n-2)T)\). These formulas also hold with empty deleted blocks at \(r=0\).

For an observed cell \(e=(i,j)\), let \(x_e(s)=\mathbf1_{i=s}+\mathbf1_{j=s}\) for \(s\le r\) and let \(m_e=\sum_s x_e(s)\) and \(d_e=n-2+m_e\). Each \(x_e(s)\) is either zero or one, because the repeated marked index is deleted. For \(f=(k,l)\), put \(S=\mathbf1_{i=k}+\mathbf1_{j=l}\). Substituting \(H^0_{e,(s,s)}=x_e(s)/n-1/n^2\) into the deletion identity and collecting terms gives
\[
 H_{ef}=\frac Sn+\frac{x_e\cdot x_f}{n(n-2)}-\frac{d_e d_f}{n(n-2)T}. \tag{1}
\]
The entries with \(S>0\) are positive. If a shared coordinate is marked, \(x_e\cdot x_f\ge1\), so the product \(d_ed_f\) is bounded by \((n-1)^2<(n-1)T\) when \(r=1\), and by \(n^2<(n-1)T\) when \(r\ge2\). If the shared coordinate is unmarked, the product is at most \((n-1)^2\) and is at most \((n-2)^2\) when \(r=0\). For \(r\ge1\), \((n-2)T\ge(n-1)^2\), with equality only for \(n=3,r=1\); equality in the product bound then requires both cells marked once, which with a shared unmarked coordinate forces \(e=f\) and \(S=2\).

For \(S=0\), entries with no marked overlap are negative. For exactly one marked overlap, the sign is that of \(T-d_ed_f\). If both cells are marked once, \(d_ed_f=(n-1)^2\) and \(T=(n-1)^2+r-1\), so the entry is nonnegative (zero when \(r=1\)). If at least one cell is marked twice, this one-overlap entry is negative: \(d_ed_f=n^2\) for two such cells, or \(n(n-1)\) for a mixed pair, in which case \(r<n\). Two marked overlaps with \(S=0\) occur only at the reversed cell of a row marked twice. This entry is positive since \(2T-n^2=n(n-4)+2r>0\) for \(n\ge3,r\ge2\).

Each row and each column of observed cells has total \(d_f\)-weight \(T\): an unmarked line has \(n(n-2)+r\), and a marked line has \((n-1)^2+r-1\). Across the whole table the weight is \(nT\). Thus the total weight of cells with \(S=0\) for target \(e\) is \((n-2)T+d_e\). Denote by \(N_j\) the negative kernel mass for a target with \(j=m_e\) marked indices, when that class exists.

- For \(j=0\), all cells with \(S=0\) are negative. Hence \(N_0=(n-2)/n+(n-2)/(nT)\).
- For \(j=1\), write the target as \((I,J)\) with \(I\) marked and \(J\) unmarked, transposing if necessary. Among disjoint cells there are \(n-r\) nonnegative overlap cells \((k,I)\) with \(k\) unmarked. Remove their weight \((n-r)(n-1)\). The other \(r-1\) overlap cells are negative and each adds \(1/[n(n-2)]\) to the signed entry in (1). Consequently
  \[
  N_1=\frac{(n-1)\big((n-2)T+n-1-(n-r)(n-1)\big)}{n(n-2)T}-\frac{r-1}{n(n-2)}.
  \]
  Subtraction gives \(N_0-N_1=[(r-n/2)^2+3(n-2)^2/4]/[n(n-2)T]>0\).
- For \(j=2\), remove only the reversed cell from the disjoint set; it has weight \(n\). The remaining single overlaps are the \(n-2\) disjoint cells in the row indexed by the target's column and the \(n-2\) in the column indexed by the target's row. Each is negative and gets the same \(1/[n(n-2)]\) signed correction. This gives \(N_2=(n-2)/n\).

Since constants are fitted, each kernel row sums to one. The maximum absolute row sum is therefore \(1+2\max_j N_j\). The zero-mark class exists for \(r<n\) and strictly dominates each other existing class; for \(r=n\) only the twice-marked class exists. Subtracting adjacent values gives the decrement formulas, using \(T_{n-2}=(n+1)(n-2)\) for their final ratio. Equality in the absolute-row-sum bound gives the norming sign patterns, taking the union over maximizing rows. For the fitted minimum, choose input one on negative entries and zero on positive entries of a maximizing row; no other row can have larger negative mass.

## Verification and relation to prior work

The unchanged companion `verify_crown.py` constructs rational additive-design projection matrices directly from the Gram inverse. It checks all observed rows for \(3\le n\le6\), including the known cases. These are finite checks; Equation (1) and the sign-and-weight argument above prove the full result.

The additive projector equals the cut-space orthogonal projector of the observed bipartite graph after changing the signs of the column vertex potentials. General transfer-current and leverage identities, such as [4,5], give its entries but do not optimize their absolute row sums. The intact case and the corresponding exact one-edge drop and maximizers were already obtained in [1], and the full crown norm was computed in [2,3]. The increment here is the exact intermediate matching-deletion law with its maximizing cells and the final-step comparison, not the known endpoint norms or the general projection identity. Earlier equivalent intermediate laws outside the inspected literature remain possible.

1. *Exact edge-erasure sensitivity of gradient projections on rectangular bicliques*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-exact-edge-erasure-sensitivity-of-gradient-projections-on-rectan--430cc80014f3/RESULT.md), finding.
2. *Sharp cut and cycle complementability after deleting a perfect matching*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-sharp-cut-and-cycle-complementability-after-deleting-a-perfect-m--6319a2a73e78/RESULT.md), finding and proof §§2–3.
3. *Sharp minimal cut-cycle projection norms on crown graphs*, [Resultary record](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-minimal-cut-cycle-projection-norms-on-crown-graphs--a18a2c603916/RESULT.md), finding.
4. D. A. Spielman and N. Srivastava, *Graph Sparsification by Effective Resistances*, [arXiv:0803.0929v1](https://arxiv.org/abs/0803.0929), Lemma 3.
5. P. Drineas and M. W. Mahoney, *Effective Resistances, Statistical Leverage, and Applications to Linear Equation Solving*, [arXiv:1005.3097v1](https://arxiv.org/abs/1005.3097), §3.2, Lemma 1.
