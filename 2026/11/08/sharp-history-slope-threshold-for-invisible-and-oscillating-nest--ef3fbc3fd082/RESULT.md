# Sharp history-slope threshold for invisible and oscillating nested delays

## Finding

A clipped initial history gives an **exact and sharp transition** at \(q=\eta M=1\) for the switched-feedback delay equation with mean delay one. Below the transition, all nested state-dependent delay equations have the same global trajectory as the constant-delay reference, by the previously published invisibility theorem. At equality the nesting operator has a genuine alternating two-cycle, and **every even nesting order has a different trajectory immediately**, despite the fact that the implicit delay remains uniquely defined and gives the unchanged reference trajectory locally. Above equality, even the second nested delay reverses the initial feedback sign.

Precisely, for every \(0<\eta<1\), \(0<a<1\), and \(M>a\), put \(q=\eta M\) and \(\delta=a/[4M(1+q)]\). With the definitions below, for all \(0<t<\delta\):

\[
\tau_2(t)=1+qt,\qquad
h_2(t)=\begin{cases}a-t&q<1,\\ a&q=1,\\ a+t&q>1.\end{cases}
\]

The unique locally admissible implicit delay and corresponding solution satisfy
\[
\tau_*(t)=1+\frac{q}{1+q}t,\qquad h_*(t)=g(t)=a-t.
\]

At \(q=1\), for **all** integers \(j\ge1\),
\[
\tau_j(t)=\begin{cases}1&j\text{ odd},\\1+t&j\text{ even},\end{cases}\qquad
h_j(t)=\begin{cases}a-t&j\text{ odd},\\a&j\text{ even}.\end{cases}
\]
Therefore all finite nesting orders agree with the reference globally in this family if and only if \(q<1\). The implication for \(q<1\) is the published sufficiency theorem; the exact equality and supercritical counterexamples, together with the critical two-cycle and unique implicit branch, constitute the present finding.

## Assumptions and scope

Fix \(\bar\tau=1\), zero forcing \(F(t)=0\), and the linear sign-preserving response \(\Psi(u)=\eta u\). Let \(\operatorname{sign}(0)=0\). The continuous history on \([-2,0]\) is
\[
\varphi_M(s)=\max\{-a,\min\{a,M(s+1)\}\},\qquad -2\le s\le0.
\]
It has exactly Lipschitz constant \(L_\varphi=M\), satisfies \(\varphi_M(-1)=0\), \(\varphi_M(0)=a\), and has \(|\varphi_M(s)|\le a\).

For each fixed integer \(j\ge1\), the nested solution \(h_j\) equals \(\varphi_M\) on \([-2,0]\), is absolutely continuous on subsequent compact intervals of existence, and for almost every positive time satisfies
\[
 h'_j(t)=-\operatorname{sign}(h_j(t-\tau_j(t))),\quad
 \tau_1(t)=1,\quad
 \tau_{k+1}(t)=1+\eta h_j(t-\tau_k(t))\quad (1\le k<j).
\]
The implicit solution pair \((h_*,\tau_*)\) satisfies the corresponding differential equation and \(\tau_*(t)=1+\eta h_*(t-\tau_*(t))\), with a continuous delay valued in \((0,2)\). The reference \(g=h_1\) uses constant delay one. These are the nested and implicit conventions of Bolduc-St-Aubin, Subramanian and Krauskopf (2026).

The local formulas hold simultaneously for every parameter triple above. The global *subcritical* identification is imported from their Theorem 1.1, whose hypotheses are independently verified here. No assertion is made about long-time continuation of supercritical nested equations or eventual dynamics of the implicit equation.

## Proof

**1. The globally bounded reference.** On \((-1,0]\), the history is strictly positive. Hence \(g(t)=a-t\) for \(0\le t\le1\). Because this solution is positive on \([0,a)\), the same derivative continues until \(t=1+a\), giving \(g(1+a)=-1\). Delayed feedback then changes sign and the reference rises linearly to \(+1\) at time \(3+a\), falls to \(-1\) at \(5+a\), and repeats with temporal period four thereafter. Explicitly, for \(t\ge1+a\), write \(r=(t-1-a)\bmod4\) with \(0\le r<4\); then
\[
 g(t)=\begin{cases}-1+r&0\le r\le2,\\3-r&2\le r<4.\end{cases}
\]
Thus \(|g(t)|\le1\) for all \(t\ge0\), and \(\eta|g(t)|<1\) since \(\eta<1\). Similarly \(\eta|\varphi_M|\le\eta a<1\).

**2. A uniform initial method-of-steps interval.** Set \(q=\eta M\) and \(\delta=a/[4M(1+q)]\). Then \(0<\delta<\min\{1/4,a/M\}\). For \(0<t<\delta\), the arguments \(t-1\), \(t-(1+qt)\), and \(t-[1+qt/(1+q)]\) all belong to the central linear segment \((-1-a/M,-1+a/M)\) of the initial history. In particular all these delayed arguments are negative and all the relevant delays lie strictly in \((0,2)\). The local right-hand sides therefore depend only on the prescribed history, and integration yields unique local absolutely continuous solutions.

