# Sharp global quadratic stability of cubic moment-curve Fourier extension

## Finding
Let \(q=p^n\) be any prime power with \(p>3\). On the cubic moment curve
\[
\Gamma_q=\{\gamma(t)=(t,t^2,t^3):t\in\mathbb F_q\}\subseteq\mathbb F_q^3
\]
use normalized curve measure \(\sigma\), an arbitrary nontrivial additive character \(\psi\), and counting measure in the target. Define
\[
E f(\xi)=q^{-1}\sum_{t\in\mathbb F_q}f(t)\psi(\xi\cdot\gamma(t)),\qquad
N=q^{-1}\sum_t|f(t)|^2>0,\qquad
\theta_t=\frac{|f(t)|^2}{qN}.
\]
Set \(u_t=1/q\) and \(A_q=6-9/q+4/q^2\). The **optimal global quadratic stability inequality** is
\[
\boxed{A_q N^3-\|Ef\|_{\ell^6(\mathbb F_q^3)}^6
\geq \left(5-\frac4q\right)N^3\sum_{t\in\mathbb F_q}\left(\theta_t-\frac1q\right)^2.}\tag{1}
\]
No coefficient larger than \(5-4/q\) holds for all nonzero \(f\). Equality in (1) occurs **exactly** when either all \(|f(t)|\) are equal and nonzero or \(f\) is supported at exactly one curve point. Phases are unrestricted.

In amplitude coordinates, the same sharp remainder is
\[
A_qN^3-\|Ef\|_6^6\ge\frac{5-4/q}{q}N\,
\big\||f|^2-N\big\|_{L^2(\sigma)}^2.\tag{2}
\]
For any probability vector \(\theta\) on \(q\) symbols, define elementary symmetric functions \(e_2(\theta),e_3(\theta)\). The stronger exact deficit decomposition is
\[
\boxed{A_q-F_3(\theta)
=\left(5-\frac4q\right)\|\theta-u\|_2^2
+\frac4q\big((q-2)e_2(\theta)-3q e_3(\theta)\big),}\tag{3}
\]
where \(F_3(\theta)\) is the expected number of distinct rearrangements of three independent draws with distribution \(\theta\). Both terms on the right of (3) are nonnegative.

## Assumptions and scope
The field has cardinality \(q=p^n\) with prime characteristic \(p>3\), so the first three power sums determine the multiset of any three elements. For \(f=0\), inequality (2) holds trivially, while (1) is stated for \(f\ne0\) to define \(\theta\). The target norm is **unnormalized counting** \(\ell^6\); the Fourier extension averages over the \(q\) curve points as above. All assertions hold over every extension field of allowed characteristic, not just prime fields. Nothing is claimed for the Euclidean extension operator or characteristic two or three.

## Proof
**(i) Moment-curve fiber identity.** Character orthogonality applied to \(\|Ef\|_6^6\) gives
\[
\|Ef\|_6^6=q^{-3}\!
\sum_{\substack{\boldsymbol s,\boldsymbol t\in\mathbb F_q^3\\
\sum_i\gamma(s_i)=\sum_i\gamma(t_i)}}
\prod_{i=1}^3 f(s_i)\overline{f(t_i)}.
\]
For \(p>3\), Newton's identities recover the elementary symmetric functions of a triple from its first three power sums. Thus equality of all three coordinate sums is equivalent to equality of the underlying multisets. Every ordered triple \(\boldsymbol s\) therefore has precisely
\(M(\boldsymbol s)=3!/\prod_a m_a!\) distinct ordered partners, all contributing \(\prod_i|f(s_i)|^2\). Since \(\sum_t |f(t)|^2=qN\), it follows exactly that
\[
\|Ef\|_6^6=N^3\mathbb E_\theta[M(T)]=N^3 F_3(\theta).\tag{4}
\]
This identity is independent of the phases of \(f\).

**(ii) An explicit cubic probability functional.** Put \(s_k=\sum_a\theta_a^k\) and \(e_3=\sum_{a<b<c}\theta_a\theta_b\theta_c\). The all-equal, exactly-two-equal, and all-distinct sample types contribute respectively \(s_3\), \(9(s_2-s_3)\), and \(36e_3\). As \(6e_3=1-3s_2+2s_3\),
\[
F_3(\theta)=6-9s_2+4s_3,\qquad F_3(u)=A_q.\tag{5}
\]
Since \(\|\theta-u\|_2^2=s_2-1/q\) and \(s_2=1-2e_2\), \(s_3=1-3e_2+3e_3\), elementary rearrangement of (5) gives the exact identity (3).

