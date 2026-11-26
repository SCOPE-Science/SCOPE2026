# Weighted clumsy coupons: exact delay transform and a two-speed critical law

## Finding

Consider a coupon collector with two fixed sampling speeds. At each discrete step, independently of previous steps, a type is drawn and its status is replaced by an independent mark: absent with probability \(p_m=c/m\), present otherwise. Initially all types are absent. Let \(C_m\) be the first time all types have been drawn (ignoring marks), \(T_m\) the first time all are present, and \(D_m=T_m-C_m\).

Fix \(c>0\), \(0<\theta<1\), and \(0<a<b\) with \(\theta a+(1-\theta)b=1\). The two group sizes are \(m_1=\lfloor\theta m\rfloor\) and \(m_2=m-m_1\). Each type in the first or second group is selected with probability \(a/(m\bar w_m)\) or \(b/(m\bar w_m)\), respectively, where \(\bar w_m=(m_1a+m_2b)/m\). Take \(m\) large enough that \(0<p_m<1\) and both groups are nonempty.

Then
\[
\left(\frac{C_m}{m}-\frac{\log m}{a},\frac{D_m}{m}\right)
\ \,\Longrightarrow\ \left(\frac{G+\log\theta}{a},\tau\right),
\qquad
\frac{T_m}{m}-\frac{\log m}{a}\Longrightarrow \frac{G+\log\theta}{a}+\tau,
\]
where \(G\) is standard Gumbel and independent of \(\tau\). The variable \(\tau\) is the first simultaneous zero time for two independent stationary immigration–death coordinates. Their immigration rates are \(aC_1\), \(bC_2\), their death rates at population \(j\) are \(aj\), \(bj\), and their stationary means are \(C_1=\theta c\), \(C_2=(1-\theta)c\). In particular the coordinates start from independent \(\mathrm{Poisson}(C_i)\) variables, not from zero. For \(s>0\),
\[
\mathbb E e^{-s\tau}=\left[s\sum_{j,k\ge0}\frac{C_1^j C_2^k}{j!k!(s+aj+bk)}\right]^{-1},\qquad
\Pr(\tau=0)=e^{-c},
\]
and
\[
\frac{\mathbb ED_m}{m}\longrightarrow\mathbb E\tau
=\sum_{j+k\ge1}\frac{C_1^jC_2^k}{j!k!(aj+bk)}
>\sum_{h\ge1}\frac{c^h}{h!h}.
\]
The last series is the stationary critical delay mean when both sampling speeds are one at the same \(c\). The strict comparison is between post-cover delays, not between centered Gumbel locations.

## Assumptions and scope

The claim is the two-speed critical limit and its delay mean comparison. It concerns a fixed positive mass of each speed and per-draw replacement of just the chosen type. It does not assert a limit for vanishing class fractions, rates approaching each other as \(m\) grows, heterogeneous loss marks, or global resets. The finite formulas below are supporting identities; separate novelty for the finite mean-completion comparison or for a stationary hitting-time resolvent is not asserted.

## Proof

### Finite preparation

For positive selection probabilities \(q_i\) with sum one and common loss \(0<p<1\), write \(C,T,D\) as above, \(r=p/(1-p)\), and \(q(S)=\sum_{i\in S}q_i\). Given the sequence of type draws up to \(C\), the last marks of the types occupy distinct draw indices. Thus at \(C\) the state is a product of Bernoulli\((1-p)\) variables, independent of that draw sequence. Future draws and marks are independent of this stopping history. Since \(T\ge C\), the delay \(D\) is independent of \(C\) and is the first all-present hitting time from the stationary product law, including possible time zero.

