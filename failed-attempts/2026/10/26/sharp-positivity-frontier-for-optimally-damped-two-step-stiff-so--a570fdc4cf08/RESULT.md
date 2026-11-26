# Sharp positivity frontier for optimally damped two-step stiff solvers

## Finding

Jensen, Lóczi and Ketcheson's optimal second-order, two-step, A-stable \(L(\kappa)\)-stable family (Corollary 4.2, Eq. (25) of [1]) has an exact *all-iterate scalar positivity threshold* when initialized by one backward-Euler step. For every \(0\le\kappa<1\), \(z=\lambda h>0\), and \(y_0=1\), \(y_1=(1+z)^{-1}\), its iterates on \(y'=-\lambda y\), \(\lambda>0\), satisfy \(y_n\ge0\) for all integers \(n\ge0\) **if and only if**

\[
0<z\le R(\kappa),\qquad
R(\kappa)=\begin{cases}
\dfrac{1+\kappa}{2(1-\kappa)},&0\le\kappa\le\tfrac12,\\[4pt]
\dfrac{1-\kappa^2}{\kappa},&\tfrac12\le\kappa<1.
\end{cases}
\]

The threshold is inclusive. The *unique* choice of stiff-damping parameter maximizing the scalar positivity radius is \(\kappa=1/2\), with radius \(R(1/2)=3/2\). At that endpoint \(z=3/2\), the recurrence produces \(y_n=0\) for every \(n\ge2\). For \(\kappa=0\), the classical backward-Euler-started BDF2 boundary \(z=1/2\) is recovered; that endpoint case is not claimed as a new result.

## Assumptions and scope

Let \(\kappa\in[0,1)\). The family is the *constant-step* method whose coefficients are

\[
(\alpha_0,\alpha_1,\alpha_2)=\left(\frac{3\kappa-1}{\kappa-3},\frac{4(1-\kappa)}{\kappa-3},1\right),
\quad
(\beta_0,\beta_1,\beta_2)=\left(\frac{2\kappa^2}{D},\frac{4\kappa}{D},\frac2D\right),
\quad D=3+2\kappa-\kappa^2.
\]

It uses \(\sum_{j=0}^2\alpha_j y_{n+j}=h\sum_{j=0}^2\beta_j f(y_{n+j})\), and one backward-Euler step from the strictly positive scalar datum \(y_0=1\) to initialize the second-order recurrence. Scaling of the initial datum by any positive constant preserves the result. Only this scalar decay equation, this specified starter, and exact arithmetic are considered. In particular, the result does not claim unconditional positivity for general positive ODE systems.

Set \(d=D+2z>0\) and \(q=(1+z)^{-1}>0\). The induced recurrence is

\[
y_{n+2}=B y_{n+1}-C y_n,\quad
B=\frac{4(1-\kappa^2-\kappa z)}d,\qquad
C=\frac{(1-3\kappa)(1+\kappa)+2\kappa^2z}d,
\quad y_0=1,\ y_1=q.
\]

The claim concerns the entire infinite sequence of iterates, not a finite-horizon computation.

## Proof

**1. Recurrence and characteristic identities.** Substitute the coefficients above and \(f(y)=-\lambda y\) into the multistep formula. Since \(D=(3-\kappa)(1+\kappa)\), clearing its positive denominator gives precisely \(B,C\). Let \(p(t)=t^2-Bt+C\). Direct expansion establishes the three identities

\[
\begin{aligned}
\Delta:=B^2-4C
&=\frac{4(1+\kappa)^3[(1+\kappa)-2(1-\kappa)z]}{d^2},\\
p(q)d(1+z)^2&=z^2[2\kappa^2z+(1+\kappa)^2]>0,\\
(2q-B)d(1+z)&=2[2\kappa^2z+\kappa^2+2\kappa z^2+2\kappa z+2\kappa+1]>0.
\end{aligned}
\]

These hold for all \(0\le\kappa<1\), \(z>0\). In particular, if \(\Delta\ge0\), then \(q\) is strictly larger than the greater real characteristic root \(r_+\): the second and third identities give \(p(q)>0\) and \(q>B/2\), excluding both the interval between the roots and the interval below the smaller root.

**2. Positivity below and at the threshold for \(\kappa\le1/2\).** In this range \(R(\kappa)=(1+\kappa)/(2(1-\kappa))\). For \(0<z\le R(\kappa)\), the displayed discriminant is nonnegative. Furthermore \(B\ge0\), since for \(\kappa>0\), the zero of its numerator is \((1-\kappa^2)/\kappa\ge R(\kappa)\); for \(\kappa=0\), \(B>0\) everywhere. If \(C\le0\), the recurrence \(y_{n+2}=By_{n+1}+(-C)y_n\) immediately preserves nonnegativity.

If \(C>0\), both characteristic roots are real and nonnegative because \(B\ge0\), \(C>0\). When they are distinct, \(q>r_+\ge r_-\ge0\), so

\[
y_n=r_+^n+\frac{q-r_+}{r_+-r_-}(r_+^n-r_-^n)\ge0.
\]

For a repeated root \(r=B/2>0\), the recurrence instead yields

\[
y_n=r^n\left[1+n\left(\frac qr-1\right)\right]>0.
\]

At the only possible \(B=C=0\) endpoint, \((\kappa,z)=(1/2,3/2)\), the recurrence gives \(y_0=1\), \(y_1=2/5\), and \(y_n=0\) for all \(n\ge2\). This covers every boundary case.

