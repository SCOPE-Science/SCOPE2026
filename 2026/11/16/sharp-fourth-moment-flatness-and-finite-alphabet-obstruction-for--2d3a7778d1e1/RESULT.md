# Sharp fourth-moment flatness and finite-alphabet obstruction for centered Fourier crosses

## Finding
For every integer \(d\ge2\), let \(\mathbb T^d\) have Haar probability measure and let
\[
P(z)=c+\sum_{j=1}^d(a_jz_j+b_jz_j^{-1}),
\qquad |c|=|a_j|=|b_j|=1.
\]
Set the intrinsic antipodal phase products \(u_j=a_jb_j\overline c^{\,2}\). Then \(|u_j|=1\), and the **exact fourth-moment identity** is
\[
\boxed{\int_{\mathbb T^d}|P|^4\,dm
=8d^2+2d+4\left|\frac12+\sum_{j=1}^d u_j\right|^2.}
\tag{1}
\]
Consequently the full sharp moment interval is
\[
\boxed{8d^2+2d\ \le\ \int|P|^4\,dm\ \le\ 12d^2+6d+1.}
\tag{2}
\]
Every minimizer, and only a minimizer, satisfies \(\sum_j u_j=-1/2\); every maximizer, and only a maximizer, satisfies \(u_1=\cdots=u_d=1\). Both bounds are attained for all \(d\ge2\).

There is an absolute **finite-phase obstruction**: if all coefficients of \(P\) belong to the same alphabet \(\mu_q=\{\exp(2\pi i k/q):0\le k<q\}\) for any finite integer \(q\ge2\), then the lower endpoint in (2) is unattainable. More quantitatively, writing \(\varphi\) for Euler's totient function, every such polynomial satisfies
\[
\int|P|^4-(8d^2+2d)\ge (2d+1)^{-2(\varphi(q)-1)}.
\tag{3}
\]
In contrast, the sharp binary-phase minimum is exactly \(8d^2+2d+1\); the same sharp minimum holds for four- and six-phase coefficients. For ternary coefficients the sharp minimum equals
\[
8d^2+2d+\begin{cases}3,&d\equiv1\pmod3,\\1,&d\not\equiv1\pmod3.\end{cases}
\tag{4}
\]
At the first two-dimensional cross, \(d=2\), the continuous-phase minimum is \(36\), whereas the exact five-phase minimum is \(41-2\sqrt5\) (strictly between \(36\) and the binary minimum \(37\)). After fixing the center and positive-arm phases to one, the four five-phase minimizing negative-arm exponent pairs are exactly \((1,3),(2,4),(3,1),(4,2)\) modulo five. Five phases are therefore the first integer alphabet size to improve on two-phase coefficients, while six phases revert to \(37\).

## Assumptions and scope
The dimension is any integer \(d\ge2\); the \(2d+1\) frequencies are exactly \(\{0,\pm e_1,\ldots,\pm e_d\}\), with no others. All coefficient magnitudes are **exactly one**, not arbitrary. Every fourth moment is computed using Haar **probability** measure. The result also holds without change on \(\prod_{j=1}^d\mathbb Z/N_j\mathbb Z\) with normalized counting measure whenever every \(N_j\ge5\), because all exponent differences needed for a fourth moment then remain distinct. The cyclic order four case has additional frequency aliasing and is not asserted.

Multiplying \(P\) by a common unimodular scalar or translating independent torus coordinates leaves the \(u_j\)'s invariant. Conversely these operations can arrange \(c=a_1=\cdots=a_d=1\), after which \(b_j=u_j\). They therefore give a complete, nonredundant gauge for the equality descriptions. If the coefficients are in \(\mu_q\), the gauge can also be chosen in \(\mu_q\).

