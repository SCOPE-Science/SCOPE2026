# Exact volume and sharp volume overhead of the cube's Thales-ball covering

## Finding

For an integer \(d\ge1\), let \(Q_d=[-1,1]^d\) and let \(D_v\) be the closed Euclidean ball of diameter \([0,v]\) for each \(v\in\{-1,1\}^d\). Put \(T_d=\bigcup_v D_v\), \(U_d=\operatorname{vol}_d(T_d)\). Then
\[
T_d=\{x:\|x\|_2^2\le\|x\|_1\},\qquad Q_d\subseteq T_d,
\qquad U_d=2(\pi/2)^{d/2}[t^d]F(t)^d,
\]
where \(F(t)=2e^{t^2/2}\Phi(t)=e^{t^2/2}(1+\operatorname{erf}(t/\sqrt2))\), and \(\Phi\) is the standard normal CDF. For \(c_k=2^{k/2}\Gamma((k+1)/2)/(\sqrt\pi\,k!)\), the coefficient is the finite sum \(\sum_{k_1+\cdots+k_d=d}\prod_j c_{k_j}\). In dimensions one through four the volumes are \(2, 2+\pi, 2+4\pi, 2+10\pi+\pi^2\).

Let \(\varphi\) be the standard normal density. There is a unique \(\tau>0\) with \(\tau^2+\tau\varphi(\tau)/\Phi(\tau)=1\). Define
\[
r=\varphi(\tau)/\Phi(\tau),\qquad
\beta=\tau(2\tau+r-\tau r(\tau+r))>0,\qquad
\Lambda=\sqrt{\pi/8}\,F(\tau)/\tau>1.
\]
Then
\[
\frac{U_d}{2^d}=\frac{2\Lambda^d}{\sqrt{2\pi\beta d}}\bigl(1+O(d^{-1})\bigr),\qquad d\longrightarrow\infty.
\]
Rounded values are \(\tau\approx0.83992367569237\), \(\beta\approx1.41094356197717\), and \(\Lambda\approx1.69763020222053\). Thus the ambient union has exponentially larger volume than the cube, with limiting volume-overhead base \(\Lambda\).

## Assumptions and scope

Volumes and distances are Euclidean. The prescribed balls are centered at \(v/2\) with radius \(\sqrt d/2\); the union is not clipped to the cube. The ratio is ambient union volume divided by cube volume, not a sum of ball volumes, a pairwise overlap statistic, or an optimal covering bound. The coefficients are Maclaurin coefficients of the indicated entire function. All constants in the error estimate are fixed, independent of \(d\).

## Proof

Membership in \(D_v\) is equivalent to \(\|x-v/2\|_2^2\le d/4\), or \(\|x\|_2^2\le x\cdot v\). The maximum of the right-hand side over signs is \(\|x\|_1\). The coordinate inequality \(x_i^2\le |x_i|\) on the cube proves containment. The radial length in a unit direction \(u\) is therefore \(\|u\|_1\).

Let \(G=R\Theta\) be a standard Gaussian vector in \(\mathbb R^d\), with length and direction independent and \(\Theta\) uniform on the sphere (uniform on the two signs for \(d=1\)). Polar integration gives \(U_d=\kappa_d\,\mathbb E\|\Theta\|_1^d\), where \(\kappa_d=\pi^{d/2}/\Gamma(d/2+1)\). The chi moment \(\mathbb E R^d=2^{d/2}\Gamma(d)/\Gamma(d/2)\) then gives
\[
U_d=\frac{2(\pi/2)^{d/2}}{d!}\,\mathbb E\left(\sum_{j=1}^d|G_j|\right)^d.
\]
Completing the square in the half-normal integral gives \(F(t)=\mathbb E e^{t|G_1|}\); the Gaussian tail allows all complex \(t\) and the power series for \(F\) is entire. The half-normal moments give the displayed \(c_k\). Independence of the \(G_j\) proves the coefficient formula; expansion through order four gives the stated small-dimensional values.

