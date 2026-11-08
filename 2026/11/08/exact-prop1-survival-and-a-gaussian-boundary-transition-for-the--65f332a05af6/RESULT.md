# Exact PROP1 survival and a Gaussian boundary transition for the two-agent Like rule

## Finding

For two agents who independently value each arriving good at either zero or one, the classical Like rule has an exact finite-horizon probability of producing an allocation proportional up to one good (PROP1). The law yields a discontinuous limiting phase diagram and a sharp Gaussian boundary window.

Let there be \(m\ge1\) goods. Agent \(i\) approves each good independently with probability \(p_i\in[0,1]\), independently across agents and goods. Let \(F_m(p_1,p_2)\) be the probability that both agents satisfy PROP1 after each good is given uniformly to an approving agent, when there is one. Put
\[
a=\frac{p_1p_2}{2},\qquad b_i=p_i\left(1-\frac{p_{3-i}}2\right),\qquad c_i=1-p_i,\qquad L_i(z)=az+b_i z^{-1}+c_i.\]
Then, for every admissible parameter pair and every finite horizon,
\[
\boxed{F_m(p_1,p_2)=1-\sum_{i=1}^{2}\sum_{k=3}^{m}[z^k]L_i(z)^m.}
\]
Here \([z^k]\) means the indicated Laurent coefficient, and an empty sum is zero.

For fixed \(0<p_1,p_2<1\), define
\[
\theta_i=\tfrac12\log(b_i/a),\quad
\rho_i=c_i+2\sqrt{a b_i},\quad
\sigma_i^2=\frac{2\sqrt{a b_i}}{\rho_i},\quad
K_i=\frac{e^{-3\theta_i}}{(1-e^{-\theta_i})\sqrt{2\pi\sigma_i^2}}.
\]
All quantities are well defined, \(\theta_i>0\), \(0<\rho_i<1\), and \(K_i>0\). The exact sharp large-horizon failure law is
\[
\boxed{1-F_m(p_1,p_2)\sim\frac{K_1\rho_1^m+K_2\rho_2^m}{\sqrt m}.}
\]
Consequently, the joint PROP1 probability tends to one exponentially fast in the interior of the parameter square, but at its upper boundary:
\[
\lim_{m\to\infty}F_m(p_1,p_2)=
\begin{cases}
1,&0<p_1,p_2<1,\\
\tfrac12,&\text{exactly one of }p_1,p_2\text{ equals }1\text{ and the other is in }(0,1),\\
0,&p_1=p_2=1.
\end{cases}
\]
If either parameter is zero, \(F_m=1\) for every horizon.

The full transition scale is explicit. If \(p_{i,m}\in[0,1]\) satisfies
\[
p_{i,m}=1-\frac{d_i}{\sqrt m}+o(m^{-1/2}),\qquad d_i\in[0,\infty),
\]
then with \(\Phi\) the standard normal cumulative distribution function,
\[
\boxed{\lim_{m\to\infty}F_m(p_{1,m},p_{2,m})=\Phi(d_1)+\Phi(d_2)-1.}
\]
In particular, the symmetric critical window \(p_{1,m}=p_{2,m}=1-d/\sqrt m\) has limit \(2\Phi(d)-1\). Both agents liking every good is a singular boundary: at \(p_1=p_2=1\), the exact finite-horizon value is
\[
F_m(1,1)=2^{-m}\begin{cases}
\binom{m}{m/2-1}+\binom{m}{m/2}+\binom{m}{m/2+1},&m\text{ even},\\
2\binom{m}{(m-1)/2},&m\text{ odd},
\end{cases}
\]
and hence is asymptotic to \(3\sqrt{2/(\pi m)}\) along even horizons and \(2\sqrt{2/(\pi m)}\) along odd horizons.

## Assumptions and scope

The two agents have additive binary utilities. Each item-agent value is an independent Bernoulli variable with the specified agent-specific probability, constant across the horizon. Each arrival is assigned immediately and irrevocably. The Like rule independently tosses a fair coin when both agents approve the current good, gives an exclusively approved good to its approving agent, and may allocate a doubly disapproved good arbitrarily. The last convention is harmless because neither agent values that good.

