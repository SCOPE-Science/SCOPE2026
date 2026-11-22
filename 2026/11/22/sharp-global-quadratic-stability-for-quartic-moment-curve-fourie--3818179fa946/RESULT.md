# Sharp global quadratic stability for quartic moment-curve Fourier extension

## Finding
Let \(q\ge2\) and let \(\theta=(\theta_1,\ldots,\theta_q)\) be any probability vector. For four independent samples from \(\theta\), let \(M(T)\) count their distinct rearrangements and put \(F_4(\theta)=\mathbb E[M(T)]\). Set \(u=(1/q,\ldots,1/q)\) and
\[
A_q=24-\frac{72}{q}+\frac{82}{q^2}-\frac{33}{q^3},\qquad
c_q=23-\frac{49}{q}+\frac{33}{q^2}.
\]
Then the following **sharp global quadratic stability inequality** holds for every probability vector:
\[
\boxed{A_q-F_4(\theta)\ge c_q\sum_{i=1}^q\left(\theta_i-\frac1q\right)^2.}\tag{1}
\]
The coefficient \(c_q\) cannot be increased. Equality holds **if and only if** \(\theta=u\) or \(\theta\) is a point mass.

In particular, if \(q=p^k\) has prime characteristic \(p>4\), define the quartic moment curve \(\Gamma=\{(t,t^2,t^3,t^4):t\in\mathbb F_q\}\), normalized counting measure \(\sigma\) on \(\Gamma\), and extension
\[
E f(x)=\frac1q\sum_{t\in\mathbb F_q} f(t)\exp\!\left(\frac{2\pi i}{p}\operatorname{Tr}\left(\sum_{j=1}^4x_jt^j\right)\right).
\]
For every nonzero complex-valued \(f\), put \(N=\frac1q\sum_t|f(t)|^2\) and \(\theta_t=|f(t)|^2/(qN)\). With **counting** measure in the target, (1) is equivalently
\[
\boxed{A_q N^4-\|Ef\|_{\ell^8(\mathbb F_q^4)}^8
\ge c_q N^4\sum_{t\in\mathbb F_q}\left(\theta_t-\frac1q\right)^2.}\tag{2}
\]
Equality in (2) is precisely constant nonzero modulus on all curve points or support on one curve point; coefficient phases are arbitrary. In the alternative normalized-amplitude form, the right side is \((c_q/q)N^2\big\||f|^2-N\big\|_{L^2(\sigma)}^2\).

## Assumptions and scope
The probability result (1) holds for every integer \(q\ge2\), independent of a field. The extension corollary requires \(q\) to be a prime power of characteristic greater than four, because Newton identities must recover every four-element multiset from its first four power sums. The target \(\ell^8\) norm is an **unnormalized sum**, while \(L^2(\sigma)\) is the normalized curve norm. The zero function satisfies the homogeneous extension inequality trivially, but the probability coordinates in (2) require \(f\ne0\). The result controls amplitudes rather than phases.

Write \(e_j=e_j(\theta)\) for elementary symmetric polynomials, with \(e_0=1\) and \(e_j=0\) beyond the number of available coordinates.

## Proof
**1. Exact four-draw functional.** Partition four ordered draws by multiplicity profiles \((4),(3,1),(2,2),(2,1,1),(1,1,1,1)\). Each ordered tuple contributes its probability times its number \(4!/\prod_i m_i!\) of distinct rearrangements. Expanding and collecting the elementary symmetric sums gives the exact identity
\[
F_4(\theta)=1+12e_2+6e_2^2+60e_3+132e_4.\tag{3}
\]
Equivalently, with \(s_j=\sum_i\theta_i^j\), Newton's formulas give
\[
F_4(\theta)=24-72s_2+18s_2^2+64s_3-33s_4.\tag{4}
\]
Substituting \(\theta=u\) yields the displayed \(A_q\).

**2. A ratio lemma.** For \(r=3,4\), the function \(e_r/e_2\) is Schur-concave on the set of probability vectors with \(e_2>0\). Indeed, for distinct indices \(i,j\) and the remaining coordinate vector \(z\), the elementary-symmetric derivative rule gives
\[
\left(\partial_i-\partial_j\right)\frac{e_r}{e_2}
=\frac{(\theta_j-\theta_i)B_r(z,\theta_i+\theta_j)}{e_2^2},\tag{5}
\]
where
\[
B_r(z,s)=e_{r-2}(z)e_2(z)-e_r(z)
+s\big[e_{r-2}(z)e_1(z)-e_{r-1}(z)\big].\tag{6}
\]
Both bracketed differences are nonnegative for nonnegative \(z\): a product \(e_a(z)e_b(z)\) with \(a+b=r\) contains every squarefree monomial of degree \(r\) at least once (indeed \(\binom r a\) times), in addition to nonnegative repeated-index monomials. The same argument applies to \(a+b=r-1\). Thus \(B_r\ge0\), and multiplication of (5) by \(\theta_i-\theta_j\) is nonpositive. Pairwise averaging therefore cannot decrease \(e_r/e_2\); a succession of such averages approaches \(u\). Continuity extends this conclusion to boundary vectors with \(e_2>0\). Therefore
\[
\frac{e_3(\theta)}{e_2(\theta)}\le\frac{e_3(u)}{e_2(u)},\qquad
\frac{e_4(\theta)}{e_2(\theta)}\le\frac{e_4(u)}{e_2(u)}.\tag{7}
\]
If \(r\) exceeds the alphabet size, its elementary symmetric function is identically zero and the argument remains valid. Likewise, \(e_2(\theta)\le e_2(u)=(q-1)/(2q)\) by Cauchy--Schwarz, with equality exactly at \(u\).

