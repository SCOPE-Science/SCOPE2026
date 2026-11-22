# All-order alternating-coefficient theorem for optimized truncated-trapezoidal symbols

## Finding

**Theorem (sharp circular symbol norm at every truncation order).** Fix an integer \(J\ge2\). Let \(\delta_J\) be the uniquely optimized \(J\)-th truncated-trapezoidal-rule symbol of Ferrari [1], i.e. the real polynomial
\[
\delta_J(z)=(1-z)+\frac12(1-z)^2+\sum_{\ell=2}^{J}2^{-\ell}c_{\ell}^{J}(1-z)^{\ell+1},
\]
with the coefficients maximizing \(c_2^J\) subject to A-stability as specified in [1, Theorem 3.1]. Write \(\delta_J(z)=\sum_{k=0}^{J+1}d_{J,k}z^k\). Then **every coefficient is nonzero with strict alternating sign**:
\[
(-1)^k d_{J,k}>0\qquad(0\le k\le J+1).
\]
In particular, for **every real radius \(r>0\)**,
\[
\max_{|z|\le r}|\delta_J(z)|=\max_{|z|=r}|\delta_J(z)|=\delta_J(-r),
\]
where \(z=-r\) is the unique maximizer. At the unit radius, the exact sharp value is
\[
\boxed{\max_{|z|\le1}|\delta_J(z)|=\frac{4}{(J+1)\sin^2\!\bigl(\pi/[2(J+1)]\bigr)}.}
\]
Thus the conjecture stated in [1, Section 5.1, footnote 3] holds at **all** truncation orders, not just the first five orders checked there. The stronger coefficient formula and circular-radius identity give sharp bounds also on nonunit contours.

## Assumptions and scope

The truncation index \(J\) is any integer at least two; all coefficients are the optimal real parameters defined in [1] rather than arbitrary coefficients of an A-stable multistep method. The variable \(z\) is complex, and \(r\) is any strictly positive real number. All maxima are complex absolute values of the polynomial symbol itself, not of a CQ solution or of an inverse operator-valued Laplace transform. No restriction on data regularity or timestep is needed for the algebraic assertion.

Define \(x=\pi/(J+1)\), \(q_j=\sin((j+1)x)\) for \(0\le j\le J-1\) and \(q_j=0\) outside that range, and set
\[
P_J(w)=(1+w)^2\sum_{j=0}^{J-1}q_jw^j=\sum_{j=0}^{J+1}a_jw^j,\qquad a_j=q_j+2q_{j-1}+q_{j-2}.
\]
Every \(a_j\) is strictly positive because all the nonzero \(q_j\) are positive. Define the positive constant
\[
C_J=\frac{1}{2(J+1)(1+\cos x)}.
\]
An explicit version of the theorem is
\[
d_{J,0}=C_J\sum_{j=0}^{J+1}a_j^2,\qquad
 d_{J,k}=2C_J(-1)^k\sum_{j=0}^{J+1-k}a_ja_{j+k}
 \quad(1\le k\le J+1).
\]
This formula remains valid even when some optimized coefficients \(c_\ell^J\) in the shifted basis become negative: the signs of the ordinary polynomial coefficients \(d_{J,k}\) are nevertheless rigid.

## Proof

**1. Fejér spectral factor of the optimal dissipation polynomial.** Ferrari [1, Lemma 4.2] proves, for \(|z|=1\) with \(z=e^{i\theta}\),
\[
\operatorname{Re}\delta_J(z)=\sin^4(\theta/2)\,T_J(\theta),
\]
where the real trigonometric polynomial \(T_J\) has constant Fourier coefficient \(4-2c_2^J\), first cosine coefficient \(-4c_2^J\), and higher cosine coefficients given in [1, Equation (30)]. Its optimal parameter is [1, Theorem 3.1]
\[
c_2^J=\frac{2\cos x}{1+\cos x}.
\]
Set \(Q_J(w)=\sum_{j=0}^{J-1}q_jw^j\) and \(S=\sum_{j=0}^{J-1}q_j^2=(J+1)/2\). The product-to-sum formula gives, for \(1\le k\le J-1\),
\[
\sum_{j=0}^{J-1-k}q_jq_{j+k}
=\frac12\left[(J-k)\cos(kx)+\frac{\sin((k+1)x)}{\sin x}\right].
\]
Consequently the constant and higher cosine coefficients of
\[
\frac{4-2c_2^J}{S}|Q_J(-e^{i\theta})|^2
\]
are precisely those of \(T_J\), using [1, Equation (30)]. The first cosine coefficient also agrees, because the eigenvector identity \(\sum q_jq_{j+1}=S\cos x\) gives the normalized value \(-2\cos x\), which equals \(-4c_2^J/(4-2c_2^J)\). Therefore
\[
T_J(\theta)=\frac{4-2c_2^J}{S}|Q_J(-e^{i\theta})|^2.
\]
This is a direct coefficient reconstruction of the extremal trigonometric polynomial, rather than an assumption that all shifted-basis coefficients are positive.

