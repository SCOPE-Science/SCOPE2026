# Exact two-cycle stability strip across the rational–logistic interpolation

## Finding

For \(0\le\lambda\le1\), let
\[
F_{\mu,\lambda}(x)=\frac{\mu x(1-x)}{1+\lambda x},\qquad x\in[0,1],\qquad
1<\mu\le\mu_{\max}(\lambda)=(1+\sqrt{1+\lambda})^2.
\]
Define
\[
\begin{aligned}
\mu_1(\lambda)&=\frac{3+\lambda+\sqrt{(1+\lambda)(9+\lambda)}}2,\\
H(\mu,\lambda)&=\mu^2-(3+\lambda)\mu-\lambda,\\
R(\mu,\lambda)&=\frac{(\mu-\lambda)(\mu+1)H(\mu,\lambda)}{\mu^2(1+\lambda)}.
\end{aligned}
\]
There is no primitive two-cycle for \(1<\mu\le\mu_1(\lambda)\). For \(\mu_1(\lambda)<\mu\le\mu_{\max}(\lambda)\) there is exactly one, with points
\[
u_\pm=\frac{\mu+1}{2\mu}\pm\frac{1}{2\mu}\sqrt{\frac{(\mu+1)H(\mu,\lambda)}{\mu-\lambda}}
\]
and multiplier \(F'_{\mu,\lambda}(u_-)F'_{\mu,\lambda}(u_+)=1-R(\mu,\lambda)\).

For each \(\lambda\), the equation \(R(\mu,\lambda)=2\) has exactly one solution \(\mu_2(\lambda)\in(\mu_1(\lambda),\mu_{\max}(\lambda))\). The cycle is hyperbolically attracting for \(\mu_1<\mu<\mu_2\), has multiplier \(-1\) at \(\mu_2\), and is hyperbolically repelling for \(\mu_2<\mu\le\mu_{\max}\). The threshold \(\mu_2\) is strictly increasing on \([0,1]\). The known endpoint values are \(\mu_2(0)=1+\sqrt6\) and \(\mu_2(1)=1+\sqrt2+\sqrt{4+2\sqrt2}\) [3,4]. The latter is the unique root above \(2+\sqrt5\) of \(\mu^4-4\mu^3-6\mu^2+4\mu+1=0\).

At fixed \(\lambda\), as \(\mu\downarrow\mu_1(\lambda)\) from above,
\[
u_+-u_-=\sqrt{\frac{(\mu_1+1)(2\mu_1-3-\lambda)}{\mu_1^2(\mu_1-\lambda)}}\,\sqrt{\mu-\mu_1}
 + O((\mu-\mu_1)^{3/2}),
\]
where \(\mu_1=\mu_1(\lambda)\).

## Assumptions and scope

A primitive two-cycle consists of two distinct points in \([0,1]\) swapped by the map. Hyperbolic attraction and repulsion mean that the absolute value of the product derivative is strictly less than or greater than one, respectively. We classify only the primitive two-cycle and its local hyperbolicity; multiplier \(-1\) by itself does not prove a period-four bifurcation. The upper bound on \(\mu\) is sharp for forward invariance of the full interval: the maximum of \(x(1-x)/(1+\lambda x)\), at \(x=1/(1+\sqrt{1+\lambda})\), is \((1+\sqrt{1+\lambda})^{-2}\).

## Proof

**Cycle points.** Write \(x,y\) for a candidate pair and set \(S=x+y\), \(P=xy\). The swap equations are
\[
y+\lambda P=\mu x(1-x),\qquad x+\lambda P=\mu y(1-y).
\]
Their difference for \(x\ne y\) gives \(S=(\mu+1)/\mu\); their sum then gives \(P=(\mu+1)/[\mu(\mu-\lambda)]\). Conversely, these values of \(S,P\) imply both the sum and the difference of the swap equations, so two distinct roots lying in the interval give a cycle. The quadratic with roots \(x,y\), cleared of denominators, is
\[
Q(x)=\mu(\mu-\lambda)x^2-(\mu+1)(\mu-\lambda)x+(\mu+1).
\]
Its discriminant is \((\mu-\lambda)(\mu+1)H\), with \(\mu-\lambda>0\). For \(\mu>1\), \(H\) is negative below \(\mu_1\) and positive above; at equality the root is double and gives no primitive pair. When \(H>0\), the vertex is at \(S/2\in(0,1)\) with negative value, and \(Q(0)=\mu+1>0\), \(Q(1)=1+\lambda>0\). Thus both roots are in \((0,1)\), give the unique cycle, and are the stated \(u_\pm\).

