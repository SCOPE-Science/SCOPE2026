# Arithmetic capture and exact firing-rate staircases on periodic observation windows

## Finding

Let \(0<\eta<1\), let \(m\) be a nonnegative integer, and let \(0<\beta<1\). On the closed, periodic observation-time domain
\[
\mathcal T_\eta=\bigcup_{k\in\mathbb Z}[k,k+\eta],\qquad \tau=m+\beta>0,
\]
consider the projected threshold-reset firing clock
\[
t_{j+1}=\Pi^+_{\mathcal T_\eta}(t_j+\tau),\qquad t_0\in\mathcal T_\eta.
\]
Write \(\{y\}=y-\lfloor y\rfloor\) and \(R_\beta(x)=\{x+\beta\}\). Its phase map on \([0,\eta]\) is the explicit **rotation-with-reset map**
\[
F(x)=\begin{cases}R_\beta(x),&R_\beta(x)\le\eta,\\0,&R_\beta(x)>\eta.\end{cases}
\]
All firing phases eventually belong to a periodic orbit (although the original time-domain spikes need not become synchronized to the same absolute clock epoch). The complete classification is:

1. If \(\beta\) is irrational, or if \(\beta=p/q\) in lowest terms with \(\eta<1-1/q\), define
\[
r=\min\{j\ge1:\{j\beta\}>\eta\}.
\]
Then \(r\) is finite and every phase enters in finite time the **same** periodic phase orbit \(\mathcal O=\{\{j\beta\}:0\le j<r\}\), whose least period is \(r\). Its unique invariant phase probability is \(r^{-1}\sum_{j=0}^{r-1}\delta_{\{j\beta\}}\). For every starting spike the asymptotic physical-time firing rate is
\[
\boxed{\nu(\eta,\beta,m)=\frac{r}{mr+\lceil r\beta\rceil}.}
\]
Moreover, this orbit experiences precisely one positive projection delay per cycle of \(r\) spikes, of size \(\lceil r\beta\rceil-r\beta\).

2. If \(\beta=p/q\) in lowest terms and \(\eta\ge1-1/q\), let
\[
E=\{x\in[0,\eta]: \{x+jp/q\}\le\eta\text{ for }j=0,\ldots,q-1\}.
\]
Every phase enters \(E\) after at most \(q\) iterates; \(F\) is rotation by \(p/q\) on \(E\), so each point of \(E\) belongs to a free \(q\)-cycle and
\[
\boxed{\nu(\eta,p/q,m)=\frac{q}{mq+p}.}
\]
The survivor set has exact Lebesgue length \(|E|=q\eta-q+1\). At \(\eta=1-1/q\), \(E\) is the single \(q\)-point orbit \(\{0,1/q,\ldots,(q-1)/q\}\), and the invariant phase probability is unique. For \(\eta>1-1/q\), \(E\) contains a continuum of distinct \(q\)-cycles and invariant probabilities are not unique; the length of initial phases eventually projecting onto the distinguished orbit of phase zero is \((q-1)(1-\eta)\) (aside from that orbit itself, which has length zero).

For every fixed irrational \(\beta\), the frequency as a function of observation width \(\eta\) is a nondecreasing rational-valued step function with a strictly positive jump exactly at each successive upper record of \(\{j\beta\}\). It approaches the continuously available firing rate \(1/\tau\) as \(\eta\uparrow1\), though every \(\eta<1\) yields an atomic periodic phase measure. More precisely, with \(r=r(\eta,\beta)\),
\[
0<\frac1\tau-\nu<\frac{1-\eta}{r\tau^2}.
\]
If \(\beta\) is badly approximable in the explicit sense \(\|j\beta\|\ge c/j\) for every positive integer \(j\) and some \(c>0\), the upper bound improves to \((1-\eta)^2/(c\tau^2)\).

## Assumptions and scope

The first spike is any point of \(\mathcal T_\eta\); indexing begins at that spike. The physical travel time \(\tau\) is fixed between resets, as in the constant-input structure-preserving leaky integrate-and-fire model of Kaymakçalan and Selçuk. Time has been normalized so that the observation pattern has period one; \(\eta\) is its nonzero open fraction. We exclude the integral travel-time case \(\beta=0\), for which every phase remains fixed and no analogous irrational/resonance dichotomy occurs. On \(\mathbb Z\)-translates of a phase orbit, one obtains the same firing pattern after an integer shift; uniqueness of the phase orbit does not assert coincidence of absolute firing times for differently initialized clocks.

