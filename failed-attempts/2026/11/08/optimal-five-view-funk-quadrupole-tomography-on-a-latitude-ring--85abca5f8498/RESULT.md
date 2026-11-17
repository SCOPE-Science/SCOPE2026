# Optimal five-view Funk quadrupole tomography on a latitude ring

## Finding

Fix the usual area measure \(d\Omega\) on the unit two-sphere and the five-dimensional Hilbert space \(V=\mathcal H_2(S^2;\mathbb C)\) of *pure degree-two* spherical harmonics. The normalized Funk operator is
\[
(Rf)(n)=\frac{1}{2\pi}\int_{x\cdot n=0}f(x)\,ds(x).
\]
For \(0<\theta<\pi/2\) put \(t=\cos^2\theta\) and choose five equally spaced great-circle normals
\[
n_j=(\sin\theta\cos(2\pi j/5),\sin\theta\sin(2\pi j/5),\cos\theta),\quad j=0,\ldots,4.
\]
Let \(A_\theta:V\to\mathbb C^5\) map \(f\) to \(((Rf)(n_j))_{j=0}^4\); the data norm is unweighted Euclidean norm. Its entire squared singular spectrum, including multiplicities, is
\[
\operatorname{spec}(A_\theta^*A_\theta)=\frac{25}{64\pi}\left\{(3t-1)^2,\ 6t(1-t),\ 6t(1-t),\ \frac32(1-t)^2,\ \frac32(1-t)^2\right\}.
\]
The five-view map is invertible if and only if \(t\ne1/3\) (within the stipulated open range). Both (i) minimizing the operator condition number and (ii) maximizing the lower frame bound among **all regular five-normal single-latitude rings** have the same unique optimum:
\[
t_*=\frac{6-\sqrt{21}}{15},\qquad \kappa_*=\frac{\sqrt{5+\sqrt{21}}}{2},\qquad B_*=\frac{11-\sqrt{21}}{32\pi}.
\]
The optimal latitude above the equator is \(\arcsin(\sqrt{t_*})\), approximately \(17.9026\) degrees. At this optimum, the lower eigenvalue \(B_*\) has multiplicity three and the upper eigenvalue \((17+3\sqrt{21})/(64\pi)\) has multiplicity two. This is a sharp *restricted-design* statement; no global claim is made for five arbitrary great-circle normals.

## Assumptions and scope

The signal is an arbitrary **complex** pure quadrupole \(f=\sum_{m=-2}^{2}c_mY_2^m\); the \(Y_2^m\) are orthonormal for unnormalized area measure \(d\Omega\), and \(\sum_m|c_m|^2=\|f\|_{L^2(S^2)}^2\). The Funk average is divided by \(2\pi\), so its eigenvalue on degree two is \(-1/2\). There are exactly five **labelled**, noiseless scalar readings, one from each unoriented great circle, with no arbitrary individual rescaling of their noise variances. The ring has free latitude but fixed azimuth increments \(2\pi/5\); a common azimuthal rotation does not alter any singular value. The same optimum holds for southern rings by reversing the pole direction, since Funk data are even in their normals. Distinct latitude rings, unequal angular separations, or more than five scans are outside the optimization domain.

## Proof

**1. Funk action and matrix normalization.** Any degree-two harmonic is the restriction of a trace-free complex quadratic \(x^TQx\). Uniform averaging over the unit circle perpendicular to a unit vector \(n\) gives the second moment \((I-nn^T)/2\). Consequently, \((Rf)(n)=\frac12(\operatorname{tr}Q-n^TQn)=-f(n)/2\). This also agrees with the well-known Funk eigenvalue \(P_2(0)=-1/2\).

