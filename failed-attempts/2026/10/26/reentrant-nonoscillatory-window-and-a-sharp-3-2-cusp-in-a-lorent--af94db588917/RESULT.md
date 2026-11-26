# Reentrant nonoscillatory window and a sharp \(3/2\)-cusp in a Lorentzian pseudomode trimer

## Finding
For the three-mode effective Hamiltonian of Lin, Kuo, Lambert, Miranowicz, Nori and Chen (arXiv:2406.18362, Eq. (28)), let the coherent coupling \(\chi>0\), reservoir linewidth \(\Lambda>0\), and bath coupling parameter \(\Gamma>0\) vary independently. Write
\[
u=\left(\frac{\chi}{\Lambda}\right)^2,\qquad v=\frac{\Gamma}{2\Lambda}.
\]
The generator has three purely imaginary, distinct eigenvalues (hence the amplitude dynamics have three nonoscillatory exponential modes) **if and only if**
\[
0<u<\frac1{27},\qquad v_-(u)<v<v_+(u).
\]
Here \(r_-(u)\in(0,1/3)\) and \(r_+(u)\in(1/3,1/2)\) are the two roots of \(u=r^2(1-2r)\), and the exact boundary functions are
\[
v_\pm(u)=2r_\pm(u)(1-r_\pm(u))^2.
\]
At the two endpoints \(v=v_\pm(u)\) the matrix has a second-order exceptional point (EP2); for smaller or larger positive \(v\), two eigenvalues have nonzero, opposite real parts. Thus changing reservoir coupling at fixed \(\chi/\Lambda\) produces the sequence oscillatory–nonoscillatory–oscillatory. If \(u>1/27\), no positive bath coupling yields three purely imaginary eigenvalues. At \(u=1/27\), the sole exceptional choice \(v=8/27\) is the known third-order exceptional point (EP3), and there is no open nonoscillatory window.

The new sharp quantitative assertion is that the nonoscillatory window closes at the EP3 with a \(3/2\)-power cusp:
\[
\boxed{\lim_{u\uparrow1/27}\frac{v_+(u)-v_-(u)}{(1/27-u)^{3/2}}=12.}
\]
Equivalently, the physical width in \(\Gamma/\Lambda\) is asymptotic to \(24(1/27-u)^{3/2}\). Both boundary functions increase strictly in \(u\), with common tangent \(v=2u+2/9\) at the cusp. The eigenvalues generate decaying amplitudes for all positive parameter choices, including the oscillatory regimes; only the oscillatory character changes.

## Assumptions and scope
The statement concerns the finite, exactly specified three-by-three amplitude Hamiltonian
\[
H=\begin{pmatrix}
0&\chi&0\\
\chi&0&\sqrt{\Gamma\Lambda/2}\\
0&\sqrt{\Gamma\Lambda/2}&i\Lambda
\end{pmatrix},\qquad \frac{d}{dt}a(t)=iHa(t),
\]
with real strictly positive \(\chi,\Lambda,\Gamma\). An overall common real frequency shift is irrelevant. The eigenvalue condition uses the convention \(E=i\Lambda y\). The decoupled boundary \(\chi=0\), the limit \(\Gamma=0\), and any claim about reduced-density-matrix Liouvillian eigenvalues beyond these amplitude modes are excluded. The source's matrix is taken exactly as printed, with no appeal to a separate wide-band normalization.

## Proof
**Characteristic cubic.** Direct expansion of \(\det(EI-H)\), followed by \(E=i\Lambda y\), yields the real polynomial
\[
P_{u,v}(y)=y^3-y^2+(u+v)y-u.
\]
The imaginary-axis spectrum condition for \(H\) is precisely that all three zeros of \(P_{u,v}\) be real. Its discriminant is
\[
\Delta(u,v)=v^2+20uv-4u-8u^2-4(u+v)^3.
\]
Three real distinct zeros occur for \(\Delta>0\); a single real zero and one nonreal conjugate pair occur for \(\Delta<0\). This is the standard exhaustive cubic classification.

