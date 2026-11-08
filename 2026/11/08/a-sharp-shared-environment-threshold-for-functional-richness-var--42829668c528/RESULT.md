# A sharp shared-environment threshold for functional-richness variance in paired ecological guilds

## Finding

For **every** integer \(g\ge2\), consider \(g\) disjoint functional guilds, each containing two species. Each guild retains its function if at least one member survives a single environmental episode. Let the common, unobserved species survival probability be
\[
P\sim\operatorname{Beta}(p\theta,(1-p)\theta),\qquad 0<p<1,\quad\theta>0.
\]
Conditionally on \(P\), all \(2g\) survival indicators are independent Bernoulli variables with probability \(P\). Define \(Y\) as the count of surviving functions, and \(V_{g,p}(\theta)=\operatorname{Var}(Y)\). The species indicators have mean \(p\) and pairwise correlation \(\rho=1/(\theta+1)\).

**Theorem (complete, sharp one-peak law).** Put \(p_c(g)=(g+5)/(12g)\). If \(0<p<p_c(g)\), then there is a **unique** positive \(\theta_*(g,p)\) such that \(V\) is strictly increasing on \((0,\theta_*)\) and strictly decreasing on \((\theta_*,\infty)\). If \(p_c(g)\le p<1\), then \(V\) is strictly decreasing throughout \((0,\infty)\). The unique positive derivative zero in the first case is simple. In the correlation coordinate \(\rho\), the first case has a unique intermediate-correlation variance maximum; the second is strictly increasing with correlation.

For an exact witness take \(g=2\), \(p=1/5\). The boundary is \(p_c(2)=7/24\), and at \(\theta=1/3\) the variance is \(2052/3125\), strictly larger than either limit \(16/25\) (perfect environmental synchrony) or \(288/625\) (independent species).

## Assumptions and scope

Each of the \(g\) guilds has exactly two distinct member species, and the guilds are disjoint. There is one common latent environmental draw \(P\) for the entire community, made before the Bernoulli survival events. The environmental concentration \(\theta\) changes species correlation while holding each marginal species survival probability \(p\) fixed. No dynamic population process, between-guild interactions, observation errors, or threshold of two or more surviving members is included. The theorem holds uniformly for every integer \(g\ge2\), every real \(p\in(0,1)\) and every real \(\theta>0\), including the exact phase boundary.

## Proof

Write \(q=1-p\), \(x=\theta\), and let \(Z_i\) indicate that **both** species in guild \(i\) fail. Then \(Y=g-\sum_{i=1}^gZ_i\). Conditional independence yields
\[
\mathbb EZ_i=u(x)=\mathbb E(1-P)^2
=\frac{q(qx+1)}{x+1},
\quad
\mathbb E(Z_iZ_j)=v(x)=\mathbb E(1-P)^4
=\frac{q(qx+1)(qx+2)(qx+3)}{(x+1)(x+2)(x+3)}
\quad(i\ne j).
\]
Therefore
\[
V_{g,p}(x)=g u(x)+g(g-1)v(x)-g^2u(x)^2.\tag{1}
\]
Differentiating (1), collecting denominators and factoring gives the **exact identity**
\[
\frac{d V_{g,p}}{dx}
=\frac{g p(p-1)\,H_{g,q}(x)}{(x+1)^3(x+2)^2(x+3)^2},
\qquad H_{g,q}(x)=\sum_{j=0}^5c_j(g,q)x^j,
\tag{2}
\]
with coefficients
\[
\begin{aligned}
c_0&=-6(12gq-11g+5),\\
c_1&=-6(12gq^2+8gq-23g+12q+7),\\
c_2&=-102gq^2+82gq+90g-18q^2-156q+7,\\
c_3&=-34gq^2+86gq+18g-40q^2-106q+29,\\
c_4&=8gq^2+20gq-28q^2-22q+11,\\
c_5&=(4g-6)q^2+1.
\end{aligned}\tag{3}
\]

We now prove the nonstandard fact that **the coefficient sequence \((c_0,c_1,\ldots,c_5)\) has zero or one sign changes, with exactly one change if and only if \(q>q_c=(11g-5)/(12g)\)**. This proof is for all real \(q\in(0,1)\) and all integers \(g\ge2\), not a finite parameter scan.

First, \(c_5>0\). For \(g=2\), \(c_4=-12q^2+18q+11\) and \(c_3=-108q^2+66q+65\); both concave quadratics have strictly positive endpoint values on \([0,1]\). Increasing \(g\) adds respectively \((g-2)(8q^2+20q)\) and \((g-2)(-34q^2+86q+18)\), which are nonnegative (the second factor is positive by concavity and positive endpoints). Thus \(c_3,c_4,c_5>0\) for all admissible parameters.

