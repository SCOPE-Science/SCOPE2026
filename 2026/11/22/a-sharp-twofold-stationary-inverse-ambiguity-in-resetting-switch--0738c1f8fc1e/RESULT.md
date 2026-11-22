# A sharp twofold stationary inverse ambiguity in resetting switching diffusion

## Finding

For a one-dimensional particle alternating between two **known, distinct** Brownian diffusivities, with unknown positive switching and full-renewal resetting rates, the full stationary position distribution determines the three unknown rates up to **at most two** possibilities. A sharp explicit condition decides whether there are one or two admissible models. All stationary position moments, including those of arbitrarily high order, agree for the two models, but a single positive-lag position covariance distinguishes them.

Write the known diffusivities as \(0<D_0<D_1\), the internal switching rates as \(\alpha\) from state \(0\) to \(1\), and \(\beta\) in the reverse direction. Let \(r>0\) be the rate of independent Poisson renewal, under which position is set to zero and the internal state is freshly sampled from its equilibrium distribution. Set
\[
 s=\alpha+\beta,\qquad \theta=\frac{\alpha}{s},\qquad
 \Sigma=D_0+D_1,\qquad \Delta=D_1-D_0,
 \qquad m=D_0+\theta\Delta,\qquad n=\Sigma-m.
\]
The distinct competing model, when admissible, is given exactly by
\[
 r^{\sharp}=\frac{rn}{m},\quad
 s^{\sharp}=\frac{m(r+s)}{n}-\frac{rn}{m},\quad
 \theta^{\sharp}=1-\theta,\quad
 \alpha^{\sharp}=s^{\sharp}(1-\theta),\quad
 \beta^{\sharp}=s^{\sharp}\theta.
\]
The partner exists with all rates **strictly positive** precisely when
\[
 \frac{s}{r}>\frac{\Sigma\Delta(1-2\theta)}{m^2}.
\]
If this condition holds and \(\theta\ne1/2\), there are exactly two distinct physically feasible triples. Otherwise the observed stationary position law identifies the sole feasible triple. In particular, every \(\theta>1/2\) admits a distinct partner, whereas a sufficiently slow switching chain with \(\theta<1/2\) does not.

Even moments through sixth order suffice to find the one or two triples; moments through fourth order generically leave a continuous family of possibilities. If one additionally measures any stationary position covariance at a known positive lag \(t\), it identifies the reset rate uniquely, and second plus fourth stationary moments then identify the remaining two rates.

For example, at \(D_0=1,D_1=3\), the two distinct triples \((r,\alpha,\beta)=(1,3/2,1/2)\) and \((3/5,11/10,33/10)\) both have the exact stationary characteristic function
\[
 \phi(k)=\frac{1+k^2/2}{1+3k^2+k^4}.
\]
They therefore agree on **the entire** positional stationary law, not just its first few moments, but have respectively \(\operatorname{Cov}(X_0,X_t)=5e^{-t}\) and \(5e^{-3t/5}\) for \(t\ge0\).

## Assumptions and scope

The model is defined for any fixed \(0<D_0<D_1<\infty\) and arbitrary strictly positive real \(r,\alpha,\beta\). The hidden continuous-time Markov chain \(I_t\in\{0,1\}\) jumps from \(0\) to \(1\) at rate \(\alpha\), and from \(1\) to \(0\) at rate \(\beta\). Between resets,
\[
 dX_t=\sqrt{2D_{I_t}}\,dW_t.
\]
Reset times are an independent Poisson process of rate \(r\). At each reset, set \(X=0\) and independently redraw \(I\) from the chain's invariant distribution \(\pi=(1-\theta,\theta)\). The Brownian increments after resetting are fresh. The observable is the stationary marginal distribution of \(X\), possibly supplemented by the stationary covariance at one known positive lag. Parameters \(D_0,D_1\) and the physical time unit must be calibrated; no entropy-production or experimental finite-sample claims are made.

Every reset regenerates the complete pair \((X,I)\), so a unique stationary law exists, with exponentially decaying spatial tails and finite moments of every order. The theorem assumes no observation of the hidden internal state.

## Proof

