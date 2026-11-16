# Sharp eighth-moment phase balancing on antipodal coordinate Fourier apertures in every dimension

## Finding

Let \(d\ge4\) be an integer and \(m\) normalized Haar probability measure on \(\mathbb T^d\). For coefficients \(a_j,b_j\in\mathbb C\) with \(|a_j|=|b_j|=1\), put
\[
P(z)=\sum_{j=1}^{d}(a_jz_j+b_jz_j^{-1}),\quad
u_j=a_jb_j,\quad S=\sum_j\nu_j,\quad T=\sum_j\nu_j^2.
\]
Define the explicit integer polynomials
\[
A_d=96(12d^2-33d+26),\qquad
C_d=2d(192d^3-864d^2+1604d-1155).
\]
Then **the following identity holds for every coefficient array**, not just extremizers:
\[
\boxed{\int_{\mathbb T^d}|P|^8\,dm=C_d+A_d|S|^2+36|2S^2-T|^2.}\tag{1}
\]
In particular the sharp minimum is \(C_d\), attained if and only if \(S=T=0\). The sharp maximum is
\[
U_d=C_d+A_dd^2+36(2d^2-d)^2,\tag{2}
\]
attained if and only if all \(\nu_j\) are equal. The full attainable range is exactly \([C_d,U_d]\). At dimensions four and five, all minimizing product phases are precisely the permutations of a common rotation of a regular \(d\)-gon:
\[
(\nu_1,\ldots,\nu_d)=\lambda(1,\zeta_d,\ldots,\zeta_d^{d-1})\ \text{up to permutation},\qquad |\lambda|=1.
\]
For each \(d\ge4\), restricting every coefficient to the binary alphabet cannot attain \(C_d\). Ternary coefficient phases attain it if and only if \(3\mid d\); quaternary phases attain it if and only if \(4\mid d\). In dimensions \(d=4,5\), coefficients from \(\mu_q\) attain \(C_d\) precisely when \(d\mid q\); when they do, exactly \((d-1)!q^{d+1}\) ordered coefficient arrays attain it.

For example, in dimension four, product phases \(\nu=(1,-1,1,-1)\) have \(S=0\) but \(T=4\), and so yield eighth moment \(30376\), while \(\nu=(1,-1,i,-i)\) have \(S=T=0\) and yield the sharp minimum \(29800\). This exhibits the separate second-power-sum obstruction, even within the first-power-sum cancellation locus.

## Assumptions and scope

The phase alphabet \(\mu_q=\{e^{2\pi i k/q}:0\le k<q\}\) constrains each **coefficient**, whereas \(\mathbb T^d\) denotes the independent continuous sampling variables. The support is exactly the \(2d\) characters \(\{\pm e_j:1\le j\le d\}\) in \(\mathbb Z^d\), with all coefficient moduli equal to one. For each \(j\), the change of variables \(w_j=a_jz_j\) reduces \(P\) to \(\sum_j(w_j+\nu_jw_j^{-1})\), proving that its moment depends on the \(\nu_j\) alone. Equivalently, independent coordinate rotations preserve all moments. Formula (1) also remains valid when integration is replaced by uniform sampling on \(\mu_{N_1}\times\cdots\times\mu_{N_d}\), provided all \(N_j\ge9\). No assertion is made for smaller sampling orders.

## Proof

