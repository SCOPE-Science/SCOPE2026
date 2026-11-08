# Sharp fixed-threshold outbreak-risk bounds for two-way cross-group transmission

## Finding

Consider a two-type Galton–Watson epidemic with no within-type transmission. Every infective of type A produces an independent Poisson number of type-B infectives with mean \(a>0\); every type-B infective produces an independent Poisson number of type-A infectives with mean \(b>0\). All reproduction events are independent. The initial infective is A or B with probability \(1/2\) each. Hold the next-generation spectral radius \(R=\sqrt{ab}\) fixed while varying the directional asymmetry \(a/b\).

**Theorem (complete fixed-\(R\) extremal classification).** If \(R>1\), let \(s_r\in(0,1)\) be the unique positive solution to \(s_r=1-\exp(-r s_r)\) for \(r>1\). The probability \(P(a,b)\) of nonextinction satisfies the sharp bounds
\[
\frac{s_{R^2}}2<P(a,b)\le s_R.
\]
The upper equality holds if and only if \(a=b=R\). The lower bound is an unattained infimum, approached as \(a/b\to0\) or \(a/b\to\infty\). Moreover \(P(a,b)\) strictly decreases as the absolute log-asymmetry \(|\log(a/b)|\) increases at fixed \(R\).

If \(0<R<1\), extinction is certain, but the expected total number of infections (including the initially infected individual) is
\[
E(a,b)=\frac{2+a+b}{2(1-R^2)}\ge\frac1{1-R},
\]
with equality if and only if \(a=b=R\), and no finite upper bound as directional asymmetry grows. At \(R=1\) extinction is certain but expected total infections are infinite. Thus balancing minimizes subcritical expected outbreak burden yet maximizes supercritical nonextinction risk, when the reproduction threshold is fixed.

For instance, at \(R=2\), the uniform-seed nonextinction probability is maximized at \(s_2\simeq0.7968121300\) and has sharp lower infimum \(s_4/2\simeq0.4900862994\). The two models have the same spectral-radius reproduction number throughout.

## Assumptions and scope

The epidemic is an *exact* discrete-generation, two-type, independent-offspring branching process, not a finite-population transmission process with susceptible depletion. Directed offspring rates \(a,b\) may be any positive real numbers; no upper bound or fixed arithmetic mean is assumed. All offspring of A are B and vice versa; the initial type is uniform. The spectral radius of the mean offspring matrix \(M=\begin{psmallmatrix}0&a\\ b&0\end{psmallmatrix}\) is \(\sqrt{ab}\). The infinite-outbreak event means nonextinction of this branching process, corresponding only to an early-phase large-population approximation in an SIR setting. The parameter cases \(R<1\), \(R=1\), and \(R>1\) are treated separately. The infimum at positive \(a,b\) is not attained.

## Proof

