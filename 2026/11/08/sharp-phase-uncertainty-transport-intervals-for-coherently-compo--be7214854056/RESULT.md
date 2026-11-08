# Sharp phase-uncertainty transport intervals for coherently composed quantum-walk coins

## Finding

Fix an integer \(n\geq 2\). For each \(i=1,\ldots,n\), suppose the transport vector \(T_i\) of an independently operated, homogeneous one-dimensional, two-state discrete-time quantum walk has been calibrated, but the corresponding unitary coin \(C_i\) is not otherwise known. Allow every choice of coins with precisely these calibrated transport vectors, and combine the coins *inside one walk step* as \(C=C_n\cdots C_1\), followed by the conditional lattice shift. The object classified here is the maximal magnitude \(M(C)\) of the limiting mean drift over pure initial coin states; it is not the drift for one prescribed initial state, nor the transport of alternating full walk steps.

Let \(z_i=(T_i)_z\in[0,1]\) and define their polar angles
\[
\delta_i=2\arcsin(1-z_i)\in[0,\pi].
\]
Starting from \(L_1=U_1=\delta_1\), form the following *exact closed-interval recursion*, for \(j=2,\ldots,n\):
\[
L_j=\operatorname{dist}\bigl(\delta_j,[L_{j-1},U_{j-1}]\bigr),\qquad
U_j=\pi-\operatorname{dist}\bigl(\pi-\delta_j,[L_{j-1},U_{j-1}]\bigr),
\]
where \(\operatorname{dist}(x,[L,U])=\max\{L-x,0,x-U\}\). Put
\[
F(h)=\sqrt{\frac{1-\sin(h/2)}{1+\sin(h/2)}}\quad(0\leq h\leq\pi).
\]
**The exact attainable set is**
\[
\boxed{\{M(C_n\cdots C_1):T(C_i)=T_i\text{ for every }i\}=[F(U_n),F(L_n)].}
\]
Every value in this interval occurs; both endpoints are attained. In particular, complete ballistic transport \(M=1\) is possible exactly when \(L_n=0\), whereas zero maximal mean drift \(M=0\) is possible exactly when \(U_n=\pi\). The recursion takes \(O(n)\) arithmetic and elementary-function operations, independent of the orientations of the calibrated vectors.

For three coins the first two have \([L_2,U_2]=[|\delta_1-\delta_2|,\min\{\delta_1+\delta_2,2\pi-\delta_1-\delta_2\}]\). Hence \(M=1\) is attainable exactly when \(\delta_3\in[L_2,U_2]\), and \(M=0\) exactly when \(\pi-\delta_3\in[L_2,U_2]\). If all three angles are \(\pi/2\), every maximal drift magnitude in \([0,1]\) is attainable while all three individual full transport vectors remain fixed.

## Assumptions and scope

A homogeneous coined walk on \(\mathbb Z\) has one-step operator \(U=S C\), where \(C\) is a unitary \(2\times2\) coin acting on the internal qubit and \(S\) shifts the two internal states in opposite lattice directions. Its initial walker position is localized. Up to a physically irrelevant scalar phase, the coin is written
\[
C=\begin{pmatrix}a&b\\-\overline b&\overline a\end{pmatrix},\qquad |a|^2+|b|^2=1.
\]
The calibrated transport vector is the long-time ballistic transport vector from de Leon–Pérez-Muralles–Neuser–Pineda [1], in the source's coin conventions:
\[
T(C)=\frac{\bigl(\operatorname{Re}(b\overline a),-\operatorname{Im}(b\overline a),|a|^2\bigr)}{1+|b|},\qquad \lim_{t\to\infty}\frac{\mathbb E[X_t]}{t}=T(C)\cdot r,
\]
with \(r\) the Bloch vector of an initial coin state. The displayed formula is taken from [1] rather than claimed here as new. Degenerate diagonal and antidiagonal coins are included by continuous endpoint interpretation.

The uncertainty set consists of all independent choices \(C_i\in U(2)\) with \(T(C_i)=T_i\), with no relations imposed among their unmeasured overall or left diagonal phases. The coherent composition \(C_n\cdots C_1\) is performed before *one* shift, and does not mean time-periodic alternation of the operators \(S C_i\). The maximal drift \(M(C)=\sup_{\|r\|=1}|T(C)\cdot r|\) is an observable attainable when the initial state can be selected; the theorem does not quantify all fixed-state drift vectors or finite-time propagation.

## Proof

**1. Calibration fibers.** Write \(s=|b|\) and \(c=|a|\). The source transport formula gives \(T_z=|a|^2/(1+s)=(1-s^2)/(1+s)=1-s\), including \(s=1\) by continuity. Thus \(s=1-T_z\) and the off-diagonal polar angle is \(\delta=2\arcsin s\). When \(0<s<1\), the transverse components of \(T\) fix the complex number \(b\overline a\), hence the relative argument of \(b\) and \(a\). The only remaining \(SU(2)\) freedom is a common phase on the first row:
\[
C\longmapsto Z(\phi)C,\qquad Z(\phi)=\operatorname{diag}(e^{i\phi},e^{-i\phi}).
\]
When \(s\) equals \(0\) or \(1\), the same description holds because the single nonzero top-row entry has one free argument. In \(U(2)\), an additional overall phase does not change transport. Therefore the entire calibration fiber is exactly the stated left-\(Z\) circle (up to overall phase), rather than merely containing it.

