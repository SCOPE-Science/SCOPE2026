# A sharp two-moment ambiguity and sixth-moment identifiability for trapped finite-tumble particles

## Finding

For the stationary one-dimensional harmonically confined finite-tumble run-and-tumble process defined below, the dimensionless positive run-to-tumble and tumble-to-run rates are **not globally identifiable** from the second and fourth stationary position moments: at every fixed attainable variance, their inverse map has one strict fold and a nonempty interval of exactly two rate pairs. Nevertheless, the second, fourth and sixth stationary position moments together identify both rates **uniquely for all positive rate pairs**. Thus three nonzero even moments are the minimum initial segment of the even-moment hierarchy giving global rate identification in this model.

Explicitly, let \(u=\mathbb E[X^2]\in(0,1)\) and \(k=\mathbb E[X^4]/u^2\). Introduce \(t=u(a+1)\in(u,1)\), where \(a>0\) is the run-to-tumble rate and \(b>0\) the tumble-to-run rate. Their reconstruction is
\[
a=\frac{t}{u}-1,\qquad b=\frac{t(t-u)}{u(1-t)}.
\]
The fourth-moment ratio is
\[
K_u(t)=\frac{3(t^2-3tu+2u)}{(t+2u)(t+u-2tu)}.
\]
For each \(0<u<1\), this function has exactly one critical point \(t_*(u)\in(u,1)\), a strict minimum. Writing \(k_*(u)=K_u(t_*(u))\), the number of positive rate pairs giving prescribed \((u,k)\) is two if \(k_*(u)<k<3/(1+2u)\), one if \(k=k_*(u)\) or \(3/(1+2u)\le k<1/u\), and zero otherwise. The two-solution interval is nonempty for every \(u\in(0,1)\).

Despite this ambiguity, if two positive rate pairs have the same \(\mathbb E[X^2]\), \(\mathbb E[X^4]\), and \(\mathbb E[X^6]\), the rate pairs are identical.

An exact witness is \((a,b)=(1,4)\) and \((a,b)=(6/5,44/5)\): both have \(\mathbb E[X^2]=2/5\) and \(\mathbb E[X^4]=9/35\), but their sixth moments are \(4/21\) and \(288/1519\), differing by \(4/4557\).

## Assumptions and scope

The dimensionless process \((X_s,J_s)\) has \(J_s\in\{+,-,0\}\). Its position obeys the deterministic equation between jumps
\[
\dot X_s=-X_s+v(J_s),\quad v(+)=1,\quad v(-)=-1,\quad v(0)=0.
\]
From either running state \(+\) or \(-\), it enters the resting state \(0\) at rate \(a>0\); from state \(0\), it independently chooses \(+\) or \(-\) at rate \(b/2\) each. The trap relaxation and speed amplitude have been fixed as known units. The rate matrix, with rows indexing source states in order \((+, -,0)\), is
\[
Q=\begin{pmatrix}-a&0&a\\0&-a&a\\b/2&b/2&-b\end{pmatrix}.
\]
The irreducible velocity chain has stationary probabilities \((b/[2(a+b)],b/[2(a+b)],a/(a+b))\). The stable linear filter \(X_s=\int_{-\infty}^s e^{-(s-r)}v(J_r)\,dr\) defines a unique stationary joint law supported on \([-1,1]\times\{+,-,0\}\). Expectations throughout refer to that law. No additional translational Brownian noise, unknown rate scales or unknown propulsion speed is allowed in the claim.

## Proof

Define the joint moment vector \(m_n\) by \((m_n)_j=\mathbb E[X^n\mathbf1_{\{J=j\}}]\) and set \(V=\operatorname{diag}(1,-1,0)\). Stationarity of the joint generator applied to \(x^n\mathbf1_{\{J=j\}}\) gives, for every positive integer \(n\),
\[
(nI-Q^{\mathsf T})m_n=nVm_{n-1},\qquad m_0=\begin{pmatrix}\frac b{2(a+b)}\\\frac b{2(a+b)}\\\frac a{a+b}\end{pmatrix}.
\]
All these matrices are invertible for \(n\ge1\), since all eigenvalues of \(Q\) have nonpositive real part. Repeated substitution through order six yields the exact raw moments (the odd raw moments vanish by reflection symmetry):
\[
\begin{aligned}
M_2&=\frac{b}{(a+1)(a+b)},\\
M_4&=\frac{3b(b+2)}{(a+1)(a+3)(a+b)(a+b+2)},\\
M_6&=\frac{15b(b+2)(b+4)}{(a+1)(a+3)(a+5)(a+b)(a+b+2)(a+b+4)}.
\end{aligned}
\]
These formulas can be checked directly by the displayed three-dimensional matrix recurrence; a standalone symbolic verifier is supplied.

