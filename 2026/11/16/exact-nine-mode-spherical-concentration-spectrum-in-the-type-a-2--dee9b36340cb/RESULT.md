# Exact nine-mode spherical concentration spectrum in the type-\(A_2\) Weyl chamber

## Finding
Let \(\Omega=\{x\in S^2:x_1\ge x_2\ge x_3\}\), and let \(\mathcal H_{\le2}=\mathcal H_0\oplus\mathcal H_1\oplus\mathcal H_2\) be the nine-dimensional real or complex spherical-harmonic space. With normalized area probability measure \(d\mu=d\sigma/(4\pi)\), the Slepian concentration operator \(C=P_{\le2}1_\Omega P_{\le2}\) on \(\mathcal H_{\le2}\) has **nine distinct, positive eigenvalues**, exactly the combined roots of the four explicit matrices below, of sizes four, two, two, and one. In ascending order their unique locations are:

| Sector | Rigorous interval for the eigenvalue |
|---|---|
| \(A\) | \((0.0003408,0.0003412)\) |
| \(B\) | \((0.0005712,0.0005716)\) |
| \(A\) | \((0.0039402,0.0039406)\) |
| \(C\) | \((0.0149137,0.0149143)\) |
| \(D\) | \((0.0288341,0.0288347)\) |
| \(B\) | \((0.1260133,0.1260139)\) |
| \(A\) | \((0.1695605,0.1695611)\) |
| \(C\) | \((0.4562513,0.4562519)\) |
| \(A\) | \((0.6995725,0.6995731)\) |

Consequently the largest captured energy fraction is \(0.699572783770823\ldots\), the least observable mode captures \(0.000340993735104\ldots\), and the exact squared restriction condition number is the ratio of the largest to the smallest eigenvalue, approximately \(2051.57078\); the restriction condition number is approximately \(45.294268754\). Each extreme is simple and invariant under both the reflection interchanging the lune sides and reflection through the equator perpendicular to the chamber axis. The trace is exactly \(3/2\).

## Assumptions and scope
Choose the polar axis \(e=(1,1,1)/\sqrt3\) and rotate azimuth to make the fundamental spherical lune \(\Omega=\{(z,u):-1\le z\le1,-\pi/6\le u\le\pi/6\}\), with \(z=x\cdot e\), and \(d\mu=du\,dz/(4\pi)\). The boundary of the chamber is measure zero. Restriction is from the nine-dimensional complex Hilbert space to \(L^2(\Omega,d\mu)\), with no normalization of \(\mu\) conditioned on the chamber. Use \(\rho=\sqrt{1-z^2}\). The orthonormal real harmonic basis, grouped by \((u,z)\)-reflection parities, is
\[
\begin{aligned}
 A:&\quad 1,\ \tfrac{\sqrt5}{2}(3z^2-1),\ \sqrt3\rho\cos u,\ \tfrac{\sqrt{15}}2\rho^2\cos2u;\\
 B:&\quad \sqrt3\rho\sin u,\ \tfrac{\sqrt{15}}2\rho^2\sin2u;\\
 C:&\quad \sqrt3 z,\ \sqrt{15}z\rho\cos u;\\
 D:&\quad\sqrt{15}z\rho\sin u.
\end{aligned}
\]
Here \(A,B,C,D\) indicate even/even, odd/even, even/odd, odd/odd, respectively. Spherical-harmonic degrees zero, one and two are all included, so the result is not the spectrum on the pure quadratic degree alone.

