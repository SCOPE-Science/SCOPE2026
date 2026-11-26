# Joint support and nonoverlined gaps in regular overpartitions: a diagonal law and sharp coincidence bias

## Finding
Fix an integer \(\ell\ge2\). For a uniformly sampled \(\ell\)-regular overpartition of \(n\), define \(X_n\) as the least positive integer not divisible by \(\ell\) that occurs **no time as a nonoverlined part**, and \(Y_n\) as the least such integer that occurs **neither overlined nor nonoverlined**. Thus \(X_n\le Y_n\). Write
\[
\rho=1-\frac1\ell,\qquad \kappa=\frac{\pi\rho^{3/2}}4.
\]
Then for all fixed real \(x,y\ge0\),
\[
\lim_{n\to\infty}\Pr(X_n>xn^{1/4},\ Y_n>yn^{1/4})
=\exp\!\left(-\kappa x^2-\frac\kappa2(y^2-x^2)_+\right).
\tag{1}
\]
The limiting joint law gives mass \(1/2\) to the diagonal; its diagonal measure is \(\kappa x e^{-\kappa x^2}\,dx\) at \((x,x)\). On \(0<x<y\) it has joint density \(\kappa^2xy e^{-\kappa(x^2+y^2)/2}\,dx\,dy\), with total mass \(1/2\), and has no mass below the diagonal. In addition, the actual integer-valued gaps satisfy the sharper **exact-coincidence asymptotic**
\[
\boxed{\Pr(X_n=Y_n)=\frac12+\frac{\pi}{8\rho^{1/4}}n^{-1/4}+o_\ell(n^{-1/4}).}\tag{2}
\]
The correction in (2) cannot be inferred from weak convergence in (1).

For exact finite counts let \(P_\ell(q)=\prod_{j\ge1,\,\ell\nmid j}(1+q^j)/(1-q^j)\), \(S_\ell(m)=\sum_{1\le j\le m,\,\ell\nmid j}j\), and \(\bar p_\ell(n)=[q^n]P_\ell(q)\), with zero values for negative indices. For integers \(a,b\ge0\), the number of \(\ell\)-regular overpartitions of \(n\) with \(X_n>a,Y_n>b\) is
\[
[q^n]P_\ell(q)q^{S_\ell(a)}
\prod_{\substack{a<j\le b\\\ell\nmid j}}\frac{2q^j}{1+q^j}.
\tag{3}
\]
The exact coincidence count is
\[
[q^n]P_\ell(q)\sum_{\substack{j\ge1\\\ell\nmid j}}
q^{S_\ell(j-1)}\frac{1-q^j}{1+q^j}.
\tag{4}
\]
All series in (3)–(4) are interpreted coefficientwise: for each coefficient only finitely many terms contribute.

## Assumptions and scope
An overpartition of \(n\) is a partition in which each distinct part size has an independent option to overline its first occurrence. An \(\ell\)-regular overpartition forbids part sizes divisible by \(\ell\). Every such overpartition of \(n\) is equally likely. Only fixed \(\ell\ge2\) and \(n\to\infty\) are considered. Both gap definitions require admissibility \(\ell\nmid j\). The exact identities hold also at \(n=0\).

## Proof
**1. Exact combinatorial decomposition.** At any admissible size \(j\), the nonoverlined multiplicity \(G_j\) is any nonnegative integer and the overline marker \(B_j\) is zero or one. The unrestricted generating factor is \((1+q^j)/(1-q^j)\). Requiring \(G_j\ge1\) multiplies this factor by \(q^j\); requiring \(G_j+B_j\ge1\) multiplies it by \(2q^j/(1+q^j)\). Applying these conditions for \(j\le a\) and for \(a<j\le b\), respectively, proves (3). The event \(X_n=Y_n=j\) requires nonoverlined copies at each earlier admissible size and no occurrence of \(j\) at all; hence its generating factor is \(q^{S_\ell(j-1)}(1-q^j)/(1+q^j)\). Sum over \(j\) to prove (4). An equivalent integer algorithm is
\[
\sum_{\ell\nmid j\ge1}\left[\bar p_\ell(n-S_\ell(j-1))
+2\sum_{k\ge1}(-1)^k\bar p_\ell(n-S_\ell(j-1)-kj)\right].
\tag{5}
\]