Let \(P_{00}(n)\) be the all-present return probability at step \(n\) from all present. Conditional on the unselected-type set \(U\), the all-present probability is \((1-p)^{m-|U|}\). Expanding \((1+r)^{|U|}\), and noting that a fixed subset \(S\) is unselected with probability \((1-q(S))^n\), gives
\[
P_{00}(n)=(1-p)^m\sum_{S\subseteq[m]}r^{|S|}(1-q(S))^n.
\]
For the equilibrium start, renewal at the first all-present time gives \((1-p)^m/(1-z)=\mathbb E z^D\sum_{n\ge0}z^nP_{00}(n)\). Hence for \(0<z<1\),
\[
\mathbb E z^D=\left[1+\sum_{S\ne\varnothing}r^{|S|}\frac{1-z}{1-z(1-q(S))}\right]^{-1},\qquad
\mathbb ED=\sum_{S\ne\varnothing}\frac{r^{|S|}}{q(S)}.
\]
The mean follows by taking \(z\uparrow1\) in \((1-\mathbb E z^D)/(1-z)\), and the generating function extends to \(z=0\) by continuity. These identities can also verify the finite balancing comparison as context: write \(w_i=mq_i\). Then
\[
\mathbb ED=m\int_0^\infty\left[\prod_i(1+r e^{-w_it})-1\right]dt,
\qquad
\mathbb EC=m\int_0^\infty\left[1-\prod_i(1-e^{-w_it})\right]dt.
\]
The second identity follows by splitting a unit-rate marked Poisson process into independent first arrival clocks and using independence of the interarrival times from the draw marks. For \(t>0\), \(\log(1+r e^{-wt})\) is strictly convex in \(w>0\) and \(\log(1-e^{-wt})\) is strictly concave. Thus each integrand, and hence each expectation, strictly increases under majorization other than permutations. This yields the same strict balancing conclusion for \(\mathbb ET\) as the earlier full first-passage result cited below; it is not a separate contribution here.

### Ordinary cover at the slow speed

In a unit-rate Poissonization, at time \(u\) the all-seen probability is
\[
(1-e^{-au/(m\bar w_m)})^{m_1}(1-e^{-bu/(m\bar w_m)})^{m_2}.
\]
At \(u=(m/a)(\log m+x)\), we have \(\bar w_m=1+O(m^{-1})\). The first factor tends to \(\exp(-\theta e^{-x})\) and the second to 1 since \(b/a>1\). This gives the stated centering and Gumbel shift. For the discrete cover index, the union bound \(m(1-\min_i q_i)^n\) gives \(C_m=O_{\mathbb P}(m\log m)\). Conditional on that index, the difference between Poissonized cover time and index is a sum of \(C_m\) independent centered mean-one-exponential interarrival increments, of conditional variance \(C_m\). Chebyshev's inequality on \(C_m\le K m\log m\) and the union bound give an \(o_{\mathbb P}(m)\) difference, transferring the weak limit.

### Delay at the critical loss scale

Write \(r_m=c/(m-c)\) and \(A_m(j,k)=\binom{m_1}{j}\binom{m_2}{k}r_m^{j+k}\), extended by zero outside the group sizes. In the finite transform, group subsets by their two class counts. For \(z=e^{-s/m}\) and each \((j,k)\ne(0,0)\), the term in the inverse transform is
\[
A_m(j,k)\frac{1-z}{1-z+z(aj+bk)/(m\bar w_m)}
\longrightarrow \frac{C_1^jC_2^k}{j!k!}\frac{s}{s+aj+bk}.
\]
The factor multiplying \(A_m\) is at most 1, and for all sufficiently large \(m\), \(A_m(j,k)\le (2c)^{j+k}/(j!k!)\), which is summable. The empty-set term in the inverse is 1. Dominated convergence gives the asserted limiting transform. Directly from the finite mean,
\[
\frac{\mathbb ED_m}{m}=\bar w_m\sum_{j+k\ge1}\frac{A_m(j,k)}{aj+bk}
\longrightarrow\sum_{j+k\ge1}\frac{C_1^jC_2^k}{j!k!(aj+bk)},
\]
by the same bound and \(aj+bk\ge a(j+k)\).

