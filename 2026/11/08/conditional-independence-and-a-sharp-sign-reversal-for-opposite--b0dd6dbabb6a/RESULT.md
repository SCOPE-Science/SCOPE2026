# Conditional independence and a sharp sign reversal for opposite-side run-and-tumble first-visit polarities

## Finding

A one-dimensional active particle that paints each newly visited point with its instantaneous propulsion polarity has a special two-point law. Although its first visits to the two sides of its starting location occur along one coupled trajectory, the two painted signs are **independent when the initial polarity is fixed**. Mixing initial polarities produces an exact positive covariance, while the *uncentered* two-point sign product changes sign once as the two observation points are moved apart.

Write the right and left first-visit polarities as \(C_+=S_{\tau_+}\) and \(C_-=S_{\tau_-}\). For \(H=\sqrt{v^2+D\alpha}\), \(q=H/D\), \(m=v/H\), initial position \(x\in(-b,a)\), and fixed initial polarity \(s\in\{-1,+1\}\),

\[
\begin{aligned}
\mathbb E[C_+\mid x,s]&=m+(s-m)e^{-q(a-x)},\\
\mathbb E[C_-\mid x,s]&=-m+(s+m)e^{-q(x+b)},\\
\mathbb E[C_+C_-\mid x,s]&=\mathbb E[C_+\mid x,s]\mathbb E[C_-\mid x,s].
\end{aligned}
\]

Thus the binary variables \(C_+,C_-\) are conditionally independent. If the initial polarity is random, independent of Brownian motion, of mean \(\mu\), then

\[
\operatorname{Cov}(C_+,C_-\mid X_0=x)=(1-\mu^2)e^{-q(a+b)}.
\]

For unbiased initialization and symmetric targets \(a=b=\ell\),

\[
\mathbb E[C_+C_-]=z^2-m^2(1-z)^2,\qquad z=e^{-q\ell},
\]

which vanishes at exactly one positive distance,

\[
\ell_*=\frac{D}{\sqrt{v^2+D\alpha}}\log\!\left(1+\frac{\sqrt{v^2+D\alpha}}{v}\right).
\]

The uncentered product is positive for \(0<\ell<\ell_*\) and negative for \(\ell>\ell_*\), even though the covariance remains strictly positive.

## Assumptions and scope

Let \(v,D,\alpha>0\). On the full real line, \(X_t\) obeys \(dX_t=vS_tdt+\sqrt{2D}\,dW_t\) with an independent standard Brownian motion and a symmetric, autonomous continuous-time polarity chain \(S_t\in\{-1,+1\}\) whose transition rate in each direction is \(\alpha/2\). The generator acting on vector functions \(f_s(x)\) is

\[
(Lf)_s=Df_s''+svf_s'+\frac{\alpha}{2}(f_{-s}-f_s).
\]

Fix \(a,b>0\), \(-b<x<a\), initial polarity \(S_0=s\), and stopping times \(\tau_+=\inf\{t\ge0:X_t=a\}\), \(\tau_-=\inf\{t\ge0:X_t=-b\}\). Both are almost surely finite: at successive completed \(+\)-then-\(-\) polarity cycles, the position increments form a non-degenerate iid centered random walk with finite variance, which oscillates to both signs without bound; path continuity forces visits to both levels. The statements apply to **eventual first visits**, possibly at different times. No reset or confinement is imposed. When the initial polarity is mixed, its law is independent of the driving noises.

## Proof

**1. One-level polarity means.** Put \(H=\sqrt{v^2+D\alpha}\), \(q=H/D\), and \(m=v/H\in(0,1)\). Define for \(x<a\) and \(x>-b\), respectively,

\[
U_s(x)=m+(s-m)e^{-q(a-x)},\qquad
V_s(x)=-m+(s+m)e^{-q(x+b)}.
\]

Direct differentiation proves \(LU=LV=0\). The boundary data are \(U_s(a)=s\), \(V_s(-b)=s\); both are bounded. Stopping at a level and then sending the finite-time cutoff to infinity gives

\[
U_s(x)=\mathbb E_{x,s}[S_{\tau_+}],\qquad
V_s(x)=\mathbb E_{x,s}[S_{\tau_-}].
\]

Indeed \(L\)-harmonicity makes the bounded stopped functions martingales; the hitting times are almost surely finite.

**2. Product-harmonic cancellation.** Set \(F_s=U_sV_s\). The generator product identity includes a continuous cross variation and a jump cross variation:

\[
(LF)_s=U_s(LV)_s+V_s(LU)_s+2D U_s'V_s'
+\frac{\alpha}{2}(U_{-s}-U_s)(V_{-s}-V_s).
\]

Writing \(Z=e^{-q(a+b)}\), the continuous cross term is \(-2Dq^2(1-m^2)Z\) and the polarity-switch cross term is \(+2\alpha Z\). They cancel *exactly* because \(Dq^2(1-m^2)=\alpha\); therefore \(LF=0\).