## Proof

**Phase reduction.** Write \(t=k+x\) with integer \(k\) and \(0\le x\le\eta\). The target time is \(k+m+x+\beta\). Its fractional part is \(R_\beta(x)\). If that fractional part lies in \([0,\eta]\), the target belongs to \(\mathcal T_\eta\) and is unchanged. Otherwise the target lies in the missing interval \((k',k'+1)\) after its open part and projects to the following integer, phase zero. This gives the displayed formula for \(F\). Before the first projection delay, the phases are exactly successive iterates of the rotation \(R_\beta\).

**Finite capture and the unique orbit when the hole is reached from zero.** Put \(H=(\eta,1)\) on the circle and let \(r\) be the first positive rotation time of zero into \(H\). The orbit starting at zero has phases \(\{j\beta\}\) for \(0\le j<r\), then returns to zero on its next iteration, hence has least period \(r\): no earlier positive iterate can equal zero in the irrational case; in the rational case considered here, \(r<q\). For irrational \(\beta\), every circle orbit meets the nonempty open interval \(H\) by minimality of irrational rotation, so every initial phase eventually resets to zero and enters this orbit. Compactness also gives a uniform finite upper bound on first-reset times: the sets \(R_\beta^{-j}(H)\), \(j\ge1\), cover the circle and admit a finite subcover. If \(\beta=p/q\), every orbit consists of \(q\) evenly spaced phases; if \(1-\eta>1/q\), this orbit must intersect the open interval \(H\). Thus every phase resets within \(q\) steps. The point-zero orbit does likewise, with \(r<q\).

**Exact clock period and unique invariant phase probability.** Starting from integer time zero, the first \(r-1\) target times are allowed exactly, so \(t_j=j\tau\) for \(0\le j<r\). The next target \(r\tau\) falls into a missing interval (its fractional part exceeds \(\eta\)), and therefore \(t_r=mr+\lceil r\beta\rceil\), an integer. The same clock segment repeats after that integer translation. Every phase orbit is eventually captured, and the only invariant probability on this finite attracting cycle is its uniform orbit measure. Every initial spike therefore has the displayed limiting firing rate. The sole nonzero delay in the block is \(\lceil r\beta\rceil-r\beta\), strictly between zero and \(1-\eta\).

**The rational resonance threshold.** For \(\beta=p/q\) reduced, the orbit of zero contains precisely the fractions \(0,1/q,\dots,(q-1)/q\). It avoids \(H\) exactly when \(\eta\ge1-1/q\). In this case the set \(E\) of phases never visiting \(H\) is the complement in the unit circle of the \(q\) translated open arcs \(H-jp/q\). Since their common length \(1-\eta\) is at most \(1/q\), those arcs are disjoint except possibly at boundary points; hence \(|E|=1-q(1-\eta)\). A point outside \(E\) reaches \(H\) in at most \(q\) free rotation steps and is sent to zero, which belongs to \(E\). For every \(x\in E\) the next \(q\) spikes are undelayed, and their total elapsed time is \(q\tau=mq+p\). At equality the translated arcs partition the circle except for the lattice of \(q\) boundary points, which form one periodic orbit. Above equality each complementary arc has positive length, producing continuum many distinct \(q\)-orbits. The set of phases which incur at least one delay is \([0,\eta]\setminus E\), whose length is \(\eta-(q\eta-q+1)=(q-1)(1-\eta)\). Since every orbit enters \(E\), every invariant probability is supported there, proving both uniqueness at equality and nonuniqueness above it.

