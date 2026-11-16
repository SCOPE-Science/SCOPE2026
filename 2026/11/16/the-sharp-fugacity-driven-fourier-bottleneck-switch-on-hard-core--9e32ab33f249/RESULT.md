# The sharp fugacity-driven Fourier bottleneck switch on hard-core cyclic ladders

## Finding

Let \(P_n=C_n\square K_2\) be the cyclic two-rail ladder, with \(n\ge3\), and give every independent vertex set \(I\) probability proportional to \(z^{|I|}\), where \(z>0\). Let \(G_n(z)\) be the probability-normalized Gram matrix of the \(2n\) **centered first-coordinate Walsh characters**, and let \(\kappa_n(z)\) be its largest eigenvalue divided by its smallest eigenvalue. Every \(G_n(z)\) is positive definite.

Define
\[
\Lambda=\frac{1+z+\sqrt{z^2+6z+1}}2,\qquad
r=\frac z\Lambda\in(0,1),\qquad D=1+2r-r^2,
\]
and
\[
\rho_{\mathrm s}=-\frac{r(1-r)}{1+r},\qquad \rho_{\mathrm a}=-r,\qquad m=\frac{2r}{D}.
\]
The two limiting rail-symmetric and rail-antisymmetric **covariance** Fourier multipliers at spatial angle \(\theta\) are exactly
\[
S_{\mathrm s}(\theta)=\frac{m(1-m)}2\frac{1-\rho_{\mathrm s}^2}{1-2\rho_{\mathrm s}\cos\theta+\rho_{\mathrm s}^2},\qquad
S_{\mathrm a}(\theta)=\frac m2\frac{1-\rho_{\mathrm a}^2}{1-2\rho_{\mathrm a}\cos\theta+\rho_{\mathrm a}^2}.
\]
More precisely, if \(\lambda_{n,k}^{\mathrm s},\lambda_{n,k}^{\mathrm a}\) are the eigenvalues of \(G_n(z)\) in the rail-even and rail-odd cyclic Fourier sectors, then for each **fixed** \(z>0\),
\[
\max_{0\le k<n}\max_{\eta\in\{\mathrm s,\mathrm a\}}
\left|\frac{\lambda_{n,k}^{\eta}}4-S_{\eta}(2\pi k/n)\right|\longrightarrow0
\qquad (n\longrightarrow\infty).
\]

The largest limiting Fourier-multiplier value is **always** at the alternating spatial frequency in the rail-antisymmetric sector. The smallest limiting eigenvalue undergoes exactly one sharp change of rail parity, at
\[
\boxed{z_*=1+\frac2{\sqrt3}}.
\]
It is rail-symmetric and at zero spatial frequency when \(0<z<z_*\), rail-antisymmetric and at zero spatial frequency when \(z>z_*\), and the **two rail-parity branches tie at zero spatial frequency** at \(z=z_*\). The limiting squared-energy conditioning is
\[
\boxed{\displaystyle\lim_{n\to\infty}\kappa_n(z)=
\begin{cases}
\frac{D^2}{(1-r)^2(1+r^2)},&0<z\le z_*,\\[3pt]
\left(\frac{1+r}{1-r}\right)^2,&z\ge z_*.
\end{cases}}
\]
The two expressions agree at the threshold, but their first derivatives with respect to activity do not: the **upward derivative jump** of the limiting condition ratio is exactly \(9(\sqrt3-1)/4\). In particular this ratio is \(4+2\sqrt2\) at \(z=1\), is \(1+6z+O(z^3)\) as \(z\downarrow0\), and is \(z^2+4z+O(1)\) as \(z\to\infty\). These are iterated limits: first ladder length tends to infinity with fixed \(z\); no claim is made for joint high-density and large-ladder scalings.

## Assumptions and scope

For each rung \(j\in\mathbb Z/n\mathbb Z\), a hard-core configuration has state \(0\) (empty), \(A\) (upper vertex occupied), or \(B\) (lower vertex occupied). States \(A,A\) and \(B,B\) cannot occur in consecutive rungs, and there can never be two occupied vertices in one rung. In particular the graph is the usual prism \(C_n\square K_2\), not a diagonally constrained triangular ladder. Write \(x_{j,A},x_{j,B}\) for occupation indicators. The corresponding Walsh characters are \(w_{j,t}=1-2x_{j,t}\); the centered Gram entries are \(G_{(j,t),(j',t')}=\mathbb E[(w_{j,t}-\mathbb Ew_{j,t})(w_{j',t'}-\mathbb Ew_{j',t'})]\), so \(G=4\operatorname{Cov}(x)\).

The ratio \(\kappa_n\) uses **all** \(2n\) eigenvalues; no zero-mode projection or pseudo-inverse convention is used. All measurements are over the independent-set probability distribution; this is **not** a quantum ladder Hamiltonian or the continuous-frequency STFT. The Fourier transform on rungs uses cyclic frequencies \(\theta_k=2\pi k/n\).

## Proof

