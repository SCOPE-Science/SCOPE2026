# Twelve symmetric phaseless samples determine every complex cubic polynomial

## Finding
Let \(\mathcal P_3\) denote complex polynomials of degree at most three. For
\[
S=\{i^k:k=0,1,2,3\}\;\cup\;\{(1+i)i^k:k=0,1,2,3\}\;\cup\;\{\sqrt3\,i^k:k=0,1,2,3\},
\]
intensities at these twelve points distinguish any two elements of \(\mathcal P_3\) up to multiplication by a constant of modulus one. The three disjoint orbits are squares centered at the origin, of radii \(1\), \(\sqrt2\), and \(\sqrt3\); the middle square is rotated by \(\pi/4\) relative to the other two. The statement applies uniformly to all coefficient vectors, without genericity or nonvanishing assumptions.

More strongly, the real-linear map from Hermitian matrices to their twelve sampled diagonal forms has a four-dimensional nullspace containing no nonzero matrix of rank one or two. Thus there is a constant \(\kappa>0\) (dependent only on these sites) such that for all unit coefficient vectors \(x,y\in\mathbb C^4\), the Euclidean distance between their twelve squared-intensity lists is at least \(\kappa\|xx^*-yy^*\|_F\). The value of the best such constant is not determined.

## Assumptions and scope
For \(a=(a_0,a_1,a_2,a_3)\in\mathbb C^4\), define \(p_a(z)=\sum_{j=0}^3 a_jz^j\). Define \(v(z)=(1,z,z^2,z^3)^T\). On a Hermitian matrix \(H\), define the real-valued linear measurement
\[
\mathcal L_S(H)_z=\sum_{j,k=0}^3 H_{jk}z^j\overline z^{\,k}\quad(z\in S).
\]
For the coefficient column \(a\), \(\mathcal L_S(aa^*)_z=|p_a(z)|^2\) (with the obvious coefficient convention), since the sum is \(\sum a_j\overline{a_k}z^j\bar z^k\). Matrix rank and kernel statements are over the real vector space of Hermitian matrices. The Frobenius norm \(\|\cdot\|_F\) is the square root of the sum of squared entry moduli.

## Proof
**Step 1: determine the complete Hermitian nullspace.** Each square consists of \(z=ri^k e^{i\theta}\) for \(k=0,1,2,3\), with \((r,\theta)=(1,0),(\sqrt2,\pi/4),(\sqrt3,0)\). Take the four-point discrete Fourier transform in \(k\) of \(\mathcal L_S(H)\). These transforms split the Hermitian matrix into the diagonal sector, a complex first-harmonic sector, and a real second-harmonic sector. In the diagonal sector the three constraints are \(\sum_{j=0}^3 H_{jj}r^{2j}=0\) for \(r^2=1,2,3\), so its general solution is \((H_{00},H_{11},H_{22},H_{33})=c(-6,11,-6,1)\), with \(c\in\mathbb R\).

In the first-harmonic sector, use \(w_0=H_{10}\), \(w_1=H_{21}\), \(w_2=H_{32}\), and \(w_3=H_{03}\). The equations are
\[
w_0+xw_1+x^2w_2+x e^{-4i\theta}w_3=0,
\]
for \((x,\theta)=(1,0),(2,\pi/4),(3,0)\). These are three independent complex equations in four complex variables and give \((w_0,w_1,w_2,w_3)=(-12u,15u,-4u,u)\), with \(u\in\mathbb C\). In the real second-harmonic sector the equations are \(\operatorname{Re}(e^{2i\theta}(H_{20}+xH_{31}))=0\); their complete solution is \((H_{20},H_{31})=(-2it,it)\), with \(t\in\mathbb R\). Thus every kernel element is, writing \(u=a+ib\),
\[
H(c,t,a,b)=\begin{pmatrix}
-6c&-12\bar u&2it&u\\
-12u&11c&15\bar u&-it\\
-2it&15u&-6c&-4\bar u\\
\bar u&it&-4u&c
\end{pmatrix},\qquad c,t,a,b\in\mathbb R.
\]
All four parameters are independent and each displayed matrix annihilates all twelve measurements. Therefore \(\operatorname{rank}_{\mathbb R}\mathcal L_S=16-4=12\).