**2. Boltzmann measure and leading saddle.** Put \(q=e^{-t}\). Normalize all overpartitions of every weight by \(P_\ell(q)\). In this measure each admissible \(G_j\) is geometric with \(\Pr(G_j=k)=(1-q^j)q^{jk}\), independent of \(B_j\), with \(\Pr(B_j=1)=q^j/(1+q^j)\). All these random variables are mutually independent. The random total weight is \(N_t=\sum_j j(G_j+B_j)\). From the Euler product and its logarithmic derivative,
\[
\log P_\ell(e^{-t})=\frac{\pi^2\rho}{4t}+O_\ell(\log(1/t)),\quad
\mathbb E N_t=\frac{\pi^2\rho}{4t^2}+O_\ell(t^{-1}),\quad
\operatorname{Var}(N_t)=\frac{\pi^2\rho}{2t^3}+O_\ell(t^{-2}).
\tag{6}
\]
The admissible-part density \(\rho\) gives \(S_\ell(m)=\rho m^2/2+O_\ell(m)\). The unique positive saddle \(t_n\) with \(\mathbb E N_{t_n}=n\) consequently satisfies
\[
t_n=\frac\pi2\sqrt{\rho/n}+O_\ell(n^{-1}).\tag{7}
\]

**3. Conditioning estimate at the \(n^{1/4}\) scale.** We record the particular coefficient/conditioning estimate needed here, including its precision. Under the Boltzmann model at \(t_n\), let \(E_j=\{X=j,Y=j\}\). For any fixed sufficiently large \(C>0\), uniformly over admissible \(j\le L_t=t^{-1/2}\sqrt{C\log(1/t)}\),
\[
\frac{\Pr_{t_n}(N_t=n\mid E_j)}{\Pr_{t_n}(N_t=n)}
=1+O_{\ell,C}(t\log^2(1/t)).\tag{8}
\]
Here is a Fourier proof of (8). Conditioning on \(E_j\) adds one copy of every earlier admissible size by geometric memorylessness and deletes both variables at size \(j\). The resulting total has distribution \(S_\ell(j-1)+N_t-j(G_j+B_j)\), with independent variables remaining. Its mean differs from \(n\) by \(O_{\ell,C}(t^{-1}\log(1/t))\) and its variance differs from the unconditioned variance by \(O(t^{-2})\). The latter two bounds use \(\mathbb E[j(G_j+B_j)]=O(t^{-1})\) and \(\operatorname{Var}(j(G_j+B_j))=O(t^{-2})\), uniformly in the deleted size.

For both totals the logarithmic characteristic-function derivatives of orders \(k=2,3,4\) are \(O_k(t^{-k-1})\). In fact, expanding each geometric or Bernoulli logarithm bounds the absolute sums of derivatives by constant multiples of \(\sum_{r\ge1}r^{k-1}\sum_{m\ge1}m^k e^{-tmr}=O_k(t^{-k-1})\); the inner sum is bounded by \(O_k((tr)^{-k-1})\) for all \(tr>0\). Write \(\theta=t^{3/2}z\) in Fourier inversion on \(|z|\le\sqrt{D\log(1/t)}\), with \(D\) fixed large. With \(v_0=t^3\operatorname{Var}(N_t)\asymp1\), the centered exponent for the conditioned total is
\[
-v_0 z^2/2+i(\delta z+\gamma z^3)+O(tz^2+tz^4),
\qquad \delta=O_{\ell,C}(\sqrt t\log(1/t)),\quad \gamma=O(\sqrt t).
\]
The term linear in the imaginary odd polynomial integrates to zero on the symmetric arc. Bounding its squared error by \(O((\delta z+\gamma z^3)^2)\) and integrating all error terms against the Gaussian gives relative error \(O_{\ell,C}(t\log^2(1/t))\). The same bound applies to the unconditioned integral, where \(\delta=0\) and the quadratic coefficient is exactly \(-v_0/2\).