## Proof
**1. Exact moment computation.** Use the preceding gauge and put \(Y_j=z_j+u_jz_j^{-1}\), with independent Haar-uniform coordinates \(z_j\). Character orthogonality gives
\[
\mathbb EY_j=0,\quad \mathbb E|Y_j|^2=2,\quad
\mathbb EY_j^2=2u_j,\quad \mathbb E|Y_j|^4=6,
\quad\mathbb E(|Y_j|^2Y_j)=0.
\]
For independent centered complex variables \(Y_j\), direct expansion of \(|1+\sum_jY_j|^4\) therefore yields
\[
1+14d+16\binom d2+4\operatorname{Re}S
+8\sum_{i<j}\operatorname{Re}(u_i\overline{u_j}),
\quad S=\sum_j u_j.
\]
Since \(|S|^2=d+2\sum_{i<j}\operatorname{Re}(u_i\overline{u_j})\), completing the square gives (1). This calculation is also valid for independent uniform roots of unity of individual orders at least five: exponents of absolute value at most four cannot alias with zero.

**2. Endpoints, attainability, and complete equality.** Nonnegativity of the square in (1) gives the lower bound. For \(d=2\), the pair
\[
(u_1,u_2)=\left(\frac{-1+i\sqrt{15}}4,\frac{-1-i\sqrt{15}}4\right)
\]
has unit magnitudes and sum \(-1/2\). For \(d=3\), choose \(u_1=-1\) and \(u_2,u_3\) unit conjugates with \(u_2+u_3=1/2\). Appending cancelling pairs \((1,-1)\) realizes the lower bound for every larger dimension. The triangle inequality gives \(|S+1/2|\le d+1/2\), with equality only when every \(u_j=1\); substituting proves the upper bound. The connected phase torus makes every intermediate fourth-moment value attainable. Formula (1) and these exact equality conditions give all extremizers modulo gauge.

**3. No finite root-of-unity alphabet attains the lower bound.** If the coefficients belong to \(\mu_q\), then each \(u_j\) is itself a root of unity. Each \(u_j\), and therefore \(S\), is an algebraic integer. Equality at the lower endpoint would require \(S=-1/2\), a rational number that is **not** an algebraic integer. This contradiction holds for every finite \(q\) and every \(d\ge2\). For the quantitative bound, set \(\alpha=1+2S\), so the gap in (1) is \(|\alpha|^2\). The nonzero algebraic integer \(\alpha\in\mathbb Q(\zeta_q)\) has nonzero integral field norm; hence \(|N_{\mathbb Q(\zeta_q)/\mathbb Q}(\alpha)|\ge1\). Each of its other \(\varphi(q)-1\) Galois conjugates has absolute value at most \(2d+1\), because every conjugate of a root of unity still has modulus one. Dividing the norm by these factors proves (3). No positive bound uniform in alphabet size is claimed.

**4. Binary, quaternary, and sixth-root alphabets.** With binary phases, \(S\in\mathbb Z\), and its parity is that of \(d\). Thus the closest allowed value to \(-1/2\) is \(S=0\) for even \(d\), or \(S=-1\) for odd \(d\). These values are achieved by balancing signs; the sharp gap is one. For fourth-root phases \(S\in\mathbb Z[i]\), whose closest points to \(-1/2\) are again \(0,-1\). For sixth-root phases \(S\) belongs to the triangular lattice \(\mathbb Z[\exp(2\pi i/3)]\), whose closest points to \(-1/2\) are again \(0,-1\) (write its elements as \(m+n(-1+i\sqrt3)/2\) and compare the squared real and imaginary parts). In each alphabet, \(S=0\) is achievable in every even dimension using cancelling pairs, and \(S=-1\) is achievable in every odd dimension by one \(-1\) and cancelling pairs. Thus all three sharp gaps equal one.

**5. Ternary phases.** Write \(\omega=\exp(2\pi i/3)\) and let \(a,b,c\) count phases \(1,\omega,\omega^2\) among \(u_1,\ldots,u_d\). Their sum satisfies
\[
4\left|S+\tfrac12\right|^2=(3a-d+1)^2+3(b-c)^2,\qquad a+b+c=d.
\]
If \(d\equiv0\pmod3\), take \(a=d/3\), \(b=c=d/3\), giving gap one. If \(d\equiv2\pmod3\), take \(a=(d-2)/3\), \(b=c=(d+1)/3\), again giving gap one. If \(d\equiv1\pmod3\), choosing \(a=(d-1)/3\) makes the first square zero but forces the odd integer \(b-c\) to have absolute value at least one, giving gap three; other values of \(a\) make the first square at least nine. All three constructions are feasible for the stated \(d\), so (4) is exact.

