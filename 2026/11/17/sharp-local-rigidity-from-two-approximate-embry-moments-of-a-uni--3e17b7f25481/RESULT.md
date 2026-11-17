# Sharp local rigidity from two approximate Embry moments of a unilateral weighted shift

## Finding
For any integer \(n\ge3\), positive bounded unilateral Hilbert-space weighted shift \(W e_j=w_j e_{j+1}\), and errors \(\alpha,\beta\ge0\), the two Loewner inequalities
\[
W^{*2}W^2\succeq e^{-\alpha}(W^*W)^2,\qquad
W^{*n}W^n\preceq e^{\beta}(W^*W)^n
\]
force the **sharp two-sided logarithmic adjacent-weight estimate**
\[
\boxed{-\alpha\le\log\frac{w_{j+1}^2}{w_j^2}
\le \frac{\beta}{n-1}+\frac{n-2}{2}\alpha}\qquad(j\ge0).
\]
Both constants are attained by positive bounded shifts with eventually constant weights. At the upper endpoint, the exact equality mechanism is a single upward spike followed by \(n-2\) maximally allowed downward increments. Small errors do not force global operator-norm proximity to a constant-weight shift: even for \(\alpha=\beta\downarrow0\), examples of norm one have minimum distance \(1/4\) to the family of scalar multiples of the ordinary unilateral shift.

## Assumptions and scope
Work on complex \(\ell^2(\mathbb N_0)\) with its standard orthonormal basis \((e_j)_{j\ge0}\). The weights \((w_j)\) are real and strictly positive, bounded above, but need not have a uniform positive lower bound. All operator inequalities are in the positive-semidefinite (Loewner) sense. Fix \(n\ge3\), \(\alpha,\beta\in[0,\infty)\). Define \(a_j=w_j^2\) and \(d_j=\log(a_{j+1}/a_j)\). The conclusion is a bound on **each** finite adjacent ratio, not a bound on the total variation of the weight sequence. The scalar shift family is \(cS\), where \(S e_j=e_{j+1}\), \(c\in\mathbb C\).

## Proof
**1. Diagonal moments and exact weighted-sum constraints.** By direct iteration, for all integers \(k\ge1\) and indices \(j\ge0\),
\[
W^{*k}W^k e_j=\left(\prod_{r=0}^{k-1}a_{j+r}\right)e_j,\qquad
(W^*W)^ke_j=a_j^ke_j.
\]
Because every \(a_j>0\), taking logarithms is legitimate. The lower second-moment inequality is exactly \(d_j\ge-\alpha\) for every \(j\). The upper \(n\)-moment inequality is equivalent to
\[
L_n(j):=\sum_{r=1}^{n-1}\log\frac{a_{j+r}}{a_j}
=\sum_{h=0}^{n-2}(n-1-h)d_{j+h}\le\beta\quad(j\ge0).
\]
These equivalences use the common diagonal basis and remain valid with no lower bound on \(\inf_jw_j\).

**2. Sharp local estimate and equality.** Put \(S_n=n(n-1)/2\). Using \(d_{j+h}\ge-\alpha\) for \(h=1,\dots,n-2\),
\[
(n-1)d_j=L_n(j)-\sum_{h=1}^{n-2}(n-1-h)d_{j+h}
\le\beta+\alpha\frac{(n-1)(n-2)}2.
\]
Division gives the displayed bound; the lower endpoint is the original second-moment inequality. Every coefficient of each future increment is strictly positive, so **upper equality** holds iff \(L_n(j)=\beta\) and \(d_{j+h}=-\alpha\) for all \(1\le h\le n-2\).

**3. Global feasibility of both extremal pulses.** Set
\[
K=\frac\beta{n-1}+\frac{n-2}{2}\alpha,\qquad j_*=n+2.
\]
Define a sequence of increments \(d_t\) by setting \(d_{j_*}=K\), setting \(d_t=-\alpha\) for each of the \(n-1\) positions immediately preceding \(j_*\) and the \(n-2\) positions immediately following it, and putting \(d_t=0\) at all other indices. Every increment is at least \(-\alpha\). For a window starting at \(j_*-h\), \(0\le h\le n-2\), that contains the positive pulse, every other increment in the window is \(-\alpha\); hence
\[
L_n(j_*-h)=(n-1-h)(K+\alpha)-\alpha S_n
=\frac{n-1-h}{n-1}(\beta+\alpha S_n)-\alpha S_n\le\beta.
\]
Every window not containing that pulse has \(L_n\le0\le\beta\). Thus this entire infinite increment sequence obeys both constraints, and at \(j_*\) attains the upper constant exactly. Integrating by \(a_0=1\) and \(a_{t+1}=a_te^{d_t}\) yields strictly positive finite-valued \(a_t\) that become constant after finitely many changes; the associated weighted shift is bounded. For the lower endpoint, take just one increment \(d_{j_*}=-\alpha\), with all others zero. It satisfies \(L_n\le0\) and realizes \(d_{j_*}=-\alpha\). Consequently neither endpoint can be improved under the stated assumptions.

