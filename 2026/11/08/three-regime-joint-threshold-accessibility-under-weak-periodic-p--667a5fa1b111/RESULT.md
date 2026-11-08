# Three-regime joint threshold accessibility under weak periodic predator–prey forcing

## Finding
Consider harmonic modulation of the prey-growth rate in the smooth positive subsystem of a threshold predator–prey model. When prey and predator threshold distances shrink proportionally to the forcing scale, the smallest forcing amplitude for which the *same attracting periodic response* reaches both population thresholds (possibly at different phases) obeys an explicit, sharp three-regime frequency law. The optimum is either the predator-response resonance, the frequency at which the prey/predator threshold requirements balance, or the prey-response resonance. The regime is decided solely by the ratio of the two threshold distances.

For positive constants \(r,a,b,m,K,d_N,d_P\) satisfying \(n=m/(ab)\in(0,K)\), put
\[
 p=\frac{r}{a}\left(1-\frac nK\right),\quad
 \gamma=\frac{rn}{K},\quad C=abp,\quad
 D=mr\left(1-\frac nK\right),\quad
 u=n\left(1-\frac nK\right)>0.
\]
For \(\omega>0\), define
\[
Q(\omega)=(D-\omega^2)^2+\gamma^2\omega^2,
\quad R_N(\omega)=\frac{u\omega}{\sqrt{Q(\omega)}},
\quad R_P(\omega)=\frac{uC}{\sqrt{Q(\omega)}}.
\]
Set \(\omega_N=\sqrt D\), \(\omega_P=\sqrt{\max\{D-\gamma^2/2,0\}}\), and \(\omega_\times=C d_N/d_P>0\). Then \(0\le\omega_P<\omega_N\), and the *unique* limiting jointly optimal frequency is
\[
\boxed{
\omega_*=
\begin{cases}
\omega_P,& \omega_\times\le\omega_P,\\
\omega_\times,&\omega_P<\omega_\times<\omega_N,\\
\omega_N,&\omega_\times\ge\omega_N.
\end{cases}}
\]
The sharp limiting scaled forcing amplitude is
\[
\boxed{\displaystyle \sigma_0=\frac{\sqrt{Q(\omega_*)}}u
\max\left\{\frac{d_N}{\omega_*},\frac{d_P}{C}\right\}.}
\]
The first case is empty when \(\omega_P=0\). The predator harmonic lags the prey harmonic by exactly one quarter of a forcing period to first order, independently of the parameters and the frequency.

## Assumptions and scope
The *smooth continuation* (no threshold switching) is
\[
\dot N=N\left[\left(r+\varepsilon\sigma\sin(\omega t)\right)
\left(1-\frac NK\right)-aP\right],\qquad
\dot P=P(abN-m),
\]
where \(\varepsilon>0\) is small, \(\sigma\ge0\), and \(\omega>0\). Define moving thresholds \(N_a(\varepsilon)=n-\varepsilon d_N\), \(P_a(\varepsilon)=p-\varepsilon d_P\). For every fixed bound \(\Sigma>\sigma_0\) and all sufficiently small \(\varepsilon\), there is a unique positive, locally attracting periodic response in a neighborhood of \((n,p)\), uniformly for \(0\le\sigma\le\Sigma\) and \(\omega>0\). Let \(\sigma_\varepsilon\) be the infimum of amplitudes \(\sigma\in[0,\Sigma]\) such that there exists \(\omega>0\) for which this periodic response satisfies **both** \(\min_tN(t)\le n-\varepsilon d_N\) and \(\min_tP(t)\le p-\varepsilon d_P\). The two minima may occur at different times. Then \(\lim_{\varepsilon\downarrow0}\sigma_\varepsilon=\sigma_0\). Any frequencies whose required amplitudes are within \(o(1)\) of \(\sigma_\varepsilon\) converge to \(\omega_*\).

These claims concern a shrinking-distance, weak-forcing limit. They do **not** assert that both switching manifolds are admissibly crossed in the full Filippov model or that an actual tipping event occurs.

## Proof
**1. Stable equilibrium and uniform periodic solution.** At zero forcing, \((n,p)\) is a positive equilibrium, with Jacobian
\[
J=\begin{pmatrix}-\gamma&-an\\ C&0\end{pmatrix},\qquad
\det J=(an)C=D>0,\qquad\operatorname{tr}J=-\gamma<0.
\]
Thus \(J\) is Hurwitz. Express a nearby solution as \((n,p)+z(t)\). With \(\eta=\varepsilon\sigma\) the equation has the form
\[
\dot z=Jz+\eta u(1,0)^\mathsf T\sin(\omega t)
+R(z,\eta\sin(\omega t)),
\]
where on a fixed neighborhood \(\lVert R\rVert\le c(\lVert z\rVert^2+\eta\lVert z\rVert)\). The stable causal integral operator \((\mathcal Kh)(t)=\int_{-\infty}^t e^{J(t-s)}h(s)\,ds\) has a finite \(L^\infty\)-operator norm independent of \(\omega\). On a ball of radius \(O(\eta)\), the fixed-point map \(z=\mathcal K[\eta u e_1\sin\omega t+R]\) is a contraction for small \(\eta\), uniformly for \(\omega>0\). Uniqueness and periodicity of the forcing imply that the bounded solution is periodic with forcing period. Its sup-norm expansion has uniform remainder \(O(\eta^2)\). The same Hurwitz property and smallness of the time-dependent Jacobian ensure local asymptotic stability. Positivity follows by closeness to \((n,p)\).

