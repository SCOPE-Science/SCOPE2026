# A sharp concentrate-or-balance law for two-ephemeris transit follow-up

## Finding
Fix an integer \(n\ge4\) and a reliability \(p\in(0,1)\). An astronomical source is known to transit at exactly one of two disjoint candidate orbital phases, initially equally likely. There are \(n\) distinct orbital cycles with one observing opportunity per cycle; in each cycle the observer must select exactly one of the two candidate phases. Whenever the selected phase is the true phase, the transit is successfully recorded with probability \(p\), independently across cycles. A confirmed detection requires **at least two distinct recorded transits**. Let \(j\) cycles target the first candidate and \(n-j\) the second. Write
\[
F_p(k)=\Pr\{\operatorname{Binomial}(k,p)\ge2\}
 =1-(1-p)^k-kp(1-p)^{k-1}\quad(k\ge1),\qquad F_p(0)=0,
\]
so the unconditional confirmation probability is \([F_p(j)+F_p(n-j)]/2\).

There exists exactly one \(p_n\in(0,1)\) such that **every** globally optimal allocation, up to exchange of phases, is concentrated \((j=0)\) for \(0<p<p_n\), is as balanced as possible \((j=\lfloor n/2\rfloor)\) for \(p_n<p<1\), and consists precisely of these two allocation types at \(p=p_n\). All other allocations are strictly suboptimal, including at the transition.

The transition is explicit. For even \(n=2m\), \(m\ge2\), write \(q_n=1-p_n\). It is the unique root in \((0,1)\) of
\[
\sum_{k=0}^{m-1}q_n^k=2m q_n^{m-1}.
\]
For odd \(n=2m+1\), \(m\ge2\), it is the unique root of
\[
\sum_{k=m}^{2m-1}(k+1)q_n^k
 =\sum_{k=0}^{m-2}(k+1)q_n^k.
\]
In particular \(p_4=2/3\), and the large-budget transition obeys
\[
\lim_{n\to\infty}n p_n=c_* =2.51286241725234\ldots,
\quad e^{c_*/2}=1+c_*,\quad c_*>0.
\]

## Assumptions and scope
The two competing ephemerides have equal prior probabilities, are mutually exclusive, and do not overlap within an observation. Their common period is known, and a selected opportunity targets one complete transit in a distinct orbital cycle. A nonmatching phase cannot generate a positive transit. Conditional on a matching phase, per-opportunity success probability \(p\) is common, constant and independent; there are no false positives, adaptive reallocations, correlated outages or period uncertainty. The confirmation criterion counts distinct observed transits rather than individual photometric points. The result is a *static, conditional design* statement; it does not calculate a planet's geometric transit probability or the instrumental signal-to-noise of a transit.

## Proof
Put \(q=1-p\), \(K=n-1\), and \(H(j)=F_p(j)+F_p(n-j)\). Binomial complementation gives the displayed formula for \(F_p\), and for integers \(k\ge1\) the exact increment is
\[
F_p(k+1)-F_p(k)=k p^2q^{k-1}.
\]
Consequently, \(H(1)-H(0)=-(n-1)p^2q^{n-2}<0\). For \(1\le j<K/2\),
\[
\operatorname{sgn}[H(j+1)-H(j)]
=\operatorname{sgn} h(j),\qquad
h(x)=\log\!\frac{x}{K-x}+(2x-K)\log q.
\]
For \(0<x<K/2\),
\[
h''(x)=-\frac1{x^2}+\frac1{(K-x)^2}<0,
\quad \lim_{x\downarrow0}h(x)=-\infty,
\quad h(K/2)=0.
\]
Strict concavity implies that the nonnegative superlevel set of \(h\) on \((0,K/2]\) is a terminal interval (possibly just its right endpoint). Thus as \(j\) increases up to the balanced split, successive differences of \(H\) can change sign only from negative to positive. The first difference is strictly negative. Hence no nonterminal interior allocation maximizes \(H\); the only candidates are \(j=0\) and \(j=\lfloor n/2\rfloor\), and their reflected allocations. In the odd case \(H(m)=H(m+1)\) by symmetry.

For \(n=2m\), direct substitution and factorization give
\[
H(0)-H(m)=(1-q^m)\bigl[2mpq^{m-1}-(1-q^m)\bigr].
\]
With \(1-q^m=p\sum_{k=0}^{m-1}q^k\), the bracket has the sign of
\(2m-\sum_{k=0}^{m-1}q^{k-(m-1)}\). That expression is strictly increasing in \(q\in(0,1)\), from \(-\infty\) to \(m>0\). There is exactly one crossing. For \(q\) near one (small \(p\)), concentration wins; for \(q\) near zero it loses.