**4. Uniform global approximation is impossible.** Fix \(\varepsilon>0\), and choose a positive integer \(N\) so large that \(N\ge S_n\log(4)/\varepsilon\). Define
\[
a_j=\tfrac14\exp\left(\frac{\log4}{N}\min(j,N)\right),\qquad w_j=\sqrt{a_j}.
\]
Then \(1/2\le w_j\le1\), \(\|W\|=1\), and every \(d_j\) is either \(0\) or \(\log4/N\), so the lower moment inequality holds with \(\alpha=\varepsilon\), while \(L_n(j)\le S_n\log4/N\le\varepsilon\) yields the upper inequality with \(\beta=\varepsilon\). Nevertheless \(w_0=1/2\) and \(w_N=1\), and for all complex \(c\),
\[
\|W-cS\|=\sup_j|w_j-c|\ge\frac12|w_N-w_0|=\frac14.
\]
Taking \(c=3/4\) makes both endpoint differences equal to \(1/4\), and every intermediate weight lies between them, so \(\inf_c\|W-cS\|=1/4\), exactly. This construction works for arbitrarily small positive \(\varepsilon\).

The zero-error case follows directly: \(d_j=0\) for all \(j\), hence every weight is equal, recovering quasinormality for this weighted-shift class.

## Verification
A standalone standard-library Python checker, `moment_weight_checker.py`, uses exact rational arithmetic for the finite logarithmic-increment inequalities. Executing `python moment_weight_checker.py` gives:

`PASS: exact upper-constant pulses 576 ; independent admissible sequences 15000 ; negative-step witnesses 27 ; global contrast probes 12`

The upper extremal construction was checked for all \(3\le n\le50\) over 12 rational error pairs, with every translated \(n\)-moment inequality tested throughout each finite pulse support. Further diagnostics cover 15,000 feasible sequences, 27 lower-endpoint witnesses, and the slowly varying obstruction for three positive error sizes and four exponents. These finite tests confirm formulas and catch index mistakes; they do not substitute for the infinite-dimensional proof in the preceding section.

## Relationship to prior work
Pietrzycki's *Reduced Embry characterizations of quasinormal operators* establishes the exact, zero-error order characterization for **all** bounded Hilbert-space operators from two opposite-sided power inequalities. That result is stronger in operator scope but does not supply this quantitative inequality for perturbed moments, its sharp constants, upper-endpoint equality pattern, or global non-approximation example. The present statement deliberately restricts to strictly positive unilateral weighted shifts; it is neither a quantitative theorem for arbitrary operators nor an improvement of the general exact characterization. Earlier work on single moment identities and on moment-infinite-divisible shifts has different premises and goals. Relevant published weighted-shift estimates on Cesàro growth, finite nilpotent moment defects, and Aluthge dynamics do not furnish this two-error local envelope. The literature comparison is by conclusions and implications, not by similarity of titles.

## Limitations
No conclusion is asserted for weights that vanish; logarithms and the moment-ratio normalization would then require a different formulation. Constants depend on \(n\); there is no uniform bound as \(n\to\infty\) with \(\alpha\) fixed. No global distance-to-quasinormal estimate follows without extra restrictions such as a finite horizon, bounded total logarithmic variation or a fixed lower support. A possible older equivalent estimate in the discrete positive-sequence literature remains a residual originality risk. Independent mathematical validation has not been performed.

## References
1. P. Pietrzycki, *Reduced Embry characterizations of quasinormal operators*, arXiv:2610.17303, first posted 12 October 2026, https://arxiv.org/abs/2610.17303.
2. P. Pietrzycki, *The single equality \(A^{*n}A^n=(A^*A)^n\) does not imply quasinormality of weighted shifts on rootless directed trees*, arXiv:1502.06396, https://arxiv.org/abs/1502.06396.
3. R. E. Curto, C. Benhida and G. R. Exner, *Moment infinitely divisible weighted shifts*, Complex Analysis and Operator Theory 13 (2019), 241–255, https://doi.org/10.1007/s11785-018-0771-z.
