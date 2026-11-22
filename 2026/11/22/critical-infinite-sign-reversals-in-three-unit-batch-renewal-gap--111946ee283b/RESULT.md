# Critical infinite sign reversals in three-unit batch-renewal gaps

## Finding

Consider an ordinary-origin batched renewal count with batches of size one or three, followed by an independent inverse-subordinator clock. The covariance between consecutive **individual-index** interarrival gaps changes sign infinitely often precisely at the mixture weight at which its eventual (stationary) covariance vanishes. A neighborhood of that critical mixture has a sharp logarithmic cutoff for the final sign reversal. These facts hold for every admissible clock, not merely exponential waiting times.

**Theorem.** Fix \(\lambda>0\), \(q\in(0,1)\), and an independent, almost surely strictly increasing, nonkilled subordinator \(D\) with Laplace exponent \(g\) and \(0<d=\mathbb E D(1)<\infty\). For definiteness suppose \(\mathbb E D(1)^2<\infty\). Let \(E(t)=\inf\{s>0:D(s)>t\}\) be its right-continuous inverse, let \(N_\lambda\) be an independent rate-\(\lambda\) Poisson process, and let independent marks \(B_j\) satisfy \(\Pr(B_j=1)=q\), \(\Pr(B_j=3)=1-q\). Put
\[
M(t)=\sum_{j=1}^{N_\lambda(E(t))}B_j,\qquad
\tau_n=\inf\{t\ge0:M(t)\ge n\},\quad
G_n=\tau_n-\tau_{n-1},\quad\tau_0=0.
\]
Thus successive individuals in the same batch have zero gap. Write \(a=1-q\), \(m=3-2q\), \(\mu=d/\lambda\), and let \(u_n=0\) for \(n<0\), \(u_0=1\), \(u_n=q u_{n-1}+a u_{n-3}\) for integers \(n\ge1\). For all integers \(1\le n<k\),
\[
\mathbb E G_n=\mu u_{n-1},\qquad
\operatorname{Cov}(G_n,G_k)
=\mu^2u_{n-1}(u_{k-n}-u_{k-1}). \tag{1}
\]
In particular, for \(n\ge2\),
\[
C_n(q):=\operatorname{Cov}(G_n,G_{n+1})
=\mu^2 u_{n-1}(q-u_n).\tag{2}
\]
Set \(r=\sqrt a\), \(\theta=\arccos(-r/2)\in(\pi/2,2\pi/3)\) and \(\kappa=q/\sqrt{a(4-a)}\). The exact sign law is
\[
C_n(q)=\frac{\mu^2 a}{m}u_{n-1}
\left[(2q-1)-2r^n\{\cos(n\theta)+\kappa\sin(n\theta)\}\right].\tag{3}
\]
Hence \(C_n(q)\) has strictly negative eventual sign if \(q<1/2\), and strictly positive eventual sign if \(q>1/2\). At \(q=1/2\), infinitely many of its terms are strictly positive and infinitely many are strictly negative, and \(|C_n(1/2)|=O(2^{-n/2})\) with the corresponding lower-order magnitude attained along infinite positive and negative subsequences.

For \(q\ne1/2\), let \(L(q)\) be the largest integer \(n\ge2\) for which \(C_n(q)\) has the sign *opposite* to \(2q-1\), taking \(L(q)=0\) if there is no such integer. Then \(L(q)<\infty\) and, as \(q\to1/2\) through either side,
\[
L(q)=\frac{2}{\log 2}\log\frac1{|q-1/2|}+O(1).\tag{4}
\]
The \(O(1)\) is uniform from both sides near the critical point. Every assertion about signs and the cutoff is independent of the detailed law of the inverse-subordinator clock, except for the positive factor \(\mu^2\).

**Minimality of the burst gap.** If the mark law instead has support \(\{1,2\}\) with positive probabilities \(q,1-q\), then consecutive noninitial individual gaps have \(\operatorname{Cov}(G_n,G_{n+1})<0\) for every \(n\ge2\); deterministic unit marks give independent gaps and zero covariance. Consequently the one-or-three family is the first two-size, unit-containing burst family that permits positive covariance and a critical infinite-reversal regime.

## Assumptions and scope

All clocks and marks are independent. The subordinator has nondecreasing cadlag paths with almost surely strict increase, zero killing, finite positive mean, and finite second moment. Such clocks include the drift-plus-compound-Poisson family \(g(s)=s+\eta(1-e^{-s})\) for every \(\eta>0\), as well as pure positive drift. The second-moment assumption guarantees that individual gap variances exist; identity (1), which only involves cross products of distinct batch waits, actually requires just the stated finite first moment. No Brownian or stable-noise assumption is made. The analysis is for ordinary initialization at individual index one; it is not a stationary-Palm indexing of individual arrivals.

