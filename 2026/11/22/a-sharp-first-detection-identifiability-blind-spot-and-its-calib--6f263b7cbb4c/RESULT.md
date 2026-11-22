# A sharp first-detection identifiability blind spot and its calibrated-effort repair

## Finding

A sensor alternates between a state with no target available and a state with the target available, at rates \(c>0\) and \(e>0\) respectively. A detection is produced at rate \(s d\) while available, where \(d>0\) is an intrinsic detection rate and \(s>0\) is a known effort multiplier. The initial probability of availability \(q\in[0,1]\) is known. Only time until the **first** detection is recorded.

**Theorem (complete one-effort blind spots and two-effort repair).** For every \(c,e,d,s>0\) the first-detection time \(T_s\) is almost surely finite, with Laplace transform
\[
\mathbb E[e^{-uT_s}]=\frac{sd(c+qu)}{u^2+(c+e+sd)u+csd},\qquad u\ge0.
\]

1. When \(q=0\), even the entire exact first-detection law at one effort identifies only \(S=c+e+sd\) and \(P=csd\). Its **complete positive parameter equivalence class** is
\[
\lambda_-<c<\lambda_+,\qquad d=\frac{P}{sc},\qquad e=S-c-\frac Pc,
\]
where \(\lambda_{\pm}=(S\pm\sqrt{S^2-4P})/2\). The sharp extinction-rate range is \(0<e\le S-2\sqrt P\), and the entire indicated open colonization-rate interval is attainable.
2. For every fixed known \(0<q\le1\), a single exact first-detection law uniquely determines all three rates, **except** at the unique parameter-dependent exceptional initial fraction
\[
q_*=\frac{S-\sqrt{S^2-4P}}{2sd}\in(0,1),\qquad S=c+e+sd,\quad P=csd.
\]
At precisely \(q=q_*\), the law is exponential with rate \(qsd\), and continuum-many distinct positive triples produce that same law at the fixed \(s,q\). At all other known positive \(q\), the first three right derivatives of the density (orders zero, one, two) explicitly recover all rates.
3. For **any** known \(q\in[0,1]\), observing the first-detection law under **two distinct known multipliers** \(s_1\ne s_2\) uniquely identifies \(c,e,d\). At \(q=0\) only three population summaries are needed: the two means \(m_1,m_2\) and the first variance \(v_1\). Writing
\[
U=\frac{s_2m_2-s_1m_1}{s_2-s_1},\quad
V=\frac{s_1s_2(m_1-m_2)}{s_2-s_1},\quad
K=\frac{2}{s_1(m_1^2-v_1)},
\]
the exact inverse is \(c=1/U\), \(d=UK\), \(e=VK-1/U\). Data are realizable by positive rates exactly when \(U>0\), \(K>0\), and \(VK>1/U\), alongside the stated positive means/variance and distinct positive efforts.

Thus one detector setting can have a full-law structural nonidentifiability even with noiseless infinite-population data, while a calibrated perturbation of sensitivity resolves it without recording recurrent detections.

## Assumptions and scope

The hidden availability process has states \(0,1\), with transitions \(0\to1\) at rate \(c\), \(1\to0\) at rate \(e\), and no false detections. Conditional on state \(1\), detections have exponential hazard \(sd\); state \(0\) has zero detection hazard. All rates and effort multipliers are strictly positive and constant during each deployment. The initial active fraction \(q\) is independently known, the same across compared effort groups, and each replicate starts fresh. Rate recovery is **structural identifiability from exact population laws**, not finite-sample estimation. Effort affects only detection, not animal availability dynamics.

At a fixed effort let \(h=sd\) and the killed two-state subgenerator be
\[
Q=\begin{pmatrix}-c&c\\ e&-(e+h)\end{pmatrix}.
\]
All comparisons use the first-detection distribution, not later arrival times or the original full point process.

## Proof

