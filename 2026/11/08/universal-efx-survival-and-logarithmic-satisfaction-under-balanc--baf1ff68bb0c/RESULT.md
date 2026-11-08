# Universal EFX survival and logarithmic satisfaction under balanced exponential lotteries

## Finding
Fix integers \(n\ge 2\) and \(r\ge2\). Before any values are observed, assign \(nr\) distinct indivisible goods to \(n\) labeled agents in a fixed allocation \(A=(A_1,\dots,A_n)\), with \(|A_i|=r\) for every agent. For every agent–good pair, draw an independent \(\operatorname{Exp}(1)\) value and extend these values additively. The allocation is envy-free ex ante. It is *EFX* ex post when, for each distinct pair \(i,j\) and every \(g\in A_j\),
\[
 v_i(A_i)\ge v_i(A_j\setminus\{g\}).
\]

Let \(Z_{n,r}\) count the agents whose own EFX comparisons against *every* other agent succeed. Set \(k=r-1\), \(a=r/(r-1)\), and
\[
 Q_r(t)=\sum_{h=0}^{k-1}\frac{t^h}{h!}+\sum_{h=0}^{k-1}\frac{(-1)^h k^{h+1}t^{k-1-h}}{(k-1-h)!},\qquad c_r=(-1)^{k-1}k^k,
\]
\[
 F_r(t)=1-e^{-t}Q_r(t)+c_r e^{-at}\quad (t\ge0),\qquad
 p_{n,r}=\frac1{(r-1)!}\int_0^\infty t^{r-1}e^{-t}F_r(t)^{n-1}\,dt.
\]
Then \(F_r\) is a cumulative distribution function, \(p_{n,r}\) is a rational number, and the **exact law** is
\[
 \boxed{Z_{n,r}\sim\operatorname{Binomial}(n,p_{n,r}),\qquad
 \Pr(A\text{ is EFX})=p_{n,r}^{\,n}.}
\]
There is a finite rational formula without numerical integration. With \(N=n-1\), \(q_{i,\ell}=[t^\ell]Q_r(t)^i\) and \(q_{0,0}=1\),
\[
 p_{n,r}=\sum_{i=0}^{N}\sum_{j=0}^{N-i}
 \frac{N!(-1)^i c_r^j}{i!j!(N-i-j)!}
 \sum_{\ell=0}^{i(r-2)}q_{i,\ell}\,
 \frac{(r+\ell-1)!}{(r-1)!}
 \left(1+i+\frac{rj}{r-1}\right)^{-(r+\ell)}.
\]
For the natural first case, two goods per agent, this simplifies to
\[
 \boxed{p_{n,2}=\frac{H_{2n-1}}{2n-1},\quad H_m=\sum_{j=1}^{m}\frac1j.}
\]
In particular \(\Pr(A\text{ is EFX})=121/324\) when \(n=r=2\).

For **every fixed** \(r\ge2\), as \(n\to\infty\),
\[
 \boxed{p_{n,r}\sim\frac{\log n}{r(r-1)n},\qquad
 \Pr(A\text{ is EFX})^{1/n}\sim\frac{\log n}{r(r-1)n}.}
\]
Despite the rarity of global EFX,
\[
 \frac{Z_{n,r}}{\log n}\xrightarrow{\Pr}\frac1{r(r-1)},\qquad
 \frac{Z_{n,r}-np_{n,r}}{\sqrt{np_{n,r}(1-p_{n,r})}}\xrightarrow{d}N(0,1),
\]
with \(\Pr(Z_{n,r}=0)=n^{-1/[r(r-1)]+o(1)}\). This is an exact binomial law plus a sharp fixed-\(r\) asymptotic, not a claim about optimal adaptive allocations.

