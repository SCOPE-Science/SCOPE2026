# Exact fourth-moment stability window of a covariance-exact stochastic midpoint scheme

## Finding

Consider the scalar Itô diffusion, with independent standard Brownian motions \(W\) and \(B\),
\[
 \mathrm dX_t=-aX_t\,\mathrm dt+bX_t\,\mathrm dW_t+\sigma\,\mathrm dB_t,
 \qquad a,b,\sigma>0,\quad 0<r:=b^2/a<2.
\]
Apply the drift-midpoint, diffusion-explicit theta-Maruyama method at any constant step \(h>0\):
\[
 Y_{k+1}=Y_k-\frac{ah}{2}(Y_k+Y_{k+1})
       +bY_k\Delta W_k+\sigma\Delta B_k.
\]
Write \(t=ah/2>0\), \(s=\sigma^2/a>0\), and
\[
 D_r(t)=(2-3r)(1+t^2)+3r(2-r)t.
\]
Both the diffusion and the numerical chain have unique invariant probability laws. Their means are zero, and their stationary second moments agree **exactly for every step size**:
\[
 \mathbb E_{\rm true}X^2=\mathbb E_{\rm num}Y^2=\frac{s}{2-r}.
\]
The true invariant fourth moment is finite exactly when \(r<2/3\); if finite, it equals
\[
 \mathbb E_{\rm true}X^4=\frac{3s^2}{(2-r)(2-3r)}.
\]
In contrast, the numerical invariant fourth moment is finite **if and only if** \(D_r(t)>0\), and in that case equals
\[
 \boxed{\displaystyle \mathbb E_{\rm num}Y^4
 =\frac{3s^2(1+t^2+rt)}{(2-r)D_r(t)}.}
\]
The resulting complete phase classification for all \(h>0\) is:

- If \(0<r\le 2/3\), the numerical invariant fourth moment is finite for every \(h>0\).
- If \(2/3<r<2/\sqrt3\), it is finite **only** in the open nonmonotone stepsize interval \(t_-<t<t_+\), where
  \[
  t_\pm=\frac{3r(2-r)\pm\sqrt{9r^2(2-r)^2-4(3r-2)^2}}{2(3r-2)},
  \qquad t_-t_+=1.
  \]
- If \(2/\sqrt3\le r<2\), the numerical invariant fourth moment is infinite for every \(h>0\), including the unique equality point \(r=2/\sqrt3,t=1\).

For every \(0<r<2/3\), the numerically generated fourth moment strictly underestimates the true one:
\[
 \boxed{\displaystyle
 \frac{\mathbb E_{\rm num}Y^4}{\mathbb E_{\rm true}X^4}
 =1-\frac{4rt}{D_r(t)}\in(0,1).}
\]
At the physical boundary \(r=2/3\), the true fourth moment is infinite whereas **every positive numerical stepsize** has finite fourth moment. For \(2/3<r<2/\sqrt3\), the numerical method likewise artificially regularizes an infinite true fourth moment for an explicitly determined interval of intermediate stepsizes.

For instance, choosing \(a=b=\sigma=1\), \(h=2\) gives \(r=t=s=1\). The true invariant law has variance \(1\) and infinite fourth moment, whereas the numerical invariant law has variance \(1\) and fourth moment \(9\). Its finite-fourth stepsize window is \((3-\sqrt5)/2<t<(3+\sqrt5)/2\).

## Assumptions and scope

The noises \(W\) and \(B\) are independent, and increments are independent across numerical steps and of initial data. All parameters are real and strictly positive with \(b^2<2a\). The midpoint is applied **only to the drift**; both diffusion coefficients are evaluated at the old state. The theorem concerns invariant laws and raw fourth moments, not finite-time strong errors, pathwise stability, or fully implicit stochastic-noise midpoint rules. The endpoint \(h=0\) is a continuous-time limit, not a numerical step. At \(D_r(t)=0\), the fourth moment is infinite, not merely unproved finite.

## Proof

**1. Continuous-time invariant law.** The diffusion generator is
\[
 \mathcal Lf(x)=-axf'(x)+\tfrac12(b^2x^2+\sigma^2)f''(x).
\]
The normalized zero-flux stationary density is
\[
 \pi(x)=C_{a,b,\sigma}(\sigma^2+b^2x^2)^{-1-a/b^2}.
\]
It is integrable because \(a>0\) and, since the diffusion coefficient is uniformly positive, determines the unique invariant law. It is symmetric. Its tails have density exponent \(-2-2/r\), making the fourth moment finite precisely when \(4<1+2/r\), or \(r<2/3\). Applying the stationary generator to the second and, in its finite regime, fourth powers gives
\[
 0=(-2a+b^2)\mathbb EX^2+\sigma^2,
 \quad 0=(-4a+6b^2)\mathbb EX^4+6\sigma^2\mathbb EX^2,
\]
which yields the stated continuous moments. The density itself justifies divergence outside the fourth-moment regime.

**2. Discrete invariant law.** Write the update as \(Y_{k+1}=A_kY_k+C_k\), where \(Z_k,U_k\) are independent standard normals and
\[
 A_k=\frac{1-t+\sqrt{2rt}\,Z_k}{1+t},\qquad
 C_k=\frac{\sqrt{2st}\,U_k}{1+t}.
\]
The independent pairs \((A_k,C_k)\) are identically distributed over steps, with \(A_k\) independent of \(C_k\). Direct Gaussian moment calculations give
\[
 \alpha_2:=\mathbb EA^2=\frac{(1-t)^2+2rt}{(1+t)^2}<1,
 \quad v:=\mathbb EC^2=\frac{2st}{(1+t)^2},
\]
\[
 \alpha_4:=\mathbb EA^4
 =\frac{(1-t)^4+12rt(1-t)^2+12r^2t^2}{(1+t)^4},
 \qquad \mathbb EC^4=3v^2.
\]
The strict \(L^2\) contraction \(\alpha_2<1\) follows from
\(1-\alpha_2=2t(2-r)/(1+t)^2>0\). Iterating backwards yields an \(L^2\)-convergent random affine series for the unique stationary law. Synchronous coupling establishes uniqueness. Symmetric Gaussian innovations and uniqueness imply its symmetry.

