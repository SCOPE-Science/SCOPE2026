# A sharp overshoot threshold and log-periodic amplification in two-rate contagion

## Finding
In a two-rate linear within-group contagion, a pooled difference between adjacent effective infection kernels may exceed **both** physical transmission slopes. The first group size that permits this apparent overshoot is exact. As the proportion of high-rate groups tends to zero, the largest pooled slope grows without bound at logarithmic speed and has a nonconstant log-periodic leading coefficient.

Let \(0<a<b\), let \(q\in(0,1)\) be the proportion of low-rate groups, and put
\[
\theta=a/b,\qquad c=q/(1-q),\qquad h=\log(b/a)>0.
\]
A group has \(N\ge3\) members, all of one static type, and each susceptible individual in a group with \(i\) infectives acquires infection from its group at rate \(i a\) or \(i b\), according to type. Infectives recover independently at rate one. The group also receives an external infection force \(\rho>0\) per susceptible. For each fixed \(N,q,a,b\), first take the stationary weak-import limit \(\rho\downarrow0\). Let \(B_i\) be the resulting **within-group** incidence rate per susceptible, conditional on observing \(i\) infectives in an untyped group, \(1\le i\le N-1\). Define the pooled finite difference \(\delta_i=B_i-B_{i-1}\) for \(2\le i\le N-1\).

**Exact cutoff.** Write
\[
f(x)=(1-\theta)x-1-c\theta^{x-1},\qquad
x_c=\frac{1}{1-\theta}+\frac{1}{h}W_0\!\left(\frac{hc}{1-\theta}e^{-h\theta/(1-\theta)}\right),
\]
where \(W_0\) is the positive real inverse of \(y\mapsto ye^y\). Then
\[
\boxed{\delta_i>b\quad\Longleftrightarrow\quad i>x_c},\qquad
\boxed{N_{\min}=1+\max\{2,\lfloor x_c\rfloor+1\}}.
\]
Thus the overshoot occurs in some *observable* incidence count if and only if \(N\ge N_{\min}\). The group-size condition is sharp; equality at an integer root does **not** count as overshoot. For \(c\to\infty\),
\[
x_c=1+\frac{\log c-\log\log c+\log[h/(1-\theta)]}{h}+o(1),
\]
and hence \(N_{\min}=(\log c-\log\log c)/h+O(1)\).

**Maximal overshoot.** Define \(m=\lfloor(\log c)/h\rfloor\), \(\phi=(\log c)/h-m\in[0,1)\), and \(F(z)=z/[(z+\theta)(z+1)]\). If the group size is allowed to depend on \(c\) and always satisfies \(N\ge m+3\), then uniformly as \(c\to\infty\),
\[
\boxed{\max_{2\le i\le N-1}(\delta_i-b)
=\frac{(b-a)(1-\theta)}{h}F(\theta^{1-\phi})\log c+O_{a,b}(1)}.
\]
The normalized maximum has exactly the following interval of accumulation points as \(c\to\infty\):
\[
\frac{(b-a)(1-\theta)}{h}
\left[\frac{1}{2(1+\theta)},\frac{1}{(1+\sqrt\theta)^2}\right].
\]
Thus even though every true within-group increment is at most \(b\), the pooled increment is unbounded in this *ordered* limit of weak import and rare high-rate groups. This logarithmic growth and its lattice modulation concern the pooled **finite difference**, not a physical per-contact transmissibility.

## Assumptions and scope
The mathematical model has two positive constant transmission slopes, exchangeable independently assigned group types with low-rate prior probability \(q\), common group size \(N\), unit exponential recovery, and homogeneous import force \(\rho\). The weak-import stationary limit is taken **at fixed** \(N,q,a,b\) before any parameter or group-size limit. Only \(i\le N-1\) are treated as observable transmission contexts because at \(i=N\) there are no susceptibles. Statements about \(N\to\infty\) concern the resulting sequence of limiting kernels, not a uniform finite-\(\rho\) approximation. They do not assert that the global epidemic can sustain such a prevalence or that empirical finite-sample estimates exhibit the exact effect.

## Proof
**1. Weak-import kernel.** In a group with slope \(\lambda\in\{a,b\}\), the exact birth and death rates of the infected count at fixed import \(\rho>0\) are \((N-j)(\rho+j\lambda)\) and \(j\). Detailed balance yields
\[
\pi_{j|\lambda}(\rho)=\pi_{0|\lambda}(\rho)\binom Nj\prod_{k=0}^{j-1}(\rho+k\lambda),\quad 1\le j\le N.
\]
Since \(\pi_{0|\lambda}(\rho)\to1\), for fixed \(j\ge1\),
\[
\lim_{\rho\downarrow0}\frac{\pi_{j|\lambda}(\rho)}{\rho}
=\binom Nj (j-1)!\lambda^{j-1}.
\]
Bayes averaging over the two types therefore gives
\[
B_i=i\frac{q a^i+(1-q)b^i}{q a^{i-1}+(1-q)b^{i-1}}
=ib-i(b-a)\frac{z_i}{1+z_i},\quad z_i=c\theta^{i-1}.
\]
This is an *endogenous within-group* rate per susceptible; the common import term cancels in adjacent finite differences.

