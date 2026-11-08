# Sharp restart-benefit interval for a reflecting finite lattice walk

## Finding

For each integer \(L\ge2\), consider a continuous-time nearest-neighbor walk on \(\{0,1,\ldots,L\}\), starting at site \(2\), absorbed at site \(0\), jumping along every available edge at rate one, and reset independently to site \(2\) at Poisson rate \(r\ge0\). Let \(M_L(r)\) be its mean absorption time. Define
\[
D_k(r)=\sum_{j=0}^k\binom{k+j}{2j}r^j,\quad
Q_L(r)=\frac{D_L(r)-D_{L-2}(r)}{r}-(2L-1)D_{L-2}(r),
\]
with the quotient interpreted as a polynomial. Then
\[
M_L(0)=2L-1,\qquad
M_L(r)=\frac{D_L(r)-D_{L-2}(r)}{rD_{L-2}(r)}\quad(r>0).
\]
For \(L=2,3\), every positive reset rate increases the mean absorption time. For every \(L\ge4\), there exists exactly one positive crossover \(\rho_L\), defined as the unique positive zero of \(Q_L\), and
\[
M_L(r)<M_L(0)\ \Longleftrightarrow\ 0<r<\rho_L,\qquad
M_L(\rho_L)=M_L(0),
\]
with the reverse strict inequality for \(r>\rho_L\). The first beneficial instance has \(L=4\) and \(\rho_4=\sqrt7\).

For \(L\ge4\) the positive-rate minimum is attained. If \(r_L\) is any global minimizer of \(M_L\), then
\[
\lim_{L\to\infty}r_L=2(\sqrt2-1),\qquad
\lim_{L\to\infty}\min_{r\ge0} M_L(r)=3+2\sqrt2.
\]
The statements refer to the stated continuous-time edge-rate normalization, not a discrete-time walk with geometric restarting.

## Assumptions and scope

The underlying walk has independent rate-one exponential clocks on incident edges. Its generator on the transient vertices \(1,\ldots,L\) is the path graph Laplacian with site \(0\) killed, plus a jump to \(2\) at rate \(r\) from every transient site other than \(2\). Resets at site \(2\) have no effect. The endpoint \(L\) has only the inward jump at rate one, so it is reflecting in the nearest-neighbor sense. The target at \(0\) is fully absorbing. Expectations start at site \(2\). All claims hold for the integers and real reset rates stated above; no continuum limit is assumed.

## Proof