## Assumptions and scope
All \(nr\) goods are distinct and assigned before values are known; each agent gets exactly \(r\) goods. All \(n\cdot nr\) values are independent, identically distributed rate-one exponentials and hence strictly positive almost surely. Agents' utilities are additive. Each EFX test removes **any** positively valued good from the rival's bundle, not just a conveniently selected good. The allocation itself is nonrandom, but the probability is the same for every balanced allocation by exchangeability. The limits keep \(r\) fixed while \(n\) increases.

## Proof
**1. Independent EFX rows.** Fix agent \(i\). Her own-bundle value \(S_i=v_i(A_i)\) has the \(\operatorname{Gamma}(r,1)\) distribution. For a rival \(j\), the largest remaining value after deleting *one arbitrary good* from \(A_j\) is the sum \(T_{ij}\) of its \(r-1\) largest \(i\)-values. All \(T_{ij}\), \(j\ne i\), are independent and independent of \(S_i\), as they use disjoint agent–good entries. The row success event is \(\{S_i\ge\max_{j\ne i}T_{ij}\}\). Its probability is \(p_{n,r}=\mathbb E[F_r(S_i)^{n-1}]\) when \(F_r\) is the distribution function of one \(T_{ij}\). Different rows use different agents' independently sampled valuations; consequently their success indicators are independent Bernoulli variables of the same parameter. The binomial law and global EFX formula follow.

**2. Law of the deletion-resistant rival value.** For \(r\) independent rate-one exponentials, write their minimum as \(M\). By exponential memorylessness, \(M\sim\operatorname{Exp}(r)\), independently of the \(r-1\) surviving residuals \(E_1,\ldots,E_{r-1}\sim\operatorname{Exp}(1)\). Thus
\[
 T=(r-1)M+\sum_{h=1}^{r-1}E_h,
\]
where the two summands are independent and have \(\operatorname{Exp}(r/(r-1))\) and \(\operatorname{Gamma}(r-1,1)\) laws. Conditioning on the gamma summand gives
\[
 \Pr(T>t)=e^{-t}\sum_{h=0}^{r-2}\frac{t^h}{h!}+
 \frac{e^{-rt/(r-1)}}{(r-2)!}\int_0^t e^{u/(r-1)}u^{r-2}\,du.
\]
Integration by parts \(r-1\) times evaluates this expression as \(e^{-t}Q_r(t)-c_r e^{-rt/(r-1)}\). Hence the displayed \(F_r\) is exactly the distribution function of \(T\). Integrating against the gamma density proves the integral formula for \(p_{n,r}\). Expanding \((1-e^{-t}Q_r(t)+c_r e^{-at})^N\) by the multinomial theorem and using \(\int_0^\infty t^{s-1}e^{-bt}\,dt=(s-1)!/b^s\) for positive integer \(s\) proves the finite rational formula.

For \(r=2\), \(T\) is simply the maximum of two exponentials, so \(F_2(t)=(1-e^{-t})^2\). Substitution \(u=e^{-t}\) gives
\[
 p_{n,2}=\int_0^1(-\log u)(1-u)^{2n-2}\,du=\frac{H_{2n-1}}{2n-1},
\]
by differentiating the beta integral or integrating its standard series.

