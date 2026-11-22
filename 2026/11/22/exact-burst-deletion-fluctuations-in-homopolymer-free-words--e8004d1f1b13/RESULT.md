# Exact burst-deletion fluctuations in homopolymer-free words

## Finding
Let \(q\ge3\), \(b\ge2\), and \(n>b\) be integers. Draw \(W\) uniformly from the length-\(n\) words over a labeled \(q\)-symbol alphabet with no equal adjacent symbols. Let \(S_{n,b}(W)\) be the number of **distinct** words obtained by deleting **exactly one nonwrapping consecutive block of \(b\) symbols**. Put \(L=n-b\) and
\[
r=-\frac{1}{q-1},\quad u_k=\frac{1+(q-1)r^k}{q},\quad v_k=\frac{1-r^k}{q},\quad p=u_b.
\]
For \(1\le d<b\), define
\[
c_d=u_d^2u_{b-d}+(q-1)v_d^2v_{b-d}-p^2
=\frac{q-1}{q^2}r^{2d}(1-r^{b-d})(1+(q-1)r^{b-d}).
\]
Then the exact all-length first and second moments are
\[
\mathbb E S_{n,b}=1+L(1-p),\qquad
\operatorname{Var}(S_{n,b})=Lp(1-p)+2\sum_{d=1}^{\min(b-1,L-1)}(L-d)c_d.
\]
All covariance terms vanish when \(d=b-1\), and are **strictly positive** when \(1\le d\le b-2\). In particular, for \(b=2\) the *entire distribution* simplifies to
\[
S_{n,2}\ \overset{d}{=}\ 1+\operatorname{Binomial}\!\left(n-2,\frac{q-2}{q-1}\right),
\]
whereas for every \(b\ge3\), the adjacent return indicators have strictly positive covariance. For any fixed \(q\ge3\) and \(b\ge2\), as \(n\to\infty\),
\[
\frac{S_{n,b}-\mathbb E S_{n,b}}{\sqrt n}
\ \Longrightarrow\ \mathcal N(0,\sigma_{q,b}^2),\qquad
\sigma_{q,b}^2=p(1-p)+2\sum_{d=1}^{b-1}c_d>0.
\]

## Assumptions and scope
Indices below begin at zero. Words are linear, the alphabet is labeled, and outputs agreeing symbol-by-symbol are counted once even if they arise from different deletion sites. Only a single burst of **exactly** \(b\) adjacent deletions is allowed, not an arbitrary \(b\)-subset of deleted positions and not a cyclic deletion. The source is uniform over the \(q(q-1)^{n-1}\) admissible words. The exact moments hold for any \(n>b\), with empty covariance sums interpreted as zero. The Gaussian claim takes \(q,b\) fixed before \(n\to\infty\); it makes no joint large-alphabet or growing-burst assertion.

## Proof
**Step 1: a deterministic collision identity.** Let \(Y_i\) be the output after erasing positions \(i,i+1,\ldots,i+b-1\), for \(0\le i\le n-b\). Directly comparing the two retained strings for \(i<j\) gives
\[
Y_i=Y_j\quad\Longleftrightarrow\quad
W_{t}=W_{t+b}\ \text{for every }\ i\le t<j.
\]
In particular, \(Y_i=Y_{i+1}\) exactly when \(W_i=W_{i+b}\). All equality classes of the \(Y_i\) are therefore contiguous intervals of starting indices. Consequently the number of distinct outputs is
\[
S_{n,b}=1+\sum_{i=0}^{n-b-1}\mathbf1\{W_i\ne W_{i+b}\}.
\]
The deterministic identity is not claimed as new: see the earlier general burst-ball formula in Reference 1.

**Step 2: independence blocks.** Identify the alphabet with residues modulo \(q\) (no field structure is used). Under the stated uniform source, \(W_0\) is uniform and independent of increments \(U_i=W_{i+1}-W_i\pmod q\), which are independent and uniform on the nonzero residues. Write \(E_i=\mathbf1\{W_i=W_{i+b}\}=\mathbf1\{U_i+\cdots+U_{i+b-1}=0\pmod q\}\). Thus \((E_i)\) is stationary and \(b\)-dependent: any groups of indicators whose index sets are separated by at least \(b\) use disjoint independent increments.