**1. A finite exact Laurent-moment calculation valid for every dimension.** Write \(F_d(\nu)=\int|P|^8dm\), and after the change of variables above expand the fourth power of \(\sum_j(w_j+\nu_j w_j^{-1})\). Orthogonality gives
\[
F_d(\nu)=\sum_{r\in\mathbb Z^d}|[w^r]P(w)^4|^2
=\sum_{h\in\mathbb Z^d}c_h\nu^h.
\tag{3}
\]
Let \(k_j,l_j\) be the multiplicities of \(w_j\) and \(\nu_jw_j^{-1}\) in one four-letter word, and \(k'_j,l'_j\) those in another. Equal spatial frequencies require \(k_j-l_j=k'_j-l'_j\), hence \(k_j-k'_j=l_j-l'_j=-h_j\) if \(h=l-l'\). The equality of total word lengths requires \(\sum_jh_j=0\); moreover, each unit of positive \(h\) requires two letters, so \(\sum_j\max(h_j,0)\le2\). Consequently the only possible nonconstant exponent types, up to permutation and sign, are
\[
e_i-e_j,\quad 2e_i-2e_j,\quad 2e_i-e_j-e_k,\quad e_i+e_j-e_k-e_l,
\tag{4}
\]
where indices displayed as different are pairwise distinct. Their coefficients are, respectively,
\[
1152d^2-2592d+1632,\qquad36,\qquad144,\qquad576.
\tag{5}
\]
For the last three types, no extra letters remain after the required swaps: their values are the products \(6^2\), \(6\cdot24\), and \(24^2\). For the first type, two common letters remain. Let \(f(x)=1+x/2+x^2/12\) for the four distinguished signed letter-types and \(g(x)=1+x+x^2/4\) for each of the other \(2d-4\) letter-types. Exact multinomial weighting gives
\[
c_{e_i-e_j}=(4!)^2[x^2]f(x)^4g(x)^{2d-4}=1152d^2-2592d+1632.
\tag{6}
\]
The constant coefficient is the collision-free multinomial-square count over \(2d\) letters:
\[
\begin{aligned}
c_0&=(4!)^2[x^4]\left(\sum_{r=0}^4\frac{x^r}{(r!)^2}\right)^{2d}\\
&=2d+34(2d)(2d-1)+72(2d)(2d-1)(2d-2)\\
&\quad+24(2d)(2d-1)(2d-2)(2d-3)\\
&=2d(192d^3-288d^2+164d-33).
\end{aligned}\tag{7}
\]
Equations (4)--(7) enumerate **all** Laurent coefficients of the moment, for every dimension. Expanding \(|S|^2\) and \(|2S^2-T|^2\), their nonconstant Laurent coefficients agree with (5) when the multiplier of \(|S|^2\) is \(A_d=96(12d^2-33d+26)\). Their constant terms, after subtracting from (7), give exactly \(C_d\). This proves (1) without induction, interpolation, or a finite-dimension extrapolation.

**2. Sharp minimum and rigidity.** The discriminant of \(12d^2-33d+26\) is \(-159\), so \(A_d>0\). Equation (1) is minimized exactly when \(S=0\) and \(2S^2-T=0\), equivalently \(S=T=0\). For every \(d\ge4\) these two conditions are simultaneously feasible: choose the \(d\)-th roots of unity as the products \(\nu_j\). Their first and second power sums vanish. Thus \(C_d\) is the sharp global minimum.

In dimensions four and five, Newton identities give \(e_1=S=0\) and \(e_2=(S^2-T)/2=0\) for the elementary symmetric polynomials of \(\nu_1,\dots,\nu_d\). As all roots have modulus one, \(e_{d-k}=e_d\overline{e_k}\). For \(d=4\) this also kills \(e_3\); for \(d=5\) it kills \(e_3,e_4\). Therefore the monic polynomial with the \(\nu_j\) as roots is \(X^d+(-1)^de_d\), so the products are a rotated regular \(d\)-gon. The converse follows from vanishing power sums.

**3. Sharp maximum and complete range.** Every Laurent coefficient in (3) is a nonnegative integer. Therefore its value on the unit torus is at most the sum of its coefficients, achieved when all products are equal. Because the coefficient of every \(\nu_i\overline{\nu_j}\) is strictly positive, equality forces all products to agree. Substituting \(S=d\lambda\), \(T=d\lambda^2\) into (1) gives (2). The coefficient torus \(\mathbb T^{2d}\) is connected and the moment is continuous, so all intermediate values between the attained extrema occur.

**4. Finite alphabets and sampling.** If all original coefficients belong to \(\mu_q\), then every \(\nu_j\in\mu_q\), and every product vector admits exactly \(q^d\) ordered factorizations \(\nu_j=a_jb_j\). For binary products, \(T=d\ne0\), excluding equality. For ternary products, \(S=0\) is equivalent to equal multiplicities of the three cubic roots, hence possible exactly when \(3\mid d\); it also implies \(T=0\). For quaternary products, \(S=T=0\) forces equal multiplicities of \(1,-1,i,-i\), hence is possible exactly when \(4\mid d\). For \(d=4,5\), the regular-polygon characterization implies \(d\mid q\). When this divisibility holds, there are \(q(d-1)!\) distinct ordered product vectors and \(q^d\) coefficient factorizations each, giving \((d-1)!q^{d+1}\). Finally, all frequencies of \(P^4\) lie in \([-4,4]^d\). With \(N_j\ge9\) they are distinct modulo the sampling orders, so discrete Parseval is identical to (3).

## Verification

Execute `python3 cross_eighth_check.py` using Python 3 with no dependencies. The script constructs the Fourier coefficients of the full fourth power of \(P\), forms the eighth-moment Laurent polynomial exactly over the integers, and compares every coefficient with equation (1) for dimensions two through six (481 nonzero Laurent coefficients in total). It separately verifies constant and two-coordinate coefficient formulas, checks the known three-dimensional specialization, and checks the endpoint polynomials. Expected final line: `EXACT_CROSS_EIGHTH_PASS`. These calculations are supplemental finite checks; the generating-function and coefficient-type argument above proves the formula in all dimensions. The two-dimensional check lies outside the novel dimension range and tests boundary normalization.

## Relationship to prior work

A publicly available earlier result, *An eighth-moment sum-of-squares law for the octahedral Fourier aperture*, proves the precise \(d=3\) case, \(6390+3360|S|^2+36|2S^2-T|^2\), and explicitly excludes higher dimensions from its scope. The present claim is restricted to \(d\ge4\); it derives the full dimension-polynomial coefficients via an all-dimensional word-pair count and gives the new dimension-four/five rigidity and dimension-dependent phase-alphabet thresholds. The earlier three-dimensional formula is not claimed as new.

Du and Jiang, *Constructions of Polyphase Golay Complementary Arrays* (2022), treat polynomial autocorrelation identities for complementary **pairs and quads**, not the eighth moment of a single \(2d\)-frequency signed-coordinate aperture. Pai and Chen (2021) treat two-dimensional complementary **sets**. Slote, Volberg and Zhang (2023) prove dimension-free Bohnenblust--Hille coefficient inequalities on finite cyclic products, not a sharp fixed-modulus eighth-moment minimum or its minimizing phases. Other research results concern fourth moments for signed-coordinate spectra or sharp sixth-moment **upper** norms with arbitrary coefficient moduli; those statements do not imply this unit-modulus eighth-moment lower extremum.

## Limitations

The claim uses continuous torus Haar integration, a single signed-coordinate Fourier polynomial, exactly unit coefficient moduli, and moment exponent eight. It does not optimize arbitrary coefficient moduli, infer sharp values for nonqualifying finite alphabets, or classify every high-dimensional solution of \(S=T=0\) beyond the two exact moment equations. The finite-torus extension requires nonaliasing sampling orders at least nine. Bibliographic priority cannot be guaranteed; classical autocorrelation and phase-array literature could contain a mathematically equivalent general identity. Independent scientific verification has not been performed.

## References

1. *An eighth-moment sum-of-squares law for the octahedral Fourier aperture*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-eighth-moment-sum-of-squares-law-for-the-octahedral-fourier-a--bd1dca0dd237 (three-dimensional result; full `RESULT.md` compared).
2. Cheng Du and Yi Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1, first public April 20, 2022, https://arxiv.org/html/2204.09372v1.
3. Cheng-Yu Pai and Chao-Yu Chen, *Two-Dimensional Golay Complementary Array Sets from Generalized Boolean Functions*, arXiv:2102.04043v1, first public February 8, 2021, https://arxiv.org/html/2102.04043v1.
4. Joseph Slote, Alexander Volberg and Haonan Zhang, *Bohnenblust--Hille inequality for cyclic groups*, arXiv:2305.10560v1, first public May 17, 2023, https://arxiv.org/html/2305.10560v4 (version four full text used for comparison; original date from version one).
