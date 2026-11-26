# Independent mathematical audit

## correctness

PASS

The survival ratio with S(-1)=1 gives log[(1-h(k+1))/(1-h(k))]=B_k-tD_k, including k=0. B_k>0 and concavity gives D_k<=0 when beta<=1. For beta>1, express D_k via the triangular second-difference kernel. The two adjacent kernels after multiplying by x^(beta-2) have likelihood ratio increasing from zero through (x-k-1)/(k+2-x) to infinity. Tilting by x^epsilon increases the adjacent D ratio strictly; the integrals near zero are finite because w(x)=x there. At beta=1+ the limiting d_k satisfies B_k/d_k=E[g(k+U)] with g(x)=x/(x+1)^2 and density for U proportional to w(u)/(k+u). For k>=1 this expectation strictly decreases as k increases: the density shifts stochastically right and g is decreasing on that range. This proves strict tail threshold descent. The independently computed rational comparisons d1/d0<2/5<B1/B0 and B2/d2<1/5<B0/d0, with d0=2 log 2 and d2=10 log 2-6 log 3, prove the initial inversion at beta=1+ and T2<T0 for all beta>1 by the ratio monotonicity. D1/D0 tends to infinity, so there is one crossing. T0 and T1 are the only possible coincident thresholds, giving exactly the stated length-three plateau. In the open two-turn region T0<t<T1 all indices k>=2 have positive increments. At t=T0<T1 the signs begin zero, negative, positive; at t=T1>T0 they begin positive, zero, positive. At beta=beta_c, T0=T1, so threshold descent from index zero is non-strict at that one pair. The exact comparison in RESULT.md governs all ties. The kernel asymptotics give T_k~1/[beta(beta-1)k^beta], and bracketing the first k with T_k<=t between neighboring thresholds yields the stated index limit for fixed beta>1. Independent replay: python3 /workspace/checks/hazard_endpoints.py exactly verifies the two logarithmic comparisons and reproduces the critical decimals (bisection is diagnostic, not the uniqueness proof). VERIFICATION.md and check_hazard.py were read, not executed; the script's static count is 238 as in VERIFICATION.md, not 227 as reported in RESULT.md. This documentation discrepancy does not affect the analytic result or the independent exact comparisons.

## originality

PASS

The DGBH law, hazard formula and several qualitative plotted shapes are already published. The distinct result is the exact infinite-support classification with a unique early threshold crossing, an analytic nonempty region for the count-one peak and count-two trough, the isolated triple plateau, and the late-turn scale. This assessment credits the qualitative overlap and does not claim that complex DGBH hazard shapes themselves are new.

## value

PASS

The result replaces plots on finite count ranges by an all-count decision rule and establishes sharp structural facts not visible reliably in near-flat plots, especially the unique three-count equality and the exact peak and trough coordinates. The delayed-turn scale explains how a finite window can miss eventual increase. This is useful within the published DGBH model, independent of any claim about fitting data or competing lifetime laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
