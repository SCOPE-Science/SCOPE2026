# Six-stratum Fourier spectrum and optimal weighting for null-ray tomography over prime-square rings

## Finding

For every odd prime \(p\), let \(R=\mathbb Z/p^2\mathbb Z\), \(V=M_2(R)\), and let \(\mathcal D\) comprise every free cyclic direction \(d=Rv\) with \(v\in V\) primitive (some entry a unit) and \(\det v=0\) in \(R\). The unnormalized affine line transform is
\[
(Tf)(d,x+d)=\sum_{y\in x+d}f(y),
\]
with one measurement for each distinct affine coset of each direction and ordinary counting-measure Hilbert norms. It is injective on all complex-valued functions on \(V\), and its complete normal-operator Fourier spectrum is as follows. Write \(N_1=(p-1)(p+1)^2\) and \(N_2=(p^2-1)(p^2-p)\). Characters are indexed by \(\xi\in V\) via the entrywise pairing \(\langle\xi,X\rangle=\sum_{i,j}\xi_{ij}X_{ij}\) modulo \(p^2\), and \(\overline\xi\) denotes reduction modulo \(p\).

| Fourier-frequency stratum | \(\lambda(\xi)/p^2\) | multiplicity |
| --- | ---: | ---: |
| \(\xi=0\) | \(p^2(p+1)^2\) | \(1\) |
| \(\xi=p\eta\), \(\operatorname{rank}\eta=1\) over \(\mathbb F_p\) | \(p^2(2p+1)\) | \(N_1\) |
| \(\xi=p\eta\), \(\operatorname{rank}\eta=2\) over \(\mathbb F_p\) | \(p^2(p+1)\) | \(N_2\) |
| primitive \(\xi\), \(\operatorname{rank}\overline\xi=2\) | \(p(p+1)\) | \(p^4N_2\) |
| primitive \(\xi\), \(\operatorname{rank}\overline\xi=1\), \(\det\xi\ne0\) in \(R\) | \(2p^2\) | \(N_1(p^4-p^3)\) |
| primitive \(\xi\), \(\operatorname{rank}\overline\xi=1\), \(\det\xi=0\) in \(R\) | \(3p^2\) | \(p^3N_1\) |

All six levels are distinct for odd \(p\); multiplying the second column by \(p^2\) gives the eigenvalues of \(T^*T\). The sharp squared condition numbers are
\[
\kappa_{\mathrm{mean\text{-}zero}}^2=\frac{p(2p+1)}{p+1},\qquad
\kappa_{\mathrm{all}}^2=p(p+1).
\]
Here the first condition number refers to the restriction to the mean-zero input space, using all measurement outputs; the second includes constant inputs. Moreover, among **all nonnegative scalar weights on the direction blocks** whose weighted transform is injective, uniform weights attain the least possible condition number, for both input spaces. No uniqueness of optimal weights is asserted.

## Assumptions and scope

The ring is exactly the residue-class ring \(R=\mathbb Z/p^2\mathbb Z\) with odd prime \(p\); directions are *free primitive determinant-zero cyclic rank-one submodules*, not all nonzero determinant-zero vectors or all lines. The projective line \(\mathbf P^1(R)\) has \(p(p+1)\) elements, and each primitive rank-one matrix direction has a unique pair of projective column and row directions. Thus \(|\mathcal D|=p^2(p+1)^2\). A positive scalar weight for direction \(d\) multiplies all its affine-coset measurements by its square root. All Fourier transforms use the additive characters of \(R^4\); no normalized counting factors are hidden. The condition number is the ratio of largest to smallest nonzero singular values on the specified input space. A noninjective weighting has infinite condition number by convention.

## Proof

**1. Parametrization and normal-operator diagonalization.** A matrix with a unit entry and determinant zero can be reduced by invertible row and column operations to \(\operatorname{diag}(1,0)\); hence it is \(uw^{\mathsf T}\) for primitive columns \(u,w\in R^2\). Its cyclic direction is determined by \(([u],[w])\in\mathbf P^1(R)^2\), proving the count of directions. For a fixed direction \(d\),
\[
(T_d^*T_df)(x)=\sum_{h\in d}f(x+h).
\]
Since \(|d|=p^2\), character orthogonality gives
\[
T^*T\chi_\xi=p^2 L(\xi)\chi_\xi,\quad
L(\xi)=\#\{([u],[w])\in\mathbf P^1(R)^2:u^{\mathsf T}\xi w=0\ \mathrm{mod}\ p^2\}.
\]
Frequency changes by invertible left and right matrices preserve this count. Smith normal form therefore gives representatives \(0\), \(\operatorname{diag}(p,0)\), \(\operatorname{diag}(p,p)\), \(\operatorname{diag}(1,1)\), \(\operatorname{diag}(1,p)\), and \(\operatorname{diag}(1,0)\), exactly the six displayed strata.

