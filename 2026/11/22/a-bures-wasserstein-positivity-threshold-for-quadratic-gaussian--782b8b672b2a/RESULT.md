# A Bures–Wasserstein positivity threshold for quadratic Gaussian integral kernels

## Finding

For every integer \(d\ge1\), let \(A,D\) be real symmetric \(d\times d\) matrices, \(b>0\), and \(s>b/2\). Consider the integral operator \(T\) on \(L^2(\mathbb R^d)\) with continuous kernel
\[
K(x,y)=e^{-s(\|x\|^2+\|y\|^2)+b\langle x,y\rangle}
\left[1+(x+y)^TA(x+y)-(x-y)^TD(x-y)\right].
\]
**Theorem.** The selfadjoint, trace-class operator \(T\) is positive semidefinite if and only if
\[
A\succeq0,\qquad D\succeq0,\qquad
\operatorname{tr}A+\operatorname{tr}D-2\operatorname{tr}(A^{1/2}DA^{1/2})^{1/2}\le b.
\]
The left side of the last inequality is the squared Bures–Wasserstein distance \(d_{\mathrm{BW}}(A,D)^2\). Singular and noncommuting matrices, equality, and every admissible \(s\) are included.

**Exact scalar benchmark.** The family from Homa and collaborators and Balka–Csordás–Homa has the polynomial \(1+\gamma(x+y)^2-(x-y)^2\) and Gaussian \(\exp[-\tfrac32(x-y)^2-(x+y)^2]\). Here \(A=\gamma\), \(D=b=1\), \(s=5/2\), so its integral operator is positive semidefinite **exactly when** \(0\le\gamma\le4\). A positive normalizing scalar does not change this answer. The 2024 study reports finite-moment exclusion bounds down to approximately \(4.03924\) but does not establish the exact boundary in its inspected example.

For a genuinely noncommuting example take
\[
A=\begin{pmatrix}4&0\\0&1\end{pmatrix},\qquad
D=\frac12\begin{pmatrix}5&3\\3&5\end{pmatrix}.
\]
Then \(d_{\mathrm{BW}}(A,D)^2=10-2\sqrt{20.5}\approx0.94461486186\). Thus for any \(b>0\) and \(s>b/2\), the kernel is positive exactly when \(b\ge10-2\sqrt{20.5}\).

## Assumptions and scope

The matrices are finite-dimensional, real, symmetric, and not assumed positive in advance. The Gaussian is strictly Hilbert–Schmidt integrable because \(2s>b>0\); the polynomial-Gaussian kernel is Schwartz. Its integral operator is selfadjoint and trace class. Positivity is in the Hilbert-space quadratic-form sense, not pointwise nonnegativity of \(K(x,y)\); the polynomial may be negative at some individual pairs even when the operator is positive.

The statement is a theorem for all real \(A,D\) satisfying the stated hypotheses, rather than a finite-Hermite-mode or numerical approximation. A comparison with \(d_{\mathrm{BW}}\) is made only after independently proving \(A,D\succeq0\).

## Proof

**1. Coherent factorization.** Let \(\mathcal F\) be the bosonic Fock space over \(\mathbb C^d\) with orthonormal number basis \(e_\alpha\), \(\alpha\in\mathbb N_0^d\). For real \(x\), define the unnormalized coherent vector
\[
v(x)=\sum_{\alpha\in\mathbb N_0^d}
\frac{b^{|\alpha|/2}x^\alpha}{\sqrt{\alpha!}}e_\alpha.
\]
Its squared norm is \(e^{b\|x\|^2}\) and \(\langle v(x),v(y)\rangle=e^{b\langle x,y\rangle}\). Write \(c_j,c_j^*\) for the annihilation and creation operators and set
\[
Q_j=c_j+c_j^*,\qquad P_j=i(c_j^*-c_j),\qquad [Q_j,P_k]=2i\delta_{jk}I.
\]
The coherent-vector identities, valid initially on the common analytic domain, are
\[
\begin{aligned}
\langle v(x),Q^TAQv(y)\rangle
 &=e^{b\langle x,y\rangle}[\operatorname{tr}A+b(x+y)^TA(x+y)],\\
\langle v(x),P^TDPv(y)\rangle
 &=e^{b\langle x,y\rangle}[\operatorname{tr}D-b(x-y)^TD(x-y)].
\end{aligned}
\]
Consequently, with \(H=Q^TAQ+P^TDP\) and
\[
S=I+\frac1b\bigl[H-(\operatorname{tr}A+\operatorname{tr}D)I\bigr],
\]
we have
\[
K(x,y)=\left\langle e^{-s\|x\|^2}v(x),
S\,e^{-s\|y\|^2}v(y)\right\rangle.
\]

**2. Positivity equivalence (the domain step).** The map \(x\mapsto v(x)\) is analytic in the graph norm of the number operator \(N+I\). Indeed, each derivative of its power series is square-summable uniformly on compact subsets even after multiplication by \(|\alpha|+1\). For any multi-index \(\alpha\), the corresponding mixed derivative at the origin equals \(b^{|\alpha|/2}\sqrt{\alpha!}\,e_\alpha\). Finite differences of coherent vectors therefore approximate every number vector in the graph norm; their span is a form core for any quadratic polynomial in the \(c_j,c_j^*\), because \(|\langle\psi,H\psi\rangle|\le C\langle\psi,(N+I)\psi\rangle\). 

