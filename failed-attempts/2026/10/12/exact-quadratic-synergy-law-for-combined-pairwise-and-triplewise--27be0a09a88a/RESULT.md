# Exact quadratic synergy law for combined pairwise and triplewise contact tracing
## Finding
For the fast-variable threshold equations of de Meijere, Pugliese, Iñiguez, Simon and Kiss, the critical trade-off between pairwise and triplewise tracing is not merely a numerical contour. When treatment compliance is incomplete, the threshold branch is an exact quadratic lying strictly below the chord joining the two pure-intervention thresholds. At full compliance the quadratic correction vanishes and the threshold is exactly that chord.

Let \(n>2\), \(a>0\), \(R_0=\tau(n-2)>1\), and assume
\[
q>q_{\min}^t:=\frac{2(R_0-1)}{R_0n-2}.
\]
This is the stronger of the two minimum-coverage conditions in the source and guarantees that both pure thresholds are finite. Denote the source's Eqs. (3.8) and (3.12) by
\[
C_p=(a+R_0)\frac{R_0-1}{F_p},
\qquad
C_t=(a+R_0)^2\frac{R_0-1}{F_t},
\]
with
\[
F_p=\frac{R_0(nq-1)+(1-q)}{nR_0},
\qquad
F_t=\frac{n-1}{n^2(n-2)}
\left(\frac{R_0(nq-2)+2(1-q)}{R_0}\right)^2.
\]
For \(0<q<1\), put
\[
B=R_0(nq-2)+2(1-q),
\]
\[
L=\frac{R_0n(R_0+a)}{B},
\qquad
Q=\frac{n[ R_0(nq-1)+(1-q)](1-q)}{(n-1)B^2}.
\]
Then the entire nonnegative threshold branch connecting \((C_p,0)\) and \((0,C_t)\) is
\[
c_t=L(C_p-c_p)+Q(C_p-c_p)^2,
\qquad 0\le c_p\le C_p.
\]
Since \(q>q_{\min}^t\) implies \(B>0\), one has \(Q>0\). Moreover
\[
C_t=LC_p+QC_p^2,
\]
so the vertical gap from the chord joining the two pure thresholds is exactly
\[
C_t\left(1-\frac{c_p}{C_p}\right)-c_t
=Q c_p(C_p-c_p).
\]
It is strictly positive for \(0<c_p<C_p\). Thus the mixed intervention is strictly synergistic in the source's fast-variable threshold algebra whenever compliance is incomplete. For \(q=1\), direct elimination gives instead
\[
\frac{c_p}{C_p}+\frac{c_t}{C_t}=1,
\]
so the synergy gap is exactly zero.

## Assumptions and scope
The statement is about positive solutions of the source's threshold algebraic system (Eq. (3.7)), obtained after the source's fast-variable and near-initial-condition reduction. The network degree parameter satisfies \(n>2\), the treated-state exit rate satisfies \(a>0\), and \(R_0>1\). The coverage condition \(q>q_{\min}^t\) ensures both pure critical rates are positive and finite. The claim does not identify the exact threshold of the unreduced ODE system for a finite epidemic seed.

## Proof
At threshold, divide the second equation of the source's Eq. (3.7) by \(x>0\). With
\[
A=\frac{n-1}{n},
\qquad
C=\frac{(n-1)(n-2)}{n^2},
\]
the first three threshold equations imply
\[
c_pAz+c_tCz^2=R_0-1,
\tag{1}
\]
and
\[
y=\frac{\tau x}{R_0}.
\tag{2}
\]
Using the first threshold equation to replace \(\tau x\), then substituting (1) and (2) into the fourth threshold equation and simplifying gives
\[
R_0n(n-1)(R_0+a)z+(n-1)(1-q)c_tz^2
=n[ R_0(nq-1)+(1-q)].
\tag{3}
\]
For \(0<q<1\), set \(w=1/z\), and abbreviate
\[
H=n[ R_0(nq-1)+(1-q)].
\]
Equation (3) becomes
\[
c_t=\frac{H}{(n-1)(1-q)}w^2
-\frac{R_0n(R_0+a)}{1-q}w.
\tag{4}
\]
Combining (1) with (3) yields
\[
c_p=\frac{R_0(R_0+a)(n-2)}{1-q}
-\frac{B}{1-q}w.
\tag{5}
\]
Hence \(w\) is affine in \(c_p\), and substitution of (5) into the quadratic (4) makes \(c_t\) quadratic in \(c_p\). Evaluating the root of (4) corresponding to \(c_t=0\) gives the pure pairwise point \(c_p=C_p\). Expanding around that root gives exactly
\[
c_t=L(C_p-c_p)+Q(C_p-c_p)^2.
\]
Setting \(c_p=0\) recovers the source's pure triplewise threshold \(C_t\), so \(C_t=LC_p+QC_p^2\). The chord-gap identity follows by subtraction.

