# Lattice multicoverage laws for macroscopic uniform coupon batches

## Finding

At each integer round sample independently and uniformly a subset of exactly \(d_N\) of \(N\) coupon types, retaining every occurrence. Assume \(d_N/N\to\rho\in(0,1)\), and fix an integer \(c\ge1\). Write \(T_{N,c}\) for the first round by which every type has appeared at least \(c\) times. Set
\[
 p_N=d_N/N,\quad q_N=1-p_N,\quad h_N(t)=\Pr\{\operatorname{Bin}(t,p_N)\le c-1\},\quad m_N(t)=Nh_N(t),
\]
\[
 b_N=\min\{t\ge0:m_N(t)\le1\},\qquad \theta_N=m_N(b_N).
\]
Here \(b_N\) is integer and \(q_N+o(1)\le\theta_N\le1\). For every integer \(k\), the number \(U_N(b_N+k)\) of types having fewer than \(c\) hits satisfies the *moving-parameter* Poisson approximation
\[
 \Pr\{U_N(b_N+k)=j\}=e^{-\theta_Nq_N^k}\frac{(\theta_Nq_N^k)^j}{j!}+o(1),\quad j=0,1,\ldots,
\]
with the error uniform over any fixed finite set of \(j,k\). Consequently, uniformly in integer \(k\),
\[
 \Pr\{T_{N,c}-b_N\le k\}=\exp(-\theta_Nq_N^k)+o(1).
\]
For \(\theta>0\) and \(0<q<1\), define the convergent series
\[
 \mu(\theta,q)=\sum_{k=0}^{\infty}(1-e^{-\theta q^k})-\sum_{k=1}^{\infty}e^{-\theta q^{-k}},
\]
\[
 v_2(\theta,q)=\sum_{k=0}^{\infty}(2k+1)(1-e^{-\theta q^k})+\sum_{k=1}^{\infty}(2k-1)e^{-\theta q^{-k}}.
\]
Then the complete moment expansions are
\[
 \mathbb E T_{N,c}=b_N+\mu(\theta_N,q_N)+o(1),\qquad
 \operatorname{Var}(T_{N,c})=v_2(\theta_N,q_N)-\mu(\theta_N,q_N)^2+o(1).
\]
In addition, with \(\lambda_N=-\log q_N\),
\[
 b_N=\frac{\log N+(c-1)\log\log N}{\lambda_N}+O(1).
\]
Thus the terminal transition occupies only a bounded number of rounds and has a lattice rather than a continuous Gumbel profile. Along every subsequence with \(\theta_N\to\theta\), the centered cover time converges to the integer-valued law with distribution function \(\exp(-\theta q^k)\) at integer \(k\).

## Assumptions and scope

The number \(N\) tends to infinity through positive integers; \(d_N\) is integer with \(1\le d_N<N\) and \(d_N/N\to\rho\) strictly between zero and one. Sampling is uniform over all size-\(d_N\) subsets and independent between rounds; within-round selections are without replacement. The multiplicity threshold \(c\) remains fixed. The theorem does **not** claim a full-sequence fixed limiting distribution without accounting for the phase \(\theta_N\), nor cover \(\rho\to0\), \(\rho\to1\), or growing \(c\).

## Proof

**Single-type scale.** Each type's number of appearances after \(t\) rounds is binomial with parameters \(t,p_N\). At large \(t\), uniformly with \(p_N\) in a fixed compact subinterval of \((0,1)\), putting \(h=h_N\),
\[
 h(t)=q_N^t\frac{(tp_N/q_N)^{c-1}}{(c-1)!}\bigl(1+O_c(t^{-1})\bigr),
 \qquad h(t+1)/h(t)=q_N+O_c(t^{-1}).
\]
These formulas include \(c=1\), when they are exact. Hence \(b_N\asymp\log N\), the displayed expansion for \(b_N\), and \(\theta_N\in[q_N+o(1),1]\). For each fixed signed integer \(k\),
\[
 m_N(b_N+k)=\theta_Nq_N^k(1+o(1)).
\]

**Joint rare-defect lemma.** Fix a positive integer \(r\). For any fixed set of \(r\) distinct types, a round has probability
\[
 a_{0,N,r}=\frac{(N-d_N)_{\underline r}}{(N)_{\underline r}}=q_N^r(1+O_r(N^{-1}))
\]
of choosing none, and for each prescribed one of these types alone the probability is \(a_{1,N,r}=p_Nq_N^{r-1}(1+O_r(N^{-1}))\). All selection-pattern probabilities for the \(r\) tagged types are bounded uniformly; the generating polynomial of their one-round hit indicators is \(F(\boldsymbol z)=a_{0,N,r}+a_{1,N,r}\sum_i z_i+\text{terms of total degree at least 2}\). In \(F(\boldsymbol z)^t\), the coefficients with each variable's degree at most \(c-1\) have leading combined contribution from \(r(c-1)\) separate rounds, each hitting exactly one tagged type:
\[
 a_{0,N,r}^{t}\frac{(ta_{1,N,r}/a_{0,N,r})^{r(c-1)}}{((c-1)!)^r}\bigl(1+O_{c,r}(t^{-1})\bigr).
\]
Indeed, every monomial involving a multi-hit round or fewer than \(r(c-1)\) one-hit rounds has at most \(r(c-1)-1\) chosen round positions and contributes a lower degree polynomial in \(t\); there are finitely many such monomials for fixed \(r,c\). For \(c=1\) this reduces to the exact all-missing probability \(a_{0,N,r}^t\). The leading expression, compared with the product of the \(r\) one-type binomial tails, gives, uniformly for \(t\asymp\log N\),
\[
 \Pr\{\text{all }r\text{ tagged types have fewer than }c\text{ hits at time }t\}
 =h_N(t)^r\bigl(1+O_{c,r}(t^{-1}+t/N)\bigr).
\]
Therefore the factorial moment of \(U_N(t)\) is \((N)_{\underline r}h_N(t)^r(1+o(1))\). At \(t=b_N+k\), it equals \((\theta_Nq_N^k)^r+o(1)\) for every fixed \(r\). Any subsequence has a further subsequence with \(\theta_N\to\theta\in[q,1]\); on it the factorial-moment criterion gives a Poisson law of mean \(\theta q^k\). Compactness gives the asserted moving-parameter law for the full sequence.

