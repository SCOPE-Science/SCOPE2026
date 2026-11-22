# Joint Gaussian fluctuations of edge count and chromatic number in random interval graphs

## Finding
For an interval-intersection graph sampled from \(n\) independent random intervals, the joint fluctuations of the **chromatic number** and the **edge count** have an explicit nondegenerate Gaussian limit:
\[
 \left(\frac{\chi_n-n/2}{\sqrt n},\frac{E_n-n(n-1)/3}{n^{3/2}}\right)
 \xrightarrow{\mathrm d}N_2\left(0,
 \begin{pmatrix}1/4&1/12\\1/12&2/45\end{pmatrix}\right).
\]
In particular, \(\operatorname{Corr}(\chi_n,E_n)\to\sqrt{10}/4\). If \(X_n=(\chi_n-n/2)/\sqrt n\) and \(Y_n=(E_n-n(n-1)/3)/n^{3/2}\), then \((X_n,Y_n-X_n/3)\) converges to independent zero-mean Gaussians of variances \(1/4\) and \(1/60\). The independence is asymptotic, not an exact finite-sample independence statement.

## Assumptions and scope
Fix \(n\ge2\). Draw \(2n\) independent endpoints from an atomless real distribution \(F\), group into labelled pairs, and regard the sorted members of each pair as a closed interval. The vertices of \(G_n\) are these intervals; two vertices are adjacent precisely when the intervals intersect. Write \(E_n=|E(G_n)|\) and \(\chi_n\) for the minimum number of proper vertex colours. A probability-integral transform preserves the almost-sure endpoint order, so all distributions below coincide with those for independent uniform endpoints on \([0,1]\). All limits are as \(n\to\infty\) without restricting subsequences.

Write \(L_i=\min(U_i,V_i)\), \(R_i=\max(U_i,V_i)\), \(C_n(t)=\sum_{i=1}^n\mathbf1\{L_i\le t\le R_i\}\), and \(C_n=C_n(1/2)\). Interval graphs are perfect, and intervals have the Helly property, hence \(\chi_n=\max_{0\le t\le1}C_n(t)\). (For nonuniform \(F\), the midpoint is replaced with any population median, and the equality is in distribution.)

## Proof
**Step 1. One-interval projection of edges.** Set \(Z_i=\mathbf1\{L_i\le 1/2\le R_i\}\), and let \(H_{ij}=\mathbf1\{[L_i,R_i]\cap[L_j,R_j]\ne\varnothing\}\). Conditioned on \((L_i,R_i)=(l,r)\), the next interval misses it exactly when both endpoints are below \(l\) or both above \(r\). Thus
\[
 h(l,r)=\mathbb E(H_{ij}\mid L_i=l,R_i=r)=1-l^2-(1-r)^2.
\]
Since \((L,R)\) has density \(2\) on \(0\le l\le r\le1\), direct integrations give
\[
 \mathbb EZ_i=\tfrac12,\quad \mathbb Eh(L,R)=\tfrac23,\quad
 \mathbb E[h(L,R)^2]=\tfrac{22}{45},\quad
 \mathbb E[Z_ih(L_i,R_i)]=\tfrac5{12}.
\]
Therefore
\[
\operatorname{Var}(Z_i)=\tfrac14,\quad
\operatorname{Var}(h(L_i,R_i))=\tfrac2{45},\quad
\operatorname{Cov}(Z_i,h(L_i,R_i))=\tfrac1{12}.
\]
The edge count has the order-two Hoeffding decomposition
\[
 E_n-\frac{n(n-1)}3
 =(n-1)\sum_{i=1}^n\left(h(L_i,R_i)-\tfrac23\right)+R_n,
\]
where \(R_n=\sum_{i<j}[H_{ij}-h(L_i,R_i)-h(L_j,R_j)+2/3]\). Distinct degenerate-kernel summands are uncorrelated, including ones sharing one index, so \(\operatorname{Var}(R_n)=O(n^2)\). Consequently \(R_n/n^{3/2}\to0\) in \(L^2\). The ordinary bivariate iid central limit theorem applied to \((Z_i-1/2,h(L_i,R_i)-2/3)\) implies the asserted limiting Gaussian vector with \(C_n\) in place of \(\chi_n\).

**Step 2. The maximum differs negligibly from midpoint coverage.** We prove the stronger \(L^2\) bound
\[
 \mathbb E\left(\max_t C_n(t)-C_n(1/2)\right)^2
 =O(n^{7/8}\log n).
\]
The population coverage profile is \(p(t)=\Pr(L\le t\le R)=2t(1-t)=1/2-2(t-1/2)^2\). Apply the Dvoretzky–Kiefer–Wolfowitz inequality separately to the \(n\) iid minima and the \(n\) iid maxima: with probability at least \(1-4e^{-2n^{1/3}}\),
\[
\sup_{0\le t\le1}|C_n(t)-np(t)|\le 2n^{2/3}+1.
\]
For large \(n\), outside \(|t-1/2|<\delta_n=n^{-1/8}\), the deterministic mean loss is at least \(2n\delta_n^2=2n^{3/4}\), larger than twice this empirical error. Thus every maximizer lies within that \(\delta_n\)-neighbourhood on the good event.