The asymptotic in (4) concerns the *last individual-index sign anomaly*, not the first arrival time nor the stationary-lag covariance. For fixed \(q\ne1/2\), sufficiently late adjacent gap covariance has its eventual sign. At criticality the sign sequence need not alternate at every consecutive index.

## Proof

**1. Reduction to a marked renewal process.** Write the Poisson operational arrival epochs \(T_j\), with \(T_0=0\). Independence and absence of fixed-time jumps imply \(D\) does not jump at any \(T_j\), almost surely. Since \(D\) is strictly increasing, the physical batch epochs are \(D(T_j)\). The successive batch waiting times \(W_j=D(T_j)-D(T_{j-1})\) are therefore iid, independent of all marks, with
\[
\mathbb E e^{-sW_j}=\frac{\lambda}{\lambda+g(s)},\qquad \mathbb E W_j=\mu.
\]
Let \(S_j=\sum_{i=1}^jB_i\), \(S_0=0\). The set of strictly positive individual gaps is exactly the set of indices \(n=S_{j-1}+1\): there \(G_n=W_j\), whereas all other \(G_n=0\). The renewal probability \(u_t=\Pr(\exists j\ge0:S_j=t)\) satisfies the displayed recurrence. Given the independent marks, \(\{S_j=n-1\}\) and \(\{S_l=k-1\}\) jointly have probability \(u_{n-1}u_{k-n}\) when \(n<k\), by the ordinary renewal property. On joint occurrence the corresponding two batch waits are distinct and independent, so
\[
\mathbb E(G_nG_k)=\mu^2u_{n-1}u_{k-n}.
\]
Subtracting \(\mathbb E G_n\,\mathbb E G_k=\mu^2u_{n-1}u_{k-1}\) proves (1) and (2).

**2. Exact oscillatory renewal mass.** The recurrence gives the rational generating function
\[
U(z)=\sum_{n\ge0}u_nz^n=\frac1{1-qz-az^3}
=\frac1{m(1-z)}+\frac{a(2+z)}{m(1+az+az^2)}.
\]
For \(v_0=2\), \(v_1=2q-1\), and \(v_n=-a(v_{n-1}+v_{n-2})\) thereafter, coefficient extraction gives \(u_n=m^{-1}+am^{-1}v_n\). The two characteristic roots are \(r e^{\pm i\theta}\), where \(r=\sqrt a<1\) and \(2\cos\theta=-r\). Matching the two initial values yields
\[
v_n=2r^n[\cos(n\theta)+\kappa\sin(n\theta)],
\qquad\kappa=\frac{q}{\sqrt{a(4-a)}}.
\]
Since \(q-1/m=a(2q-1)/m\), substitution into (2) proves (3). The bound \(|v_n|\le2r^n\sqrt{1+\kappa^2}\) immediately proves the two noncritical eventual signs and geometric covariance decay about those signs.

**3. Infinite critical reversals.** At \(q=1/2\), \(a=1/2\) and \(2\cos\theta=-1/\sqrt2\). The angle \(\theta/\pi\) is irrational: if it were rational, \(2\cos\theta\) would be an algebraic integer (being the sum of two roots of unity), whereas \(-1/\sqrt2\) has nonintegral norm \(-1/2\) and is not an algebraic integer. Consequently the angles \(n\theta\bmod2\pi\) are dense. The continuous nonzero sinusoid \(\cos x+\kappa\sin x\) takes both positive and negative values on open arcs, hence infinitely many indices yield each sign. At those indices \(u_{n-1}\to1/m>0\) and the sinusoid stays bounded away from zero along suitable infinite subsequences, establishing the claimed \(2^{-n/2}\) magnitude on both signs.

**4. Sharp logarithmic cutoff near criticality.** Put \(\delta=q-1/2\), \(F_q(n)=\cos(n\theta(q))+\kappa(q)\sin(n\theta(q))\), and \(h(q)=-\log r(q)>0\). The bracket in (3) is \(2\delta-2e^{-nh(q)}F_q(n)\). Its second term is uniformly bounded by \(2e^{-nh(q)}\sqrt{1+\kappa(q)^2}\) near \(q=1/2\). Thus no opposite-sign terms occur beyond \(\log(1/|\delta|)/h(q)+O(1)\).

