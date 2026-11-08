# A sharp periodic-delay instability boundary despite stable frozen IMEX recurrences

## Finding

For the scalar second-order IMEX method in Rodríguez-Gutiérrez and Martín-Vaquero [1], the period-three, mesh-aligned delay schedule \(m_j=(1,2,3)\) for \(j\equiv(0,1,2)\pmod 3\) has an exact numerical stability transition at
\[
\mu_c=-\frac{10773}{13315}\approx-0.809087495306046.
\]
With fixed \(\beta_0=4/5\), grid step \(h=1\), local decay coefficient \(-5\), and feedback coefficient \(5\mu\), \(-1<\mu<1\), the period-three numerical solution decays exponentially for every valid discrete starting history **if and only if** \(\mu>\mu_c\). At \(\mu=\mu_c\), there are nondecaying numerical modes; below it, some numerical solutions grow exponentially. For example, \(\mu=-9/10\) yields a real period-three multiplier below \(-1\). This occurs despite exponential stability of the exact variable-delay DDE and of every frozen integer-delay numerical recurrence throughout \(-1<\mu<1\).

## Assumptions and scope

Consider \(y'(t)=-5y(t)+5\mu y(t-\tau(t))\), \(-1<\mu<1\), and a bounded continuous delay \(1\le\tau(t)\le3\) whose values at nonnegative integers are \(\tau(j)=m_j\), with \(m_j=1\) if \(j\equiv0\), \(m_j=2\) if \(j\equiv1\), and \(m_j=3\) if \(j\equiv2\pmod3\). A smooth such delay exists by connecting successive integer samples using a flat smooth monotone transition, taking values only between its endpoints. The same discrete recurrence is meaningful directly for this specified indexed schedule, without making any off-grid interpolation.

Use equation (29) of [1] with parameter \(\beta_0=4/5\) and \(h=1\), applying the delayed term *at each of its own three stages* \(j-2,j-1,j\), as in Section 4.3 of [1]. Thus the index \(m_j\) is evaluated at stage \(j\), not held fixed across each two-step update. Starting values comprise a discrete history and the two standard starting approximations. Stability means every such solution of the homogeneous recurrence tends exponentially to zero; instability means that at least one admissible real starting history has exponentially growing errors. This is a statement for this exact fixed grid and three-phase delay schedule, not a uniform result over arbitrary delays or steps.

## Proof

**1. The underlying continuous problem is uniformly stable.** For \(-1<\mu<1\), the upper Dini derivative of \(|y(t)|\) obeys
\[
D^+|y(t)|\le-5|y(t)|+5|\mu|\max_{t-3\le s\le t}|y(s)|.
\]
Choose \(\gamma>0\) small enough that \(5-\gamma>5|\mu|e^{3\gamma}\), possible because \(|\mu|<1\). Applying the classical Halanay comparison argument to \(e^{\gamma t}|y(t)|\) shows exponential decay for all continuous histories. This uses only the delay bound \(0\le\tau(t)\le3\), not periodicity or smoothness. In particular, it remains valid for the smooth delay with the prescribed mesh samples.

**2. Exact stage-dependent recurrence.** Setting \(a=5\), \(b=4/5\) and \(u=\mu\), the method is
\[
(1+a)y_j=(1-b)(2+a)y_{j-1}+(2b-1-ab)y_{j-2}
+au\bigl(y_{j-m_j}-(1-b)y_{j-1-m_{j-1}}+b y_{j-2-m_{j-2}}\bigr).
\]
On the state \(X_j=(y_j,y_{j-1},y_{j-2},y_{j-3},y_{j-4})^\mathsf T\), define the one-stage companion maps \(X_j=W_{j\bmod3}(u)X_{j-1}\). The first row of \(W_j\) is obtained by placing the coefficients \((1-b)(2+a)/(1+a)\), \((2b-1-ab)/(1+a)\), \(au/(1+a)\), \(-au(1-b)/(1+a)\), and \(aub/(1+a)\) at lags \(1,2,m_j,1+m_{j-1},2+m_{j-2}\), summing coefficients if lags coincide; its other rows shift the history. The maximal lag is five. Direct exact multiplication gives the three-stage monodromy \(P(u)=W_2(u)W_1(u)W_0(u)\) and
\[
\det(zI-P(u))=\frac{z^2}{27000}\,p_u(z),
\quad p_u(z)=27000z^3+(10367-28675u)z^2+(4913-7825u)z-5780u.
\]
The two zero multipliers are harmless, and stability is controlled by the cubic.

**3. Sharp cubic Schur test.** Divide \(p_u\) by \(27000\) and write \(z^3+Az^2+Bz+C\), with
\[
A=\frac{10367-28675u}{27000},\quad B=\frac{4913-7825u}{27000},\quad C=-\frac{5780u}{27000}.
\]
The elementary Schur reduction \((p(z)-Cz^3p(1/z))/z\), after normalization, says its three roots lie in the open unit disk exactly when
\[
|C|<1,\quad p_u(1)>0,\quad -p_u(-1)>0,\quad 1-C^2\pm(B-AC)>0.
\]
For \(-1<u<1\), \(|C|<1\) and \(p_u(1)=42280(1-u)>0\). The last two inequalities reduce to
\[
\frac{43082550-7567687u-9957495u^2}{36450000}>0,\qquad
\frac{29817450+7567687u+6616655u^2}{36450000}>0.
\]
The first numerator exceeds \(43082550-7567687-9957495>0\); the second exceeds \(29817450-7567687>0\), uniformly for \(-1<u<1\). Finally,
\[
-p_u(-1)=21546+26630u=2(10773+13315u).
\]
Thus the Schur criterion holds exactly for \(u>\mu_c\). For \(u<\mu_c\), \(p_u(-1)>0\) while \(p_u(z)\to-\infty\) as \(z\to-\infty\), so some real root lies strictly below \(-1\). At equality,
\[
p_{\mu_c}(z)=\frac4{2663}(z+1)(17975250z^2+4372369z+3113397),
\]
whose quadratic roots have modulus \(\sqrt{3113397/17975250}<1\); \(-1\) is simple. Nonzero Floquet eigenvectors give admissible histories because any nonzero-eigenvalue eigenvector of the period matrix is in the image of the stage map that finishes its period; the two freely specified initial values and past mesh samples can be chosen to realize it. Therefore the three cases above genuinely describe numerical trajectories, not merely a formal polynomial.

**4. Every frozen recurrence remains stable.** For any constant integer delay \(m\ge1\), the characteristic equation is
\[
z^m(\rho(z)+5\sigma(z))-5u\sigma(z)=0,
\quad \rho(z)=z^2-\frac25 z-\frac35,
\quad \sigma(z)=z^2-\frac15 z+\frac45.
\]
The quadratic \(\rho+5\sigma=6z^2-7z/5+17/5\) has both roots with modulus \(\sqrt{17/30}<1\). On \(|z|=1\),
\[
\operatorname{Re}(\rho(z)\overline{\sigma(z)})=\frac{|z-1|^4}{10}\ge0,
\]
so \(|\rho+5\sigma|\ge5|\sigma|>5|u\sigma|\) for \(|u|<1\) (and \(\sigma\ne0\) on the circle). Rouché's theorem therefore puts all \(m+2\) frozen roots strictly inside the unit disk. This independently proves the relevant fixed-delay guarantee instead of assuming frozen stability implies switching stability.

## Verification

The accompanying `verify.py` reconstructs the three companion matrices from the recurrence, multiplies the exact symbolic monodromy, verifies the cubic polynomial, the Schur polynomials and the threshold factorization, and checks frozen-delay companion polynomials for delays one through three. It uses exact rational/symbolic arithmetic and prints `CHECKS_OK`. Run `python verify.py` with Python 3.9+ and SymPy 1.10+. The analytic inequalities and the Rouché argument above prove the quantified claim; finite sample checks do not replace those arguments.

For \(u=-9/10\) the monodromy polynomial is
\[
\det(zI-P)=\frac{z^2}{54000}(54000z^3+72349z^2+23911z+10404),
\]
and its value at \(z=-1\) is exactly \(269/3000>0\), displaying the unstable multiplier without numerical root finding.

## Relationship to prior work

Rodríguez-Gutiérrez and Martín-Vaquero [1] derive the IMEX family and prove the frozen grid-aligned stability disk; their Section 4.3 explicitly distinguishes variable-delay products from frozen spectra and supplies a sufficient common-Lyapunov condition. The new part here is the **exact parameter-complete Floquet classification** for a natural three-phase delay pattern, including an explicit rigorous instability on an exponentially stable continuous test equation and a stability boundary inside the frozen disk. Koto [2] and Watanabe–Roth [3] treat important IMEX/fixed-delay stability contexts but are not cited as establishing the present switching threshold. Polynomial Schur tests, Rouché's theorem, and the continuous Halanay bound are classical tools, not new claims.

## Limitations

Only this scalar equation, this two-step parameter, \(h=1\), exact grid-aligned three-phase delays, and real \(-1<u<1\) are classified. The result does not imply failure at sufficiently small \(h\) with one fixed physical delay function, nor instability for every history, nor a result for arbitrary switching, matrix coefficients, nonlinear delays, or non-grid-aligned interpolation. The continuous exact solution is exponentially stable despite numerical divergence; this is a fixed-mesh asymptotic phenomenon. Independent external validation and historical completeness have not been established.

## References

[1] J. Rodríguez-Gutiérrez and J. Martín-Vaquero, *On the stability of second-order methods for DDEs and PDDEs*, arXiv:2610.33780v1, first public 2026-10-24, https://arxiv.org/html/2610.33780v1, especially Eq. (29), Thm. 3.8, Sections 4.2–4.3.

[2] T. Koto, *Stability of implicit-explicit linear multistep methods for ordinary and delay differential equations*, Frontiers of Mathematics in China **4** (2009), 113–129, DOI: 10.1007/s11464-009-0005-9.

[3] D. S. Watanabe and M. G. Roth, *The stability of difference formulas for delay differential equations*, SIAM Journal on Numerical Analysis **22** (1985), 132–145, DOI: 10.1137/0722010.