**3. Two-level joint expectation.** Let \(\tau=\min(\tau_+,\tau_-)\), the finite first exit from \((-b,a)\). At upper exit, the first mark is \(S_\tau\), and the conditional mean of the *later* lower mark is \(V_{S_\tau}(a)\), by the strong Markov property. At lower exit the analogous later upper mean is \(U_{S_\tau}(-b)\). Consequently, the conditional product expectation given the stopped state equals \(S_\tau V_{S_\tau}(a)\) at upper exit and \(S_\tau U_{S_\tau}(-b)\) at lower exit. These are exactly \(F_{S_\tau}(X_\tau)\) because \(U_s(a)=V_s(-b)=s\). Bounded optional stopping for the \(L\)-harmonic \(F\) yields

\[
\mathbb E_{x,s}[C_+C_-]=\mathbb E_{x,s}[F_{S_\tau}(X_\tau)]=F_s(x)=U_s(x)V_s(x).
\]

The two marks take only the values \(\pm1\). For two binary random variables, their two means and product moment uniquely determine the joint table \(\mathbb P(C_+=i,C_-=j)=[1+i\mathbb EC_++j\mathbb EC_-+ij\mathbb E(C_+C_-)]/4\); the product equality therefore proves conditional independence, not merely absence of linear correlation.

**4. Initial mixing and exact crossover.** With \(\mu=\mathbb ES_0\), write \(z_+=e^{-q(a-x)}\), \(z_-=e^{-q(x+b)}\). The conditional means are affine in \(s\): \(U_s=m(1-z_+)+sz_+\), \(V_s=-m(1-z_-)+sz_-\). The law of total covariance and conditional independence give

\[
\operatorname{Cov}(C_+,C_-)=(1-\mu^2)z_+z_-=(1-\mu^2)e^{-q(a+b)}.
\]

At \(x=0\), \(a=b=\ell\), \(\mu=0\), the raw product equals \(z^2-m^2(1-z)^2=[(1+m)z-m][(1-m)z+m]\). The second factor is strictly positive for \(0<m<1\), \(z\in(0,1)\), and the first is strictly increasing in \(z\) with exactly one root \(z=m/(1+m)\). Since \(z=e^{-q\ell}\) decreases strictly from one to zero, this yields the stated unique \(\ell_*\) and signs.

## Verification

The standalone `verify.py` is part of the package. It checks, using exact symbolic algebra, the three harmonic equations \(LU=LV=L(UV)=0\), boundary values, mixture covariance and sign-polynomial factorization. As an independent numerical method, it solves the coupled two-state backward boundary-value problem for the sequential first-visit product on an asymmetric interval, for 16 positive parameter triples, three initial positions and both initial polarities; it does not assume the interior product solution. It also tests the exact sign threshold. All **161** component checks passed. These finite checks support reproducibility but do not replace the analytic proof.

## Relationship to prior work

Sezik, Britton, Touma and Pruessner (arXiv:2603.24277, first posted March 25, 2026) introduced the same polarity-painting interpretation and computed single-site state-dependent visit probabilities and explored-volume statistics. Their Sections II, IV, V and appendices do not provide the joint signed first-visit law for opposite sites. The **model and one-site visit formalism are prior results**; the claim here concerns two sites on the same sample path.

Sezik, Knight, Alston and collaborators (arXiv:2508.07386, August 10, 2025), especially Section 4.1, solved the joint distribution of *which boundary is first exited* and *the polarity on that first exit*. That is a different random pair from the eventual polarity marks at **both** boundary levels; neither its two-boundary first-exit formulas nor their marginals state the conditional product cancellation. General Markov-additive first-passage ladder methods of D'Auria, Ivanovs, Kella and Mandjes (arXiv:1006.2965, June 15, 2010) provide one-sided first-passage phase transition matrices and broadly applicable machinery, but do not in the inspected material identify this two-sided fixed-initial-polarity independence or the signed-moment crossover.

## Limitations

The independence is special to the symmetric binary switching model with constant opposing propulsion velocities and positive translational diffusivity. It is conditional on **both** initial position and polarity; unconditionally it usually fails. The zero of the *raw* two-site moment is not a zero of covariance, which stays positive for a non-degenerate initial polarity mixture. The result does not assert time-resolved independence, same-side independence, robustness to unequal switching rates, or optimality for experiments. The original model is established in the literature; priority for the exact special two-point identity should be assessed against additional Markov-modulated-Brownian first-passage literature, particularly one inaccessible relevant 2026 chapter on first-passage phase processes.

## References

1. E. Sezik, C. Britton, A. Touma and G. Pruessner, *Run, Tumble and Paint*, arXiv:2603.24277, first posted March 25, 2026. https://arxiv.org/abs/2603.24277
2. E. Sezik, J. Knight, H. Alston et al., *Conditional splitting probabilities for hidden-state inference in drift-diffusive processes*, arXiv:2508.07386, first posted August 10, 2025, especially Sections 2 and 4.1. https://arxiv.org/abs/2508.07386
3. B. D'Auria, J. Ivanovs, O. Kella and M. Mandjes, *First passage process of a Markov additive process, with applications to reflection problems*, arXiv:1006.2965, posted June 15, 2010, especially Sections 1.2 and 6. https://arxiv.org/abs/1006.2965
4. G. Latouche, *First Passage Across a Level*, 2026 book chapter, DOI:10.1007/978-3-031-98576-8_2 (abstract accessible; full text not inspected). https://doi.org/10.1007/978-3-031-98576-8_2
