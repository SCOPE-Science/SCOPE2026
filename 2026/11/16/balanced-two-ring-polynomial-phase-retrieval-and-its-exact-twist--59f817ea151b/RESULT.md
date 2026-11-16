# Balanced two-ring polynomial phase retrieval and its exact twist resonance

## Finding

For every integer \(K\ge 1\), consider the complex polynomial space \(\mathcal P_K=\{P(z)=\sum_{j=0}^{K}a_jz^j:a_j\in\mathbb C\}\). For positive radii \(r_0,r_1\) and angular twist \(\delta\in\mathbb R\), set
\[
 S(r_0,r_1,\delta)=\left\{r_0e^{\pi i j/K}:0\le j<2K\right\}\cup\left\{r_1e^{i(\delta+\pi j/K)}:0\le j<2K\right\}.
\]
The \(4K\) measurements \(\{|P(z)|^2:z\in S(r_0,r_1,\delta)\}\), retaining their labeled positions, determine **every** \(P\in\mathcal P_K\) up to multiplication by a constant of modulus one **if and only if**
\[
 \boxed{r_0\ne r_1\quad\text{and}\quad\sin(K\delta)\ne0.}
\]
Whenever \(\sin(K\delta)\ne0\), a linear two-FFT operation reconstructs the entire continuous squared-modulus trace on **each** circle. This statement is stronger at the interpolation stage: it holds for the real diagonal traces of every Hermitian coefficient matrix, without a rank-one assumption. The only angularly aliased Fourier channel has a normalized real \(2\times2\) inversion matrix with condition number
\[
 \boxed{\kappa_{\rm top}(K,\delta)=\sqrt{\frac{1+|\cos(K\delta)|}{1-|\cos(K\delta)|}}.}
\]
This channel has minimum condition number \(1\) exactly when \(\delta=(2m+1)\pi/(2K)\), for an integer \(m\), modulo \(\pi/K\). No assertion is made that this twist optimizes the conditioning of nonlinear polynomial recovery.

## Assumptions and scope

The degree bound \(K\), not an exact degree requirement, governs the result, so zero leading or constant coefficients are included. The two sample rings are centered at the origin; \(r_0,r_1>0\) are otherwise arbitrary and need not lie inside the unit disk, although one can rescale both to lie inside it. The two samples at different radii are regarded as distinct labeled measurements. Equality of data means equality of squared magnitudes at every specified point; recovery is modulo a *single global* factor \(e^{it}\), not modulo complex conjugation, reflection, or individual ring phases. No noise or lower-bound-on-coefficients hypothesis is imposed.

## Proof

**1. The angular Fourier data and its sole alias.** Let \(H\) be any Hermitian \((K+1)\times(K+1)\) matrix, and write
\[
 I_H(re^{it})=v(re^{it})^*Hv(re^{it}),\qquad v(z)=(1,z,\ldots,z^K)^{\mathsf T}.
\]
Its Fourier expansion is
\[
 I_H(re^{it})=\sum_{m=-K}^{K}c_m(r)e^{imt},\quad
 c_m(r)=\sum_{j=0}^{K-m}H_{j,j+m}r^{2j+m}\ (0\le m\le K),\quad c_{-m}(r)=\overline{c_m(r)}.
\]
In particular \(c_K(r)=r^K H_{0K}\). If the grid on a ring has offset \(\phi\), let
\[
 \widehat y_{\phi}(m)=\frac1{2K}\sum_{j=0}^{2K-1}I_H\bigl(re^{i(\phi+\pi j/K)}\bigr)e^{-\pi imj/K}.
\]
For \(0\le m<K\) there is no alias and \(\widehat y_\phi(m)=e^{im\phi}c_m(r)\). For \(m=K\), the positive and negative extreme harmonics coincide on the grid and
\[
 \widehat y_\phi(K)=2r^K\operatorname{Re}\bigl(e^{iK\phi}H_{0K}\bigr).
\]
Write \(H_{0K}=x+iy\), divide the two extreme DFT readings by \(2r_0^K\) and \(2r_1^K\), and use \(\phi_0=0\), \(\phi_1=\delta\). Their normalized observation matrix is
\[
 \begin{pmatrix}u_0\\u_1\end{pmatrix}
 =\underbrace{\begin{pmatrix}1&0\\\cos(K\delta)&-\sin(K\delta)\end{pmatrix}}_{M_K(\delta)}
 \begin{pmatrix}x\\y\end{pmatrix}.
\]
It is invertible precisely when \(\sin(K\delta)\ne0\). Under that condition one recovers \(c_K(r_j)\) as well as the \(2K-1\) real degrees of freedom in each lower Fourier band, and thus both full continuous intensity functions \(t\mapsto I_H(r_je^{it})\). The eigenvalues of \(M_K(\delta)^*M_K(\delta)\) are \(1\pm|\cos(K\delta)|\), proving the condition-number formula and its sharp twist minimizers. This conditioning statement concerns the dimensionless, radius-normalized two-real-unknown *top-channel matrix*, not the complete measurement map.

