# A source-driven double reversal in two serial saturating stream reaches

## Finding

A fixed positive concentration addition **between** two saturable removal reaches can make the order minimizing nutrient export reverse twice as upstream concentration increases, even though without an intermediate addition these same two reaches have one strictly preferred order at every positive input. The complete one-parameter phase diagram for the explicit, physically positive two-reach model below has thresholds \(r=2/5\), \(r=12/25\), and \(r=2\): no crossing, exactly two, exactly one, and no crossing, respectively. At the onset of the two-crossing regime a double switching concentration splits with a sharp square-root law, and its upper root escapes to infinity at the next threshold. All claims refer to this exact pair of finite-step response maps, not arbitrary saturating kinetics or an empirical stream network.

## Assumptions and scope

Consider two idealized, strictly increasing, one-pass, finite-step nutrient removal reaches with dimensionless inlet concentration \(x>0\). The removal response maps are
\[
T_1(y)=y-\frac{3y}{5(1+y)},\qquad T_2(y)=y-\frac{4y}{5(2+y)},\qquad y\ge0.
\]
Both satisfy \(T_i(0)=0\), \(0<T_i(y)<y\) and \(T_i'(y)>0\) for \(y>0\). After the first reach and before the second, an external source adds the same fixed concentration increment \(r\ge0\) in either arrangement. (This idealization prescribes constant volume flow; it does not model dilution, varying discharge, or water mixing.) The possible final concentrations are
\[
F_{12}(x;r)=T_2(T_1(x)+r),\qquad F_{21}(x;r)=T_1(T_2(x)+r).
\]
A smaller final concentration is preferable; a zero difference represents a tie. For fixed \(r\), the upstream concentration \(x\) ranges over **all** positive real numbers. No averaging, dynamic feedback, or repeated stage reuse is allowed.

## Proof

**Exact sign reduction.** Clearing the positive denominators gives
\[
F_{12}(x;r)-F_{21}(x;r)=\frac{P_r(x)}{Q_r(x)},
\]
with
\[
\begin{aligned}
P_r(x)={}&(60-125r)x^4+(120-300r-125r^2)x^3\\
 &+(96-130r-425r^2)x^2+(200r-400r^2)x\\
 &+200r-100r^2,
\end{aligned}
\]
and
\[
\begin{aligned}
Q_r(x)={}&5(x+1)(x+2)
(5rx+5r+5x^2+12x+10)\\
&\quad\cdot(5rx+10r+5x^2+11x+10)>0
\end{aligned}
\]
for all \(x>0\), \(r\ge0\). Thus the sign of \(P_r\) completely determines the preferred arrangement: \(P_r>0\) favors reach 2 upstream, while \(P_r<0\) favors reach 1 upstream.

**Below and at the first threshold.** At \(r=0\),
\(P_0(x)=12x^2(5x^2+10x+8)>0\) for \(x>0\). At \(r=2/5\),
\[
P_{2/5}(x)=2(x-2)^2(5x^2+10x+8),
\]
nonnegative with exactly one positive zero, \(x=2\), of multiplicity two. For any fixed \(x\ge0\), \(P_r(x)\) is strictly concave in \(r\), since the \(r^2\) coefficient is \(-125x^3-425x^2-400x-100<0\). Therefore it lies above the chord between \(r=0\) and \(r=2/5\), and \(P_r(x)>0\) for every \(x>0\), \(0\le r<2/5\). Consequently no ordering reversal occurs in that range; exactly at \(2/5\) a single tangential tie occurs without a reversal.

**The exact two-crossing window.** If \(2/5<r<12/25\), the polynomial's descending coefficient signs are \(+,-,-,+,+\). The cubic and quadratic coefficients are strictly negative already at \(r=2/5\) and decrease as \(r\) increases. The linear coefficient is positive since \(r<1/2\), while the leading and constant coefficients are positive. Descartes' rule of signs therefore bounds the number of positive roots, counting multiplicities, by two. Moreover
\[
P_r(0)=100r(2-r)>0,\qquad
P_r(2)=-144(5r-2)(5r+8)<0,
\]
whereas \(P_r(x)\to+\infty\) as \(x\to\infty\). The intermediate value theorem supplies at least one root on each side of 2; both must therefore be distinct, simple and positive, denoted \(x_-(r)<2<x_+(r)\). The signs are positive, negative, positive in the successive intervals. The minimizing order is respectively 2 then 1, 1 then 2, and again 2 then 1.

**The one-crossing window.** For \(12/25\le r<2\), the leading coefficient is nonpositive and the cubic and quadratic coefficients are strictly negative. The linear coefficient is positive up to \(r=1/2\), zero at \(1/2\), and negative thereafter; the constant term is strictly positive. Thus the descending nonzero coefficient signs have exactly one variation. Descartes' rule bounds the number of positive roots by one. Since \(P_r(0)>0\) and \(P_r(x)\to-\infty\), exactly one simple positive root exists, and the minimizing order switches from 2 then 1 to 1 then 2. At the left boundary the degree drops from four to three, but the same sign argument applies.

**Above the final threshold.** If \(r\ge2\), every positive-power coefficient is strictly negative, and the constant term is nonpositive. Hence \(P_r(x)<0\) for every \(x>0\). Reach 1 first is always uniquely best. This proves the complete phase diagram including all boundary cases.

**Sharp birth and escape of the two switches.** Expand about \(x=2\), \(r=2/5\). The quadratic coefficient in the \(x\) direction is 96 because \(P_{2/5}(x)=2(x-2)^2(5x^2+10x+8)\); the first \(r\) derivative there is \(-7200\). Standard local Taylor factorization and the simple sign-separated roots yield
\[
x_\pm(r)=2\pm5\sqrt3\sqrt{r-2/5}+O(r-2/5)
\quad(r\downarrow2/5).
\]
For \(r\uparrow12/25\), the upper root diverges: the leading coefficient is \(125(12/25-r)\) while the cubic coefficient tends to \(-264/5\). Dividing the root equation by \(x^3\) and using that the positive finite root persists yields
\[
x_+(r)\sim\frac{264}{625(12/25-r)}.
\]
The lower root tends to the unique positive root of the limiting cubic \(P_{12/25}\). In particular, the discontinuity in the number of finite positive switches at \(12/25\) is a root escaping to infinity, not a finite double-root annihilation.

## Verification

Run `python verification/check_interstage.py` with Python 3 and SymPy. It checks the exact numerator/denominator identity, the double-zero and tangent identities, the critical asymptotic coefficients, and 63 strictly rational input/source pairs (two independent checks each). In total it reports 139 passed symbolic/rational/numerical assertions, including the exact polynomial at \(r=43/100\), whose only two positive zeros are approximately \(1.10383290344146\) and \(6.05382660573888\). It checks positive, negative, positive signs at \(x=1,2,10\), respectively. The checker is finite corroboration; the all-real \(x,r\) proof is the coefficient-sign and concavity argument above.

## Relationship to prior work

Covino, McGlynn and Baker (2010) document Michaelis–Menten uptake kinetics that differ across successive stream reaches and demonstrate the importance of stream–groundwater gains and losses for downstream nutrient export. Their observed system is more complicated than this finite-step model and their full article supplies neither the rational permutation polynomial nor the exact injection-driven double-switch phase diagram. Dalwadi, Griffiths and Bruna (2015) optimize filtration properties using a homogenized transport/adsorption PDE and porosity gradients, a distinct object. Previously published analysis of *two-index ordering of serial saturating nutrient-removal reaches* treats this exact family of one-step maps **without intermediate nutrient addition** and establishes a single-switch upper bound in that different model. Its own assumptions exclude the source term \(r\), and inserting an intermediate source is not a substitution into its original commutator: it changes the algebraic degree and produces the twice-reversing order established here. We do not claim novelty for Michaelis–Menten saturation, adjacent interchanges, or the source-free model. Priority relative to general rational-composition theory and inaccessible process-engineering literature remains provisional.

## Limitations

This is a parameterized counterexample and complete classification for **one explicit pair** of reach responses; it does not classify arbitrary pairs or arbitrary sequences. The additive source is modeled as an equal fixed concentration increment independent of ordering, so the theorem does not directly cover physical groundwater dilution, conservation of discharge, variable contact time, continuous plug-flow kinetics, transport dispersion, multiple solutes, or costs of swapping fixed reaches. The result has no empirical claim that actual streams exhibit the quantified reversals. Numerical roots are illustrative; they are not used to certify the continuous inequalities. Historical literature coverage is bounded by accessible material and could miss a more general pre-existing theorem.

## References

1. T. Covino, B. McGlynn and M. Baker, “Separating physical and biological nutrient retention and quantifying uptake kinetics from ambient to saturation in successive mountain stream reaches,” *Journal of Geophysical Research: Biogeosciences* 115 (2010), G04010, doi:10.1029/2009JG001263; first published 2010-10-08. Full article: https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2009JG001263.
2. M. P. Dalwadi, I. M. Griffiths and M. Bruna, “Understanding how porosity gradients can make a better filter using homogenization theory,” arXiv:1507.01722, first submitted 2015-07-07. https://arxiv.org/abs/1507.01722.
3. “A two-index ordering law for serial saturating nutrient-removal reaches,” publicly available mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-two-index-ordering-law-for-serial-saturating-nutrient-removal--15d05df5ff61; used to delimit the previously established **no-intermediate-source** ordering theorem.