Use the deterministic mesh \(\{j/n^2:0\le j\le n^2\}\). For any mesh point \(t\) within \(2\delta_n\) of \(1/2\), set \(W_i(t)=\mathbf1\{L_i\le t\le R_i\}-Z_i\). A change of membership requires at least one of the two endpoints to lie between \(t\) and \(1/2\), so \(|W_i(t)|\le1\) and \(\operatorname{Var}(W_i(t))\le4\delta_n\). Bernstein's inequality followed by a union bound over at most \(n^2+1\) mesh points shows, with failure probability \(O(n^{-8})\) for sufficiently large absolute \(K\),
\[
\max_{|t-1/2|\le2\delta_n,\ t\text{ on mesh}}
\left|\sum_{i=1}^n(W_i(t)-\mathbb EW_i(t))\right|
\le K\left(\sqrt{n\delta_n\log n}+\log n\right).
\]
Every mesh cell has length at most \(n^{-2}\). A binomial tail bound and a union bound show that no cell contains more than \(K\log n\) of the \(2n\) endpoints, except on an event of probability \(O(n^{-8})\). Between grid points, \(C_n(t)\) consequently changes by at most \(K\log n\). Since \(np(t)\le np(1/2)\), these bounds give
\[
 0\le\max_t C_n(t)-C_n(1/2)
 \le K'\left(\sqrt{n^{7/8}\log n}+\log n\right)
\]
outside an event of probability \(O(e^{-2n^{1/3}}+n^{-8})\). As the gap is always bounded by \(n\), squaring and taking expectations yields \(O(n^{7/8}\log n)\), as claimed.

**Step 3. Transfer and independence.** Step 2 shows \((\chi_n-C_n)/\sqrt n\to0\) in \(L^2\), so Slutsky's theorem transfers the bivariate limit in Step 1 to \((\chi_n,E_n)\). The exact moments for the simpler midpoint model are
\[
 \operatorname{Var}(C_n)=n/4,\quad
 \operatorname{Var}(E_n)=\frac{n(n-1)(2n+1)}{45},\quad
 \operatorname{Cov}(C_n,E_n)=\frac{n(n-1)}{12}.
\]
Because the normalized edge fluctuations have uniformly bounded second moments, the \(L^2\) transfer also transfers the limiting covariance and variance from \(C_n\) to \(\chi_n\). This proves the asymptotic correlation \(\sqrt{10}/4\). The Gaussian limiting vector has \(\operatorname{Cov}(X,Y)=1/12\) and \(\operatorname{Var}(X)=1/4\); hence \(X\) and \(Y-X/3\) are uncorrelated and therefore independent. The residual variance is \(2/45-1/36=1/60\). This completes the proof.

## Verification
The standalone Python 3 script `check_interval.py` enumerates all \((2n)!\) labelled endpoint orderings for \(n=2,3,4\). It verifies the interval Helly clique/maximum-coverage identity in all 41,064 configurations and 15 exact rational moment identities for midpoint coverage, edges and their covariance. Independently, symbolic polynomial integration checks \(\mathbb Eh=2/3\), \(\mathbb Eh^2=22/45\), and \(\mathbb E[Zh]=5/12\). These finite checks corroborate algebra and boundary handling; the infinite asymptotic theorem follows from the displayed analytic argument, not enumeration.

Run: `python3 check_interval.py`. No nonstandard Python modules or external data are needed.

## Relationship to prior work
Scheinerman's classic random-interval-graph analysis treats first-order edges and chromatic number, and Diaconis–Holmes–Janson give an interval-graph limit perspective. Janson's separate random-runs model gives an analogous maximum-process CLT, not a chromatic result for this model; Iliopoulos discusses edge and clique statistics separately. The exact finite midpoint-coverage/edge regression and its limiting explained-variance fraction \(5/8\) are not newly claimed. The finding here is the **joint** nondegenerate law of the random *maximum* clique/colour count with edge count, including independent Gaussian residual noise, which cannot be inferred from marginal limit laws or finite covariance identities alone.

## Limitations
The distribution requires independent interval pairs and common atomless endpoint law; it does not automatically extend to other random interval models, such as fixed-length intervals. The residual is independent only in the asymptotic Gaussian limit, not for finite \(n\). The argument provides a nonoptimal \(L^2\) rate for the maximum-versus-midpoint discrepancy; no Berry–Esseen rate for the full vector is claimed. The original 1988 random-interval-graph source was not available in full in the accessible literature and could conceal historical equivalents. No independent audit has been performed.

## References
1. E. R. Scheinerman, *Random interval graphs*, Combinatorica 8 (1988), 357–371. DOI: https://doi.org/10.1007/BF02189092.
2. P. Diaconis, S. Holmes, S. Janson, *Interval graph limits*, arXiv:1102.2841, originally posted 2011-02-14. https://arxiv.org/abs/1102.2841.
3. V. Iliopoulos, *Random Interval Graphs*, arXiv:1507.06275, originally posted 2015-07-22. https://arxiv.org/abs/1507.06275.
4. S. Janson, *Sorting using complete subintervals and maximum number of runs in a randomly evolving sequence*, 2007, for an analogous, but different, random-runs maximum CLT. https://arxiv.org/abs/math/0701288.
