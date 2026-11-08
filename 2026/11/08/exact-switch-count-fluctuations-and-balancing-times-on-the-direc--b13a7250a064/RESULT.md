# Exact switch-count fluctuations and balancing times on the directed triangle

## Finding
Consider a positive matrix supported exactly on the directed triangle: the only nonzero entries are \(K_{12}=w_1>0\), \(K_{23}=w_2>0\), and \(K_{31}=w_3>0\). Perform successive diagonal-similarity Osborne updates in the \(\ell_1\)-balancing convention, selecting each coordinate independently and uniformly from \(\{1,2,3\}\). Write \(g=(w_1w_2w_3)^{1/3}\), \(y^{(n)}=(\log(w_1^{(n)}/g),\log(w_2^{(n)}/g),\log(w_3^{(n)}/g))\), and \(R_n=\|y^{(n)}\|_2\).

For every first update choice \(I_1=i\), and every integer \(n\ge1\), there exist independent Bernoulli random variables \(J_2,\ldots,J_n\), each with success probability \(2/3\), such that
\[
R_n=R_1 2^{-N_{n-1}},\qquad N_{n-1}=\sum_{k=2}^{n}J_k\sim\operatorname{Binomial}(n-1,2/3).
\]
This is an exact finite-time law, including cases where \(R_1=0\). In particular, conditional on \(I_1=i\), for every \(p>0\),
\[
\mathbb E[R_n^p\mid I_1=i]=R_1^p\left(\frac13+\frac23\,2^{-p}\right)^{n-1}.
\]
If \(R_1>0\), the squared-log-error mean contracts exactly by \(1/2\) per further update, while the almost-sure log-error exponent is \(-(2/3)\log2\) per update. These two rates are different.

For a log-error tolerance \(0<\delta<R_1\), let \(T_\delta\) be the number of updates *after the first* to reach \(R\le\delta\). Put \(k_\delta=\lceil\log_2(R_1/\delta)\rceil\). Then \(T_\delta\mid I_1=i\) has exactly the negative-binomial law of the number of Bernoulli\((2/3)\) trials needed to obtain \(k_\delta\) successes, with
\[
\mathbb E[T_\delta\mid I_1=i]=\frac32 k_\delta,\qquad
\operatorname{Var}(T_\delta\mid I_1=i)=\frac34 k_\delta.
\]
For \(R_1\le\delta\), \(T_\delta=0\).

The original normalized \(\ell_1\) matrix-balancing residual is
\[
B_n=\frac{\sum_{j=1}^3 |w_j^{(n)}-w_{j-1}^{(n)}|}{\sum_{j=1}^3w_j^{(n)}},
\]
with cyclic indices. Assume the *generic condition* that \(\|P_i y^{(0)}\|_2>0\) for all three choices \(i\), where \(P_i\) averages entries \(i-1\) and \(i\). Let \(\tau_\varepsilon=\min\{n\ge0:B_n\le\varepsilon\}\). As \(\varepsilon\downarrow0\),
\[
\mathbb E\tau_\varepsilon=\frac{3}{2\log2}\log\frac1\varepsilon+O(1),\qquad
\frac{\operatorname{Var}(\tau_\varepsilon)}{\log(1/\varepsilon)}\longrightarrow\frac{3}{4\log2},
\]
\[
\frac{\tau_\varepsilon-\frac{3}{2\log2}\log(1/\varepsilon)}{\sqrt{\log(1/\varepsilon)}}
\ \Longrightarrow\ \mathcal N\!\left(0,\frac{3}{4\log2}\right).
\]
All constants in these leading asymptotics are independent of the three positive initial weights, as long as the generic condition holds.

## Assumptions and scope
The only input edges are \(1\to2\), \(2\to3\), \(3\to1\), with strictly positive weights and zero diagonal. At a coordinate \(i\), the diagonal-similarity update multiplies the \(i\)-th diagonal scaling component by the square root of the ratio of its current column sum to row sum. The coordinate choices are iid uniform across all three indices. There is one update per time step, without rounding error. The generic condition on the initial logarithmic deviations excludes precisely the possibility of exact balance at the first update. Conditional finite-time claims do not require this genericity. The class is intentionally the smallest nontrivial strongly connected directed cycle, not arbitrary matrices or sampling distributions.

## Proof
1. **Exact logarithmic linearization.** In a directed cycle the outgoing weight at node \(i\) is \(w_i\) and the incoming weight is \(w_{i-1}\). The Osborne update replaces both by \(\sqrt{w_iw_{i-1}}\), leaving the third weight unchanged. Thus the product \(w_1w_2w_3\) is conserved and, on zero-sum logarithmic deviations, the update is the orthogonal projection \(P_i\) onto the line \(L_i=\{y:\sum_jy_j=0,\ y_i=y_{i-1}\}\).

2. **Projection geometry.** In the two-dimensional zero-sum plane, the three lines \(L_1,L_2,L_3\) have pairwise angles with absolute cosine \(1/2\). Consequently, for \(v\in L_i\), \(\|P_jv\|_2=\|v\|_2\) when \(j=i\), and \(\|P_jv\|_2=\|v\|_2/2\) otherwise. Once the first coordinate has been selected, each subsequent change of selected coordinate halves the norm, and each repetition leaves it unchanged.

