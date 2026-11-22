# Twenty-one cells are the sharp first skipped allocation stage for three wildfire compartments

## Finding
On a homogeneous row of \(n\) flammable cells, two impermeable intercell firebreaks form three positive-length compartments. Each cell has an independent chance \(p\in(0,1)\) of igniting, fire spreads through a whole compartment upon any ignition, and a barrier prevents spread between compartments. Write \(q=1-p\). For lengths \((a,b,c)\) with \(a+b+c=n\), let
\[
U_n(a,b,c;q)=a q^a+b q^b+c q^c.
\]
This is the expected count of unburned cells. We optimize over *unordered* length profiles, so the three permutations of \((5,5,11)\) represent one profile, though they correspond to different physical barrier locations.

**Sharp canonical-stage finding.** For each integer \(3\le n\le20\), every profile \((a,a,n-2a)\) with integer \(1\le a\le\lfloor n/3\rfloor\) is the uniquely optimal unordered profile for at least one ignition survival probability \(q\in(0,1)\). In contrast, with \(n=21\), the canonical profile \((6,6,9)\) is *never* optimal for any \(q\in(0,1)\).

**Actual sharp jump.** On the entire explicit range \(q\in[151/200,153/200]\), global optima are exactly
\[
(5,5,11)\quad(q<q_*),\qquad
\{(5,5,11),(7,7,7)\}\quad(q=q_*),\qquad
(7,7,7)\quad(q>q_*),
\]
where
\[
q_* =\sqrt{\frac{\sqrt{561}-11}{22}}=0.7593489605233618228\ldots.
\]
The risk threshold in ignition-probability units is \(p_*=1-q_*\approx0.240651039477\). This is an exact finite-size failure of the tempting assumption that every intermediate two-equal-shorter-segment size must become optimal as ignition risk varies.

## Assumptions and scope
Cells are equally valuable and equally likely to ignite, with mutually independent ignition events. Ignition is a single-period event; the spread inside each compartment is certain, and cross-firebreak spread is impossible. Exactly two zero-width intercell barriers are allowed, no cell is removed by installation, and all three compartments must be nonempty. No empirical spread speeds, time dynamics, spotting or correlated ignitions are asserted. The theorem concerns only the canonical family up to \(n=21\), plus an exact local globally optimal classification at \(n=21\); it does **not** claim a global classification of all profile transitions for arbitrary \(n\).

## Proof
1. A segment of size \(j\) remains wholly unburned precisely if none of its \(j\) cells ignites, an event of probability \(q^j\). Linearity of expectation gives the objective \(U_n\), independently of any possible dependence between survival of different segments (here events are in fact independent).

2. **Sharp lower-order existence.** For each integer \(3\le n\le20\) and each canonical \(a\) allowed above, `witnesses.json` contains an exact rational probability \(q_{n,a}\in(0,1)\). The standalone `checker.py` enumerates **all** nondecreasing positive triples summing to \(n\) and confirms the strict rational inequality
\[
U_n(a,a,n-2a;q_{n,a})>U_n(i,j,k;q_{n,a})
\]
for every distinct unordered profile \((i,j,k)\). Thus each of the 63 canonical profiles has a fully exhaustive exact-arithmetic global-optimality witness. The finite claim needs no inference from a sampled parameter grid: each tabulated witness is checked against the entire finite feasible set.

3. **The skipped profile at \(n=21\).** Let
\[
A(q)=10q^5+11q^{11},\quad B(q)=12q^6+9q^9,\quad C(q)=21q^7.
\]
For all \(q\in(0,1)\), these are the values for \((5,5,11)\), \((6,6,9)\), and \((7,7,7)\). Algebra gives
\[
A-B=q^5(q-1)S(q),\quad S(q)=11q^5+11q^4+2q^3+2q^2+2q-10,
\]
\[
C-B=-3q^6(q-1)T(q),\quad T(q)=3q^2+3q-4.
\]
Both \(S\) and \(T\) are strictly increasing on the positive real line. The *exact rational* tests \(S(759/1000)<0<T(759/1000)\) imply \(A>B\) throughout \(0<q\le759/1000\), and \(C>B\) throughout \(759/1000\le q<1\). In particular, \(B(q)<\max\{A(q),C(q)\}\) everywhere in the open physical parameter interval, proving that \((6,6,9)\) is never globally optimal.