## Proof
The chamber has azimuthal aperture \(\pi/3\), since the inward normals to the planes \(x_1=x_2\) and \(x_2=x_3\) form an angle of \(2\pi/3\). The chosen basis is orthonormal on the entire sphere by separation of variables and standard Legendre moments. Symmetry makes the Gram matrix \(\langle f_i,1_\Omega f_j\rangle_{S^2}\) a direct sum of four blocks. Direct integration uses
\[
 \int_{-1}^{1}z^{2k}(1-z^2)^{q/2}\,dz=B(k+\tfrac12,q/2+1),
\]
odd powers integrating to zero, together with \(\int_{-\pi/6}^{\pi/6}\cos(mu)\cos(nu)\,du\) and the analogous sine integral. Writing \(p=\pi\), \(s=\sqrt3\), \(t=\sqrt5\), the *exact* four blocks are
\[
 A=\begin{pmatrix}
1/6&0&s/8&t/(4p)\\
0&1/6&-st/64&-1/(4p)\\
s/8&-st/64&1/6+s/(4p)&15t/128\\
t/(4p)&-1/(4p)&15t/128&1/6+s/(8p)
\end{pmatrix},
\]
\[
 B=\begin{pmatrix}1/6-s/(4p)&3t/128\\3t/128&1/6-s/(8p)\end{pmatrix},\qquad
 C=\begin{pmatrix}1/6&3t/32\\3t/32&1/6+s/(4p)\end{pmatrix},\qquad
 D=(1/6-s/(4p)).
\]
The attached verifier recomputes every entry from gamma/beta integrals, proves equality of the explicitly written characteristic polynomials to the determinants, and uses rational interval arithmetic to certify **nine pairwise disjoint sign-changing root brackets** shown above. The \(\pi\) enclosure follows from Machin's identity \(\pi=16\arctan(1/5)-4\arctan(1/239)\) with exact alternating-series errors, and the \(\sqrt3\) enclosure follows by squaring rational endpoints. The four block sizes sum to nine; each sign-changing interval contains an eigenvalue by continuity, while the nine intervals exhaust the algebraic degree. Thus every eigenvalue is simple, the displayed order is certified, the largest and smallest are both in block \(A\), and there are no additional spectrum values. Since \(C\) is the Gram operator of restriction, eigenvalues are squared singular values. Finally, the addition theorem gives \(\mathrm{tr}(C)=\dim(\mathcal H_{\le2})\mu(\Omega)=9/6=3/2\), agreeing with the matrices.

## Verification
Run \(`python verify_lune.py`\) with SymPy installed. This independently reconstructs all four blocks from separated integrals, checks their characteristic equations, and gives exact root enclosures rather than treating floating-point eigenvalues as proofs. The program uses only finite rational arithmetic for its decisive root signs. Approximate eigenvalue values are for exposition; the block matrices and rational intervals provide exact definitions and certified ordering. The sharp condition number is the ratio of the specified extreme block-\(A\) eigenvalues, not a stand-alone decimal assertion.

## Relationship to prior work
Simons, Dahlen and Wieczorek (arXiv:math/0408424, Sections 4 and A.2) formulate Slepian concentration for arbitrary spherical regions, including numerical Gram-matrix integration, but do not state these exact nine eigenvalues for a sixty-degree fundamental chamber. Zandieh, Han and Avron (arXiv:2202.12995v1, Sections 1 and 3) address randomized recovery of low-degree spherical harmonic expansions from uniform full-sphere point samples; their sample-complexity theorem neither computes nor implies this region-restriction condition number. Related numerical methods for arbitrary-region Slepian functions address scalable computation, rather than exact closed block spectra. Previously reported pure degree-two lune concentration and full-band right-angle wedge examples concern inequivalent harmonic subspaces or apertures: none of their stated spectra determines the mixed-degree sixty-degree chamber matrix. The general finite Gram framework provides a method to derive this result but does not itself tabulate its sharp values.

## Limitations
The theorem is for the degree-\(\le2\) band and a single exact sixty-degree lune, not arbitrary bandwidths or apertures. Its condition number is for noisily observed *continuous* restriction and uniform whole-sphere normalization, not arbitrary discrete sampling. Exact algebraic-looking values involve \(\pi\), and hence are defined as roots of the displayed real coefficient matrices rather than algebraic numbers over \(\mathbb Q\). Historical originality is assessed against the cited sources and records, not guaranteed by a search, and independently organized mathematical validation has not occurred.

## References
1. F. J. Simons, F. A. Dahlen, M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (31 August 2004), https://arxiv.org/html/math/0408424v1.
2. A. Zandieh, I. Han, H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995v1 (25 February 2022), https://arxiv.org/html/2202.12995v1.
3. A. P. Bates, Z. Khalid, R. A. Kennedy, *Efficient Computation of Slepian Functions for Arbitrary Regions on the Sphere*, arXiv:1608.05479v1 (19 August 2016), https://arxiv.org/abs/1608.05479.