**3. Exact second moment.** Independence gives
\[
 (1-\alpha_2)\mathbb EY^2=v,
 \qquad\mathbb EY^2=s/(2-r).
\]
This matches the diffusion for every \(h>0\).

**4. Sharp fourth-moment criterion.** When \(\alpha_4<1\), the backward affine series converges in \(L^4\) by Minkowski's inequality, so its fourth moment exists. Conversely, assuming a finite fourth moment in the unique symmetric stationary law and expanding the independent centered additive Gaussian noise yields
\[
 (1-\alpha_4)\mathbb EY^4=6\alpha_2v\mathbb EY^2+3v^2>0,
\]
forcing \(\alpha_4<1\). Consequently the condition is necessary and sufficient, even on the equality boundary. Polynomial factorization shows
\[
 1-\alpha_4=\frac{4tD_r(t)}{(1+t)^4}.
\]
Substituting the second moment into the fourth-moment identity and simplifying proves the displayed exact fourth-moment formula.

**5. Complete phase diagram.** If \(r<2/3\), both terms in \(D_r(t)\) are positive; if \(r=2/3\), then \(D_r(t)=8t/3>0\). If \(r>2/3\), divide by \(t>0\) to obtain
\[
 \frac{D_r(t)}t=(2-3r)(t+t^{-1})+3r(2-r).
\]
Since \(t+t^{-1}\ge2\), its unique maximum is at \(t=1\), where it equals \(4-3r^2\). It is positive somewhere exactly when \(r<2/\sqrt3\); the two simple positive roots in that regime are the stated \(t_\pm\). The quadratic has equal leading and constant coefficients, giving \(t_-t_+=1\). At \(r=2/\sqrt3\), equality in the maximum gives \(\alpha_4=1\), hence no finite fourth moment.

**6. Bias and benchmark.** For \(0<r<2/3\), substitution of both exact moments yields the ratio \(1-4rt/D_r(t)\); positivity is witnessed by \(D_r(t)-4rt=(2-3r)(1+t^2+rt)>0\). At \(r=t=s=1\), one has \(A=Z/\sqrt2\), \(C=U/\sqrt2\), \(\alpha_2=1/2\), \(\alpha_4=3/4\). Hence \(\mathbb EY^2=1\), \(\mathbb EY^4=9\), while the continuous density decays as \(|x|^{-4}\), making its fourth moment infinite.

## Verification

The accompanying `verify.py` implements the independent Gaussian-moment identities and exact rational reductions with standard-library fractions. Running `python3 verify.py` produces `verification_output.txt`; the recorded execution passed 3,028 exact-rational assertions spanning the second-moment identity, quartic factorization, fourth-moment recursion, bias, kurtosis, phase boundaries, and benchmark. Finite rational checks are consistency tests and are not a substitute for the all-parameter proof above.

## Relationship to prior work

Liu, Mao and Wu (arXiv:2206.09970, first posted 20 June 2022) establish existence and numerical approximation of invariant measures for the **backward Euler-Maruyama** method under broad dissipativity assumptions. Their main theorems do not provide an exact fourth-moment stepsize phase diagram for the distinct drift-midpoint scheme studied here. Qiu, Liu and Hu's 2014 paper on stochastic theta methods treats second-moment boundedness and small moments, rather than this exact stationary fourth-order threshold. Higham (2000) studies mean-square and asymptotic stability for the homogeneous multiplicative-noise test equation, which does not have the additive forcing and nondegenerate stationary law required for the present comparison. Li, Liu and Xiao (arXiv:2606.19886) prove invariant-measure results for \(\theta>1/2\) under small-step assumptions; the sharp midpoint endpoint \(\theta=1/2\), all-step fourth-moment window and exact bias are outside their stated main theorem. General random-affine recurrence moment criteria are used as standard tools, not claimed as new.

## Limitations

This is a scalar, affine diffusion with two **independent** Gaussian drivers; correlated drivers change the moment recursion. Finite fourth moment does not imply distributional closeness or practical sampling efficiency. The finite-step fourth moment can be badly biased even when the second moment is exact. The closed-form phase thresholds do not address higher moments, multidimensional noncommuting drift, varying step sizes, or other theta values. Similar exact classifications could exist in less-visible older specialist literature, and independent literature validation has not been performed.

## References

1. W. Liu, X. Mao and Y. Wu, *The backward Euler-Maruyama method for invariant measures of stochastic differential equations with super-linear coefficients*, arXiv:2206.09970 (v1, 20 June 2022), https://arxiv.org/abs/2206.09970.
2. Q. Qiu, W. Liu and L. Hu, *Asymptotic moment boundedness of the stochastic theta method and its application for stochastic differential equations*, Advances in Difference Equations **2014**, article 310, https://doi.org/10.1186/1687-1847-2014-310.
3. D. J. Higham, *Mean-square and asymptotic stability of the stochastic theta method*, SIAM Journal on Numerical Analysis **38** (2000), 753–769, https://doi.org/10.1137/S003614299834736X.
4. X. Li, W. Liu and W. Xiao, *Invariant measures of the stochastic theta method for stochastic differential equations with super-linearly growing coefficients*, arXiv:2606.19886 (2026), https://arxiv.org/abs/2606.19886.
