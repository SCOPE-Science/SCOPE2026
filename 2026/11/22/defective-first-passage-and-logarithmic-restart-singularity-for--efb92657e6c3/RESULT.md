# Defective first passage and logarithmic restart singularity for geometric-counting telegraph transport

## Finding

A persistent searcher with alternating velocities \(+v\) and \(-v\), whose two directional reversal clocks are independent geometric counting processes, can fail to hit a fixed target even though the two clocks have the same marginal intensity. Explicitly, let both directional rates be independently drawn from an exponential law of mean \(\lambda\) at the start of each trajectory. The particle starts at the origin with velocity \(+v\), and its target is at \(+L\). Write \(T_L\) for the no-reset first hitting time, with \(T_L=\infty\) if the target is never hit. For \(v,L,\lambda>0\), set \(\beta=\lambda L/v\). Then

\[
\Pr(T_L=\infty)=\frac{\beta}{2(1+\beta)}>0,
\qquad
\mathbb E[T_L\mathbf1_{\{T_L<\infty\}}]=\infty.
\]

For the defective first-passage Laplace transform \(\phi(s)=\mathbb E[e^{-sT_L}\mathbf1_{\{T_L<\infty\}}]\), the exact expression and singular limit are

\[
\phi(s)=\mathbb E_{A,B}\!\left[\exp\!\left(-\frac{L}{2v}\left[A-B+\sqrt{(A-B)^2+4s(s+A+B)}\right]\right)\right],
\]

\[
\phi(0)=\frac{2+\beta}{2(1+\beta)},\qquad
\phi(0)-\phi(s)=\frac{L}{2v}s\log\frac{\lambda}{s}+O(s)\quad(s\downarrow0).
\]

Here \(A,B\) are independent exponential random variables of mean \(\lambda\). If independent Poisson resets at rate \(r>0\) return the particle to the origin and renew both directional clocks and the initial velocity, then the first-contact time \(T_{L,r}\) is almost surely finite with mean

\[
M(r)=\mathbb E T_{L,r}=\frac{1-\phi(r)}{r\phi(r)}.
\]

The mean has the two sharp extreme-rate asymptotics

\[
M(r)=\frac{\beta}{\beta+2}\frac1r
+\frac{2L}{v}\left(\frac{1+\beta}{\beta+2}\right)^2\log\frac{\lambda}{r}
+O(1)\quad(r\downarrow0),
\]

\[
M(r)\sim(1+\beta)\frac{e^{rL/v}}r\quad(r\to\infty).
\]

Consequently \(M\) attains at least one global minimum at a finite strictly positive reset rate. Uniqueness of this minimizer is not asserted.

## Assumptions and scope

The two independent geometric counting processes have a mixed-Poisson realization: draw \(A,B\overset{\mathrm{iid}}\sim\mathrm{Exp}(\text{mean }\lambda)\) at the beginning of one movement episode, then conditionally use a Poisson switching process of rate \(A\) while moving right and rate \(B\) while moving left. The rates remain fixed throughout that movement episode, including any repeated visits to either velocity. This produces dependent, heavy-tailed same-direction holding times after mixing. An independent Poisson reset terminates an episode; the next episode redraws both rates and restarts at position zero with positive velocity. All resets are instantaneous, the target is absorbing, and there is no additional diffusion. The claims concern a right-hand target \(+L\); reflection gives the analogous left-target protocol with reflected initial velocity. Degenerate limits such as \(\lambda=0\), \(v=0\), and \(L=0\) are excluded.

The primary classification is MSC2020 82C31, for stochastic persistent transport and resetting in statistical physics.

## Proof

**1. Conditional first-passage transform.** Conditional on \(A=a>0\) and \(B=b>0\), let \(f_\pm(x;s)\) denote the discounted probability of hitting \(+L\) from \(x<L\) when the current velocity is \(\pm v\). The backward equations are

\[
v\partial_x f_+-(s+a)f_++af_-=0,\qquad
-v\partial_x f_--(s+b)f_-+bf_+=0.
\]

For \(s>0\), the bounded solution as \(x\to-\infty\) and outgoing boundary condition \(f_+(L;s)=1\) yield \(f_+(0;s)=\exp[-k(a,b;s)L]\), with

\[
k(a,b;s)=\frac{a-b+\sqrt{(a-b)^2+4s(s+a+b)}}{2v}.
\]

Indeed the two spatial characteristic roots have opposite signs, and the bounded root is the displayed nonnegative root. The negative-velocity boundary value at \(L\) is determined by the interior equations, not independently prescribed. Mixing over \(a,b\) gives the exact stated transform. The formula extends to \(s=0\) by monotone convergence.

