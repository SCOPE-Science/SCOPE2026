# An exact 4–3–1 spectral reduction for quadratic polynomial concentration in a ball orthant

## Finding
Let \(d\ge4\) be an integer and put
\[
B_d=\{x\in\mathbb R^d:\|x\|\le1\},\qquad
Q_d=\{x\in B_d:x_j\ge0\text{ for }1\le j\le d\}.
\]
Let \(\mu_d\) be normalized Lebesgue measure on \(B_d\), and let \(\mathcal P_{\le2}(B_d)\) denote complex polynomials of total degree at most two, restricted to the ball. Define the Hermitian concentration operator by
\[
\langle T_df,g\rangle_{B_d}=\int_{Q_d}f(x)\overline{g(x)}\,d\mu_d(x).
\]
The following gives its **entire spectrum in every dimension**, with generalized eigenvalue problems of sizes at most four.

Write \(s=\sum_{j=1}^d x_j\), \(r=\sum_{j=1}^d x_j^2\), and \(e=\sum_{i<j}x_ix_j\). Introduce the polynomial lists
\[
U_0=(1,s,r,e),\quad
U_1=(x_1-x_2,\ x_1^2-x_2^2,\ (x_1-x_2)\sum_{j=3}^d x_j),
\quad U_2=((x_1-x_4)(x_2-x_3)).
\]
For any list \(U=(u_1,\ldots,u_k)\), define \(G_B(U)_{ij}=\int_{B_d}u_i\overline{u_j}\,d\mu_d\) and \(G_Q(U)_{ij}=\int_{Q_d}u_i\overline{u_j}\,d\mu_d\). Define \(\Lambda(U)\) as the multiset of generalized eigenvalues of \(G_Q(U)v=\lambda G_B(U)v\). All these Gram matrices are explicitly computable using the moment formula in the proof.

**Theorem.** For every integer \(d\ge4\), the eigenvalue multiset of \(T_d\) is exactly
\[
\boxed{\quad
\Lambda(U_0)\;\uplus\;(d-1)\Lambda(U_1)\;\uplus\;
\left\{2^{-d}\left(1-\frac{2}{\pi}\right)^2\right\}^{[d(d-3)/2]} .\quad}
\]
Here \((d-1)\Lambda\) repeats each eigenvalue \(d-1\) times, and brackets indicate multiplicity. The final scalar comes from the entire irreducible edge-difference sector, not merely from one trial polynomial. Coincident eigenvalues from different blocks have additive multiplicities. Thus the exact sharp minimum and maximum of the concentration quotient are the smallest and largest numbers among only eight generalized-eigenvalue roots and the displayed scalar, regardless of \(d\).

The trace identity is
\[
\operatorname{tr}(T_d)=2^{-d}\binom{d+2}{2}.
\]
All eigenvalues lie strictly between zero and one. For example, for \(d=4\), the sharp extremes numerically are \(0.0000793986560408\ldots\) and \(0.483477188673\ldots\); the region occupies only \(1/16\) of the ball. These decimals are illustrations, not definitions of the sharp constants.

## Assumptions and scope
The claim is for **complex or real, total-degree-at-most-two algebraic polynomials** with the ordinary uniform volume inner product on the **solid unit ball**, not for spherical-surface harmonics, bandlimits based on Fourier–Bessel transforms, higher polynomial degrees, or arbitrary subregions. The orthant is the positive coordinate orthant; boundary conventions do not matter for volume integrals. The displayed lists are linearly independent for \(d\ge4\), and the generalized eigenvalue problems are positive definite on the right-hand side.

## Proof
**1. Exact orthant moments.** For a multi-index \(\alpha\in\mathbb N_0^d\), write \(|\alpha|=\sum_j\alpha_j\). Direct radial integration on the ball, followed by a Dirichlet integral over the coordinate squares of the unit sphere, gives
\[
M_d(\alpha):=\int_{B_d}\prod_{j=1}^d|x_j|^{\alpha_j}\,d\mu_d(x)
=\frac{\Gamma(d/2+1)}{\Gamma((d+|\alpha|)/2+1)}
\prod_{j=1}^d\frac{\Gamma((\alpha_j+1)/2)}{\Gamma(1/2)}.
\]
The integral of the corresponding signed monomial on \(B_d\) vanishes if any exponent is odd and otherwise equals \(M_d(\alpha)\). On \(Q_d\) it always equals \(2^{-d}M_d(\alpha)\). Linear expansion therefore gives **every entry** in the eight-by-eight total of the listed block Gram matrices from explicit gamma functions, with no numerical integration or unknown constants.

**2. Complete representation decomposition.** Coordinate permutations preserve both \(B_d\) and \(Q_d\), hence preserve their two Hermitian forms and the operator. The coefficient spaces for constants, linear monomials, diagonal quadratic monomials, and off-diagonal quadratic monomials are, respectively, the one-dimensional trivial representation, two copies of the permutation representation on \(d\) letters, and the permutation representation on unordered pairs.

