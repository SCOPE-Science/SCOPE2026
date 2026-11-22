# A logarithmic critical-flip clock in a three-dimensional sinusoidal recurrence

## Finding
Let \(0<b\le 1/2\) and consider the smooth real map
\[
F_b(x,y,z)=(y,\sin z,\,b(x+y)-\sin z).
\]
The origin is locally asymptotically stable even though the derivative has the neutral eigenvalue \(-1\). There is a local two-dimensional strong-stable manifold \(W^{ss}_b\), tangent to the eigenspaces with eigenvalues \(\pm\sqrt b\). For each sufficiently small initial triple outside \(W^{ss}_b\), define the *physical* signed critical amplitude
\[
U_n=\frac{z_n-bx_n}{1-b}.
\]
Then \(U_n\ne0\) for all sufficiently large \(n\), and a finite orbit-dependent real constant \(C\) satisfies
\[
\boxed{\frac1{U_n^2}=\frac{n}{3(1-b)}+\frac{9b^2+7b+4}{20(1-b)^2}\log n+C+o(1).}
\]
In particular \(nU_n^2\to3(1-b)\). Every sufficiently small initial triple on \(W_b^{ss}\) converges exponentially, as opposed to the generic alternating algebraic relaxation. Moreover, \(z_n=U_n+O(U_n^3)+O(\vartheta^n)\) for some \(\vartheta\in(0,1)\), so \(nz_n^2\to 3(1-b)\) for the non-strong-stable trajectories.

## Assumptions and scope
The parameter \(b\) is fixed in \((0,1/2]\); initial data are arbitrary real triples sufficiently close to the origin, and the clock is in integer map iterations. The precise local neighborhood can depend on \(b\). No assertion is made about the global basin, distant equilibria or nonlocal periodic orbits. The strong-stable exceptional manifold is defined by local invariant-manifold theory; it is not identified with a coordinate plane.

The map is the zero-translation, no-self-feedback, equal-linear-coupling specialization of the three-dimensional sine map studied in the cited literature, including the exact fixed-sine-coefficient map of Mammeri (2017). The primary MSC is \(37C75\).

## Proof
**1. Spectrum and coordinates.** At the origin,
\[
J_b=\begin{pmatrix}0&1&0\\0&0&1\\b&b&-1\end{pmatrix},\qquad
\det(\lambda I-J_b)=(\lambda+1)(\lambda^2-b).
\]
The right \(-1\) eigenvector is \(e=(1,-1,1)^T\), and the left eigenfunctional normalized by \(\ell e=1\) is \(\ell(x,y,z)=(z-bx)/(1-b)\). The remaining eigenvalues are \(\pm\sqrt b\) of modulus at most \(1/\sqrt2\). Thus a one-dimensional smooth center manifold, a local strong-stable manifold of dimension two, and exponential stable fibers exist. The odd symmetry \(F_b(-X)=-F_b(X)\) permits an odd local center-manifold parameterization with \(\ell H(u)=u\).

**2. Fifth-order center reduction.** Write
\[
H(u)=eu+c_3u^3+c_5u^5+O(u^7),\quad
f(u)=-u+a u^3+d u^5+O(u^7),\quad F_b(H(u))=H(f(u)).
\]
Comparison of cubic coefficients, with \(\ell c_3=0\), gives
\[
a=\frac1{6(1-b)},\qquad
c_3=\frac1{6(1-b)^2}\begin{pmatrix}1+b\\-2b\\b(1+b)\end{pmatrix}.
\]
Comparison of quintic coefficients with \(\ell c_5=0\) gives
\[
d=\frac{9b^2+12b-1}{120(1-b)^3},
\quad c_5=\frac1{120(1-b)^4}\begin{pmatrix}
9b^3+21b^2+41b+9\\
-2b(9b^2+17b+14)\\
b(9b^3+21b^2+41b+9)
\end{pmatrix}.
\]
These identities follow directly from \(\sin u=u-u^3/6+u^5/120+O(u^7)\) and can be reproduced by the included symbolic checker.