**2. Defect at zero discount.** At \(s=0\), \(k(a,b;0)=(a-b)_+/v\). Since \(A-B\) is symmetric Laplace with density \(e^{-|d|/\lambda}/(2\lambda)\),

\[
\phi(0)=\frac12+\frac1{2\lambda}\int_0^\infty e^{-d(1/\lambda+L/v)}\,\mathrm{d}d
=\frac{2+\beta}{2(1+\beta)}.
\]

The complementary probability is the claimed positive defect.

**3. A one-dimensional quadrature and the logarithmic singularity.** Let \(c=L/(2v)\) and \(h=\sqrt{s\lambda}\). The variables \(d=|A-B|\) and \(u=2\min(A,B)/\lambda\) are independent, with \(d\) exponential of mean \(\lambda\) and \(u\) unit exponential; the sign of \(A-B\) is equiprobable. Integrating \(u\) using a Gaussian tail yields the exact one-dimensional formula

\[
\phi(s)=e^{-2cs}\int_0^\infty w(d)\left[1-c\sqrt{\pi}\,h\;\operatorname{erfcx}\!\left(\frac{d+2s(1+c\lambda)}{2h}\right)\right]\,\mathrm{d}d,
\qquad
w(d)=\frac{e^{-d/\lambda}}{2\lambda}(1+e^{-2cd}),
\]

where \(\operatorname{erfcx}(z)=e^{z^2}\operatorname{erfc}(z)\), and \(\int_0^\infty w(d)\,\mathrm{d}d=\phi(0)\). In particular, writing the bracket correction integral as \(J_s\), one has \(\phi(s)=e^{-2cs}[\phi(0)-J_s]\).

Here is an explicit asymptotic error argument. The region \(0<d<h\) contributes \(O(s)\) to \(J_s\), since \(\operatorname{erfcx}(z)\le1\) for \(z\ge0\), and \(c\sqrt{\pi}h\int_0^h w(d)\,\mathrm{d}d=O(s)\). For \(d\ge h\), the classical Gaussian-tail integration-by-parts estimate, uniform for \(z\ge1/2\), is \(\operatorname{erfcx}(z)=(\sqrt\pi z)^{-1}+O(z^{-3})\). The remainder contributes \(O(s)\), because \(h^4\int_h^\infty w(d)d^{-3}\,\mathrm{d}d=O(s)\). The shift \(2s(1+c\lambda)\) in the argument also changes the leading integral by \(O(s)\). Therefore

\[
J_s=2cs\lambda\int_h^\infty \frac{w(d)}d\,\mathrm{d}d+O(s)
=cs\log(\lambda/s)+O(s),
\]

using \(w(d)=\lambda^{-1}+O(d)\) near zero and its exponential decay at infinity. As \(e^{-2cs}=1+O(s)\), this gives the claimed logarithmic expansion. Differentiating the Laplace transform in its monotone-difference form and letting \(s\downarrow0\) shows

\[
\mathbb E[T_L\mathbf1_{\{T_L<\infty\}}]
=\lim_{s\downarrow0}\frac{\phi(0)-\phi(s)}s=\infty.
\]

**4. Renewal resetting.** Each attempt succeeds before its independent exponential reset precisely with probability \(\phi(r)>0\). Its expected elapsed duration is \([1-\phi(r)]/r\), including both successful and failed attempts. The renewal equation gives \(M(r)=[1-\phi(r)]/[r\phi(r)]\). The number of attempts is almost surely finite since each attempt has the same strictly positive success probability. Expanding the reciprocal of the small-\(r\) formula gives the asserted \(1/r\) plus logarithm expansion. In detail, \(\phi(0)=(2+\beta)/[2(1+\beta)]\), and the reciprocal expansion has logarithm coefficient \(c/\phi(0)^2=2L(1+\beta)^2/[v(\beta+2)^2]\). The stronger \(O(s)\) remainder from step 3 suffices for the displayed \(O(1)\) remainder in \(M\).

**5. Frequent resetting and existence of an optimal rate.** For each fixed \(a,b\),

\[
\lim_{s\to\infty}\big(k(a,b;s)-s/v\big)=a/v,
\qquad k(a,b;s)\ge s/v.
\]

The inequality follows because the square-root term is at least \(2s+b-a\), since its square differs from \((2s+b-a)^2\) by \(8as\), which is positive. Dominated convergence in the rate mixture therefore gives