**2. Two distinct continuous circles determine the polynomial.** Apply the preceding interpolation to \(H=aa^*\), where the coefficient vector is chosen consistently so that \(I_H(z)=|P(z)|^2\). Equivalently, use the scalar expansion directly. Suppose polynomials \(P,Q\in\mathcal P_K\) have the same continuous modulus on circles of distinct positive radii. If one is zero, both are zero by the identity theorem. Otherwise \(R=P/Q\) is a nonzero rational function. For every \(r>0\), its rational reflection is \(R_r^\#(z)=\overline{R(r^2/\overline z)}\) (where both sides are read as rational functions). Modulus equality on \(|z|=r\) gives the rational identity \(R(z)R_r^\#(z)=1\); this remains valid across any isolated zeros or poles by continuation. Applying it for \(r_0,r_1\) yields \(R_{r_0}^\#=R_{r_1}^\#\), hence \(R(\lambda z)=R(z)\) identically for \(\lambda=r_1^2/r_0^2\ne1\). The Laurent series of \(R\) at the origin has only the constant coefficient because \(\lambda>0\) and \(\lambda^n\ne1\) for all nonzero integers \(n\). Thus \(R\) is constant; the measured modulus forces \(|R|=1\). This establishes sufficiency for every degree at most \(K\).

**3. Both assumptions are necessary.** If the radii coincide at \(r\), the polynomials \(P(z)=z^K\) and \(Q(z)=r^K\) have identical modulus at all sampling locations (indeed on the entire common circle), yet are not unimodular multiples. If \(\sin(K\delta)=0\), the two nonproportional polynomials \(P(z)=1+iz^K\) and \(Q(z)=1-iz^K\) have equal squared magnitude at all first-ring nodes, since the \(K\)-th power of each node is real; the same is true on the second ring because \(e^{iK\delta}=\pm1\). Both failures apply for every integer \(K\ge1\), regardless of coefficients vanishing at either endpoint. \(\square\)

## Verification

Run `python3 verify.py` with Python 3 and NumPy. The standalone script reconstructs every angular Fourier coefficient for \(432\) random Hermitian matrices across \(K\in\{1,2,3,4,5,7\}\) at three nonresonant twists, compares direct sampling with analytic coefficient expressions, verifies the two explicit ambiguity pairs at each tested degree, and checks the exact two-by-two singular-value formula. Last replay: `BALANCED_TWO_RING_PHASE_RETRIEVAL_PASS hermitian_cases=432 degrees=1,2,3,4,5,7 maximum_coefficient_error=3.39e-14 resonance_and_equal_radius=checked`. These finite tests are corroborative only; the proof above establishes all degrees and all admissible parameters.

## Relationship to prior work

Bodmann and Hammen (2013) achieve \(4K\) phaseless polynomial evaluations by using circles that intersect and hence share sampling nodes, rather than two centered, equal-size regular grids. Philipp (2014) uses a different collection including derivative magnitudes. Pohl, Li and Boche (2017) prove \(4K\)-sample recovery on concentric circles using \(2K+1\) outer nodes and \(2K-1\) inner nodes; their full-concentric-circle uniqueness mechanism and total sample count are not presented here as new. Chalendar and Partington (2024) prove general continuous-circle modulus uniqueness. The present statement instead classifies **all angular twists** for two **balanced** regular grids of \(2K\) nodes each, exhibits the exact obstruction at resonance, and specifies sharp angular Nyquist-channel conditioning. It does not claim a smaller overall sample count or a new continuous-circle rigidity theorem.

## Limitations

The conclusion is for centered regular angular grids, polynomial degree bounded by \(K\), complex data with labeled positions, and noiseless measurements. Global phase retrieval does not imply uniformly stable inversion near zero signals or under nearly coincident radii; the top-channel condition number is not the condition number of recovering the full polynomial. Related results may exist under Vandermonde-frame, analytic-phase-retrieval, or two-mask Fourier sampling terminology. No independent mathematical audit has been performed.

## References

1. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487v1 (2013), Section 2.3. https://arxiv.org/html/1302.5487v1
2. F. Philipp, *Phase Retrieval from 4N-4 Measurements*, arXiv:1403.4769 (2014), Theorem 1.1. https://arxiv.org/abs/1403.4769
3. V. Pohl, N. Li and H. Boche, *Phase Retrieval in Spaces of Analytic Functions on the Unit Disk*, SampTA conference presentation dated 4 July 2017, summary theorem on slide 18. https://www.ce.cit.tum.de/fileadmin/w00cgn/lti/pdf/vortraege/Pohl-Phase_Retrieval_in_Spaces_of_Analytic_Functions_on_the_Unit_Disk.pdf
4. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (2024), Section 2.2, Theorem 2.6. https://arxiv.org/html/2403.16255v3
