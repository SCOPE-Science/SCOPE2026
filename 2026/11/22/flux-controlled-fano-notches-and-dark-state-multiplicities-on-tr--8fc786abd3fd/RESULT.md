# Flux-controlled Fano notches and dark-state multiplicities on triangular bouquets

## Finding
Let a unit-hopping infinite tight-binding wire be side-coupled at one vertex to the hub of a bouquet of \(m\) identical magnetic triangles, with \(m\geq1\). Each triangle has unit hoppings, the common edge phase is \(e^{i\phi}\), and all onsite energies vanish. With \(c=\cos\phi\in(-1,1)\), define
\[
F_m(E,c)=E^3-(2m+1)E-2mc.
\]
For every propagating energy \(-2<E<2\), the exact transmission probability (under continuous extension at isolated exceptional energies) is
\[
\mathcal T_m(E,\phi)=\frac{(4-E^2)F_m(E,c)^2}{(4-E^2)F_m(E,c)^2+(E^2-1)^2}.
\]
Exactly two interior energies, \(E=-1,+1\), have perfect transmission. Every perfect-reflection energy is a real root of \(F_m\) inside the open band. Their complete number is three if \(m=1\); it is two if \(m=2\) and \(|c|>1/2\), and one if \(m=2\) and \(|c|\leq1/2\); it is **exactly one for all \(m\geq3\)**. For \(m=2\) the additional reflection root is negative when \(c>1/2\) and positive when \(c<-1/2\). At \(|c|=1/2\) it lies at a band edge and is not counted. Thus three loops are the smallest number ensuring one and only one in-band Fano notch at every nontrivial flux.

For every \(0<\phi<\pi\), the wire-plus-bouquet operator has exactly \(m-1\) square-summable embedded eigenfunctions at \(E=1\) and \(m-1\) at \(E=-1\), each supported only on the pendant pairs. At the zero-flux endpoint their multiplicities are respectively \(m-1\) and \(m\); at the half-flux endpoint they are \(m\) and \(m-1\). For \(m\geq3\), neither endpoint flux has an interior perfect-reflection energy.

For fixed \(m\geq3\), as \(\phi\downarrow0\), set \(\varepsilon=1-\cos\phi\). The unique interior reflecting energy satisfies
\[
E_*(\phi)=-1+\frac{m}{m-1}\varepsilon+O_m(\varepsilon^2).
\]
At \(E=-1+s\varepsilon\), the reflection probability converges for fixed real \(s\) to the *asymmetric* Fano profile
\[
\mathcal R_{m}(s)=\frac{s^2}{s^2+3[m-(m-1)s]^2}.
\]
The two local half-reflection points are
\[
E_{\pm}=-1+\frac{m\varepsilon}{m-1\mp1/\sqrt3}+O_m(\varepsilon^2),
\]
where the minus subscript corresponds to the plus sign in the denominator. Their full separation is
\[
E_+-E_-=\frac{m}{\sqrt3[(m-1)^2-1/3]}\phi^2+O_m(\phi^4).
\]
The limiting right-to-left half-width ratio is
\[
\frac{m-1+1/\sqrt3}{m-1-1/\sqrt3}>1.
\]
In particular, the coefficient of \(\phi^2\) in the full local width is asymptotic to \(1/(\sqrt3m)\) as the number of triangles tends to infinity.

## Assumptions and scope
The single-particle Hamiltonian is the bounded self-adjoint weighted adjacency operator on vertices \(\mathbb Z\cup\{h,a_j,b_j:1\leq j\leq m\}\). On the wire, \(H_{k,k+1}=H_{k+1,k}=1\). Its contact is \(H_{0h}=H_{h0}=1\). For each triangle \(j\), put \(H_{h a_j}=H_{a_j h}=1\), \(H_{h b_j}=e^{i\phi}\), \(H_{b_j h}=e^{-i\phi}\), and \(H_{a_j b_j}=H_{b_j a_j}=1\). All other entries vanish. Every integer \(m\geq1\) is admissible. Magnetic flux is characterized by \(\cos\phi\), with \(0<\phi<\pi\) for the generic-flux claims; the endpoint comparisons use \(\phi=0,\pi\). Units fix the hopping and wire-band half-width; all transmissions are stationary, elastic, one-channel probabilities, not thermodynamic transport coefficients. The phrase half-width refers only to the two half-reflection points converging to the weak-flux notch, not to all half-reflection points in the band.