For the final bundles \(A_1,A_2\), PROP1 means, for each \(i\in\{1,2\}\),
\[
v_i(A_i)+\max_{g\notin A_i}v_i(g)\ge\frac{v_i(G)}2,
\]
where the maximum over an empty set is zero. Probabilities include both the random valuations and the Like coin tosses. The asymptotic constants above assume interior fixed parameters; they are not claimed to be uniform at the boundary.

## Proof

**1. Exact fairness reduction.** Write \(T_i=v_i(G)\), \(U_i=v_i(A_i)\), and \(D_i=T_i-2U_i\). When an outside good is positively valued, PROP1 is exactly \(D_i\le2\). When no outside good is positively valued, \(T_i=U_i\), so \(D_i=-T_i\le0\) and PROP1 holds. Thus PROP1 is equivalent to \(D_i\le2\) in all cases.

Let \(E_i\) count goods approved only by agent \(i\). Let \(W\) be the number of jointly approved goods sent to agent 2 minus the number sent to agent 1. Since a singly approved good goes to its sole approver,
\[
D_1=W-E_1,\qquad D_2=-W-E_2,\qquad D_1+D_2=-E_1-E_2\le0.
\]
In particular, the two violation events \(\{D_i\ge3\}\) cannot occur simultaneously. This disjointness is why the finite-horizon law is a sum of two univariate tails rather than an independence approximation.

**2. Single-item probability and exact law.** For fixed \(i\), a single item contributes \(+1\) to \(D_i\) only if both agents approve and the other receives it, of probability \(a=p_1p_2/2\). It contributes \(-1\) if the item is approved only by \(i\) or by both and assigned to \(i\), with probability \(b_i=p_i(1-p_{3-i}/2)\). Otherwise the increment is zero, with probability \(c_i=1-p_i\). Increments are independent across goods, so \(\Pr(D_i=k)=[z^k]L_i(z)^m\). Summing the two disjoint tails proves the exact formula.

**3. Sharp interior asymptotics.** Fix \(0<p_1,p_2<1\). Since \(b_i-a=p_i(1-p_{3-i})>0\), the increment has negative mean, and its moment-generating polynomial \(c_i+ae^t+b_ie^{-t}\) is minimized at \(\theta_i=\frac12\log(b_i/a)>0\) with minimum \(\rho_i=c_i+2\sqrt{ab_i}<1\). Under the exponentially tilted probability measure, the step law assigns probabilities \(\sqrt{ab_i}/\rho_i\) to each of \(+1\) and \(-1\), and \(c_i/\rho_i\) to zero. It is centered, aperiodic (since \(c_i>0\)), and has variance \(\sigma_i^2\). For any integer \(k\), exponential change of measure gives
\[
\Pr(D_i=k)=\rho_i^m e^{-\theta_i k}\Pr_*(D_i=k).
\]
The lattice local central limit theorem gives \(\Pr_*(D_i=k)\sim(2\pi m\sigma_i^2)^{-1/2}\) for each fixed \(k\), and its uniform point-mass bound is \(O(m^{-1/2})\). Dominated convergence for the geometrically weighted sum over \(k\ge3\) therefore yields
\[
\Pr(D_i\ge3)\sim\frac{\rho_i^m}{\sqrt{2\pi m\sigma_i^2}}\sum_{k=3}^{\infty}e^{-\theta_i k}
=K_i\rho_i^m m^{-1/2}.
\]
Adding the two disjoint events gives the stated sharp failure law.

**4. Boundary limits.** In the interior, the strong law for bounded independent increments, or the preceding asymptotic, gives \(F_m\to1\). If \(p_1=1\) and \(0<p_2<1\), then \(D_1\) has strictly negative drift, so its upper-tail failure probability tends to zero. The increments of \(D_2\) are symmetric, with \(\pm1\) each having probability \(p_2/2\) and zero having probability \(1-p_2\). The central limit theorem and vanishing atom mass imply \(\Pr(D_2\ge3)\to1/2\). The other asymmetric case follows by relabeling. When both parameters equal one, all goods are jointly approved and the count received by agent 1 is \(\operatorname{Bin}(m,1/2)\). The two PROP1 inequalities say that the difference in allocated bundle sizes has absolute value at most two, giving the displayed exact binomial expression and parity-dependent asymptotics by Stirling's formula. If one approval probability is zero, every positively valued good goes to its sole approver and PROP1 holds surely.