The letter representation splits into trivial and the \((d-1)\)-dimensional standard module \(V\). The edge representation splits into trivial, another \(V\), and the \(d(d-3)/2\)-dimensional module \(W\) consisting of symmetric edge coefficients with all vertex row sums zero. To verify irreducibility of \(W\) without relying on a classification theorem, note that an invariant endomorphism of the edge permutation module has one free entry for each of the three orbits of ordered edge pairs (equal, incident, disjoint), so its commutant has dimension three. Its trivial and standard constituents are already nonisomorphic irreducibles, and their multiplicities each equal one. Therefore the remaining \(W\) must be a single irreducible constituent of multiplicity one (otherwise the commutant dimension would exceed three). The dimension formula follows by subtracting the rank-\(d\) unsigned vertex-edge incidence map from \(\binom d2\), valid for \(d\ge4\).

Consequently, \(\mathcal P_{\le2}(B_d)\) decomposes as four trivial copies, three copies of \(V\), and one copy of \(W\). Schur's lemma, applied simultaneously to the two invariant Hermitian forms, shows that the concentration spectrum is the generalized spectrum of a four-dimensional multiplicity form, a three-dimensional multiplicity form repeated \(d-1\) times, and a scalar repeated \(d(d-3)/2\) times. The lists \(U_0\), \(U_1\), and \(U_2\) select nonzero matching vectors in precisely these three isotypic sectors; their Gram pencils therefore reproduce the full spectra without extraneous scaling. The dimension check is \(4+3(d-1)+d(d-3)/2=\binom{d+2}{2}\).

**3. Evaluation of the large-multiplicity eigenvalue.** The polynomial \(h=(x_1-x_4)(x_2-x_3)\) has edge coefficients whose row sums vanish, so \(h\in W\). The moment formula gives
\[
M_d(2,2,0,\ldots)=\frac1{(d+2)(d+4)},\quad
M_d(2,1,1,0,\ldots)=\frac{2}{\pi(d+2)(d+4)},
\]
\[
M_d(1,1,1,1,0,\ldots)=\frac4{\pi^2(d+2)(d+4)}.
\]
Expanding \(|h|^2\) first on the full ball and then on the orthant gives
\[
\frac{\int_{Q_d}|h|^2\,d\mu_d}{\int_{B_d}|h|^2\,d\mu_d}
=2^{-d}\frac{M_{22}-2M_{211}+M_{1111}}{M_{22}}
=2^{-d}(1-2/\pi)^2.
\]
Because \(W\) is irreducible and occurs once, this is its full scalar concentration spectrum, with the stated multiplicity.

**4. Sharpness and trace.** The preceding decomposition exhausts the polynomial space, so its smallest/largest eigenvalues are exactly the minimum/maximum possible Rayleigh quotients (the finite-dimensional spectral theorem). No additional eigenvalues exist. A nonzero polynomial cannot vanish identically on either of the two open regions \(Q_d^\circ\) and \(B_d^\circ\setminus Q_d\); hence both the concentration and complementary Gram forms are positive definite, giving strict eigenvalue bounds \(0<\lambda<1\). Finally, the diagonal of the degree-at-most-two reproducing kernel is invariant under all orthogonal rotations, so its integral over any orthant is exactly \(2^{-d}\) of its integral over the whole ball. The latter equals the dimension \(\binom{d+2}{2}\), proving the trace formula.

## Verification
Run `python verify.py` with Python 3 and NumPy. The standalone script constructs the two Gram pencils from the gamma-moment formula; it **separately** constructs the complete monomial Gram pencil, without using the representation block decomposition, in each of the dimensions \(4,5,6,7,8\). It compares every eigenvalue with multiplicities, checks the exact scalar formula and the trace, and records sharp numerical extrema. All tests passed in the construction environment. The general-dimensional theorem rests on the above exact proof, not the finite checks.

## Relationship to prior work
Gerhards and Huang (first public version August 7, 2023) formulate polynomial-bandlimited concentration in the \(d\)-ball and investigate high-bandlimit spectral distributions and general bounds; their Sections 2 and 4 and Appendix B do not provide this fixed-quadratic orthant pencil or its complete all-dimensional spectrum. Khalid, Kennedy and McEwen (2014) use Fourier–Bessel and Fourier–Laguerre bandwidths on the ball, not the total-degree-two polynomial space used here. Prior spherical-orthant results, including low-degree harmonic-band spectra, concern surface measure and omit the independent radial quadratic mode. In particular, a previously known spherical-orthant edge-sector scalar may coincide with the displayed scalar after normalization; **that scalar alone is not claimed as independently novel**. The claimed object is the full solid-ball polynomial spectrum with its four-dimensional radial/symmetric sector and the associated sharp concentration constants.

## Limitations
This theorem does not assert that every block root is distinct, nor prove a uniform ordering of the roots of the four- and three-dimensional pencils as the dimension varies. The extrema are nevertheless exact and attained as the minimum/maximum of a fixed collection of explicit roots. No explicit radicals for those roots, higher-degree asymptotics, or external independent audit are claimed. A related unindexed specialist formula remains a historical-priority risk.

## References
1. Christian Gerhards and Xinpeng Huang, *Slepian spatiospectral concentration problem on the d-dimensional ball for different notions of bandwidth*, arXiv:2308.03543, first posted August 7, 2023, https://arxiv.org/abs/2308.03543 .
2. Zubair Khalid, Rodney A. Kennedy, and Jason D. McEwen, *Slepian spatial-spectral concentration on the ball*, arXiv:1403.5553, first posted March 21, 2014, https://arxiv.org/abs/1403.5553 .