## Proof
For \(E\neq\pm1\), the two peripheral amplitudes of each triangle solve the linear system with coefficient matrix \(\begin{pmatrix}E&-1\\-1&E\end{pmatrix}\). The hub-to-pair coupling vector is \((1,e^{i\phi})\). A Schur complement therefore contributes
\[
\frac{(1,e^{i\phi})\begin{pmatrix}E&1\\1&E\end{pmatrix}(1,e^{i\phi})^*}{E^2-1}=\frac{2(E+\cos\phi)}{E^2-1}
\]
to the hub self-energy. Summing \(m\) identical copies gives \(\Sigma(E)=2m(E+c)/(E^2-1)\). Eliminating the hub yields a single energy-dependent wire-site potential
\[
V(E)=\frac1{E-\Sigma(E)}=\frac{E^2-1}{E^3-(2m+1)E-2mc}.
\]
The one-dimensional wire ansatz with incoming wave \(e^{ikx}\), \(E=2\cos k\), has transmission amplitude \(t(E)=2i\sin k/(2i\sin k+V(E))\). Taking squared modulus proves the displayed rational formula; its continuous extension settles the isolated energies. For \(|c|<1\), \(F_m(-1,c)=2m(1-c)>0\) and \(F_m(1,c)=-2m(1+c)<0\), so no zero of \(F_m\) occurs at \(\pm1\); hence precisely these two energies have transmission one. In the open band a zero of transmission is exactly a zero of \(F_m\).

The endpoint evaluations are
\[
F_m(-2,c)=4m-6-2mc,\qquad F_m(2,c)=6-4m-2mc.
\]
For \(m=1\), their signs and those at \(\pm1\) give three disjoint intervals each containing a root, namely \((-2,-1)\), \((-1,1)\), and \((1,2)\). For \(m=2\), the negative outer root is in the band precisely when \(c>1/2\); the positive outer root is in the band precisely when \(c<-1/2\). At equality it is at \(\pm2\). For \(m\geq3\), \(F_m(-2,c)>0\) and \(F_m(2,c)<0\) for \(-1<c<1\), while \(F_m(E,c)\to\mp\infty\) as \(E\to\mp\infty\); one root is strictly below \(-2\), one lies in \((-1,1)\), and one lies strictly above \(2\). Cubic degree makes these lists exhaustive; all three roots are simple by their interval separation. This also proves uniqueness of the interior notch.

An embedded \(\ell^2\) eigenfunction with \(-2<E<2\) vanishes identically on the free wire, since the homogeneous second-order lead recurrence has only oscillatory nondecaying solutions. The equation at wire site zero then forces hub amplitude zero. Each peripheral pair must consequently be an eigenvector of the dimer adjacency matrix, whose only eigenvalues are \(\pm1\). At \(E=1\) pair amplitudes have \(a_j=b_j\); the hub equation imposes \((1+e^{i\phi})\sum_j a_j=0\). At \(E=-1\), \(a_j=-b_j\), and the condition is \((1-e^{i\phi})\sum_j a_j=0\). Thus the respective kernels each have dimension \(m-1\) at generic flux and rise to \(m\) only when the relevant prefactor vanishes. There are no other embedded eigenvalues. At \(c=1\) the factorization \(F_m=(E+1)(E^2-E-2m)\), and at \(c=-1\), \(F_m=(E-1)(E^2+E-2m)\), show after the removable factor is canceled in \(V\) that for \(m\geq3\) neither endpoint produces an interior pole; at \(m=3\) a remaining pole may sit at the band edge only.

