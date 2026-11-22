# An exact one-crossing phase law and a spectral–progeny reversal under two-channel message displacement

## Finding

In a two-channel information-diffusion branching model with partial displacement of offspring from the initially seeded channel, moderation may lower the asymptotic reproduction rate *and* nevertheless raise the expected number of messages. This effect occupies an exact, nonempty parameter wedge. The mean number of concurrently active messages has a universal, unique, positive-time crossing relative to unmoderated dynamics in the competing-sign regimes; the integrated excess can keep its initial sign over **every** finite horizon even after the instantaneous excess turns negative.

**Theorem.** Let \(0<d<a<1\), \(b,c>0\), and \(0<u\le1\). Define
\[
M(u)=\begin{pmatrix}a(1-u)&c\\bu&d\end{pmatrix},\qquad
B=b-a,\qquad D=bc-a(a-d).
\]
Let \(R_u(t)\) be the expected total number of active messages at time \(t\), from one initially active type-one message, and let \(C_u=\int_0^\infty R_u(t)\,dt\), whenever the integral is finite. Then:

1. \(R_0(t)=e^{(a-1)t}\). For every \(u>0\), the sign of \(R_u(t)-R_0(t)\) at all \(t>0\) is strictly positive if \(B\ge0,D\ge0\) but not both zero, and strictly negative if \(B\le0,D\le0\) but not both zero. If \(B>0>D\) there exists exactly one \(t_*>0\), with positive excess before and negative after. If \(B<0<D\), the corresponding unique crossing is from negative to positive. If \(B=D=0\), the total expected trajectories coincide for all times.
2. The spectral radius \(\rho(M(u))\) is strictly less than \(a\), equal to \(a\), or strictly greater than \(a\), according as \(D<0\), \(D=0\), or \(D>0\); this comparison is independent of the chosen positive moderation intensity.
3. If \(D<0\), both processes are subcritical and
\[
 C_u=\frac{1-d+bu}{(1-a)(1-d)+u[a(1-d)-bc]},\quad
 C_u-C_0=\frac{u[b(1-a+c)-a(1-d)]}{(1-a)\{(1-a)(1-d)+u[a(1-d)-bc]\}}.
\]
 Consequently a spectral reduction together with a strictly greater total mean progeny is possible **exactly** for
\[
 c<a-d,\qquad \frac{a(1-d)}{1-a+c}<b<\frac{a(a-d)}c.
\]
 Every such point has \(b>a\) and a unique instantaneous excess crossing from above to below.
4. Fix \(D<0\) and \(b>a\). Let \(F_u(T)=\int_0^T[R_u(t)-R_0(t)]\,dt\). If \(b\ge a(1-d)/(1-a+c)\), then \(F_u(T)>0\) for every finite \(T>0\) (equality in the threshold gives \(\lim_{T\to\infty}F_u(T)=0\)). If \(a<b<a(1-d)/(1-a+c)\), then \(F_u\) has exactly one positive zero, strictly after \(t_*\), and is eventually negative.

## Assumptions and scope

Messages have independent exponential lifetimes of mean one. A type-one message, upon removal, produces independent Poisson offspring of types one and two with respective means \(a(1-u)\) and \(bu\); a type-two message produces independent Poisson offspring with means \(c\) and \(d\). Every offspring starts a new independent lifetime. This is a linear infinite-audience branching approximation, with column \(j\) of \(M\) encoding the expected offspring vector from parent type \(j\). No unobserved type-specific seed mixture is assumed. The parameter \(u\) is an idealized displacement intensity and does not directly measure an actual platform's moderation efficacy.

The observable \(R_u(t)\) counts currently active messages, whereas \(C_u\) counts their lifetime-integrated activity; since mean lifetime is one, \(C_u\) also equals the expected total number of messages ever generated, *including the initial seed*, in the subcritical model.

## Proof

