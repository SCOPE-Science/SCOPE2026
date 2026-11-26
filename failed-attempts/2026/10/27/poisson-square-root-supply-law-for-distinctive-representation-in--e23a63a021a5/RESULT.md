# Poisson square-root supply law for distinctive representation in random approval elections

## Finding

Fix an integer \(k\geq2\). In an approval election with \(n\) voters and \(m_n\geq k\) candidates, each voter independently approves each candidate with probability
\[
p_n=\frac1k+\frac{\lambda}{\sqrt n},\qquad \lambda\in\mathbb R\text{ fixed},
\]
for all sufficiently large \(n\). Assume \(m_n\leq n^B\) for some fixed finite \(B>0\). A committee of size \(k\) has **distinctive representation (DR)** when it satisfies justified representation (JR) and each elected candidate has exactly \(q_n=\lceil n/k\rceil\) supporters.

Let \(E_n\) be the number of candidates having exactly \(q_n\) supporters; let \(H_n\) be the number of DR committees. Write
\[
v_k=\frac{k-1}{k^2},\qquad
r_{k,\lambda}=\frac{\exp[-\lambda^2/(2v_k)]}{\sqrt{2\pi v_k}},\qquad
a_n=\Pr\{\operatorname{Bin}(n,p_n)=q_n\}.
\]
Then \(E_n\) has the exact binomial law \(\operatorname{Bin}(m_n,a_n)\), and \(\sqrt n\,a_n\longrightarrow r_{k,\lambda}\). Moreover, with probability at least
\[
1-\binom{m_n}{k}(m_n-k)\exp\!\left(-\frac{n}{2k^4}\right),
\]
**every committee of \(k\) exact-quota candidates satisfies JR**, so \(H_n=\binom{E_n}{k}\) simultaneously for all such committees. In particular, with \(D_n=\{H_n\geq1\}\),
\[
0\leq\Pr\{E_n\geq k\}-\Pr(D_n)
\leq\binom{m_n}{k}(m_n-k)\exp\!\left(-\frac{n}{2k^4}\right)
\]
for all sufficiently large \(n\).

If \(m_n/\sqrt n\longrightarrow\tau\in[0,\infty)\), then, for a Poisson variable \(Z\) with mean \(\mu=\tau r_{k,\lambda}\),
\[
H_n\ \xrightarrow{\ d\ }\ \binom Zk,
\qquad
\Pr(D_n)\longrightarrow 1-e^{-\mu}\sum_{j=0}^{k-1}\frac{\mu^j}{j!},
\qquad
\mathbb E H_n\longrightarrow\frac{\mu^k}{k!}.
\]
Thus candidate supply has an exact critical scale of order \(\sqrt n\): if \(m_n=o(\sqrt n)\), DR fails with probability tending to one, whereas if \(m_n/\sqrt n\to\infty\) subject to the polynomial bound, DR holds with probability tending to one. For any *fixed* approval probability \(p\in(0,1)\setminus\{1/k\}\) and polynomially bounded \(m_n\), DR instead fails with probability tending to one.

## Assumptions and scope

Voters and candidates are labeled. The approval matrix consists of independent Bernoulli variables with common parameter \(p_n\). The integer \(k\) and real \(\lambda\) do not vary with \(n\); \(m_n\) may vary but grows at most polynomially. The statement applies only when \(0<p_n<1\), which holds eventually for fixed \(k,\lambda\). For any voter group \(S\) with \(|S|\geq n/k\) whose members share an approved candidate, JR requires that at least one voter in \(S\) approves some elected candidate. Unlike coverage of *all* voters, JR need only represent cohesive groups.

The count \(H_n\) is the number of **labeled size-\(k\) candidate subsets** satisfying both conditions; repeated support sets are not identified. The limiting claim for \(m_n/\sqrt n\to\tau\) includes \(\tau=0\), with the limiting Poisson variable identically zero. The explicit error bound may exceed one at small \(n\); it is meaningful asymptotically and valid mathematically whenever the proof's sufficiently-large-\(n\) conditions hold.

## Proof