Conversely, for any \(c_p\in[0,C_p]\), equation (5) defines a positive \(w\) between its pure-pairwise and pure-triplewise endpoint values, hence \(z=1/w>0\). Equation (4) yields \(c_t\ge0\), and then the source's first threshold equation defines \(x>0\) while (2) defines \(y>0\). Therefore the quadratic law parametrizes the whole nonnegative branch between the two pure endpoints.

When \(q=1\), equation (3) loses its quadratic term and gives \(z=1/(R_0+a)\). Equation (1) then reduces directly to
\[
\frac{c_p}{C_p}+\frac{c_t}{C_t}=1.
\]
This proves both cases.

## Verification
For the parameter values used in the source's mixed-intervention figure, \(n=5\), \(\tau=7/10\), \(a=1\), and \(q=3/5\), one has \(R_0=21/10\) and
\[
C_p=\frac{7161}{920}\approx7.78370,
\qquad
C_t=\frac{13985433}{134560}\approx103.93455,
\]
\[
L=\frac{651}{58},
\qquad
Q=\frac{230}{841}.
\]
At the midpoint \(c_p=C_p/2\), the quadratic threshold gives
\[
c_t=\frac{592049997}{12379520}\approx47.82496,
\]
whereas the straight chord gives
\[
\frac{C_t}2\approx51.96727.
\]
The exact gap is
\[
\frac{51279921}{12379520}\approx4.14232>0.
\]
The bundled checker reproduces these rational values and verifies the endpoint and chord-gap identities for this exact rational instance.

## Relationship to prior work
The motivating paper derives closed forms only for pure pairwise and pure triplewise tracing, then studies combined tracing through a numerical final-size map and describes a slight reinforcement relative to the chord joining the pure thresholds. The calculation above eliminates the same threshold system analytically and gives the exact combined curve, including a closed-form synergy gap and the singular simplification at full compliance.

Eames and Keeling developed the classical pairwise contact-tracing threshold framework under fast tracing. Rizi, Keating, Gleeson, O'Sullivan and Kivelä analyzed contact tracing on clustered networks with cliques and derived epidemic thresholds for a different mechanism. Neither inspected comparison contains the pairwise-plus-triplewise fast-variable system or the quadratic mixed-threshold law above.

## Limitations
The fast-variable equations are an approximation justified in the source by early-time correlation saturation and numerical comparison. Therefore the quadratic law is exact for the source's reduced threshold system, not an exact theorem for every trajectory of the unreduced pairwise ODE model. The strict synergy statement also uses \(0<q<1\) and the regime where both pure thresholds are finite. No claim is made about stochastic networks, heterogeneous degree distributions, finite-seed final sizes, or optimal allocation under an external cost function.

## References
1. G. de Meijere, A. Pugliese, G. Iñiguez, P. L. Simon, I. Z. Kiss, “To trace or not to trace: analytical insights from network-based contact-tracing models,” Journal of Mathematical Biology 93, 45 (2026), doi:10.1007/s00285-026-02455-6; first public as arXiv:2603.04059v1 on 2026-03-04.
2. K. T. D. Eames, M. J. Keeling, “Contact tracing and disease control,” Proceedings of the Royal Society B 270 (2003), 2565–2571, doi:10.1098/rspb.2003.2554.
3. A. K. Rizi, L. A. Keating, J. P. Gleeson, D. J. P. O'Sullivan, M. Kivelä, “Effectiveness of contact tracing on networks with cliques,” Physical Review E 109, 024303 (2024), doi:10.1103/PhysRevE.109.024303.
