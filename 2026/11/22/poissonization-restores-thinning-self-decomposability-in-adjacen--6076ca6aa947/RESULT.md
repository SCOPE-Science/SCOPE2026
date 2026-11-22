# Poissonization restores thinning self-decomposability in adjacent-gamma mixtures

## Finding
For a gamma mixture with two adjacent shapes, its Poisson count mixture is always compound Poisson, and the exact boundary for *Bernoulli-thinning self-decomposability* is generally different from the self-decomposability boundary of the continuous mixing variable. In particular, Poissonization can restore the former even when the mixing variable is not self-decomposable. The boundary contains a natural infinite hierarchy: every factorial-Palm residual of the Poisson new X-Lindley count law lies on the critical, rate-uniform self-decomposable line.

For \(r>0\), \(\theta>0\), and \(0\le s\le1\), let \(\Lambda\) have the mixture distribution
\[
\Lambda\sim s\,\mathrm{Gamma}(r,\text{rate }\theta)
 +(1-s)\,\mathrm{Gamma}(r+1,\text{rate }\theta),
\qquad X\mid\Lambda\sim\mathrm{Poisson}(\Lambda).
\]
Writing \(g_\theta(z)=\theta/(\theta+1-z)\), its probability-generating function is
\[
G(z)=s g_\theta(z)^r+(1-s)g_\theta(z)^{r+1}
=\frac{\theta^r[\theta+s(1-z)]}{(\theta+1-z)^{r+1}}.
\]
The law of \(X\) is compound Poisson for **all** these parameters. It is Bernoulli-thinning self-decomposable if and only if
\[
\boxed{(r+1)(\theta+s)^2\ge s(\theta+1)^2.}\tag{1}
\]
Equivalently, for \(s=0\) or \(s\ge1/(r+1)\), it is thinning self-decomposable at every rate \(\theta>0\). For \(0<s<1/(r+1)\), it is so precisely for
\[
\boxed{\theta\ge\theta_*(r,s)
=\frac{\sqrt{s}-s\sqrt{r+1}}{\sqrt{r+1}-\sqrt{s}}>0.}\tag{2}
\]
The mixing variable \(\Lambda\), by contrast, is continuously self-decomposable if and only if \(s=0\) or \(s\ge1/(r+1)\), regardless of \(\theta\). Consequently, every \(0<s<1/(r+1)\) with \(\theta\ge\theta_*(r,s)\) yields a genuinely thinning-self-decomposable count law with a **non-self-decomposable mixing distribution**.

At the Poisson new X-Lindley (PNXL) specialization \(r=1\), \(s=1/2\), define the factorial-Palm residual \(Y_m\) for each integer \(m\ge0\) by
\[
\Pr(Y_m=n)=\frac{(n+m)_m\,\Pr(X=n+m)}{\mathbb E[(X)_m]},
\qquad n=0,1,2,\ldots,
\]
where \((x)_m=x(x-1)\cdots(x-m+1)\) and \((x)_0=1\). Every one of these laws is thinning self-decomposable at every \(\theta>0\), and in fact
\[
\boxed{\mathbb E[z^{Y_m}]
=\frac1{m+2}g_\theta(z)^{m+1}
 +\frac{m+1}{m+2}g_\theta(z)^{m+2}.}\tag{3}
\]
Here \(1/(m+2)=1/((m+1)+1)\) is exactly the critical mixing weight for shape \(m+1\).

