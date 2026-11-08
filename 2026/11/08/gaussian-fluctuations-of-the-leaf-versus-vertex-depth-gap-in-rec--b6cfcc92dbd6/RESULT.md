# Gaussian fluctuations of the leaf-versus-vertex depth gap in recursive trees

## Finding

For a uniformly random recursive tree \(T_n\) on labels \(1,\ldots,n\), rooted at label \(1\), let \(D_{v,n}\) denote a vertex's depth, \(P_n=\sum_v D_{v,n}\) the internal path length, \(L_n\) the number of leaves (vertices with no children), and \(E_n=\sum_{v:\,v\text{ leaf}}D_{v,n}\) the external path length, using *actual leaves* rather than null attachment positions. Then

\[
\boxed{\sqrt{\frac{n}{\log n}}\left(\frac{E_n}{L_n}-\frac{P_n}{n}-\frac12\right)\xrightarrow{\mathrm d}\mathcal N(0,1/3).}
\]

Thus the nonconstant second-order term in the mean-leaf-depth minus mean-vertex-depth gap is of order \(\sqrt{\log n/n}\), with limiting normal variance exactly \(1/3\).

## Assumptions and scope

Start with a singleton root and, for each \(j\ge2\), attach vertex \(j\) to one uniformly chosen member of \(\{1,\ldots,j-1\}\), independently at different arrivals. There are no other weights, conditioning events or parameters. All depths are measured in edges from the root. A leaf means a vertex with *zero children*. We study integer \(n\ge2\); \(L_n\ge1\) ensures the ratio is defined. Logarithms are natural. The central limit statement is annealed weak convergence; no functional or almost-sure Gaussian statement is claimed.

## Proof

All conditional expectations below are with respect to the tree just before vertex \(n+1\) arrives. Define
\[
B_n=P_n/n,\qquad C_n=E_n-L_nB_n,\qquad
W_n=L_n-n/2,\qquad F_n=C_n-n/4,\qquad
Q_n=\frac1n\sum_v(D_{v,n}-B_n)^2.
\]
Write \(I_v\) for the indicator that \(v\) is a leaf, \(l_n=L_n/n\), and let \(U\) be the uniformly chosen parent, with \(I=I_U\) and \(R=D_{U,n}-B_n\). Then \(\mathbb E(R\mid T_n)=0\), \(\mathbb E(I\mid T_n)=l_n\), and \(\mathbb E(IR\mid T_n)=C_n/n\). The exact updates are
\[
P_{n+1}=P_n+D_{U,n}+1,\quad L_{n+1}=L_n+1-I,\quad E_{n+1}=E_n+D_{U,n}+1-ID_{U,n}.
\]
Substituting into the definition of \(C_n\) yields the pointwise identity
\[
C_{n+1}-C_n=\frac{n}{n+1}(1-l_n-I)R+\frac{n-L_n+I}{n+1}.
\]
Its exact conditional expectation is
\[
\mathbb E(C_{n+1}\mid T_n)=\frac{n}{n+1}C_n+1-l_n+\frac{2l_n-1}{n+1}.
\]
The last correction is essential at finite sizes. Put
\[
\xi_{n+1}=\frac{n}{n+1}\left[(1-l_n-I)R+\frac{C_n}{n}\right]
+\frac{I-l_n}{n+1}.
\]
It has conditional mean zero, and straightforward algebra gives the exact recursion
\[
F_{n+1}=\frac{n}{n+1}F_n-\frac{n-1}{n(n+1)}W_n+\frac1{4(n+1)}+\xi_{n+1}.
\]
Since \(F_2=0\), multiplication by \(n+1\) and iteration gives
\[
 nF_n=\sum_{k=2}^{n-1}\left[(k+1)\xi_{k+1}-\frac{k-1}{k}W_k+\frac14\right].\tag{1}
\]