**1. Transform.** For Laplace variable \(u\ge0\), the absorbing intensity column is \((0,h)^{\mathsf T}\), so the phase-type resolvent gives
\[
(1-q,q)(uI-Q)^{-1}(0,h)^{\mathsf T}
=\frac{h(c+qu)}{(u+c)(u+e+h)-ce}.
\]
This is the asserted transform. At \(u=0\) it equals one. The eigenvalue polynomial has positive roots \(\lambda_-<\lambda_+\), since
\[
S^2-4P=(c-h)^2+e^2+2e(c+h)>0.
\]
Also \(\lambda_-<\min(c,h)\le\max(c,h)<\lambda_+\) follows by evaluating the polynomial at \(c,h\). Hence almost-sure detection and strict positivity of the ensuing bounds.

**2. The fully unobserved initial state.** At \(q=0\), the transform is \(P/(u^2+Su+P)\). Its reduced monic denominator uniquely reveals \(S,P\), and no additional parameter is present in the full law. Holding these two invariants fixed forces \(h=P/c\) and \(e=S-c-P/c\). The latter is strictly positive exactly when \(c\) lies between the roots of \(c^2-Sc+P\). The arithmetic-geometric-mean inequality gives the sharp maximum \(e=S-2\sqrt P\) at \(c=\sqrt P\); the lower endpoint zero is approached but not attained at positive rates. This proves the exact equivalence class, including the endpoints.

**3. Exceptional initialization.** For \(0<q\le1\), the transform numerator has a zero at \(u=-c/q\). A pole cancels precisely when
\[
c-q(c+e+h)+hq^2=0.
\]
The left side is positive at \(q=0\), negative at \(q=1\) (it equals \(-e\)), and a strictly convex quadratic with exactly one root in \((0,1)\). Factoring the root polynomial shows that this root is \(q_*=\lambda_-/h\); the other root \(\lambda_+/h\) exceeds one. At \(q_*\), the transform simplifies to \(\lambda_-/(u+\lambda_-)\), or an exponential law of rate \(q_*h\). If \(q\in(0,1)\) and \(r>0\) is the observed exponential rate, every choice \(c>r\) combined with
\[
h=r/q,\quad e=(1-q)(c-r)/q,\quad d=h/s
\]
reproduces exactly the same law; this is a positive one-parameter ambiguity. At \(q=1\) no such root exists.

Outside the cancellation set the reduced rational function has a quadratic monic denominator, which uniquely fixes \(S,P\); the nonzero coefficient of \(u\) in the numerator then reveals \(qh\) and hence \(h,c,e\). More strongly, let \(f\) be the right-hand density and \(f_j=f^{(j)}(0+)\) for \(j=0,1,2\). With \(X=f_1/h\), \(Y=f_2/h\), direct differentiation of the killed Kolmogorov equations gives
\[
f_0=qh,\quad X=c-qS,\quad Y=-SX-qch.
\]
At nonexceptional \(q>0\), the quantity \(X+q^2h=c-qS+q^2h\) is nonzero, and therefore
\[
h=f_0/q,\qquad S=-\frac{Y+qhX}{X+q^2h},\qquad
c=X+qS,\qquad d=h/s,\qquad e=S-c-h.
\]
This is an explicit three-jet inverse; at the exceptional initial fraction the denominator vanishes exactly.

**4. Two known efforts eliminate all exceptions.** For \(q\in(0,1)\), the cancellation polynomial at effort \(s\) is \(c-q(c+e+sd)+sdq^2\). At two distinct efforts, their difference is \(d(s_2-s_1)q(q-1)\ne0\). Thus at least one law is nonexceptional and identifies the rates using step 3; for \(q=1\), either law already does so.

For \(q=0\), differentiating \(P/(u^2+Su+P)\) at zero yields
\[
m_s=\frac{c+e+sd}{csd}=\frac1c+\frac{c+e}{scd},\qquad
\operatorname{Var}(T_s)=m_s^2-\frac{2}{scd}.
\]
Hence \(m_s=U+V/s\) with \(U=1/c\), \(V=(c+e)/(cd)\). Two distinct means determine \(U,V\), and the variance at \(s_1\) determines \(K=cd\). Substitution proves the inverse formulas and the strict positivity criterion in the Finding. Conversely, given those inequalities, the constructed positive rates reproduce the three summaries exactly. This completes all cases.