**2. Exact Smith-stratum counts.** Every projective point has a unique representative of one of the forms \((1,t)\), \(t\in R\), or \((ps,1)\), \(s\in\mathbb F_p\). For \(\xi=\operatorname{diag}(1,1)\), each projective \(u\) has exactly one orthogonal projective \(w\), giving \(p(p+1)\). For \(\xi=\operatorname{diag}(1,p)\), the first chart gives one \(w\) for each of \(p^2\) values of \(u\); the second gives \(p\) admissible \(w\)'s for each of \(p\) values of \(u\); hence \(2p^2\). For \(\xi=\operatorname{diag}(1,0)\), the first chart contributes \(p^2\); on the second, \(s\ne0\) contributes \(p(p-1)\), and \(s=0\) contributes the entire \(p(p+1)\)-point projective line, totaling \(3p^2\). If \(\xi=p\eta\), orthogonality depends only on projective reductions modulo \(p\). Each residue-field projective pair has exactly \(p^2\) lifts. For rank-one \(\eta\), there are \(2p+1\) orthogonal pairs over \(\mathbb F_p\); for invertible \(\eta\), there are \(p+1\). The zero frequency has all \(p^2(p+1)^2\) pairs. These are the table's multipliers.

**3. Multiplicities.** Over \(\mathbb F_p\) there are \(N_1=(p-1)(p+1)^2\) rank-one matrices and \(N_2=(p^2-1)(p^2-p)\) invertible matrices. The frequencies divisible by \(p\) are in bijection with residue matrices. Each invertible residue matrix admits \(p^4\) lifts, all primitive invertible-reduction. Each rank-one residue matrix has \(p^4\) lifts; after changing bases to \(\operatorname{diag}(1,0)\), exactly one linear congruence on its four first-order lift entries forces determinant zero modulo \(p^2\), leaving \(p^3\) such lifts and \(p^4-p^3\) others. This proves every multiplicity and yields a total of \(p^8=|V|\).

**4. Injectivity, optimal conditioning, and weights.** Every table entry is positive, so \(T\) is injective. The least nonconstant multiplier is \(p(p+1)\) and the greatest nonconstant multiplier is \(p^2(2p+1)\), giving the first sharp squared condition number; the constant multiplier is \(p^2(p+1)^2\), giving the second. For weights \(a_d\ge0\), the character eigenvalue becomes
\[
p^2\sum_{d\in\mathcal D}a_d\mathbf 1_{\{\xi\perp d\}}.
\]
The group \(\mathrm{GL}_2(R)\times\mathrm{GL}_2(R)\) acts transitively on the null directions and permutes Fourier characters, preserving both the full and mean-zero input spaces. Averaging the weights over this group makes them uniform while averaging the corresponding eigenvalues over permutations of the frequency index set. Thus the maximum eigenvalue cannot increase and the minimum cannot decrease. Uniform direction weights therefore minimize each squared condition number. Uniform weights are strictly positive, so the optima are attained.

## Verification

The included `checker.py` is a standard-library exact integer enumeration. It constructs every projective null direction and exhausts every Fourier frequency for \(p=2\) and \(p=3\), independently counts orthogonal null directions, verifies the six Smith-stratum values and multiplicities, and checks that primitive isotropic vectors are exactly unit multiples of the constructed directions. For \(p=5,7,11\) it checks a representative of each stratum rather than exhaustively enumerating all frequencies. All checks passed, with terminal marker `RING_NULL_RAY_EXACT_SPECTRUM_CHECKS_PASS`. Character orthogonality and the Smith-form argument above prove the unbounded-prime theorem; finite enumeration is not represented as an infinite proof.

## Relationship to prior work

Koh's finite-field X-ray transform article provides a classical harmonic-analytic setting and sharp mapping estimates for *all* affine directions over fields, not the local-ring determinant-restricted spectrum here. Iosevich, Liu, Mayeli, and Pakianathan discuss prime-power cyclic modules, wavelets, and multiscale lines, but do not establish this six-level null-direction transform. Feldman and Grinberg study projective finite-field admissible line families and doubly ruled quadrics, not local-ring affine Fourier multipliers. Landjev and Vandendriessche establish ranks for incidence matrices of *unrestricted shapes* in projective Hjelmslev geometries over chain rings; their theorem does not state the restricted null-ray singular values or weighted condition-number optimum. Projective cyclic-grid Radon-transform conditioning results concern all projective directions in two variables, in contrast to the four-variable determinant-zero restriction.

## Limitations

This is an exact result for odd prime-square cyclic residue rings, not an assertion for arbitrary finite local rings or higher nilpotency length. The weighting optimum asserts existence of uniform optimal weights, not uniqueness. The present scientific review is bounded; an earlier unindexed chain-ring polar-space incidence identity may yield the same spectrum, so historical priority and independent verification are not certified. The numerical checks are finite corroboration only.

## References

1. D. Koh, *Sharp endpoint estimates for the X-ray transform and the Radon transform in finite fields*, arXiv:1209.1215, first posted 2012-09-06, https://arxiv.org/abs/1209.1215.
2. A. Iosevich, A. Liu, A. Mayeli, and J. Pakianathan, *Wavelet decomposition and bandwidth of functions defined on vector spaces over finite fields*, arXiv:1601.03473, first posted 2016-01-14, https://arxiv.org/abs/1601.03473.
3. D. V. Feldman and E. L. Grinberg, *Admissible Complexes for the Projective X-Ray Transform over a Finite Field*, arXiv:1707.06695, first posted 2017-07-20, https://arxiv.org/abs/1707.06695.
4. I. Landjev and P. Vandendriessche, *On the rank of incidence matrices in projective Hjelmslev spaces*, Designs, Codes and Cryptography 73 (2014), 615–623, doi:10.1007/s10623-014-9959-z; https://biblio.ugent.be/publication/5722101/file/5722116.pdf.
