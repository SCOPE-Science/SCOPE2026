# Infinite first moments for Gaussian-sketched FOM despite finite GMRES variance

## Finding

For one step in a Krylov linear-system solver, **Gaussian sketching creates a permanent heavy-tail distinction between sketched FOM (orthogonal-residual projection) and sketched GMRES (minimum sketched residual)**. Both methods are algebraically well defined almost surely, and both act on the same one-dimensional trial space, but their unconditional error moments have different thresholds.

Precisely, fix any integer \(d\ge2\), a real symmetric positive-definite \(A\in\mathbb R^{d\times d}\), and a unit vector \(b\in\mathbb R^d\) that is not an eigenvector. Define
\[
\alpha=b^\top Ab>0,\qquad
\beta=\|Ab-\alpha b\|_2>0,\qquad
\gamma^2=\|Ab\|_2^2=\alpha^2+\beta^2,
\qquad\eta=\frac{\beta^2}{\gamma^2}\in(0,1).
\]
Let \(S\in\mathbb R^{s\times d}\), for arbitrary integer \(s\ge2\), have mutually independent standard normal entries. Define the one-step approximations \(\widehat x_F=c_F b\), \(\widehat x_G=c_Gb\) by
\[
c_F=\frac{\|Sb\|_2^2}{(Sb)^\top(SAb)},\qquad
c_G=\frac{(SAb)^\top(Sb)}{\|SAb\|_2^2}.
\]
Both denominators vanish with probability zero. If \(T_s\) is the usual Student distribution with \(s\) degrees of freedom, then
\[
\frac1{c_F}\overset d=\alpha+\frac\beta{\sqrt{s}}T_s,
\qquad
c_G\overset d=\frac\alpha{\gamma^2}+\frac\beta{\gamma^2\sqrt{s}}T_s.
\tag{1}
\]
The appearances of the same Student law are mathematically different: it describes the **reciprocal** FOM coefficient but the **coefficient itself** for GMRES.

For every real \(p>0\), with \(x_*=A^{-1}b\),
\[
\mathbb E\|\widehat x_F-x_*\|_2^p<\infty\iff p<1,
\qquad
\mathbb E\|\widehat x_G-x_*\|_2^p<\infty\iff p<s.
\tag{2}
\]
The same thresholds hold with errors replaced by the approximation norms or the true residual norms. In particular, FOM's expected absolute solution error is infinite for every finite sketch size, even if the sketch has far more rows than the two-dimensional relevant Krylov space; GMRES has finite variance for \(s\ge3\).

The scalar sketched FOM Ritz value \(H=1/c_F\) has the exact density
\[
f_H(h)=\frac{\Gamma((s+1)/2)}{\sqrt\pi\,\beta\,\Gamma(s/2)}
\left(1+\frac{(h-\alpha)^2}{\beta^2}\right)^{-(s+1)/2}.
\tag{3}
\]
Write \(I_z(a,b)\) for the regularized incomplete beta function. Then the exact probability that this Ritz value is negative and the sharp reciprocal tail constant are
\[
\Pr\{H<0\}=\frac12I_\eta\!\left(\frac s2,\frac12\right)>0,
\qquad
\lim_{t\to\infty}t\Pr\{|c_F|>t\}=2f_H(0)
=\frac{2\Gamma((s+1)/2)}{\sqrt\pi\,\beta\,\Gamma(s/2)}\eta^{(s+1)/2}>0.
\tag{4}
\]
Even rejecting all sketches with \(H<0\) leaves the FOM absolute first moment infinite: the conditional density is positive arbitrarily close to the singular point \(H=0\) from the positive side.

For \(s>2\), the GMRES coefficient and true-residual second moments are
\[
\mathbb E c_G=\frac\alpha{\gamma^2},\qquad
\operatorname{Var}(c_G)=\frac{\beta^2}{\gamma^4(s-2)},\qquad
\mathbb E\|b-A\widehat x_G\|_2^2
=\frac{\beta^2}{\gamma^2}\frac{s-1}{s-2}.
\tag{5}
\]

**An exact example.** For \(A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}\), \(b=(1,0)^\top\), and \(s=3\), one has \(\alpha=2\), \(\beta=1\), \(\gamma^2=5\). Formula (4) gives
\[
\Pr\{H<0\}=\frac{\arcsin(1/\sqrt5)-2/5}{\pi}\approx0.02025966,\qquad
\lim_{t\to\infty}t\Pr\{|c_F|>t\}=\frac4{25\pi}.
\]
The FOM expected absolute true-solution error is infinite, whereas GMRES has expected squared true residual \(2/5\) (the deterministic one-dimensional GMRES optimum is \(1/5\)). This example embeds unchanged into arbitrary ambient dimensions by using a block-diagonal SPD matrix and appending zero coordinates to \(b\).

