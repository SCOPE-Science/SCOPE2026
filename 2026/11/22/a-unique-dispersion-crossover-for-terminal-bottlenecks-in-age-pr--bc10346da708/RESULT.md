# A unique dispersion crossover for terminal bottlenecks in age-preferential random graphs

## Finding

In the exponentially age-preferential growing multigraph, the number of terminal minimal cuts has a *unique* sub-Poisson to super-Poisson variance transition as the age-bias parameter varies. The critical bias has a two-term asymptotic when the number of parents becomes large.

Fix an integer \(m\ge1\) and \(0<q<1\). Begin with vertex \(v_0\). At birth \(t\ge1\), vertex \(v_t\) chooses \(m\) parents independently, each parent \(v_{t-d}\), \(1\le d\le t\), with probability
\[
\Pr(D_{t,a}=d)=\frac{(1-q)q^{d-1}}{1-q^t}.
\]
Parallel edges are retained. For \(j\ge0\), let \(A_j\) mean that all \(m\) parents of \(v_{j+1}\) equal \(v_j\) and *no future edge* from a vertex born after \(j+1\) has a parent among \(v_0,\ldots,v_j\). Let \(K_N=\sum_{j=0}^{N-1}\mathbf1_{A_j}\) be the number of these infinite-horizon terminal bottlenecks with cut indices below \(N\). Define
\[
P_j(q)=\prod_{h=j+1}^{\infty}(1-q^h),\quad
\rho_m(q)=\bigl[(1-q)P_0(q)\bigr]^m,
\quad S_m(q)=\sum_{j=0}^{\infty}\bigl(P_j(q)^{-m}-1\bigr).
\]
The products are strictly positive and the series converges for each fixed \(m,q\).

**Theorem.** For each fixed \(m\ge1\) and \(0<q<1\), the positive variance coefficient
\[
v_m(q)=\rho_m(q)\bigl[1-\rho_m(q)+2\rho_m(q)S_m(q)\bigr]
\]
satisfies
\[
\frac{\operatorname{Var}(K_N)}{N}\longrightarrow v_m(q),\qquad
\frac{K_N-\rho_m(q)N}{\sqrt N}\ \Longrightarrow\ \mathcal N(0,v_m(q)).
\]
Moreover,
\[
\mathbb E K_N=\rho_m(q)N+\rho_m(q)S_m(q)+O_{m,q}(q^N).
\]
There is a **unique** \(q_m\in(0,1/2)\) satisfying \(S_m(q_m)=1/2\), and it is the exact variance-to-mean crossover:
\[
\begin{aligned}
0<q<q_m&\quad\Longrightarrow\quad v_m(q)<\rho_m(q),\\
q=q_m&\quad\Longrightarrow\quad v_m(q)=\rho_m(q),\\
q_m<q<1&\quad\Longrightarrow\quad v_m(q)>\rho_m(q).
\end{aligned}
\]
The thresholds \(q_m\) strictly decrease with \(m\), and, writing \(c=\log(3/2)\),
\[
\boxed{q_m=\frac{c}{m}-\frac{13c^2}{6m^2}+O(m^{-3})\qquad (m\to\infty).}
\]
For orientation, numerical roots are \(q_1\approx0.2333802023\), \(q_2\approx0.1455841517\), and \(q_3\approx0.1064751163\). These decimal values are not used in the proof.

## Assumptions and scope

The number of parent edges \(m\) is a positive integer. Every edge-choice random variable is independent, with the geometric-age law above; no degree-dependent reinforcement is present. The limit \(N\to\infty\) holds at each *fixed* \((m,q)\). The separate expansion for \(q_m\) concerns \(m\to\infty\) and is not a uniform central limit theorem in jointly varying parameters. A terminal bottleneck is defined using all future births; \(K_N\) is not an online-observable statistic of the finite graph at time \(N\). Its exact mean and variance use the infinite process.

## Proof