**Frequency staircase and the zero-blackout limit.** At fixed irrational \(\beta\), the first hit time \(r(\eta)\) changes only as \(\eta\) passes a new strict record high in the sequence \(\{j\beta\}\). Those records strictly increase, and their indices strictly increase. For each record index \(r\), let \(d_r=1-\{r\beta\}=\lceil r\beta\rceil-r\beta\). The exact rate is \(\nu=(\tau+d_r/r)^{-1}\). Along successive records, \(d_r\) strictly decreases while \(r\) increases, so the rates strictly increase. Since the rotation is irrational, records approach one and their times diverge; the discrepancy is
\[
\frac1\tau-\nu=\frac{d_r/r}{\tau(\tau+d_r/r)}<\frac{1-\eta}{r\tau^2}.
\]
Under the stated Diophantine condition, \(d_r\ge\|r\beta\|\ge c/r\) and \(d_r<1-\eta\), hence \(r>c/(1-\eta)\). Substitution gives the claimed quadratic upper bound. The limiting time scale \(\eta=1\) has no blackout and becomes a rigid irrational phase rotation, showing the singular change in phase measures at the endpoint.

## Verification

The self-contained script `verification/check.py` performs exact rational arithmetic for reduced fractions with denominators from two to twelve, sampling widths both at and off the critical value, and checks the phase map, finite capture, recurrence periods, exact firing rates and exceptional-set lengths. It also performs high-precision finite tests for the golden-mean irrational rotation. Its recorded output was `PASS rational parameter cases 2356 exact and high-precision checks 210492`. These computations are finite stress tests; the stated global and infinite-time conclusions are established by the analytic proof above.

## Relationship to prior work

Kaymakçalan and Selçuk (2026, sections 5–6) prove the forward-projection firing recursion for arbitrary closed time scales and the lattice formula, and explicitly leave periodic time-scale arithmetic for later study in their discussion (section 8). The present result uses their recursion but classifies an essentially different one-periodic *interval-window* time scale: it identifies the arithmetic trapping mechanism, exact rate plateaux, sharp rational threshold, and exceptional phase mass. Earlier studies of periodically *forced* integrate-and-fire neurons demonstrate mode locking and Arnold tongues; their forcing dynamics is not the constant-input, periodically restricted observation clock treated here. Classical irrational-rotation minimality and elementary rational orbit geometry underlie the proof, and should not be regarded as new abstract lemmas. Bunimovich and Dettmann analyse survival for open circular billiards via periodic orbits, and Anagnostopoulou et al. classify entrance times for expanding flat-spot circle maps. The rational survivor-set calculation here is an elementary rotation-with-a-hole fact, not claimed as a novel general survivor theorem; the new object of study is the physically elapsed reset clock, with its capture and frequency classification. The flat-spot paper assumes a continuous circle map and strict expansion away from the flat spot, hypotheses absent from the piecewise rigid discontinuous map considered here.

## Limitations

The classification concerns a single interval of observation opportunity per period, a fixed reset-to-threshold travel time, and the on-time-scale (not event-enriched) spike semantics. It does not classify multiple windows, variable input, stochastic observation, or coupled neurons. The result supplies exact phase and time frequencies but no claim about noise robustness or physiological realism. Although inspected related work did not exhibit the complete specific classification, a preexisting equivalent theorem for a reset rotation with a hole may subsume it; historical-priority uncertainty remains.

## References

1. B. Kaymakçalan and B. İ. Selçuk, *Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales*, arXiv:2611.17219v1 (first public 2026-11-12), https://arxiv.org/html/2611.17219v1 .
2. P. H. E. Tiesinga, *Precision and reliability of periodically and quasiperiodically driven integrate-and-fire neurons*, Physical Review E 65 (2002), 041913, https://doi.org/10.1103/PhysRevE.65.041913 .
3. J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, and G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495 (2024), https://arxiv.org/abs/2411.01495 .
4. P. Glendinning, S. Ma, and J. Montaldi, *Piecewise linear circle maps and conjugation to rigid rational rotations*, arXiv:2505.13689 (2025), https://arxiv.org/abs/2505.13689 .
5. L. A. Bunimovich and C. P. Dettmann, *A Billiard in an Open Circle and the Riemann Zeta Function*, Experimental Mathematics 35 (2026), 24–48 (online 2024-11-18), https://doi.org/10.1080/10586458.2024.2423180 .
6. V. Anagnostopoulou, K. Díaz-Ordaz, O. Jenkinson, and C. Richard, *Entrance Time Functions for Flat Spot Maps*, Nonlinearity 23 (2010), 1477–1494, https://doi.org/10.1088/0951-7715/23/6/011 .