**Renewal formula.** Write \(T\) for the absorption time without resetting and \(\varphi_i(r)=\mathbb E_i[e^{-rT}]\). First-step conditioning gives \(\varphi_0=1\),
\[
(2+r)\varphi_i=\varphi_{i-1}+\varphi_{i+1}\quad(1\le i<L),\qquad
(1+r)\varphi_L=\varphi_{L-1}.
\]
The continuants \(D_0=1\), \(D_1=1+r\), \(D_k=(2+r)D_{k-1}-D_{k-2}\) satisfy \(\varphi_i=D_{L-i}/D_L\). The displayed binomial coefficient representation of \(D_k\) follows from this recurrence and initial values (or coefficientwise from Pascal's identity). In particular \(\varphi_2=D_{L-2}/D_L\). Each reset renews an independent attempt: the success probability is \(\varphi_2(r)\), while the expected duration of one attempt is \((1-\varphi_2(r))/r\). The renewal equation therefore gives \(M_L(r)=(1-\varphi_2)/(r\varphi_2)\). At zero resetting the simple Poisson equation \(m_0=0\), \(2m_i-m_{i-1}-m_{i+1}=1\) for interior sites and \(m_L-m_{L-1}=1\) gives \(m_i=i(2L+1-i)/2\), hence \(m_2=2L-1\).

**A one-sign-change polynomial.** For \(L\ge2\), expansion of the binomial continuants shows that the constant coefficient of \(Q_L\) is zero, that its leading coefficient (degree \(L-1\)) is one, and that the coefficient of degree \(L-2\) is zero. For \(1\le j\le L-3\), binomial cancellation gives
\[
[r^j]Q_L=-\frac{2j(2L-1)(L-j-2)}{(2j+1)(L-j-1)}\binom{L+j-2}{2j}<0.
\]
Indeed the expression before simplification is
\[
\binom{L+j+1}{2j+2}-\binom{L+j-1}{2j+2}
 -(2L-1)\binom{L+j-2}{2j}.
\]
Thus \(Q_2=r\), \(Q_3=r^2\), while for \(L\ge4\)
\[
Q_L=r^{L-1}-\sum_{j=1}^{L-3}c_{L,j}r^j,\qquad c_{L,j}>0.
\]
Dividing by \(r^{L-1}\) gives \(1-\sum_{j=1}^{L-3}c_{L,j}r^{j-L+1}\), which increases strictly from \(-\infty\) to \(1\) as \(r\) goes from zero to infinity. It therefore has precisely one positive zero. Since \(D_{L-2}(r)>0\) for \(r\ge0\), the sign of \(M_L(r)-(2L-1)\) agrees with that of \(Q_L(r)\). The asserted sharp threshold follows; \(Q_4=r(r^2-7)\).

**Optimal large-volume limit.** For \(r>0\), choose \(\theta>0\) with \(2\cosh\theta=2+r\), and put \(y=e^\theta>1\). The continuants are
\[
D_k=\frac{\cosh((k+\tfrac12)\theta)}{\cosh(\theta/2)},\qquad
M_L(r)\longrightarrow m_\infty(r)=\frac{y^2-1}{r}=\frac{y(y+1)}{y-1}.
\]
Here \(r=y+y^{-1}-2\). Differentiation of the last rational function gives the unique minimizing \(y=1+\sqrt2\), whence \(r_\infty=2(\sqrt2-1)\) and \(m_\infty(r_\infty)=3+2\sqrt2\). For fixed \(r>0\), the ratio \(D_{L-2}/D_L\) strictly decreases with \(L\), so \(M_L(r)\) strictly increases to \(m_\infty(r)\). Every \(L\ge4\) has a positive minimizing rate: the mean starts below its zero-reset value for small positive \(r\), while \(M_L(r)\sim r\) as \(r\to\infty\). Any choice of minimizers stays bounded above, because \(M_L(r)\ge M_2(r)=r+3\), and stays bounded away from zero: choose fixed \(K\) with \(M_K(0)>3+2\sqrt2+1\); continuity yields an interval near zero in which \(M_L(r)\ge M_K(r)>3+2\sqrt2\) for all \(L\ge K\), whereas \(M_L(r_\infty)\le3+2\sqrt2\). Uniform convergence on the resulting compact positive-rate interval and uniqueness of the minimizer of \(m_\infty\) prove both limits.

## Verification

The accompanying standalone `verify.py` uses only the Python standard library. It checks the displayed rational mean against an independently constructed finite-state continuous-time generator using exact fraction Gaussian elimination for 60 graph/rate instances; checks every polynomial coefficient and its sign through \(L=150\); checks strict finite-volume monotonicity for rational test rates; and checks the limiting optimization constants. Run `python3 verify.py`. These finite checks are corroboration, not substitutes for the all-size arguments above.

## Relationship to prior work

Poisson restarting, the renewal identity, and optimal reset rates were established in the continuous-diffusion setting by Evans and Majumdar (2014). Christou and Schadschneider (2015) analyzed continuous diffusion with resetting on bounded domains and found a second-order transition in optimal rate. Bonomo and Pal (2021) established general discrete-time renewal criteria and treated confined walks with two absorbing boundaries. Das and Giuggioli (2022) derived broad propagator and first-passage formulas for discrete lattice walks with resetting, including reflective geometries. These methods furnish general input for a specialized calculation and are not claimed as new. The specific results stated here are the all-rate strict improvement interval, its unique polynomial endpoint, the first beneficial reflecting path at five vertices, and the exact infinite-volume optimal rate and mean in the edge-rate-one normalization. The inspected material did not provide these conclusions together or imply their strict coefficient-sign classification as a stated result.

## Limitations

The classification is restricted to source site \(2\), a reflecting upper endpoint, and a fully absorbing lower endpoint. It does not establish uniqueness of the minimizing rate for each finite \(L\); only existence and convergence of all minimizers are proved. The full text of Christou and Schadschneider (2015) was not available for a definitive detailed comparison; an earlier specialized result remains a historical-priority risk. The mathematical findings have not undergone independent review.

## References

- M. R. Evans and S. N. Majumdar, *Diffusion with resetting in arbitrary spatial dimension*, arXiv:1404.4574, 2014. https://arxiv.org/abs/1404.4574
- C. Christou and A. Schadschneider, *Diffusion with resetting in bounded domains*, J. Phys. A 48 (2015), 285003. https://doi.org/10.1088/1751-8113/48/28/285003
- O. L. Bonomo and A. Pal, *First passage under restart for discrete space and time: application to one dimensional confined lattice random walks*, arXiv:2102.00895, 2021. https://arxiv.org/abs/2102.00895
- D. Das and L. Giuggioli, *Discrete space-time resetting model: Application to first-passage and transmission statistics*, arXiv:2209.08330, 2022. https://arxiv.org/abs/2209.08330
