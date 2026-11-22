# Sharp three-node spectral compensation for perturbed Fourier sampling

## Finding

The **smallest critically sampled Fourier grid on which positive diagonal reweighting can improve the first-order worst-case Gram spectrum has three nodes**. In that dimension, a one-parameter family of node velocities has an exact, nontrivial interval on which its operator-norm first-order defect reaches a universal Rayleigh lower bound. The operator norm and the spectral half-spread (hence first-order condition-number distortion) require different, oppositely directed weight adjustments even for a symmetric perturbation.

Let \(A_{\ell j}(t)=\exp(i\ell x_j(t))\), with \(\ell,j\in\{0,1,2\}\), \(x_j(t)=2\pi j/3+t\epsilon_j\), and \(\epsilon=(0,u,1)\), where \(0\le u\le1\). For strictly positive real weights satisfying \(\sum_jv_j=1\), put
\[
G(t,v)=A(t)\operatorname{diag}(v)A(t)^*,\qquad
E_{\mathrm{op}}(t,u)=\inf_v\|G(t,v)-I\|_{\mathrm{op}},\qquad
E_{\mathrm{sp}}(t,u)=\inf_v\frac{\lambda_{\max}(G(t,v))-\lambda_{\min}(G(t,v))}{2}.
\]
The one-sided limits \(L_{\mathrm{op}}(u)=\lim_{t\downarrow0}E_{\mathrm{op}}(t,u)/t\) and \(L_{\mathrm{sp}}(u)=\lim_{t\downarrow0}E_{\mathrm{sp}}(t,u)/t\) exist. Set \(u_\pm=(9\pm\sqrt{21})/18\). Then
\[
L_{\mathrm{op}}(u)\ge\frac4{3\sqrt3},\qquad
L_{\mathrm{op}}(u)=\frac4{3\sqrt3}\quad\Longleftrightarrow\quad u_-\le u\le u_+.
\]
Within that **closed sharp interval**, its unique first-order optimal weight correction is
\[
v_j(t)=\frac13+t\zeta_{\mathrm{op},j}(u)+o(t),\qquad
\zeta_{\mathrm{op}}(u)=\frac1{3\sqrt3}(\tfrac13-u,\tfrac13,u-\tfrac23).
\]
The same statement concerns uniqueness of the tangent, not uniqueness of exact minimizers at each positive \(t\). At \(u=1/2\),
\[
L_{\mathrm{op}}(1/2)=\frac4{3\sqrt3},\qquad
L_{\mathrm{sp}}(1/2)=\frac9{8\sqrt3}.
\]
For the symmetric case a spectral-half-spread-minimizing tangent is
\[
\zeta_{\mathrm{sp}}=\frac1{3\sqrt3}(\tfrac14,-\tfrac12,\tfrac14),
\]
which points in the *opposite direction* from the unique operator-norm-optimal tangent
\(\zeta_{\mathrm{op}}=\frac1{3\sqrt3}(-\tfrac16,\tfrac13,-\tfrac16)\).
The unweighted coefficients are \((1+\sqrt3)/(2\sqrt3)\) for operator norm and \((3+\sqrt3)/(4\sqrt3)\) for half-spread, both strictly larger. In contrast, unweighted first-order squared Frobenius norm is \(1\), while operator- and spread-optimal tangent choices increase it to \(19/18\) and \(9/8\), respectively.

## Assumptions and scope

All matrices are complex with Hermitian adjoints. The operator norm is the spectral norm; the half-spread is half the range of Hermitian eigenvalues. The weights are strictly positive and sum to \(1\), with no constraint on their smoothness as functions of \(t\); optimization is repeated separately at every \(t>0\). Limits hold for each fixed \(u\in[0,1]\). Zero-step normalized weights are \(v^0=(1/3,1/3,1/3)\). The frequency set and nodes are specified above; different frequency bands or general jitters are not asserted to obey these numerical constants.

## Proof

