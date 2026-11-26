# Exact finite-time spectral variance of the KMP energy center

## Finding

For the infinite one-dimensional Kipnis–Marchioro–Presutti (KMP) heat-exchange chain with unit-rate Poisson clocks on nearest-neighbor bonds, the **complete, finite-time center-of-energy variance** after one-site energy release has an explicit positive spectral representation. If total energy is \(W>0\), let \(u_j(t)\) be the energy at lattice site \(j\), initially \(u_0(0)=W\) and \(u_j(0)=0\) otherwise. Define the normalized center
\[
X_t=\frac{1}{W}\sum_{j\in\mathbb Z}j u_j(t),\qquad V(t)=\operatorname{Var}(X_t).
\]
Then for all \(t\ge0\),
\[
\boxed{V(t)=\int_0^4\frac{1-e^{-\lambda t}}{\lambda}\,\rho(\lambda)\,d\lambda,\quad
\rho(\lambda)=\frac{(\lambda+2)\sqrt{4-\lambda}}{2\pi\sqrt\lambda\,(3\lambda^2-4\lambda+4)}.}
\]
The multiplier \((1-e^{-\lambda t})/\lambda\) extends continuously to \(t\) at \(\lambda=0\). For \(t>0\), its product with the density has an integrable inverse-square-root singularity there; the spectral integral is understood as an improper integral. The density is strictly positive on \((0,4)\); therefore \(V\) is strictly increasing and strictly concave on \((0,\infty)\). The microscopic short- and long-time laws are
\[
\boxed{V(t)=\frac23t-\frac5{18}t^2+O(t^3),\quad t\downarrow0,}
\]
\[
\boxed{V(t)=\sqrt{\frac t\pi}+\frac14-\frac{11}{16\sqrt{\pi t}}+O(t^{-3/2}),\quad t\to\infty.}
\]
The additive constant \(1/4\) and every finite-time value are exact lattice corrections beyond the long-time continuum variance previously determined by macroscopic fluctuation theory. If clocks on each bond have rate two rather than one, replace \(t\) by \(2t\); the leading amplitude becomes \(\sqrt{2t/\pi}\), matching the published continuum normalization.

## Assumptions and scope

The configuration is a nonnegative sequence with conserved sum \(W\). Each unordered nearest-neighbor bond \((j,j+1)\) has an independent rate-one Poisson clock. When its clock rings, draw a fresh uniform \(U\in(0,1)\) and replace its pre-event energies \((a,b)\) by \((U(a+b),(1-U)(a+b))\). Events at bonds with zero energy have no effect. Initially all energy is at site zero. At each finite time, the active energy support is almost surely finite: outward boundary events are dominated by two independent unit-rate Poisson counting processes. The same domination yields the moment bounds required for the generator identities and martingale quadratic-variation calculations. All statements are for arbitrary \(W>0\) after normalization by \(W\), and arbitrary real \(t\ge0\).

## Proof

**1. Center martingale and quadratic variation.** Across bond \((j,j+1)\), the center jump is \(\Delta X=(a-U(a+b))/W\), equivalently the change of the right-site energy divided by \(W\). Its conditional mean is \((a-b)/(2W)\). Summing the mean drift over all bonds telescopes to zero, so \(X_t\) is a centered square-integrable martingale. Uniform averaging gives
\[
\mathbb E[(\Delta X)^2\mid a,b]=\frac{a^2-ab+b^2}{3W^2}.
\]
Consequently, with \(F_k(t)=W^{-2}\sum_j\mathbb E[u_j(t)u_{j+k}(t)]\) for \(k\ge0\),
\[
V'(t)=\frac{2F_0(t)-F_1(t)}3. \tag{1}
\]
The initial values are \(F_0(0)=1\), \(F_k(0)=0\) for \(k\ge1\).

**2. Exact translation-summed pair equations.** A single bond redistribution has conditional expectation \(\mathbb E[U^2]=1/3\) and \(\mathbb E[U(1-U)]=1/6\). Applying the generator to each product and summing over translations yields the closed half-line system
\[
\begin{aligned}
F'_0&=-\tfrac23F_0+\tfrac43F_1,\\
F'_1&=\tfrac13F_0-\tfrac53F_1+F_2,\\
F'_k&=F_{k-1}-2F_k+F_{k+1},\qquad k\ge2.
\end{aligned} \tag{2}
\]
The identity \(F_0+2\sum_{k\ge1}F_k=1\) follows from energy conservation. In particular, all transforms below exist for \(s>0\).

