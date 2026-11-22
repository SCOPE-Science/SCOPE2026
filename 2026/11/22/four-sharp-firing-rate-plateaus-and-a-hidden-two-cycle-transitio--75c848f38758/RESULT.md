# Four sharp firing-rate plateaus and a hidden two-cycle transition on three-phase clocks

## Finding
For the constant-input, threshold-reset leaky integrate-and-fire model with firing opportunity times
\[\mathcal T=\mathbb Z\cup(\mathbb Z+\alpha)\cup(\mathbb Z+\beta),\qquad0<\alpha<\beta<1,\]
write the three cyclic opportunity gaps in increasing *size* as \(a\le b\le c\), with \(a+b+c=1\). Let the continuous reset-to-threshold travel time be \(s\), where \(0<s<1\). Starting after any spike \(t_0\in\mathcal T\), define subsequent firing times recursively by
\[t_{n+1}=\min\{u\in\mathcal T:u\ge t_n+s\}.\]
The physical-time firing frequency \(\nu(s)=\lim_{n\to\infty}n/(t_n-t_0)\) exists, is independent of initial phase and is exactly
\[
\nu(s)=\begin{cases}
3,&0<s\le a,\\
2,&a<s\le c,\\
\tfrac32,&c<s\le1-c,\\
1,&1-c<s<1,
\end{cases}\quad (c<\tfrac12),
\]
and
\[
\nu(s)=\begin{cases}
3,&0<s\le a,\\
2,&a<s\le1-c,\\
1,&1-c<s<1
\end{cases}\quad(c\ge\tfrac12).
\]
Empty parameter ranges are omitted. In particular, four distinct plateaus are possible, and four is the maximal number for a period-one opportunity clock with three phases and \(0<s<1\).

For the concrete asymmetric clock \(\alpha=1/4\), \(\beta=2/3\), there are **five** sharp consecutive spike-train laws. In each row the displayed interspike intervals repeat cyclically after a finite transient; all endpoints are as indicated:

| Travel time \(s\) | Firing rate | Repeating interspike intervals | Interspike variance |
| --- | ---: | --- | ---: |
| \(0<s\le1/4\) | \(3\) | \(1/4,5/12,1/3\) | \(1/216\) |
| \(1/4<s\le1/3\) | \(2\) | \(2/3,1/3\) | \(1/36\) |
| \(1/3<s\le5/12\) | \(2\) | \(5/12,7/12\) | \(1/144\) |
| \(5/12<s\le7/12\) | \(3/2\) | \(2/3,7/12,3/4\) | \(1/216\) |
| \(7/12<s<1\) | \(1\) | \(1\) | \(0\) |

Thus \(s=1/3\) is a **rate-invisible spike-pattern transition**: the frequency remains \(2\) but the limiting interspike variance changes sharply by a factor of four.

## Assumptions and scope
The time scale is the bi-infinite, closed, period-one discrete set above; periods are measured in physical time, not event count. The neuron has constant input \(V_\infty>V_{th}>V_r\), positive membrane time constant \(\tau_m\), and \(s=\tau_m\log[(V_\infty-V_r)/(V_\infty-V_{th})]\in(0,1)\). Firing is only permitted at opportunity times, and every firing resets immediately. The first spike may be at any opportunity phase. The three gaps are the successive differences \(\alpha\), \(\beta-\alpha\), and \(1-\beta\), sorted as \(a\le b\le c\); the theorem is independent of their cyclic order.

## Proof
The published forward-projection law for this constant-input model gives the recurrence in the finding. Put \(F_s(t)=\min\{u\in\mathcal T:u\ge t+s\}\). It is nondecreasing and satisfies \(F_s(t+1)=F_s(t)+1\) on opportunity times. Therefore, for any two starting opportunities after an integer translation, \(t\le u<t+1\), monotonicity gives
\[F_s^n(t)\le F_s^n(u)\le F_s^n(t)+1.\]
The residues of iterates modulo one lie in a finite set of three phases. Every orbit is eventually cyclic in phase, say with \(m\in\{1,2,3\}\) distinct residues and net advancement \(q\) integer periods. Its physical-time frequency is \(m/q\). The preceding squeeze inequality shows that this frequency is the same for all starting phases.