**2. Strictly alternating Taylor coefficients.** Since \(\sin^4(\theta/2)=|1-z|^4/16\) on the unit circle,
\[
\operatorname{Re}\delta_J(z)=\frac{4-2c_2^J}{16S}|(1-z)^2Q_J(-z)|^2
=C_J|P_J(-z)|^2.
\]
The last equality follows from \(4-2c_2^J=4/(1+\cos x)\). Expanding \(P_J\) gives
\[
|P_J(-e^{i\theta})|^2
=\sum_{j=0}^{J+1}a_j^2
 +2\sum_{k=1}^{J+1}(-1)^k
   \left(\sum_{j=0}^{J+1-k}a_ja_{j+k}\right)\cos(k\theta).
\]
On the other hand, because \(\delta_J(z)=\sum d_{J,k}z^k\) has real coefficients,
\[
\operatorname{Re}\delta_J(e^{i\theta})
=d_{J,0}+\sum_{k=1}^{J+1}d_{J,k}\cos(k\theta).
\]
Uniqueness of the finite Fourier cosine expansion proves the displayed formula for every \(d_{J,k}\). Each correlation sum is strictly positive, establishing \((-1)^kd_{J,k}>0\) for every index. No finite enumeration or sign sampling is used in this deduction.

**3. Sharpness and uniqueness at every radius.** For \(|z|\le r\), the triangle inequality and strict coefficient signs yield
\[
|\delta_J(z)|\le \sum_{k=0}^{J+1}|d_{J,k}|\,|z|^k
\le\sum_{k=0}^{J+1}|d_{J,k}|\,r^k=\delta_J(-r).
\]
At \(z=-r\) all summands are strictly positive real numbers, so equality holds. If \(r>0\), equality first forces \(|z|=r\), since at least the first-degree coefficient is nonzero. Equality in the complex triangle inequality then forces \(d_{J,1}z\) to have the positive real phase of \(d_{J,0}>0\); since \(d_{J,1}<0\), necessarily \(z=-r\). The maximizer is therefore unique.

**4. Exact endpoint value.** At \(r=1\), the correlation identity gives
\[
\delta_J(-1)=C_J\Big(\sum_{j=0}^{J+1}a_j\Big)^2.
\]
The polynomial factorization implies \(\sum a_j=4\sum_{j=0}^{J-1}q_j\), and the finite sine sum under \((J+1)x=\pi\) gives \(\sum_{j=0}^{J-1}q_j=\cot(x/2)\). Hence
\[
\delta_J(-1)=\frac{8\cot^2(x/2)}{(J+1)(1+\cos x)}
=\frac{4}{(J+1)\sin^2(x/2)},
\]
as claimed. Its large-\(J\) asymptotic is \(16(J+1)/\pi^2\), consistent with [1, Proposition 3.6 and Remark 3.7]. This closes the proof. \(\square\)

## Verification

The analytic argument covers infinitely many values of \(J\) and every complex radius; finite numerical checks are only independent diagnostics. The included `verify.py` reconstructs the optimized parameters using Ferrari's inverse-binomial coefficient formula [1, Lemma 4.3 and Equation (30)], independently expands the generating polynomial, and compares each coefficient to the newly derived autocorrelation formula. At 110 decimal digits it checks every order \(2\le J\le30\), strict coefficient signs, endpoint values, and sampled angular inequalities for radii \(0.1\), \(0.5\), \(1\), and \(1.7\). The actual execution returned `VERIFY_OK 5394`. Run it with Python 3 and the `mpmath` package installed using `python verify.py`.

For a simple exact consistency check, \(J=2\) gives \(c_2^2=2/3\) and
\[
\delta_2(z)=\frac53-\frac52z+z^2-\frac16z^3,
\qquad \delta_2(-1)=\frac{16}{3},
\]
which matches the universal formula. These checks do not replace the proof or certify results outside its stated hypotheses.

## Relationship to prior work

Ferrari [1] supplies the A-stable optimal coefficients, the trigonometric factorization of the real part, and the exact endpoint value. In Section 5.1, footnote 3, [1] explicitly conjectures that the endpoint also controls the supremum for every order, observing a proof only up to \(J=6\) under positivity of the shifted-basis coefficients. This theorem proves that conjecture for all \(J\), strengthens it to every circular radius, and supplies a strictly alternating ordinary-coefficient formula. It does not claim novelty for the previously established optimized coefficients or endpoint evaluation.

Banjai [2, Section 6] introduced truncated trapezoidal symbols and numerically optimized an instance with finite \(J\). That construction neither states nor implies the complete optimal-family coefficient-sign theorem. The Fejér trigonometric extremal theorem used by Ferrari [1, Theorem 4.1] is classical; the new step is translating the positive spectral factor into strictly alternating **analytic-symbol** coefficients, which yields the sharp circular norms. The literature comparison does not establish historical uniqueness beyond the searched sources.

## Limitations

The result addresses only Ferrari's specifically optimized real polynomial family, not every A-stable truncated-trapezoidal choice or arbitrary multistep method. An exact supremum of the scalar discrete symbol can inform CQ contour bounds but is not itself a convergence theorem, a sharp operator perturbation threshold, or a claim about practical floating-point errors. The proof relies on the published Fejér-extremal representation and optimality relations, and an independent mathematical audit has not been performed.

## References

[1] M. Ferrari, *Convolution quadrature based on a truncated trapezoidal rule*, arXiv:2607.11422 (first public version July 13, 2026). https://arxiv.org/abs/2607.11422 . See especially Theorem 3.1, Lemmas 3.8 and 4.2–4.3, Equation (30), Proposition 3.6, and Section 5.1 footnote 3.

[2] L. Banjai, *Implicit/explicit, BEM/FEM coupled scheme for acoustic waves with the wave equation in the second order formulation*, arXiv:2203.00986 (2022). https://arxiv.org/abs/2203.00986 . See Section 6.