**1. One- and two-cut identities.** The independent parent choices give, at the step \(j+1\), a factor \((1-q)/(1-q^{j+1})\) per edge. At step \(j+1+h\), \(h\ge1\), the conditional probability of a parent with index at least \(j+1\) is \((1-q^h)/(1-q^{j+1+h})\). Multiplying and telescoping yields
\[
b_j:=\Pr(A_j)=\left[(1-q)\prod_{h=1}^{j}(1-q^h)\right]^m
=\rho_m(q)P_j(q)^{-m}.
\]
For \(d\ge1\), condition on \(A_j\). The constraints on later births factor independently; after relabeling \(v_{j+1}\) as the root, their conditional parent distributions are the original truncated geometric-age laws. The event \(A_{j+d}\) becomes the cut event at relative index \(d-1\). Hence
\[
\Pr(A_j\cap A_{j+d})=b_jb_{d-1}.
\]
In particular \(b_j\downarrow\rho_m(q)>0\), and \(b_j-\rho_m(q)=O_{m,q}(q^{j+1})\). The probability of two prescribed cuts is thus not in general the product of their one-cut probabilities.

**2. Stationary extension and mixing.** On all integer birth labels \(t\in\mathbb Z\), take independent untruncated lags \(D_{t,a}^*\) with \(\Pr(D_{t,a}^*=d)=(1-q)q^{d-1}\) for \(d\ge1\). Define \(B_j\) by the identical terminal-cut inequalities for these lags. The two-sided indicator process \((\mathbf1_{B_j})_{j\in\mathbb Z}\) is stationary, with \(\Pr(B_j)=\rho_m(q)\), and the same conditional resetting computation gives
\[
\Pr(B_0\cap B_d)=\rho_m(q)b_{d-1},\quad d\ge1.
\]
It is exponentially strongly mixing. Indeed, truncate all conditions defining \(B_j\) for \(j\le0\) to parent choices at birth times at most \(L\). If no edge born later than \(L\) returns to a vertex with index at most zero, the entire infinite past collection of cut indicators agrees with its truncation. A union bound gives the failure probability
\[
\sum_{t>L}m\Pr(D^*_{t,a}\ge t)=\frac{mq^L}{1-q}.
\]
The truncated past depends on parent-choice variables at times at most \(L\), whereas all \(B_j\) for \(j\ge L\) depend on choices after \(L\); these are independent. Thus the strong-mixing coefficient is at most \(mq^L/(1-q)\) (up to a harmless index shift). Boundedness and exponential mixing satisfy the standard stationary strong-mixing central limit theorem.

**3. Transfer to the finite-start graph.** Couple each actual lag at birth \(t\ge1\) to \(D^*_{t,a}\): use the latter if it is at most \(t\), otherwise independently resample from the geometric distribution conditioned to be at most \(t\). The actual lags have precisely the required truncated law; the chance of a mismatch for one edge is at most \(q^t\). A mismatch at birth \(t\) can affect only cuts indexed below \(t\). Hence, for counts formed from \(A_j\) and \(B_j\) over any initial interval,
\[
\sup_N\left|\sum_{j=0}^{N-1}(\mathbf1_{A_j}-\mathbf1_{B_j})\right|
\le\sum_{t\ge1}t\mathbf1_{\{\text{a mismatch at birth }t\}}.
\]
The right-hand side belongs to \(L^2\), since its \(L^2\)-norm is at most \(\sqrt m\sum_{t\ge1}tq^{t/2}<\infty\). Thus its contribution vanishes after division by \(\sqrt N\). The stationary mixing CLT transfers to \(K_N\).

**4. Exact fluctuation coefficient.** Summing the absolutely convergent stationary covariance series gives
\[
\begin{aligned}
v_m(q)&=\operatorname{Var}(\mathbf1_{B_0})
+2\sum_{d=1}^{\infty}\operatorname{Cov}(\mathbf1_{B_0},\mathbf1_{B_d})\\
&=\rho_m(q)(1-\rho_m(q))
+2\rho_m(q)\sum_{j=0}^{\infty}(b_j-\rho_m(q))\\
&=\rho_m(q)\bigl[1-\rho_m(q)+2\rho_m(q)S_m(q)\bigr].
\end{aligned}
\]
This is strictly positive because \(0<\rho_m(q)<1\) and \(S_m(q)>0\). The \(L^2\) coupling and the stationary covariance formula also yield \(\operatorname{Var}(K_N)/N\to v_m(q)\). Summing \(b_j=\rho_m(q)[1+(P_j^{-m}-1)]\) and bounding the geometric tail establishes the stated mean expansion.