**3. Critical attraction and reciprocal clock.** Since \(a>0\),
\[
f(f(u))=u-2a u^3+O(u^5),
\]
so zero attracts locally in the center direction. The uniformly contracting stable directions then imply local asymptotic stability of the three-dimensional origin. For nonzero small center orbits, eventually \(f(u)/u<0\), \(|f(u)|<|u|\), and \(|u_n|\to0\). Squaring yields
\[
 u_{n+1}^2=u_n^2-2a u_n^4+(a^2-2d)u_n^6+O(u_n^8).
\]
Writing \(v_n=u_n^{-2}\), inversion gives
\[
v_{n+1}=v_n+2a+\frac{3a^2+2d}{v_n}+O(v_n^{-2}).
\]
First, \(v_n=2an+O(\log n)\) by summation. Then
\[
\sum_{k<n}\frac1{v_k}=\frac{\log n}{2a}+C_1+o(1),
\]
and the \(O(v_k^{-2})\) errors are summable. Consequently,
\[
v_n=2an+\frac{3a^2+2d}{2a}\log n+C_2+o(1).
\]
Substitution of the explicit \(a,d\) gives \(2a=1/[3(1-b)]\) and \((3a^2+2d)/(2a)=(9b^2+7b+4)/[20(1-b)^2]\).

**4. General initial triples.** The local strong-stable foliation exponentially shadows a center-manifold orbit. Off the strong-stable leaf through the origin, the shadowing center orbit is nonzero and obeys the reciprocal law. Since its amplitude is of order \(n^{-1/2}\), exponentially small shadowing errors change its reciprocal square by \(o(1)\), and hence preserve the linear term, logarithmic term and existence of a finite remainder constant for the actual amplitude \(U_n=\ell(X_n)\). On the exceptional strong-stable leaf the orbit decays exponentially. Because the third component of \(H(u)\) equals \(u+O(u^3)\), the asserted limit for \(z_n\) follows.

## Verification
The accompanying `verify.py` reconstructs the cubic and quintic invariance equations using exact rational-symbolic algebra, verifies \(\ell H(u)=u\), checks the reciprocal-clock coefficients, and runs finite trajectory diagnostics for rational sample parameters. The identities, not the finite trajectories, establish the asymptotics. Run `python verify.py` with Python and SymPy installed; no other assets are required.

## Relationship to prior work
Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps* (published January 12, 2017), treats the exact sine-coefficient map, gives boundedness and strict spectral stability conditions, and supplies numerical dynamics. The present parameter slice is the equal-coupling critical \(-1\) spectral boundary and requires a nonlinear fifth-order calculation, not a strict-Schur stability inequality. Rajagopal et al. (2023) include the map as a specialization of a self-feedback family and study numerical dynamical transitions. Almatroud et al. (2024) examine fixed-point stability and multistability in a related sine-delay family.

A previously indexed finding on the same general sine-delay map classifies primitive two-cycles and their nilpotent special locus. It does not give this fixed-point logarithmic relaxation law. Classical center-manifold and stable-foliation theorems justify the reduction and shadowing; these general theorems are credited rather than claimed new.

## Limitations
The theorem is local, holds for a fixed \(b\in(0,1/2]\), and says nothing about global attraction or dynamics outside a small neighborhood. The strong-stable manifold is given existentially, not by an explicit global formula. The expansion is asymptotic and its remainder constant depends on the initial triple. Source comparison cannot exclude equivalent unpublished or unindexed work. Independent verification has not been performed.

## References
1. M. Mammeri, *Symmetry and Periodic-Chaos in 3-D Sinusoid Discrete Maps*, Bulletin of Mathematical Analysis and Applications 9(1) (2017), 1–8. Published 2017-01-12. https://emis.muni.cz/journals/BMAA/repository/docs/BMAA9-1-1.pdf
2. K. Rajagopal, S. Kanagaraj, C. Volos and A. Karthikeyan, *Influence of Parametric Symmetry on the Dynamics of 3D Sinusoidal Discrete Systems*, Symmetry 15 (2023), 780. Published 2023-03-23. https://doi.org/10.3390/sym15040780
3. O. A. Almatroud and collaborators, *Multistability, Chaos, and Synchronization in Novel Symmetric Difference Equation*, Symmetry 16 (2024), 1093. Published 2024-08-22. https://doi.org/10.3390/sym16081093
4. Standard smooth center-manifold and strong-stable foliation results for finite-dimensional discrete dynamical systems (used as general theory; no new theorem of that theory is asserted).