**1. Exact transfer representation.** Using weights on both endpoints symmetrically, the symmetric three-state transfer matrix in state order \((0,A,B)\) is
\[
T_z=\begin{pmatrix}1&\sqrt z&\sqrt z\\\sqrt z&0&z\\\sqrt z&z&0\end{pmatrix}.
\]
The product of its entries around any state cycle is \(z^{|I|}\) precisely for legal hard-core configurations; all forbidden transitions contribute zero. Thus the partition function is \(\operatorname{tr}(T_z^n)\). Interchanging the rails splits the state space into a two-dimensional even block \(\left(\begin{smallmatrix}1&\sqrt{2z}\\\sqrt{2z}&z\end{smallmatrix}\right)\) and a one-dimensional odd block \((-z)\). Their eigenvalues are \(\Lambda\), \(\lambda_-=(1+z-\sqrt{1+6z+z^2})/2=-z/\Lambda\), and \(-z\). Since \(0<z<\Lambda\), the Perron eigenvalue \(\Lambda\) is simple and strictly dominates all other eigenvalues in magnitude.

The relation \(z=r(1+r)/(1-r)\) follows from \(\Lambda^2-(1+z)\Lambda-z=0\), so \(\Lambda=(1+r)/(1-r)\). Differentiating the limiting pressure \(\log\Lambda\) with respect to \(\log z\) gives the occupied-rung probability
\[
m=z\frac{d}{dz}\log\Lambda=\frac{2r}{1+2r-r^2}.
\]
Consequently \(0<m<1\) for all \(z>0\).

**2. Two exact infinite-volume covariance modes.** Let \(u_j=(x_{j,A}+x_{j,B})/\sqrt2\) and \(v_j=(x_{j,A}-x_{j,B})/\sqrt2\). The infinite-volume limit is the unique Perron state of \(T_z\). Rail symmetry gives \(\mathbb Ev_j=0\), \(\operatorname{Var}(u_j)=m(1-m)/2\) and \(\operatorname{Var}(v_j)=m/2\). The centered operator for \(u\) acts within the even two-dimensional transfer sector; after subtracting its Perron expectation it has only the \(\lambda_-\) spectral channel. The \(v\) operator is odd and connects the Perron eigenvector only to the odd eigenvector of eigenvalue \(-z\). Hence for every integer \(d\)
\[
\operatorname{Cov}(u_0,u_d)=\frac{m(1-m)}2\left(\frac{\lambda_-}{\Lambda}\right)^{|d|},\quad
\operatorname{Cov}(v_0,v_d)=\frac m2\left(\frac{-z}{\Lambda}\right)^{|d|},\quad
\operatorname{Cov}(u_0,v_d)=0.
\]
The two correlation ratios are \(\rho_{\mathrm s}=-r(1-r)/(1+r)\) and \(\rho_{\mathrm a}=-r\). Applying the absolutely convergent identity \(\sum_{d\in\mathbb Z}\rho^{|d|}e^{-id\theta}=(1-\rho^2)/(1-2\rho\cos\theta+\rho^2)\) gives the asserted two Fourier multipliers. Both are strictly positive for all \(\theta\).