**Step 2: exclude all low-rank Hermitian kernel elements.** Let \(P_{012},P_{013},P_{023},P_{123}\) be the four principal minors of order three. Direct determinant expansion yields
\[
\begin{pmatrix}P_{012}\\P_{013}\\P_{023}\\P_{123}\end{pmatrix}
=\begin{pmatrix}
2214&1440&396&-44\\
-155&48&-66&6\\
102&-32&36&-4\\
-401&-240&-66&6
\end{pmatrix}
\begin{pmatrix}c(a^2+b^2)\\abt\\c^3\\ct^2\end{pmatrix}.
\]
The coefficient matrix has determinant \(6064128\), so vanishing of all four principal minors implies \(c^3=0\) and hence \(c=0\). Under this condition, the full determinant is
\[
\det H(0,t,a,b)=1089(a^2+b^2)^2+11520a^2b^2+132(a^2+b^2)t^2+4t^4.
\]
Every summand is nonnegative and the sum vanishes only for \(a=b=t=0\). Consequently, a kernel matrix of rank at most two (whose principal order-three minors all vanish, and whose determinant vanishes) must be zero.

**Step 3: phase retrieval and stability.** If the intensities of \(p_a\) and \(p_b\) agree, the Hermitian matrix \(aa^*-bb^*\) lies in \(\ker\mathcal L_S\) and has rank at most two. Step 2 forces \(aa^*=bb^*\), which means \(b=\zeta a\) for some \(|\zeta|=1\) (including the case \(a=b=0\)). For stability, consider the compact set of unit-Frobenius-norm differences \((xx^*-yy^*)/\|xx^*-yy^*\|_F\), with unit vectors \(x,y\) and \(xx^*\ne yy^*\), together with its compact closure. Every limit has Hermitian rank at most two, because the rank-at-most-two locus is closed. Step 2 ensures none of these matrices is in the nullspace. Thus the continuous function \(H\mapsto\|\mathcal L_S(H)\|_2\) has a strictly positive minimum on that closure, proving the asserted uniform inverse-Lipschitz bound.

## Verification
The included `check_cubic_squares.py` uses exact algebraic arithmetic with SymPy. It independently constructs all twelve sites, builds all sixteen real Hermitian basis measurements, establishes the rank twelve statement, checks the displayed four-parameter matrices directly at all sites, reconstructs each order-three principal minor and its coefficient matrix, checks its nonzero determinant, and verifies the full determinant polynomial when \(c=0\). Run `python check_cubic_squares.py` in a Python environment with SymPy installed. Its success message reports the sample count, lifting rank, nullity, and exact coefficient determinant. No floating-point experiment is used in the proof or checker.

## Relationship to prior work
Bodmann and Hammen (2013), Theorem 2.3, gave a different structured \(4d-4\)-sample polynomial phase-retrieval construction on two *intersecting* circles, using \(2d-1\) points on one circle and \(2d-3\) on the other, with an irrational-angle condition. Philipp (2014), Theorem 1.1, gave \(4N-4\) measurements by evaluating both the polynomial and its derivative on the unit circle. These prove the general existence of comparably small systems, but neither statement covers the particular three *concentric* square orbits proved here. Grohs, Liehr and Rathmair (first public 2023-08-01) prove phase retrieval from infinite irregular Liouville-type sets in the full Bargmann–Fock space, rather than the present finite-degree, twelve-sample configuration. The new contribution is the exact symmetric sampling design and its Hermitian rank obstruction, not the general concept of finite-dimensional phaseless sampling.

## Limitations
The finding establishes injectivity and existence of a positive stability constant only for complex polynomials of degree at most three and the specified twelve samples. It does not claim that twelve is the fewest possible number of measurements among all complex four-dimensional frames, does not compute the optimal inverse-Lipschitz constant, and does not furnish a noisy reconstruction algorithm. Its historical priority is provisional pending wider specialized literature comparison; generic phase-retrieval theorems may imply the result for many *other* configurations, but do not supply this explicit arithmetic certificate.

## References
1. P. Grohs, L. Liehr, M. Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets*, arXiv:2308.00385, first version 2023-08-01, published in Revista Matemática Iberoamericana 41 (2025), 969–1008.
2. B. G. Bodmann, N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487 (2013), especially Theorem 2.3.
3. F. Philipp, *Phase Retrieval from 4N–4 Measurements*, arXiv:1403.4769 (2014), especially Theorem 1.1 and its comparison with Bodmann–Hammen.
4. A. S. Bandeira, J. Cahill, D. G. Mixon, A. A. Nelson, *Saving phase: Injectivity and stability for phase retrieval*, arXiv:1302.4618 (2013).
5. J. Chalendar, J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255 (2024).
