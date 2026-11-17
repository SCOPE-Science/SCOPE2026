# Exact stroboscopic reversibility and two-clock detection in planar Ornstein–Uhlenbeck diffusion

## Finding

For a stationary planar Ornstein–Uhlenbeck (OU) diffusion with an irreversible steady current, **a positive observation interval makes the entire sampled chain reversible if and only if the drift has nonreal eigenvalues and the interval is an integer multiple of half its oscillation period**. More precisely, with definitions below, if the drift eigenvalues are \(a\pm i\omega\), \(\omega>0\), then the exceptional sampling intervals are exactly
\[
\mathcal H=\{n\pi/\omega:n=1,2,3,\ldots\}.
\]
If its drift eigenvalues are real, no positive interval hides irreversibility. Consequently, observing at two positive intervals with irrational ratio guarantees that at least one stationary two-time law detects every irreversible planar OU diffusion. Conversely, a rational ratio admits an irreversible rotating OU diffusion whose two sampled chains are both exactly reversible.

For the isotropic rotating OU diffusion defined below, the ordered-pair versus reversed-pair Kullback–Leibler divergence at lag \(h>0\) is exactly
\[
K(h)=\frac{4\sin^2(\omega h)}{e^{2\gamma h}-1},\qquad
\lim_{h\downarrow0}\frac{K(h)}{h}=\frac{2\omega^2}{\gamma}>0.
\]
Thus finite-rate observation can yield *zero* measured time asymmetry even when the underlying continuous process dissipates at a strictly positive rate.

## Assumptions and scope

Let \(X_t\in\mathbb R^2\) obey
\[
dX_t=B X_t\,dt+\sqrt{2D}\,dW_t,
\]
where \(B\) is a real \(2\times2\) Hurwitz matrix, \(D=D^{\mathsf T}\succ0\), and both coordinates are even under physical time reversal. Put \(\Sigma\succ0\) for the unique solution of
\[
B\Sigma+\Sigma B^{\mathsf T}+2D=0.
\]
Initialize \(X_0\) in the centered stationary Gaussian law \(N(0,\Sigma)\). Define the continuous stationary-current matrix
\[
J=B\Sigma-\Sigma B^{\mathsf T}.
\]
Irreversible means \(J\ne0\); this definition is equivalent to nonzero Gaussian stationary probability current and to strictly positive standard overdamped entropy production. For \(h>0\), the sampled chain is \(Y_k=X_{kh}\) for all integer \(k\). Reversible means its complete stationary finite-dimensional distributions are invariant under reversing time, equivalently its one-step joint law is symmetric under exchange of the two vector-valued coordinates. This is **not** a claim about time reversal of an unobserved interpolation between samples.

## Proof

**(1) Paired Gaussian law and detailed balance.** The stationary OU transition is Gaussian with conditional mean \(e^{Bh}x\) and covariance \(\Sigma-e^{Bh}\Sigma e^{B^{\mathsf T}h}\). The joint covariance of \((X_0,X_h)\) is
\[
\begin{pmatrix}
\Sigma&\Sigma e^{B^{\mathsf T}h}\\
e^{Bh}\Sigma&\Sigma
\end{pmatrix}.
\]
A centered nonsingular Gaussian law is unchanged when the two blocks are exchanged precisely when its off-diagonal covariance blocks agree. Hence the lag-\(h\) sampled chain satisfies detailed balance if and only if
\[
J_h:=e^{Bh}\Sigma-\Sigma e^{B^{\mathsf T}h}=0.
\]
Because the sampled process is a stationary Markov chain, detailed balance for one transition implies reversible path laws of every finite length.

**(2) Exact Cayley–Hamilton reduction.** Write \(a=\tfrac12\operatorname{tr}B\), \(H=B-aI\), and \(\Delta=a^2-\det B\). Cayley–Hamilton gives \(H^2=\Delta I\). Therefore, for every real \(h\),
\[
e^{Bh}=e^{ah}\big(c_\Delta(h)I+s_\Delta(h)H\big),
\]
where \(c_\Delta\) is an even scalar function and
\[
s_\Delta(h)=
\begin{cases}
\sinh(\sqrt\Delta h)/\sqrt\Delta,&\Delta>0,\\
h,&\Delta=0,\\
\sin(\sqrt{-\Delta}h)/\sqrt{-\Delta},&\Delta<0.
\end{cases}
\]
The scalar identity part cancels from \(J_h\), and \(H\Sigma-\Sigma H^{\mathsf T}=J\). Thus the **exact finite-lag current identity** is
\[
\boxed{J_h=e^{ah}s_\Delta(h)J.}
\]
If \(J=0\), all lags are reversible. If \(J\ne0\), for \(\Delta\ge0\) the scalar factor is nonzero at every \(h>0\). For \(\Delta<0\), its positive zeros are exactly \(h=n\pi/\sqrt{-\Delta}\). These are exactly the eigenvalue-imaginary-part half-periods in the statement. At these times the full propagator is the scalar matrix \((-1)^ne^{ah}I\), independently of \(D\) and of whether \(B\) is normal.