**All exceptional boundaries.** If a multiple root \(r\) exists, solving \(P(r)=P'(r)=0\) gives exactly
\[
u=r^2(1-2r),\qquad v=2r(1-r)^2.
\]
Because \(u,v>0\), one must have \(0<r<1/2\). The function \(r^2(1-2r)\) increases strictly until \(r=1/3\), decreases strictly thereafter, and has maximum \(1/27\). Thus exactly two candidate bath couplings exist for \(0<u<1/27\), one candidate at the maximum, and none for \(u>1/27\). For fixed positive \(u\), the discriminant is negative at \(v=0\), since \(\Delta(u,0)=-4u(u+1)^2\), and negative for large \(v\). At each exceptional point its transverse derivative is
\[
\left.\frac{\partial\Delta}{\partial v}\right|_{u=r^2(1-2r),\,v=2r(1-r)^2}=-4r(3r-1)^3.
\]
The derivative is positive for \(r_-(u)\) and negative for \(r_+(u)\). These are the **only** positive discriminant zeros, so the discriminant has the claimed negative–positive–negative sign sequence, proving both necessity and sufficiency. At \(u=1/27\), direct factorization gives
\[
\Delta\left(\frac1{27},v\right)=-\frac{(27v-8)^2(108v+49)}{19683},
\]
so the unique zero is \(v=8/27\), with all three roots \(y=1/3\).

**Defectiveness and completeness.** With both subdiagonal entries nonzero, a tridiagonal eigenvector is uniquely determined by its first coordinate: if that coordinate vanished, successive rows would force every coordinate to vanish. Consequently every eigenspace has dimension one. A repeated eigenvalue is therefore genuinely exceptional: double at either simple boundary and triple at the cusp. For any positive \(u,v\), the polynomial \(-P_{u,v}(-z)=z^3+z^2+(u+v)z+u\) meets the strict cubic Routh–Hurwitz conditions \(1>0\), \(u+v>0\), \(u>0\), and \(u+v>u\). Hence every root of \(P\) has positive real part. Under \(\dot a=iHa\), all spectral factors decay, whether oscillatory or not.

**Exact cusp law.** Set \(r=1/3+s\). The exceptional-curve parameterization becomes the exact pair of polynomial identities
\[
u=\frac1{27}-s^2-2s^3,\qquad v=2u+\frac29+6s^3.
\]
For \(\delta=1/27-u\downarrow0\), its two branches satisfy \(s_\pm=\pm\sqrt\delta+O(\delta)\). Therefore
\[
v_\pm(u)=2u+\frac29\pm6\delta^{3/2}+O(\delta^2),
\]
which implies the stated sharp coefficient \(12\). Along either noncusp branch, direct differentiation gives \(dv/du=(1-r)/r>0\). The common limiting slope is \(2\), confirming the cusp tangent.

## Verification
A reproducible standalone script, `checks/check_spectrum.py`, uses exact symbolic expansion of the matrix characteristic polynomial, exact cubic discriminant, exact repeated-root and derivative identities, and the exact polynomial cusp identities. It separately computes finite-dimensional eigenvalues for parameter values inside and outside the claimed window, and checks numerical approach of the rescaled width to \(12\). A successful numerical check illustrates the theorem but is **not** substituted for the proof above. Run `python checks/check_spectrum.py` in a Python environment containing SymPy and NumPy.

## Relationship to prior work
Lin et al., arXiv:2406.18362 (first public version 26 June 2024), introduced this precise effective Hamiltonian, identified the EP3 parameter pair \(u=1/27\), \(v=8/27\), and displayed numerical EP2 and EP3 spectral curves at fixed \(\Gamma\) (arXiv Eq. (28)–(31); published article Fig. 4). Those model, EP3, and qualitative exceptional-curve statements are **prior work**. The specific new mathematical assertion reviewed here is the exact **necessary-and-sufficient global parameter interval at varying bath coupling**, including the complete EP2 endpoint count and the sharp \(3/2\)-cusp width coefficient. It is not a new physical model, a new discovery of the EP3 itself, or a claim that cubic discriminants are novel. Peřina et al., arXiv:2206.14745, gave a more general Heisenberg–Langevin method and explicitly analyzed two physical modes with damping/amplification; its two-mode formulas do not state the present Lorentzian three-amplitude spectral window. The 2025 work of Khandelwal and Blasi on exact Liouvillian exceptional points concerns a dissipative double-quantum-dot system instead. The exact trimer criterion could in principle also be recovered by explicitly solving the source's cubic, so previously unnoticed or unindexed equivalent calculations remain a residual originality risk.

## Limitations
The result is an exact spectral classification for the given **three-by-three amplitude matrix**, not a general assertion about every non-Markovian open system, its density matrix, or operational measures of information backflow. Its boundaries are defective eigenvalue collisions; their spectral conditions alone do not establish an observable quantum information advantage. It does not estimate finite-time state-preparation error, cover additional pseudomodes, or identify a physical dynamical phase transition. The \(3/2\) exponent is a local cusp exponent, not a global scaling law away from the EP3. An independent mathematical and literature audit has not yet been performed.

## References
1. J.-D. Lin, P.-C. Kuo, N. Lambert, A. Miranowicz, F. Nori and Y.-N. Chen, *Non-Markovian Quantum Exceptional Points*, arXiv:2406.18362v1 (26 June 2024), https://arxiv.org/abs/2406.18362; later *Nature Communications* **16**, 1289 (2025), doi:10.1038/s41467-025-56242-w. Especially effective Hamiltonian Eq. (28), EP3 Eq. (29), and Fig. 4.
2. J. Peřina Jr., A. Miranowicz, G. Chimczak and A. Kowalewska-Kudłaszyk, *Quantum Liouvillian exceptional and diabolical points for bosonic fields with quadratic Hamiltonians: The Heisenberg–Langevin equation approach*, arXiv:2206.14745 (2022), *Quantum* **6**, 883 (2022), doi:10.22331/q-2022-12-22-883.
3. S. Khandelwal and G. Blasi, *Emergent Liouvillian exceptional points from exact principles*, arXiv:2409.08100 (2024), *Quantum* **9**, 1944 (2025), doi:10.22331/q-2025-12-15-1944 (different model).