**Step 3: exact return and pair probabilities.** The transition matrix for \(W\) is \(P=(J-I)/(q-1)\). Its diagonal and off-diagonal entries in \(P^k\) are respectively \(u_k\) and \(v_k\), by diagonalizing the constant-vector eigenmode and the \((q-1)\)-dimensional eigenmode with eigenvalue \(r\). Therefore \(\Pr(E_i=1)=p=u_b\). For \(1\le d<b\), conditioning on the symbols at positions \(i,i+d,i+b,i+b+d\) shows
\[
\Pr(E_i=E_{i+d}=1)=u_d^2u_{b-d}+(q-1)v_d^2v_{b-d}.
\]
Subtracting \(p^2\) and simplifying the explicit eigenvalue forms gives the stated \(c_d\). It is zero for \(d=b-1\), since \(1+(q-1)r=0\), and strictly positive for \(d\le b-2\), because \(-1<r<0\) and \(b-d\ge2\). For \(d\ge b\) covariance is zero by disjoint increments. Summing the stationary means and covariances of \(S_{n,b}=1+L-\sum_i E_i\) proves the finite-length identities.

**Step 4: exact two-deletion binomial law.** For \(b=2\), the condition \(E_i=1\) is \(U_i+U_{i+1}=0\). Given any previous increments, the new independent nonzero increment \(U_{i+1}\) matches the required negative of \(U_i\) with fixed probability \(1/(q-1)\). Induction makes the full family \(E_0,\ldots,E_{L-1}\) independent Bernoulli variables with this parameter, proving the claimed shifted binomial distribution for \(S_{n,2}\).

**Step 5: Gaussian fluctuations.** For fixed \(q,b\), \((E_i-p)\) is a uniformly bounded, stationary, \(b\)-dependent sequence and its asymptotic variance per index is \(\sigma_{q,b}^2>0\), since \(0<p<1\) and all \(c_d\ge0\). For completeness, partition the index range into long blocks of length \(\lfloor L^{1/3}\rfloor\) separated by gaps of \(b\) indices. The long-block sums are independent; the omitted gaps have total variance \(O_b(L^{2/3})=o(L)\). Each centered block is bounded by \(O(L^{1/3})=o(\sqrt L)\), so Lindeberg's condition holds for the independent-block array. Their variance divided by \(L\) converges to \(\sigma_{q,b}^2\). The independent-array CLT and negligibility of omitted gaps prove the stated limit by Slutsky's theorem.

## Verification
The self-contained Python program `burst_check.py` enumerates all nonzero modular increment sequences for \(q\in\{2,3,4\}\) and \(2\le n\le9\) where the total is computationally bounded. It separately constructs actual sets of burst-erasure outputs, computes empirical means and variances exactly as rational numbers, evaluates the closed formulas, verifies their two algebraic covariance expressions, and checks all two-burst binomial histogram coefficients. The observed output is `VERIFY_OK 108 (q,n,b) strata; exact moments and sphere counts; n up to 9`. Finite checks are only corroboration of the proof; they do not establish the infinite-domain identities or the limit theorem.

## Relationship to prior work
The deterministic burst-deletion sphere-size formula and the unconstrained **binary** sphere-size histogram are due to older work, including Levenshtein and Schoeny–Wachter-Zeh–Gabrys–Yaakobi (Reference 1, Section IV and Appendix A). They are neither new nor treated as independent proofs of the stochastic result here. The new assessed content is the **uniform no-equal-neighbors, nonbinary** source law: exact covariance/dispersion at every finite length, the sharp independence-versus-positive-correlation burst threshold, and fixed-parameter Gaussian fluctuations. The proper-word/Kautz shift is independently motivated by homopolymer avoidance in Reference 2, whose Kautz-sequence results concern universal cycles, not burst-deletion fluctuation statistics.

## Limitations
No claim of optimal codebook size, encoding redundancy, reliability against two separate bursts, or large-\(b\) normal approximation is made. The source restriction applies to the input only; erasing symbols can create adjacent equal symbols in outputs. The deterministic formula and ordinary spectral/finite-dependent central-limit techniques are known; their combination for this specific constrained-source burst channel is the assessed contribution. An earlier equivalent result in unindexed constrained-coding or symbolic-dynamics literature remains possible. No independent mathematical audit is represented.

## References
1. C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820, first publicly posted 2016-02-22. https://arxiv.org/abs/1602.06820 . Consulted full HTML v2: https://arxiv.org/html/1602.06820v2 , particularly Sections II, IV, V and Appendix A.
2. Y.-P. Chen, J. Sima, and O. Milenkovic, *Generalized Orthogonal de Bruijn and Kautz Sequences*, Entropy 27(4), 366 (2025), https://doi.org/10.3390/e27040366 . Consulted introduction and Section 6 on proper-word/Kautz constraints.