Every jump from one phase to another distinct phase has duration strictly below one, because \(s<1\), and a jump returning to the same phase has duration exactly one. Consequently, a one-phase orbit has frequency \(1\), a two-phase orbit has total duration one and frequency \(2\), and a three-phase orbit has total duration one or two and hence frequency \(3\) or \(3/2\). This proves that **no other rates occur**.

To identify which possible rate is realized, note that forward projection is the greedy earliest-feasible schedule. If an alternative infinite periodic schedule begins at the same opportunity and has gaps at least \(s\), its \(n\)-th event cannot precede the \(n\)-th greedy event, by induction. Comparing its event counts with the greedy eventual cycle shows that the greedy rate is the **largest rate of any feasible periodic schedule**. A shifted copy of any periodic schedule can be compared with an arbitrary greedy initial phase, and phase independence then removes this initialization restriction.

A three-event-per-period schedule exists exactly when all three successive gaps are at least \(s\), or \(s\le a\). A two-event-per-period schedule exists exactly when a pair of phases has both complementary separations at least \(s\). Its largest permissible spacing threshold is
\[\max_{g\in\{a,b,c\}}\min(g,1-g)=\min(c,1-c).\]
A three-event-per-two-period schedule exists exactly when the phases are taken in the reverse cyclic order, whose three successive durations are \(1-g\) for \(g\in\{a,b,c\}\), hence precisely when \(s\le1-c\). A single-phase period-one schedule is always feasible when \(s<1\). Taking the highest available rate and distinguishing \(c<1/2\) from \(c\ge1/2\) gives both displayed piecewise formulas, including all equality cases.

For \(\mathcal T=\mathbb Z\cup(\mathbb Z+1/4)\cup(\mathbb Z+2/3)\), the positive phase-to-phase distances less than one are \(1/4,1/3,5/12,7/12,2/3,3/4\). Direct comparison with \(s\) gives the five cycles listed in the table: first the chronological three-cycle, then the two-cycles on phase sets \(\{0,2/3\}\) and \(\{1/4,2/3\}\), then the reverse three-cycle, then a fixed phase. Their intervals sum to one, one, one, two, and one periods respectively. The variance entries follow by averaging squared deviations of each cyclic list from its mean. These transitions are sharp because the earliest-feasible map changes at the listed boundary spacings.

## Verification
Run `python3 check.py` in the same directory. The standalone checker uses exact rational arithmetic; it compares the general formula to every initial phase for all 171 positive ordered integer gap triples of denominator twenty, across 2,232 threshold/interior cases and three initial phases, yielding 6,696 exact checks; it additionally verifies every phase and endpoint of the five explicit regimes. Computation is a finite cross-check, not a substitute for the all-parameter proof above.

## Relationship to prior work
Kaymakçalan and Selçuk establish the on-time-scale forward-projection recurrence for all closed unbounded time scales and its firing-rate quantization on a uniform lattice; their discussion explicitly leaves periodic-clock arithmetic structure for further study. The present theorem solves that finite-phase question completely for three phase opportunities and identifies a rate-preserving change in the fine spike statistics. Previously established two-phase formulas and more general circle-map rotation principles overlap with the underlying monotone-map method, but do not supply the three-gap sharp staircase or the five-law asymmetric example. Classical periodically *driven* integrate-and-fire models exhibit mode locking; a temporally restricted firing-opportunity clock with constant input is a different model.

## Limitations
The theorem is restricted to three opportunity phases per period and to \(0<s<1\); it does not classify more phases, aperiodic clocks, or event-enriched firing between opportunities. Its phase and interval laws follow a finite transient; no claim of identical transients is made. Standard circle-map and scheduling theory may contain equivalent formulations of some structural steps, and independent historical-priority review remains outstanding.

## References
1. B. Kaymakçalan and B. İ. Selçuk, *Structure-Preserving Leaky Integrate-and-Fire Dynamics on Arbitrary Time Scales*, arXiv:2611.17219v1 (public November 12, 2026), https://arxiv.org/html/2611.17219v1, Theorem 3, Corollary 4, and Section 8.
2. S. Coombes, M. R. Owen and G. D. Smith, *Mode locking in a periodically forced integrate-and-fire-or-burst neuron model*, Phys. Rev. E **64**, 041914 (2001), https://doi.org/10.1103/PhysRevE.64.041914.
3. *Precision and reliability of periodically and quasiperiodically driven integrate-and-fire neurons*, Phys. Rev. E **65**, 041913 (2002), https://doi.org/10.1103/PhysRevE.65.041913.
