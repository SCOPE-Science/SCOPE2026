# Independent mathematical audit

## correctness

PASS

The random cyclic anchor makes all circular spacings Dirichlet(1,...,1). Conditioning on a clockwise r-gap partial sum Beta(r,n-r) and reweighting the disjoint opposing gap produces a Beta(r,n-r+1) order-statistic integral; a centered binomial absolute-moment identity gives Delta_n=1/4−2^(−n−1)binom(n,(n−1)/2) for odd n. Uniform deletion from even n preserves iid uniform remaining locations and adds an independent omitted agent with conditional mean distance 1/4, yielding Delta_(n−1). The empirical circle cost process H_n(t)=sqrt(n)(average d(X_i,t)−1/4) has bounded fourth increments and finite-dimensional Gaussian limit in C(T), covariance 1/48−h²/2+2h³/3. Its exact antipodal symmetry implies sup G=−inf G>0 almost surely. The PCD/EPCD opposing-gap selection measures converge weakly to Haar uniformly in continuous test functions; tightness of H_n upgrades their integrals to o_P(1). Therefore all conditional selected costs equal n/4+o_P(sqrt(n)), while optimum equals n/4+sqrt(n)min H_n, giving the common joint 4 sup G limit and non-Gaussian positive law. Independent exact rational identity checks reproduced Delta_3=1/16, Delta_5=3/32, Delta_7=29/256, Delta_9=65/512. Numerical Monte Carlo in the checker is not used as an infinite proof.

## originality

PASS

Meir 2019, Rogowski–Dziubiński 2025 and Chan–Lin–Wang 2026 introduce PCD, RD mixtures and EPCD and analyze strategic worst-case approximation guarantees. They do not assert in their inspected central statements the iid Haar average conditional cost exact gain or joint Gaussian-supremum fluctuation. Generic empirical-process weak convergence proves only one analytic step, not the mechanism-specific Dirichlet cost identity or opposing-gap selection weak limit. Best-of-knowledge positive but specialized older average-case and inaccessible sections of the latest primary paper remain risks.

## value

PASS

The exact finite-population expected gain is a natural performance metric under a homogeneous input distribution and distinguishes lotteries whose worst-case guarantees differ. The non-Gaussian Gaussian-supremum law quantifies the first stochastic order of approximation inefficiency and shows three mechanism ratios share a fluctuation limit despite distinct unconditional costs. This is a motivated concrete mechanism-specific comparison, not merely a general empirical-process exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