**1. Stationary transform.** The two-state generator, in row convention, is
\[
 Q=\begin{pmatrix}-\alpha&\alpha\\\beta&-\beta\end{pmatrix}.
\]
Renewal at exponential age \(T\sim\mathrm{Exp}(r)\) gives the stationary characteristic function
\[
 \phi(k)=r\,\pi^\top\bigl(rI-Q+k^2\operatorname{diag}(D_0,D_1)\bigr)^{-1}\mathbf{1}.
\]
Direct inversion of this \(2\times2\) resolvent yields
\[
 \phi(k)=\frac{1+A k^2}{1+B k^2+C k^4},\qquad
 A=\frac{n}{r+s},\qquad
 B=\frac{r\Sigma+sm}{r(r+s)},\qquad
 C=\frac{D_0D_1}{r(r+s)}.
\]
The forward steady-state distribution and its two-exponential spatial representation are established in the reset-switching literature [1]; the new conclusions below concern its inverse fibers, feasibility boundary, and minimal observations.

**2. Exact extraction from sixth-order moments.** Define \(u_j=\mathbb E[X^{2j}]/(2j)!\) for \(j=1,2,3\). Expanding \(\phi(k)\) at zero gives
\[
 u_1=B-A=\frac{m}{r},\qquad
 u_2=Bu_1-C,\qquad
 u_3=Bu_2-Cu_1.
\]
Moreover,
\[
 u_2-u_1^2=\frac{(m-D_0)(D_1-m)}{r(r+s)}
 =\frac{\theta(1-\theta)\Delta^2}{r(r+s)}>0.
\]
Thus the observed moments uniquely reconstruct the rational characteristic function coefficients, without any cancellation ambiguity:
\[
 B=\frac{u_3-u_1u_2}{u_2-u_1^2},\qquad
 C=Bu_1-u_2,\qquad A=B-u_1.
\]
Set \(H=D_0D_1/C=r(r+s)\). Any possible positive reset rate \(R\) satisfies \(m_R=u_1R\) and, since \(AH=rn=R(\Sigma-m_R)\), the quadratic
\[
 u_1R^2-\Sigma R+AH=0.
\]
The discriminant of this equation, evaluated at the given true model, is \((m-n)^2=\Delta^2(2\theta-1)^2\). Its roots are exactly \(R=r\) and \(R=rn/m\), coincident only for \(\theta=1/2\). Every candidate root must obey
\[
 R>0,\qquad D_0<u_1R<D_1,\qquad S_R:=H/R-R>0.
\]
Conversely, each root meeting these three inequalities defines the unique admissible triple
\[
 \theta_R=\frac{u_1R-D_0}{\Delta},\quad
 \alpha_R=S_R\theta_R,\quad
 \beta_R=S_R(1-\theta_R),
\]
which reproduces all three coefficients \(A,B,C\) and hence the entire stationary law. This proves completeness of the one-or-two classification.

**3. Partner existence and sharpness.** For the other root \(r^\sharp=rn/m\), the implied mean diffusivity is \(m^\sharp=n\in(D_0,D_1)\), so \(\theta^\sharp=1-\theta\) and the mean-diffusivity restriction is automatically satisfied. Its total switching rate is
\[
 s^\sharp=\frac{m(r+s)}n-\frac{rn}{m}.
\]
Multiplying by the strictly positive \(mn\) gives
\[
 mn\,s^\sharp=m^2s+r(m^2-n^2)
 =m^2s+r\Sigma\Delta(2\theta-1).
\]
Hence \(s^\sharp>0\) if and only if the claimed sharp inequality holds. Equality forces the competing switching rate to zero and excludes that boundary from the strictly positive model class. Replacing primed with unprimed data yields the same involution, and no third root exists.

**4. Why fourth-order observations do not suffice.** At a given valid model, hold \(u_1\) and \(K=u_2-u_1^2>0\) fixed. For every \(\vartheta\) in a sufficiently small open interval about \(\theta\), define
\[
 m(\vartheta)=D_0+\vartheta\Delta,\quad
 r(\vartheta)=\frac{m(\vartheta)}{u_1},\quad
 s(\vartheta)=\frac{\vartheta(1-\vartheta)\Delta^2}{r(\vartheta)K}-r(\vartheta).
\]
By continuity, \(s(\vartheta)>0\) in a neighborhood of the original point. The physical rates \(\alpha(\vartheta)=s(\vartheta)\vartheta\) and \(\beta(\vartheta)=s(\vartheta)(1-\vartheta)\) then define infinitely many distinct valid triples with identical second and fourth positional moments. Thus sixth order is the first generic even-moment cutoff for a finite inverse fiber; the sixth-order theorem above bounds that fiber sharply by two.