**1. Criterion for JR.** Fix any committee \(W\) of size \(k\), let \(R_W\) be the voters approving at least one member of \(W\), and set \(U_W=[n]\setminus R_W\). For candidate \(d\), let \(N_d\) denote its supporter set. JR fails exactly when some cohesive group lies wholly inside \(U_W\). This is equivalent to the existence of a candidate \(d\) satisfying
\[
|N_d\cap U_W|\geq\lceil n/k\rceil=q_n.
\]
Indeed, any \(q_n\) such supporters form a cohesive, unrepresented group, while any violating cohesive group contains at least \(q_n\) unrepresented supporters of one of its commonly approved candidates. Every \(d\in W\) has \(N_d\cap U_W=\emptyset\).

**2. Uniform exponential protection of quota committees.** Fix a committee \(W\) of \(k\) distinct candidates; condition on all approval edges incident to candidates in \(W\), and suppose each elected candidate has exactly \(q_n\) supporters. Because \(W\) contains an exact-quota candidate,
\[
|U_W|\leq n-q_n.
\]
For any \(d\notin W\), independence across candidate columns gives, conditional on the selected columns,
\[
X_{d,W}:=|N_d\cap U_W|\sim\operatorname{Bin}(|U_W|,p_n).
\]
For sufficiently large \(n\), we have \(p_n\leq1/k+1/(4k^2)\). Hence
\[
\begin{aligned}
q_n-\mathbb E[X_{d,W}\mid W\text{ columns}]
&\geq \frac nk-(n-q_n)\left(\frac1k+\frac1{4k^2}\right)\\
&\geq\frac{3n}{4k^2}\geq\frac n{2k^2}.
\end{aligned}
\]
Hoeffding's inequality for independent Bernoulli trials, together with \(|U_W|\leq n\), therefore gives
\[
\Pr\{X_{d,W}\geq q_n\mid W\text{ columns}\}
\leq \exp\left(-\frac{2[n/(2k^2)]^2}{|U_W|}\right)
\leq\exp\left(-\frac n{2k^4}\right)
\]
when \(|U_W|>0\); if \(|U_W|=0\), the failure probability is zero. There are \(\binom{m_n}{k}\) committees and at most \(m_n-k\) outside candidates per committee. Union-bounding all pairs proves that, except on the displayed exponentially unlikely event, all exact-quota committees satisfy JR simultaneously. On its complement, every \(k\)-subset counted by \(\binom{E_n}{k}\) is DR, and no other committee is DR; hence \(H_n=\binom{E_n}{k}\). The inequality for DR existence follows because \(D_n\subseteq\{E_n\geq k\}\).

**3. Candidate-count law.** Different candidate columns are independent, and each contains \(q_n\) approvals with probability \(a_n\). Therefore \(E_n\sim\operatorname{Bin}(m_n,a_n)\) exactly. Since \(q_n=n/k+O(1)\), \(p_n=1/k+\lambda/\sqrt n\), and \(v_k=(1/k)(1-1/k)>0\), Stirling's formula applied to
\[
a_n=\binom n{q_n}p_n^{q_n}(1-p_n)^{n-q_n}
\]
gives the local central limit estimate
\[
a_n=\frac{r_{k,\lambda}+o(1)}{\sqrt n}.
\]
This step uses both the local-Gaussian prefactor and the centered displacement of order \(\sqrt n\); it is not a global normal CDF approximation.

**4. Critical law and moments.** If \(m_n/\sqrt n\to\tau<\infty\), then \(m_na_n\to\mu=\tau r_{k,\lambda}\) and \(a_n\to0\). The standard binomial-to-Poisson law gives \(E_n\Rightarrow Z\sim\operatorname{Poisson}(\mu)\). The simultaneous-JR bound tends to zero because \(m_n\) is polynomial, yielding the asserted distribution of \(H_n\) and its existence probability. For the expectation, note that \(0\leq\binom{E_n}{k}-H_n\leq\binom{m_n}{k}\mathbf1_{\mathcal B_n}\) on the exceptional event \(\mathcal B_n\). Thus
\[
\left|\mathbb E H_n-\binom{m_n}{k}a_n^k\right|
\leq\binom{m_n}{k}^2(m_n-k)e^{-n/(2k^4)}=o(1).
\]
Here \(\mathbb E\binom{E_n}{k}=\binom{m_n}{k}a_n^k\to\mu^k/k!\). If \(m_n/\sqrt n\to\infty\), then \(m_na_n\to\infty\) and \(\Pr(E_n\geq k)\to1\), for example by a variance bound, so DR exists with high probability by Step 2. If \(m_n=o(\sqrt n)\), Markov's inequality applied to \(E_n\) gives \(\Pr(D_n)\leq\Pr(E_n\geq k)\to0\).