**Mean dynamics.** The continuous-time branching generator gives \(z'_u(t)=(M(u)-I)z_u(t)\), with \(z_u(0)=(1,0)^\top\), so \(R_u(t)=(1,1)e^{(M(u)-I)t}(1,0)^\top\). At \(u=0\), no type-two message is generated and \(R_0(t)=e^{(a-1)t}\).

**Spectral comparison.** For \(u>0\) the off-diagonal entries are strictly positive. Its eigenvalues are
\[
 \lambda_\pm=\tfrac12\left(a(1-u)+d\pm\sqrt{[a(1-u)-d]^2+4bcu}\right),\quad \lambda_-<\min\{a(1-u),d\}<a.
\]
The characteristic polynomial at \(a\) equals \(u[a(a-d)-bc]=-uD\). Since \(\lambda_-<a\), its sign determines whether \(\lambda_+\) lies below, at or above \(a\). Because this is a positive matrix, \(\rho(M(u))=\lambda_+\).

**Single crossing.** Remove the common survival factor and normalize by the unmoderated mean: \(f_u(t)=R_u(t)/R_0(t)=(1,1)e^{(M(u)-aI)t}(1,0)^\top\). Diagonalization yields
\[
 f_u(t)=A_ue^{(\lambda_+-a)t}+(1-A_u)e^{(\lambda_--a)t},\qquad
 A_u=\frac{a+u(b-a)-\lambda_-}{\lambda_+-\lambda_-}>0.
\]
The strict positivity holds because \(a+u(b-a)=a(1-u)+bu\) exceeds \(\lambda_-\). The derivative is a linear combination of two exponentials with distinct exponents; after division by either exponential, it is a strictly monotone exponential plus a constant, unless one coefficient vanishes. Thus \(f'_u\) has **at most one zero** for positive time. We have \(f_u(0)=1\), \(f'_u(0)=uB\), and \(f_u(t)\to0\) for \(D<0\), \(f_u(t)\to\infty\) for \(D>0\). If \(D=0\), \(\lambda_+=a\) and \(f_u(t)=A_u+(1-A_u)e^{(\lambda_--a)t}\) is monotone or constant. With \(D\ne0\), these endpoint properties and the one-extremum bound give exactly the sign cases and unique positive crossings in the theorem (including cases where the initial derivative is zero). In the simultaneous boundary \(B=D=0\), \(b=a\) and \(c=a-d\), so both columns of \(M(u)\) sum to \(a\), giving \(R_u(t)=R_0(t)\) exactly.

**Expected total progeny and the wedge.** If \(D<0\), \(\lambda_+<a<1\), hence \(C_u=(1,1)(I-M(u))^{-1}(1,0)^\top\). Direct inversion gives the displayed expression. Its denominator is strictly positive because \(\rho(M(u))<1\), so the sign of the excess is exactly that of \(b(1-a+c)-a(1-d)\). Combining this with \(bc<a(a-d)\) gives the interval in part 3. It is nonempty exactly if \(c<a-d\), obtained by cross-multiplying its two strictly positive endpoints. Under that inequality, its lower endpoint exceeds \(a\), proving initial activity rises in the wedge.

**Finite-horizon ordering.** For \(B>0>D\), part 1 yields a unique \(t_*\), with \(F'_u(T)>0\) before that time and \(F'_u(T)<0\) thereafter. The finite-horizon difference starts from zero, rises strictly to a positive maximum, and falls monotonically to \(C_u-C_0\). If the limit is nonnegative, all finite values remain positive; if negative, it has exactly one subsequent zero. This proves part 4.

## Verification

The included standalone `checker.py` reconstructs the matrix exponential and resolvent directly, using `numpy` and `scipy`. It checks the exact rational witness, 1,600 seeded parameter draws (12,800 two-exponential comparisons), 120 parameter draws in the paradox wedge, and finite-horizon cumulative behavior. The tests passed in this package. These finite tests supplement, but are not substitutes for, the analytic proof.

**Exact rational witness.** Choose \(a=7/10\), \(d=1/5\), \(b=2\), \(c=1/10\), and \(u=1\). Then
\[
 \rho(M(0))=\frac7{10},\quad \rho(M(1))=\frac{1+\sqrt{21}}{10}<\frac7{10},\quad C_0=\frac{10}{3},\quad C_1=\frac{14}{3}.
\]
The instantaneous excess is initially positive, becomes negative exactly once, and its unique crossing is approximately \(t_*=6.658067198521\). Nonetheless, \(F_1(T)>0\) for *every* finite \(T>0\).

## Relationship to prior work

Murdock, Carley and Yağan (2024) experimentally model cross-platform user migration after moderation and document potential global increases in misinformation awareness under single-platform moderation. That qualitative adverse-displacement phenomenon is prior work; it is not a novel claim here. Keating, Gleeson and O'Sullivan (2022) use multitype branching mean matrices for complex contagion, including spectral analysis and expected cascade sizes through matrix resolvents. Those general tools are established and are not claimed as inventions. Allen (2015) reviews multitype branching and dispersal applications in population and epidemic models. The narrower claim assessed here is the complete *closed-form* two-channel displacement phase diagram—its universal one-crossing time structure, an exact feasibility wedge for opposed spectral and total-progeny rankings, and its finite-horizon consequence—under the displayed matrix and stated hypotheses. These sources do not themselves explicitly state that combined classification. Other mathematical sources may imply portions of it; exhaustive historical priority is not claimed.

## Limitations

The model assumes constant per-message reproduction, infinite message-receptive audience, two homogeneous channels, unit-rate independent exponential lifetimes and independent Poisson offspring. It does not model strategic migration, actual user exposure, network saturation, content virality measurement or finite population effects. The mean active-message count and total message progeny are *not* probabilities of belief change, distinct persons reached, real-world harm or policy effects. The spectral-growth paradox is an exact theoretical warning, not evidence that any specific moderation policy increases misinformation. Novelty assessments are limited to the inspected sources and index searches; independent external audit has not been performed.

## References

1. Murdock, I., Carley, K. M. and Yağan, O. (2024). *An agent-based model of cross-platform information diffusion and moderation*. Social Network Analysis and Mining **14**, 145. First public date: 2024-07-26. https://doi.org/10.1007/s13278-024-01305-x
2. Keating, L. A., Gleeson, J. P. and O'Sullivan, D. J. P. (2022). *Multitype branching process method for modeling complex contagion on clustered networks*. Physical Review E **105**, 034306. https://doi.org/10.1103/PhysRevE.105.034306
3. Allen, L. J. S. (2015). *Applications of Multi-Type Branching Processes*. In *Stochastic Population and Epidemic Models*. https://pmc.ncbi.nlm.nih.gov/articles/PMC7124073/
