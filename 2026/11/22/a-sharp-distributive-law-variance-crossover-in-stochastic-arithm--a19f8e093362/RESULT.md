# A sharp distributive-law variance crossover in stochastic arithmetic networks

## Finding

Two stochastic chemical reaction networks implement the same identity \((a+b)c=ac+bc\) at the level of stationary means, yet their stationary output variances exchange order along a sharp straight boundary. For positive source immigration rates \(a,b,c\), put \(s=a+b\) and \(m=sc\). The **factor-first** architecture has final output \(Y\), whereas the **distribute-first** architecture has final output \(Z\). Their exact variance difference is

\[
\boxed{\operatorname{Var}(Z)-\operatorname{Var}(Y)=\frac{m}{24}(4-3s-12c).}
\]

Thus the factor-first architecture has smaller stationary variance if and only if \(a+b+4c<4/3\); the distribute-first architecture has smaller stationary variance if and only if \(a+b+4c>4/3\). Equality holds exactly at \(a+b+4c=4/3\). Since both output means are \(m\), the same classification applies to Fano factors and to the variances of averages of independent stationary output samples. In the symmetric subfamily \(a=b=c\), equality occurs exactly at \(a=b=c=2/9\). The weight four on \(c\) means that equal total source intensity does not determine the preferred circuit.

## Assumptions and scope

For each \(T\in\{A,B,C\}\), the independent source process has births at constant rate \(a\), \(b\), or \(c\), respectively, and each individual dies at rate one. The sources are independent as *processes* and are sampled in their stationary Poisson immigration–death laws. All downstream birth channels use independent Poisson reaction randomness conditional on their upstream histories, and all downstream molecule lifetimes are independent exponential variables of rate one. Every birth-channel rate constant is one; all source parameters \(a,b,c\) are strictly positive. Upstream species are only catalysts, never consumed by downstream reactions.

In architecture F, \(X\) has catalytic birth intensity \(A+B\) and death intensity \(X\), while final \(Y\) has catalytic birth intensity \(XC\) and death intensity \(Y\). In architecture D, intermediate \(U\) and \(V\) have catalytic birth intensities \(AC\) and \(BC\) and unit death intensities; final \(Z\) has birth intensity \(U+V\) and death intensity \(Z\). Shared source \(C\) is **not** independently resampled between the two product channels. Every stationary process is defined by immigration events extending to the infinite past; finite moments and stationarity follow by successive conditional-Poisson constructions. The finding compares *single-time* stationary output variances and not temporal integrated autocorrelation.

## Proof

**1. The queue filter.** Given a jointly stationary nonnegative intensity process \(\Lambda\) with mean \(\mu\), let \(Q\) be the unit-death immigration process with conditional birth rate \(\Lambda\) and independently marked births. Its stationary construction implies

\[
\mathbb E Q=\mu,\qquad
\operatorname{Var}(Q)=\mu+\int_0^\infty e^{-t}K_\Lambda(t)\,dt,
\]

where \(K_\Lambda(t)=\operatorname{Cov}(\Lambda(0),\Lambda(t))\) for \(t\ge0\). Its two-time covariance has the form

\[
K_Q(t)=\mu e^{-t}+\int_0^\infty\!\int_0^\infty e^{-u-v}
K_\Lambda(t+u-v)\,du\,dv\qquad(t\ge0),
\]

using the even extension of the stationary covariance to all real lags. For the input mode \(e^{-\lambda|t|}\), convolution with the two exponential kernels produces

\[
F_1(t)=\frac{1+t}{2}e^{-t},\quad F_2(t)=\frac{2e^{-t}-e^{-2t}}{3},
\]

and direct integration yields

\[
\int_0^\infty e^{-t}F_1(t)\,dt=\frac38,\qquad
\int_0^\infty e^{-t}F_2(t)\,dt=\frac29.
\]

These follow either by splitting the integral at \(u-v=-t\) or evaluating the Laplace integrals of the elementary exponential-polynomial expressions. They require only integrable stationary covariance, which holds for the present networks.

**2. Factor first.** Since the independent sources \(A\) and \(B\) have the same unit decay parameter, \(S=A+B\) is a stationary immigration–death process of mean \(s=a+b\) with covariance \(K_S(t)=se^{-t}\). The intermediate \(X\) is a *second*, randomly driven immigration–death process: it is **not** stationary Poisson of mean \(s\). By the queue covariance formula,

\[
\mathbb E X=s,\qquad K_X(t)=s\bigl(e^{-t}+F_1(t)\bigr)
=\frac{s}{2}(3+t)e^{-t}.
\]

Importantly, the entire \(X\) process is independent of \(C\). Because \(\mathbb EC=c\) and \(K_C(t)=ce^{-t}\), independence gives the exact driver covariance

