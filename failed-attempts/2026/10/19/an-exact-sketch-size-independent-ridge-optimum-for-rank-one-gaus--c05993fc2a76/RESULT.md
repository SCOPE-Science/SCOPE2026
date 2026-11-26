# An exact sketch-size-independent ridge optimum for rank-one Gaussian generalized Nyström

## Finding
For the two-dimensional diagonal benchmark, a QR-normalized generalized Nyström core with a single right Gaussian direction and \(s\) independent left Gaussian test directions has an **exact, unique Frobenius-risk-optimal ridge parameter**:
\[
\boxed{\lambda_* = \frac{ab}{a^2-ab+b^2},\qquad a\ge b>0,\quad s\ge1.}
\]
The parameter does not depend on \(s\), even though the benefit of regularization does. Its complete expected squared Frobenius loss is
\[
R_s(\lambda)=ab+\mathbb E_{W_s\sim\chi_s^2}\left[
\frac{\lambda^2(a^2-ab+b^2)+abW_s}{(W_s+\lambda)^2}\right],\qquad\lambda>0,
\]
with attained minimum
\[
R_s(\lambda_*)=ab\left(1+\mathbb E\frac1{W_s+\lambda_*}\right).
\]
In particular, the unregularized squared loss is not integrable with one or two left sketch rows; for three or more it has exact expectation \(ab(s-1)/(s-2)\). A positive ridge yields finite error moments of every fixed order.

The same theorem exposes an objective conflict: on a scalar identity matrix, a ridge improves Frobenius risk but worsens the error in the original matrix trace. This is a benchmark for choosing low-rank stage approximation parameters, **not** a convergence theorem for a randomized integrator.

## Assumptions and scope
Fix real numbers \(a\ge b>0\), integer \(s\ge1\), and the matrix \(B=\operatorname{diag}(a,b)\). Choose independent standard Gaussian \(x\in\mathbb R^2\) and \(\Psi\in\mathbb R^{2\times s}\). The single normalized right direction and ridge-regularized approximation are
\[
q=\frac{Bx}{\|Bx\|_2},\qquad
\widehat B_\lambda
=q\frac{(\Psi^{\mathsf T}q)^{\mathsf T}\Psi^{\mathsf T}B}
{\|\Psi^{\mathsf T}q\|_2^2+\lambda},\qquad \lambda\ge0.
\]
The value at \(\lambda=0\) uses the almost-surely nonzero denominator (equivalently a rank-one pseudoinverse). The ridge is applied to the **QR-normalized core**, so its parameter is dimensionless; it is not a ridge applied directly to the unnormalized sketch product. Each \(\lambda\) is deterministic and is held constant independently of \(x\) and \(\Psi\). All statements are in exact arithmetic. The expectation is over both sketches.

## Proof
**1. Exact Gaussian error decomposition.** Given \(q\), select an orthogonal unit companion \(q_\perp\), and write \(p=q^{\mathsf T}B\) and \(r=q_\perp^{\mathsf T}B\) (row vectors). Rotational invariance makes \(U=\Psi^{\mathsf T}q\) and \(V=\Psi^{\mathsf T}q_\perp\) independent standard Gaussian vectors in \(\mathbb R^s\), independent of the random right direction. Put \(W=\|U\|_2^2\). Conditional on \(U\), the scalar \(U^{\mathsf T}V\) has distribution \(\sqrt W Z\), where \(Z\sim N(0,1)\) is independent of \(W\sim\chi_s^2\) and the right sketch. Orthogonal output-row decomposition now gives the *samplewise* identity
\[
\|B-\widehat B_\lambda\|_F^2
=\|r\|_2^2+
\left\|\frac{\lambda p-\sqrt W Zr}{W+\lambda}\right\|_2^2.
\tag{1}
\]
For \(\lambda=0\), the second term is \(Z^2\|r\|_2^2/W\).

**2. The right Gaussian angle integral.** Writing \(x/\|x\|=(\cos\theta,\sin\theta)\), where \(\theta\) is uniform on a circle, yields
\[
q_1^2=\frac{a^2\cos^2\theta}{a^2\cos^2\theta+b^2\sin^2\theta},
\qquad \mathbb E q_1^2=\frac{a}{a+b}.
\]
For example, the second equality follows by \(t=\tan\theta\) in the quadrant integral and elementary partial fractions, and it remains true at \(a=b\) by continuity. Therefore
\[
\mathbb E\|p\|_2^2=a^2-ab+b^2,
\qquad \mathbb E\|r\|_2^2=ab.
\tag{2}
\]
The latter is the ordinary one-sided Gaussian range-finding residual; it is included here as a known baseline, not claimed as an independent result.

**3. Risk and exact optimum.** Conditional expectation of (1) over \(Z\), followed by (2), proves the displayed risk formula. For every \(\lambda>0\), differentiation under the chi-square integral is justified on compact positive intervals by integrable rational bounds, yielding
\[
R_s'(\lambda)
=2\big[\lambda(a^2-ab+b^2)-ab\big]
\mathbb E\frac{W}{(W+\lambda)^3}.
\tag{3}
\]
The expectation factor is strictly positive for every integer \(s\ge1\). Consequently the derivative is negative below the stated \(\lambda_*\) and positive above it. At the minimizer, the numerator in the risk integrand becomes \(ab(W+\lambda_*)\), proving its exact attained value. Monotone convergence of the error integrand at \(\lambda\downarrow0\) shows that the optimum is global even if \(R_s(0)\) is infinite.