**2. The one-step angular interval.** Write any present product in the standard form with coefficients \(u,v\), and let \(\theta=2\arcsin|v|\in[0,\pi]\). A new factor has \(|a|=\cos(\delta/2)\) and \(|b|=\sin(\delta/2)\). The crucial independent control is the *previous* outermost left phase: if a previous product \(P\) achieves polar angle \(\theta\), adjusting the left-\(Z\) phase of its outermost constituent replaces it by \(Z(\chi)P\) without changing \(\theta\) or any calibrated \(T_i\). In \(C_{j}Z(\chi)P\), the two complex contributions to the upper-right entry have magnitudes \(\cos(\delta/2)\sin(\theta/2)\) and \(\sin(\delta/2)\cos(\theta/2)\); their relative argument may take any angle. Equivalently, for a freely chosen \(\psi\in[0,2\pi]\),
\[
\cos\theta'=\cos\theta\cos\delta-\sin\theta\sin\delta\cos\psi.
\]
The complete interval of accessible \(\theta'\) at a fixed \(\theta\) is therefore
\[
\bigl[|\theta-\delta|,\;\pi-|\pi-(\theta+\delta)|\bigr].
\]
The identity still holds at every endpoint because the phase contribution that vanishes does not affect the angle.

**3. Induction on composition length.** Assume the reachable prior angles form the full interval \([L,U]\). Every \(\theta\in[L,U]\) has a realization by the induction hypothesis, and the left phase of its outermost factor remains free; it independently controls the next multiplication without changing the previously realized angle. The new angle is a continuous function of the previous phases and this new phase; the domain of all phases is a connected compact torus. Its image in \([0,\pi]\) must be a closed interval. The smallest possible angle is
\[
\min_{\theta\in[L,U]}|\theta-\delta|=\operatorname{dist}(\delta,[L,U]),
\]
and the largest is
\[
\max_{\theta\in[L,U]}\{\pi-|\pi-(\theta+\delta)|\}
=\pi-\operatorname{dist}(\pi-\delta,[L,U]).
\]
Hence the recursion gives the exact interval, with extrema realized by compactness; this proves the assertion for all integers \(n\ge2\). The application order of the individual coins does not change this scalar interval, though it can change the composite vector's direction.

**4. Conversion from angle to transport magnitude.** Using \(|a|^2=1-s^2\) and \(|b\overline a|^2=s^2(1-s^2)\) in the source formula,
\[
\|T(C)\|^2=\frac{s^2(1-s^2)+(1-s^2)^2}{(1+s)^2}
=\frac{1-s}{1+s}.
\]
Since \(s=\sin(\theta/2)\), it follows that \(M(C)=F(\theta)\). The function \(F\) is continuous, strictly decreasing on \([0,\pi]\), and satisfies \(F(0)=1\), \(F(\pi)=0\). Applying it to the exact angular interval proves the claimed full speed interval, its attainable extrema and both endpoint tests.

**5. Three-coin boundary.** The two-coin interval is the single-angle formula with \(\theta=\delta_1\). The third update has lower endpoint zero precisely when \(\delta_3\) lies in that two-coin interval, and upper endpoint \(\pi\) precisely when \(\pi-\delta_3\) lies there. At three balanced angles, the second interval is \([0,\pi]\), so the third remains \([0,\pi]\). This completes the proof.

## Verification

The standalone standard-library script `verify.py` directly constructs \(SU(2)\) matrices and transport vectors; checks invariance of every calibrated vector under the left-\(Z\) phase; computes products for randomly chosen phases and verifies their polar angles satisfy the recursion; validates the transport-magnitude identity; and checks that numerical two- and three-coin phase grids approach the predicted attainable extrema. Run with `python3 verify.py` in the extracted package. The checked script completed 16,593 diagnostics. These tests are finite diagnostics and are not substitutes for the connected-image induction proof.

## Relationship to prior work

The transport-vector formula, the separation of initial-state dependence and coin dependence, and the distinction between coin composition and step alternation all belong to [1]. The observation that left diagonal rotations leave an isolated transport vector invariant also appears in [1]. The new target here is different: given *all* the isolated transport vectors but not the individual coins, characterize **the full range of maximum ballistic speeds of an arbitrarily long product**, including sharp attainable endpoint thresholds and an \(O(n)\) closed-interval algorithm. No previous formula for these exact calibration-constrained intervals was found in the inspected primary sources; this is a comparison, not a claim of exhaustive priority.

Variable-phase composite \(SU(2)\) rotations and target transition probabilities are already studied in [2], so phase steering is not claimed as a new phenomenon. Work [2] constructs robust fixed-target pulse sequences, but does not state the calibration-invariant, all-sequence-length drift envelope above. The result is a specialized application of elementary \(SU(2)\) geometry to a physically meaningful observable. A broader pre-existing reachable-rotation or composite-pulse theorem could independently imply the angular recursion without using its transport language.

## Limitations

Only the homogeneous two-internal-state, one-dimensional walk and **coherent coin multiplication before each shift** are covered. The source-derived ballistic formula presumes localized initial position and the specified shift convention. The theorem concerns the *maximum over initial qubit states* and does not claim the same interval for any fixed Bloch vector, finite-time mean or step-alternating protocol. The phase freedom is essential: external constraints coupling unobserved phases across coins can narrow the reachable set. The relation to general spherical-polygon and composite-pulse reachability theorems is a residual originality risk; independent expert validation and publication-priority checking are not performed.

## References

[1] J. A. de Leon, M. Pérez-Muralles, J. Neuser, C. Pineda, *The Geometry of Transport in Quantum Walks and Parrondo's Paradox*, arXiv:2609.09269 (first public 2026-09-08), https://arxiv.org/abs/2609.09269.

[2] B. T. Torosov and N. V. Vitanov, *Arbitrarily accurate variable rotations on the Bloch sphere by composite pulse sequences*, arXiv:1810.03833 (first public 2018-10-09), https://arxiv.org/abs/1810.03833.