For weak positive flux, set \(E=-1+s\varepsilon\), \(\varepsilon=1-c\). Direct expansion yields
\[
F_m(E,c)=2\varepsilon[m-(m-1)s]-3s^2\varepsilon^2+s^3\varepsilon^3,\quad E^2-1=-2s\varepsilon+s^2\varepsilon^2.
\]
The simple central root is at \(s=m/(m-1)+O_m(\varepsilon)\) by the implicit function theorem. Substitution into the exact transmission formula, using \(4-E^2=3+O(\varepsilon)\), gives the stated limiting reflection function. The limiting function has a unique interior maximum one at the central pole, vanishes at \(s=0\), and crosses \(1/2\) transversely at \(s_-=m/(m-1+1/\sqrt3)\) and \(s_+=m/(m-1-1/\sqrt3)\). The implicit function theorem justifies the two expansions of the local half-reflection points. Their difference, followed by \(\varepsilon=\phi^2/2+O(\phi^4)\), proves the full-width coefficient and the strictly asymmetric right-to-left half-width ratio. The final large-\(m\) asymptotic is elementary.

## Verification
Run `python3 verify.py`. The supplied standard-library checker independently solves the full \((2m+1)\)-dimensional internal scattering system with complex Gaussian elimination at specified energies and compares it with the reduced rational transmission formula. It checks the reflection-root endpoint signs for \(m=1,2,3,4,5,8\), numerically tests the weak-flux center and half-width expansions for \(m=3,4,5,9\), and verifies the elementary kernel-rank conditions for embedded states, totaling 345 assertions. The recorded run printed `ALL_CHECKS_PASSED 345`. The analytic cubic sign argument and hub/dimer kernel proof, not finite sampling, establish the infinite-family statements.

## Relationship to prior work
Bound states in the continuum and flux-controlled Fano line shapes are established phenomena. Ladrón de Guevara and Orellana (2005) study parallel-coupled quantum-dot molecules and molecular dark-state symmetry, including arrays; their lead topology and spectra are different. Bulgakov et al. (2006) examine open Aharonov–Bohm rings with isolated BIC flux/energy points. Chakrabarti (2006) studies Fibonacci side chains attached to a quantum wire; Szafran and Poniedziałek (2010) study a finite-width continuous side ring. Those mechanisms motivate the question but the investigated claims do not give the exact single-contact common-hub \(m\)-triangle reflection-zero census, flux-persistent pairwise embedded eigenspaces, and asymmetric \(m\)-dependent weak-flux half-widths. The current result uses elementary Schur reduction; its precise new object is the all-size joint classification, not the general Fano or BIC mechanisms.

## Limitations
This is a noninteracting one-particle discrete graph model with equal triangle weights and coherent uniform flux. It does not describe arbitrary ring geometries, disorder, electron-electron interactions, decoherence, or finite-width wires. The original priority of the exact bouquet specialization cannot be conclusively established from accessible literature alone. No many-body or thermodynamic phase transition is asserted. The asymptotics hold at each fixed \(m\) as \(\phi\to0\); exchanging that limit with \(m\to\infty\) is not proved. The local half-reflection points are not asserted to be the only half-reflection points in the entire propagation band.

## References
1. M. L. Ladrón de Guevara and P. A. Orellana, “Electronic transport through a parallel-coupled triple quantum dot molecule: Fano resonances and bound states in the continuum,” 2005, https://arxiv.org/abs/cond-mat/0508727 (first public 2005-08-30).
2. E. N. Bulgakov, K. N. Pichugin, A. F. Sadreev, and I. Rotter, “Bound states in the continuum in open Aharonov–Bohm rings,” 2006, https://arxiv.org/abs/cond-mat/0610197.
3. A. Chakrabarti, “Electronic transmission in a model quantum wire with side coupled quasiperiodic chains: Fano resonance and related issues,” 2006, https://arxiv.org/abs/cond-mat/0609082.
4. B. Szafran and M. R. Poniedziałek, “Tuning Fano resonances by magnetic forces for electron transport through a quantum wire side-coupled to a quantum ring,” 2010, https://arxiv.org/abs/1010.1118.
