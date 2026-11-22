# Three exact storm-order reversals across two heterogeneous retention roofs

## Finding
Consider a rainfall sequence consisting of two instantaneous depths, \(A=1/2\) and \(B=1/4\), with \(A>B\). Two independent parallel retention roofs are subject to the same two depths but have different capacities and between-storm water-retention fractions. At the start, each roof has the *same fraction* \(s\in[0,1]\) of its own capacity filled. A prescribed initial drying interval occurs before the first event, and an equal-retention drying interval occurs between the two events. The roofs have capacities \((C_1,C_2)=(1/2,2)\), fractions retained per interval \((q_1,q_2)=(1/5,9/10)\), and catchment-area weights \((w_1,w_2)=(1,10)\).

Let \(W_{AB}(s)\) be the area-weighted sum of total overflow under the larger-then-smaller sequence, and \(W_{BA}(s)\) the sum under the reverse sequence. Then the difference \(D(s)=W_{AB}(s)-W_{BA}(s)\) has **exactly three distinct zeros** in \([0,1]\):

\[
\boxed{s_1=\frac58,\qquad s_2=\frac{635}{806},\qquad s_3=\frac{45}{47}.}
\]

These are strict sign changes, with \(D(s)<0\), \(D(s)>0\), \(D(s)<0\), \(D(s)>0\) successively on the four open regions separated by the zeros. Negative difference favors the larger-first storm order for minimizing combined overflow; positive difference favors smaller-first. In contrast, **a single retention roof of the same capped linear-loss type cannot have more than one strict sign reversal** as a function of its starting fractional saturation. Hence two independent roof types are the minimum needed to exhibit three such reversals.

## Assumptions and scope
All depths and capacities are expressed in consistent per-unit-area water-depth units. For one roof with capacity \(C>0\), dry-interval retention \(0<q<1\), and initial fractional fill \(s\in[0,1]\), the pre-first-event storage is \(qCs\). A rainfall depth \(x\) causes instantaneous saturation-excess overflow \((qCs+x-C)_+\), leaving storage \(\min(C,qCs+x)\). Before the second event storage is again multiplied by \(q\). Thus the two-event overflow for ordered depths \(x,y\) is

\[
R_{xy}(s;C,q)=(qCs+x-C)_+ + \big(q\min(C,qCs+x)+y-C\big)_+,
\qquad u_+=\max(u,0).
\]

Parallel roofs do not exchange water. Their overflows are summed with fixed nonnegative area weights. We compare *equal total rainfall* in opposite orders, holding all physical parameters and the initial fractional saturation fixed. No implication is asserted for continuous rainfall, preferential drainage, finite infiltration rates, stochastic storm times, or a calibrated roof.

## Proof
**Single-roof sign bound.** For general \(x>y>0\), write \(z=qCs\) and \(d(s)=R_{xy}-R_{yx}\). Partition into the exhaustive cases \(z+y\ge C\), \(z+x\le C\), and \(z+y<C<z+x\), allowing equality to be assigned to either adjoining case where values match.

If \(z+y\ge C\), then \(qC+y\ge C\) because \(z\le qC\); both orders fill the reservoir on both events and \(d(s)=0\). If \(z+x\le C\), first-event overflow vanishes in both orders and

\[
d(s)=\big(q(z+x)+y-C\big)_+-\big(q(z+y)+x-C\big)_+\le0,
\]

because the second positive-part argument exceeds the first by \((1-q)(x-y)>0\). In the remaining case \(z+y<C<z+x\), the larger-first initial pulse overflows and the smaller-first initial pulse does not. Direct substitution yields

\[
d(s)=
\begin{cases}
-(1-q)(C-z-y),&qC+y\ge C,\\
\min\{z+x-C,(1-q)z-qy\},&qC+y<C.
\end{cases}
\]

In the first line this is negative. In the second, the first argument is positive and the second crosses zero only at \(s=y/((1-q)C)\). The region \(z+x\le C\) cannot have positive difference, and in the remaining region any passage between negative and positive values goes only from negative to positive. This proves that **one roof cannot have two or more strict sign reversals** in \(s\in[0,1]\).

**Two-roof exact calculation.** Substituting the stated rational parameters into the general overflow definition gives