**3. Uniform cyclic convergence.** The finite-ring one- and two-point functions are trace ratios of the form \(\operatorname{tr}(OT_z^dO'T_z^{n-d})/\operatorname{tr}(T_z^n)\), with diagonal occupation matrices \(O,O'\). Spectrally expanding them using the three eigenvalues from step 1 shows that, after periodizing the absolutely summable infinite-volume covariance, the error in each cyclic covariance at distance \(d\) is bounded by \(C_z(\alpha_z^{n-d}+\alpha_z^{n}+\alpha_z^d\alpha_z^n)\) for \(0\le d\le n/2\), where \(\alpha_z=\max\{|\lambda_-|,z\}/\Lambda=r<1\). For the complementary half-cycle use \(d\mapsto n-d\). Summing the resulting error bounds in Fourier space gives an \(O_z(n\alpha_z^{n/2})\) bound, uniform across frequencies and both rail sectors. The Fourier transform of the periodized covariance at \(2\pi k/n\) equals its infinite-lattice Fourier series evaluated at that frequency. Because \(G_n=4\operatorname{Cov}(x)\), the claimed uniform multiplier convergence follows.

**4. Sharp extrema and unique crossover.** Both \(\rho\)-parameters lie in \((-1,0)\), hence both \(S\)-branches decrease strictly as \(\cos\theta\) increases. Their respective minima occur at \(\theta=0\) and maxima at \(\theta=\pi\). Direct simplification using \(D=1+2r-r^2\) yields
\[
\begin{aligned}
S_{\mathrm s}(0)&=\frac{r(1-r^2)(1+r^2)}{D^3},&
S_{\mathrm a}(0)&=\frac{r(1-r)}{(1+r)D},\\
S_{\mathrm s}(\pi)&=\frac{r(1-r^2)}{(1+r^2)D},&
S_{\mathrm a}(\pi)&=\frac{r(1+r)}{(1-r)D}.
\end{aligned}
\]
The comparisons factor **exactly** as
\[
S_{\mathrm a}(\pi)-S_{\mathrm s}(\pi)=\frac{2r^2(1+r)}{(1-r)(1+r^2)D}>0,
\]
and
\[
S_{\mathrm a}(0)-S_{\mathrm s}(0)=\frac{2r^2(1-r)(1-3r^2)}{(1+r)D^3}.
\]
Therefore the top is always rail-odd at \(\pi\), while the bottom changes sign exactly when \(r=1/\sqrt3\). Because \(z=r(1+r)/(1-r)\) is strictly increasing on \((0,1)\), this occurs at the **single** positive activity \(z_*=1+2/\sqrt3\). At the threshold the two rail sectors at zero frequency tie and no other frequency attains the minimum. Division of the maximum by the smaller of the two endpoint minima yields the two displayed rational expressions for \(\kappa_\infty\). Differentiating both rational branches with respect to \(r\), then using \(dz/dr=(1+2r-r^2)/(1-r)^2\), gives \(\kappa_\infty'(z_*+)-\kappa_\infty'(z_*-)=9(\sqrt3-1)/4>0\).

**5. Conditioning and asymptotics.** Step 3 together with positivity in step 2 implies convergence of the extreme eigenvalues and thus \(\kappa_n(z)\to\kappa_\infty(z)\) for fixed \(z\). For odd \(n\), frequencies closest to \(\pi\) converge to it, so parity creates no different limiting condition ratio. The high-activity branch equals \(\Lambda^2\) because \(\Lambda=(1+r)/(1-r)\); expanding the explicit Perron root gives \(z^2+4z+O(1)\). Expanding the low-activity branch gives \(1+6z+O(z^3)\). Substitution of \(z=1\) gives \(4+2\sqrt2\).

Finally, finite-volume positive definiteness does **not** depend on the asymptotic analysis: every legal configuration has positive probability, including the empty set and every singleton. A linear combination of occupation indicators constant on this support must vanish on the empty set and have every coefficient zero by testing the singletons. Thus the covariance and centered-Walsh Gram matrices are positive definite for every finite \(n\ge3\).

## Verification

The included `checker.py` checks every displayed endpoint identity, both factorized differences, the threshold transformation and both conditioning expressions by exact symbolic simplification. It independently enumerates all legal cyclic rung words for \(3\le n\le9\) at activities \(z\in\{1/2,1,3\}\), comparing weighted two-point functions exactly to transfer trace formulas. Further numerical tests compare full cyclic covariance eigenvalue arrays to the continuum multipliers for ring lengths \(32,64,96,128\) and activities \(0.1,1,1+2/\sqrt3,3,10\). The largest error at length \(128\) in these tests is below \(10^{-7}\). Execute `python checker.py` with Python 3, NumPy and SymPy. Finite checks supplement, but do not replace, the all-parameter proof above.

## Relationship to prior work

The hard-core activity distribution and occupancy method are standard; Davies, Kang, Pirot and Sereni (2020) give a general local-occupancy framework for graph independent sets but do not give Fourier sampling spectra of cyclic prisms. The independence polynomial of the prism is a known closed formula, as tabulated by MathWorld; the partition function and three transfer eigenvalues are background facts, **not** the novelty. The new point is the exact **arbitrary-activity spatial covariance spectrum and its sharp limiting rail-parity bottleneck switch**. A previously available uniform-activity Fourier-frame theorem gives the full finite-ring spectrum at \(z=1\) and its limiting constant \(4+2\sqrt2\). That isolated activity is included as a consistency check, and is **not** claimed as a new case. The present piecewise activity law and unique threshold are not implied by knowing the uniform special case or the single-variable independence polynomial.

Work on quantum hard-core bosonic ladders studies different dynamical observables and different Hamiltonians; equal terminology does not make its structure factors equivalent to the classical grand-canonical covariance operator here. The available literature comparison does not constitute a proof of historical priority.

## Limitations

This is an exact thermodynamic-limit result for each fixed positive fugacity, together with finite-ring nonsingularity. It does **not** give closed finite-ring extrema for every activity, does **not** establish simultaneous limits with activity changing with ring length, and describes no thermodynamic phase transition. The minimum-sector switch is a transition in reconstruction conditioning only. Although relevant sources and semantic mathematical records were searched, an unindexed earlier classical ladder static-structure-factor formula could cover some or all of these expressions; independent historical review remains outstanding.

## References

1. E. Davies, R. J. Kang, F. Pirot, J.-S. Sereni, *Graph structure via local occupancy*, arXiv:2003.14361, first public version 2020-03-31. https://arxiv.org/abs/2003.14361
2. E. W. Weisstein, *Independence Polynomial*, MathWorld, table entry for prism graphs (known partition-function formula). https://mathworld.wolfram.com/IndependencePolynomial.html
3. J. Schmidt, G. M. Schütz, H. van Beijeren, *A lattice Gas Model for Generic One-Dimensional Hamiltonian Systems*, J. Stat. Phys. 183 (2021), article 8, DOI:10.1007/s10955-021-02709-1 (different dynamical exclusion ensemble).