For the standard Condon–Shortley convention the harmonic values at longitude zero have squared magnitudes
\[
|Y_2^0(\theta,0)|^2=\frac5{16\pi}(3t-1)^2,\quad
|Y_2^{\pm1}(\theta,0)|^2=\frac{15}{8\pi}t(1-t),\quad
|Y_2^{\pm2}(\theta,0)|^2=\frac{15}{32\pi}(1-t)^2.
\]
The entries in the five-by-five scan matrix are \(M_{jm}=-\tfrac12Y_2^m(\theta,0)e^{2\pi imj/5}\), with columns indexed by \(m=-2,-1,0,1,2\). Since any two different orders differ by a nonzero integer of absolute value at most four, the five-point Fourier identity gives
\[
\sum_{j=0}^4e^{2\pi i(m-m')j/5}=5\,\mathbf1_{m=m'}.
\]
Thus the columns are orthogonal and \(M^*M\) is diagonal, with entries \(5|Y_2^m(\theta,0)|^2/4\). Substitution proves the full spectrum. In \(0<t<1\), its only zero is the \(m=0\) entry at \(t=1/3\). Five readings are also dimension-minimal for linear recovery on \(V\).

**2. Exact condition-number minimax.** Set \(r=t/(1-t)>0\). After dividing the three distinct eigenvalue factors by the common positive factor \((1-t)^2\), they are
\[
v_0=(2r-1)^2,\qquad v_1=6r,\qquad v_2=\frac32.
\]
For \(0<r\le1/4\), \(v_2\) is the largest, so the squared condition number equals \((3/2)/\min(v_0,v_1)\). Here \(v_0\) strictly decreases and \(v_1\) strictly increases, meeting only at \(r_*=(5-\sqrt{21})/4\); this is the unique optimum on that interval. Its value is \((3/2)/(6r_*)=(5+\sqrt{21})/4\).

No larger \(r\) can improve it. For \(1/4\le r\le3/5\), the inequality \(v_0\le1/4\) implies \(\kappa^2\ge v_2/v_0\ge6\) (at \(r=1/2\) the map is singular). For \(r\ge3/5\), the ratio \(v_1/v_2=4r\ge12/5>(5+\sqrt{21})/4\). Hence \(r_*\) is the **unique global minimum**. Substitution yields \(t_*=r_*/(1+r_*)=(6-\sqrt{21})/15\).

**3. Independent optimum of the lower frame bound.** Let \(a_0(t)=(3t-1)^2\), \(a_1(t)=6t(1-t)\), and \(a_2(t)=\tfrac32(1-t)^2\). The lower frame bound is \(\frac{25}{64\pi}\min\{a_0(t),a_1(t),a_2(t)\}\). On \((0,t_*)\), \(a_1(t)\) increases and is strictly below its value at \(t_*\). On \((t_*,1/3)\), \(a_0(t)\) decreases and is strictly below its value at \(t_*\). On \([1/3,1/2]\), \(a_0(t)\le1/4\); on \([1/2,1)\), \(a_2(t)\le3/8\). Both upper bounds are strictly less than \(a_0(t_*)=a_1(t_*)=(22-2\sqrt{21})/25\). At \(t_*\), \(a_2\) is larger than this common value, so \(t_*\) uniquely maximizes the minimum. Multiplication by \(25/(64\pi)\) gives \(B_*=(11-\sqrt{21})/(32\pi)\). The threefold and twofold multiplicities and upper level follow by direct substitution.

**4. Exact inversion.** Write \(a_m=Y_2^m(\theta,0)\) and \(y_j=(Rf)(n_j)\). For any admissible \(t\), the inverse is the azimuthal five-point DFT
\[
c_m=-\frac{2}{5a_m}\sum_{j=0}^4y_je^{-2\pi imj/5},\qquad m=-2,-1,0,1,2.
\]
The inversion is well-defined precisely at the five-view injective latitudes. Its sharp worst-case error-amplification factor for Euclidean additive measurement errors is \(1/\sqrt{B(t)}\); thus at \(t_*\) it equals \(\sqrt{32\pi/(11-\sqrt{21})}\). The condition-number result additionally quantifies relative stability.

## Verification

The standalone standard-library script `verify_funk_pentagon.py` separately constructs all five measurement columns, their complex Gram matrix, and the inverse five-point DFT. Run `python verify_funk_pentagon.py`; its expected completion is `CHECKS_PASS 1353`. Tests include eleven interior latitudes, 1,000 grid comparisons with the sharp minimizer, random complex coefficient reconstructions, and direct great-circle averaging of trace-free quadratic test functions. Algebraic arguments above, not sampled grids, prove the infinite-domain minimax and uniqueness.

## Relationship to prior work

Quellmalz, Weissinger, Hubmer, and Erchinger (first public March 9, 2023) develop a frame decomposition of the Funk transform. Their equation (10) supplies the general spherical-harmonic eigenvalue used here, while their infinite-dimensional frame treatment does not state a finite five-view ring conditioning optimum. Elahi, Khalid, Kennedy, and McEwen (first public September 5, 2018) study optimally sized spin-weighted *full-band* sphere sampling on multiple iso-latitude rings and choose latitudes through a numerical conditioning heuristic. They do not assert the present closed-form optimality or lower-frame-bound coincidence for a **pure spin-zero, degree-two, single-ring Funk** system. Khalid, Kennedy, and McEwen (first public March 19, 2014) numerically optimize the colatitudes for a complete multi-ring low-pass sampling scheme of dimension \(L^2\); at \(L=3\), this uses nine readings, not a single five-view pure quadrupole ring. The distinction is one of hypothesis and implication, not merely nomenclature. General five-frequency DFT orthogonality and harmonic formulas are treated as classical ingredients, not new discoveries.

## Limitations

The theorem is restricted to exact quadrupole signals and regular equal-azimuth, single-latitude five-circle scans. Its best condition number is **not** asserted to be optimal among all five-view geometries, nonuniform scan weightings, or higher spherical-harmonic bands. All noise claims are deterministic operator-norm consequences, not distribution-specific estimation guarantees. The reported literature comparison does not certify publication priority: some broader sampling results could contain an equivalent special case not indexed under the same terminology. Independent review is not part of this mathematical statement.

## References

1. M. Quellmalz, L. Weissinger, S. Hubmer, and P. D. Erchinger, *A Frame Decomposition of the Funk-Radon Transform*, arXiv:2303.05179v1 (public March 9, 2023), https://arxiv.org/abs/2303.05179 ; DOI 10.1007/978-3-031-31975-4_4.
2. U. Elahi, Z. Khalid, R. A. Kennedy, and J. D. McEwen, *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321v1 (public September 5, 2018), https://arxiv.org/abs/1809.01321 ; DOI 10.1109/LSP.2018.2865676.
3. Z. Khalid, R. A. Kennedy, and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661v1 (public March 19, 2014), https://arxiv.org/abs/1403.4661 ; DOI 10.1109/TSP.2014.2337278.
4. Standard degree-two spherical harmonic normalization and finite Fourier orthogonality; explicit identities are reproduced within the proof, so no additional external theorem is required.
