# A sharp sampling-resolution transition in geometric discrete generalized exponential hazards

## Finding
Consider the univariate geometric discrete generalized exponential (UGDGE) count law obtained by taking a geometric number of independent discrete generalized exponential lifetimes and retaining their maximum. For its three interior parameters \(\alpha>0\), \(0<p<1\), \(0<\theta<1\), the entire sequence of conditional discrete failure probabilities is either strictly increasing, strictly decreasing, or decreases and then increases with at most one bottom tie. Moreover, in the bathtub-eligible region the visibility of the bathtub has a **unique sharp transition in the bin-resolution parameter**.

More precisely, define \(\theta_c(\alpha)=2\alpha/(1+\alpha)\). For \(\alpha\ge1\), the discrete failure probabilities are strictly increasing. For \(0<\alpha<1\) and \(\theta\ge\theta_c(\alpha)\), they are strictly decreasing. For \(0<\alpha<1\) and \(\alpha\le\theta<\theta_c(\alpha)\), they strictly decrease at the first step and eventually strictly increase, with only one change of monotonicity. Finally, if \(0<\theta<\alpha<1\), there exists a **unique** \(p_*(\alpha,\theta)\in(0,1)\): for \(p<p_*\) the entire sequence is strictly increasing; for \(p>p_*\) it decreases initially and then increases; at \(p=p_*\) its first two entries are equal and all subsequent entries strictly increase.

The unique threshold is specified by an exact finite expression. With
\[
a=1-(1-p)^\alpha,\qquad b=1-(1-p^2)^\alpha,
\]
set
\[
R_{\alpha,\theta}(p)=a\,[a(1+b)-2b]-\theta b(1-a)^2.
\]
Then \(p_*\) is the unique root of \(R_{\alpha,\theta}(p)=0\) on \((0,1)\). In the entire bathtub-eligible region \(0<\alpha<1\), \(0<\theta<\theta_c(\alpha)\), the sign of \(R\) decides the initial comparison: positive means strictly increasing from the start, zero means equality at the first step, and negative means an initial decrease (followed eventually by increase).

For example, at \(\alpha=1/2\), \(\theta=1/10\), the unique threshold is \(p_*\approx0.669739585966281\). Choosing \(p=1/2\) gives a strictly increasing discrete failure sequence; choosing \(p=9/10\) gives a bathtub-shaped one, although both parameter choices correspond to continuous-time laws with a bathtub-shaped hazard.

## Assumptions and scope
Let \(X_i\) be independent DGE counts with
\[
\Pr(X_i\le j)=(1-p^{j+1})^\alpha,\qquad j=0,1,\ldots,
\]
and let \(N\) be independent geometric on \(\{1,2,\ldots\}\) with \(\Pr(N=n)=\theta(1-\theta)^{n-1}\). Put \(X=\max_{1\le i\le N}X_i\). These assumptions imply
\[
\Pr(X\le j)=\frac{\theta (1-p^{j+1})^\alpha}{1-(1-\theta)(1-p^{j+1})^\alpha}.
\]
For \(j\ge0\), write \(s_j=\Pr(X\ge j)\), \(d_j=\Pr(X=j\mid X\ge j)=1-s_{j+1}/s_j\), and \(s_0=1\). All comparisons concern \(d_j\) at **integer** indices; continuous hazard derivatives are used only within the proof. "Bathtub" means the differences \(d_{j+1}-d_j\) change sign at most once, from negative to positive, and both signs occur. An equality at the unique boundary may create a two-element bottom plateau. The result does not address the alternative geometric-minimum construction, nongeometric random system sizes, or boundary values of the parameters.

