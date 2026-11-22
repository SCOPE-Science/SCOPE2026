# Prime-power observation complexity and a cadence barrier for duotransit period aliases

## Finding

Suppose a strictly periodic transiting object produces observed transit midpoints separated by a baseline \(\Delta>0\), with no informative observations at intervening times. The remaining candidate orbital periods are exactly \(\Delta/k\), for integers \(1\le k\le N\), with \(N\ge2\). A nonadaptive follow-up program consists of predetermined instantaneous photometric probes after the second observed transit. Each probe reports reliably whether a transit occurs at the probed time.

**Theorem.** Let \(\mathcal Q_N=\{p^a: p\text{ prime},\ a\ge1,\ p^a\le N\}\) and \(Q_N=|\mathcal Q_N|\). The least number of nonadaptive probes whose complete binary detection vector uniquely determines \(k\) for *every* \(1\le k\le N\) is exactly \(Q_N\). One optimal set of times is

\[
 t_q=\Delta(1+1/q),\qquad q\in\mathcal Q_N.
\]

Every successful program must, for each \(q\in\mathcal Q_N\), include a probe at a time whose fractional phase after the second observed transit has reduced denominator exactly \(q\). If instead only the longest period \(\Delta\) needs to be certified by all-negative probes, exactly \(\pi(N)\) probes are necessary and sufficient, using prime denominators.

If probes are constrained to a uniform exact timing grid \(t=\Delta(1+j/H)\), \(j\in\{1,\ldots,H-1\}\), a universally identifying program exists **if and only if**

\[
\operatorname{lcm}(1,2,\ldots,N)\mid H.
\]

Thus the smallest permissible regular-grid denominator is \(L_N=\operatorname{lcm}(1,\ldots,N)\), even though the flexible schedule requires only \(Q_N\) observations.

**Finite-duration robustness.** Suppose, instead, a probe at phase \(x\in(0,1)\) reports a detection exactly when it lies at circular phase distance at most \(\varepsilon\) from a transit midpoint of the candidate, with common \(0\le\varepsilon<1/(2N^2)\). (Equivalently, a known common transit half-duration and observational timing tolerance have been folded into \(\varepsilon\Delta\).) The minimal number of nonadaptive probes is **still exactly** \(Q_N\), and the proposed \(1/q\) schedule still works. The regular-grid characterization above is asserted only at \(\varepsilon=0\).

For example, \(N=12\) requires exactly eight flexible probes at phases \(1/2,1/3,1/4,1/5,1/7,1/8,1/9,1/11\), but an exact regular grid must have at least \(27720\) subdivisions. For \(N=38\), the corresponding figures are \(19\) probes and \(5342931457063200\) subdivisions. The latter number is an *idealized exact-epoch arithmetic requirement*, not a practical instrument specification.

## Assumptions and scope

Time is measured relative to the second known transit, with fractional phase \(x=(t/\Delta)-1\in(0,1)\). There is one strictly periodic clock, no transit-time variations, no second body, no missed/false detections, and no uncertainty in \(\Delta\). For candidate \(k\), ideal transit midpoints in this cycle are \(x=j/k\), with \(j=1,\ldots,k-1\). The two discovery transits are known and provide no additional information among the remaining candidates. All integers \(1\le k\le N\) are assumed physically admissible and have not been pruned by ancillary photometry. Each follow-up probe is a binary, predetermined, equal-cost question. There are no visibility or weather constraints. Nonadaptive identification is stronger than certification of one specified candidate. In the finite-duration variant the same dimensionless tolerance applies to every alias, and a probe is positive iff at least one midpoint is within \(\varepsilon\) in normalized phase. Because \(\varepsilon<1/(2N^2)\le1/8\), there are no wraparound ambiguities near phase endpoints affecting the chosen interior probes; the proofs also hold using circular distance.

## Proof

**1. Arithmetic incidence.** Write a probe phase in lowest terms as \(x=a/b\) with \(0<a<b\) and \(\gcd(a,b)=1\). It is a transit under candidate \(k\) precisely when \(kx\) is an integer; this is equivalent to \(b\mid k\). An irrational phase is never a midpoint for any candidate and cannot distinguish them. Thus the exact binary observation is a *divisibility query on the unknown alias index*.