**Leaf deviations.** The exact leaf update gives \(\mathbb E(W_{n+1}\mid T_n)=(1-1/n)W_n\) and \(\mathbb E[(W_{n+1}-\mathbb E(W_{n+1}\mid T_n))^2\mid T_n]=l_n(1-l_n)\le1/4\). Consequently \(\mathbb E W_n=0\) and \(\mathbb E W_n^2\le(n-2)/4\). Therefore \(l_n\to1/2\) in \(L^2\), and by Minkowski
\[
\left\|\sum_{k=2}^{n-1}\frac{k-1}{k}W_k\right\|_2=O(n^{3/2}).\tag{2}
\]

**Uniform depth dispersion.** The incremental mean-depth identity \(B_{n+1}=B_n+(R+1)/(n+1)\) gives the exact Welford update
\[
 Q_{n+1}=\frac n{n+1}Q_n+\frac{n}{(n+1)^2}(R+1)^2.
\]
Because \(\mathbb E[(R+1)^2\mid T_n]=Q_n+1\), there are martingale differences \(\eta_{n+1}\) such that
\[
Q_{n+1}-Q_n=\frac n{(n+1)^2}-\frac{Q_n}{(n+1)^2}+\eta_{n+1},\quad
\eta_{n+1}=\frac{n}{(n+1)^2}\big[(R+1)^2-Q_n-1\big].\tag{3}
\]
The depth of a fixed vertex \(j\) has the law of a sum of independent Bernoulli random variables with success probabilities \(1/i\), \(1\le i<j\). Thus \(\mathbb E e^{D_{j,n}}\le\exp((e-1)\sum_{i<j}1/i)\). A union bound and exponential Markov inequality show that the maximum depth \(H_n\) satisfies \(\mathbb E H_n^r=O((\log n)^r)\) for every fixed \(r>0\). Since \(Q_n\le H_n^2\), the deterministic drift correction in (3) has absolutely summable \(L^2\) norms:
\[
\sum_{n\ge2}\frac{\|Q_n\|_2}{(n+1)^2}<\infty.
\]
Also \(\mathbb E\eta_{n+1}^2=O((1+\log^4 n)/n^2)\), a summable sequence; hence the martingale \(\sum\eta\) converges in \(L^2\). Equation (3) therefore implies
\[
Q_n-\sum_{k=2}^{n-1}\frac{k}{(k+1)^2}\longrightarrow Q_\infty
\quad\text{in }L^2
\]
for some finite random variable, and in particular
\[
Q_n/\log n\longrightarrow1\quad\text{in }L^2.\tag{4}
\]

**Innovation variance.** Let \(A=(1-l_n-I)R+C_n/n\). Then \(\mathbb E(A\mid T_n)=0\), and the exact identity
\[
\mathbb E(A^2\mid T_n)= (1-l_n)^2Q_n+(2l_n-1)Q_n^{\mathrm{leaf}}-(C_n/n)^2,\quad
Q_n^{\mathrm{leaf}}=\frac1n\sum_v I_v(D_{v,n}-B_n)^2\le Q_n
\tag{5}
\]
holds. Because \(|A|\le2H_n\), \(\mathbb E\xi_{n+1}^2=O(\log n)\) follows more sharply from \(\mathbb E(A^2\mid T_n)\le Q_n\) up to bounded terms and \(\mathbb E Q_n=O(\log n)\). Using martingale orthogonality in (1), (2), and the sum \(\sum_{k<n} k^2\log(k+1)=O(n^3\log n)\), one obtains \(\|F_n\|_2=O(\sqrt{n\log n})\). Hence \(C_n/n=1/4+F_n/n\to1/4\) in \(L^2\), without presupposing the first-order theorem. Now (4), \(l_n\to1/2\), (5), and the \(O(1/n)\) correction in \(\xi\) give
\[
\frac{\mathbb E(\xi_{n+1}^2\mid T_n)}{\log n}\longrightarrow\frac14\quad\text{in }L^1.\tag{6}
\]
In particular, weighted summation of (6) gives the predictable variance limit
\[
\frac1{n^3\log n}\sum_{k=2}^{n-1}(k+1)^2\mathbb E(\xi_{k+1}^2\mid T_k)
\longrightarrow\frac14\int_0^1t^2dt=\frac1{12}\quad\text{in probability}.\tag{7}
\]