**5. Sharp sign transition.** The exact comparison simplifies to
\[
\frac{v_m(q)}{\rho_m(q)}-1=\rho_m(q)\bigl(2S_m(q)-1\bigr).
\]
For each \(j\), \(P_j(q)^{-m}-1\) is continuous and strictly increasing in \(q\); locally uniform convergence of the series gives continuity and strict monotonicity of \(S_m\). As \(q\downarrow0\), \(S_m(q)\to0\). As \(q\uparrow1\), its first term diverges. Thus exactly one root of \(S_m(q)=1/2\) exists. At \(q=1/2\), \(P_0(q)\le1-q=1/2\), so the first summand is at least \(2^m-1>1/2\), and the root is below \(1/2\). Since each summand increases strictly with \(m\), \(q_m\) decreases strictly with \(m\).

**6. High-multiplicity asymptotic of the transition.** For \(q=O(m^{-1})\), with \(m q\) bounded,
\[
-\log P_0(q)=q+\tfrac32q^2+O(q^3),\qquad
-\log P_1(q)=q^2+O(q^3),
\]
and the sum of terms indexed \(j\ge2\) in \(S_m(q)\) is \(O(mq^3)\). Consequently if \(q=c/m+d/m^2\),
\[
S_m(q)=e^c-1+\frac{e^c(d+\frac32c^2)+c^2}{m}+O(m^{-2}).
\]
The unique critical equation first yields \(e^c=3/2\), and at the next order yields \(d=-(3/2+2/3)c^2=-13c^2/6\). The convergence of \(S_m(x/m)\) to \(e^x-1\) is uniform on compact positive \(x\)-intervals, and its derivative with respect to \(q\) is bounded below by a positive multiple of \(m\) near the root; therefore the error in the root is \(O(m^{-3})\), proving the expansion.

## Verification

The standalone `verify.py` (Python standard library only) checks finite-start cut probabilities and all pair probabilities by exhaustive enumeration of parent histories, checks exact stationary finite-window joint probabilities over multiple rational parameters and multiplicities, and certifies rational lower/upper bounds for the proposed under-/over-dispersion brackets. Run `python3 verify.py` from the folder containing this file. These finite calculations are neither used as proof of the stationary CLT nor as proof of the large-m expansion; both follow analytically from the arguments above.

## Relationship to prior work

Aguech, Mahmoud, Mohamed and Yang introduced exponentially preferential recursive trees and investigated vertex degree laws in the single-parent model. Tang, Wang and Wu introduced the multi-parent graph and established its terminal bottleneck renewal structure, recurrence and infinite collisions. The previously published manuscript *Poisson activation of terminal bottlenecks in weakly age-biased recursive trees* gives the exact one-cut probability and finite-window pair identity and proves a rare-bias Poisson point-process limit for fixed \(m\). All these constructions and pair probabilities are credited as existing inputs, not new discoveries.

The new conclusion is the **fixed-bias Gaussian count variance with a unique switch from under- to over-Poisson dispersion**, its exact parameter frontier and the second-order \(m\to\infty\) location of that frontier. A Poisson point-process limit as \(q\uparrow1\) with fixed \(m\) does not determine the sign of the fixed-parameter variance-to-mean difference, nor does a generic renewal CLT determine the model-specific frontier. The formulas can be reduced to known joint probabilities plus new infinite-series and uniform large-m analysis; an unindexed prior derivation remains a priority risk.

## Limitations

The observed count is a terminal infinite-horizon cut count, not an online estimator. The CLT does not cover simultaneously growing \(N\) and \(m\) or bias drifting with \(N\); the second-order frontier location is a separate limit. Only independent exponentially age-weighted parents and retained parallel edges are included. The novelty conclusion is based on a bounded literature comparison and is not a certification of global priority. No independent validation has been performed.

## References

1. R. Aguech, H. Mahmoud, H. Mohamed and Z. Yang, *Exponentially preferential trees*, Network Science **13** (2025), e5, DOI: 10.1017/nws.2025.3, https://doi.org/10.1017/nws.2025.3.
2. J. Tang, F. Wang and X.-Y. Wu, *Random Walk on age-preferential random growth processes*, arXiv:2611.02329, first posted 2026-11-02, https://arxiv.org/abs/2611.02329.
3. *Poisson activation of terminal bottlenecks in weakly age-biased recursive trees*, publicly accessible mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-poisson-activation-of-terminal-bottlenecks-in-weakly-age-biased--eec88f3506ed.
4. I. A. Ibragimov, *Some limit theorems for stationary processes*, Theory of Probability and Its Applications **7** (1962), 349–382, a classical stationary strong-mixing CLT; see also R. C. Bradley, *Introduction to Strong Mixing Conditions*, 2007.