## Assumptions and scope
The gamma laws use the shape–**rate** parameterization: their Laplace transforms are \((\theta/(\theta+t))^r\). The count laws live on \(\{0,1,\dots\}\). Self-decomposability of \(\Lambda\) means that for every \(0<c<1\), \(\Lambda\) has the distribution of \(c\Lambda'+R_c\), with independent nonnegative \(\Lambda'\stackrel{d}{=}\Lambda\) and \(R_c\). Discrete thinning self-decomposability means the corresponding representation \(X\stackrel d=c\circ X'+Z_c\), where \(c\circ X'\) is independent Bernoulli thinning of a copy \(X'\), and the count \(Z_c\) is independent. These are **different** properties. The endpoint \(s=0\) is interpreted as a single \(\mathrm{Gamma}(r+1,\theta)\) law.

## Proof
**1. Lévy measures and ordinary infinite divisibility.** By the mixture formula,
\[
L(t)=\mathbb E[e^{-t\Lambda}]
=\frac{\theta^r(\theta+st)}{(\theta+t)^{r+1}}.
\]
For \(s>0\), the elementary identity \(\log(a/(a+t))=\int_0^\infty(e^{-tx}-1)e^{-ax}\,dx/x\) gives
\[
\log L(t)=\int_0^\infty(e^{-tx}-1)\,
\frac{k(x)}{x}\,dx,
\quad k(x)=(r+1)e^{-\theta x}-e^{-\theta x/s}.
\tag{4}
\]
Since \(\theta/s\ge\theta\) and \(r>0\), \(k(x)>0\) at every \(x>0\). For \(s=0\), the same identity gives \(k(x)=(r+1)e^{-\theta x}\). The Lévy integrability condition follows from boundedness near zero and exponential decay at infinity. Thus the continuous laws are infinitely divisible. The characterizing Lévy-density criterion for continuous self-decomposability requires \(k\) to be nonincreasing. For \(s>0\),
\[
k'(x)=-(r+1)\theta e^{-\theta x}+(\theta/s)e^{-\theta x/s}.
\]
Because \(e^{-\theta x/s}/e^{-\theta x}\) decreases in \(x\), the inequality \(k'(x)\le0\) for **all** \(x>0\) is equivalent to its zero-limit condition \(1/s\le r+1\). For \(s=0\), it decreases strictly. This proves the continuous classification, including the singularly isolated endpoint \(s=0\).

Set \(q=1/(\theta+1)\) and \(a=s/(\theta+s)\) for \(s>0\), and \(a=0\) for \(s=0\). Here \(0\le a\le q<1\). Expanding \(\log G(z)\) at \(z=0\) yields
\[
\log G(z)=\log G(0)+\sum_{n\ge1}\lambda_n z^n,
\qquad \lambda_n=\frac{(r+1)q^n-a^n}{n}>0.
\tag{5}
\]
Indeed \(\sum_{n\ge1}\lambda_n=-\log G(0)<\infty\) because \(G(1)=1\). Hence \(G(z)=\exp(\sum_{n\ge1}\lambda_n(z^n-1))\), a genuine compound-Poisson generating function. No finite coefficient test is being used to prove its positivity.

**2. Sharp thinning criterion, with an explicit innovation law.** For \(u\in[0,1]\), put
\[
q_u=\frac{u}{\theta+u},\quad
a_u=\frac{su}{\theta+su},\quad
b_n(u)=(r+1)q_u^n-a_u^n,
\]
with \(a_u=0\) when \(s=0\). The logarithmic coefficient of positive degree \(n\) in \(G(1-c+cz)\) is \(b_n(c)/n\), so the candidate independent-innovation generating function \(H_c(z)=G(z)/G(1-c+cz)\) satisfies
\[
\log H_c(z)=\log H_c(0)+\sum_{n\ge1}\nu_n(c)z^n,
\quad \nu_n(c)=\frac{b_n(1)-b_n(c)}{n}.
\tag{6}
\]
For \(s>0\) and \(u>0\), direct differentiation gives
\[
\frac{d}{du}b_n(u)=n\theta u^{n-1}
\left[\frac{r+1}{(\theta+u)^{n+1}}
-\frac{s^n}{(\theta+su)^{n+1}}\right].
\tag{7}
\]
The ratio of the second bracketed magnitude to the first, without \(r+1\), is
\[
\frac{s^n(\theta+u)^{n+1}}{(\theta+su)^{n+1}}
=\frac{s(\theta+u)^2}{(\theta+su)^2}
\left(\frac{s(\theta+u)}{\theta+su}\right)^{n-1}
\le\frac{s(\theta+1)^2}{(\theta+s)^2}.
\tag{8}
\]
The final bound uses \(s(\theta+u)/(\theta+su)\le1\) and the monotonicity of \((\theta+u)/(\theta+su)\) on \([0,1]\). Thus condition (1) forces \(b_n(u)\) to increase with \(u\) for every integer \(n\ge1\). In particular \(\nu_n(c)\ge0\) for every \(0<c<1\); the sum is finite by comparison with \(\sum_n\lambda_n\). Since \(H_c(1)=1\), (6) gives an explicit compound-Poisson innovation law with jump intensities \(\nu_n(c)\). The case \(s=0\) follows by dropping the second term of (7).

Conversely, when (1) fails, (7) at \(n=1,u=1\) is strictly negative. Hence for all \(c<1\) sufficiently close to one, \(\nu_1(c)<0\). As \(H_c(0)>0\), its coefficient of \(z\) is \(H_c(0)\nu_1(c)<0\): no count-valued innovation exists. This proves the **if and only if**, including the equality boundary. Taking square roots in (1), then rearranging, yields (2) and the uniform-rate regime.

**3. Critical factorial-Palm hierarchy.** The published PNXL mixing density is \(\theta(1+\theta x)e^{-\theta x}/2\), the equal mixture of gamma shapes one and two at common rate \(\theta\). For any integer \(m\ge0\), the identity \(\frac{d^m}{dz^m}g_\theta(z)^v=(v)_m\theta^{-m}g_\theta(z)^{v+m}\) gives
\[
\frac{G^{(m)}(z)}{G^{(m)}(1)}
=\frac{m!\,g_\theta(z)^{m+1}+(m+1)!\,g_\theta(z)^{m+2}}{m!+(m+1)!},
\]
which is (3). Its lower-shape weight equals \(1/(m+2)\), exactly the all-rate boundary in (1), so every residual is thinning self-decomposable.

## Verification
The standalone standard-library script `checks/checker.py` implements exact rational arithmetic and independently checks the generating-function identities, the logarithmic jump formula, innovation coefficients, endpoint inequalities and factorial-Palm weights on a range of rational examples. In particular, for \(r=1,s=1/4\), its exact first canonical difference is \(-230/5929\) at \(\theta=1/10\) (thinning self-decomposability fails) and \(7/100\) at \(\theta=1/4\) (thinning self-decomposability holds), while continuous self-decomposability fails at both rates. A finite checker does not establish statements over all parameter values or all indices: those conclusions follow from the inequalities (4)–(8).

## Relationship to prior work
Irshad, Aswathy, Maya and Nadarajah (2023) introduced the PNXL count distribution, its generating function and an INAR(1) model using PNXL innovations. Those definitions and calculations are prior work; this result concerns the exact **stationary-marginal thinning criterion**, continuous-versus-discrete separation, and all-order factorial-Palm closure. Pakes (2022) gives the established Lévy and discrete canonical-sequence characterizations of self-decomposability; these characterizations are used here, not claimed as new. Kella and Löpker (2022) study general thinning and mixing. The established two-parameter Poisson-generalized Lindley family with PGF \(\theta^\alpha(\theta+2-z)/[(\theta+1)(\theta+1-z)^\alpha]\) is exactly the subfamily \(r=\alpha-1\), \(s=\theta/(\theta+1)\) for \(\alpha>1\); it is not presented as a new distribution or independent special case. The present classification includes that curve but determines the full independent-weight region, its mixing-versus-count separation, and the critical PNXL Palm hierarchy. Ong and collaborators (2023) analyze an NB/one-step-*shifted*-NB mixture, whose generating function is a Bernoulli factor times an NB generating function, not this mixture of two **adjacent shapes**.

## Limitations
No claim is made that *every* discrete self-decomposable law admits a continuously self-decomposable Poisson mixing variable: the explicit examples disprove the converse. The classification is limited to the specified two-component common-rate mixture; it does not assert analogous thresholds for arbitrary gamma mixtures or arbitrary thinning mechanisms. The finite reproducibility checks are corroborative and not infinite certificates. The originating PNXL paper was accessible through its indexed mathematical sections but the publisher PDF/full article rendering could not be retrieved in this inspection; priority against uninspected portions and older specialized mixture literature remains a residual risk. No independent mathematical audit has been performed.

## References
1. M. R. Irshad, S. Aswathy, R. Maya, S. Nadarajah, “New One-Parameter Over-Dispersed Discrete Distribution and Its Application to the Nonnegative Integer-Valued Autoregressive Model of Order One,” *Mathematics* 12 (2024), 81; first public 26 December 2023. https://doi.org/10.3390/math12010081
2. A. G. Pakes, “Mutant Number Laws and Infinite Divisibility,” *Axioms* 11 (2022), 584, especially Section 2, Definitions 1–3. https://doi.org/10.3390/axioms11110584
3. O. Kella and A. Löpker, “On Binomial Thinning and Mixing,” arXiv:2202.10296, first public 21 February 2022. https://arxiv.org/abs/2202.10296
4. M. R. Irshad, V. D'cruz, R. Maya, N. Mamode Khan, “Inferential properties with a novel two parameter Poisson generalized Lindley distribution with regression and application to INAR(1) process,” *Journal of Biopharmaceutical Statistics* 33 (2023), 335–356. https://doi.org/10.1080/10543406.2022.2152832
5. H. Papageorgiou and M. Vardaki, “Bivariate Discrete Poisson–Lindley Distributions,” *Journal of Statistical Theory and Practice* 16 (2022), 30. https://doi.org/10.1007/s42519-022-00261-z
6. S. H. Ong, S. Z. Sim, S. Liu, H. M. Srivastava, “A Family of Finite Mixture Distributions for Modelling Dispersion in Count Data,” *Stats* 6 (2023), 942–955. https://doi.org/10.3390/stats6030059