For the complementary arcs, retain just the geometric factors with \(1/t\le m\le 2/t\) and \(m\equiv1\pmod\ell\); none is affected by conditioning. The product modulus is at most \(\exp(-c\sum_m\sin^2(m\theta/2))\) for an absolute \(c>0\), since \(e^{-tm}\) is bounded away from 0 and 1. For \(|\theta|\le\varepsilon t\) (fixed small \(\varepsilon>0\)) the sum is bounded below by \(c_\ell t^{-3}\theta^2\). Outside fixed-width \(Kt\) neighborhoods of \(2\pi k/\ell\), the geometric sum of \(e^{im\theta}\) has modulus at most \(2/|1-e^{i\ell\theta}|\), which is at most half the number of terms for fixed sufficiently large \(K\). In a neighborhood write \(\theta=2\pi k/\ell+tv\). Uniformly for bounded \(v\), the sine-square sum times \(t\) converges to \(\ell^{-1}\int_1^2\sin^2((2\pi k/\ell+vx)/2)\,dx\). This integral is positive except at \(v=0\) and \(k\equiv0\pmod\ell\), already handled by the small-\(|\theta|\) bound. Thus the complementary integral is \(O(t^A)\) for any required fixed \(A\) by choosing \(D\) sufficiently large. Combining the arcs proves (8).

The bound in (8) also holds for the shift-only conditioning on \(X>L_t\), whose shift is \(S_\ell(\lfloor L_t\rfloor)\). For the joint-tail events in Step 4, the nonoverlined-copy restrictions add deterministic shifts. An at-least-one-occurrence restriction at a size \(m\) multiplies its generating factor by \(2q^m/(1+q^m)\), so the change in order-\(k\) log-characteristic derivatives on the central arc is \(O_k(m^k)\); the normalization at \(\theta=0\) is constant. The total mean change is \(O(t^{-1})\); changes in the variance and higher derivatives are no larger than those needed for the same central estimates (for example the variance change is \(O(t^{-3/2})\)). The large-size block is again unchanged. This gives a relative \(1+o(1)\) conditioning estimate for the joint-tail events.

**4. Joint limit.** With integers \(a=\lfloor xn^{1/4}\rfloor\), \(b=\lfloor yn^{1/4}\rfloor\), the Boltzmann probability corresponding to (3) is
\[
\exp(-tS_\ell(a))\prod_{\substack{a<j\le b\\\ell\nmid j}}\frac{2e^{-tj}}{1+e^{-tj}}.
\]
For \(a,b=O(n^{1/4})\), \(\log(2e^{-u}/(1+e^{-u}))=-u/2+O(u^2)\), and the total quadratic error is \(O(t^{1/2})\). From (7), this tends to (1), since \(t_n S_\ell(a)\to\kappa x^2\) and \(t_n(S_\ell(b)-S_\ell(a))\to\kappa(y^2-x^2)\) when \(b>a\). The last conditioning assertion in Step 3 passes the Boltzmann joint probability to the fixed-weight uniform measure. The limiting joint survival determines a continuous-cdf law. Differentiating its interior distribution and taking the jump across the diagonal gives the stated densities. The diagonal density integrates to \(1/2\), and the off-diagonal density integrates to \(1/2\).

**5. Sharp probability of exact coincidence.** Under Boltzmann weighting, \(\Pr_t(X>m)=e^{-tS_\ell(m)}\). Conditioned on \(X=j\), the independent overline bit at \(j\) remains Bernoulli with success probability \(e^{-tj}/(1+e^{-tj})\). Therefore \(\Pr_t(X=Y\mid X=j)=1/(1+e^{-tj})\), and the exact identity
\[
\Pr_t(X=Y)-\frac12=\frac12\,\mathbb E_t\tanh(tX/2)
\tag{9}
\]
holds. Tail summation with \(S_\ell(m)=\rho m^2/2+O_\ell(m)\) gives, as \(t\downarrow0\),
\[
\mathbb E_t X=\sqrt{\frac\pi{2\rho t}}+O_\ell(1),\qquad
\mathbb E_t X^3=O_\ell(t^{-3/2}).\tag{10}
\]
In (9), use \(\tanh u=u+O(u^3)\) (uniformly for nonnegative \(u\)); hence
\[
\Pr_t(X=Y)=\frac12+\frac14\sqrt{\frac\pi{2\rho}}\sqrt t+O_\ell(t).\tag{11}
\]
To transfer the first correction to fixed weight, truncate the coincidence events \(E_j\) at the \(L_t\) from Step 3. Since \(E_j\subseteq\{X=j\}\), the omitted Boltzmann probability is at most \(\Pr_t(X>L_t)=e^{-tS_\ell(L_t)}=O(t^2)\) for large \(C\). The fixed-weight tail is the exact ratio \(\bar p_\ell(n-S_\ell(L_t))/\bar p_\ell(n)\), which is also \(O(t^2)\) by the same local saddlepoint estimate (or the standard eta-quotient coefficient estimate), because \(S_\ell(L_t)=O(t^{-1}\log(1/t))\). Applying (8) term by term gives
\[
\Pr_n(X_n=Y_n)=\Pr_{t_n}(X=Y)+O_\ell(t_n\log^2(1/t_n))
=\Pr_{t_n}(X=Y)+o_\ell(\sqrt{t_n}).\tag{12}
\]
Substituting (7) into (11) proves (2), since the coefficient simplifies to \(\pi/(8\rho^{1/4})\).