**3. Fixed-bundle-size asymptotics.** The tail from Step 2 obeys, for each fixed \(r\),
\[
 \Pr(T>t)\sim b_r t^{r-2}e^{-t},\qquad b_r=\frac{r}{(r-2)!},\qquad t\to\infty.
\]
Indeed, the highest coefficient of \(Q_r\) is \(r/(r-2)!\), while the second exponential decays faster. Put \(N=n-1\) and \(u_N=\log N+(r-2)\log\log N+\log b_r\). For every fixed \(z\in\mathbb R\), \(N\Pr(T>u_N+z)\to e^{-z}\) and hence \(F_r(u_N+z)^N\to\exp(-e^{-z})\). With the change of variable \(t=u_N+z\), the gamma integral divided by \(u_N^{r-1}e^{-u_N}/(r-1)!\) converges to
\[
 \int_{-\infty}^{\infty}e^{-z}\exp(-e^{-z})\,dz=1.
\]
For completeness, this passage is justified by splitting \(t\) into \([0,u_N/2]\), \([u_N/2,u_N]\), and \([u_N,\infty)\). The first part is exponentially negligible since \(F_r(u_N/2)^N\le \exp(-N\Pr(T>u_N/2))\) with \(N\Pr(T>u_N/2)\to\infty\) at least on a positive power scale. On the middle part, the tail lower bound \(\Pr(T>t)\ge c t^{r-2}e^{-t}\) gives an integrable majorant \(e^{-z}\exp(-c' e^{-z})\) for \(z\le0\). On the last part, \(e^{-z}(1+z)^{r-1}\) dominates for \(z\ge0\). Therefore
\[
 p_{n,r}\sim\frac{u_N^{r-1}e^{-u_N}}{(r-1)!}
 \sim\frac{\log n}{r(r-1)n}.
\]
Finally the row indicators are binomial; \(np_{n,r}\sim\log n/[r(r-1)]\to\infty\) and \(p_{n,r}\to0\). Binomial variance, Chebyshev's inequality, the binomial central limit theorem, and \(n\log(1-p_{n,r})\sim-np_{n,r}\) give the remaining assertions.

## Verification
The standalone `check_efx_survival.py` independently integrates the hypoexponential cumulative distribution function numerically, compares it against the finite **exact rational** expansion for \(2\le r\le5\) and \(2\le n\le6\), checks the harmonic identity for all tested \(r=2\) cases, and compares five cases with directly sampled agent–good valuations. Run `python check_efx_survival.py` in an environment with Python 3 and SciPy. These checks test finite identities and implementation; the general asymptotic follows from the analytic bounds in Step 3 rather than simulation.

## Relationship to prior work
Neoh and Teh, *Online Fair Division with Frequency Predictions* (2026), study worst-case online EFX and EF1 under predictions of future values, whereas the current probability model fixes a balanced allocation before independent random utility realizations. Igarashi and Oh, *Fair Division of Lotteries* (2026), analyze ex-post **exact envy-freeness** under uncertain item values; their results do not evaluate the stronger EFX deletion comparisons or this binomial count. Cohen, Teh and Wooldridge (2026) and Chen and Long (2026) establish adversarial online EFX success limitations with randomness in the allocation algorithm rather than independent exogenous valuations after a fixed allocation. Earlier exact calculations for EF1 under balanced exponential lotteries use the **sum of the smallest** \(r-1\) rival values; here EFX uses the **largest** \(r-1\), with a qualitatively different asymptotic exponent. These distinctions are mathematical non-implications, not proofs of global novelty.

## Limitations
The theorem describes a fixed balanced allocation and independent rate-one exponential valuations. It does not characterize optimized allocations, dependent or heterogeneous valuations, shared realized item values, variable bundle sizes, or any regime with \(r\) growing with \(n\). The exact binomial law relies on independence between agents' entire valuation rows. No independent scientific audit has been performed; related unindexed results might exist.

## References
- T. Y. Neoh and N. Teh, *Online Fair Division with Frequency Predictions*, arXiv:2610.34625, first posted 2026-10-25, https://arxiv.org/abs/2610.34625.
- A. Igarashi and Y. Oh, *Fair Division of Lotteries*, arXiv:2610.34906, first posted 2026-10-26, https://arxiv.org/abs/2610.34906.
- S. Cohen, N. Teh and M. Wooldridge, *Online Fair Division Against an Oblivious Adversary*, arXiv:2609.28333, first posted 2026-09-23, https://arxiv.org/abs/2609.28333.
- T. Chen and J. Long, *Randomized Online Fair Division: High-Probability and Expected Realized Fairness*, arXiv:2609.23577, first posted 2026-09-20, https://arxiv.org/abs/2609.23577.
- B. Plaut and T. Roughgarden, *Almost Envy-Freeness with General Valuations*, arXiv:1707.04769, 2017, https://arxiv.org/abs/1707.04769.