**3. Resolvent.** Write \(\widehat F_k(s)=\int_0^\infty e^{-st}F_k(t)dt\). Set
\[
r(s)=\frac{s+2-\sqrt{s(s+4)}}2,
\]
with the square root positive for \(s>0\) and the branch analytic off \([-4,0]\). For \(s>0\), \(0<r(s)<1\). The unique bounded decaying solution to the tail recurrence in (2) obeys \(\widehat F_k=\widehat F_1r^{k-1}\) for \(k\ge1\). Solving the two boundary equations gives
\[
\widehat F_1=\big[(s+\tfrac23)(3s+5-3r)-\tfrac43\big]^{-1},\qquad
\widehat F_0=(3s+5-3r)\widehat F_1.
\]
Thus the Laplace transform of \(D(t)=V'(t)\) simplifies, using \(s=(1-r)^2/r\), to
\[
\boxed{\widehat D(s)=\frac{r(s)[2-r(s)]}{[1-r(s)]([1-r(s)]^2+2)}.} \tag{3}
\]
This equals \((2/3)s^{-1}+O(s^{-2})\) as \(s\to\infty\).

**4. Positive spectral inversion.** The branch cut of (3) is \([-4,0]\). Away from it, the physical root satisfies \(|r|<1\), whereas the only possible zeros of the denominator occur at \(r=1\) on the unit circle or at \(r=1\pm i\sqrt2\) outside it. There are no isolated poles. At \(s=-\lambda+i0\), \(0<\lambda<4\), use
\[
r=1-\frac\lambda2-\frac i2\sqrt{\lambda(4-\lambda)}.
\]
Direct simplification of the imaginary part yields
\[
-\frac1\pi\operatorname{Im}\widehat D(-\lambda+i0)
=\frac{(\lambda+2)\sqrt{4-\lambda}}{2\pi\sqrt\lambda(3\lambda^2-4\lambda+4)}=\rho(\lambda).
\]
Contour inversion of the analytic resolvent, using its decay at infinity and integrable endpoint singularities, gives \(D(t)=\int_0^4e^{-\lambda t}\rho(\lambda)d\lambda\). Integration in time gives the stated formula for \(V\). Since \(3\lambda^2-4\lambda+4>0\) for all real \(\lambda\), strict increase and concavity follow.

**5. Expansions.** From the generator (2), \(D(0)=2/3\) and \(D'(0)=-5/9\), giving the small-time expansion. Setting \(z=\sqrt s\) in (3), ordinary algebra gives
\[
\widehat D(s)=\frac1{2\sqrt s}+\frac14-\frac{11}{16}\sqrt s+O(s),\qquad s\downarrow0.
\]
Equivalently \(\rho(\lambda)=1/(2\pi\sqrt\lambda)+11\sqrt\lambda/(16\pi)+O(\lambda^{3/2})\) as \(\lambda\downarrow0\). Watson's lemma provides \(D(t)=1/(2\sqrt{\pi t})+11/(32\sqrt\pi\,t^{3/2})+O(t^{-5/2})\). The finite constant in the integrated asymptotics follows by subtracting the leading term in the Laplace transform:
\[
\int_0^\infty\left[D(t)-\frac1{2\sqrt{\pi t}}\right]dt
=\lim_{s\downarrow0}\left[\widehat D(s)-\frac1{2\sqrt s}\right]=\frac14.
\]
The integrand is integrable at both endpoints, so integration of the asymptotic tail gives the displayed \(t^{-1/2}\) correction and remainder. This completes the proof.

## Verification

The standalone file `verify_kmp.py` uses standard-library Simpson integration after the nonsingular substitution \(\lambda=4\sin^2\theta\). It checks both exact spectral moment sum rules \(\int\rho=2/3\) and \(\int\lambda\rho=5/9\), five independent resolvent comparisons, and three direct event-driven simulations of the microscopic lattice chain with 20,000 runs each. The simulation independently implements uniform bond exchanges, not the half-line moment equations. Reproduce with `python3 verify_kmp.py`. Numerical experiments corroborate, but are not substituted for, the infinite-lattice proof.

## Relationship to prior work

Schorlepp, Meerson and Sasorov (arXiv:2611.15739, first publicly available 2026-11-11) study precisely the localized KMP pulse and the spatial moment observables. Section IV, especially their equations (28)–(40), derives **leading long-time** variance using continuum macroscopic fluctuation theory. Their Section IX explicitly summarizes the result at leading order. The present statement concerns the unapproximated microscopic chain at every finite time, gives a positive compactly supported spectral density, establishes strict global concavity, and determines the nonzero lattice constant and subsequent correction. Its leading coefficient agrees with the earlier continuum result after accounting for the factor-two convention in bond rates; the leading coefficient is not presented as new.

The earlier Bettelheim–Smith–Meerson work (arXiv:2112.02474) concerns long-time heat transferred across a point; Bettelheim–Meerson (arXiv:2407.06335) concerns energy in a fixed spatial interval. Those observables do not determine the complete finite-time center variance without an additional derivation. Standard KMP moment duality and two-particle methods motivate (2) but are not claimed as novel techniques.

## Limitations

This is an exact **second-moment** statement for a one-site deterministic pulse and symmetric uniform KMP redistribution on an infinite line. It does not establish a finite-time distribution for the center, higher cumulants, large-deviation tails, heterogeneous bond rates, or boundaries. The spectral curve is for unit-rate microscopic bonds; comparison with continuum formulas requires explicit rate normalization. Novelty was checked against the specifically inspected literature and indexed records; unindexed equivalent two-particle resolvents remain a possibility. Independent scientific validation has not been performed.

## References

1. T. Schorlepp, B. Meerson and P. Sasorov, *Large deviations of spatial moments of the Kipnis–Marchioro–Presutti lattice gas following a localized energy release*, arXiv:2611.15739 (2026), https://arxiv.org/html/2611.15739v1 .
2. E. Bettelheim, N. R. Smith and B. Meerson, *Inverse Scattering Method Solves the Problem of Full Statistics of Nonstationary Heat Transfer in the Kipnis–Marchioro–Presutti Model*, arXiv:2112.02474 (2021), https://arxiv.org/abs/2112.02474 .
3. E. Bettelheim and B. Meerson, *Full Statistics of Regularized Local Energy Density in a Freely Expanding Kipnis–Marchioro–Presutti Gas*, arXiv:2407.06335 (2024), https://arxiv.org/abs/2407.06335 .
4. C. Kipnis, C. Marchioro and E. Presutti, *Heat flow in an exactly solvable model*, Journal of Statistical Physics 27 (1982), 65–74.