## Verification
The accompanying standard-library script `verify.py` enumerates all admissible overpartitions for \(0\le n\le12\) and \(2\le\ell\le6\), compares exact joint-tail probabilities with the independent Euler-product calculation, and validates the coincidence sum (5). It performs 520 exact checks and reports finite-value trends up to \(n=500\). The exact generating identities are proved combinatorially; the infinite asymptotics require Steps 2–5 and are not certified by finite tests. Run `python3 verify.py`.

## Relationship to prior work
Bhowmick and Meher [1] define the \(\ell\)-regular nonoverlined gap and investigate its aggregate generating series, parity and asymptotic sums. Donato [2] studies individual overpartition mex conventions including full-support absence. Aricheta and Donato [3] address the marginal nonoverlined version. Reference [4] proves a joint running-minimum law and a coincidence limit for thresholds on **nonoverlined multiplicities** in unrestricted overpartitions; full-support absence depends on the overline bit as well. References [5,7] give joint and sharp coincidence results for multiplicity gaps in unmarked \(\ell\)-regular partitions. In particular, [7] has an analogous positive \(n^{-1/4}\) correction, but its local marks encode multiplicity classes in unmarked partitions rather than the presence of an independent overline bit. Reference [6] treats odd versus even disjoint nonoverlined groups, not the nested gaps here. The contribution is the coupled singular limit and first fixed-weight coincidence correction for the marked pair. These comparisons do not establish universal priority.

## Limitations
The modulus \(\ell\) is fixed; no uniformity for \(\ell\) growing with \(n\) is asserted. The \(o_\ell(n^{-1/4})\) remainder is not made effective, and no higher-order corrections or joint local limit at individual lattice points are claimed. The Fourier conditioning argument is analytic, not a machine-certified proof. A yet-unindexed paper treating this precise coupled statistic could cover the result.

## References
[1] S. Bhowmick and N. K. Meher, *The minimal excludant of \(\ell\)-regular overpartitions*, arXiv:2611.18129v1 (submitted 13 Nov 2026), https://arxiv.org/html/2611.18129v1.

[2] J. A. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402v1 (submitted 6 Jul 2025), https://arxiv.org/html/2507.04402v1.

[3] V. M. R. Aricheta and J. A. L. Donato, *Minimal Excludant over Overpartitions*, arXiv:2309.04398 (2023), https://arxiv.org/abs/2309.04398.

[4] *Joint Rayleigh running-minimum law and universal coincidence probabilities for overpartition least gaps*, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-joint-rayleigh-running-minimum-law-and-universal-coincidence-pro--e1bdf9b70b4a/RESULT.md.

[5] *Joint least-multiplicity-gap laws for regular partitions*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-joint-least-multiplicity-gap-laws-for-regular-partitions--a7d5664f9d36/RESULT.md.

[6] *Sharp residual dependence of odd and even nonoverlined gaps in overpartitions*, https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-sharp-residual-dependence-of-odd-and-even-nonoverlined-gaps-in-o--4e2f726ecdf2/RESULT.md.

[7] *The first finite-size multiplicity-mark bias at a least gap of regular partitions*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-the-first-finite-size-multiplicity-mark-bias-at-a-least-gap-of-r--11f1f81a8477/RESULT.md.