**4. Moment boundaries.** At zero ridge, (1) reads
\[
\|B-\widehat B_0\|_F^2=\|r\|_2^2\left(1+\frac{Z^2}{W}\right).
\tag{4}
\]
Because \(b\le\|r\|_2\le a\), finiteness of the \(p\)-th error moment is equivalent to \(\mathbb E W^{-p/2}<\infty\), since \(Z\) has all positive moments. The chi-square density behaves like a positive constant times \(w^{s/2-1}\) near zero; thus the condition is exactly \(0<p<s\). For \(s>2\), \(\mathbb E W^{-1}=1/(s-2)\), yielding the explicit unregularized risk. At positive ridge, \(\sqrt W/(W+\lambda)\le1/(2\sqrt\lambda)\), and (1) bounds the error by a constant depending on \(a,b,\lambda\) times \(1+|Z|\); hence every positive error moment is finite.

**5. Trace and full isotropic tail.** If \(a=b=t>0\), then \(p=tq^{\mathsf T}\) and \(r=tq_\perp^{\mathsf T}\). The trace of the mixed term in (1)'s underlying matrix decomposition is zero because \(q^{\mathsf T}q_\perp=0\), so
\[
\operatorname{tr}(\widehat B_\lambda)=t\frac{W}{W+\lambda}.
\]
For every fixed \(W>0\), the absolute discrepancy from \(\operatorname{tr}B=2t\) increases strictly with \(\lambda\). Hence its square expectation also increases, whereas (3) makes positive ridge strictly favorable to Frobenius risk until the optimum \(\lambda_*=1\). Finally, (4) yields \(\|B-\widehat B_0\|_F=t\sqrt{1+Z^2/W}\). The squared ratio \(Z^2/(Z^2+W)\) has the beta distribution with parameters \((1/2,s/2)\), proving
\[
\Pr\{\|B-\widehat B_0\|_F>z\}=I_{t^2/z^2}(s/2,1/2),\qquad z\ge t,
\]
where \(I\) is the regularized incomplete beta function. This completes all statements for every specified \(a,b,s\) and parameter range.

## Verification
The included `verify.py` uses exact symbolic differentiation, generalized Laguerre quadrature for chi-square expectations, deterministic direct-sketch matrix evaluations, angle quadrature, and the beta–Student distribution identity. Its fixed-seed execution reports **6,049 checks passed**. These are finite reproducibility checks; the proof of all-parameter claims is the analytic argument above. Run `python verify.py` with NumPy, SymPy, and SciPy installed. No external datasets are needed.

## Relationship to prior work
Lam, Ceruti, and Kressner (2024) introduce randomized low-rank Runge–Kutta integration and, in their generalized Nyström description, the QR-normalized unregularized core used as the starting point here (Section 2.3, Equations (8)–(9), Theorem 2). Nakatsukasa (2020), Tropp and coauthors (2017), and Epperly and Webber (2026) analyze unregularized generalized Nyström or sketched least-squares Frobenius-error bounds. Exact Student-type denominator phenomena and the one-sided range-projection baseline were also previously analyzed. None of these mechanisms is claimed to be new.

The assessed distinction is the **specified QR-normalized ridge variant**, its exact risk function, its **unique Gaussian-sketch-count-independent positive risk minimizer**, and the contrasting trace behavior on an identity matrix. Existing exact unregularized error identities alone do not provide a positive ridge optimizer without a new bias–variance calculation. Classical ridge regression intuition offers a plausible route to rediscovery; an equivalent earlier normalized-core result may exist. No priority or independence certification is asserted.

## Limitations
The theorem treats a fixed two-by-two *real* positive diagonal target, a single right Gaussian vector, an arbitrary positive integer number of independent left Gaussian vectors, a deterministic scalar ridge, and Frobenius and trace losses. It does not prove optimality over data-dependent penalties or more general regularizers. It does not analyze finite precision, general matrix sizes, nonsymmetric spectra, or an entire low-rank Runge–Kutta trajectory. Ridge changes the original unregularized generalized Nyström method, and any practical use requires assessing algorithmic approximation bias. Literature coverage is necessarily incomplete, particularly potential older ridge-regression reformulations.

## References
1. H. Y. Lam, G. Ceruti, and D. Kressner, *Randomized low-rank Runge-Kutta methods* (2024), arXiv:2409.06384v1, https://arxiv.org/html/2409.06384v1, especially Section 2.3.
2. Y. Nakatsukasa, *Fast and stable randomized low-rank matrix approximation* (2020), arXiv:2009.11392v1, https://arxiv.org/html/2009.11392v1.
3. J. A. Tropp, A. Yurtsever, M. Udell, and V. Cevher, *Practical sketching algorithms for low-rank matrix approximation* (2016 preprint / 2017 journal), arXiv:1609.00048v1, https://arxiv.org/abs/1609.00048.
4. E. N. Epperly and R. J. Webber, *Sharp analysis of sketched least squares and randomized low-rank approximation* (2026), arXiv:2605.19096v2, https://arxiv.org/html/2605.19096v2, especially Sections 2.1 and 4.1.