**(3) Two-clock criterion and sharpness.** For any irreversible planar OU diffusion, if two lags both lie in its exceptional set, their ratio must be a ratio of positive integers. Consequently irrational \(h_1/h_2\) prevents simultaneous exact reversibility. Conversely, if \(h_1/h_2=p/q\) with coprime positive integers, choose \(\omega=\pi p/h_1=\pi q/h_2\) and \(B=-\gamma I+\omega R\), where \(\gamma>0\) and \(R=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). For \(D=dI\), \(d>0\), the steady current is nonzero but both lags belong to \(\mathcal H\), proving sharpness.

**(4) Exact information-loss example.** In this rotating case, \(\Sigma=(d/\gamma)I\) and \(e^{Bh}=\rho R_\theta\), with \(\rho=e^{-\gamma h}\) and \(\theta=\omega h\). The forward and block-reversed stationary two-time Gaussian covariance matrices differ by transposing the rotation in their off-diagonal blocks; they have equal determinants. The zero-mean Gaussian relative-entropy formula therefore gives
\[
K(h)=\frac12\big(\operatorname{tr}(C_{\rm rev}^{-1}C)-4\big)
=\frac{4\rho^2\sin^2\theta}{1-\rho^2}
=\frac{4\sin^2(\omega h)}{e^{2\gamma h}-1}.
\]
The stationary overdamped entropy-production rate (Boltzmann constant set to one) is
\[
\sigma=\frac14\operatorname{tr}\big(\Sigma^{-1}J^{\mathsf T}D^{-1}J\big)=\frac{2\omega^2}{\gamma}>0.
\]
Taylor expansion of the displayed exact \(K(h)\) yields \(\lim_{h\downarrow0}K(h)/h=\sigma\). In particular, \(K(n\pi/\omega)=0\), even though \(\sigma>0\).

## Verification

The included standalone program `check.py` numerically reconstructs \(\Sigma\), the Gaussian ordered-pair covariance, the swapped-pair divergence, and the continuous entropy-production rate. It evaluates normal and nonnormal rotating drifts, anisotropic and correlated diffusion, real and repeated-real spectra, resonance and nonresonance, and two incommensurable lags. Running `python check.py` passed 403 deterministic assertions with NumPy and SciPy in the checked environment. These computations are finite diagnostics; the universally quantified classification, exact Kullback–Leibler identity, and arithmetic criterion follow from the proof above.

## Relationship to prior work

Das, Manikandan, and Banerjee (2022) examine entropy-production inference in gyrators and explicitly discuss sampling-interval dependence in the short-time estimation method; their results do not give a complete exact discrete-time reversibility set for planar linear dynamics. Ghosal and Bisker (2022) quantify coarse-grained and partially observed irreversibility from dwell-time asymmetries, rather than the complete two-vector OU path law at specified sampling times. Viot and collaborators (2023) study time-discretized angular momentum and angular velocity distributions in a gyrator; their observables and inference question differ from this exact joint-law classification. Nagayama, Kolchinsky, and Ito (2026) develop a spectral decomposition of continuous-time OU dissipation; their paper discusses oscillatory eigenmodes but does not formulate the complete set of reversible discrete sampling lags or the two-clock condition. Classical Gaussian detailed-balance and Cayley–Hamilton identities are foundational tools, not claimed as new.

## Limitations

This result concerns stationary, fully observed, two-dimensional OU diffusions with constant positive-definite diffusion and even-parity state variables. At finite data length, exact zero/nonzero asymmetry cannot be decided with mathematical certainty, and near-resonant sampling can be statistically difficult. A second sampling interval of irrational ratio prevents *exact* aliasing, but does not guarantee a uniform positive detection margin over unknown frequencies. Neither higher-dimensional drifts nor partial observation are classified here. A general theorem in an unindexed reference concerning reversible elements of Markov semigroups may imply part of the classification; the publication-priority comparison is not exhaustive.

## References

- B. Das, S. K. Manikandan, and A. Banerjee, *Inferring entropy production in anharmonic Brownian gyrators*, first public 2022-04-20, https://arxiv.org/abs/2204.09283.
- A. Ghosal and G. Bisker, *Inferring entropy production rate from partially observed Langevin dynamics under coarse-graining*, first public 2022-05-29, https://arxiv.org/abs/2205.14688.
- P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, and G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, first public 2023-07-11, https://arxiv.org/abs/2307.05248.
- R. Nagayama, A. Kolchinsky, and S. Ito, *Oscillatory-nonnormal decomposition of dissipation in Ornstein–Uhlenbeck processes*, first public 2026-06-05, https://arxiv.org/abs/2606.07263. (Later comparative literature, not used for the date scope.)