For fixed \(u=M_2\), algebra gives \(b=ua(a+1)/(1-u(a+1))\). Strict positivity forces \(0<a<1/u-1\), equivalently \(u<t=u(a+1)<1\). Substitution gives the reconstruction and \(K_u(t)\) displayed above. Differentiation yields
\[
K'_u(t)=-\frac{6u P_u(t)}{(t+2u)^2(t+u-2tu)^2},
\quad P_u(t)=(5u-3)t^2+(2-6u)t+3u-u^2.
\]
The denominator is strictly positive on \((u,1)\), and
\[
P_u(u)=5u(1-u)^2>0,\qquad P_u(1)=-(1-u)^2<0.
\]
A quadratic taking opposite nonzero signs at the interval endpoints has exactly one root in the open interval; hence \(K_u\) first decreases and then increases. Its endpoint limits are \(K_u(u)=1/u\) and \(K_u(1)=3/(1+2u)\), with \(3/(1+2u)<1/u\). Since both endpoints are excluded and the minimum is attained in the interior, the claimed zero/one/two cardinalities follow, including strict nonemptiness of the two-to-one interval.

For the sixth-moment statement define
\[
R_u(t)=\frac{M_6}{uM_4}
=\frac{5(t^2-5tu+4u)}{(t+4u)(t+3u-4tu)}.
\]
All denominators are positive for \(u<t<1\), \(0<u<1\). Suppose two distinct parameters \(t,w\in(u,1)\) give the same \(K_u\) and the same \(R_u\). Cross-multiply the two rational equalities, cancel the nonzero factor \(t-w\), and put \(S=t+w\) and \(T=tw\). The resulting *necessary* linear equations are
\[
\begin{aligned}
(3u-1)S+(3-5u)T+u^2-3u&=0,\\
(7u-1)S+(3-9u)T+u^2-7u&=0.
\end{aligned}
\]
Their coefficient determinant is \(8u(u-1)\ne0\), and their unique solution is
\[
S=\frac{u+3}{2},\qquad T=\frac{u+1}{2}.
\]
Consequently \(t,w\) are roots of
\[
z^2-Sz+T=(z-1)\left(z-\frac{u+1}{2}\right).
\]
One of them must equal the excluded endpoint \(1\), a contradiction. Thus \((K_u,R_u)\) is injective at fixed \(u\), establishing global identification by \((M_2,M_4,M_6)\). Direct substitution of the two explicit witness pairs verifies their values.

## Verification

Run `python verify.py` with SymPy installed (tested with the locally available SymPy version). The script constructs the original three-state generator, independently computes stationary state-resolved moment vectors through sixth order, compares them against the claimed closed formulas, checks all change-of-variable and cross-multiplication identities exactly, verifies the exact witness, and checks the moment expressions across thirty rational rate pairs. All 119 assertions passed. The infinite parameter-domain statements are established by the preceding algebra, not by finite test coverage.

## Relationship to prior work

Sun, Ye and Chen (2026) give the conditional position distributions and their relationship to the full Fokker–Planck system for finite-tumble run-and-tumble motion, including the three-state model and its moments. Sun, Ye and Podgornik (2024, revised 2025) derive arbitrary-order stationary moments and the exact one-dimensional marginal distribution for that same model. These are foundational source results, **not** claimed here. Basu and coauthors (2019) treat a related three-state harmonic process with a single shared switching-rate parameter. Seyrich and coauthors (2018) develop inference from richer time-resolved swimming measurements, rather than this stationary-position moment hierarchy. The new assertion is the complete global inverse-moment multiplicity classification and the sharp sixth-moment resolution of all collisions; previously available moment formulas alone are not being asserted as novel.

## Limitations

This is an idealized, exactly known two-parameter continuous-time model with known trap and propulsion scales. The theorem concerns exact population stationary moments, not statistically stable inference from finite noisy observations. In the explicit collision, the sixth-moment separation is only \(4/4557\), so sampling precision may be demanding. The result does not extend by assertion to spatially heterogeneous rates, unknown speed, arbitrary velocity-renewal kernels, inertial dynamics or added Brownian noise. Published all-order moment formulas make this a derived structural theorem rather than an entirely new stationary-law calculation; publication priority is not independently established.

## References

- A. Sun, F. Ye, J. Z. Y. Chen, *Run-and-tumble particles in a harmonic external field: constructing the solution of the Fokker-Planck equation from the equations of motion*, arXiv:2610.24961v1, first posted 2026-10-18. https://arxiv.org/html/2610.24961
- A. Sun, F. Ye, R. Podgornik, *Exact moments for a run and tumble particle in a harmonic trap with a finite tumble time*, arXiv:2409.00578, first posted 2024-09-01; Phys. Rev. E 111, 044136 (2025). https://arxiv.org/pdf/2409.00578
- U. Basu, S. N. Majumdar, A. Rosso, S. Sabhapandit, G. Schehr, *Exact stationary state of a run-and-tumble particle with three internal states in a harmonic trap*, arXiv:1910.10083 (2019). https://arxiv.org/html/1910.10083v1
- M. Seyrich, Z. Alirezaeizanjani, C. Beta, H. Stark, *Statistical parameter inference of bacterial swimming strategies*, arXiv:1805.08860 (2018). https://arxiv.org/abs/1805.08860