\[
K_{XC}(t)=c^2K_X(t)+s^2K_C(t)+K_X(t)K_C(t).
\]

The three terms have queue-variance integrals, respectively,

\[
c^2s\left(\frac12+\frac38\right),\quad
s^2c\left(\frac12\right),\quad
sc\left(\frac13+\frac12\left(\frac13+\frac19\right)\right).
\]

The final parentheses in the third term equal \(5/9\). The final output mean is \(m=sc\), hence

\[
\boxed{\operatorname{Var}(Y)=m\left(\frac{14}{9}+\frac{s}{2}+\frac{7c}{8}\right).}
\]

**3. Distribute first.** Conditioned on the common source paths \((A,B,C)\), the two independent output birth streams for \(U,V\) superpose. Their sum \(P=U+V\) is therefore exactly a unit-death Cox immigration process driven by \(AC+BC=SC\). The shared \(C\) must be retained: the two intermediate species are not independent. Independence of \(S\) and \(C\) instead gives

\[
\mathbb E(SC)=m,\qquad K_{SC}(t)=m(s+c)e^{-t}+me^{-2t}.
\]

Applying the queue filter once,

\[
K_P(t)=me^{-t}+m(s+c)F_1(t)+mF_2(t).
\]

The final \(Z\) is another unit-death queue driven by \(P\), so

\[
\boxed{\operatorname{Var}(Z)=m\left(1+\frac12+\frac{3(s+c)}8+\frac29\right)
=m\left(\frac{31}{18}+\frac{3(s+c)}8\right).}
\]

**4. Sharp comparison.** Subtraction gives

\[
\operatorname{Var}(Z)-\operatorname{Var}(Y)
=m\left(\frac16-\frac{s}{8}-\frac{c}{2}\right)
=\frac{m}{24}(4-3s-12c).
\]

Since \(m>0\), the signs and equality set in the finding follow without approximation. Each possible strict ordering occurs for open sets of positive parameters; the equality locus is attainable, for example at \(a=b=c=2/9\). The common mean is \(m\) because \(X\) is independent of \(C\), and because each of \((A,C)\) and \((B,C)\) is independent. This proves all stated conclusions.

## Verification

A standalone Python 3 script, `verify.py`, uses only the standard library and exact rational arithmetic. It independently reconstructs the queue-filter Laplace integrals, computes both architecture variances, and checks the closed forms and both strict sign branches over 216 positive rational source-rate triples. It reports 1,086 passed assertions on the enumerated test set. It also checks exact equality at \(a=b=c=2/9\) and strict reversal at two same-total-intensity parameter examples. These finite checks serve as arithmetic diagnostics only; the preceding integral and independence arguments establish the theorem for all positive real source rates.

## Relationship to prior work

Anderson and Moon [1] introduce the relevant catalytic arithmetic modules, illustrate *exactly these two distributive architectures* in their Figures 4–5, and derive the general stationary conditional-Poisson moment formulas (Section 4). Their architecture comparison in Section 6 treats repeated addition or repeated multiplication, not the exact mixed-operation variance ordering; Section 7 expressly identifies mixed arithmetic composition as a direction for further study. Therefore neither the general queue-filter identities nor the existence of these two diagrams is claimed as new here. The contribution is their exact specialized combination with dependent parallel intermediate species, an explicit joint structural cancellation, and the sharp anisotropic variance-ordering boundary for all positive source intensities.

Dean and Ganesh [2] study second-order noise dissipation in a tandem of modulated infinite-server queues, supplying relevant earlier context for linear cascade filters. Available publisher material does not establish a direct distributive-architecture comparison. Its complete text was not accessible for a conclusive implication check, so an unlocated earlier equivalent specialization cannot be ruled out. General Cox-queue covariance formulas are treated as prior tools, not newly discovered lemmas.

## Limitations

Only stationary *single-time variance* is compared. The result does not compare autocovariance-integrated time-series readout error, transient convergence, rates other than one, extra correction/identification modules, or architectures outside the two specified. The independence of all three source processes and independent reaction randomness is substantive. No claim of historical uniqueness or external mathematical validation is made; priority may require additional literature review, especially of earlier queue-network papers available only through restricted full text.

## References

[1] David F. Anderson and Seokhwan Moon, *Mean-level arithmetic computation via stochastic reaction networks*, arXiv:2611.11069v1, first public version November 8, 2026. https://arxiv.org/html/2611.11069v1

[2] Justin J. Dean and Ayalvadi Ganesh, *Noise dissipation in gene regulatory networks via second order statistics of networks of infinite server queues*, Journal of Mathematical Biology 85 (2022), article 14. https://doi.org/10.1007/s00285-022-01781-9