**1. Exact first variation.** Write \(\omega=e^{2\pi i/3}\), \(F_{\ell j}=\omega^{\ell j}/\sqrt3\) and \(P=\operatorname{diag}(1,e^{i\pi/3},\omega)\). The matrices \(F,P\) are unitary. For a zero-sum tangent \(v_j(t)=1/3+t\zeta_j+o(t)\), direct differentiation of the exponential entries, then unitary conjugation, yields
\[
P^*F^*\left[\frac{G(t,v(t))-I}{t}\right]FP\longrightarrow
\frac1{\sqrt3}\left[B(u)+\operatorname{diag}(d)\right],\qquad
B(u)=\begin{pmatrix}0&u&1\\u&0&1-u\\1&1-u&0\end{pmatrix},\quad
 d=3\sqrt3\zeta,\quad\sum_jd_j=0.
\]
The identity can be verified directly from \(A'(0)_{\ell j}=i\ell\epsilon_j\omega^{\ell j}\), without using an unproved Fourier-perturbation lemma.

**2. Optimization may be interchanged with the first-order limit.** At \(t=0\), \(G(0,v)=3F\operatorname{diag}(v)F^*\). Thus the uniform vector uniquely minimizes both defects, with \(\|G(0,v)-I\|_{\mathrm{op}}=\max_j|3v_j-1|\). The uniform candidate at small \(t\) has defect \(O(t)\), forcing any nearly optimal weight vector to satisfy \(v-v^0=O(t)\). For the half-spread, \(\operatorname{tr}G=3\), hence its half-spread bounds the operator defect from below up to an absolute dimensional factor, giving the same conclusion. After dividing by \(t\), all nearly optimal tangent vectors are bounded. Compactness and uniform Taylor estimates identify each infimum limit with the minimum of the corresponding Hermitian tangent objective over \(\sum d_j=0\). The minimizers exist by coercivity and can be implemented by strictly positive weights for all sufficiently small \(t>0\).

**3. Universal operator lower bound and its exact equality window.** Put \(w=(1,1,1)^T/\sqrt3\). For \(S=B+\operatorname{diag}(d)\) and \(\sum d_j=0\),
\[
w^TSw=\frac43,\qquad \|S\|_{\mathrm{op}}\ge\frac43.
\]
Equality forces \(Sw=(4/3)w\). This is equivalent to constant row sums and uniquely determines
\[
d=d_{\mathrm{bal}}=(\tfrac13-u,\tfrac13,u-\tfrac23).
\]
The eigenvalues of this balanced matrix are exactly
\[
\frac43,\qquad -\frac23\pm\sqrt{1-3u(1-u)}.
\]
Its spectral radius equals \(4/3\) exactly when \(\sqrt{1-3u(1-u)}\le2/3\), or equivalently \(u\in[(9-\sqrt{21})/18,(9+\sqrt{21})/18]\). Outside the interval no diagonal perturbation attains the universal bound; since the optimization is coercive and its minimum is attained, the optimal norm is **strictly** greater. This proves the sharp interval and unique equality-case tangent.

**4. Different sharp half-spread correction at symmetric motion.** For \(u=1/2\), \(B\) is symmetric under exchange of its first and third coordinates. The spectral half-spread is convex under matrix averaging and invariant under orthogonal conjugation. Averaging any candidate with its coordinate-reflection therefore does not increase the objective. The optimal symmetric diagonal is of the form \(d=(a,-2a,a)\). Its three eigenvalues are
\[
a-1,\qquad \frac{1-a\pm\sqrt{(1+3a)^2+2}}{2}.
\]
For \(a\le1/4\), the full eigenvalue spread is \([3-3a+\sqrt{(1+3a)^2+2}]/2\), strictly decreasing in \(a\). For \(a\ge1/4\), it is \(\sqrt{(1+3a)^2+2}\), strictly increasing. Hence the sharp minimizer among symmetric candidates is \(a=1/4\), with eigenvalues \(3/2,-3/4,-3/4\). By convex symmetrization this is a **global** half-spread minimizer. Multiplication by \(1/\sqrt3\) gives \(L_{\mathrm{sp}}=9/(8\sqrt3)\). At the operator optimum \(d=(-1/6,1/3,-1/6)\), the balanced eigenvalues are \(4/3,-1/6,-7/6\). The strict improvement compared with \(d=0\) follows from the unweighted eigenvalues \(-1,(1\pm\sqrt3)/2\). Squaring the tangent entries shows the claimed Frobenius values.

**5. Minimality of three nodes.** For one Fourier node, the normalized Gram operator is always the identity. For two square-DFT nodes, after unitary conjugation every first-order node tangent is a Hermitian off-diagonal matrix, while a normalized weight change is traceless diagonal. A further diagonal phase makes the node tangent real. Therefore every total first-order tangent is, up to overall scaling,
\[
\begin{pmatrix}a&b\\b&-a\end{pmatrix},\qquad \lambda_{\pm}=\pm\sqrt{a^2+b^2},
\]
so both operator norm and half-spread are minimized at \(a=0\). No strict gain from reweighting exists with fewer than three nodes.

## Verification

The included `verify.py` is a standalone Python 3 script using SymPy and NumPy. It reproduces the exact DFT derivative and unitary phase reduction; symbolic characteristic polynomials; the balanced phase-window roots; the symmetric half-spread eigenvalue crossing; the Frobenius ratios and two-node minimality; and several small-\(t\) numerical asymptotic checks. Run `python verify.py` from a directory with `sympy` and `numpy` installed. A passing run prints `VERIFY_OK symbolic_spectrum_phase_window_minimality`. Exact symbolic identities support finite algebraic steps; the quantified minimax and limiting assertions follow from the proof, not the finite tests.

## Relationship to prior work

Wind-Andersen [1] derives the first-order node/weight Gram decomposition and proves Frobenius orthogonality at critical sampling. Crucially, its Section 8.3 **already gives a four-node example where nonzero weights improve spectral half-spread even though Frobenius error worsens**. The present theorem therefore does **not** claim that broad observation as novel. Its new assessed contribution is the exact three-node minimality, a sharp nontrivial interval of node-motion ratios saturating a universal operator-norm floor, and the two distinct exact optimal spectral weight directions in the minimal dimension. In [1], spectral optimization is explicitly outside the main Frobenius theorem. Kircheis and Potts [2] study exact and least-squares density compensation of Fourier sampling, rather than this spectral minimax phase window. Austin and Trefethen [3] study perturbed-point interpolation and quadrature stability, a distinct issue. A literature and mathematical-record comparison was conducted; it is not a proof of historical uniqueness.

## Limitations

This is a fixed three-frequency, three-node first-order theorem, with a one-parameter velocity family; it does not classify all movements or all grid sizes, or give an exact global minimizer for positive finite \(t\). Outside the stated phase window, the strict lower-bound separation is proved but its exact minimum value is not given. For the half-spread the displayed optimal symmetric correction is proved globally optimal, without a classification of every possible nonsymmetric minimizer. The results involve normalized positive weights and Gram spectral objectives, not operator reconstruction error for a particular signal. Historical priority and generalization beyond this model require independent verification.

## References

[1] E. Wind-Andersen, *Alias Geometry and Density Compensation in Perturbed Fourier Sampling*, arXiv:2611.02379v1 (first posted 2026-11-02), especially Sections 2, 7, 8.3. https://arxiv.org/html/2611.02379v1

[2] M. Kircheis and D. Potts, *Optimal density compensation factors for the reconstruction of the Fourier transform of bandlimited functions*, arXiv:2304.00094v2, especially Section 2. https://arxiv.org/html/2304.00094v2

[3] A. P. Austin and L. N. Trefethen, *Trigonometric interpolation and quadrature in perturbed points*, arXiv:1612.04018 (2016), *SIAM J. Numer. Anal.* 55 (2017), 2113–2122. https://arxiv.org/abs/1612.04018