3. **The independent switch law.** Let \(I_1,I_2,\ldots\) be iid uniform on three indices, and define \(J_k=\mathbf1_{\{I_k\ne I_{k-1}\}}\). Conditional on the complete past through \(I_{k-1}\), \(\Pr(J_k=1)=2/3\). This constant conditional probability implies independence of the entire sequence of switch indicators, even conditional on \(I_1\). The finite-time norm and moment formulas follow. The strong law of large numbers applied to switches gives the almost-sure exponent for \(R_1>0\).

4. **Exact hitting time for log imbalance.** A norm reduction from \(R_1\) to at most \(\delta\) requires exactly \(k_\delta\) switches, with the convention \(k_\delta=0\) when already below tolerance. The waiting time to \(k_\delta\) successes in iid Bernoulli\((2/3)\) trials is a sum of \(k_\delta\) independent geometric\((2/3)\) variables. This proves the exact law and the stated expectation and variance.

5. **Transfer to the actual matrix-balancing residual.** After the first update, \(y^{(n)}\) belongs to one of the three lines \(L_i\). For example, if \(y=(a,a,-2a)\), then
\[
B(y)=\frac{2|e^{3a}-1|}{2e^{3a}+1},\qquad
\|y\|_2=\sqrt6|a|.
\]
The same formula holds after permuting coordinates. Uniformly for these six rays as \(\|y\|_2\downarrow0\),
\[
\frac{B(y)}{\|y\|_2}\longrightarrow\sqrt{\frac23}.
\]
For any fixed initial weights satisfying the generic condition, all post-first norms lie in a fixed compact interval \((0,R_{\max}]\). Continuity and strict positivity therefore give deterministic \(0<c_-\le c_+<\infty\), depending only on the input, such that \(c_-R_n\le B_n\le c_+R_n\) for every \(n\ge1\). Hence \(\tau_\varepsilon\) is sandwiched between two negative-binomial switch waiting times with success requirements
\[
k_\pm(\varepsilon)=\frac{\log(1/\varepsilon)}{\log2}+O(1),\qquad
k_+(\varepsilon)-k_-(\varepsilon)=O(1).
\]
The upper minus lower waiting time is bounded in second moment by the waiting time for a fixed finite number of additional successes. Therefore \(\tau_\varepsilon\) differs in bounded \(L^2\) from a negative-binomial stopping time with \(\log(1/\varepsilon)/\log2+O(1)\) successes. The geometric-sum central limit theorem, its mean and variance formulas, and Cauchy--Schwarz give the three asserted limiting statements. The possible first-update cases are a mixture of three versions with the same leading coefficients; the generic condition ensures none terminates at step one. This completes the proof.

## Verification
The standalone program `verify_triangle_osborne.py` uses exact rational arithmetic to exhaust all coordinate words of lengths up to eight (conditioning on each possible first coordinate), verifying the projection norm, switch counts, binomial multiplicities and all finite-word contraction identities. It also checks three positive input-weight triples directly in floating point under the original diagonal-similarity row/column update, including conservation of the cyclic product and equality with the logarithmic projection. Run with `python verify_triangle_osborne.py`; the recorded result is `PASS 10005 exact-geometry and numerical-matrix checks`. The proof above, rather than finite computation, establishes the claims for every length and every positive input.

## Relationship to prior work
Altschuler and Parrilo (2020) establish general randomized Osborne balancing complexity bounds and analyze nonuniform and cyclic strategies. The present statement specializes their uniform-update algorithm to the directed triangle but asks a different exact distributional question: the full finite-time log-error law, a negative-binomial hitting-time law and a central limit theorem for the original nonlinear \(\ell_1\) residual. Classical gossip averaging (Boyd et al., 2006), the finite-time-consensus obstruction for three nodes (Shi et al., 2012/2015), and graph averaging analysis (Movassagh, Szegedy and Wang, 2022) are closely related. Their general mixing or reachability results supply the model and context, not the explicit complete switch-count and residual stopping-time laws above. The basic pairwise-projection equivalence is not claimed as novel.

## Limitations
This is an exact three-vertex, one-way-cycle result. On longer cycles the projection ranges are not all one-dimensional, so the switch-count formula does not automatically generalize. No statement about floating-point implementations, weighted/nonuniform sampling, random initial weights, or arbitrary directed graphs is made. When a first update can already balance the matrix, the asymptotic stopping-time law above can fail unconditionally because an atom remains at immediate termination; the exact conditional finite-time laws continue to hold. The result has not undergone independent scientific validation. A specialized prior derivation of the same triangle stopping law, if found, would affect the originality assessment.

## References
- Jason M. Altschuler and Pablo A. Parrilo, *Near-linear convergence of the Random Osborne algorithm for Matrix Balancing*, arXiv:2004.02837 (first public 2020-04-06), and Mathematical Programming (2023), https://arxiv.org/abs/2004.02837.
- Stephen Boyd, Arpita Ghosh, Balaji Prabhakar and Devavrat Shah, *Randomized Gossip Algorithms*, IEEE Transactions on Information Theory 52 (2006), 2508--2530, https://web.stanford.edu/~boyd/papers/pdf/gossip.pdf.
- Guodong Shi, Bo Li, Mikael Johansson and Karl Henrik Johansson, *Finite-time Convergent Gossiping*, arXiv:1206.0992 (first public 2012-06-05), https://arxiv.org/abs/1206.0992.
- Ramis Movassagh, Mario Szegedy and Guanyang Wang, *Repeated Averages on Graphs*, arXiv:2205.04535 (first public 2022-05-09), https://arxiv.org/abs/2205.04535.