**Multiplier.** At an orbit pair, differentiation of \((1+\lambda x)F(x)=\mu x(1-x)\) gives \((1+\lambda x)F'(x)=\mu(1-2x)-\lambda y\). Set \(\Delta=y-x\). Since \(\mu S=\mu+1\), the two derivative numerators are \(\mu\Delta-(1+\lambda y)\) and \(-\mu\Delta-(1+\lambda x)\). Their product divided by the denominator gives
\[
F'(x)F'(y)=1-\frac{\mu(\mu-\lambda)\Delta^2}{(1+\lambda x)(1+\lambda y)}.
\]
Here \((1+\lambda x)(1+\lambda y)=1+\lambda S+\lambda^2 P=\mu(1+\lambda)/(\mu-\lambda)\), and \(\Delta^2=(\mu+1)H/[\mu^2(\mu-\lambda)]\), giving \(1-R\).

**Stability threshold.** For \(\mu>\mu_1\), the three positive numerator factors of
\[
R=\frac{(1-\lambda/\mu)(\mu+1)(\mu-3-\lambda-\lambda/\mu)}{1+\lambda}
\]
are nondecreasing in \(\mu\), and the last two are strictly increasing. At \(\mu_1\), \(R=0\). At \(\mu_{\max}\), with \(t=\sqrt{1+\lambda}\), one has \(\mu_{\max}-\lambda=2(t+1)\) and \(H=2t^2(t+1)>0\), so \(\mu_{\max}>\mu_1\) and
\[
R(\mu_{\max},\lambda)=\frac{4(t^2+2t+2)}{(t+1)^2}>2.
\]
There is exactly one crossing of \(R=2\), and the multiplier gives the stated stability strip.

For fixed \(\mu\) with \(H>0\), \(R\) decreases strictly as \(\lambda\) increases within that region: \(\mu-\lambda\) and \(H=\mu^2-3\mu-\lambda(\mu+1)\) decrease and \(1+\lambda\) increases. For \(\lambda'<\lambda''\), put \(M=\mu_2(\lambda')\). If \(M\le\mu_1(\lambda'')\), the desired strict inequality is immediate. Otherwise \(M<\mu_{\max}(\lambda'')\) since \(\mu_{\max}\) is increasing, and \(R(M,\lambda'')<R(M,\lambda')=2\), proving \(M<\mu_2(\lambda'')\). At \(\lambda=0\), \(R=(\mu+1)(\mu-3)\), giving \(1+\sqrt6\). At \(\lambda=1\), clearing denominators gives the displayed quartic. Dividing it by \(\mu^2\) and writing \(s=\mu-1/\mu\) gives \(s^2-4s-4=0\). The admissible solution has \(s=2+2\sqrt2\), since \(\mu>2+\sqrt5\); solving for \(\mu\) gives \(1+\sqrt2+\sqrt{4+2\sqrt2}\).

**Opening law.** The root \(\mu_1\) of \(H\) is simple, with derivative \(2\mu_1-3-\lambda>0\). In \(\Delta^2\), the remaining factor is positive and analytic at \(\mu_1\). Taking the square root of the resulting first-order expansion yields the coefficient and the stated remainder.

## Verification

The accompanying `verify.py` uses SymPy to check the exact second-iterate factorization, discriminant, endpoint values of \(Q\), derivative product, \(R(\mu_{\max},\lambda)\), and endpoint quartic. Its seven interpolation parameters and 21 cycle-point pairs provide finite diagnostic checks, not proofs for all parameters. The endpoint radical follows from the quartic reduction above without relying on a decimal approximation.

## Relationship to prior work

Conejero, Lizama and Quijada [1] introduced the interpolation and established the exact first fixed-point stability boundary \(\mu_1(\lambda)\) in Section 2. Section 7 estimated the period-two-to-period-four boundary numerically as approximately \(3.45,3.99,4.53,5.03\) for \(\lambda=0,0.33,0.67,1\), respectively. Kumar and collaborators [2] also reported numerical intervals at the rational endpoint. Both endpoints of the exact secondary threshold are prior results: the classical logistic threshold [3], and the exact rational endpoint classification, multiplier, and secondary threshold in [4]. The latter also proves a local period-four birth at that endpoint, which is not claimed here. The contribution is the uniform parameter classification, in particular the exact multiplier, strictly increasing secondary threshold and opening coefficient for the interior interpolation \(0<\lambda<1\).

## Limitations

The argument does not settle global convergence, higher-period orbits, nonlinear stability at multiplier \(-1\), or parameters beyond the interval-invariance range. Priority of the interior interpolation formulas remains subject to possible coverage by unlocated general rational-map results.

## References

1. J. A. Conejero, C. Lizama and D. Quijada, *Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps*, Mathematics **13** (2025), 518. https://doi.org/10.3390/math13030518
2. A. Kumar, J. Alzabut, S. Kumari, M. Rani and R. Chugh, *Dynamical properties of a novel one dimensional chaotic map*, Mathematical Biosciences and Engineering **19** (2022), 2489–2505. https://doi.org/10.3934/mbe.2022115
3. R. M. May, *Simple mathematical models with very complicated dynamics*, Nature **261** (1976), 459–467. https://doi.org/10.1038/261459a0
4. *Exact second-flip boundary and local attracting four-cycle in a rational unimodal map*, record `c832b5af1161`, 2026-11-02. https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-exact-second-flip-boundary-and-local-attracting-four-cycle-in-a--c832b5af1161
