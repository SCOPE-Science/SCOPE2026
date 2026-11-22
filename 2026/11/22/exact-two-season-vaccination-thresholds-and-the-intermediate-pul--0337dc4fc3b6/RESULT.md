# Exact two-season vaccination thresholds and the intermediate pulse-mass law

## Finding
Consider the periodic susceptible-renewal equation with a fixed vaccination budget and two constant transmission seasons, defined precisely below. For every strictly positive set of model parameters, there is an **exact maximal budget for which a single pulse at the low-to-high-season transition is globally optimal among all positive periodic vaccination measures**:

\[
M_0=\log\min\left\{\frac{H}{x},\frac{x}{L}\right\},\qquad
x=H\frac{1-ca_0}{1-ba_0},\quad
a_0=e^{-\delta h},\quad b=e^{-\delta(T-h)},\quad
c=1-\frac{L}{H}(1-b).
\]

The single-pulse schedule is the unique global optimizer when \(0<M\le M_0\), and no single-pulse schedule is globally optimal for \(M>M_0\). In particular, this is a **finite-budget** result, not merely a limit as vaccine supply tends to zero.

When \(x>\sqrt{HL}\), the *entire next budget regime* can also be found without numerical optimization. Put

\[
q=\sqrt{H/L},\qquad
a_* = \frac{q-1}{qc-b},\qquad
y_* = h+\delta^{-1}\log a_*,
\]
\[
a(y)=e^{-\delta(h-y)},\quad
p(y)=\log\frac{1-ba(y)}{1-ca(y)},\quad
\eta(y)=\frac{\delta a(y)(c-b)}{[1-ca(y)][1-ba(y)]},\quad
M(y)=p(y)+y\eta(y),
\]
\[
M_1=M(y_*).
\]

Here \(0<y_*<h\), and \(M(y)\) is strictly increasing on \([0,y_*]\), from \(M_0\) to \(M_1\). Thus each \(M\) with \(M_0<M\le M_1\) determines a unique \(y\), and the **unique global optimal schedule** is

\[
dm^{\mathrm{opt}}=p(y)\,d\delta_0+\eta(y)\mathbf 1_{(0,y)}(t)\,dt
\quad\text{per period.}
\]

This gives an exact analytic parametric expression for the intermediate optimal pulse mass \(p\), even though vaccination has already begun continuously during the high-transmission season. At the endpoint \(M_1\), the pulse mass is exactly \(\tfrac12\log(H/L)\). No classification is claimed for budgets exceeding \(M_1\), nor for the intermediate allocation beyond the single-pulse regime when \(x\le\sqrt{HL}\).

## Assumptions and scope
Fix \(T>h>0\), transmission rates \(H>L>0\), susceptible replenishment rate \(\delta>0\), and total vaccination hazard \(M\ge0\) per period. Transmission is \(T\)-periodic and equals \(H\) during \(0<t<h\) and \(L\) during \(h<t<T\); a rise from \(L\) to \(H\) occurs at \(t=0\) modulo \(T\). Minimize

\[
J[m]=\int_0^T\beta(t)S_m(t)\,dt
\]