\[
d_1(s)=R_{AB}(s;C_1,q_1)-R_{BA}(s;C_1,q_1)=\frac{2s}{25}-\frac1{20}.
\]

For the second roof the only interior changes in which overflow branches are active occur at \(85/108,65/81,5/6,35/36\), in that order. Direct substitution gives the complete formula

\[
d_2(s)=\begin{cases}
0,&0\le s\le85/108,\\
51/40-81s/50,&85/108\le s\le65/81,\\
-1/40,&65/81\le s\le5/6,\\
9s/50-7/40,&5/6\le s\le35/36,\\
0,&35/36\le s\le1.
\end{cases}
\]

Consequently \(D(s)=d_1(s)+10d_2(s)\). On the five consecutive subintervals displayed above, this is respectively

\[
\frac{2s}{25}-\frac1{20},\quad
\frac{127}{10}-\frac{403s}{25},\quad
\frac{2s}{25}-\frac3{10},\quad
\frac{47s}{25}-\frac95,\quad
\frac{2s}{25}-\frac1{20}.
\]

The zeros of these affine expressions are respectively \(5/8\), \(635/806\), \(15/4\), \(45/47\), and \(5/8\). Only the first, second and fourth lie in their corresponding subintervals. All endpoint values match, and none of the four interior branch points is a zero. The three zeros therefore are exhaustive and simple sign changes. Since one roof has at most one strict reversal but this two-roof construction has three, two is the sharp minimum number of roof types for a three-reversal phenomenon.

## Verification
The standalone `verify.py` uses exact Python rational arithmetic. It independently evaluates the capped two-pulse recurrence for both roofs, checks both piecewise formulas at all breakpoints and 2,001 rational grid states, verifies the three exact zeros, and checks alternating signs at \(s=0,3/4,7/8,1\). The corresponding exact differences are \(-1/20,1/100,-31/200,3/100\). Run `python verify.py` with Python 3; no external packages are required. This finite testing supports, but is not a substitute for, the exhaustive piecewise proof.

## Relationship to prior work
Paus and Braskerud (2024) document the importance of antecedent water conditions for extreme green-roof runoff. Raimondi and Becciu (2020) analyze chains of rainfall events and partially filled roofs through an analytical probabilistic model. Ashitey and coauthors (2023) compare rainfall retention across roof media configurations. These supply the hydrological motivation and do not establish the exact two-roof, three-reversal construction. A published mathematical note on a *single periodic* store with three repeating rainfall depths concerns a stationary three-event ordering, not two independent roofs initialized to equal saturation fractions. The elementary capped-storage recurrence and the single-store ordering behavior are not claimed as novel: the contribution here is the exact multiple-switch counterexample under aggregation and the sharp minimum in the number of parallel roof types.

## Limitations
The signs compare the runoff from two hypothetical ordered storms, not a controllable storm-order intervention or a measured field forecast. The starting fraction \(s\) is matched across roofs, whereas their actual starting moisture fractions may differ. Drying is multiplicative and uniform for each roof; the two intervals were chosen to have the same fractional retention within each roof. The area ratio of \(10:1\), roof capacities and pulse depths are constructed rather than calibrated. No universal upper bound of three switches for arbitrary two-roof parameters is claimed. The result does not address peak discharge, which depends on within-event timing.

## References
1. Paus, K. H., and Braskerud, B. C. (2024). *Runoff from an extensive green roof during extreme events: Insights from 15 years of observations*. Hydrological Processes 38(6), e15220. First online June 27, 2024. https://doi.org/10.1002/hyp.15220
2. Raimondi, A., and Becciu, G. (2020). *Performance of Green Roofs for Rainwater Control*. Water Resources Management 35, 99–111. First online November 16, 2020. https://doi.org/10.1007/s11269-020-02712-3
3. Ashitey, P., Benjankar, R., Morgan, S., Retzlaff, W., and Celik, S. (2023). *Analyses of the Effectiveness of Different Media Depths and Plant Treatments on Green Roof Rainfall Retention Capability under Various Rainfall Patterns*. Hydrology 10(7), 149. https://doi.org/10.3390/hydrology10070149
4. *A sharp storm-ordering window for saturation runoff in a periodic linear store* (2026), public mathematical result: https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-sharp-storm-ordering-window-for-saturation-runoff-in-a-periodi--d7dd28e86fa3