## Assumptions and scope

The matrix and right-hand side are deterministic. The sketch is drawn only once, with independent real \(N(0,1)\) entries. The trial space is \(\mathcal K_1(A,b)=\operatorname{span}\{b\}\), the initial guess is zero, and the matrix is SPD. The two sketched Galerkin conditions are exact mathematical operations without numerical rounding or truncation. There is no conditioning on a successful subspace embedding. A global positive scalar normalization of \(S\) cancels from both formulas. For a vector that is an exact eigenvector, \(\beta=0\), both methods are exact and the theorem's heavy-tail conclusions do not apply.

The moment threshold in (2) is for **every fixed finite** sketch height \(s\ge2\). It does not preclude increasingly accurate convergence in probability as \(s\) increases. Finite high-probability embedding bounds can coexist with divergent unconditional moments. The theorem does not address multi-step Krylov spaces, non-Gaussian sketches, pseudoinverse stabilization, explicit regularization, or floating-point safeguards.

## Proof

**1. Orthogonal Gaussian decomposition.** Let \(v=(Ab-\alpha b)/\beta\). The vectors \(b,v\) are orthonormal. By rotation invariance of each independent Gaussian sketch row, the vectors \(X=Sb\) and \(Y=Sv\) are independent standard Gaussian vectors in \(\mathbb R^s\). The sketch of the matrix action is \(SAb=\alpha X+\beta Y\).

Let \(R=\|X\|_2\). It has the chi distribution with \(s\) degrees of freedom. Conditional on \(X\), the random variable \(Z=X^\top Y/\|X\|_2\) is standard normal with a distribution independent of \(X\); thus \(Z\) and \(R\) are independent. Therefore
\[
H=\frac{X^\top(\alpha X+\beta Y)}{\|X\|_2^2}
=\alpha+\beta\frac ZR.
\]
Since \(\sqrt s\,Z/R\) is Student \(t_s\), this proves the FOM part of (1). Changing variables in the Student density gives (3); inserting \(h=0\) gives the strictly positive density value in (4). As \(SAb\) is nonzero almost surely, the GMRES denominator is positive almost surely. The FOM denominator vanishes only when the continuously distributed \(H\) is zero, a probability-zero event.

**2. Exact wrong-sign probability and sharp tail.** The event \(H<0\) is \(\{Z<-(\alpha/\beta)R\}\). The angular ratio \(Z^2/(Z^2+R^2)\) has the \(\operatorname{Beta}(1/2,s/2)\) law, and the sign of \(Z\) is an independent fair sign. Hence its probability is one half the upper tail at \(\alpha^2/\gamma^2\), namely \(I_\eta(s/2,1/2)/2\). For the coefficient \(c_F=1/H\), continuity and positivity of (3) at zero imply
\[
\Pr\{|c_F|>t\}=\int_{-1/t}^{1/t}f_H(h)\,dh
=\frac{2f_H(0)}{t}+o(t^{-1}).
\]
The same argument restricted to \(0<H<1/t\) shows that discarding negative \(H\) cannot make the conditional first moment finite.

**3. All FOM moments.** In a sufficiently small neighborhood of zero, the density \(f_H\) is bounded above and below by strictly positive constants. Thus \(\mathbb E|c_F|^p=\int_{\mathbb R}|h|^{-p}f_H(h)\,dh\) is finite at the origin if and only if \(p<1\). Outside that neighborhood the integrand is bounded, so no other divergence occurs. Because \(\|b\|_2=1\), the vector \(c_F b\) has norm \(|c_F|\); adding or subtracting the fixed finite vector \(x_*\) cannot alter any moment-finiteness threshold. Since \(Ab\ne0\), the same is true for \(b-c_FAb\). This proves the first equivalence in (2).

**4. Independent Gaussian regression for GMRES.** Set \(W=SAb\). The joint Gaussian pair \((X,W)\) has covariance \(\operatorname{Cov}(X,W)=\alpha I_s\) and \(\operatorname{Var}(W)=\gamma^2I_s\). Gaussian regression yields the decomposition
\[
X=\frac\alpha{\gamma^2}W+\frac\beta\gamma V,
\]
where \(V\sim N(0,I_s)\) is independent of \(W\sim N(0,\gamma^2I_s)\). Writing \(W=\gamma U\) gives
\[
c_G=\frac{W^\top X}{\|W\|_2^2}
=\frac\alpha{\gamma^2}+\frac\beta{\gamma^2}\frac{U^\top V}{\|U\|_2^2}
\overset d=\frac\alpha{\gamma^2}+\frac\beta{\gamma^2}\frac{Z'}{R'},
\]
where \(R'\sim\chi_s\) and \(Z'\sim N(0,1)\) are independent. This proves the GMRES part of (1). A standard Student density has tails on the order of \(|t|^{-(s+1)}\), so its absolute moment of order \(p\) is finite exactly when \(p<s\). Fixed affine translations and nonzero linear maps preserve this threshold, which establishes the second equivalence in (2) and the residual version.

