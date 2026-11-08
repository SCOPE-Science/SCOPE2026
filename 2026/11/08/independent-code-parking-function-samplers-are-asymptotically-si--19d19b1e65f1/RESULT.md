# Independent-code parking-function samplers are asymptotically singular from uniform parking functions

## Finding

Let \(PF_n\) denote the parking functions of length \(n\): vectors \(\pi\in\{1,\ldots,n\}^n\) satisfying \(\#\{i:\pi_i\le k\}\ge k\) for every \(1\le k\le n\). Write \(U_n\) for the uniform probability law on \(PF_n\).

For each \(n\), independently sample arbitrary random variables \(X_{n,j}\in\{1,\ldots,j\}\), \(1\le j\le n\), with completely unrestricted marginal laws, which may depend on \(n\). Independently sample a uniform random permutation \(\tau_n\) of \(\{1,\ldots,n\}\) and put
\[
\Pi_n=(X_{n,\tau_n(1)},\ldots,X_{n,\tau_n(n)}),\qquad Q_n=\mathcal L(\Pi_n).
\]
Then \(Q_n\) is supported on \(PF_n\), and **uniformly over all choices of the independent coordinate laws**,
\[
\boxed{\lim_{n\to\infty}\ \inf_{\mathcal L(X_{n,1}),\ldots,\mathcal L(X_{n,n})}
\lVert Q_n-U_n\rVert_{\mathrm{TV}}=1.}
\]
In particular, for the Mallows-permutation-generated parking-function law \(\mathcal P_n^{(q_n)}\) introduced by Pinsky, **every deterministic sequence** \(q_n\in(0,\infty)\) satisfies
\[
\boxed{\lim_{n\to\infty}\lVert\mathcal P_n^{(q_n)}-U_n\rVert_{\mathrm{TV}}=1.}
\]
Thus no choice of the Mallows parameter can keep the full-law total-variation distance asymptotically below one; the minimum asymptotic distance asked about in Pinsky's open question is one.

## Assumptions and scope

The coordinates \(X_{n,1},\ldots,X_{n,n}\) are mutually independent for each \(n\), but are not required to be identically distributed. Their marginal distributions and the sampling permutation may vary from row to row; the permutation is uniform and independent of the coordinates. Only the support condition \(X_{n,j}\in\{1,\ldots,j\}\) is imposed. The assertion concerns total variation of the *entire* probability measures on \(PF_n\), not a fixed number of sampled entries. No probabilistic coupling between different values of \(n\) is assumed.

Total variation is \(\lVert Q-U\rVert_{\mathrm{TV}}=\sup_{A\subseteq PF_n}|Q(A)-U(A)|\). For an integer \(k\in[1,n]\), define the parking surplus
\[
S_n(k;\pi)=\#\{i:\pi_i\le k\}-k\ge0.
\]
Fix the bulk cutoff \(k_n=\lfloor n/2\rfloor\) and abbreviate \(S_n=S_n(k_n;\Pi_n)\). For the uniform parking function denote the corresponding statistic by \(S_n^{\mathrm{unif}}\).

## Proof

**1. Independent-code surplus.** For every \(k\), the first \(k\) coordinate variables satisfy \(X_{n,j}\le j\le k\), so the coordinate multiset obeys the parking inequalities. Its random permutation is therefore a parking function. At \(k=k_n\), permutation has no effect on the count and
\[
S_n=\sum_{j=k_n+1}^{n}\mathbf1\{X_{n,j}\le k_n\}.
\]
The summands are independent Bernoulli variables. Write \(m_n=\mathbb E_{Q_n}S_n\). Then
\[
0\le m_n\le n-k_n,\qquad
\operatorname{Var}_{Q_n}(S_n)=\sum_{j=k_n+1}^n p_{n,j}(1-p_{n,j})\le m_n,
\]
where \(p_{n,j}=\Pr(X_{n,j}\le k_n)\). These are exact identities for every choice of coordinate laws.

**2. Continuous bulk-surplus law under the uniform ensemble.** The established parking-function empirical-process theorem of Chassaing--Marckert and Diaconis--Hicks gives
\[
\left(\sqrt n\left[n^{-1}\#\{i:\pi_i\le\lfloor nt\rfloor\}-\frac{\lfloor nt\rfloor}{n}\right]\right)_{0\le t\le1}
\ \Longrightarrow\ (e(t))_{0\le t\le1},
\]
under \(U_n\), where \(e\) is standard Brownian excursion. In particular,
\[
Y_n:=S_n^{\mathrm{unif}}/\sqrt n\Longrightarrow Y=e(1/2).
\]
The law of \(Y\) is non-atomic and tight: it is the law of the Euclidean length of three independent centered normal variables of variance \(1/4\). (One may also obtain the empirical-process theorem by applying the cyclic parking lemma to a multinomial occupancy bridge, then Donsker's theorem and Vervaat's bridge-to-excursion transformation.)

We record the following elementary anti-concentration consequence. Whenever \(Y_n\Rightarrow Y\) and \(Y\) has no atoms, for every deterministic \(\varepsilon_n\downarrow0\),
\[
\omega_n(\varepsilon_n):=\sup_{a\in\mathbb R}\Pr_{U_n}\{|Y_n-a|\le\varepsilon_n\}\longrightarrow0.
\]
Indeed, if not, tightness yields a subsequence of centers with positive mass and a further convergent subsequence of those centers. The portmanteau theorem would then give positive probability to one point of the limit law, a contradiction.

**3. A separating event, uniformly over code distributions.** Consider two alternatives determined only by the deterministic mean \(m_n\).

If \(m_n\le n^{2/3}\), take
\[
A_n=\{|S_n-m_n|\le n^{5/12}\}.
\]
Chebyshev's inequality and the variance bound imply
\[
Q_n(A_n)\ge1-\frac{m_n}{n^{5/6}}\ge1-n^{-1/6}.
\]
Under \(U_n\), the same event corresponds to a shrinking interval for \(Y_n\), centered at \(m_n/\sqrt n\) with radius \(n^{-1/12}\). Hence
\[
U_n(A_n)\le\omega_n(n^{-1/12})=o(1)
\]
uniformly over the possible centers.

If \(m_n>n^{2/3}\), instead take
\[
B_n=\{S_n>m_n/2\}.
\]
Chebyshev again gives
\[
Q_n(B_n)\ge1-\frac{4\operatorname{Var}(S_n)}{m_n^2}
\ge1-4n^{-2/3}.
\]
Under \(U_n\), this event requires \(Y_n>\frac12 n^{1/6}\), so
\[
U_n(B_n)\le\Pr_{U_n}\{Y_n>n^{1/6}/2\}\longrightarrow0
\]
by tightness. Therefore, writing
\[
r_n=\max\left\{n^{-1/6}+\omega_n(n^{-1/12}),\ 4n^{-2/3}+\Pr_{U_n}\{Y_n>n^{1/6}/2\}\right\},
\]
we have \(r_n\to0\) and, simultaneously for every independent-code law, \(\lVert Q_n-U_n\rVert_{\mathrm{TV}}\ge1-r_n\). The opposite bound \(\lVert Q_n-U_n\rVert_{\mathrm{TV}}\le1\) is automatic. This establishes uniform asymptotic singularity.

**4. Mallows consequence.** For a Mallows permutation with parameter \(q_n>0\), Pinsky records that the inversion-by-value code variables \(X_{n,j}=1+I_{n,<j}\) are independent and lie in \(\{1,\ldots,j\}\). Their exact laws are
\[
\Pr(X_{n,j}=a)=\frac{q_n^{a-1}}{\sum_{r=0}^{j-1}q_n^r},\qquad 1\le a\le j,
\]
with the continuous interpretation at \(q_n=1\). An independent random reshuffle gives precisely \(\mathcal P_n^{(q_n)}\). The preceding uniform theorem applies for every positive deterministic parameter sequence, including parameters approaching zero, one, or infinity at arbitrary rates.

## Verification

The standalone `verify.py` uses exact rational arithmetic. It independently enumerates Mallows permutations and calculates their Lehmer codes, computes the implied Poisson--binomial surplus law, verifies their agreement for \(2\le n\le6\) and \(q\in\{1/2,1,3/2,2\}\), enumerates all uniform parking functions in this range, and checks the parking inequalities for every bounded code vector. The code is a finite diagnostic, not evidence of the infinite limiting theorem. The infinite proof depends on the cited uniform parking-function excursion limit, the exact independent Bernoulli decomposition, elementary concentration, and anti-concentration of a non-atomic weak limit.

## Relationship to prior work

Pinsky (arXiv:2509.24452, first posted 2025-09-29) introduces the Mallows-based family, establishes independence of the inversion code, analyzes one-coordinate and single-symbol-count asymptotics, and explicitly asks whether any parameter regime can have a limiting full-law total-variation distance below one from the uniform parking-function law (Section 1, Open Question). The theorem above resolves that question negatively and strengthens it from Mallows laws to arbitrary independent factorial-code marginals. It uses, with explicit attribution, the uniform parking-function Brownian-excursion theorem proved by Chassaing and Marckert (2001) and presented as Theorem 15 by Diaconis and Hicks (2017). Bellin's work on small coordinate projections is compatible: agreement of small projections does not imply agreement of the full law.

## Limitations

The result concerns independent code coordinates and independent uniform reshuffling. It does not prohibit dependent-coordinate constructions, including exact uniform parking-function samplers; indeed the dependency structure in the uniform ensemble produces Brownian-excursion-scale fluctuations. No explicit optimal finite-size total-variation distance or convergence rate beyond the displayed distribution-free bound is established. The absence of an identified published equivalent is not a proof of historical uniqueness; independent priority assessment remains appropriate. Brownian-excursion weak convergence is an imported, published theorem, not newly proved here in its full functional form.

## References

1. R. G. Pinsky, *A family of non-uniform distributions on the set of parking functions generated by random permutations*, arXiv:2509.24452, first version 2025-09-29, https://arxiv.org/abs/2509.24452 .
2. P. Chassaing and J.-F. Marckert, *Parking Functions, Empirical Processes, and the Width of Rooted Labeled Trees*, Electronic Journal of Combinatorics **8** (2001), R14, https://doi.org/10.37236/1558 .
3. P. Diaconis and A. Hicks, *Probabilizing Parking Functions*, Advances in Applied Mathematics **89** (2017), 125--155, Theorem 15, https://doi.org/10.1016/j.aam.2017.05.004 ; preprint https://arxiv.org/abs/1611.09821 .
4. E. Bellin, *Asymptotic behaviour of the first positions of uniform parking functions*, Journal of Applied Probability **60** (2023), 1201--1218, https://doi.org/10.1017/jpr.2022.131 .