**Uniform tails and moments.** Let \(A_i(t)\) be the indicator that type \(i\) has fewer than \(c\) hits at time \(t\). For distinct types \(i,j\), conditional on the full round-indicator vector of \(i\), the Bernoulli success probability for \(j\) in a round is \((d_N-1)/(N-1)\) if \(i\) was drawn, and \(d_N/(N-1)\) otherwise. Thus the conditional probability of \(A_j(t)=1\) is coordinatewise nondecreasing in the round indicators of \(i\), while \(A_i(t)\) is coordinatewise nonincreasing. The indicator vector of \(i\) has independent coordinates, so the elementary product-measure covariance inequality implies \(\operatorname{Cov}(A_i(t),A_j(t))\le0\). Consequently
\[
 \operatorname{Var}(U_N(t))\le\mathbb EU_N(t)=m_N(t),\quad
 \Pr\{U_N(t)=0\}\le1/m_N(t),\quad
 \Pr\{U_N(t)>0\}\le m_N(t).
\]
Select any \(\eta\) with \(q<\eta<1\). For all sufficiently large \(N\), the ratio \(m_N(t+1)/m_N(t)\le\eta\) for \(t\ge\lfloor b_N/2\rfloor\). The last two probability bounds now give uniform right and left geometric tails for \(T_{N,c}-b_N\) when the left deviation is at most \(b_N/2\). For larger left deviations, \(m_N(\lfloor b_N/2\rfloor)\ge N^{\delta}\) for some \(\delta>0\), and there are only \(O(\log N)\) possible integers. These bounds imply uniform integrability of the squares of centered cover times. Thus the pointwise lattice distribution approximation extends to uniform CDF convergence and to convergence of the first two centered moments. The integer-tail summation identities give exactly the stated series for \(\mu\) and \(v_2\).

## Verification

The accompanying standalone `verify.py` uses two independently structured finite-state calculations: full capped-occupancy distributions over all possible uniformly drawn subsets, and the distribution of a prescribed fixed set of tagged coupons. It checked equality of exact factorial moments, the one-type binomial mean, negative pair covariance, total mass, and the range of the exact completion probability. It passed 2,268 exact-rational assertions for \(4\le N\le7\), every \(1\le d<N\), \(1\le c\le3\), and \(0\le t\le5\). These finite tests do not establish the asymptotic theorem; the preceding proof does.

## Relationship to prior work

Doumas–Spektor, arXiv:2607.01463 (first public version July 1, 2026), analyze keep-all batch coverage with fixed batch size and state continuous-Gumbel and smooth mean/variance expansions. These fixed-size formulas do not imply the nonvanishing-sampling-fraction lattice phase or fixed-threshold multicoverage law. Schilling–Henze (2021) study fixed-size group drawings with \(c\)-fold coverage, using the centering \((N/d)\{\log N+(c-1)\log\log N+O(1)\}\); at \(d/N\to\rho>0\), its coefficient is not the correct \(1/[-\log(1-\rho)]\). Betken–Thäle (2023) explicitly use fixed \(s\) for their quantitative approximation. Berend–Sher (arXiv:2509.17201) give order-one *bounds* on the uniform-group mean in the macroscopic regime but not the displayed phase-resolved \(o(1)\) expansion or the repeated-hit terminal distribution. Older general group-allocation Poisson theorems address empty cells and may offer overlapping tools; no claim is made that Poisson approximation as a method is new.

## Limitations

No external independent review has been performed. General Poisson approximation or Russian-language group-allocation literature could subsume the defect-count step. The terminal lattice law and phase-resolved expectation/variance are claimed only under the stated macroscopic-batch and fixed-multiplicity hypotheses. No rate is claimed, and the result does not cover a variable target multiplicity or adversarial selection of batches.

## References

1. A. V. Doumas and S. Spektor, *Two Multi–Draw Coupon Collector models with different retention rules*, arXiv:2607.01463, first version July 1, 2026. https://arxiv.org/abs/2607.01463
2. J. Schilling and N. Henze, *Two Poisson limit theorems for the coupon collector's problem with group drawings*, Journal of Applied Probability 58 (2021), 966–977. https://www.math.kit.edu/stoch/~henze/seite/aiwz/media/ap-17926-final.pdf
3. C. Betken and C. Thäle, *Approaching the coupon collector's problem with group drawings via Stein's method*, Journal of Applied Probability 60 (2023). https://doi.org/10.1017/jpr.2023.6
4. D. Berend and T. Sher, *On a Conjecture on Uniform Group Drawings in the Coupon Collector Problem*, arXiv:2509.17201, first version September 21, 2025. https://arxiv.org/abs/2509.17201
5. V. A. Vatutin and V. G. Mikhailov, *Limit Theorems for the Number of Empty Cells in an Equiprobable Scheme for Group Allocation of Particles*, Theory of Probability and Its Applications 27 (1983), 734–743. https://doi.org/10.1137/1127084
6. V. G. Mikhailov, *Estimate for the accuracy of the Poisson approximation for the number of empty cells in an equiprobable scheme for group allocation of particles, and applications*, Proc. Steklov Inst. Math. 282 (2013). https://www.mathnet.ru/eng/tm3497