**5. Critical Gaussian window.** Under the stated sequence of parameters, \(E_1/\sqrt m\to d_2\) and \(E_2/\sqrt m\to d_1\) in probability: their expectations have those limits and their variances divided by \(m\) vanish. The independently randomized jointly approved goods contribute centered \(\pm1\) steps to \(W\) while all other goods contribute zero. Their variance per good is \(p_{1,m}p_{2,m}\to1\), so a bounded triangular-array central limit theorem gives \(W/\sqrt m\Rightarrow Z\sim N(0,1)\). The joint PROP1 event is precisely
\[
-E_2-2\le W\le E_1+2.
\]
Slutsky's theorem and continuity of the normal law give \(\Pr(-d_1\le Z\le d_2)=\Phi(d_2)-\Phi(-d_1)=\Phi(d_1)+\Phi(d_2)-1\), as claimed.

## Verification

The included standard-library Python file `verify.py` evaluates the two trinomial marginal tails using exact rational arithmetic, and independently enumerates all five valuation-and-recipient outcomes per item. It compares their PROP1 verdicts for six rational parameter pairs and horizons \(1\) through \(6\). It additionally checks the all-liked binomial formula for horizons through \(34\), parameter symmetry, and two small-horizon identities, for a total of \(106\) assertions. Running `python verify.py` gives `PASS` and the exact examples \(F_5(1/2,1/2)=4047/4096\), \(F_6(1/3,2/3)=524998/531441\), and \(F_5(1,1)=5/8\). These checks do not substitute for the infinite-horizon local limit and central limit arguments above.

## Relationship to prior work

Aleksandrov, Aziz, Gaspers and Walsh (2015) introduced the Like mechanism and showed it is ex-ante envy-free but can exhibit unbounded realized envy with binary utilities. Neoh and Teh (first public preprint September 4, 2026) established optimal worst-case *order* of high-probability PROP1 approximation by Like on arbitrary fixed inputs. Choo et al. (2025) analyze PROP1 for online rules, principally uniform allocation and prediction-assisted methods; Chen and Long (2026) analyze randomized online high-probability and expected approximation guarantees.

Those results do not, in the inspected material, give the exact joint success probability under independent Bernoulli approval profiles, the parameter-boundary trichotomy, the explicit interior exponential prefactor, or its Gaussian transition window. The new theorem is a special *input distribution* analysis, not a strengthening of the worst-case algorithmic guarantee. Standard local limit and Cramér tilting tools are used as known mathematical ingredients, not claimed as new.

## Limitations

The model assumes two agents, additive binary values, independent identical laws across goods, independence across agents, truthful approvals, and independent fair tie-breaking by Like. It does not assert a comparable phase transition for three or more agents, arbitrary correlated goods, nonbinary preferences, adversarially selected profiles, or balanced-Like. The sharp interior asymptotic requires parameters strictly between zero and one; at a boundary it is replaced by separate results. Literature-index and text searches cannot establish absolute publication novelty; unindexed or inaccessible related work remains a priority risk. The proof and finite checks are not independent external validation.

## References

1. M. Aleksandrov, H. Aziz, S. Gaspers and T. Walsh, *Online Fair Division: Analysing a Food Bank Problem* (IJCAI 2015), https://ijcai.org/proceedings/2015/360 ; first preprint https://arxiv.org/abs/1502.07571 .
2. T. Y. Neoh and N. Teh, *Closing Gaps in Online Fair Division* (first posted 2026-09-04), https://arxiv.org/abs/2609.05310 , especially Section 5 and the conclusion.
3. D. Choo, W. Fu, D. Khu, T. Y. Neoh, T.-Y. Poon and N. Teh, *Approximate Proportionality in Online Fair Division* (2025), https://arxiv.org/abs/2508.03253 .
4. T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness* (first posted 2026-09-20), https://arxiv.org/abs/2609.23577 .