among all locally finite, nonnegative, \(T\)-periodic Borel measures \(m\) with \(m([0,T))=M\). The periodic susceptible trajectory is governed between atoms by \(S'=\delta(1-S)-S\,dm/dt\), and across an atom of mass \(p\) by \(S(t+)=e^{-p}S(t-)\). A unique periodic trajectory exists and is strictly positive. This is the disease-free susceptibility equation in the seasonal SIRVS vaccination model of Gavish and Katriel (2026). Multiplying \(J\) by the fixed positive factor \(1/[T(\gamma+\mu)]\) gives that paper's disease-invasion reproduction number; hence the minimizers agree. The budget counts administered *hazard*, not automatically the number of distinct people immunized.

## Proof
**1. Convexity and a sufficient first-order condition.** Let \(E=e^{-\delta T}\). Extend \(m\) and \(\beta\) periodically to the real line. For any fixed budget \(M\), the stationary renewal representation is

\[
S_m(t)=\frac{\delta}{1-Ee^{-M}}\int_0^T
 e^{-\delta s-m((t-s,t])}\,ds,
\]

with endpoints immaterial under integration. Consequently, \(J[m]\) is convex in \(m\): its integrand is an exponential of an affine functional of \(m\), multiplied by positive factors. It is strictly convex on the fixed-budget feasible set: equality in the convexity inequality forces the masses assigned by two competing measures to almost every circular time interval to coincide, which forces the measures themselves to coincide.

Define the positive future-weight function \(P\) as the unique periodic backward adjoint for the controlled equation. On every atom-free interval, \(P'=(\delta+\eta)P-\beta\); at a pulse of mass \(p\), \(P(t-)=e^{-p}P(t+)\). The first variation in the direction of redistributing one unit of vaccination measure from an existing support point to a new time \(t\) equals \(Q(\text{support})-Q(t)\), where

\[
Q(t)=S(t)P(t),
\]

using right limits at a pulse. This follows by differentiating the renewal integral, or by differentiating the state equation and integrating the adjoint identity. The product \(Q\) is continuous across impulses; between impulses and at their smooth limits,

\[
Q'=\delta P-\beta S.
\]

Therefore **a feasible measure is globally optimal** if \(Q\) equals a common maximum on its support and is nowhere larger off its support. Necessity follows from transfer variations and sufficiency from convexity. Strict convexity gives uniqueness.

**2. Exact single-pulse threshold.** Take \(m=M\delta_0\), and put \(z=e^{-M}\), \(E=e^{-\delta T}\). Immediately after and before the pulse,

\[
S(0+)=\frac{z(1-E)}{1-zE},\qquad
S(T-)=\frac{1-E}{1-zE}.
\]

Let

\[
B=\frac{H(1-e^{-\delta h})+L(e^{-\delta h}-E)}{\delta}
=\frac{x(1-E)}{\delta}.
\]

The backward adjoint has \(P(0+)=B/(1-zE)\) and \(P(T-)=zP(0+)\). Thus the two one-sided derivatives at the pulse satisfy

\[
Q'(0+)=\frac{(1-E)(x-Hz)}{1-zE},\qquad
Q'(T-)=\frac{(1-E)(xz-L)}{1-zE}.
\]

For the pulse to maximize \(Q\), it is necessary that \(Q'(0+)\le0\) and \(Q'(T-)\ge0\), i.e.

\[
z\ge\max\{x/H,L/x\}.
\]

It is also sufficient. To see this, on any atom-free constant-transmission interval with \(S=1-Ae^{-\delta t}\) and \(A>0\), write \(P=\beta/\delta+Ce^{\delta t}\). Then

\[
Q'=\delta Ce^{\delta t}+A\beta e^{-\delta t}.
\]

If this derivative is nonpositive at the left endpoint, it stays negative to its right. If it is nonnegative at the right endpoint, it was positive throughout the interval to its left. Hence the above inequalities make \(Q\) decrease throughout the high season and increase throughout the low season, reaching its only maximum at the pulse. Conversely, violating either inequality gives a strictly beneficial infinitesimal redistribution of pulse mass. Converting \(z\) to \(M\) yields the displayed sharp threshold.

A pulse placed at another phase cannot do better. For any fixed \(M>0\), the reduction in \(J\) due to a single pulse at \(\tau\) is a positive constant times \(B(\tau)=\int_0^T\beta(\tau+s)e^{-\delta s}\,ds\). Between seasonal jumps,

\[
B'(\tau)=\delta B(\tau)-(1-E)\beta(\tau).
\]

Because \(L(1-E)/\delta < B(\tau)<H(1-E)/\delta\), this derivative is strictly negative in the high season and strictly positive in the low season. Thus \(B\) has its unique maximum at the low-to-high transition. This excludes every other single-pulse schedule when \(M>M_0\).

**3. Exact intermediate phase.** Suppose \(x>\sqrt{HL}\). From \(b<c<1\), the function \(p(y)\) above increases strictly from \(\log(H/x)=M_0\) at \(y=0\) to \(\log(H/L)\) at \(y=h\). There is exactly one \(y_*\in(0,h)\) at which \(p(y_*)=\tfrac12\log(H/L)\), and solving this identity yields the displayed explicit \(a_*\). Differentiation gives

\[
p'(y)=\eta(y)>0,\qquad\eta'(y)>0,\qquad
M'(y)=2\eta(y)+y\eta'(y)>0.
\]

For a given \(y\in[0,y_*]\), consider a pulse of mass \(p(y)\) at the season's start, constant vaccination rate \(\eta(y)\) during \((0,y)\), and zero vaccination afterwards. Put \(k=\delta+\eta(y)\). Direct substitution in the susceptible equation gives \(S(t)=\delta/k\) throughout \((0,y)\). The uncontrolled recovery from \(y\) to \(T\), followed by the pulse, closes the periodic orbit exactly because

\[
e^{p(y)}=\frac{1-ba(y)}{1-ca(y)},\qquad
\frac{\delta}{k}=\frac{1-ba(y)}{e^{p(y)}-ba(y)}.
\]

The backward adjoint is similarly constant \(P(t)=H/k\) on \((0,y)\). Indeed, putting \(a=a(y)\), the remaining discounted transmission integral is \(W(y)=H[1-ca]/\delta\), and the adjoint condition

\[
\frac{H}{k}\bigl(1-ba e^{-p(y)}\bigr)=W(y)
\]

is exactly the defining identity for \(p(y)\) and \(k\). Hence \(Q=\delta H/k^2\) is constant on the pulse and the continuously treated interval.

On the untreated remainder of the high season, \(Q'(y+)=0\) and \(Q''(y+)=2\delta H(\delta/k-1)<0\), so the constant-transmission formula above makes \(Q\) strictly decrease until the end of the high season. On the low season, periodicity gives

\[
Q'(T-)=\frac{\delta}{k}\left(He^{-p(y)}-Le^{p(y)}\right)\ge0
\]

because \(p(y)\le\tfrac12\log(H/L)\). The same constant-transmission derivative formula makes \(Q\) increase toward the period boundary throughout the low season. Thus it never exceeds its value on the vaccination support. The sufficient optimality condition from step 1 applies, and strict convexity establishes the claimed unique mixed optimizer.

## Verification
The source's square-wave example has \(H=7/4\), \(L=1/4\), \(h=1/2\), \(T=1\), \(\delta=1\). The formulas give

\[
M_0=0.3909799575971128\ldots,\qquad
M_1=2.232928304349943\ldots,
\]

and the mixed-regime endpoint has \(y_*=0.361353956663426\ldots\). The source reports approximate numerical changes around \(0.4\) and \(2.25\) but no analytic description of the intermediate pulse mass. Here \(p(M)\) is specified uniquely and exactly by the increasing parametric function \(M(y)\).

A second example permits rational checks: choose \(H=4\), \(L=1\), \(h=1\), \(T=2\), \(\delta=\log 2\). Then \(a_0=b=1/2\), \(c=7/8\), \(x=3\), \(a_*=4/5\), and

\[
M_0=\log(4/3),\qquad
M_1=\log2+\frac53\log(8/5).
\]

At the second transition \(\eta(y_*)/\delta=5/3\). The standalone file `check.py` uses exact rational arithmetic for the latter identities and numerical evaluation of the derived first-variation inequalities, including the source-example thresholds and parameterized active intervals. It is supporting evidence only; the all-parameter conclusions follow from the displayed analytic proof, not from numerical sampling.

## Relationship to prior work
Gavish and Katriel (2026, *Bulletin of Mathematical Biology*, Theorem 10 and Fig. 9) establish a broad structure theorem for optimal vaccination measures and present the same square-wave forcing. They numerically observe the transition from a single pulse to pulse-plus-continuous vaccination, but explicitly leave the intermediate pulse-mass formula and additional pulse conditions unresolved. The present result supplies a sharp finite-budget boundary for the complete single-pulse regime, and an exact analytic description of the first mixed phase for a broad, explicitly stated parameter class. It does **not** claim convexity of the optimization functional, existence and uniqueness in general, or the qualitative presence of pulses as new: these were previously established.

The foundational convex measure-optimization theorem of Gavish and Katriel (2026, *Applied Mathematics & Optimization*) supplies the general variational methodology but does not contain these evaluated two-season thresholds. Doutor and coauthors (2016) optimize a stronger pointwise monotone-infection criterion, rather than the average invasion criterion used here. Onyango and Müller (2014) study a susceptible-only vaccination formulation with a different administered-dose constraint; accessible source material does not establish these exact hazard-budget phases. As with all literature-led mathematical results, equivalence to an unindexed or unavailable prior derivation remains possible.

## Limitations
The claim concerns deterministic disease-free linear invasion potential and idealized instantaneous vaccination hazard; it is not a statement about actual infection counts, clinical implementation, vaccine uptake, or finite-population dynamics. The total vaccination hazard \(M\) is not a count of unique vaccinated individuals. A pulse is a measure, not a bounded-rate intervention. The formula for the mixed phase requires \(x>\sqrt{HL}\) and is asserted only through \(M_1\); the next regime and the other parameter ordering are not classified here. Independent mathematical audit has not been performed.

## References
1. N. Gavish and G. Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Bulletin of Mathematical Biology **88**, article 170 (published September 2, 2026), DOI: https://doi.org/10.1007/s11538-026-01741-0 ; open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC13538159/ .
2. N. Gavish and G. Katriel, *Optimal Regulation in a Time-Periodic Environment: Insights from a Simple Model*, Applied Mathematics & Optimization **93**, article 22 (published January 10, 2026), DOI: https://doi.org/10.1007/s00245-025-10374-z ; open full text: https://link.springer.com/article/10.1007/s00245-025-10374-z .
3. P. Doutor, P. Rodrigues, M. do Céu Soares, and F. A. C. C. Chalub, *Optimal Vaccination Strategies and Rational Behaviour in Seasonal Epidemics*, Journal of Mathematical Biology **73** (2016), 1437–1465; preprint: https://arxiv.org/abs/1507.02940 .
4. N. O. Onyango and J. Müller, *Determination of optimal vaccination strategies using an orbital stability threshold from periodically driven systems*, Journal of Mathematical Biology **68** (2014), 763–784, DOI: https://doi.org/10.1007/s00285-013-0648-8 .
