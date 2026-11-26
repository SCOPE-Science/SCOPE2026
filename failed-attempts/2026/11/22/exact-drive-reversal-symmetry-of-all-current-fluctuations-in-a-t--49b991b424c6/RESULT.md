# Exact drive-reversal symmetry of all current fluctuations in a three-site disordered exclusion ring

## Finding

For a three-site periodic exclusion process with exactly two particles and arbitrary positive site-dependent departure rates \(a,b,c\), let a particle at site \(i\) hop clockwise at rate \((1+\varepsilon)w_i/2\) and counterclockwise at rate \((1-\varepsilon)w_i/2\) when the destination is vacant, with \(-1<\varepsilon<1\). Let \(Q_t\) count clockwise particle hops minus counterclockwise hops by time \(t\). Its stationary long-time scaled cumulant-generating function exists and obeys the exact identity

\[
\psi_\varepsilon(s)=\lim_{t\to\infty}t^{-1}\log\mathbb E_\varepsilon e^{sQ_t}
=\psi_{-\varepsilon}(-s),\qquad s\in\mathbb R.
\]

Thus every stationary long-time current cumulant obeys \(\kappa_n(\varepsilon)=(-1)^n\kappa_n(-\varepsilon)\), for every positive integer \(n\). This parity persists for fully non-reflection-symmetric disorder. For example, the distinct site rates \((a,b,c)=(1,2,4)\) give a total signed-current mean rate \(24\varepsilon(\varepsilon^2+3)/[7(\varepsilon^2+7)]\), while the one-particle total mean current is \(12\varepsilon/7\); hence bias-reversal symmetry of all two-particle current fluctuations does not require particle–hole current-density symmetry.

## Assumptions and scope

The ring has labeled sites \(1,2,3\) and exactly two indistinguishable hard-core particles; the one vacancy performs a three-state irreducible continuous-time Markov chain. Departure rates \(a,b,c\) are strictly positive. The bias satisfies \(-1<\varepsilon<1\). Each successful clockwise particle hop contributes \(+1\) to \(Q_t\), and each counterclockwise hop contributes \(-1\). A stationary initial law is used, although the long-time scaled cumulants are independent of initial configuration. The claim concerns *long-time* cumulants and current large deviations, not equality of the complete finite-time current distributions.

## Proof

Set \(u=e^s\) and let \(L_\varepsilon(u)\) be the three-by-three tilted generator on the vacancy states. For each allowed particle hop, multiply the off-diagonal transition rate by \(u\) for a clockwise hop or \(u^{-1}\) for a counterclockwise hop; leave its diagonal entry at minus the untilted escape rate. Writing \(S_1=a+b+c\), \(S_2=a^2+b^2+c^2\), and \(S_{11}=ab+bc+ca\), direct three-state determinant expansion yields

\[
\begin{aligned}
\det(zI-L_\varepsilon(u))={}&z^3+S_1z^2
+\frac{(1-\varepsilon^2)S_2+2(1+\varepsilon^2)S_{11}}4z\\
&-\frac{abc}{8}\left[(1+\varepsilon)^3(u^3-1)
+(1-\varepsilon)^3(u^{-3}-1)\right].
\end{aligned}
\]

Indeed the trace and the sum of principal two-by-two minors depend only on the symmetric combinations displayed, and every nontrivial directed three-cycle traverses each departure site once. The two oriented three-cycle products are \(abc(1\pm\varepsilon)^3/8\), weighted by \(u^{\pm3}\). The remaining determinant terms cancel those cycle products at \(u=1\), because the untilted generator has eigenvalue zero. This establishes the full polynomial, not merely an expansion in bias.

Under \((\varepsilon,u)\mapsto(-\varepsilon,u^{-1})\) the two cycle contributions exchange places while the other coefficients are unchanged. Consequently the entire characteristic polynomial is invariant. For real \(s\), \(L_\varepsilon(e^s)\) is an irreducible Metzler matrix. Its simple dominant real eigenvalue is the scaled cumulant-generating function by finite-state Feynman–Kac/Perron–Frobenius theory. The characteristic-polynomial identity therefore identifies the dominant eigenvalues, proving \(\psi_\varepsilon(s)=\psi_{-\varepsilon}(-s)\). Differentiating at zero proves cumulant parity at all orders. The Legendre–Fenchel transform also yields \(I_\varepsilon(j)=I_{-\varepsilon}(-j)\) for the long-time current rate function.

For the explicit contrast, differentiating the principal eigenvalue for \((1,2,4)\) at \(s=0\) gives the stated total-current formula. In the one-particle process, the stationary site probabilities are proportional to \(1/w_i\), so the total mean current is \(3\varepsilon/(1/a+1/b+1/c)=12\varepsilon/7\). The two mean currents differ for generic bias, while each has reversal parity.

## Verification

The accompanying \(verify.py\) constructs the three-state tilted generator from the exclusion rule with independent symbolic positive site rates, checks the characteristic polynomial identically, and checks exact invariance under simultaneous bias and counting-field reversal. It also verifies the explicit mean-current example. The exact identity for the symbolic indeterminates is the finite algebraic certificate; no finite sampling is used as an infinite proof.

## Relationship to prior work

Sakai and Akimoto analyze bond- and site-disordered asymmetric exclusion processes, establish and discuss current symmetry criteria, and report nonlinear bias-response effects [1]. Their examined main-text treatment concerns average current, not a full three-site tilted spectral identity or all orders of current fluctuations. The three-site mean-current reversal itself was identified in existing indexed mathematical results, so it is not claimed here as original. The new assertion is the all-cumulant and current-large-deviation parity under arbitrary positive site disorder in the two-particle three-site ring. Standard finite-state tilted-generator and Perron–Frobenius methods are used without claims of novelty for those methods.

## Limitations

The ring has three sites and two particles. Larger rings and arbitrary filling fractions are not covered. The identity compares asymptotic current statistics under reversed bias, not finite-time current distributions, nor entropy-production observables with differently weighted jumps. An unindexed, equivalent three-cycle spectral identity or its application to exclusion may already exist; this publication-priority risk requires independent investigation. No independent scientific audit has been performed.

## References

[1] I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316, first public version December 3, 2025, https://arxiv.org/abs/2512.03316.