**3. The second nesting order is a sharp sign test.** Direct substitution gives
\[
 \tau_2(t)=1+\eta\varphi_M(t-1)=1+qt,
 \quad \varphi_M(t-\tau_2(t))=M(1-q)t.
\]
Its sign is positive, zero, or negative as \(q<1\), \(q=1\), or \(q>1\). Since \(h_2(0)=a\), integrating \(h'_2=-\operatorname{sign}\varphi_M(t-\tau_2(t))\) yields the displayed exact three-case formula. In particular, for \(q>1\), \(h_2(t)-g(t)=2t\), while at equality it equals \(t\): immediate genuine dynamical failure, not a failure of a numerical iteration stopping test.

**4. A unique implicit branch survives the transition.** For fixed \(t\), the function
\[
 H_t(u)=u-1-\eta\varphi_M(t-u)
\]
is strictly increasing in \(u\), because \(\varphi_M\) is nondecreasing. Hence there is at most one implicit delay in \((0,2)\). The proposed value \(\tau_*(t)=1+qt/(1+q)\) lies there and satisfies \(H_t(\tau_*)=0\); moreover \(\varphi_M(t-\tau_*(t))=Mt/(1+q)>0\). Consequently the unique local implicit solution is \(h_*(t)=a-t=g(t)\), even for \(q\ge1\). This uniqueness uses monotonicity, not a contraction estimate.

**5. The critical nonconvergent nesting operator.** If \(q=1\), then starting at \(\tau_1=1\) gives \(\tau_2=1+t\), and \(\varphi_M(t-1-t)=\varphi_M(-1)=0\), so \(\tau_3=1\). Induction gives an exact two-cycle \(1,1+t,1,1+t,\ldots\) at each fixed \(0<t<\delta\). An odd-order delay samples positive history; an even-order delay samples the zero at \(-1\). Integrating the corresponding feedback gives the alternating stated formulas for all \(j\). The fixed point is instead the unique value \(1+t/2\). It is not the limit of the nested iterates.

**6. Why invisibility holds globally on the strict side.** For \(q=\eta M<1\), choose a positive number \(c\) with \(\eta(1+c)<1\), possible since \(\eta<1\). The zero forcing is bounded by \(c\); \(\Psi\) is \(\eta\)-Lipschitz and sign-preserving; the history has Lipschitz constant \(M\); and Step 1 verifies the strict amplitude hypotheses for the entire reference trajectory. Theorem 1.1 of Bolduc-St-Aubin et al. therefore supplies \(h_j=g=h_*\) globally for every finite \(j\). Conversely \(q\ge1\) fails already at \(j=2\) by Step 3. This proves the if-and-only-if classification for the displayed family.

## Verification

The standalone `verify.py` checker uses exact rational arithmetic and reproduces the initial-history evaluations, the three possible second-order feedback signs, the implicit fixed-point equation, and the critical nesting two-cycle. It was run successfully on 140 rational parameter triples spanning all three regimes, with 25 nesting orders in the critical/subcritical cases. It also checks the reference triangle-wave formula against the differential equation at many rational nonswitching times. Run from the extracted package directory with `python3 verify.py`. These computations test the derivation; they are not substituted for the parameter-uniform proof above.

## Relationship to prior work

Bolduc-St-Aubin, Subramanian and Krauskopf (2026), Theorem 1.1, proved **sufficiency** of \(\eta L_\varphi<1\) together with \(\eta(1+c)<1\) and amplitude control for invisibility of all nested and implicit delays. Their Section 6 identifies the noncontracting regime and possible periodic delay iterates as directions for further study, but does not give this explicit history, an if-and-only-if threshold within it, the critical even/odd solution split, or the uniquely defined implicit solution coexisting with nonconvergent nesting. The sufficiency direction and the general suggestion of period-two nesting are **prior results**, not independently claimed here.

Keane, Krauskopf and Dijkstra (2019) investigated a smooth ENSO delay model through bifurcation analysis, including delayed state dependence; their model and claims do not give the present switched, clipped-history sharpness classification. Humphries, Krauskopf, Ruschel and Sieber (2021 preprint) analyzed nonlinear bifurcations for delayed state dependence in a different, smooth scalar feedback equation, also without this nested-iteration threshold.

## Limitations

This theorem is deliberately about one natural monotone clipped-history family and an initial time interval when \(q\ge1\); it is not a general necessary condition for invisibility for every history. Other noncontracting histories may remain invisible. For \(q>1\), possible high-order nesting branches and long-time continuation are not classified. For \(q=1\), the existence and exact disagreement of all finite nesting levels are established locally; no claim is made about their global attractors. The uniqueness of the implicit delay is local, and does not imply global implicit uniqueness. Historical priority remains provisional against specialized unindexed or nonpublic work.

## References

1. S. Bolduc-St-Aubin, P. Subramanian and B. Krauskopf, *Dynamic invisibility of implicit and nested state-dependent delays in a class of externally forced delay equations*, arXiv:2610.39281v1, first public 2026-10-29. https://arxiv.org/html/2610.39281v1
2. A. Keane, B. Krauskopf and H. A. Dijkstra, *The effect of state dependence in a delay differential equation model for the El Niño Southern Oscillation*, 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6661334/ ; doi:10.1098/rsta.2018.0121.
3. A. R. Humphries, B. Krauskopf, S. Ruschel and J. Sieber, *Interplay between instantaneous and delayed feedback with delayed state dependence* (preprint 2021; later published under a revised title), arXiv:2110.01850v1. https://arxiv.org/abs/2110.01850
