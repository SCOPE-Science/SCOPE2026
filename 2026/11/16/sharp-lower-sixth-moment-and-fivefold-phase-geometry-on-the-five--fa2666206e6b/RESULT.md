# Sharp lower sixth moment and fivefold phase geometry on the five-point finite parabola

## Finding
Let \(\omega=\exp(2\pi i/5)\) and let \(a=(a_t)_{t\in\mathbb F_5}\) be any complex coefficients with \(|a_t|=1\). Define the finite-parabola Fourier sum and its probability-normalized sixth moment by
\[
P_a(x,y)=\sum_{t\in\mathbb F_5} a_t\omega^{xt+yt^2},\qquad
M_6(a)=\frac1{25}\sum_{x,y\in\mathbb F_5}|P_a(x,y)|^6.
\]
All indices below are modulo five. Form five unit phases
\[
b_s=\frac{a_{s-1}a_{s+1}}{a_{s-2}a_{s+2}}\qquad(s\in\mathbb F_5).
\]
Then the following is an **exact identity**, with no unspecified constants:
\[
\boxed{M_6(a)=500+9\left|\sum_{s\in\mathbb F_5}b_s\right|^2.}
\]
Consequently, the complete sharp range of the phase-only sixth moment is \([500,725]\). The lower endpoint is attained **if and only if** \(\sum_s b_s=0\); the upper endpoint is attained **if and only if** all \(b_s\) agree. The cubic chirp \(a_t=\omega^{t^3}\) attains the lower endpoint, while constant phases attain the upper endpoint.

The phase-ratio map from coefficient phases modulo a common scalar phase to tuples \((b_s)\) with \(\prod_s b_s=1\) is an onto covering map of degree exactly five. Thus **every** five-unit-vector zero sum with product one comes from precisely five distinct coefficient-phase classes minimizing \(M_6\). This characterizes the full minimizer set, not just the displayed chirp. Within the restricted alphabet of fifth roots of unity, the minimizing sequences modulo a common phase are **exactly 100** cubic chirps \(a_t=\omega^{At+Bt^2+Ct^3}\), with \(A,B\in\mathbb F_5\) and \(C\in\mathbb F_5^\times\); no fourth-degree phase pattern is minimizing. In the normalized extension convention \(\mathcal E a=P_a/5\) with counting measure on \(\mathbb F_5^2\), the sharp phase-only sixth-power range is \([4/5,29/25]\).

## Assumptions and scope
The field is exactly \(\mathbb F_5\), the complete five-point parabola \(\{(t,t^2):t\in\mathbb F_5\}\subset\mathbb F_5^2\), and every input coefficient has modulus exactly one. The output sum \(M_6\) uses normalized counting measure; the extension \(\mathcal E\) uses the factor \(1/5\) and *unnormalized* output counting measure. All arithmetic in the Fourier exponent is modulo five. Equivalence of coefficient vectors is only under multiplication by one common phase; no phase quantization is assumed. This does not assert a minimum over arbitrary coefficient magnitudes or a corresponding formula over larger fields.

## Proof
**1. Triple-sum Fourier expansion.** For each \((u,v)\in\mathbb F_5^2\), let \(\mathcal F_{u,v}\) be the set of ordered triples \((r,s,t)\in\mathbb F_5^3\) satisfying \(r+s+t=u\) and \(r^2+s^2+t^2=v\). Character orthogonality, with the factor \(1/25\) in \(M_6\), gives exactly
\[
M_6(a)=\sum_{u,v\in\mathbb F_5}\left|\sum_{(r,s,t)\in\mathcal F_{u,v}}a_ra_sa_t\right|^2.
\]
The \(35=\binom73\) multisets of three elements of \(\mathbb F_5\) break into five all-equal multisets of permutation weight one, twenty double-plus-single multisets of weight three, and ten all-distinct multisets of weight six.

**2. Exhaustive collision classification.** Of the \(25\) fibers labelled by \((u,v)\), fifteen contain one multiset and ten contain exactly two. All ten two-multiset fibers have weight-three triples and are given by the following two five-member families, with \(j\in\mathbb F_5\):
\[
(j,j,j+1)\ \longleftrightarrow\ (j+3,j+4,j+4),\qquad
(j,j,j+2)\ \longleftrightarrow\ (j+1,j+3,j+3).
\]
The displayed triples have equal sum and equal sum of squares modulo five. To establish exhaustiveness, enumerate the \(35\) unordered multisets, compute both residues and group them into \(25\) residue classes. Equivalently, the standalone checker performs precisely this exhaustive 35-case exact-integer computation and independently checks the above collision list. The fifteen singleton fibers are the five all-equal and ten all-distinct multisets. Therefore the diagonal part of the squares in Step 1 is
\[
5\cdot1^2+20\cdot3^2+10\cdot6^2=545.
\]
Each doubleton contributes the additional term \(18\operatorname{Re}(m\overline n)\), where \(m,n\) are the corresponding unit monomial products.