**3. Sharp remainder.** Whenever \(e_2(\theta)>0\), divide (3) by \(2e_2\):
\[
\frac{F_4(\theta)-1}{2e_2(\theta)}
=6+3e_2(\theta)+30\frac{e_3(\theta)}{e_2(\theta)}
+66\frac{e_4(\theta)}{e_2(\theta)}
\le\frac{A_q-1}{2e_2(u)}
=\frac{A_q-1}{1-1/q}=c_q.\tag{8}
\]
The inequality is strict unless \(\theta=u\), because the coefficient of \(e_2\) is positive and \(e_2\) is uniquely maximized at \(u\). For \(e_2=0\), nonnegativity and total mass one force a point mass, and (3) gives \(F_4=1\). Thus, for all \(\theta\),
\[
F_4(\theta)\le1+2c_qe_2(\theta).\tag{9}
\]
Finally \(\sum_i(\theta_i-1/q)^2=s_2-1/q=(1-1/q)-2e_2\) and \(A_q=1+(1-1/q)c_q\), so (9) is exactly (1). Both uniform and point masses give equality; point masses have positive squared distance \(1-1/q\), proving optimality of \(c_q\). These are the only equality cases.

**4. Fourier transfer.** Character orthogonality expands the eighth target moment into pairs of ordered four-tuples whose first four power sums agree. In characteristic \(p>4\), Newton's identities recover the same elementary symmetric polynomials and hence the same multiset. Every four-tuple therefore has exactly \(M(T)\) partners, with a common product of squared moduli. Dividing by the normalization yields the exact identity
\[
\|Ef\|_{\ell^8(\mathbb F_q^4)}^8=N^4F_4(\theta).\tag{10}
\]
Multiplying (1) by \(N^4\) proves (2), its optimality and all equality cases. The field trace defining the additive character works in arbitrary extension fields of the stated characteristic.

## Verification
The self-contained `CHECK.py` performs exact rational enumeration of the four-draw rearrangement expectation for \(1494\) probability vectors on alphabets of sizes two through five, compares it independently with both polynomial identities (3) and (4), checks (1), (9), and the equality classification, and verifies \(10878\) instances of the sign expression (6). It separately evaluates six direct complex eighth Fourier moments on the quartic moment curves over \(\mathbb F_5\) and \(\mathbb F_7\) and compares with the exact probabilistic identity (10). The successful output was:

`CHECK_OK exact_probability_vectors=1494 complex_Fourier_eighth_moments=6 Schur_derivative_checks=10878`

Run `python3 CHECK.py` from the directory containing the extracted file, using Python's standard library. The exact theorem is proved by (3)--(10), not by finite checks; the complex Fourier comparisons are numerical sanity checks with a stated tolerance.

## Relationship to prior work
Biswas, Carneiro, Flock, Madrid, Oliveira e Silva, Stovall and Tautges (arXiv:2609.29882v1, first posted September 24, 2026) prove that the uniform law uniquely maximizes \(F_d\) and establish the exact finite-field Fourier reduction, but do not claim a sharp fourth-draw global quadratic coefficient. Gonçalves (arXiv:2609.31979v1, September 25, 2026) proves a stronger *qualitative* component-wise permutation-match comparison, without the distance remainder here.

*Quadratic stability for endpoint finite-field moment-curve extension* (published mathematical finding October 2026) gives the general valid coefficient \(d(d-1)/2\); at \(d=4\) that is \(6\), strictly smaller than the optimal \(c_q\) for every admissible field size \(q\ge5\). *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer* computes a local Hessian, not the global best coefficient. *Sharp global quadratic stability of cubic moment-curve Fourier extension* (November 2026) determines the exact corresponding degree-three coefficient \(5-4/q\); it does not cover four draws. Elementary-symmetric ratio monotonicity is used as a transparent proof device and no general discovery of this classical technique is claimed.

## Limitations
No extension to moments beyond the fourth sample, to characteristics at most four, to Euclidean Fourier extension, or to pointwise phase stability is asserted. Although all coefficient phases are allowed, the eighth moment depends only on their magnitudes in this special endpoint model. The global optimum is fixed by point-supported boundary data, whereas uniform data represent the zero-deficit case. Possible older equivalents in the majorization literature remain a bibliographic risk; the closest sources were compared for mathematical implication, not merely title similarity. No independent mathematical audit has been performed.

## References
1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall and J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1, first posted 2026-09-24, https://arxiv.org/abs/2609.29882 .
2. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1, first posted 2026-09-25, https://arxiv.org/abs/2609.31979 .
3. *Quadratic stability for endpoint finite-field moment-curve extension*, public finding, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-quadratic-stability-for-endpoint-finite-field-moment-curve-exten--e3a60ec2aa94 .
4. *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer*, public finding, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-isotropic-quadratic-stability-at-the-uniform-finite-field-moment--49b4f93ca348 .
5. *Sharp global quadratic stability of cubic moment-curve Fourier extension*, public finding, November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-global-quadratic-stability-of-cubic-moment-curve-fourier-e--3c25c0192069 .