**1. Existence and uniqueness of survival probabilities.** Let \(x\) (respectively \(y\)) be the probability of nonextinction from one type-A (respectively type-B) founder. Independence and the Poisson generating function give
\[
x=1-e^{-ay},\qquad y=1-e^{-bx}.
\]
For \(R\le1\), standard finite-type Galton–Watson extinction theory, or the scalar concave fixed-point argument below, implies \(x=y=0\). For \(R>1\), substituting the second equation into the first yields \(x=f(x)\), where \(f(x)=1-\exp[-a(1-\exp(-bx))]\). This function is strictly increasing and strictly concave on \([0,1]\), with \(f(0)=0\), \(f'(0)=ab>1\), and \(f(1)<1\). Consequently \(f(x)-x\) has precisely one positive root in \((0,1)\); the second equation uniquely gives \(y\in(0,1)\). The uniform-seed survival probability is \(P(a,b)=(x+y)/2\).

**2. A strict convexity lemma.** Put \(h(u)=-\log(1-u)\), \(H(u)=h(u)/u\), and \(F(u)=\log H(u)\) for \(0<u<1\). Since \(H(u)=\sum_{n\ge0}u^n/(n+1)\), it is strictly increasing from 1 to infinity; therefore \(F\) is a strictly increasing bijection \((0,1)\to(0,\infty)\). The crucial additional property is strict convexity:
\[
F''(u)=\frac1{u^2}+\frac{h(u)-1}{(1-u)^2h(u)^2}>0.
\]
For \(h(u)\ge1\) this is immediate. For \(t=h(u)\in(0,1)\), after multiplying by positive denominators, the claimed inequality is equivalent to
\[
t^2>(1-t)(e^t-1)^2.
\]
To prove this for the whole interval, write \((e^t-1)^2=\sum_{n=2}^{\infty}c_n t^n\), where \(c_n=(2^n-2)/n!\). We have \(c_2=c_3=1\), while \(c_n<c_{n-1}\) for every integer \(n\ge4\) (indeed \((n-2)2^{n-1}>2n-2\)). Hence the coefficient of \(t^3\) in \((1-t)(e^t-1)^2\) is zero and every coefficient of degree at least four is strictly negative. Absolute convergence for \(0<t<1\) gives the strict inequality. This proves the lemma without relying on a finite numerical test.

Thus the inverse \(g=F^{-1}\), continuously extended by \(g(0)=0\), is strictly increasing and strictly concave on \([0,\infty)\).

**3. Supercritical sharp bounds and optimizer.** The survival equations are \(h(x)=ay\) and \(h(y)=bx\), so
\[
H(x)H(y)=ab=R^2,\qquad F(x)+F(y)=2\log R.
\]
Write \(L=\log R>0\), \(z=F(x)\in(0,2L)\). Then \(x=g(z)\), \(y=g(2L-z)\), and
\[
P(a,b)=\frac{g(z)+g(2L-z)}2.
\]
Strict Jensen concavity yields \(P(a,b)\le g(L)\), with equality exactly at \(z=L\), hence \(x=y\), hence \(a=b=R\). Since \(F(g(L))=L\), the defining equation is \(h(g(L))=R g(L)\), or \(g(L)=s_R\).

Strict concavity and \(g(0)=0\) give the two strict chord inequalities \(g(z)>[z/(2L)]g(2L)\) and \(g(2L-z)>[(2L-z)/(2L)]g(2L)\). Adding gives \(P(a,b)>g(2L)/2=s_{R^2}/2\).

This lower bound is sharp: as \(z\uparrow2L\), \(y=g(2L-z)\downarrow0\) and \(x\uparrow g(2L)=s_{R^2}\). The corresponding positive rates \(a=h(x)/y\) and \(b=h(y)/x\) satisfy \(ab=R^2\), with \(a\to\infty\), \(b\to0\). Interchanging the types gives the other extreme.

To establish the claimed *strict monotonicity*, for \(z>L\) the derivative of \(g(z)+g(2L-z)\) is \(g'(z)-g'(2L-z)<0\) by strict concavity. Meanwhile
\[
\frac ab=\frac{x h(x)}{y h(y)}
\]
is a strictly increasing function of \(z\) on \((L,2L)\): its numerator increases with \(x=g(z)\), and its denominator decreases with \(y=g(2L-z)\). It equals 1 at \(z=L\) and tends to infinity as \(z\uparrow2L\). Symmetry in the types gives strict decrease with \(|\log(a/b)|\) everywhere off the balanced point.

**4. Subcritical expected total infections.** For \(R<1\), the expected total progeny vector from one ancestor of each type is \((I-M)^{-1}\mathbf1\), where
\[
(I-M)^{-1}=\frac1{1-ab}\begin{pmatrix}1&a\\b&1\end{pmatrix}.
\]
Averaging the two founder types gives \(E(a,b)=(2+a+b)/[2(1-R^2)]\). AM–GM yields \(a+b\ge2\sqrt{ab}=2R\), with equality exactly when \(a=b=R\), giving \(E\ge(1+R)/(1-R^2)=1/(1-R)\). At fixed product, \(a\to\infty\) makes this expectation unbounded. When \(R=1\), the nonnegative expected generation sizes do not form a summable series, since \(M^2=I\); extinction nonetheless holds by the critical nondegenerate branching theorem (or by concavity of the fixed-point map with derivative 1 at zero).

## Verification

The accompanying `verification.py` uses only Python's standard library. Running `python3 verification.py` executes 1,664 deterministic assertions. They include exact-rational confirmation of the subcritical expectation, coefficient monotonicity through degree 120 as a diagnostic, positivity of the analytic curvature at 999 interior sample points, numerical root-equation residuals and strict-range comparisons over multiple fixed reproduction numbers and directional imbalances, and convergence to the sharp lower bound. The infinite strict coefficient argument and the complete all-parameter conclusions are proved above independently of these finite checks.

## Relationship to prior work

Ball, Britton and Lyne (2004) develop multitype epidemic threshold theory and optimal vaccination allocation in a population of households, including a Perron-root threshold parameter and constraints on vaccination coverage. Their optimization concerns bringing a threshold below one, rather than comparing **nonextinction probabilities at an exactly fixed Perron root** or establishing the sharp risk interval above. Rao and Bauch (2006) discuss Galton–Watson epidemic extinction and vaccination in a single-type setting, rather than the directed two-type fixed-product extremum. Alexander and Day (2010) study multitype pathogen emergence with mutation and heterogeneous host contact structures, rather than the pure cross-type Poisson family with fixed \(ab\). Aravinda, Kovchegov, Otto and Sarkar (2024), in Sections 4–5, derive general multitype Poisson extinction equations and a series representation for their solutions, but do not optimize uniform-seed nonextinction probabilities along the fixed-Perron-root, cross-only two-type family or establish the sharp bounds. Singh, Schneider and Myers (2014) study zoonotic spillover and outbreak statistics in a coupled branching model; their accessible abstract does not establish the fixed-product inequality, and its unavailable full text is an outstanding priority risk. These connections establish motivation and methodological context, not independent priority certification. General multitype branching theory supplies the fixed-point and spectral threshold facts, which are not claimed new. A later heterogeneous-SIR concordance study (El Khalifi, 2026) concerns fixed trait marginals and concordance ordering, not the present fixed-geometric-mean directed-pair feasible set.

## Limitations

The result concerns an exact branching process with Poisson offspring, purely cross-type reproduction, a uniform index-case type, and fixed geometric mean \(\sqrt{ab}\); it is not a theorem for finite closed SIR epidemics, all multitype offspring distributions, unequal seed mixtures, or general mixing networks. Fixed spectral radius does not mean fixed total contact budget: \(a+b\) increases under imbalance. The lower bound is a limit over arbitrarily large directional rates and is not attained by finite rates. Clinical intervention costs and susceptible depletion are outside scope. Novelty is provisional pending independent priority review, especially of broader multitype epidemic optimization literature.

## References

1. F. Ball, T. Britton and O. Lyne, "Stochastic multitype epidemics in a community of households: estimation and form of optimal vaccination schemes," *Mathematical Biosciences* **191** (2004), 19–40. DOI: 10.1016/j.mbs.2004.05.001. Public online 2 July 2004; full text: https://staff.math.su.se/tom.britton/papers/J24.pdf.
2. A. S. R. Srinivasa Rao and C. T. Bauch, "Epidemic branching processes with and without vaccination," arXiv:math/0604607, first version 27 April 2006. https://arxiv.org/abs/math/0604607.
3. H. K. Alexander and T. Day, "Risk factors for the evolutionary emergence of pathogens," *Journal of the Royal Society Interface* **7** (2010), 1455–1474. DOI: 10.1098/rsif.2010.0123. Full text: https://www.pure.ed.ac.uk/ws/portalfiles/portal/123416830/rsif.2010.0123.pdf.
4. S. Singh, D. J. Schneider and C. R. Myers, "Using multitype branching processes to quantify statistics of disease outbreaks in zoonotic epidemics," *Physical Review E* **89** (2014), 032702. DOI: 10.1103/PhysRevE.89.032702. (Abstract and metadata compared.)
5. H. Aravinda, Y. Kovchegov, P. T. Otto and A. Sarkar, "Gelation in Vector Multiplicative Coalescence and Extinction in Multi-Type Poisson Branching Processes," arXiv:2409.06910 (first posted 10 September 2024). Full text: https://arxiv.org/abs/2409.06910.
6. M. El Khalifi, "Dependence Structure and Epidemic Outcomes in Heterogeneous SIR Models," arXiv:2601.01549 (2026). https://arxiv.org/abs/2601.01549. (Related later work under different invariants.)