**2. Mandatory prime-power probes.** Fix \(q=p^a\le N\), and compare candidates \(k=q\) and \(k'=q/p\). These must have distinct binary vectors in any universally identifying program. Every divisor of \(q/p\) divides \(q\), so the only possible distinguishing response is a transit for \(q\) but not for \(q/p\). By Step 1 its reduced denominator \(b\) must divide \(q\) but not \(q/p\). Among divisors of the prime power \(q\), the unique such \(b\) is \(q\) itself. Consequently some probe has reduced denominator \(q\). Distinct prime powers require distinct probes, proving the lower bound \(Q_N\).

**3. Sharp construction and certificates.** Probe at \(x_q=1/q\) for every prime power \(q\le N\). The response for candidate \(k\) is \(\mathbf 1_{q\mid k}\). For each prime \(p\le N\), these bits record exactly the maximal exponent \(a\) for which \(p^a\mid k\). Unique factorization then recovers \(k\) from its vector. In particular, the all-negative vector corresponds exactly to \(k=1\). If only \(k=1\) is to be certified, each prime candidate \(k=p\) forces one denominator-\(p\) probe; all primes suffice since every \(k\ge2\) has a prime divisor. This proves the \(\pi(N)\) minimum.

**4. Exact regular grid.** Every reduced denominator of \(j/H\) divides \(H\). Step 2 therefore forces \(q\mid H\) for every prime power \(q\le N\), equivalent to \(L_N\mid H\). Conversely if \(L_N\mid H\), all \(1/q\) phases occur on the grid as \(j=H/q\), and Step 3 gives an identifying program. This proves necessity and sufficiency without assuming that *every* grid point is observed.

**5. Positive-duration robustness.** The midpoint set for alias \(q/p\) is a subset of the midpoint set for alias \(q=p^a\). Any probe distinguishing these two aliases when each transit is widened by \(\varepsilon\) must lie within \(\varepsilon\) of an additional midpoint \(j/q\) with \(\gcd(j,p)=1\); otherwise detection for \(q\) would imply detection for \(q/p\). Such a fraction has reduced denominator exactly \(q\). Distinct reduced fractions \(a/b\ne c/d\), with \(b,d\le N\), satisfy

\[
 \left|\frac{a}{b}-\frac{c}{d}\right|=\frac{|ad-bc|}{bd}\ge\frac{1}{N^2}.
\]

When \(2\varepsilon<1/N^2\), a single probe cannot lie within tolerance of additional midpoints with two different prime-power denominators; therefore Step 2's \(Q_N\) lower bound persists. Conversely, at \(x=1/q\), every alias divisible by \(q\) yields a transit, while any alias \(k\) not divisible by \(q\) has all its midpoint phases \(j/k\) at distance at least \(1/(qk)\ge1/N^2>\varepsilon\). Hence the finite-tolerance response vector is exactly the divisibility vector from Step 3, giving the matching upper bound.

## Verification

The included standalone `checker.py` uses exact rational arithmetic to test full distinctness of the proposed signatures for \(2\le N\le150\), mandatory prime-power witness coordinates, small-\(N\) finite-tolerance signatures, separation of reduced fractions, and the stated constants. On execution it prints `PASS: 11025 exact assertions`. These finite checks do not prove the universal theorem; the proof is Steps 1–5. The chosen examples are \(Q_{12}=8\), \(L_{12}=27720\), \(Q_{38}=19\), and \(L_{38}=5342931457063200\).

## Relationship to prior work

Cooke et al. (2020) analyze follow-up photometry and spectroscopy for TESS single-event recurrences and show how two separated transits leave integer-divisor period aliases. Hawthorn et al. (2023) survey duotransit targets and describe targeted follow-up on discrete aliases. Osborn et al. (2022) combine candidate-alias priors and actual targeted CHEOPS observations. Those works supply the physical problem and practical scheduling context. The theorem here isolates an idealized *worst-case, nonadaptive, all-alias* binary identification question, for which prime-power necessity and regular-grid divisibility give exact minima. It is not a replacement for realistic Bayesian, adaptive, noise-aware scheduling. Unique factorization and the rational-separation bound are established mathematical facts, not novel lemmas. An earlier public mathematics question, *Minimum number of divisibility tests required in order to identify a number between 1 and n* (Math Stack Exchange, 2016-08-09), expressly poses the equivalent integer-divisibility test-count problem and gives the small examples for 4 and 6. It contains no posted proof or general answer in the inspected content. Accordingly the arithmetic question, its simple examples, and its divisor-oracle reformulation are prior art; the combined astronomical timing, finite-duration threshold and exact-grid feasibility classification are the distinctions assessed here.

## Limitations

The exact optimality is confined to the fully retained alias set \(\{\Delta/k:1\le k\le N\}\), one stable orbital clock, common known transit tolerance, reliable independent binary readout, arbitrarily schedulable epochs, equal probe costs and nonadaptive planning. Actual observing campaigns have daylight, weather, instrument overhead, finite time baselines, uncertain ephemerides, unequal prior likelihoods and candidate-dependent transit durations; these can radically change an optimal schedule. Adaptive programs can use positive detections to reduce the remaining possibilities and need not meet the nonadaptive lower bound. The regular-grid obstruction is exact-time arithmetic only: it does not extend to any positive finite tolerance. These mathematical minima have not been independently validated against observational data or the complete historical mathematical literature.

## References

1. Cooke, B. F., et al., *Resolving period aliases for TESS monotransits recovered during the extended mission*, arXiv:2011.05832v1 (first public 2020-11-11); DOI: 10.1093/mnras/staa3569. Full primary preprint consulted, including Sections 2–5 and Appendix A. https://arxiv.org/abs/2011.05832
2. Osborn, H. P., et al., *Uncovering the true periods of the young sub-Neptunes orbiting TOI-2076*, arXiv:2203.03194 (2022); DOI: 10.1051/0004-6361/202243065. Author manuscript and relevant alias-follow-up discussion consulted. https://arxiv.org/abs/2203.03194
3. Hawthorn, F., et al., *TESS Duotransit Candidates from the Southern Ecliptic Hemisphere*, arXiv:2310.17268v1 (first public 2023-10-26); DOI: 10.1093/mnras/stad3783. Full primary preprint consulted for the period family, selection methodology, follow-up discussion, and appendices. https://arxiv.org/abs/2310.17268
4. *Minimum number of divisibility tests required in order to identify a number between 1 and n*, Mathematics Stack Exchange, asked 2016-08-09. Question and comments inspected; an equivalent unproved arithmetic optimization question predates this result. https://math.stackexchange.com/questions/1886768/minimum-number-of-divisibility-tests-required-in-order-to-identify-a-number-betw
