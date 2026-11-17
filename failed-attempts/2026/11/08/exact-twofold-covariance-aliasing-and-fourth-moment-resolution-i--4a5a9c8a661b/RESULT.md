# Exact twofold covariance aliasing and fourth-moment resolution in an intermittently trapped Brownian particle

## Finding

A stationary Brownian particle in a trap that randomly switches between off and on has a **two-to-one map from its mechanical rates to its full stationary position autocovariance**. In the nondegenerate case, the two models are exactly related by
\[
(\kappa,\nu,D)\longmapsto(2\nu,\kappa/2,D).
\]
They differ in their stationary fourth moments. Hence a single fourth-position moment breaks an ambiguity that survives knowing the second-order correlation function at every time lag.

Set \(\Sigma=\kappa+2\nu\) and \(\Pi=\kappa\nu\), and let \(0<u<v\) be the roots of \(z^2-\Sigma z+\Pi=0\). For all \(t\ge0\),
\[
C(t)=\mathbb E[X_0X_t]=\frac{D}{v-u}\left(\frac{v}{u}e^{-ut}-\frac{u}{v}e^{-vt}\right).
\]
The invariant parameters are exactly determined by the observable one-sided derivatives:
\[
D=-C'(0+),\qquad
\Pi=\frac{C'''(0+)}{D},\qquad
\Sigma=\frac{\Pi C(0)}{D}.
\]
Every candidate stiffness is a positive root of \(\kappa^2-\Sigma\kappa+2\Pi=0\). Thus there are precisely two possible rate pairs if \(\Sigma^2>8\Pi\), and one if \(\Sigma^2=8\Pi\). The additional observation
\[
m_4=\mathbb E[X_0^4]=\frac{3D^2}{\Pi^2}(\Sigma^2+3\Sigma\kappa-4\Pi)
\]
recovers the original rates without ambiguity:
\[
\kappa=\frac{\Pi^2m_4/(3D^2)-\Sigma^2+4\Pi}{3\Sigma},
\qquad \nu=\frac{\Pi}{\kappa}.
\]
This is a complete classification, not a claim about finite-sample statistical distinguishability.

## Assumptions and scope

Fix \(\kappa>0\), \(\nu>0\), and \(D>0\). The state \(S_t\in\{0,1\}\) is a two-sided stationary symmetric continuous-time Markov chain, with jump rate \(\nu\) in **each** direction, independent of a two-sided standard Brownian motion \(W_t\). The position satisfies
\[
dX_t=-\kappa S_tX_t\,dt+\sqrt{2D}\,dW_t.
\]
The particle is *not spatially reset*: the trap strength is set to zero when \(S_t=0\), and to \(\kappa\) when \(S_t=1\). All correlation and moment statements concern the unique joint stationary law of \((X,S)\). The autocovariance is \(C(t)=\operatorname{Cov}(X_0,X_t)\), which equals \(\mathbb E[X_0X_t]\) because the stationary spatial mean is zero. Derivatives at zero are **right derivatives**, since the two-sided stationary covariance is even in lag and generally has a cusp at zero.

## Proof

**1. Existence, symmetry, and moments.** Couple two solutions using the same \((S,W)\). Their difference is multiplied by \(\exp(-\kappa\int_0^t S_a\,da)\), which tends to zero almost surely by ergodicity of the symmetric two-state chain. The past-noise convolution
\[
X_t=\sqrt{2D}\int_{-\infty}^t\exp\left(-\kappa\int_s^t S_a\,da\right)dW_s
\]
gives the unique stationary solution. Conditional Gaussian symmetry makes every stationary odd moment zero. All even moments are finite: the joint generator equations for order \(2n\) have strictly positive determinant \(2n\kappa\nu\), and the inverse of the resulting nonsingular \(M\)-matrix has nonnegative entries, giving a finite-moment recursion beginning with the stationary state probabilities \(1/2\).

**2. Second moments by the joint generator.** Write \(w_j=\mathbb E[X_0^2\mathbf 1_{\{S_0=j\}}]\). Applying the generator to \(x^2\mathbf 1_{\{S=j\}}\) yields
\[
0=D+\nu(w_1-w_0),\qquad
0=D+\nu(w_0-w_1)-2\kappa w_1.
\]
Consequently,
\[
w_1=\frac{D}{\kappa},\qquad
w_0=\frac{D}{\kappa}+\frac{D}{\nu},\qquad
C(0)=w_0+w_1=\frac{D(\kappa+2\nu)}{\kappa\nu}.
\]

**3. The full two-time covariance.** For \(t\ge0\), define \(v_j(t)=\mathbb E[X_0X_t\mathbf 1_{\{S_t=j\}}]\). The Brownian increment has zero conditional contribution, and therefore
\[
\frac{d}{dt}\begin{pmatrix}v_0\\v_1\end{pmatrix}=
\begin{pmatrix}-\nu&\nu\\\nu&-\nu-\kappa\end{pmatrix}
\begin{pmatrix}v_0\\v_1\end{pmatrix},\qquad
v(0)=\begin{pmatrix}w_0\\w_1\end{pmatrix}.
\]
Call the matrix \(Q\). Its characteristic polynomial is \(\lambda^2+\Sigma\lambda+\Pi\), where \(\Sigma=\kappa+2\nu\), \(\Pi=\kappa\nu\), and \(\Sigma^2-4\Pi=\kappa^2+4\nu^2>0\). Thus \(Q\) has distinct eigenvalues \(-u\), \(-v\), with \(0<u<v\). By direct multiplication,
\[
C(0)=\frac{D\Sigma}{\Pi},\quad C'(0+)=-D,\quad C''(0+)=0,\quad C'''(0+)=D\Pi.
\]
Solving the resulting second-order ordinary differential equation with the first two initial conditions gives the displayed exact two-exponential covariance. Both modal coefficients are nonzero because \(D,u,v>0\).

**4. Classification of the covariance aliases.** Equality of entire covariance functions forces equality of \(D\), \(\Pi\), and \(\Sigma\) through the three observed derivatives/values above. Conversely, these three parameters determine the covariance formula. Solving \(\kappa^2-\Sigma\kappa+2\Pi=0\) produces the two possible positive stiffnesses
\[
\kappa_\pm=\frac{\Sigma\pm\sqrt{\Sigma^2-8\Pi}}{2},
\qquad\nu_\pm=\frac{\Pi}{\kappa_\pm}.
\]
Their product is \(2\Pi\), so the second rate pair is exactly \((2\nu,\kappa/2)\). The discriminant is \((\kappa-2\nu)^2\); the pair is distinct if and only if \(\kappa\ne2\nu\). This exhausts **all** positive-rate models with that covariance.

**5. Stationary fourth moment and separation.** Write \(z_j=\mathbb E[X_0^4\mathbf 1_{\{S_0=j\}}]\). Generator stationarity for the fourth power yields
\[
0=12D w_0+\nu(z_1-z_0),\qquad
0=12D w_1+\nu(z_0-z_1)-4\kappa z_1.
\]
Solving and summing produces
\[
m_4=z_0+z_1=\frac{6D^2}{\kappa^2}\left(2+\frac{3\kappa}{\nu}+\frac{2\kappa^2}{\nu^2}\right).
\]
Using \(\nu=\Pi/\kappa\) and \(\kappa^2-\Sigma\kappa+2\Pi=0\), this reduces exactly to the displayed linear function of \(\kappa\). In particular,
\[
m_4(\kappa_+)-m_4(\kappa_-)=
\frac{9D^2\Sigma\sqrt{\Sigma^2-8\Pi}}{\Pi^2}>0
\]
when the aliases are distinct. Solving the linear formula gives the stated unique inverse. The second moment was already included in \(C(0)\), and all odd one-time moments vanish, so the fourth moment is the **lowest-order additional stationary position moment** capable of resolving the ambiguity.

## Verification

The standalone `checker.py` recomputes the conditional second and fourth moments from independent stationary-generator equations, verifies the matrix characteristic identity and zero-lag derivatives symbolically, confirms the fourth-moment inverse formula and rate duality, and independently compares closed-form and matrix-exponential covariances for six rational parameter triples at five lags each. It also checks that every non-self-dual tested pair has different fourth moments. Run with Python 3, SymPy, and mpmath:

`python checker.py`

An independent series expansion of the published stationary characteristic function in [1] gives the same second and fourth moment expressions. For \((\kappa,\nu,D)=(1,1,1)\), the dual is \((2,1/2,1)\). Both have \(C(0)=3\), \(C'(0+)=-1\), and \(C'''(0+)=1\), and their covariance functions coincide at every lag, but their fourth moments are respectively \(42\) and \(69\).

## Relationship to prior work

Santra, Das, and Nath [1], arXiv:2104.00609 (first public version 1 April 2021), introduced the same on/off harmonic diffusion and established its time-dependent one-time variance, stationary characteristic function, stationary distribution, and first-passage properties. Their variance relaxation is **not** the two-time stationary autocovariance considered here. Frydel [2], arXiv:2407.12213 (first public version 16 July 2024), derived its stationary Gaussian-mixture representation and explicit second and fourth moments (Sec. II, Eq. (7)), together with physical observables. Those moments and the underlying two-state model are prior results, not claimed as novel.

The assessed result is the exact **twofold hidden-parameter aliasing of the entire stationary autocovariance**, the full equivalence classification including its self-dual boundary, and a minimal-order supplementary stationary moment that breaks the alias. Although the ingredients are accessible from known forward equations, the examined sources do not state or compare this inverse-identifiability theorem. General finite-state linear filtering may offer an alternative derivation and constitutes a remaining publication-priority risk.

## Limitations

The switching is exactly symmetric with equal off-to-on and on-to-off rates; stiffness is zero in the off state, spatial noise is additive and homogeneous, and the model is stationary. Exact derivatives and moments are population quantities; their inference from finite, discretely sampled or noisy data can be ill-conditioned, and no estimator or finite-sample guarantee is proved. This is not a claim about identifying parameters from nonstationary marginal relaxation, higher-order time series, direct measurements of the trap state, or asymmetric switching. No independent scientific audit is claimed.

## References

[1] I. Santra, S. Das, S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609, first public version 2021-04-01. https://arxiv.org/abs/2104.00609

[2] D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213, first public version 2024-07-16; *Physical Review E* **110**, 024613 (2024). https://arxiv.org/abs/2407.12213