**(iii) Sharp nonnegative remainder.** For a probability vector on \(q\ge3\) symbols, the normalized Newton inequality \((e_2/\binom q2)^2\ge (e_1/q)(e_3/\binom q3)\), with \(e_1=1\), yields
\[
e_3\le \frac{2(q-2)}{3(q-1)}e_2^2.\tag{6}
\]
Also \(e_2=(1-s_2)/2\le(q-1)/(2q)\) by Cauchy--Schwarz. Combining these bounds gives
\[
3q e_3\le \frac{2q(q-2)}{q-1}e_2^2\le(q-2)e_2.\tag{7}
\]
Consequently both right-hand terms in (3) are nonnegative, proving (1) through (4). Equality in (7) requires \(e_2=0\), hence a point mass, or \(e_2=(q-1)/(2q)\), hence uniformity. This proves all equality cases in (1). Substitution of \(\theta_t=|f(t)|^2/(qN)\) yields (2).

**(iv) Optimal coefficient.** At a point mass, \(F_3=1\), while \(\|\theta-u\|_2^2=1-1/q\). Thus
\[
\frac{A_q-1}{1-1/q}=5-\frac4q,
\]
so no larger global coefficient can hold. At the uniform law the deficit and the distance both vanish. For comparison, expanding (5) near \(u\) gives
\[
A_q-F_3(u+h)=\left(9-\frac{12}{q}\right)\|h\|_2^2-4\sum_a h_a^3,\quad \sum_a h_a=0.
\]
Hence the optimal global coefficient is strictly smaller than the local quadratic curvature for \(q>2\); a boundary point, rather than a near-uniform perturbation, fixes the sharp constant.

## Verification
The standalone `CHECK.py` uses exact rational arithmetic to enumerate 276 probability vectors on symbol sets of sizes \(5,7,11\), independently computes \(F_3\) both by ordered-triple enumeration and by (5), tests the exact identity (3), nonnegativity, and equality classification, and checks eight direct complex Fourier sixth moments for prime fields of sizes \(5,7\). Executing `python3 CHECK.py` produced:

`CHECK_OK exact_probability_vectors= 276 direct_Fourier_tests= 8 cases= [(5, 126, 'point_mass,uniform'), (7, 84, 'point_mass'), (11, 66, 'point_mass')]`

These finite calculations are only cross-checks. The unrestricted theorem follows from Newton identities, character orthogonality, and symmetric-function inequalities, not from enumeration. The checker requires Python standard libraries only.

## Relationship to prior work
Biswas, Carneiro, Flock, Madrid, Oliveira e Silva, Stovall and Tautges (arXiv:2609.29882v1, first posted 2026-09-24) establish the sharp endpoint moment-curve extension theorem, its rearrangement-expectation reduction, and constant-modulus extremizers. Gonçalves (arXiv:2609.31979v1, 2026-09-25) obtains a stronger qualitative component-wise permutation-match inequality. These establish the underlying maximization principle; neither accessible statement gives the global sharp quadratic coefficient here.

The public record *Quadratic stability for endpoint finite-field moment-curve extension* (October 2026) establishes an all-degree quantitative remainder with coefficient \(d(d-1)/2\), explicitly without claiming its optimality for \(d>2\). At the cubic degree, that gives \(3\), versus the sharp \(5-4/q\) in (1). The public record *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer* computes the exact **local** Hessian but makes no global sharpness claim. Equation (3), the exact global constant, and equality at both the uniform and point-mass laws distinguish the present theorem from both results. The symmetric-function inequalities used in the proof are classical and are not claimed as new.

## Limitations
The improvement is confined to cubic moment-curve extension, the first endpoint with a nonlinear probability functional; it does not optimize the global remainder for general moment-curve degree. The exact moment identity requires characteristic greater than three. The deficit controls squared amplitudes but cannot control phases, which are invisible to this Fourier moment. Direct full-text comparisons with the two 2026 preprints were not available in this review; their abstracts, a detailed secondary exposition, and two highly relevant full published mathematical findings were inspected. A concealed equivalent exact global coefficient in an inaccessible full manuscript or older majorization literature remains a residual originality risk. No independent review has been performed.

## References
1. C. Biswas, E. Carneiro, T. C. Flock, J. Madrid, D. Oliveira e Silva, B. Stovall, J. Tautges, *Sharp endpoint extension inequalities for the moment curve on finite fields II: an extremal property of the uniform distribution*, arXiv:2609.29882v1, 24 September 2026, https://arxiv.org/abs/2609.29882 .
2. F. Gonçalves, *A component-wise inequality for permutation matches*, arXiv:2609.31979v1, 25 September 2026, https://arxiv.org/abs/2609.31979 .
3. *Quadratic stability for endpoint finite-field moment-curve extension*, public mathematical result, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-quadratic-stability-for-endpoint-finite-field-moment-curve-exten--e3a60ec2aa94 .
4. *Isotropic quadratic stability at the uniform finite-field moment-curve extremizer*, public mathematical result, October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-isotropic-quadratic-stability-at-the-uniform-finite-field-moment--49b4f93ca348 .
5. Classical Newton inequalities for elementary symmetric means (used only as a standard algebraic input).