For \(g\ge3\), \(c_2=(-324q^2+90q+277)+(g-3)(-102q^2+82q+90)>0\); both parenthesized quadratics are concave and have strictly positive values at \(q=0,1\). For \(g=2\), \(c_2=-222q^2+8q+187\), which is strictly positive on \([0,9/10]\), since it is concave with positive endpoint values. Whenever this \(c_2\) is nonpositive, \(q>9/10\), and then \(c_1<0\): the expression inside the minus-six in \(c_1\) increases strictly with \(q\) and equals \(141/25>0\) at \(g=2,q=9/10\). Thus **a negative \(c_2\) cannot follow a nonnegative \(c_1\)**.

Next, the expression inside the minus-six in \(c_1\) has derivative \(24gq+8g+12>0\). At \(q_c=(11g-5)/(12g)\) its value is
\[
-\frac{67g^2-66g+35}{12g}<0,
\]
because the displayed quadratic is strictly positive. Hence \(c_1>0\) whenever \(q\le q_c\). Meanwhile \(c_0\ge0\) precisely for \(q\le q_c\), and \(c_0<0\) for \(q>q_c\).

Consequently, if \(q\le q_c\), all six coefficients are nonnegative, and in fact the last five are positive; hence \(H_{g,q}(x)>0\) for every \(x>0\). If \(q>q_c\), \(c_0<0\), \(c_3,c_4,c_5>0\), and the established relation among \(c_1,c_2\) rules out any negative-after-positive return. There is exactly **one** sign change in ascending order. By Descartes' rule of signs (equally valid with the coefficients reversed), \(H_{g,q}\) has at most one positive root counting multiplicity; since \(H_{g,q}(0)=c_0<0\) and \(H_{g,q}(x)\to+\infty\) as \(x\to\infty\), it has exactly one, necessarily simple. By (2), the prefactor \(gp(p-1)\) is negative; hence the derivative is first positive and then negative. The case \(q\le q_c\) has negative derivative for all \(x>0\). Since \(q>q_c\) is exactly \(p<p_c(g)=(g+5)/(12g)\), the theorem follows.

Finally, using \(u(0+)=v(0+)=q\) and \(u(\infty)=q^2\), \(v(\infty)=q^4\) in (1) gives
\[
\lim_{x\downarrow0}V_{g,p}(x)=g^2p(1-p),\qquad
\lim_{x\to\infty}V_{g,p}(x)=g(2p-p^2)(1-p)^2.
\]
The limits correspond respectively to a two-point all-survive/all-fail environment and deterministic common survival parameter \(P=p\), and are not finite-\(\theta\) equilibria.

## Verification

`check.py` is an executable exact-arithmetic reproduction of the derivative identity, coefficient sign certificate at representative rational parameters, and a distinct direct Beta-binomial enumeration of species-survival configurations. It compares the latter to the moment formula for guild counts at several community sizes and positive rational environmental parameters; it also verifies the exact witness. Symbolic algebra checks support formula (2), while the textual sign proof establishes all infinite parameter ranges. Run `python check.py` after installing the dependency in `requirements.txt`.

## Relationship to prior work

Fonseca and Ganade (2001) introduce functional-redundancy loss under fixed-count random extinction and cite classic rarefaction variance. Kendall (1998) uses a beta-distributed individual survival probability to model environmental stochasticity in survivorship, but addresses statistical estimation rather than finite-guild functional-richness variance. Kaneryd and coauthors (2012) investigate correlated environmental responses in stochastic food webs, but their dynamic simulations and continuous population densities do not imply the exact phase diagram for the present static Beta mixture. The present statement concerns a different quantity: the **global number of all-or-one partner functions** under a single shared Beta-distributed survival propensity, with a parameter-exact unique-peak criterion for every number of two-species guilds.

## Limitations

This is a mathematical result for an idealized common-environment, conditionally independent survival model with uniform two-species guilds. It does not establish ecological causal effects of increasing observed climate variability, nor does it imply changes in long-term population persistence, abundance, or dynamic coextinction cascades. The general ecological literature is broad; the inspected sources and search records do not establish definitive historical priority, and a theorem stated under general exchangeable Bernoulli mixtures could conceivably imply this special Beta-family derivative law. The result has not undergone independent audit.

## References

1. Kendall, B. E. (1998). *Estimating the magnitude of environmental stochasticity in survivorship data*. Ecological Applications 8, 184–193. https://doi.org/10.1890/1051-0761(1998)008[0184:ETMOES]2.0.CO;2 (first online 1998-02-01).
2. Fonseca, C. R. & Ganade, G. (2001). *Species functional redundancy, random extinctions and the stability of ecosystems*. Journal of Ecology 89, 118–125. https://doi.org/10.1046/j.1365-2745.2001.00528.x (first online 2001-12-21).
3. Kaneryd, L. et al. (2012). *Species-rich ecosystems are vulnerable to cascading extinctions in an increasingly variable world*. Ecology and Evolution 2, 858–874. https://doi.org/10.1002/ece3.218 (version of record online 2012-03-30).
