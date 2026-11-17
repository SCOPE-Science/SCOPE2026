# Exact two-cycle stability strip across the rational logistic interpolation

## Finding

The logistic-to-rational interpolation of Conejero, Lizama and Quijada admits an exact, all-parameter classification of its primitive two-cycle, including a unique, strictly increasing secondary stability threshold. For \(0\leq\lambda\leq1\), consider
\[
F_{\mu,\lambda}(x)=\frac{\mu x(1-x)}{1+\lambda x},\qquad 0\leq x\leq1,
\]
with \(1<\mu\leq\mu_{\max}(\lambda)=(1+\sqrt{1+\lambda})^2\). Define
\[
\begin{aligned}
\mu_1(\lambda)&=\frac{3+\lambda+\sqrt{(1+\lambda)(9+\lambda)}}2,\\
H(\mu,\lambda)&=\mu^2-(3+\lambda)\mu-\lambda,\\
R(\mu,\lambda)&=\frac{(\mu-\lambda)(\mu+1)H(\mu,\lambda)}{\mu^2(1+\lambda)}.
\end{aligned}
\]
There is no primitive two-cycle in \([0,1]\) for \(1<\mu\leq\mu_1(\lambda)\). For \(\mu_1(\lambda)<\mu\leq\mu_{\max}(\lambda)\), exactly one such cycle exists, with distinct points
\[
u_\pm=\frac{\mu+1}{2\mu}\pm\frac{1}{2\mu}\sqrt{\frac{(\mu+1)H(\mu,\lambda)}{\mu-\lambda}}.
\]
Its two-step multiplier is exactly
\[
F'_{\mu,\lambda}(u_-)F'_{\mu,\lambda}(u_+)=1-R(\mu,\lambda).
\]
For each \(\lambda\), precisely one \(\mu_2(\lambda)\in(\mu_1(\lambda),\mu_{\max}(\lambda))\) solves
\[
(\mu-\lambda)(\mu+1)[\mu^2-(3+\lambda)\mu-\lambda]=2\mu^2(1+\lambda).
\]
The cycle is hyperbolically attracting when \(\mu_1<\mu<\mu_2\), has multiplier \(-1\) at \(\mu_2\), and is hyperbolically repelling for \(\mu_2<\mu\leq\mu_{\max}\). The threshold \(\mu_2(\lambda)\) is **strictly increasing** on \([0,1]\). Its endpoints are \(\mu_2(0)=1+\sqrt6\) (the classical logistic case) and \(\mu_2(1)=5.027339492125706\ldots\), the unique root above \(2+\sqrt5\) of \(\mu^4-4\mu^3-6\mu^2+4\mu+1=0\).

As \(\mu\downarrow\mu_1(\lambda)\) with fixed \(\lambda\), the cycle is born with the explicit square-root opening
\[
u_+-u_-=C(\lambda)\sqrt{\mu-\mu_1(\lambda)}+O\bigl((\mu-\mu_1(\lambda))^{3/2}\bigr),
\]
where
\[
C(\lambda)=\sqrt{\frac{(\mu_1+1)(2\mu_1-3-\lambda)}{\mu_1^2(\mu_1-\lambda)}}
\]
and here \(\mu_1\) denotes \(\mu_1(\lambda)\).

## Assumptions and scope

All statements concern the real interval map with \(\lambda\in[0,1]\) and \(1<\mu\leq(1+\sqrt{1+\lambda})^2\), so that \(F_{\mu,\lambda}\) maps \([0,1]\) into itself. A *primitive two-cycle* is an unordered pair of different points \(\{u_-,u_+\}\subset[0,1]\) such that \(F(u_-)=u_+\) and \(F(u_+)=u_-\). *Hyperbolically attracting* means the absolute value of the product derivative is strictly below one, and *hyperbolically repelling* means strictly greater than one. The theorem classifies this orbit and its **local** stability, not global basins, all higher periods, or the existence of period-four cycles at the secondary neutral threshold.

The restriction on \(\mu\) is sharp for full-interval invariance. Indeed, \(x(1-x)/(1+\lambda x)\) attains its maximum \((1+\sqrt{1+\lambda})^{-2}\) in \([0,1]\).

## Proof

**1. Complete two-cycle factorization.** Direct composition, with a denominator positive on the specified interval, gives the exact identity
\[
F_{\mu,\lambda}^{\circ 2}(x)-x=-\frac{x[(\mu+\lambda)x-(\mu-1)]Q_{\mu,\lambda}(x)}{(1+\lambda x)[1+\lambda x+\lambda\mu x(1-x)]},
\]
where
\[
Q_{\mu,\lambda}(x)=\mu(\mu-\lambda)x^2-(\mu+1)(\mu-\lambda)x+(\mu+1).
\]
The linear factor corresponds to the nonzero fixed point \(x_*=(\mu-1)/(\mu+\lambda)\), and \(x=0\) is the other fixed point. The discriminant of \(Q\) equals
\[
(\mu-\lambda)(\mu+1)H(\mu,\lambda).
\]
Since \(\mu>1\geq\lambda\), the first two factors are positive. The polynomial \(H\) has exactly one positive zero, \(\mu_1(\lambda)\), and is negative before and positive after that zero. At \(\mu=\mu_1\), the double root of \(Q\) equals \(x_*\), so it produces no primitive two-cycle.

