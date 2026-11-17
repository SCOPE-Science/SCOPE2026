# Sharp spectral KL loss of trace-matched isotropic Gaussian covariance

## Finding

**Theorem.** Let \(d\ge2\) be an integer, \(K>1\), and let \(C\) range over all real symmetric positive-definite \(d\)-by-\(d\) matrices with spectral condition number \(\kappa_2(C)\le K\). Define \(m_C=\operatorname{tr}(C)/d\) and
\[
\mathcal D(C)=\operatorname{KL}\bigl(\mathcal N(0,m_C I_d)\,\|\,\mathcal N(0,C)\bigr).
\]
For \(p\in[0,1]\), write
\[
F_K(p)=\frac{(K-1)^2}{K}p(1-p)-\log\bigl(1+(K-1)p\bigr)+p\log K.
\]
Then the **exact, attained, dimension-dependent optimum** is
\[
\boxed{\sup_{\kappa_2(C)\le K}\mathcal D(C)=\frac d2\max_{1\le j\le d-1}F_K(j/d).}
\]
Every maximizing covariance, and no other one, is a positive scalar multiple of an orthogonal conjugate of \(\operatorname{diag}(K I_j,I_{d-j})\), for an integer \(j\) maximizing the expression. The discrete maximizers are among the floor and ceiling of \(d p_K\), where \(p_K\in(0,1)\) is the unique maximum point of \(F_K\).

For fixed \(d\), the sharp small- and large-condition-number regimes are
\[
\sup\mathcal D(C)=\frac{\lfloor d^2/4\rfloor}{4d}(K-1)^2+O_d((K-1)^3)\quad(K\downarrow1),
\]
\[
\sup\mathcal D(C)=\frac{\lfloor d^2/4\rfloor}{2d}K+O_d(\log K)\quad(K\to\infty).
\]
For \(d=4\), \(K=10\), the exact optimum is approximately \(2.943088908517195\), realized with two eigenvalues at either endpoint.

## Assumptions and scope

All Gaussian laws are real, centered, nondegenerate, and of dimension \(d\); logarithms are natural. The isotropic variance \(m_C\) is *trace matched* to the exact covariance \(C\). The directed relative entropy is \(\operatorname{KL}(\text{isotropic}\|\text{exact})\); reversing the arguments changes the optimization. The condition-number constraint is on the covariance \(C\) (equivalently on its inverse). The same theorem applies to an isolated inverse-covariance complement block \(C=B^{-1}\) in numerical linear algebra. It does not assert an exact relative entropy for a larger block-coupled covariance unless that full covariance satisfies these hypotheses.

If \(K=1\), then \(C\) is a scalar multiple of the identity, so the optimum is zero; the two-level characterization above concerns \(K>1\).

## Proof

**1. Spectral reduction.** Gaussian relative entropy and orthogonal invariance give, for the eigenvalues \(x_1,\dots,x_d>0\) of \(C\) and \(M=d^{-1}\sum_i x_i\),
\[
2\mathcal D(C)=Q(x_1,\ldots,x_d)
=M\sum_{i=1}^d\frac1{x_i}-d-d\log M+\sum_{i=1}^d\log x_i.
\]
Scaling all eigenvalues together leaves \(Q\) unchanged. Normalize their smallest eigenvalue to one, so each \(x_i\in[1,K]\). It suffices to maximize \(Q\) on the full compact cube \([1,K]^d\); its corners belong to the admissible condition-number family.

**2. All maximizers are vertices.** Fix an index \(i\) and hold the other coordinates fixed. Write \(x=x_i\), \(S=\sum_{j\ne i}x_j\), \(H=\sum_{j\ne i}x_j^{-1}\), and \(z=S/x\). Direct differentiation yields
\[
\frac{\partial Q}{\partial x}=\frac Hd-\frac S{d x^2}-\frac d{x+S}+\frac1x,
\qquad
\frac{\partial^2 Q}{\partial x^2}=\frac1{x^2}\left(\frac{2z}{d}+\frac d{(1+z)^2}-1\right).
\]
At an interior stationary point, the first equation is equivalent to
\[
HS-(d-1)^2=\frac{(z-d+1)(z^2+d-1)}{1+z}.
\]
Cauchy--Schwarz gives \(HS\ge(d-1)^2\). Since \(z^2+d-1>0\) and \(1+z>0\), stationarity forces \(z\ge d-1\). Consequently \(2z/d-1\ge 1-2/d\ge0\), and the remaining term \(d/(1+z)^2\) is strictly positive. So every interior coordinatewise stationary point has **positive** second derivative and cannot be a maximizer of the full cube. Each coordinate of every global maximizer lies in \(\{1,K\}\).

