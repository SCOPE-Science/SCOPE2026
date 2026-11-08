# Gaussian, logarithmic and birthday-window laws for the temporal proportionality price

## Finding
For every integer \(n\ge2\), every positive integer \(a\), and any number \(R_n\ge1\) of named parties, let each of \(n\) voters independently choose one party uniformly, approving that party's candidate in every round of an \(\ell=an\)-round temporal approval election. Every round selects one candidate and the candidate may recur. Write \(B_{n,j}\) for party populations, \(M_n=\max_j B_{n,j}\), and \(Q_n=\sum_j B_{n,j}^2\). Define the price \(\rho_n^\Phi\) as unconstrained maximum total approval welfare divided by maximum welfare subject to \(\Phi\).

The three group-proportionality axioms \(\Phi\in\{\mathrm{PJR},\mathrm{EJR},\mathrm{EJR+}\}\), in their temporal definitions, have exactly the same attainable welfare here, and for each realized electorate:
\[
\max_{o:\Phi(o)}\operatorname{UTIL}(o)=aQ_n,\qquad
\rho_n^\Phi=\rho_n=\frac{nM_n}{Q_n}.
\]
Thus the price does not depend on which of the three axioms is chosen or on the positive integer multiplier \(a\). Under independent uniform party choices, the following distributional limits all hold.

**A. Fixed party menu.** If \(R_n=r\ge2\) is fixed and \(G_1,\ldots,G_r\) are independent standard Gaussians, with \(\bar G=r^{-1}\sum_jG_j\), then
\[
\rho_n\xrightarrow{\Pr}1,\qquad
\sqrt n(\rho_n-1)\Rightarrow\sqrt r\left(\max_jG_j-\bar G\right).
\]

**B. Linear-sized party menu.** If \(R_n/n\to1/\lambda\) for fixed \(\lambda>0\), then
\[
\frac{\rho_n}{\log n/\log\log n}\xrightarrow{\Pr}\frac1{1+\lambda}.
\]

**C. Sparse staircase.** If \(R_n\sim n^\gamma\), where \(1<\gamma<2\) and \(\gamma/(\gamma-1)\notin\mathbb Z\), then
\[
\rho_n\xrightarrow{\Pr}\left\lfloor\frac\gamma{\gamma-1}\right\rfloor.
\]
At the exact staircase thresholds, for any fixed integer \(k\ge2\), fixed \(c>0\), and \(R_n\sim c n^{k/(k-1)}\), put \(\theta=1/(k!c^{k-1})\). Then
\[
\rho_n\Rightarrow(k-1)+B,\qquad B\sim\operatorname{Bernoulli}(1-e^{-\theta}).
\]
In particular, at the birthday threshold \(R_n\sim c n^2\), the price has limiting mass \(e^{-1/(2c)}\) at one and the remaining mass at two. If \(R_n/n^2\to\infty\), then \(\Pr(\rho_n=1)\to1\).

This is an exact finite welfare identity and a multi-scale typical-case theorem; it does not assert worst-case bounds for unrestricted temporal elections.