4. **Global local-window classification.** There are exactly 37 nondecreasing positive integer triples summing to 21. For each of the other 35 profiles \(P\) not equal to \(A\) or \(C\), the exact certificates verify \(A(q)>U_{21}(P;q)\) on \([151/200,3797/5000]\), and \(C(q)>U_{21}(P;q)\) on \([3797/5000,153/200]\). Each certificate factors the difference as \(q^m(1-q)R(q)\), expands \(R\) in the Bernstein basis of the specified rational interval, and checks **every Bernstein coefficient is a strictly positive rational number**. The Bernstein basis is pointwise nonnegative and sums to one, so these are valid continuum inequalities, not numerical sampling or a finite approximation. The fully standalone checker reproduces all 70 checks without packages outside the Python standard library.

5. Finally
\[
A-C=q^5(q-1)(q+1)(11q^4+11q^2-10).
\]
The quartic factor increases strictly on \((0,1)\), is negative at zero and positive at one, and has the unique root \(q_*\) specified above. It has \(A>C\) below and \(C>A\) above that root; combined with step 4 this proves the exact stated global local-window phase switch and its unique tie. The rational windows contain \(q_*\), by exact endpoint substitution.

## Verification
Run `python3 checker.py` in a directory containing `witnesses.json`. It uses only Python 3 standard-library integer and rational operations; no floating-point computation participates in the acceptance certificates. The checker verifies every strict rational lower-order witness, both global factor-sign inequalities, all 70 rational Bernstein certificates, and the location of the unique algebraic root. The final printed decimal expansion is illustrative only. The 63 lower-order canonical witnesses and 70 full-interval inequalities correspond to 1,224 counted assertions/comparisons in the checker.

## Relationship to prior work
Wildfire treatment-location optimization and the importance of spatial barriers are established in Belval, Wei and Bevers (2015) and Russo, Russo and Siettos (2015), but their full models address spatial propagation and control-location design, not the exact independent-ignition three-compartment phase structure proved here. The closest published two-firebreak *cycle* classification concerns only **two** resulting compartments and reports an adjacent no-skips staircase. That result has the identical type of per-compartment expected-unburned term but does not imply the present three-compartment skip; in fact, the change in the number of compartments is crucial. The novelty assessment is limited to inspected texts and retrievable source summaries; historical priority remains open to older partition-optimization literature.

## Limitations
This is an analytically exact benchmark for a deliberately simplified independent-ignition model. It does not address landscape geometry beyond a row, correlated ignition, wind, varying fire intensities, multiple time steps, firebreak costs, breaks failing, partial within-compartment burns, or utility weights. The theorem proves first omission from the canonical family through \(n=21\), not the complete optimizer envelope for all larger landscapes. The lower-order existence result uses exact finite enumeration, which is exhaustive for the stated domain but not a statement about all integers.

## References
1. Belval, E. J., Wei, Y., and Bevers, M., *A mixed integer program to model spatial wildfire behavior and suppression placement decisions*, Canadian Journal of Forest Research **45** (2015), 384–393. DOI: https://doi.org/10.1139/cjfr-2014-0252 . Published online 24 November 2014.
2. Russo, L., Russo, P., and Siettos, C. I., *A complex network theory approach for the spatial distribution of fire breaks in heterogeneous forest landscapes for the control of wildland fires*, arXiv:1509.04065 (first posted 14 September 2015), https://arxiv.org/abs/1509.04065 .
3. *Exact staircase of optimal two-firebreak gaps on a uniformly ignited cycle*, published-finding corpus public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-staircase-of-optimal-two-firebreak-gaps-on-a-uniformly-ign--20549d04bba2 (relevant two-compartment comparison; full file unavailable at inspection).