## Proof
**1. Exact survival and a continuous embedding.** Let \(h(t)=1-(1-t)^\alpha\), \(\lambda=-\log p>0\), and define the positive function
\[
S(u)=\frac{h(e^{-u})}{\theta+(1-\theta)h(e^{-u})},\qquad u\ge0.
\]
The law above gives \(s_j=S(j\lambda)\). Indeed, this is the survival of an exponentially scaled continuous geometric-maximum generalized exponential lifetime, whose integer sampling gives the discrete UGDGE law. Its continuous hazard \(r(u)=-S'(u)/S(u)\) is strictly positive away from zero. Write \(y=1-e^{-u}\) and \(k=1-\theta\). Direct differentiation gives
\[
r(u)=\frac{\theta\alpha(1-y)y^{\alpha-1}}{(1-y^\alpha)(1-ky^\alpha)}.
\]
The sign of \(r'(u)\) equals the sign of
\[
E(y)=(\alpha-1)-\alpha y+(1+k)y^\alpha-k(1+\alpha)y^{2\alpha}+k\alpha y^{2\alpha+1}.
\]
All denominators used to obtain this expression are strictly positive for \(0<y<1\).

**2. Continuous hazard shape, independently checked.** Write
\[
E(y)=A(y)+kB(y),\quad A(y)=\alpha(1-y)+y^\alpha-1,\quad B(y)=y^\alpha[1-y^\alpha(1+\alpha(1-y))].
\]
We have \(B(y)>0\) on \((0,1)\), using \(\log y<y-1\) and \(\log(1+t)<t\). For \(\alpha>1\), convexity gives \(A(y)>0\), and for \(\alpha=1\), \(A=0\), so \(r\) increases strictly (as \(k>0\)). For \(0<\alpha<1\), concavity gives \(A(y)<0\); also \(E(0+)=\alpha-1<0\), \(E(1)=E'(1)=0\), and
\[
E(y)=\frac{\alpha}{2}\left[-(1-\alpha)+k(1+\alpha)\right](1-y)^2+O((1-y)^3)
\]
as \(y\uparrow1\). At equality \(\theta=\theta_c(\alpha)\), the quadratic term vanishes and the next term is \(2\alpha^2(\alpha-1)(1-y)^3/3<0\), so its near-endpoint sign is still negative. The displayed \(E\) is a generalized polynomial whose coefficients, after collecting equal exponents and ordering by exponent, have exactly three sign variations. The generalized Descartes rule (proved by induction using Rolle's theorem after dividing by the lowest power) bounds its positive zeros, including multiplicities, by three. Because \(y=1\) is already a double zero, there is at most one zero in \((0,1)\). Thus if \(\theta\ge 2\alpha/(1+\alpha)\), then \(E<0\) throughout \((0,1)\) and \(r\) strictly decreases. Otherwise \(E\) changes sign exactly once from negative to positive, and \(r\) has exactly one strict minimum. This verifies the needed continuous premise without assuming that a numerical plot proves uniqueness.

**3. Monotonicity survives sampling with at most one change.** Define the integrated hazard
\[
L_\lambda(x)=\int_{x\lambda}^{(x+1)\lambda}r(u)\,du
=\log\frac{S(x\lambda)}{S((x+1)\lambda)},\qquad x\ge0.
\]
Then \(d_j=1-e^{-L_\lambda(j)}\), so their adjacent comparisons have the same sign as those of \(L_\lambda(j)\). If \(r\) is monotone, so is \(L_\lambda\). If \(r\) strictly decreases up to \(u_0\) and then strictly increases, then \(L_\lambda'(x)=\lambda[r((x+1)\lambda)-r(x\lambda)]\): it is negative when both endpoints precede \(u_0\), positive when both follow it, and strictly increases across the intervening interval because its derivative there equals \(\lambda^2[r'((x+1)\lambda)-r'(x\lambda)]>0\). Thus \(L_\lambda\) is either strictly increasing on \([0,\infty)\) or decreases to a unique minimum and then increases. Sampling at integers cannot introduce an additional reversal. In the bathtub-eligible region the tail derivative is strictly positive, so the discrete sequence eventually increases. Therefore the sole decision is the sign of \(d_1-d_0\); if the first step is nonnegative, all subsequent steps are strictly positive (with the equality case only at the first step).

**4. Exact one-step discriminator.** Set \(a=h(p)\), \(b=h(p^2)\). The two initial survival probabilities are
\[
s_1=\frac{a}{\theta+(1-\theta)a},\qquad
s_2=\frac{b}{\theta+(1-\theta)b}.
\]
Consequently \(d_1-d_0=(s_1^2-s_2)/s_1\). Multiplying its numerator by positive denominators yields exactly
\[
a^2[\theta+(1-\theta)b]-b[\theta+(1-\theta)a]^2
=\theta R_{\alpha,\theta}(p).
\]
This establishes the sign criterion with no approximation.

**5. Uniqueness of the resolution threshold.** Work in \(0<\alpha<1\), \(0<\theta<\theta_c(\alpha)\), where the continuous hazard \(r\) has one minimum at \(u_0>0\). For \(\lambda>0\), define
\[
H(\lambda)=\log\frac{S(\lambda)^2}{S(2\lambda)}.
\]
Its sign equals that of \(d_1-d_0\); \(H(0+)=0\), and
\[
H'(\lambda)=2[r(2\lambda)-r(\lambda)].
\]
The bracket is negative if \(2\lambda\le u_0\) and positive if \(\lambda\ge u_0\). In \(u_0/2<\lambda<u_0\) it is strictly increasing, since \(r(2\lambda)\) rises while \(r(\lambda)\) falls. Thus \(H\) first decreases and then strictly increases, with precisely one derivative sign change. Since
\[
S(u)=\frac\alpha\theta e^{-u}(1+o(1)),\qquad u\to\infty,
\]
we have \(\lim_{\lambda\to\infty}H(\lambda)=\log(\alpha/\theta)\). If \(\theta\ge\alpha\), this limit is nonpositive; therefore \(H<0\) for every finite \(\lambda\), proving persistent discrete bathtub behavior. If \(0<\theta<\alpha\), the limit is strictly positive, and exactly one positive crossing \(\lambda_*\) follows. With \(p_*=e^{-\lambda_*}\), the signs for \(p<p_*\), \(p=p_*\), and \(p>p_*\) are respectively positive, zero, and negative. Step 4 gives the equivalent exact root equation and completes all cases.

## Verification
The included standalone `check_hazard.py` tests the explicit survival law and discriminator with 70-digit arithmetic across 378 parameter triples, compares the classification with up to 140 sampled hazards for each triple (ignoring numerically unresolvable deep-tail differences), and checks the algebraic sign identity exactly at 2,584 rational parameter triples. It also computes illustrative high-precision root brackets for \(\alpha=1/2\), \(\theta=1/10\), and exhibits both hazard shapes at \(p=1/2\) and \(p=9/10\). These finite computations do not substitute for Steps 1–5, which cover all stated real parameters and infinite sequences. Run with `python check_hazard.py` and the `mpmath` Python package.

## Relationship to prior work
Kundu and Nekoukhou (2018, arXiv:1802.06715), Sections 2–3, define the discrete geometric-maximum family and its exact survival, a reliability motivation, and a hazard transformation, but do not classify the complete discrete hazard sequence or the unique dependence on \(p\). Ristić and Kundu (2015), Section 3, classify the continuous Marshall–Olkin generalized exponential hazard under a reciprocal parameterization; that result supplies essential background for the continuous stage, not the lattice sampling threshold or the three-region resolution diagram. The present claim concerns precisely how integer sampling can erase an underlying bathtub and the uniqueness of its recovery threshold, not a newly invented distribution or the already-established continuous hazard phases. General surveys of discrete analogues discuss discretization techniques without the stated UGDGE-specific threshold.

## Limitations
The result is for a geometric **maximum**, independent parent counts, positive interior shape and probability parameters, and a fixed equal-width integer lattice. The continuous hazard-shape phase is known from earlier work; the claimed increment is the discrete hazard's complete resolution-sensitive classification. No new estimator or inference power guarantee is asserted. The illustrative threshold decimal is numerical, whereas its existence, uniqueness and exact root equation are analytic. An independent historical-priority review has not been performed; closely related generalized exponential-geometric constructions remain a residual search risk.

## References
1. D. Kundu and V. Nekoukhou, *Univariate and Bivariate Geometric Discrete Generalized Exponential Distributions*, first public arXiv submission 2018-02-16, https://arxiv.org/abs/1802.06715 ; journal DOI https://doi.org/10.1080/15598608.2018.1441082 .
2. M. M. Ristić and D. Kundu, *Marshall-Olkin generalized exponential distribution*, METRON 73 (2015), 317–333, https://doi.org/10.1007/s40300-014-0056-x ; lawful full text https://home.iitk.ac.in/~kundu/moged-rev-3.pdf .
3. A. Barbiero, *Generating discrete analogues of continuous probability distributions: A survey of methods and constructions*, 2015, https://link.springer.com/article/10.1186/s40488-015-0028-6 .