**5. Breaking the alias with one time lag.** After a complete renewal the process is independent of its previous state and has mean zero. Without a renewal, the displacement increment over any time interval has conditional mean zero even when the diffusion state changes. Therefore, by conditioning on whether a reset falls within \((0,t]\),
\[
 \mathbb E[X_0X_t]=\mathbb E[X_0^2]e^{-rt}=2u_1e^{-rt}\qquad(t\ge0).
\]
For any known \(t>0\) the observed covariance uniquely yields
\[
 r=-t^{-1}\log\frac{\operatorname{Cov}(X_0,X_t)}{2u_1}.
\]
Knowing \(r\) and \(u_1\) gives \(m=ru_1\) and \(\theta=(m-D_0)/\Delta\). Knowing \(K=u_2-u_1^2\) then gives
\[
 s=\frac{\theta(1-\theta)\Delta^2}{rK}-r,
\]
followed by the unique \(\alpha=s\theta\), \(\beta=s(1-\theta)\). This is stronger than merely selecting between the two sixth-moment branches.

## Verification

The standalone standard-library program `verify.py` solves the stationary **phase-resolved** polynomial moment equations independently of the characteristic-function expansion, then checks exact-rational second, fourth, and sixth moments, algebraic coefficient recovery, both admissible inverse branches, degenerate equal-occupancy cases, and equality of the rational characteristic functions of valid partners. It includes the explicit unequal-reset-rate example above.

Execute `python3 verify.py` alongside this document. The recorded execution passed 906 exact-rational assertions across 81 independently selected positive parameter tuples, with 27 single-branch and 54 two-branch cases. These finite tests are supplemental: claims for arbitrary positive real parameters follow from the exact resolvent and algebraic proof, not extrapolation from samples.

## Relationship to prior work

Bressloff [1] analyzes exactly the forward two-state diffusivity-switching process with Poisson resetting of both position and hidden state, and explicitly obtains the stationary position density as a sum of two exponentials. That **known forward result is not claimed as new**. The present question is instead the global inverse map from a stationary *position-only* distribution to three unknown rates at calibrated diffusivities, including its twofold duality, sharp physical boundary, moment cutoff, and temporal resolution. The accessible abstract and opening material of [1] explicitly cover the forward NESS and first-passage optimization but do not establish what the inaccessible remainder might imply about inverse identifiability. Its full main text could not be inspected, leaving a genuine priority risk.

Bressloff [2] develops truncated hybrid processes, survival statistics, and switching dynamics rather than this static inverse-rate ambiguity; the available full-text introduction, sections on switching/truncation, and discussion were compared. Nearby published mathematical results on inverse fluctuations for nonreset switching diffusivity, harmonic trapping, and covariance camouflage concern different observations or generators and have not been shown to imply the precise duality and positivity condition here. Non-identification in a literature search is not a proof of historical novelty.

## Limitations

The twofold inverse theorem requires distinct calibrated diffusivities, positive internal switching rates, complete joint renewal (including a fresh equilibrium hidden-state draw), independent Brownian driving, and one-dimensional free diffusion. It does not apply to position-only resets that preserve the hidden state, unknown diffusion coefficients, state-dependent resets, arbitrary resetting laws, or imperfect experimental observation. A single time-lag covariance resolves the ambiguity only when its lag and stationary variance are known exactly in the mathematical model. Finite-sample conditioning and experimental precision are not analyzed. A plausible same-model original article [1] was only partially accessible, so a full-text priority comparison remains unresolved. Independent validation has not been performed.

## References

[1] P. C. Bressloff, "Switching diffusions and stochastic resetting," *Journal of Physics A: Mathematical and Theoretical* **53**, 275003 (2020), published 17 June 2020, https://doi.org/10.1088/1751-8121/ab97e0.

[2] P. C. Bressloff, "Truncated stochastically switching processes," *Physical Review E* **109**, 024103 (2024), published 7 February 2024, https://doi.org/10.1103/PhysRevE.109.024103.