For the matching lower bound, irrational rotation by \(\theta(1/2)\) visits both a fixed positive arc and a fixed negative arc of the sinusoid with bounded gaps: choose finitely many rotated open arcs covering the circle, using density and compactness. Hence some constants \(K\in\mathbb N\), \(c>0\) have the property that, for every phase and every block of \(K\) consecutive indices, the sinusoid attains a value above \(c\) and a value below \(-c\). Continuity of \(\theta(q)\) and \(\kappa(q)\) makes the same property hold uniformly for all \(q\) sufficiently close to \(1/2\) (possibly with smaller \(c\)). In the block immediately preceding \(\log(1/|\delta|)/h(q)-C\), for sufficiently large fixed \(C\), the oscillating term dominates \(2|\delta|\) at the appropriate phase, giving an opposite-sign term. Therefore
\[
L(q)=\frac{\log(1/|\delta|)}{h(q)}+O(1).
\]
Because \(h(q)=\tfrac12\log2+O(\delta)\) and \(\delta\log(1/|\delta|)\to0\), this is (4).

**5. Why maximum burst two cannot do this.** With marks \(1\) and \(2\), the renewal generating function factors as
\[
\frac1{1-qz-(1-q)z^2}=
\frac1{(1-z)[1+(1-q)z]}.
\]
Consequently \(u_n=[1+(1-q)(-1+q)^n]/(2-q)\). For each \(n\ge2\), direct comparison gives \(u_n>q\). Applying the same renewal covariance identity (2) gives strictly negative consecutive covariance for every \(n\ge2\). This proves minimality within the stated unit-containing two-point mark laws.

## Verification

The standalone Python 3 program `verify.py` checks 1,310 exact rational and numerical finite assertions: the renewal recurrence against exhaustive small compositions, joint boundary probabilities against explicit weighted burst paths, the rational partial fractions, the complex-root formula, the noncritical and critical finite-index sign patterns, and the maximum-two-burst inequality. Run `python3 verify.py` using Python's standard library. The proof above, not finite truncation, establishes irrational phase recurrence, infinitely many reversals and the logarithmic cutoff.

## Relationship to prior work

Tathe and Ghosh (first publicly posted 2026-11-12, arXiv:2611.16676v1) define a broad time-changed compound Poisson framework and derive state-count marginals, waiting-time distributions and arrival-time transform/matrix representations. Their construction includes the inverse-clock special case used here, but the inspected Sections 3 and 6.4 do not give ordinary-origin adjacent **individual-gap** covariances, an exact three-unit burst phase diagram or a last-sign-reversal scaling law.

Fretwell and Kouvatsos, in their chapter *Modelling LRD and SRD Traffic with the Batch Renewal Process* (in *Network Performance Engineering*, 2011, Section 3), give general **stationary** batch-renewal covariance generating functions and identify renewal-batch dependence mechanisms. Their theory covers the eventual stationary covariance and is not claimed as new. The present question specifically retains the ordinary initial batch, so its index-dependent transient covariance, critical infinite oscillation, uniform-clock invariance and critical-window cutoff require a separate renewal analysis.

Meerschaert, Nane and Vellaisamy (2011) establish the renewal representation for the fractional Poisson process via inverse stable subordinators, providing context for the clock reduction. The result here does not assert a new basic inverse-subordinator renewal representation.

## Limitations

The universal sign results concern independent iid burst marks, the explicit \(\{1,3\}\) mixture, and ordinary-origin individual indexing. They do not classify arbitrary burst supports, general dependent marking, or correlations measured by physical-time lag. Finite arithmetic experiments do not establish the infinite phase results. Some older specialized literature may contain an equivalent oscillatory-renewal specialization; historical priority is not guaranteed. The accessible text of the relevant batch-renewal handbook chapter was inspected, but PDF page images could not be rendered; this limits full-layout verification of that source. Independent review has not been performed.

## References

1. K. Tathe and S. Ghosh, *Time-changed Compound Poisson Process*, arXiv:2611.16676v1 (first public version 2026-11-12), https://arxiv.org/html/2611.16676v1 and https://arxiv.org/abs/2611.16676.
2. R. J. Fretwell and D. D. Kouvatsos, *Modelling LRD and SRD Traffic with the Batch Renewal Process: Review of Results and Open Issues*, in D. D. Kouvatsos (ed.), *Network Performance Engineering*, LNCS 5233, Springer, 2011, Chapter beginning p. 141, Section 3; available at https://pws.npru.ac.th/sartthong/data/files/Network_Performance_Engineering__A_Handbook.pdf.
3. M. M. Meerschaert, E. Nane and P. Vellaisamy, *The fractional Poisson process and the inverse stable subordinator*, *Electronic Journal of Probability* 16 (2011); arXiv:1007.5051, https://arxiv.org/abs/1007.5051.