For \(n=2m+1\), the increment identity gives exactly
\[
H(0)-H(m)=p^2 P_m(q),\quad
P_m(q)=\sum_{k=m}^{2m-1}(k+1)q^k
 -\sum_{k=0}^{m-2}(k+1)q^k.
\]
The function \(P_m(q)/q^{m-1}\) is strictly increasing for all \(q>0\): every positive-coefficient term has a positive exponent, while every negative-coefficient term has a negative exponent. It tends to \(-\infty\) as \(q\downarrow0\), and its value at \(q=1\) is \(m(m+1)>0\). This proves the unique crossing and all equality cases. The even equation with \(m=2\) yields \(q_4=1/3\), hence \(p_4=2/3\).

Finally set \(p=z/n\) for fixed \(z>0\). The binomial-to-Poisson limit, applied to the displayed elementary formulas, gives
\[
\lim_{n\to\infty}[H(0)-H(\lfloor n/2\rfloor)]
=(1-e^{-z/2})\bigl[z e^{-z/2}-(1-e^{-z/2})\bigr].
\]
Its sign is strictly positive for \(0<z<c_*\) and strictly negative for \(z>c_*\), where \(e^{c_*/2}=1+c_*\). The equation has one positive solution besides the boundary solution zero because \(e^{z/2}-1-z\) decreases initially and then strictly increases to infinity. Since each finite-\(n\) crossing is unique, bracketing between any fixed \(z_-<c_*<z_+\) yields \(z_-<np_n<z_+\) for large \(n\), proving the limit.

## Verification
Run `python3 checker.py`. The standalone standard-library diagnostic checks every rational reliability with denominator at most 29 for each budget from 4 through 74, every possible integer allocation, the claimed strict dominance of nonterminal interior splits, the exact signs of both transition polynomials, and single-minimum finite differences. It also checks the \(n=4\) exact transition and numerically brackets the limiting constant. This run passed 1,693,847 diagnostic assertions. The all-integer and all-real statements above follow from the proof, not from this finite grid.

## Relationship to prior work
Von Braun, Kane and Ciardi (2009, arXiv:0907.1614v1) explicitly use a two-transit confirmation requirement and examine observing-run length, phase coverage, cadence, and noise effects. Their Sections 2.3 and 3.2–3.5 and Figures 3–6 compare observational windows, but do not classify allocations between two discrete rival ephemerides with independent visit failures. Dzigan and Zucker (2011, arXiv:1105.5393; MNRAS 415, 2513–2522), Section 2, develop Bayesian follow-up priorities from posterior peaks and iterative updating; they do not solve this static equal-prior, two-confirmation allocation problem. A relevant published mathematical study, *A sharp weather-reliability threshold for three transit-observation windows* (2026; public published-finding corpus record `4e69c33bc1b2`), proves an optimization over three continuous phase arcs; its domain is exactly three sessions and variable arc overlap, not arbitrary \(n\) and a two-point phase posterior. Its result and proof were inspected in full and do not imply the present discrete all-budget threshold classification. The elementary binomial-tail identities and discrete concavity argument are not themselves asserted to be new.

## Limitations
The model ignores partial transits, correlated weather, variable sensitivity, scheduling calendar constraints, unequal prior probabilities, false alarms, adaptive posterior updates and period aliasing. In particular, confirming two separate dimming events need not recover a unique orbital period. The classification is specific to two equiprobable phases and a two-success criterion; it should not be extrapolated to three candidate phases or higher success thresholds. Priority relative to older unindexed operations-research results on discrete binomial allocation cannot be completely excluded by a finite literature search. The result does not claim a new astrophysical measurement or an empirically optimized telescope program.

## References
1. K. von Braun, S. R. Kane, and D. R. Ciardi, *Observational Window Functions in Planet Transit Surveys*, arXiv:0907.1614v1 (public July 9, 2009), https://arxiv.org/abs/0907.1614, DOI:10.1088/0004-637X/702/1/779.
2. Y. Dzigan and S. Zucker, *Directed follow-up strategy of low-cadence photometric surveys in search of transiting exoplanets – I. Bayesian approach for adaptive scheduling*, arXiv:1105.5393 (May 26, 2011), DOI:10.1111/j.1365-2966.2011.18876.x, https://academic.oup.com/mnras/article/415/3/2513/1049486.
3. *A sharp weather-reliability threshold for three transit-observation windows*, publicly indexed in 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-weather-reliability-threshold-for-three-transit-observat--4e69c33bc1b2.