\[
\lim_{s\to\infty}e^{sL/v}\phi(s)=\mathbb E[e^{-AL/v}]=\frac1{1+\beta}.
\]

Substitution into the renewal formula proves the high-reset asymptotic. Since \(M\) is continuous on \((0,\infty)\), positive, and diverges as \(r\downarrow0\) and \(r\to\infty\), it attains a global minimum at an interior positive rate.

## Verification

The accompanying `check.py` evaluates the one-dimensional Gaussian-tail quadrature and compares it with a distinct double-integral representation over the independent positive rate difference and minimum for multiple \((L,v,\lambda,r)\) choices. It checks the exact zero-discount success probability, the small-\(s\) logarithmic coefficient, the high-\(s\) exponential prefactor, positivity and representative reset-cost values. The script uses Python 3 and SciPy; running `python check.py` prints the number of passing deterministic assertions. All asymptotic, nonhitting, and optimization-existence statements above are proved analytically; finite quadrature tests do not certify infinite limits.

## Relationship to prior work

Di Crescenzo, Iuliano, Mustaro and Verasani (arXiv:2310.10231, Sections 2–5) develop exactly the two-geometric-clock transport with Poisson resetting and obtain position laws and moments, not a first-hitting-time result. Their conclusion explicitly identifies the first-passage problem for this model as a direction for further investigation. Ratanov (arXiv:2102.04905, Section 2) analyzes first-passage distributions for a two-state Markov telegraph with deterministic reversal rates. This supplies a closely related conditional method but not the exponential mixture, positive no-hit defect, logarithmic threshold or renewed-reset asymptotics. Cinque and Orsingher (arXiv:2010.02689) analyze extrema for a Poisson-driven asymmetric-velocity telegraph; the switching-clock model is different. Iuliano and Verasani (2024, DOI 10.1007/s11009-024-10083-0) introduce first passage for a different four-direction three-dimensional geometric-counting process. Di Crescenzo, Iuliano and Verasani (2026, DOI 10.1007/s10955-026-03670-7) study Bernoulli resets at velocity-switching times, also a distinct protocol.

The originality asserted here is the *annealed two-geometric-clock first-passage/Poisson-reset theorem and its sharp rate asymptotics*, not the general fixed-rate Markov telegraph backward equations or generic resetting renewal identity. Literature and research-database searches found no dominating result among inspected sources; lack of universal indexing means unlocated equivalent work remains possible.

## Limitations

No uniqueness, numerical value, or monotonicity of the optimal positive reset rate is proved. The result assumes the two hidden rates are drawn once per movement episode, are exponential with the same positive mean, and are refreshed upon each Poisson reset. It does not apply to independent redraws at every velocity switch, to rates retained across resets, to Lévy-reset clocks, to finite intervals or to a diffusive particle. The result concerns the unconditional annealed success and mean search time; conditioned quenched paths can behave differently. Publication priority is conditional on accessible full-text and indexed literature coverage; independent scientific validation has not been performed.

## References

1. A. Di Crescenzo, A. Iuliano, V. Mustaro, G. Verasani, *On the Telegraph Process Driven by Geometric Counting Process with Poisson-Based Resetting*, arXiv:2310.10231 (first public 16 October 2023); Journal of Statistical Physics 190, 191 (2023), DOI: 10.1007/s10955-023-03189-1. https://arxiv.org/pdf/2310.10231
2. A. Di Crescenzo, A. Iuliano, V. Mustaro, *On Some Finite-Velocity Random Motions Driven by the Geometric Counting Process*, Journal of Statistical Physics 190, 44 (2023), DOI: 10.1007/s10955-022-03045-8.
3. N. Ratanov, *On Telegraph Processes, Their First Passage Times and Running Extrema*, arXiv:2102.04905 (2021). https://arxiv.org/pdf/2102.04905
4. F. Cinque, E. Orsingher, *On the Exact Distributions of the Maximum of the Asymmetric Telegraph Process*, arXiv:2010.02689 (2020). https://arxiv.org/pdf/2010.02689
5. A. Iuliano, G. Verasani, *A Cyclic Random Motion in Three Dimensions Driven by Geometric Counting Processes*, Methodology and Computing in Applied Probability 26, 14 (2024), DOI: 10.1007/s11009-024-10083-0.
6. A. Di Crescenzo, A. Iuliano, G. Verasani, *A Generalized Telegraph Process with Resetting to the Origin Driven by Bernoulli Trials*, Journal of Statistical Physics (2026), DOI: 10.1007/s10955-026-03670-7.