Since the kernel is continuous, positivity of its integral operator implies positivity of each finite kernel Gram matrix: approximate point masses by smooth localized test functions in the integral quadratic form. The coherent identity then gives \(\langle\psi,S\psi\rangle\ge0\) on all finite coherent spans, hence on the finite-particle core. Conversely, if this last form is nonnegative, the coherent Gram matrices are positive; integrating against simple functions and then using density gives \(T\succeq0\). Thus \(T\succeq0\) if and only if the quadratic form of \(S\) is nonnegative on finite-particle vectors. The factors \(e^{-s\|x\|^2}>0\) do not affect the sign. This justifies the equivalence rather than assuming that a finite-dimensional truncation proves positivity.

**3. Necessity of the two matrix inequalities.** If \(u^TAu<0\) for a real unit vector \(u\), apply a Weyl displacement translating the expectation of \(Q\) by \(t u\) in a fixed normalized finite-energy Gaussian vector, while keeping the variance of \(Q\) and the mean and variance of \(P\) fixed. Then the expectation of \(H\) equals \(t^2 u^TAu+O(t)+O(1)\), and is unbounded below. A momentum displacement likewise proves that a negative direction of \(D\) makes \(H\) unbounded below. Approximate the displaced vectors by finite-particle vectors in the quadratic-form norm. Therefore positivity forces \(A,D\succeq0\).

**4. Exact oscillator lower bound.** Suppose first \(A,D\) are positive definite. Make the canonical linear change of quadratures \(Q'=A^{1/2}Q\), \(P'=A^{-1/2}P\). These still satisfy \([Q'_j,P'_k]=2i\delta_{jk}\), and
\[
H=(Q')^TQ'+(P')^T(A^{1/2}DA^{1/2})P'.
\]
A common orthogonal rotation diagonalizes the positive symmetric matrix in the second term without changing the canonical commutation relations. In each independent mode, the harmonic oscillator \(Q'^2+\lambda P'^2\) has lower bound \(2\sqrt\lambda\), attained by its squeezed ground state. Hence
\[
\inf_{\|\psi\|=1}\langle\psi,H\psi\rangle
=2\operatorname{tr}(A^{1/2}DA^{1/2})^{1/2}.
\]
For positive semidefinite, possibly singular \(A,D\), apply the positive-definite result to \(A+\varepsilon I,D+\varepsilon I\). The corresponding forms decrease pointwise on finite-particle vectors as \(\varepsilon\downarrow0\); the variational infima converge to the infimum of the limiting form by testing any fixed finite-particle vector, while the square-root traces converge continuously. Thus the displayed equality remains valid at singularity, whether or not the infimum is attained.

**5. Conclusion.** The lowest form bound of \(S\) is
\[
\inf S=1-\frac{\operatorname{tr}A+\operatorname{tr}D-
2\operatorname{tr}(A^{1/2}DA^{1/2})^{1/2}}{b}.
\]
Combining Steps 2–4 proves both directions of the criterion, including equality and the independence of \(s\).

## Verification

The accompanying `check.py` recomputes coherent-vector kernel identities and all entries of the scalar parity-banded Fock matrix for several parameters; it also checks scalar and noncommuting Bures formulas and compares truncated oscillator spectra with the rigorous variational lower bound. Run `python check.py` with NumPy installed. The embedded script completed 7,855 numerical algebra and variational assertions in the reported run. All finite computations are supplemental diagnostics. Infinite-dimensional positivity, necessity, singular limits, and the sharp boundary follow from the proof above, not from extrapolation of the numerical tests.

## Relationship to prior work

Homa–Balka–Bernád–Károly–Csordás (arXiv:2207.06119, first public 2022-07-13) give a countable, moment-based positivity criterion and calculate finite conditions for scalar polynomial-Gaussian integral kernels. Balka–Csordás–Homa (arXiv:2405.04438, first public 2024-05-07), especially their Section 2.3.1 and Table 1, study the exact scalar polynomial \(1+\gamma(x+y)^2-(x-y)^2\). Their finite-order moment bounds approach \(4\) from above but do not supply an exact admissibility interval in the inspected sections. The present theorem gives precisely \([0,4]\) and extends it to a complete matrix-valued, possibly noncommuting and singular family. Their general results on Gaussian positivity and Gaussian-kernel preorder are compatible with, but do not directly yield, this sharp coefficient criterion.

The matrix distance was previously studied by Bhatia–Jain–Lim (arXiv:1712.01504, first public 2017-12-05). Its metric theory, by itself, does not assert positivity of polynomial-Gaussian integral operators. The present connection follows from coherent-kernel factorization and the oscillator minimum.

## Limitations

The Gaussian covariance is isotropic and real, the cross-coupling is the scalar \(bI\), and the multiplier is exactly the indicated quadratic in \(x+y\) and \(x-y\). The theorem does not assert a positivity condition for arbitrary quadratic multipliers, anisotropic cross-Gaussians or complex phase twists. A bounded operator outside the strict integrability range \(s>b/2\) is not addressed. The historical-priority comparison is evidence-based rather than a proof that no equivalent result exists in unindexed literature. No independent mathematical audit has been performed.

## References

1. G. Homa, R. Balka, J. Z. Bernád, M. Károly, A. Csordás, *Newton's identities and positivity of trace class integral operators*, arXiv:2207.06119 (first posted 2022-07-13). https://arxiv.org/abs/2207.06119
2. R. Balka, A. Csordás, G. Homa, *Positivity and entanglement of polynomial Gaussian integral operators*, arXiv:2405.04438 (first posted 2024-05-07). https://arxiv.org/abs/2405.04438
3. R. Bhatia, T. Jain, Y. Lim, *On the Bures–Wasserstein distance between positive definite matrices*, arXiv:1712.01504 (first posted 2017-12-05). https://arxiv.org/abs/1712.01504