For \(\mu>\mu_1\), \(Q\) is strictly convex, has two real roots, and has its vertex at \((\mu+1)/(2\mu)\in(0,1)\). Both endpoint values are positive: \(Q(0)=\mu+1\) and \(Q(1)=1+\lambda\). Since its vertex value is negative, both roots belong to \((0,1)\). Neither is fixed; hence they are interchanged by \(F\) and constitute exactly one primitive two-cycle. The quadratic formula yields the stated \(u_\pm\).

**2. Multiplier identity.** Differentiation gives
\[
F'_{\mu,\lambda}(x)=\frac{\mu(1-2x-\lambda x^2)}{(1+\lambda x)^2}.
\]
Vieta's formulas for the two roots give
\[
u_-+u_+=\frac{\mu+1}{\mu},\qquad
u_-u_+=\frac{\mu+1}{\mu(\mu-\lambda)}.
\]
Substituting these two symmetric expressions into the derivative product and simplifying yields the exact multiplier \(1-R\). In the positive-discriminant range \(R>0\), so the multiplier is always less than one.

**3. Existence, uniqueness and location of the secondary boundary.** Rewriting gives
\[
R(\mu,\lambda)=\frac{(1-\lambda/\mu)(\mu+1)(\mu-3-\lambda-\lambda/\mu)}{1+\lambda}.
\]
On \(\mu>\mu_1(\lambda)\), all three numerator factors are positive and nondecreasing in \(\mu\), with the last two strictly increasing. Therefore \(R\) increases strictly from zero. Put \(t=\sqrt{1+\lambda}\in[1,\sqrt2]\). At the invariance endpoint \(\mu=(1+t)^2\), exact substitution gives
\[
R(\mu_{\max},\lambda)=\frac{4(t^2+2t+2)}{(t+1)^2}>2.
\]
The intermediate value theorem and strict monotonicity give a unique \(\mu_2\) with \(R=2\), and the claimed local stability intervals follow from \(|1-R|<1\) exactly when \(0<R<2\).

**4. Strict shift with interpolation.** For fixed \(\mu\) in the common positive-discriminant domain, the product representation \(R=(\mu-\lambda)(\mu+1)H/[\mu^2(1+\lambda)]\) shows that \(R\) decreases strictly with \(\lambda\): the factors \(\mu-\lambda\) and \(H=\mu^2-3\mu-\lambda(\mu+1)\) decrease, while \(1+\lambda\) increases. The first threshold \(\mu_1\) itself increases with \(\lambda\). Thus the unique \(R=2\) solution \(\mu_2\) increases strictly with \(\lambda\), including the case where a lower-parameter \(\mu_2\) falls below the higher-parameter \(\mu_1\). The endpoint substitutions produce \(\mu_2(0)=1+\sqrt6\) and the stated quartic at \(\lambda=1\).

**5. Opening law.** For fixed \(\lambda\), a Taylor expansion at the simple positive root of \(H\) gives
\[
H(\mu,\lambda)=(2\mu_1-3-\lambda)(\mu-\mu_1)+O((\mu-\mu_1)^2).
\]
The difference of the explicit roots is \(\mu^{-1}\sqrt{(\mu+1)H/(\mu-\lambda)}\). Taking the leading coefficient yields the positive \(C(\lambda)\) and the stated remainder.

## Verification

The self-contained `verify.py` uses SymPy to check the entire composition factorization, quadratic discriminant, endpoint values, symmetric derivative multiplier, endpoint comparison, and one-parameter quartic. It additionally checks seven interpolation parameters and 21 explicit numerical cycle points, comparing the two-step product with \(1-R\). The outputs are diagnostic complements to the universal algebraic proof, not its substitute. Run with Python 3 and SymPy by executing `python verify.py` in the directory containing this document and the script.

## Relationship to prior work

Conejero, Lizama and Quijada (2025) introduced this interpolation and established the first fixed-point stability boundary \(\mu_1(\lambda)\). Their Sections 3–7 provide graphical and numerical estimates for the period-two-to-period-four transition at selected \(\lambda\), approximately \(3.45,3.99,4.53,5.03\) when \(\lambda=0,0.33,0.67,1\), respectively. The result here replaces those samples by a unique exact equation valid for the whole interpolation interval and supplies a complete primitive-two-cycle census, its explicit multiplier and its monotonic parameter dependence. The logistic endpoint \(\mu_2(0)=1+\sqrt6\) and square-root onset in the classical logistic map are established background, not new claims. Kumar and collaborators (2022) had investigated the \(\lambda=1\) endpoint and numerically located the higher-period transition; their analysis does not give the all-interpolation exact equation.

## Limitations

This is a local periodic-orbit stability statement, not global convergence or a classification of all possible attractors. It does not prove a nondegenerate period-four bifurcation at \(\mu_2\), nor address parameter values above the interval-invariance endpoint. The algebraic calculation uses the already known family and standard one-dimensional multipliers. Historical priority remains subject to possible coverage by unlocated general rational-map results; independent scientific verification has not been performed.

## References

1. J. A. Conejero, C. Lizama and D. Quijada, *Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps*, Mathematics **13** (2025), 518. Published 2025-02-04. DOI: 10.3390/math13030518. https://www.mdpi.com/2227-7390/13/3/518
2. A. Kumar, J. Alzabut, S. Kumari, M. Rani and R. Chugh, *Dynamical properties of a novel one dimensional chaotic map*, Mathematical Biosciences and Engineering **19** (2022), 2489–2505. Published 2022-01-07. DOI: 10.3934/mbe.2022115. https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf
3. R. M. May, *Simple mathematical models with very complicated dynamics*, Nature **261** (1976), 459–467. DOI: 10.1038/261459a0 (classical logistic-map background).