**2. Exact overshoot and unique crossing.** Subtracting consecutive expressions gives the identity
\[
\delta_i-b=(b-a)
\frac{z_i\,[i(1-\theta)-1-z_i]}{(\theta+z_i)(1+z_i)}.
\]
Every omitted factor has positive sign. The bracket is \(f(i)\), and
\[
f'(x)=1-\theta+hc\theta^{x-1}>0.
\]
The bracket has one real zero \(x_c>1\), is negative before it and positive after it. Solving \((1-\theta)x-1=c e^{-h(x-1)}\) by substituting \(y=x-1/(1-\theta)\) gives the stated principal-Lambert formula. Because the largest observable count is \(N-1\), the first feasible group size is exactly \(N_{\min}\). The classical \(W_0(z)=\log z-\log\log z+o(1)\) asymptotic, with its constants retained, proves the expanded cutoff.

**3. Sharp maximum and lattice effect.** Rearrange the exact identity as
\[
\delta_i-b=(b-a)\left[(1-\theta)iF(z_i)-\frac{z_i}{\theta+z_i}\right].
\]
Write \(i=m+1+j\), so \(z_i=\theta^{j-\phi}\). The quantity \(|j-1|F(\theta^{j-\phi})\) is uniformly bounded for all integers \(j\), \(\phi\in[0,1]\), because of geometric decay at both ends. Also \(0<z_i/(\theta+z_i)<1\). Consequently, uniformly in all admissible \(i\),
\[
\delta_i-b=(b-a)(1-\theta)(m+2)F(\theta^{j-\phi})+O_{a,b}(1).
\]
A direct cancellation yields
\[
F(\theta z)-F(z)=\frac{(1-\theta)z(z-1)}{(z+1)(\theta z+1)(z+\theta)}.
\]
This difference is positive for \(z>1\) and negative for \(0<z<1\). Since \(\theta^{-\phi}\ge1\) and \(\theta^{1-\phi}\le1\), the maximum over all integer \(j\) is \(F(\theta^{1-\phi})\), attained at \(j=1\) (with a possible adjacent tie when \(\phi=0\)). The group-size condition \(N\ge m+3\) ensures that index \(i=m+2\) is observable. Finally \(m+2=(\log c)/h+O(1)\), proving the uniform expansion. As \(\phi\) varies through a complete logarithmic period, \(F(\theta^{1-\phi})\) ranges continuously between \(1/[2(1+\theta)]\) and \(1/(1+\sqrt\theta)^2\); both endpoints and every intermediate value are attained along sequences of positive \(c\to\infty\). This proves the complete accumulation interval.

## Verification
The accompanying `check.py` uses exact rational arithmetic to reproduce the finite-difference identity over multiple parameter grids and to verify the sharp integer cutoff, including the endpoint restriction \(i\le N-1\). For \(a=1\), \(b=3\), \(q=99/100\), the real crossing is approximately \(4.5397477824\) and the smallest group has \(N=6\) people. The preceding finite difference is \(31/14<3\), while \(\delta_5=53/14>3\); with \(N\ge7\), \(\delta_6=191/38\). The checker also tests the asymptotic coefficient along fixed logarithmic phases, but these finite tests are not used as proof of the limiting statement. Reproduce by running `python3 check.py` with the standard library.

## Relationship to prior work
Hébert-Dufresne et al. (2026) introduce the two different observational increments and describe an apparent pooled slope exceeding a group's measured marginal increment. St-Onge, Hébert-Dufresne and Allard (2023) give the critical moment-ratio representation and an explicit two-atom posterior mean, with a qualitative sigmoid around a logarithmic posterior crossover. These works already cover the *existence* of Simpson-type nonlinearity and of a soft two-type crossover. The result here is the exact strict threshold for a **pooled finite difference to exceed the maximum physical slope**, the sharp first feasible group size including the all-infected boundary, the negative log-log correction to that threshold, and the unbounded overshoot with its explicitly determined log-periodic coefficient. General results about moment ratios and Lambert functions are not claimed as new.

## Limitations
The conclusions concern one homogeneous group-size stratum and a limiting stationary kernel; finite importation, simultaneous population-wide dynamics, observations with noise and heterogeneous recovery are outside scope. Because both cited contagion works already provide the rate representation, independent priority review should assess whether an equivalent sharp finite-difference or rare-component amplification theorem was previously derived elsewhere, including in supplementary literature. No inference of genuine synergistic infection from the pooled slope is warranted. No independent audit has been performed.

## References
1. L. Hébert-Dufresne, A. Allard, J.-G. Young, W. H. W. Thompson, G. St-Onge, "Simpson's paradox explains the ubiquity of nonlinear, threshold, and complex contagions," arXiv:2605.00791v1 (first public May 1, 2026), https://arxiv.org/html/2605.00791v1 .
2. G. St-Onge, L. Hébert-Dufresne, A. Allard, "Nonlinear bias toward complex contagion in uncertain transmission settings," *PNAS* 121 (2024), e2312202121, first online December 28, 2023, https://pmc.ncbi.nlm.nih.gov/articles/PMC10769855/ .
3. G. St-Onge, H. Sun, A. Allard, L. Hébert-Dufresne, G. Bianconi, "Universal nonlinear infection kernel from heterogeneous exposure on higher-order networks," *Phys. Rev. Lett.* 127 (2021), 158301, https://doi.org/10.1103/PhysRevLett.127.158301 .