**3. Positivity below and at the threshold for \(\kappa>1/2\).** Now \(R(\kappa)=(1-\kappa^2)/\kappa\), where \(B=0\). For \(0<z\le R(\kappa)\), \(B\ge0\). The numerator of \(C\) is increasing with \(z\), and its value at \(R(\kappa)\), after division by \(d\), is

\[
C\bigl(\kappa,R(\kappa)\bigr)=\frac{\kappa(2\kappa-1)}{\kappa-2}<0.
\]

Therefore \(C<0\) throughout the range. Induction in the recurrence proves that all iterates are strictly positive, including the \(B=0\) endpoint.

**4. Failure above the threshold for \(\kappa\le1/2\).** If \(z>R(\kappa)\), then \(\Delta<0\). Let the complex characteristic roots be \(\rho e^{\pm i\theta}\), with \(\rho>0\) and \(0<\theta<\pi\). Every nonzero real solution has

\[
y_n=\rho^n\{A\cos(n\theta)+T\sin(n\theta)\},\qquad (A,T)\ne(0,0).
\]

Such a trigonometric sequence cannot be nonnegative for all nonnegative integers. If \(\theta/(2\pi)\) is irrational, the nonnegative orbit is dense on the circle, encountering an arc where the sinusoid is negative. If rational, its finite rotation orbit has at least three points and the sinusoid sums to zero over one complete period, yet is not identically zero (its value at \(n=0\) is \(y_0=1\)); hence one term is negative. The latter conclusion also covers the case of four or more roots of unity, with the same sum-zero argument. Thus positivity fails.

**5. Failure above the threshold for \(\kappa>1/2\).** If \(z>R(\kappa)\), then \(B<0\). If \(C\ge0\), the very next computed value \(y_2=Bq-C\) is negative. If \(C<0\), the characteristic roots satisfy \(r_-<0<r_+\) and \(|r_-|>r_+\), the latter because their sum is \(B<0\). By the two identities in step 1, \(q>r_+\). Solving the initial-value equations gives the coefficient of \(r_-^n\) as \((r_+-q)/(r_+-r_-)<0\). It dominates the even iterates for sufficiently large \(n\), proving \(y_{2n}<0\) eventually. This establishes necessity in every case.

**6. Optimal parameter.** The first branch of \(R\) is strictly increasing on \([0,1/2]\), while \((1-\kappa^2)/\kappa=1/\kappa-\kappa\) is strictly decreasing on \([1/2,1)\). Their common endpoint value is \(3/2\). The maximizer is unique, and the proof is complete.

## Verification

The companion standalone `CHECK.py` uses Python's exact rational arithmetic to check the coefficient reductions, discriminant identity, starter-root identities and sample threshold evaluations. It also checks explicit finite negative witnesses beyond the boundary for representative rational parameters. These reproducibility checks are *not* substituted for the infinite-sequence proof above. Invoke `python3 CHECK.py` in the directory containing the file. The identity reductions were separately verified symbolically by polynomial factorization.

## Relationship to prior work

Reference [1, Corollary 4.2, Eq. (25)] supplies the optimal constant-step \(L(\kappa)\)-stable family and its A-stability/error tradeoff. Its analyzed stability factors and reported stiff numerical tests do not supply the present all-iterate, starter-specific sign classification. The \(\kappa=0\) member is classical BDF2, for which the \(z=1/2\) positivity boundary is previously known; this is a consistency check, not an originality claim. References [2] and [3] analyze broader numerical monotonicity and step-size conditions for multistep algorithms, including starters, but their investigated coefficient families and quantified nonlinear/SSP conditions are not equivalent to a complete scalar, fixed-starter phase diagram for [1, Eq. (25)]. Reference [4] analyzes algebraic boundedness coefficients for existing BDF and Adams families; a possibility of historical implicit specialization remains and warrants independent checking.

## Limitations

The theorem concerns exact arithmetic, one positive scalar linear decay mode, constant step size, and a backward-Euler first step. It neither guarantees positivity for semidiscrete PDEs or arbitrary matrices nor covers the alternative starting procedures reported in [1]. The phase diagram is an all-time positivity property, distinct from absolute stability, error-constant optimality, strong stability preservation, and mere eventual decay. Literature comparisons cannot rule out every unindexed or implicit historical equivalent. Independent mathematical assessment has not been performed.

## References

[1] T. Jensen, L. Lóczi, and D. I. Ketcheson, *Optimized linear multistep methods for stiff problems* (2026), arXiv:2610.22685, especially Section 4.1 and Corollary 4.2. First public posting 2026-10-15. https://arxiv.org/pdf/2610.22685

[2] W. Hundsdorfer, S. J. Ruuth, and R. J. Spiteri, *Monotonicity-Preserving Linear Multistep Methods*, SIAM J. Numer. Anal. 41 (2003), 605–623. https://doi.org/10.1137/S0036142902406326 ; lawful preprint https://ir.cwi.nl/pub/4231

[3] W. Hundsdorfer, *Partially implicit BDF2 blends for convection dominated flows*, CWI report (1998), subsequently SIAM J. Numer. Anal. 38 (2001), 1763–1783. https://ir.cwi.nl/pub/4596/04596D.pdf ; https://doi.org/10.1137/S0036142999364741

[4] L. Lóczi, *Exact optimal values of step-size coefficients for boundedness of linear multistep methods* (2016), arXiv:1609.07858. https://arxiv.org/abs/1609.07858
