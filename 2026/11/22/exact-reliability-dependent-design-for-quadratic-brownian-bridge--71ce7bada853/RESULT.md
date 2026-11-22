# Exact reliability-dependent design for quadratic Brownian-bridge energy

## Finding
Let \(B\) be the standard centered Brownian bridge on \([0,1]\), let \(Q=\int_0^1 B(t)^2\,dt\), and choose two predetermined, possibly coincident locations \(0\le x\le y\le1\). Their exact values, if available, are independently delivered with probability \(p\in(0,1]\); failures are observed as erasures. The estimator is the conditional mean of \(Q\) given the delivered values and the erasure pattern, and risk means unconditional squared error.

**The unique optimal ordered design**, allowing all boundaries and coincidences, is
\[
x_p=\tfrac12-d_p,\qquad y_p=\tfrac12+d_p,\qquad
d_p=\frac{3p+\sqrt{33p^2-8p+16}-4}{8(3p+2)}.
\]
The half-separation \(d_p\) is strictly increasing in \(p\), tends to zero as \(p\downarrow0\), and equals \((\sqrt{41}-1)/40\) at \(p=1\). It is strictly positive for every \(p>0\). At \(p=1/2\), the optimal sites are exactly \((3/7,4/7)\), and the risk is exactly \(697/61740\), compared with \(17/1440\) for two coincident midpoint attempts. At \(p=0\) all sites tie; uniqueness is not claimed at that excluded endpoint.

## Assumptions and scope
The bridge is Gaussian with covariance \(K(s,t)=\min(s,t)-st\), zero endpoints, and no observation noise on successful delivery. Each of the two attempts independently succeeds with the same known probability \(p\), independently of the bridge. Both sites must be set before either delivery is known. Distinct attempts at a common site return the same exact path value if successful. The squared-error estimator may be any measurable function of the available values and delivery indicators; the conditional mean minimizes its risk. The result does not cover adaptive placement, other Gaussian processes, additive value noise, nonlinear delivery mechanisms or unequal probabilities.

## Proof
**1. Exact Bayes risk.** Given a set \(T\) of delivered knots, write \(C_T\) for the conditional covariance operator and \(\mu_T\) for the conditional mean. Gaussian conditioning and the quadratic-form identity give
\[
\mathbb E[\operatorname{Var}(Q\mid B|_T)]
=2\operatorname{tr}(C_T^2)+4\operatorname{tr}\bigl(C_T(K-C_T)\bigr)
=4\operatorname{tr}(C_TK)-2\operatorname{tr}(C_T^2).
\]
Here \(\mathbb E[\mu_T\otimes\mu_T]=K-C_T\), and all traces exist because the covariance operators are Hilbert--Schmidt. Conditional on knots \(0=t_0\le t_1\le\cdots\le t_m\le t_{m+1}=1\), \(C_T\) is block diagonal with standard bridge covariance on each interval. For a cell \([a,b]\) of length \(\ell=b-a\), direct integration of the kernels yields its contribution
\[
r(a,b)=\frac{a(1-b)\ell^3}{3}+\frac{\ell^4}{9}-\frac{4\ell^5}{45}.
\]
Indeed, writing the cell bridge covariance as \(C(u,v)=\min(u,v)-uv/\ell\), the prior covariance restricted to the cell is \(C(u,v)+D(u,v)\), where \(D\) is the covariance of the linear interpolation of the endpoint values. The integrals \(\iint C(u,v)(1-u/\ell)(1-v/\ell)\,du\,dv=\ell^3/45\) and \(\iint C(u,v)(1-u/\ell)(v/\ell)\,du\,dv=7\ell^3/360\), together with \(\operatorname{tr}(C^2)=\ell^4/90\), give the displayed cell formula. Repeated knots have zero-length cells and cause no singularity.

Let \(R_0=r(0,1)=1/45\), \(R_1(t)=r(0,t)+r(t,1)=[1-10t^2(1-t)^2]/45\), and \(R_2(x,y)=r(0,x)+r(x,y)+r(y,1)\). Independence of the erasures gives the exact unconditional risk
\[
R_p(x,y)=(1-p)^2 R_0+p(1-p)\bigl(R_1(x)+R_1(y)\bigr)+p^2R_2(x,y).
\]
All endpoints, ties and interior designs are included continuously.

**2. Separating position and spacing.** Set \(x=1/2-a-d\) and \(y=1/2-a+d\). The full feasible domain is \(0\le d\le1/2\), \(|a|\le1/2-d\). Elementary expansion of the exact cell risks yields
\[
R_p(a,d)=R_p(0,d)+\frac{pa^2}{9}\left[C_0(d,p)+C_2(d,p)a^2\right],
\]
with
\[
C_0=2-p-24d^2+p(12d^2-8d^3),\qquad
C_2=8dp+2p-4.
\]
For \(0\le d\le1/4\), \(C_2\le0\). Thus the square bracket is bounded below by its value at \(a^2=(1/2-d)^2\). This lower bound is affine in \(p\), with endpoint values \(1+4d-28d^2\) at \(p=0\) and \((1+8d-44d^2)/2\) at \(p=1\). Both concave quadratics are strictly positive throughout \([0,1/4]\). Hence \(a=0\) uniquely minimizes risk for every fixed \(d\) in this interval.

