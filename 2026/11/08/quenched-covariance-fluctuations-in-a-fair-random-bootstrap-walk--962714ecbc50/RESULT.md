# Centered quenched covariance fluctuations for the static fair bootstrap walk

## Finding

Let \((\beta_j)_{j\ge0}\) be independent fair bits, sampled once and kept fixed throughout the walk. Independently let \((\xi_i)_{i\ge1}\) be independent fair signs. Put
\[
S_k=\sum_{i=1}^k\mathbf1_{\{\xi_i=-1\}},\qquad
\omega_j=(-1)^{\sum_{r=0}^j\binom jr\beta_r},\qquad
A_j=\sum_{r=0}^{j-1}\omega_r,
\]
with \(S_0=A_0=0\) and exponents interpreted modulo two. Define \(\zeta_0=1\), \(\zeta_k=\omega_{S_k}\) for \(k\ge1\), and \(H_k=\sum_{r=0}^{k-1}\zeta_r\). This is the predictable cross-covariation of \(X_k=\sum_{i=1}^k\xi_i\) and \(Y_k=\sum_{i=1}^k\zeta_{i-1}\xi_i\) in the filtration that fixes the coefficient environment.

For almost every environment, under the conditional walk law, in \(D([0,1],\mathbb R)\) with its Skorokhod \(J_1\) topology,
\[
\left(\frac{H_{\lfloor nt\rfloor}-2A_{\lfloor nt/2\rfloor}}{\sqrt n}\right)_{0\le t\le1}
\ \Longrightarrow\ (B_t)_{0\le t\le1},
\]
where \(B\) is standard Brownian motion. The deterministic-in-environment centering has almost surely
\[
\limsup_{n\to\infty}\frac{2A_{\lfloor n/2\rfloor}}{\sqrt{n\log\log n}}=2,
\qquad
\liminf_{n\to\infty}\frac{2A_{\lfloor n/2\rfloor}}{\sqrt{n\log\log n}}=-2.
\]
In particular the uncentered quenched laws of \(H_n/\sqrt n\) are not tight: for almost every environment there are subsequences escaping to each of \(+\infty\) and \(-\infty\) in conditional probability.

## Proof

Each finite Pascal-parity transform from \((\beta_0,\ldots,\beta_m)\) to its first \(m+1\) output bits is triangular with ones on the diagonal, hence invertible over \(\mathbb F_2\). Thus \((\omega_j)\) consists of iid fair signs. For \(k\ge1\), put \(D_k=\sum_{r=0}^{k-1}\omega_{S_r}\) and \(M_k=\sum_{r=0}^{k-1}\xi_{r+1}\omega_{S_r}\); put \(D_0=M_0=0\). On any trajectory,
\[
A_{S_{r+1}}-A_{S_r}=\mathbf1_{\{\xi_{r+1}=-1\}}\omega_{S_r},
\qquad D_k=2A_{S_k}+M_k,
\qquad H_k=D_k+1-\omega_0\quad(k\ge1).
\]
For every fixed scenery the next increment of \(M\), conditional on the whole past, is a fair sign: its multiplier is predictable and the next coin is fresh. Thus the increments of \(M\) are iid fair signs under the conditional walk law, and Donsker's theorem gives its quenched functional limit.

It remains to replace the random clock in the centering. For each dyadic integer \(N\), use Hoeffding's inequality on all scenery intervals with endpoints in \([0,2N]\) at distance at most \(N^{2/3}\). The probability that any of the associated partial-sum increments exceeds \(N^{5/12}\) in absolute value is at most \(2(2N+1)^2\exp(-N^{1/6}/2)\). Borel–Cantelli shows that for almost every scenery the bound \(N^{5/12}\) holds eventually for every dyadic \(N\). Given large \(n\), take the least dyadic \(N\ge n\). By a maximal bounded-increment inequality the coin event \(\max_{k\le n}|S_k-k/2|\le N^{2/3}/2\) has conditional probability tending to one. On this event the distance from \(S_k\) to \(\lfloor k/2\rfloor\) is at most \(N^{2/3}\) for every \(k\le n\), and those endpoints are within \([0,2N]\). Hence
\[
\frac{1}{\sqrt n}\max_{k\le n}|A_{S_k}-A_{\lfloor k/2\rfloor}|\ 
\xrightarrow{\mathbb P_\xi}\ 0
\]
for each scenery in the full-measure set. Because \(\lfloor\lfloor nt\rfloor/2\rfloor=\lfloor nt/2\rfloor\) and the initial convention costs at most two, the difference between the centered process and \(M_{\lfloor nt\rfloor}/\sqrt n\) tends to zero uniformly in conditional probability. This proves the functional limit.

The classical two-sided iterated-logarithm law for \(A_m\), with denominator \(\sqrt{2m\log\log m}\), gives the two constants upon taking \(m=\lfloor n/2\rfloor\). Thus \(2A_{\lfloor n/2\rfloor}/\sqrt n\) has deterministic subsequences tending to each signed infinity for almost every environment. Adding the tight centered conditional variables at \(t=1\) implies escape to the corresponding signed infinity in conditional probability.

## Verification and scope

The finite Pascal bijection and pathwise decomposition can be tested by enumerating coefficient prefixes and coin words. For a fixed scenery each desired martingale-increment word determines a unique coin word by recursively undoing the predictable sign. The functional and iterated-logarithm limits use the analytic proof, not finite tests. The claim concerns only static independent fair coefficients and does not imply a fluctuation theorem for biased coefficients. The centering displayed is a particular scenery partial sum, not a definition using the exact conditional mean.

## Relationship to prior work

Hamza and Tournier, [*Are random random walks normal?*](https://arxiv.org/abs/2610.01658), §4.3, Corollary 12, give annealed Brownian normality of the walk pair for elliptic coefficients. The [fair static scenery record](https://github.com/Resultary/2026/tree/main/2026/10/18/SCOPE-hidden-independent-scenery-quenched-normality-and-variance-three--7435461eecaa) already establishes the independent-pair quenched limit, the annealed variance-three covariation limit and the finite variance in the present model; these are not contributions of this finding. The [static elliptic record](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-quenched-brownian-normality-for-static-cardinality-driven-bootst--366d80019b89) also covers the first-order quenched limit under broader hypotheses. Neither first-order normality nor an annealed fluctuation theorem identifies the quenched order-\(\sqrt n\) centering and variance rate. Guillotin-Plantard and Poisat, [*Quenched central limit theorems for random walks in random scenery*](https://arxiv.org/abs/1210.6135), Theorem 1.1, treat a renewal process with strictly positive jumps; the lazy clock here visits each site for a random holding time. General random-scenery and iterated-logarithm methods are not claimed as new. Historical priority for the specific centered functional limit remains conditional on the literature examined.