**Martingale Gaussian limit.** From \(|\xi_{k+1}|\le 2H_k+1\) and the established height fourth-moment bound, the fourth-moment Lyapunov upper bound for the normalized array is
\[
\frac{\sum_{k<n}(k+1)^4\mathbb E\xi_{k+1}^4}{n^6(\log n)^2}
=O(\log^2 n/n)\longrightarrow0.
\]
Thus the conditional Lindeberg condition holds. The standard martingale triangular-array central limit theorem applied with (7) yields
\[
\frac{\sum_{k=2}^{n-1}(k+1)\xi_{k+1}}{n\sqrt{n\log n}}
\xrightarrow{\mathrm d}\mathcal N(0,1/12).
\]
The \(W\)-sum in (1) is negligible on this scale by (2), as is the deterministic \((n-2)/4\) term. Consequently
\[
 F_n/\sqrt{n\log n}\xrightarrow{\mathrm d}\mathcal N(0,1/12).
\]
Finally, the identity
\[
\frac{E_n}{L_n}-\frac{P_n}{n}-\frac12
=\frac{C_n-L_n/2}{L_n}=\frac{F_n-W_n/2}{L_n}
\]
and \(L_n/n\to1/2\), \(W_n/\sqrt{n\log n}\to0\) in probability prove the asserted limit with variance \(4/12=1/3\). \(\square\)

## Verification

Run `python verify.py` with Python 3. The standalone checker enumerates every labeled recursive tree through eight vertices, tests every possible next-parent transition, verifies all exact depth/leaf/path updates, the centered innovation and the finite-size drift including its correction, the variance identity (5), and the quadratic depth update using exact rational arithmetic. It is a finite identity test, not a proof of the martingale CLT; the infinite steps are established analytically above by the moment bounds, martingale convergence, conditional variance and Lindeberg arguments.

## Relationship to prior work

Lundblad and Wagner (2026), Theorem 6 with \(\alpha=0\), proved \(E_n/L_n-P_n/n\to1/2\) in probability and convergence of its first two moments, but did not state the fluctuation rate or a central limit for the *difference*. The result here is a second-order refinement for this uniform recursive-tree case. Grübel and Kabluchko (2015), Section 5.5.2, obtained a sharp Gaussian tail fluctuation theorem for the **centered internal path-length martingale** of uniform recursive trees; that variable is not the cross-statistic \(E_n/L_n-P_n/n\), and its result does not directly imply the normalization or variance given here. The source also studies external nodes of binary search trees, which are not the leaves counted here. The recent deterministic-weight total-path-length martingale analysis of Gałązka and Wdowicka (2026) concerns internal path length without the coupled leaf denominator. Related root-degree/path-length and root-degree/leaf-count identities involve distinguished vertices rather than the full mean-depth gap. No definitive priority assertion is made beyond these statement-level comparisons.

## Limitations

The theorem covers uniform one-parent recursive trees only; no affine-attachment, weighted-attachment, conditioned or nonrecursive tree extension is claimed. It is an ordinary weak Gaussian limit, not a functional limit, Berry–Esseen bound or almost-sure theorem. Exhaustive checking is limited to small trees and cannot establish an infinite limit. Historical priority could be affected by a broader prior theorem not identified in the searches; independent mathematical validation has not been performed.

## References

1. Jacob Lundblad and Stephan Wagner, *Path Length and External Path Length in Random Trees*, AofA 2026, LIPIcs 381, article 2, first published 2026-07-13, https://doi.org/10.4230/LIPIcs.AofA.2026.2 (particularly Theorem 6, Lemma 14 and Section 5).
2. Rudolf Grübel and Zakhar Kabluchko, *A Functional Central Limit Theorem for Branching Random Walks, Almost Sure Weak Convergence, and Applications to Random Trees*, https://arxiv.org/abs/1410.0469 (particularly Section 5.5.2).
3. Marek Gałązka and Hanna Wdowicka, *Total Path Length in Power-Weight Recursive Trees: Martingale Limits and Global Fluctuations*, https://arxiv.org/abs/2610.00614 (background comparison concerning internal path lengths).