**2. Complex transfer and the phase relation.** For a complex input with frequency \(\omega\), solve \((i\omega I-J)H=u e_1\). The solution is
\[
H_N(\omega)=\frac{u i\omega}{D-\omega^2+i\gamma\omega},\qquad
H_P(\omega)=\frac{u C}{D-\omega^2+i\gamma\omega}.
\]
Their moduli are \(R_N,R_P\), respectively, and \(H_P/H_N=C/(i\omega)=-iC/\omega\). Hence the predator harmonic is shifted by \(-\pi/2\) relative to the prey harmonic. The extrema of a sinusoid with a uniform \(O(\eta^2)\) perturbation obey, uniformly in \(\omega>0\) and bounded \(\sigma\),
\[
\min_tN(t)=n-\varepsilon\sigma R_N(\omega)+O(\varepsilon^2),\quad
\min_tP(t)=p-\varepsilon\sigma R_P(\omega)+O(\varepsilon^2).
\]

**3. Exact minimax and three phases.** The limiting amplitude needed for both minima to cross their separate levels at frequency \(\omega\) is
\[
S(\omega)=\max\left\{\frac{d_N}{R_N(\omega)},
\frac{d_P}{R_P(\omega)}\right\}
=\frac{\sqrt{Q(\omega)}}{u}
\max\left\{\frac{d_N}{\omega},\frac{d_P}{C}\right\}.
\]
The ratio between the two entries in the maximum equals \(\omega_\times/\omega\). Thus the prey constraint dominates below \(\omega_\times\), and the predator constraint above it. The prey cost is proportional to \(\sqrt{Q(\omega)/\omega^2}\), where
\[
\frac{Q(\omega)}{\omega^2}
=\omega^2+\frac{D^2}{\omega^2}+\gamma^2-2D,
\]
which decreases strictly up to \(\omega_N=\sqrt D\) and increases strictly thereafter. The predator cost is proportional to \(\sqrt{Q(\omega)}\), where
\[
Q'(\omega)=4\omega\big(\omega^2-D+\gamma^2/2\big),
\]
which decreases up to \(\omega_P\), when positive, and increases thereafter (or is strictly increasing for \(\omega>0\) when \(\omega_P=0\)). Since \(\omega_P<\omega_N\), the entire piecewise cost has a unique minimum at the stated three-case \(\omega_*\). Even in the node regime \(D\le\gamma^2/2\), the optimum remains strictly positive because \(\omega_\times>0\).

**4. Transfer of the optimum to small nonlinear forcing.** On every compact frequency interval, the error in the periodic extrema is uniformly \(O(\varepsilon^2)\) for bounded \(\sigma\). In fact that bound is uniform over \(\omega>0\). Since \(R_N(\omega)\to0\) as \(\omega\to0\) or \(\omega\to\infty\), the prey threshold with fixed \(d_N>0\) cannot be reached at bounded \(\sigma\) outside a common compact frequency interval once \(\varepsilon\) is small. On this compact interval the preceding threshold inequalities imply that the feasible scaled-amplitude infimum converges to \(\min S=\sigma_0\). Strictness and uniqueness of the minimum imply convergence of any asymptotically minimizing frequencies to \(\omega_*\).

## Verification
The accompanying `verify.py` checks the exact derivative identities defining both individual resonances, reconstructs the exact rational parameters in one published numerical example, and tests all three minimax phases against independent bounded numerical minimization. It additionally integrates the unthresholded nonlinear equations at twelve frequency/forcing combinations and compares the observed prey/predator amplitudes against the proved first-order formulas. A successful execution prints `VERIFY_OK exact_identities=3 minimax_regimes=6 nonlinear_amplitude_checks=24`. The mathematical conclusion for **all** positive parameters follows from the proof above, **not** from these finite checks. Python dependencies are SymPy, SciPy, and NumPy.

## Relationship to prior work
Gao, Poloni, Wang, and Lewis identify frequency-induced tipping in a threshold predator–prey system and numerically display separate frequency intervals for prey and predator threshold crossings. They establish admissible Filippov crossings that govern actual tipping. The present analysis isolates a different, sharply specified problem: the **joint** threshold accessibility of the attracting periodic solution of their no-switching smooth subsystem, under a proportional shrinking-threshold limit. It gives the exact trichotomy of optimal forcing frequencies and threshold-distance ratios. Earlier literature on periodically forced predator–prey systems and resonance establishes neither this parameter-complete joint minimax classification nor its proof in the material inspected. The stable-equilibrium and linear response techniques themselves are standard and are not claimed as new.

## Limitations
The result gives only the \(\varepsilon\to0\) critical-amplitude limit; it does not claim a closed finite-amplitude threshold, a uniform expansion when scaled forcing is unbounded, transient minima from arbitrary initial states, admissibility of switched-system boundary crossings, or a tipping outcome. The prey and predator extrema are generally separated by a quarter-period; “joint” means both occur on the same orbit, not at one instant. The available literature search does not amount to a proof of global historical novelty; one related older study was accessible only in abstract form. Independent audit has not been performed.

## References
1. S. Gao, S. Poloni, H. Wang, and M. Lewis, *Frequency-induced Tipping: Resonance-Driven Tipping in a Threshold Predator-Prey System*, arXiv:2610.39113v1, first posted 2026-10-29. https://arxiv.org/html/2610.39113v1
2. G. Sabin and D. Summers, *Chaos in a periodically forced predator–prey ecosystem model*, 1993, PMID 8431649. https://pubmed.ncbi.nlm.nih.gov/8431649/
3. E. Benincà et al., *Resonance of Plankton Communities with Temperature Fluctuations*, 2011. https://pmc.ncbi.nlm.nih.gov/articles/PMC3168990/
