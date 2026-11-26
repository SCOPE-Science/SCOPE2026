# Exact finite-transient two-cycle and resonant rank loss for two-row PolarGrad

## Finding

Let \(0<\alpha<2\), \(\alpha\ne1\), and put \(d=1-\alpha\) and \(c=|d|\). In the nuclear-norm-scaled polar iteration defined below, let \(s_1\ge s_2>0\) be the singular values of a full-row-rank initial error \(E_0\), and write \(r_0=(s_1-s_2)/(s_1+s_2)\).

* If \(r_0=0\), then \(E_t=d^t E_0\).
* If \(r_0=c^k\) for an integer \(k\ge1\), the first rank drop is at update \(k\), and \(E_{k+j}=(1-\alpha/2)^jE_k\) for \(j\ge0\).
* Otherwise put \(x=\log(r_0)/\log(c)\) and \(m=\lfloor x\rfloor\). The contrast first enters \((c,1)\) at update \(m\). For every \(t\ge m\), the error remains of rank two and
  \[
  r_{t+1}=c/r_t,\qquad r_{t+2}=r_t,\qquad E_{t+2}=d E_t.
  \]
  The eventual contrast has least period two unless \(x-m=1/2\), when it is fixed at \(\sqrt c\). The matrix two-step law holds in both cases.

The per-update asymptotic norm factor, defined as \(\lim_{t\to\infty}\|E_t\|_{\mathrm F}^{1/t}\), is \(\sqrt c\) in the third case and \(1-\alpha/2\) after rank loss. These factors coincide at the single allowed step \(\alpha=4-2\sqrt2\); rank loss and the distinct rank-one update law still occur at that step. The equal-singular start in the first case has factor \(c\).

## Assumptions and scope

Let \(n\ge2\), \(X_\star\in\mathbb R^{2\times n}\), and \(f(X)=\tfrac12\|X-X_\star\|_{\mathrm F}^2\). Write \(E_t=X_t-X_\star\). For a thin singular value decomposition \(E=U\operatorname{diag}(s_1,\ldots,s_r)V^\top\) with positive singular values, define
\[
\Phi(E)=\|E\|_*\operatorname{polar}(E)=\left(\sum_{i=1}^r s_i\right) UV^\top,
\qquad \Phi(0)=0.
\]
The exact iteration is \(E_{t+1}=E_t-(\alpha/2)\Phi(E_t)\). The factor \(1/2\) is the inverse left-Hessian trace (the Hessian acts on the error by left multiplication by \(I_2\)). The result is in exact arithmetic, for arbitrary singular vectors and real matrices of the stated shape. Rank-one initial errors follow the same rank-one law with \(k=0\); zero remains zero.

## Proof

**One update.** At full row rank put \(a=(s_1+s_2)/2>0\) and \(r=(s_1-s_2)/(s_1+s_2)\). In the current singular-vector frames the update has signed entries \(a(d+r)\), \(a(d-r)\). Their magnitudes are the new singular values, up to ordering. For \(r=0\), \(\Phi(E)=2E\), which gives \(E_t=d^tE_0\). For \(0<r<c\), the magnitudes have mean \(ac\) and half-difference \(ar\), hence the new contrast is \(r/c\). For \(c<r<1\), the larger and smaller magnitudes have mean \(ar\) and half-difference \(ac\), hence the contrast is \(c/r\). At \(r=c\) exactly one signed entry vanishes. On any rank-one error, \(\Phi(E)=E\); the next iterate is \((1-\alpha/2)E\), still of rank one since the multiplier is positive.

**Solving the contrast iteration.** Write \(r_0=c^x\) for \(0<r_0<1\). Whenever the exponent is greater than one it decreases by one on the next update. If \(x=k\) is an integer, after \(k-1\) steps the contrast is \(c\) and the next update has rank one. If \(x\) is not an integer, the first contrast in \((c,1)\) is \(r_m=c^{x-m}\). The map \(r\mapsto c/r\) preserves that interval and squares to the identity; its only fixed point there is \(\sqrt c\), attained exactly at \(x-m=1/2\). This gives the stated times and minimal contrast periods.

**Signed two-step law and rates.** When \(r>c\), the first signed coefficients in the current frames have signs \((+,-)\), irrespective of the sign of \(d\). Their mean magnitude is \(ar\). Thus the next signed entries in those same frames are
\[
 a(d+r)-\alpha ar=ad(1+r),\qquad
 a(d-r)+\alpha ar=ad(1-r).
\]
They give \(E_{t+2}=d E_t\) in the original matrix coordinates, including in the fixed-contrast case. Both parity subsequences have norm multiplier \(c\) per two steps, giving the root factor \(\sqrt c\). On the rank-one branch the factor is the positive multiplier itself. If \(\alpha<1\) then \((1-\alpha/2)^2=1-\alpha+\alpha^2/4>c\). If \(1<\alpha<2\), equality of the two factors is equivalent to \(\alpha^2-8\alpha+8=0\); only \(4-2\sqrt2\) lies in the interval.

## Verification

The unchanged `checker.py` gives rational diagonal checks for the two-step and rank-loss formulas and seeded numerical checks across different singular-vector frames. Its finite tests are supplementary, not the proof. As a fixed-contrast example, at \(\alpha=3/4\) and \(E_0=\operatorname{diag}(3,1)\), the first two iterates are \(\operatorname{diag}(3/2,-1/2)\) and \(\operatorname{diag}(3/4,1/4)\): the contrast is constantly \(1/2=\sqrt c\), while \(E_2=(1/4)E_0\). The rate-coincidence assertion is an exact algebraic equality, not a numerical tolerance.

## Relationship to prior work

Shulgin, Laing, Orvieto and Richtárik give a general full-row-rank covariance-root recursion (Appendix I, Proposition 17) and explicitly state the commuting fixed-step singular-value law \(s_i^+=|s_i-\alpha\bar s_H|\) after Corollary 4. For \(H=I_2\) it gives this problem's magnitude update. They also analyze two-cluster dynamics and two-row collapse at exact line search, corresponding here to \(\alpha=1\), which is excluded. The distinction here is solving the off-line-search map over arbitrarily many updates, including the complete set of hitting times for rank loss and the signed matrix return law; neither the one-step recurrence nor the optimizer is claimed as new. Related work by Jawanpuria, Garai and Mishra establishes uniform convergence bounds under nuclear scaling, not these orbit or rank-loss classifications. Lau, Long and Su introduce the nuclear-scaled polar update. These comparisons do not establish historical priority.

## Limitations

The proof concerns deterministic exact thin-polar dynamics on an isotropic two-row quadratic. It does not extend the classification to anisotropic curvature, other row counts, approximate polar maps, momentum, stochastic updates, or finite-precision rank decisions. In particular the rank-loss conditions are exact equalities.

## References

1. E. Shulgin, S. Laing, A. Orvieto, and P. Richtárik, *A Quadratic Lens on Muon's Polar Update: Benefits, Pitfalls, and the Role of Newton–Schulz*, https://arxiv.org/html/2610.30280v1.
2. P. Jawanpuria, B. Garai, and B. Mishra, *Constant Step Sizes for Muon-Type Spectral Optimizers on Strongly Convex Quadratics*, https://arxiv.org/html/2610.27747v1.
3. T. T.-K. Lau, Q. Long, and W. Su, *PolarGrad: A Class of Matrix-Gradient Optimizers from a Unifying Preconditioning Perspective*, https://arxiv.org/abs/2505.21799.