For the two immigration–death coordinates started at zero, the number of immigrants still present at time \(t\) in class \(i\) is Poisson of mean \(C_i(1-e^{-w_i t})\), where here \(w_1=a,w_2=b\). Thus their joint zero probability is \(P_{00}(t)=\exp(-c+C_1e^{-at}+C_2e^{-bt})\). With the stationary start, the strong Markov property at \(\tau\) gives
\[
\frac{e^{-c}}{s}=\mathbb E e^{-s\tau}\int_0^\infty e^{-st}P_{00}(t)\,dt.
\]
This remains valid before establishing finiteness, using zero for \(e^{-s\tau}\) at infinity. Expanding the integrand gives the same inverse Laplace transform as the discrete limit. As \(s\downarrow0\) its inverse tends to 1 because the positive-index series with denominators \(aj+bk\) is finite, so \(\tau\) is almost surely finite. The first-order term at zero identifies its mean by monotone convergence. The stationary probability of zero is \(e^{-c}\), and positive initial populations have a strictly positive first jump time. Laplace transform continuity now gives \(D_m/m\Rightarrow\tau\); finite independence gives the independent joint limit with the ordinary cover and hence the sum limit.

Finally, the limiting delay mean can be written by Tonelli as
\[
\int_0^\infty \left[\exp\{c(\theta e^{-at}+(1-\theta)e^{-bt})\}-1\right]dt.
\]
The convexity of \(x\mapsto e^{-tx}\) is strict for \(t>0\), so the weighted sum inside is strictly greater than \(e^{-t}\) by the speed normalization. At equal speeds it is \(e^{-t}\); termwise integration then gives \(\sum_{h\ge1}c^h/(h!h)\). This proves the strict delay penalty.

## Verification

The accompanying standard-library `verify.py` tests the finite identities by exact-rational Markov chains and verifies numerical consistency of the limiting mean and transform on specified inputs. The frozen test report records 1168 deterministic checks. Neither the script nor the numerical checks certify the all-parameter limit or historical novelty; the proof above gives the parameter ranges and limit exchanges.

## Relationship to prior work

Attrill and Garoni prove cover/delay independence and the critical Gumbel-plus-stationary-queue law for **uniform sampling** (arXiv:2605.14206v1, Lemmas 4.2 and 4.9, Theorem 4.10). That case has a single death speed. The indexed note *Exact first-passage transform and strict balancing law for nonuniform clumsy coupons* (`d79ee5d7e4b4`) already gives the full first-completion transform and strict Schur-convex mean in this same unequal-selection, common-loss model. The finite decomposition here is used to separate slow ordinary cover from the critical delay, not to claim an independent discovery of the full finite mean comparison. The indexed *Poisson dust and finite exceptional loss modes in clumsy coupon collection* (`94997b0a46f8`) uses uniform selection and instead varies loss probabilities; it does not give two distinct death rates from two draw speeds.

Long's unequal-probability case (arXiv:2605.14511v1, §3.6) is a global-reset collector; his clumsy replacement case is uniform. Anceaume, Busnel and Sericola (arXiv:1402.5245v1) address the monotone collector, not the nonempty delay. The stationary renewal identity and infinite-server interpretation are standard methods, not proposed new theorems about queues. The distinct claim is the coupon-model limit with a Gumbel location controlled only by the slow class and a nontrivial residual emptying law involving both fixed classes, together with convergence of the delay mean and its strict comparison.

## Limitations

Completion-time moment convergence beyond the post-cover mean is not asserted, nor is stochastic majorization of the finite full law. No general historical priority claim follows from comparison with the above sources.

## References

1. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1.
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1.
3. E. Anceaume, Y. Busnel and B. Sericola, *New results on a generalized coupon collector problem using Markov chains*, arXiv:1402.5245v1.
4. A. M. Makowski, *On a Random Sum Formula for the Busy Period of the M/G/Infinity Queue with Applications*, University of Maryland technical report TR 2001-9.
5. *Exact first-passage transform and strict balancing law for nonuniform clumsy coupons*, Resultary `d79ee5d7e4b4`.
6. *Poisson dust and finite exceptional loss modes in clumsy coupon collection*, Resultary `94997b0a46f8`.