**3. Endpoint evaluation.** Let exactly \(j\) eigenvalues equal \(K\), the remainder one, and put \(p=j/d\). Then \(M=1+(K-1)p\), \(d^{-1}\sum_i x_i^{-1}=1-p+p/K\), and substitution gives \(Q=dF_K(p)\). Vertices with \(j=0\) or \(j=d\) have zero relative entropy, while every mixed vertex has strictly positive relative entropy because its two Gaussian covariances differ. This proves the exact finite maximum and the equality cases.

**4. Location of the discrete optimum.** Let \(a=(K-1)^2/K\). Then
\[
F'_K(p)=a(1-2p)-\frac{K-1}{1+(K-1)p}+\log K,
\qquad
F''_K(p)=-2a+\frac{(K-1)^2}{(1+(K-1)p)^2}.
\]
The second derivative is strictly decreasing in \(p\), so \(F'_K\) is strictly concave. Its endpoint values are \(F'_K(0)=\log K-1+1/K>0\) and \(F'_K(1)=\log K-(K-1)<0\). Thus it has exactly one zero, and \(F_K\) increases before this zero and decreases after it. Sampling at the discrete mesh \(j/d\) leaves only the neighboring floor and ceiling as candidate maximizers (with endpoints excluded where appropriate).

**5. Limiting regimes.** Uniform Taylor expansion over the finite mesh gives \(F_K(p)=\tfrac12(K-1)^2p(1-p)+O((K-1)^3)\) as \(K\downarrow1\). For fixed \(0<p<1\), \(F_K(p)=Kp(1-p)+O(\log K)\) as \(K\to\infty\). In both cases the maximum of \(j(d-j)\) for integer \(j\in\{1,\ldots,d-1\}\) is \(\lfloor d^2/4\rfloor\). The displayed expansions follow.

## Verification

The included standalone `verify.py` uses the Python standard library only. Run `python verify.py` from the extracted package. It checks the exact corner formula, thousands of random interior spectra against the bound, the analytical gradient by central differences, one concrete numerical example, and the small-/large-condition-number coefficients. The analytic proof, not the finite computation, covers every admissible dimension, covariance and condition number.

## Relationship to prior work

Fifen, Karambal and Hennig (2026), in their discussion of the trace-matched isotropic bulk approximation for stochastic Lanczos uncertainty quantification, give a general condition-ratio relative-entropy estimate. Their Theorem 13 does not give the exact dimension-dependent extremum, vertex characterization, or its large-condition-number linear asymptotic. The present result is a sharp replacement for the **isolated covariance-block** spectral comparison, not a new Lanczos algorithm.

The classical Kantorovich inequality bounds the arithmetic-mean times reciprocal-mean factor, and Liao and Wu (2015) analyze reverse arithmetic--harmonic mean operator inequalities. Those results alone do not optimize the combined reciprocal trace and log-determinant expression above, or determine its finite-dimensional equality cases. The analysis uses elementary spectral calculus and Cauchy--Schwarz; no new Gaussian KL identity is asserted.

## Limitations

This result assumes a positive-definite, centered Gaussian covariance and exact trace matching. The bound is worst-case rather than a typical-case estimate and does not quantify stochastic Lanczos trace-estimation error, covariance block coupling, algorithmic computational cost, or finite-precision effects. An independent literature search may identify an equivalent inequality framed in terms of the joint arithmetic--harmonic--geometric means; priority should not be inferred solely from the absence of a matching title or formula in indexed searches.

## References

1. H. Fifen, I. Karambal and P. Hennig, *Stochastic Lanczos Quadrature for Computational Uncertainty in Linear Algebra*, arXiv:2609.10080v1 (first public preprint, 2026-09-09), especially Section 4.3 and Theorem 13. https://arxiv.org/abs/2609.10080
2. W. Liao and J. Wu, *Reverse arithmetic-harmonic mean and mixed mean operator inequalities*, Journal of Inequalities and Applications **2015**, 215 (2015), DOI:10.1186/s13660-015-0735-z. https://link.springer.com/article/10.1186/s13660-015-0735-z
3. The classical Kantorovich arithmetic--harmonic mean inequality, as recalled in Liao--Wu, Lemma 2.1.