**5. The GMRES mean-square law.** For \(s>2\), \(\mathbb E[1/(R')^2]=1/(s-2)\), since \((R')^2\) is chi-squared with \(s\) degrees of freedom. Therefore \(\mathbb E c_G=\alpha/\gamma^2\) and \(\operatorname{Var}(c_G)=\beta^2/[\gamma^4(s-2)]\). The deterministic identity
\[
\|b-cAb\|_2^2=1-2\alpha c+\gamma^2c^2
=\frac{\beta^2}{\gamma^2}+\gamma^2\left(c-\frac\alpha{\gamma^2}\right)^2
\]
then gives the final expression (5).

**6. Exact example.** The stated \(2\times2\) matrix has eigenvalues \(1,3\). Substituting its parameters into (3)–(5), together with the elementary identity for \(I_{1/5}(3/2,1/2)\), gives the values quoted in the finding. No general-\(s\) conclusion relies on the example.

## Verification

The accompanying `verify.py` uses double-precision Gaussian simulations and numerical integration only to check the analytic formulas, constants and examples; it does not attempt to infer infinite moments from truncated samples. It checks the exact symmetric \(2\times2\) example, independently integrates the density for multiple sketch heights, tests the reciprocal tail constant at increasing thresholds, and compares sketched FOM/GMRES coefficient identities to direct Gaussian sketches. It also checks the explicit mean-square GMRES formula. Run `python verify.py` with the listed dependencies; the corresponding execution output is `verify_output.txt`.

## Relationship to prior work

Güttel and Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions* (first public arXiv version 2022-08-24), introduce sketched FOM and GMRES and derive the sketched Galerkin/projected formulas. Their section 2.3 explicitly observes that sketched Ritz values need not remain in the positive half-plane even when the original matrix is positive-real, and their experiments show irregular FOM errors. These qualitative observations and the projection definitions are prior knowledge. The present result instead gives the exact finite-sketch distribution, nonzero negative-Ritz probability, sharp \(t^{-1}\) rare-event coefficient and the complete unconditional moment dichotomy on SPD systems.

Timsit, Grigori and Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers* (first public 2023-02-15), derive high-probability quasi-optimality bounds and report large occasional projected-method error spikes, including small Ritz-value outliers. Those observations do not determine the distribution or all-moment finiteness of the one-step Gaussian specialization. Burke, Güttel and Soodhalter, *GMRES with randomized sketching and deflated restarting* (2023), analyze sketched GMRES and its minimum-residual/orthogonal-residual relationship with sketched FOM, but do not give the present exact Gaussian-coefficient law or the unconditional mean-square contrast. The Student distribution of scalar Gaussian regression ratios is classical; it is not claimed as a novel probability distribution. The contribution is its exact and distinct placement within these two solver coefficients and the quantified solver-risk consequences.

## Limitations

This is a complete theorem for the specified one-dimensional Gaussian-sketch model, not a claim about all algorithms labeled FOM or GMRES, all sketch distributions, all Krylov dimensions, or any finite-precision implementation. High-probability embeddings and condition-number-based guarantees may offer useful safeguards while remaining compatible with this unconditional result. An implementer may explicitly reject near-singular projected systems or add regularization, thereby changing the distribution and its moments; merely rejecting negative Ritz values does not cure the absolute moment divergence. Precedence risk remains for an equivalent elementary Gaussian-ratio calculation in older specialist randomized projection or inverse-moment literature; general probabilistic facts are acknowledged.

## References

1. S. Güttel and M. Schweitzer, *Randomized sketching for Krylov approximations of large-scale matrix functions*, arXiv:2208.11447 (first publicly posted 2022-08-24), subsequently SIAM J. Matrix Anal. Appl. 44 (2023). https://arxiv.org/abs/2208.11447
2. E. Timsit, L. Grigori and O. Balabanov, *Randomized Orthogonal Projection Methods for Krylov Subspace Solvers*, arXiv:2302.07466 (2023). https://arxiv.org/abs/2302.07466
3. L. Burke, S. Güttel and K. M. Soodhalter, *GMRES with randomized sketching and deflated restarting*, arXiv:2311.14206 (2023). https://arxiv.org/abs/2311.14206
4. O. Balabanov and A. Nouy, *Randomized linear algebra for model reduction. Part I: Galerkin methods and error estimation*, arXiv:1803.02602 (2018). https://arxiv.org/abs/1803.02602