**5. Exact examples.** At \(q=0,s_1=1\), \((c,e,d)=(1,3,2)\) and \((1/2,3/2,4)\) have identical entire laws, namely transform \(2/(u^2+6u+2)\). Their means at effort \(s_2=2\) are respectively \(2\) and \(5/2\). At \(q=1/2,s=1\), the distinct triples \((3,1,4)\) and \((5,3,4)\) both yield exactly an \(\mathrm{Exp}(2)\) first-detection time, demonstrating the positive-initialization exceptional case.

## Verification

The standalone `checker.py` evaluates the exact rational counterexamples, both inverse formulas, the phase-type Laplace transform against a separately formed matrix resolvent, the cancellation identity, and the Markov matrix exponential's survival probability. Deterministic randomized positive-parameter tests cover off-exception reconstruction. Reproduce using `python checker.py` with NumPy and SciPy installed. Passing numerical examples confirm algebraic implementation but **do not replace** the universal proof above.

## Relationship to prior work

Pautrel et al. (2024) explicitly study interrupted Poisson and two-state Markov-modulated sensor detection and distinguish continuous detection-time modelling from discretized occupancy data. They explicitly omit first-detection-only models; their displayed first-detection probability is a general matrix exponential, not the parameter recovery or exceptional-initialization classification established here. Priyadarshani et al. (2024), Halstead et al. (2021), and Haines et al. (2023) motivate time-to-detection ecological inference under different replicated-visit, abundance or closure frameworks. Classical two-state phase-type theory and the general nonidentifiability of Markovian arrival representations (Ramírez-Cobo, Lillo & Wiper, 2010) supply important background; neither the general phase-type absorption law nor the general fact that quasi-stationarity yields exponential survival is claimed as new. The present contribution is the exact **initialization-dependent identification frontier, its exceptional exponential ambiguity and a calibrated two-effort restoration from minimal accessible summaries** for this ecological observation model. No claim of global priority beyond inspected evidence is made.

## Limitations

This is an intentionally minimal two-state Markov model; real animal availability may have memory, spatial dependence, false triggers and effort-induced behavior changes. The known-initial-mixture assumption is demanding. Near the exceptional initial fraction, the inverse is ill-conditioned even where structurally unique; finite-sample performance and optimal allocation between efforts are not proved. The two-effort inversion at \(q=0\) uses population means and a population variance, not finite observations or censored outcomes. The results concern identifiability within the stipulated model, not practical certainty that field species parameters can be recovered.

## References

- Pautrel, L., Moulherat, S., Gimenez, O. & Etienne, M.-P. (2024), *Analysing biodiversity observation data collected in continuous time: Should we use discrete- or continuous-time occupancy models?*, *Methods in Ecology and Evolution* 15, 935–950. First public version 2024-03-19. https://doi.org/10.1111/2041-210X.14314
- Priyadarshani, D., Huynh, H.-D., Altwegg, R. & Hwang, W.-H. (2024), *A unified framework for time-to-detection occupancy and abundance models*, *Methods in Ecology and Evolution* 15, 555–568. https://doi.org/10.1111/2041-210X.14296
- Halstead, B. J., Rose, J. P. & Kleeman, P. M. (2021), *Time-to-detection occupancy methods: performance and utility for improving efficiency of surveys*, *Ecological Applications* 31, e02267. https://doi.org/10.1002/eap.2267
- Ramírez-Cobo, P., Lillo, R. E. & Wiper, M. P. (2010), *Nonidentifiability of the two-state Markovian arrival process*, *Journal of Applied Probability* 47, 630–649. https://doi.org/10.1239/jap/1285335400
- Haines, L. M., Altwegg, R. & Borchers, D. L. (2023), *Exact likelihoods for N-mixture models with time-to-detection data*, *Australian & New Zealand Journal of Statistics* 65, 327–343. https://arxiv.org/abs/2309.14777