**6. The exact two-dimensional five-phase threshold.** Write \(u_1=\zeta_5^r\), \(u_2=\zeta_5^s\). Equation (1) becomes
\[
\int|P|^4=45+8\cos\frac{2\pi(r-s)}5
+4\cos\frac{2\pi r}5+4\cos\frac{2\pi s}5.
\]
The five cosine values consist of \(1\), \((\sqrt5-1)/4\) (twice), and \(-(\sqrt5+1)/4\) (twice). Comparing the 25 exact values in \(\mathbb Q(\sqrt5)\) gives the unique minimum value \(41-2\sqrt5\), achieved precisely for the four ordered exponent pairs stated above. The standalone exact checker enumerates these 25 values using integer coefficient pairs and an exact sign comparison in \(\mathbb Q(\sqrt5)\). The preceding alphabet calculations show that all \(q=2,3,4\) have minimum \(37\) at \(d=2\), while \(q=6\) also has minimum \(37\).

## Verification
Run `python3 artifacts/checker.py` from the directory containing this file. The standard-library program evaluates \(576\) exact Gaussian-integer convolution comparisons on cross apertures, enumerates the complete 25-case five-phase table in exact \(\mathbb Q(\sqrt5)\) arithmetic, and corroborates ternary congruence cases through dimension 30. It prints `CENTERED_CROSS_FOURTH_PASS gaussian_convolutions= 576 quintic_alphabet_exact_cases= 25 ternary_dimensions= 29`. None of these finite checks substitutes for the all-dimensional proof or the all-alphabet algebraic-integer obstruction.

## Relationship to prior work
Das, Banerjee and Parampalli (2023) analyze two-dimensional polyphase complementary array **quads**, aperiodic correlation sums, and peak-to-mean-envelope-power constraints. Their full text does not classify the sharp integrated fourth moment of one centered nearest-neighbor frequency cross, its phase minimizers, or the impossibility of exact optimum under any finite phase alphabet.

The published *Sharp fourth moments and a torsion threshold for signed-coordinate Fourier crosses* considers precisely the same frequency set, but proves a sharp **upper** \(L^4/L^2\) inequality for coefficients of arbitrary magnitudes, together with upper extremizer equality and energy deficits. Its statement does not imply the **lower** fourth-moment bound under equal magnitudes, the phase-sum equality locus, or the alphabet obstructions in this theorem. The published *Sharp sixth Fourier moment for the five-point toral cross* concerns an arbitrary-amplitude **upper sixth** moment in dimension two. A published finite-abelian coordinate-cross extension theorem again optimizes an upper norm on a different, much larger frequency union. None supplies this lower-moment finite-alphabet classification. Classical character orthogonality and cyclotomic algebraic-integer facts are used as established tools.

## Limitations
The theorem concerns fixed-support **unimodular** coefficients, and does not optimize arbitrary amplitudes, peak sidelobes, or fourth moments on finite cyclic orders below five. The gap to continuous phases for each fixed finite alphabet is positive by nonattainment, but it need not be uniform across alphabet sizes: the union of roots of unity is dense in the circle. No general exact formula is asserted for alphabet sizes other than two, three, four, six, and the five-phase two-dimensional case. Distinguishing this exact low-rank identity and its consequences from every earlier specialized radar/array paper may require an independent historical literature review.

## References
1. S. Das, A. Banerjee and U. Parampalli, *Two-Dimensional Z-Complementary Array Quads with Low Column Sequence PMEPRs*, arXiv:2308.06690v1, first public 2023-08-13, https://arxiv.org/html/2308.06690v1.
2. *Sharp fourth moments and a torsion threshold for signed-coordinate Fourier crosses*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-fourth-moments-and-a-torsion-threshold-for-signed-coordina--5bb2dcd28dff.
3. *Sharp sixth Fourier moment for the five-point toral cross*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-sixth-fourier-moment-for-the-five-point-toral-cross--ca9958648029.
4. *Sharp fourth-moment extension and one-axis rigidity for finite abelian crosses*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-extension-and-one-axis-rigidity-for-finite-a--5b31463115dc.