## Assumptions and scope
There is one candidate per party, each voter approves exactly one candidate (their party's) in every round, and approvals are static and nonempty. Empty parties are allowed, but every voter has exactly one approved candidate. The horizon is \(\ell=an\) for an integer \(a\ge1\), possibly varying with \(n\). Utilitarian welfare counts approving voter-round pairs. Axioms PJR, EJR and EJR+ are those of temporal approval voting, not one-shot committee voting. All limits use \(n\to\infty\); the number of party labels has the scaling explicitly stated in each part. Natural logarithms are used. Independent per-voter choices are essential to the stochastic laws.

## Proof
### 1. Deterministic proportionality and welfare identity
Condition on a vector of populations \(b_1,\ldots,b_R\) with sum \(n\), and let \(x_j\) be the number of rounds in which party candidate \(j\) wins, so \(\sum_jx_j=an\). The unanimous group of all \(b_j\) voters approving candidate \(j\) agrees in every one of the \(an\) rounds. Under temporal PJR or EJR this group is entitled to \(\lfloor(an)b_j/n\rfloor=ab_j\) satisfied rounds. All these voters have satisfaction exactly \(x_j\), so each axiom forces \(x_j\ge ab_j\). The same follows from EJR+: for the group of \(b_j\) voters take \(\sigma=b_j\) and \(\tau=an\); whenever any round selects a candidate other than \(j\), the EJR+ disjunction forces at least one member to have satisfaction \(ab_j\). If every round instead selects \(j\), the inequality also holds. Groups with zero size are immaterial.

Since \(\sum_jab_j=an=\sum_jx_j\), the preceding inequalities imply \(x_j=ab_j\) simultaneously for every \(j\). Conversely these counts satisfy all three axioms. Any voter group with a unanimous approved candidate must consist entirely of voters from one party, and its greatest possible proportional claim is at most that party's \(ab_j\) satisfaction; mixed groups have no unanimously approved candidate, so they create no PJR/EJR group demand and no EJR+ round-specific demand. The EJR+ satisfaction disjunction is met for homogeneous groups at every admissible \(\sigma,\tau\), since \(\lfloor\tau\sigma/n\rfloor\le ab_j\).

Each victory of party \(j\) produces exactly \(b_j\) approval units, hence constrained maximum welfare equals \(\sum_jb_j(ab_j)=a\sum_jb_j^2=aQ_n\), whereas unconstrained welfare is \((an)\max_jb_j=anM_n\). The identity follows, even if some parties are empty.

### 2. Occupancy denominator
The random party populations have multinomial distribution. Let \(C_n=\sum_{1\le u<v\le n}\mathbf1\{\text{voters }u,v\text{ chose the same party}\}\). Counting within-party pairs yields the exact identity \(Q_n=n+2C_n\). Each coincidence indicator has mean \(1/R_n\), and distinct indicators are pairwise independent, even when the corresponding pairs share one voter. Thus
\[
\mathbb EC_n=\binom n2R_n^{-1},\qquad
\operatorname{Var}(C_n)=\binom n2R_n^{-1}(1-R_n^{-1}).
\]
If \(R_n/n\to1/\lambda\), this proves \(Q_n/n\to1+\lambda\) in \(L^2\). If \(R_n/n\to\infty\), nonnegativity and Markov's inequality give \(Q_n/n\to1\) in probability. These statements account for the normalization \(Q_n\), not merely for the maximum load.

### 3. Fixed menu
For fixed \(r\), the multinomial central limit theorem gives
\[
\left(\frac{B_{n,j}-n/r}{\sqrt n}\right)_{j=1}^r
\Rightarrow\left(\frac{G_j-\bar G}{\sqrt r}\right)_{j=1}^r.
\]
Because \(\sum_j(B_{n,j}-n/r)=0\), we have \(Q_n=n^2/r+\sum_j(B_{n,j}-n/r)^2=n^2/r+O_{\Pr}(n)\). Substitution into the exact ratio and continuity of the maximum yields part A, including the displayed Gaussian-maximum (non-Gaussian for \(r\ge2\)) law.

### 4. Linear menu
Set \(L_n=\log n/\log\log n\). If \(R_n\sim n/\lambda\), use a union bound and \(\Pr(B_{n,1}\ge h)\le\binom nhR_n^{-h}\) to show \(\Pr(M_n\ge\lceil(1+\varepsilon)L_n\rceil)\to0\) for any fixed \(\varepsilon>0\). For the lower bound let \(h=\lfloor(1-\varepsilon)L_n\rfloor\) and let \(Y_h\) count parties with occupancy exactly \(h\). Then
\[
\mathbb EY_h=R_n\binom nhR_n^{-h}(1-R_n^{-1})^{n-h}=n^{\varepsilon+o(1)}\to\infty.
\]
Moreover, the exact joint occupancy probability for two distinct parties is
\[
\Pr(B_{n,1}=h,B_{n,2}=h)
=\frac{n!}{(h!)^2(n-2h)!}R_n^{-2h}(1-2/R_n)^{n-2h}.
\]
Dividing by the square of the one-party probability gives \(1+o(1)\) because \(h=O(\log n/\log\log n)=o(\sqrt n)\) and \(R_n\asymp n\). Hence \(\operatorname{Var}(Y_h)/(\mathbb EY_h)^2\to0\), and \(\Pr(M_n\ge h)\to1\). Thus \(M_n/L_n\to1\) in probability; combine with section 2 for part B.

### 5. Sparse birthday windows and staircase
For fixed \(k\ge2\), let \(Y_{n,k}\) be the number of parties with exactly \(k\) voters. When \(R_n\sim c n^{k/(k-1)}\), the falling-factorial moments obey, for every fixed positive integer \(d\),
\[
\mathbb E(Y_{n,k})_d
=(R_n)_d\frac{(n)_{kd}}{(k!)^dR_n^{kd}}(1-d/R_n)^{n-kd}
\longrightarrow\left(\frac1{k!c^{k-1}}\right)^d.
\]
(The notation \((z)_d\) is the falling factorial.) By the factorial-moment characterization, \(Y_{n,k}\Rightarrow\operatorname{Poisson}(\theta)\). Simultaneously, a union bound gives \(\Pr(M_n\ge k+1)\le\binom n{k+1}R_n^{-k}\to0\). The expected number of parties with exactly \(k-1\) voters diverges like a positive constant times \(n^{1/(k-1)}\), and the two-party joint-count formula shows its relative variance tends to zero. Therefore \(\Pr(M_n\ge k-1)\to1\). Since \(Q_n/n\to1\), the stated two-point law for the price follows.

For \(R_n\sim n^\gamma\) at noncritical \(1<\gamma<2\), write \(k=\lfloor\gamma/(\gamma-1)\rfloor\). Now \(n^k/R_n^{k-1}\to\infty\) and \(n^{k+1}/R_n^k\to0\). The same exact occupancy moment estimates give at least one \(k\)-occupied party with high probability, while the union bound excludes all \((k+1)\)-occupied parties. Hence \(M_n\to k\) in probability and \(Q_n/n\to1\), proving the staircase law. Finally, if \(R_n/n^2\to\infty\), then \(\Pr(C_n>0)\le\binom n2/R_n\to0\). When \(C_n=0\), all nonempty parties are singletons and the exact identity gives \(\rho_n=1\), completing the proof.

## Verification
A standalone Python 3 checker in `check.py` exhaustively tests 848 small approval-profile, party-menu and integer-horizon instances using literal PJR, EJR and EJR+ tests on voter subsets and all candidate-multiplicity vectors. In all cases the three constrained welfare maxima equal \(aQ_n\), and the ratio matches \(nM_n/Q_n\). The checker also confirms 62 exact sparse-occupancy factorial-moment identities by exhaustive label enumeration. Seeded simulations independently calculate the price from sampled party populations and compare the birthday-window Bernoulli masses for \(k=2,3,4\), solely as finite-size sanity checks. The proof of the infinite claims is analytic; the numerical checks do not certify limits.

## Relationship to prior work
Teh, *The Price of Proportional Representation in Temporal Voting* (first public May 11, 2026), defines the same welfare ratio and group-proportionality axioms, establishes worst-case efficiency losses, and proves the static-profile equivalence of EJR and EJR+ (Lemma 4.2). It does not provide a distribution law for the welfare price under random party choice, a birthday-window transition, or the resulting reentrant behavior. The random-party model is a specialized stochastic complement to those worst-case results. Standard balls-into-bins results supply the classical probabilistic context for occupancy maxima; neither the occupancy facts nor the central limit theorem are asserted to be new. The contribution is their exact connection to the common PJR/EJR/EJR+ welfare optimum and the resulting multi-scale price laws. The 2024 paper of Elkind, Neoh and Teh studies an individual proportionality notion rather than these group axioms; the 2024 paper by Elkind et al. addresses a one-shot committee instead of recurrent temporal winners.

## Limitations
The theorem assumes one approved candidate per voter, static votes, iid uniform choices and an integer multiple of the number of voters as the horizon. The joint behavior with unequal party probabilities, time-varying approval, overlapping approval sets, nonintegral horizon ratios or more general random environments is not established. The underlying classical occupancy limits and multinomial central limit theorem are not claimed as new. Unindexed equivalent fair-welfare calculations remain a literature risk.

## References
1. Nicholas Teh, *The Price of Proportional Representation in Temporal Voting*, arXiv:2605.11157, first posted 2026-05-11; IJCAI 2026, paper 394, https://ijcai.org/proceedings/2026/0394.pdf .
2. Edith Elkind, Tzeh Yuan Neoh and Nicholas Teh, *Temporal Elections: Welfare, Strategyproofness, and Proportionality*, arXiv:2408.13637 (2024), https://arxiv.org/abs/2408.13637 .
3. Edith Elkind, Piotr Faliszewski, Ayumi Igarashi, Pasin Manurangsi, Ulrike Schmidt-Kraepelin and Warut Suksompong, *The Price of Justified Representation*, ACM Transactions on Economics and Computation 12(3), article 11 (2024), https://doi.org/10.1145/3676953 .
4. *Balls into bins problem*, overview of classical maximum-load and occupancy laws, https://en.wikipedia.org/wiki/Balls_into_bins_problem .