**5. Off-critical scarcity.** For fixed \(p\in(0,1)\setminus\{1/k\}\), the binomial Chernoff bound or Stirling's entropy estimate gives \(\Pr\{\operatorname{Bin}(n,p)=q_n\}=\exp[-n D(1/k\Vert p)+o(n)]\) with strictly positive Bernoulli relative entropy \(D(1/k\Vert p)\). Polynomially many independent columns then contain no quota-exact candidate with probability tending to one; DR is impossible. This does not rely on Step 2.

## Verification

The standalone program `verify_dr.py` exhaustively checked \(2^{nm}\) approval profiles for \((n,m,k)=(3,3,2),(4,3,2),(5,3,2)\). It compared JR's group-by-group definition with the uncovered-support criterion for every committee, and counted quota-feasible and DR-feasible profiles. At \((4,3,2)\), the exact counts were \(1296\) profiles with enough quota-exact candidates versus \(1242\) admitting DR, demonstrating why the theorem is probabilistic rather than an unconditional deterministic equivalence. It also checked the local-Gaussian coefficient numerically and compared \(2400\) seeded samples with the exact independent-column binomial probability. All encoded checks passed. These finite checks support but do not replace the infinite proof.

Reproduce with an ordinary Python 3 installation by executing `python3 verify_dr.py` from the directory containing the standalone file. No third-party libraries are required.

## Relationship to prior work

Chingoma, Grossi, Lindeboom, and Maly introduced DR with precisely the JR-plus-exact-support definition in Definition 22 of their 2026 preprint. Their Section 6 and Appendix D establish general impossibility instances and hardness of DR decision; their Section 8 reports empirical tests mainly of related optimization notions. They do not give the square-root candidate-supply asymptotic, an exact limiting probability, or the joint law of DR committee counts under this independent Bernoulli model.

Han, Tao, Xia, Zhang, and Zhou (2025) study random **average justified representation (AJR)** elections under a constant candidate count and find approval-probability phase transitions. AJR is different from DR and does not impose exact supporter counts. Their results do not imply the Poisson quota-candidate count or the simultaneous JR equivalence derived here. Elkind and coauthors (2021/2023, Theorem 3.1 and Proposition 1) show that under independent approval sampling with **fixed** candidate count and approval probability, all size-\(k\) committees satisfy JR with high probability. The new simultaneous-JR estimate extends this behavior to polynomially many candidates **after conditioning on exact-quota supporter counts**; the exact support rarity then creates the nondegenerate square-root candidate-supply window and a transformed Poisson committee-count law. The earlier fixed-candidate JR theorem alone does not determine the probability or count of DR committees in this growing-candidate regime.

The novelty claim is restricted to combining the **specific DR axiom**, polynomial candidate supply, a moving central-limit approval window, a quantitative JR error, and the limiting random count of feasible DR committees. Standard local binomial asymptotics and Poisson approximation are used as established tools, not claimed as new methods.

## Limitations

The model assumes complete voter/candidate independence and homogeneous approval probabilities; correlations and heterogeneous voter types may change both supply and JR behavior. The result fixes \(k\); it does not cover committee sizes growing with \(n\), exponentially many candidates, or an adversarial approval matrix. Off-critical scarcity is stated only for fixed \(p\), not every moving sequence. The central limit concerns eligible candidates and existence, not the quality of non-DR committees. The paper-priority comparison cannot exclude inaccessible or unindexed literature; no independent scientific audit has been performed.

## References

1. J. Chingoma, D. Grossi, F. Lindeboom, J. Maly. *Diverse Representation in Approval-Based Committee Voting.* arXiv:2609.29332v1 (first public 2026-09-24), Definition 22, Section 6, Appendix D, Section 8. https://arxiv.org/abs/2609.29332
2. Q. Han, B. Tao, L. Xia, C. Zhang, H. Zhou. *Likelihood of the Existence of Average Justified Representation.* arXiv:2510.18718v1 (first public 2025-10-21), Sections 1–3, 6. https://arxiv.org/abs/2510.18718
3. E. Elkind, P. Faliszewski, A. Igarashi, P. Manurangsi, U. Schmidt-Kraepelin, W. Suksompong. *Justifying Groups in Multiwinner Approval Voting.* arXiv:2108.12949 (first public 2021-08-30); *Theoretical Computer Science* 969 (2023), 114039. https://arxiv.org/abs/2108.12949
