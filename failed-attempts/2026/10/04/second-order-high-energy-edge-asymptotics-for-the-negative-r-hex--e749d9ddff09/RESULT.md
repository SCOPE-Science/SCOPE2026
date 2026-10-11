# Second-order high-energy edge asymptotics for the negative-\(R\) hexagonal quantum lattice
## Finding
For the equilateral hexagonal quantum graph with edge length \(l>0\), coupling-length scale normalized to one, and the negative-\(R\) preferred-orientation vertex condition of Exner--Pekař, put \(K_m=m\pi/(2l)\). For all sufficiently large \(m\), the two neighboring absolutely-continuous band edges \(E_{m,-}<K_m^2<E_{m,+}\) satisfy: if \(m\) is even, then \(E_{m,q}=K_m^2+q\,4/(\sqrt3\,l)+[-4/(3l^2)-q\,4\sqrt3/(27l)]K_m^{-2}+O(K_m^{-4})\); if \(m\) is odd, then \(E_{m,q}=K_m^2+q\,2/(\sqrt3\,l)+[-1/(3l^2)-q\,2\sqrt3/(27l)]K_m^{-2}+O(K_m^{-4})\), for \(q\in\{-1,1\}\). Thus the neighboring AC-edge separation is \(8/(\sqrt3\,l)-8\sqrt3/(27l)K_m^{-2}+O(K_m^{-4})\) for even \(m\), and \(4/(\sqrt3\,l)-4\sqrt3/(27l)K_m^{-2}+O(K_m^{-4})\) for odd \(m\). For even \(m\), \(K_m^2\) is itself an exact flat-band eigenvalue, so the AC-free neighborhood is split by this spectral point; for odd \(m\) there is no such flat band at the center and the interval between the two edges is a genuine open spectral gap.

## Assumptions and scope
The model is the equilateral periodic hexagonal metric graph of Exner and Pekař with every edge of length \(l>0\) and vertex condition \(U=-R\); the coupling length scale is normalized to one, as in their equilateral calculation. The source's exact positive-energy condition has a flat-band factor \(\sin(kl)\), and its absolutely-continuous part is bounded by
\[
h_+(k)=\frac{1-18k^2+9k^4}{(3k^2+1)^2},\qquad h_-(k)=\frac{1-3k^2}{1+3k^2}.
\]
For \(k>1\), \(h_-(k)<h_+(k)\).

## Proof
Write \(k=K_m+\delta\), \(K_m=m\pi/(2l)\). For even \(m\), the neighboring AC edges solve \(\cos(2l\delta)=h_+(K_m+\delta)\). For odd \(m\), they solve \(-\cos(2l\delta)=h_-(K_m+\delta)\).

Set \(\delta=q aK_m^{-1}+b_qK_m^{-3}+O(K_m^{-5})\), with \(q\in\{-1,1\}\). In the even case, direct expansion of the exact equation gives
\[
0=K_m^{-2}\left(\frac83-2a^2l^2\right)+K_m^{-4}\left(\frac23a^4l^4-4qabl^2-\frac{16}3qa-\frac{16}9\right)+O(K_m^{-6}).
\]
Hence \(a=2/(\sqrt3\,l)\) and \(b_q=-4/(3l^2)-q\,2\sqrt3/(27l)\). Squaring \(K_m+\delta\) gives the stated even energy expansion.

In the odd case, the corresponding expansion is
\[
0=K_m^{-2}\left(2a^2l^2-\frac23\right)+K_m^{-4}\left(-\frac23a^4l^4+4qabl^2+\frac43qa+\frac29\right)+O(K_m^{-6}),
\]
so \(a=1/(\sqrt3\,l)\) and \(b_q=-1/(3l^2)-q\,\sqrt3/(27l)\), yielding the stated odd energy expansion.

After the rescaling \(x=K_m\delta\), the limiting even equation is \(8/3-2l^2x^2=0\) and the limiting odd equation is \(2l^2x^2-2/3=0\). Their relevant roots are simple, so the implicit-function theorem gives unique local branches and the displayed remainders. Subtracting the branches gives the two separation formulas. Finally, \(\sin(K_ml)=\sin(m\pi/2)\) vanishes exactly for even \(m\), proving the flat-band parity statement.

## Verification
The bundled `verify.py` solves the unexpanded boundary equations by bisection for three edge lengths and both parities, and checks the two-term energy approximations across increasing indices. It also checks the center flat-band parity directly. The script prints `VERIFY_OK`. These finite calculations are supplementary; the all-large-index statement follows from the analytic implicit-function argument.

## Relationship to prior work
Exner and Pekař derive the exact determinant, identify the flat bands, and state the leading energy-scale separations \(8/(\sqrt3\,l)+O(m^{-2})\) for even \(m\) and \(4/(\sqrt3\,l)+O(m^{-2})\) for odd \(m\). The claim above resolves the individual edge positions and the coefficient of the first correction. It also makes explicit that an even center is a flat-band spectral point, so the neighboring AC-edge separation is not one spectrum-free interval. The earlier preferred-orientation hexagonal-lattice paper treats \(R\), rather than negative-\(R\), and does not imply these coefficients.

## Limitations
The result is local to the equilateral negative-\(R\) model at positive high energy with the source's normalization. It does not cover the three-length dilated cell, negative energies, the \(R\) coupling, or higher corrections. The later journal version of the motivating work was identified bibliographically; statement-level comparison used the openly accessible arXiv preprint.

## References
1. P. Exner and J. Pekař, *Spectral properties of hexagonal lattices with the negative-\(R\) coupling*, arXiv:2409.03538v1 (2024); later *Reports on Mathematical Physics* 96 (2025), 101--114, DOI:10.1016/S0034-4877(25)00057-6.
2. P. Exner and M. Tater, *Quantum graphs with vertices of a preferred orientation*, arXiv:1710.02664v1 (2017), *Physics Letters A* 382 (2018), 283--287.