For \(t>0\), define \(N_t\) on the nonnegative integers by \(\Pr(N_t=k)=c_kt^k/F(t)\). Differentiating its generating function gives \(\mu(t)=\mathbb E N_t=tF'(t)/F(t)\) and \(t\mu'(t)=\operatorname{Var}N_t>0\) because all \(c_k\) are positive. The mean tends to zero as \(t\downarrow0\), and to infinity as \(t\to\infty\) since \(F'/F=t+\varphi/\Phi\). Hence the stated saddle \(\tau\) exists and is unique. Differentiating \(r(t)=\varphi(t)/\Phi(t)\) gives \(r'=-r(t)(t+r(t))\), so the variance at the saddle is \(\beta\). Also \(F(t)/t\ge 1/t+\sqrt{2/\pi}+t/2\ge\sqrt2+\sqrt{2/\pi}\), giving \(\Lambda\ge(\sqrt\pi+1)/2>1\).

Let \(N_1,\ldots,N_d\) be independent copies of \(N_\tau\). The exact convolution identity is
\[
\Pr\left(\sum_j N_j=d\right)=\tau^d F(\tau)^{-d}[t^d]F(t)^d.
\]
To evaluate the probability, apply lattice Fourier inversion to the centered variable \(N_\tau-1\). Its characteristic function \(\psi\) has modulus bounded strictly below one on every closed subarc of \([-\pi,\pi]\) away from zero, since the support has span one. Near zero, \(\log\psi(\theta)=-\beta\theta^2/2-i\kappa_3\theta^3/6+O(\theta^4)\), where \(\kappa_3\) is the third centered moment; the expansion follows from the exponential moments. After setting \(x=\sqrt d\,\theta\), on \(|x|\le d^{1/12}\) the integrand is the Gaussian \(e^{-\beta x^2/2}\) times \(1-i\kappa_3 x^3/(6\sqrt d)+O((x^4+x^6)/d)\). The odd term integrates to zero there. Outside that window, the remaining small-angle portion is bounded by a Gaussian tail (the real part of \(\log\psi\) is at most \(-c\theta^2\) for some \(c>0\)); the fixed outer subarcs are exponentially small. Thus the probability is \((2\pi\beta d)^{-1/2}(1+O(d^{-1}))\). Substituting into the volume coefficient and dividing by \(2^d\) gives the asserted ratio.

## Verification

The companion `verify_thales_volume.py` gives finite numerical checks of the low-dimensional expressions, the saddle constants, the finite-size error at selected dimensions up to 64, and radial formulas via angular quadrature and a seeded Gaussian-direction experiment. These are diagnostics, not a proof of the all-dimensional or asymptotic statements. The rounded constants can also be reproduced by bisection on \((0,1)\), using \(\Phi(t)=1/2+(2\pi)^{-1/2}\sum_{k\ge0}(-1)^k t^{2k+1}/(2^k k!(2k+1))\).

## Relationship to prior work and limitations

Pavlík's polytope theorem supplies the general Thales-ball covering and an internal power-diagram tiling, not the ambient union volume. Zhigljavsky and Noonan study fractions of the cube covered by other arrangements, not the ambient volume of the prescribed balls here. Large-powers saddle-point estimates are classical; the geometric coefficient identification gives the particular function and scale used here. No claim of an optimal arrangement or of exhaustive historical priority is made.

1. J. Pavlík, *Thales’s theorem in higher dimensions*, [arXiv:2611.14277](https://arxiv.org/abs/2611.14277), §5, Theorem 5.1 and Corollary 5.3.
2. A. Zhigljavsky and J. Noonan, *Covering of High-Dimensional Cubes and Quantization*, Operations Research Forum **1**, article 18 (2020), [doi:10.1007/s43069-020-0015-8](https://doi.org/10.1007/s43069-020-0015-8).
3. P. Flajolet and R. Sedgewick, *Analytic Combinatorics* (2009), Theorem VIII.8.