**3. Excluding larger separations globally.** We prove that the risk is strictly increasing in \(d\) for every fixed admissible \(a\) whenever \(1/4\le d<1/2\). Put \(s=4d-1\in[0,1)\), \(z=[4a/(1-s)]^2\in[0,1]\), and \(D=18(\partial_dR_p)/p\). The exact polynomial \(D\) is affine in \(p\): \(D=(1-p)D_0+pD_1\), where
\[
D_0=\frac{(1-s^2)[3+s-3(1-s)z]}{2}\ge0.
\]
For the \(p=1\) endpoint polynomial \(D_1(s,z)\), exact differentiation gives
\[
D_1(s,1)=\frac{(1-s^2)(s^2+18s+1)}8>0,
\]
\[
\partial_zD_1(s,1)=-\frac{(1-s)^2(s^2+22s+13)}{16}\le0,
\qquad \partial_z^2D_1(s,z)=\frac{(1-s)^4}{8}\ge0.
\]
Convexity in \(z\) and the nonpositive derivative at \(z=1\) show \(D_1(s,z)\ge D_1(s,1)>0\) for \(0\le z\le1\), so \(\partial_dR_p>0\) for \(p>0\) and \(d<1/2\). For every feasible \((a,d)\) with \(d>1/4\), the point \((a,1/4)\) is also feasible, and consequently
\[
R_p(a,d)>R_p(a,1/4)\ge R_p(0,1/4).
\]
Thus no optimum can have \(d>1/4\); the endpoint \(d=1/2\) follows by continuity and strict increase on preceding intervals.

**4. Unique optimal half-separation.** For \(a=0\) the exact polynomial is
\[
R_p(0,d)=\frac{8-10p+5p^2-20p^2d+(80p-40p^2)d^2+240p^2d^3-(160p+240p^2)d^4}{360}.
\]
Its derivative factors as
\[
\partial_d R_p(0,d)= -\frac{p(2d-1)}{18}
\left[(24p+16)d^2+(8-6p)d-p\right].
\]
For \(0<p\le1\), the bracket has one positive root in \((0,1/4)\), is negative to its left and positive to its right; at \(d=1/4\) it equals \(3-p>0\). Hence that root is the sole global minimum, yielding the stated radical. The inverse relation
\[
p=\frac{16d^2+8d}{1+6d-24d^2},\qquad
\frac{dp}{dd}=\frac{8(36d^2+4d+1)}{(1+6d-24d^2)^2}>0
\]
proves strict increasing dependence. Substitution gives the half-reliability and fully reliable expressions. This proves all claims.

## Verification
Run `python verify.py` with Python 3, SymPy and NumPy. It checks, using exact symbolic arithmetic, the cell-aggregation identities, the centered-risk expansion, both sides of the derivative-certification split, the optimizer equation, and the rational half-reliability risk. It also compares the analytic optimum with 14,000 reproducibly randomized feasible ordered pairs; these finite checks supplement, rather than replace, the proof above.

## Relationship to prior work
Neuberger, Alexanderian and van Bloemen Waanders (2024, arXiv:2411.07532v1) derive a general Gaussian quadratic-goal posterior-variance criterion, and analyze computational sensor selection in PDE examples. Its general risk identity is a precursor, not a claim of novelty here. The present result gives a closed-form **unique global optimizer** across every pair of locations and every positive independent erasure probability, with a global boundary proof. Related deterministic Brownian-bridge two-sensor quadratic-energy calculations give the \(p=1\) endpoint; that endpoint alone is not new. Existing Brownian-bridge random-erasure reconstruction designs optimize the whole path's integrated error rather than the scalar nonlinear quadratic-energy target. Tsirpitzi, Miller and Burman (2023) optimize prediction under Brownian-bridge misspecification with a different linear-process/path loss; their designs do not specialize to this quadratic-energy erasure problem. The distinction is a claim about implications of mathematical statements, not a proof that no unexamined paper exists.

## Limitations
No adaptive or unequally reliable sensing, measurement noise, unknown covariance, or other nonlinear functionals are treated. The exact full-information endpoint and general quadratic-Gaussian trace formulas have precursors, so novelty is specifically the all-reliability exact optimal pair, strict uniqueness and global centering/spacing argument. Independent mathematical and historical-priority reviews have not been performed. Randomized tests do not certify a continuum statement by themselves.

## References
1. J. N. Neuberger, A. Alexanderian and B. van Bloemen Waanders, *Goal oriented optimal design of infinite-dimensional Bayesian inverse problems using quadratic approximations*, arXiv:2411.07532v1, first submitted 2024-11-12, https://arxiv.org/abs/2411.07532.
2. R. E. Tsirpitzi, F. Miller and C.-F. Burman, *Robust optimal designs using a model misspecification term*, Metrika 86 (2023), 781–804, https://doi.org/10.1007/s00184-023-00893-6.
3. J. Foster, T. Lyons and H. Oberhauser, *An optimal polynomial approximation of Brownian motion*, arXiv:1904.06998v1, first submitted 2019-04-15, https://arxiv.org/abs/1904.06998.