**3. Ten resonances become ten pairwise phase products.** Direct substitution into the definition of \(b_s\) shows that the first collision family in Step 2 has monomial quotient \(b_{j+1}\overline{b_{j+3}}\), and the second has quotient \(b_{j+1}\overline{b_{j+2}}\). As \(j\) runs over five residues, these are precisely all ten unordered pairs of distinct \(b\)'s, once each. Consequently
\[
M_6(a)=545+18\sum_{0\le s<t\le4}\operatorname{Re}(b_s\overline{b_t})
=500+9\left|\sum_{s=0}^4b_s\right|^2.
\]
The nonnegative square gives the claimed lower bound, and \(|\sum b_s|\le5\) gives the upper bound and its equality condition. For \(a_t=\omega^{t^3}\), binomial expansion yields
\[
b_s=\omega^{(s-1)^3+(s+1)^3-(s-2)^3-(s+2)^3}=\omega^{2s},
\]
whose sum vanishes. Constant \(a_t\) gives \(b_s=1\). Thus both inequalities are sharp. By continuity of \(M_6\) on the connected phase torus, all intermediate values occur.

**4. Exact phase map and all minimizers.** Clearly \(\prod_{s=0}^4 b_s=1\). Fix \(a_0=1\), and use \(b_1,b_2,b_3,b_4\) as independent target coordinates (then \(b_0=(b_1b_2b_3b_4)^{-1}\)). The four-by-four integer exponent matrix is obtained by deleting row and column zero from
\[
W=\begin{pmatrix}
0&1&-1&-1&1\\
1&0&1&-1&-1\\
-1&1&0&1&-1\\
-1&-1&1&0&1\\
1&-1&-1&1&0
\end{pmatrix}.
\]
Its determinant is \(5\), as is checked by direct integer elimination and independently by the checker. An integral matrix of nonzero determinant induces a surjective homomorphism of four-dimensional real tori, with the absolute determinant as the number of preimages of every point. Hence the ratio map is surjective with exactly five lifts modulo global phase. Its inverse image of \(\{(b_s):|b_s|=1,\ \prod_s b_s=1,\ \sum_s b_s=0\}\) is exactly the complete minimizing family. This proves the claimed fivefold correspondence.

**5. Exact fifth-root alphabet classification.** Suppose additionally that each coefficient is a fifth root of unity. Modulo a common phase, write \(a_t=\omega^{h(t)}\) with \(h(0)=0\). Every function \(h:\mathbb F_5\to\mathbb F_5\) has a unique interpolation polynomial of degree at most four, and here it has the form \(h(t)=At+Bt^2+Ct^3+Dt^4\). The five cyclic second-difference ratios above have exponents
\[
 b_s=\omega^{-B+2Cs-Ds^2}.
\]
For five fifth roots of unity to sum to zero, their exponent multiplicities must all be equal: the polynomial with nonnegative integer coefficients representing that sum must be a multiple of the minimal polynomial \(1+X+X^2+X^3+X^4\), and it has five coefficients in total. Hence the exponent map \(s\mapsto-B+2Cs-Ds^2\) must permute \(\mathbb F_5\). Every genuine quadratic polynomial over an odd field is noninjective, so necessarily \(D=0\). It is then bijective exactly when \(C\neq0\). Conversely every such cubic phase achieves the minimum. There are precisely \(5\cdot5\cdot4=100\) sequences modulo common phase, proving the asserted discrete-alphabet rigidity.

## Verification
Run `python3 checker.py` with Python 3 and its standard library. The checker enumerates all 35 three-element multisets and all 25 Fourier-sum fibers; verifies the ten collision-to-ratio identifications and the exact determinant; checks the identity as an equality in the cyclotomic quotient \(\mathbb Z[X]/(1+X+X^2+X^3+X^4)\) for all 625 coefficient assignments \(a_0=1\), \(a_1,\ldots,a_4\in\{1,\omega,\ldots,\omega^4\}\); compares 200 additional independently evaluated continuous-phase Fourier moments against the square identity, and independently enumerates all 100 fifth-root minimum sequences against the cubic-chirp formula. It also tests both explicit endpoints. These computations are finite consistency checks; the proof of the identity and covering assertion is the finite classification and integer matrix argument above.

## Relationship to prior work
González-Riquelme and Oliveira e Silva [1] prove the general finite-field parabola sharp \(L^2\)-to-\(L^6\) **upper** extension inequality in characteristic greater than three, including the fact that maximizers have constant modulus (Theorem 1.3). Their upper bound yields \(M_6\le725\) at field size five but gives neither the sharp lower endpoint, the exact five-ratio square identity, nor the minimum's phase-fiber structure. A later exact classification of the upper equality cases, *Complete sixth-moment extremizers on the prime-field parabola* [2], likewise addresses the opposite endpoint and does not imply the phase-only minimum. The three-frequency parabolic sixth-moment problem [3] is phase-independent outside characteristic three and does not cover the complete five-frequency support. The present result concerns the missing lower phase-only endpoint in the first admissible prime field and an exact nontrivial fivefold map of its full optimizer set.

## Limitations
The classification is specific to \(\mathbb F_5\) and fixed unit magnitudes; no claim is made for other primes, prime-power fields, missing parabola frequencies, or arbitrary coefficient magnitudes. The equation \(\sum b_s=0\) classifies the minimizers as an explicit geometric fiber rather than as a finite list, because continuously many minimizers exist. The historical search cannot exclude an equivalent identity in specialized small-field sequence or phase-code literature; the originality assessment is not a claim of exhaustive priority.

## References
1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647v1, first public 2024-05-26, especially Theorem 1.3 and Section 6. https://arxiv.org/abs/2405.16647
2. *Complete sixth-moment extremizers on the prime-field parabola*, published mathematical record (2026), identifier `a84363193055`, complete equality classification for the sharp upper endpoint.
3. *Sharp sixth Fourier moments for three parabolic modes in every odd characteristic*, published mathematical record (2026), identifier `52302cf3414e`, complete three-mode sharp-extension result.
