# A sixth-order gap in the equal-weight bound for circumscribed random polytopes

## Finding

For the planar oval with support function \(h_t(\theta)=1-(t/3)\cos(2\theta)\), \(0<|t|<1\), the true minimax of the separately normalized leading expected excess-area and mean-width errors of random circumscribed polygons exceeds the equal-weight lower bound of Hoehner [1]. If \(\mathcal Q(K_t)\) is the minimax and \(L(K_t)\) is that lower bound, then
\[
\mathcal Q(K_t)-L(K_t)=\frac{25}{55296}t^6+O(t^8)>0
\]
for sufficiently small nonzero \(t\). In the scalar dual, with \(\lambda\) weighting the area error, the optimal weight is \(\lambda_*(t)=1/2+(5/96)t^2+O(t^4)\). Thus even an arbitrarily small smooth perturbation of the disk can make the equal-weight bound strictly low, although the discrepancy does not appear through fourth order.

## Model and known minimax reduction

Let \(K\subset\mathbb R^d\), \(d\ge2\), be full-dimensional, compact and \(C_+^2\) (twice continuously differentiable boundary and strictly positive principal curvatures). Independently sample \(N\) boundary points from a fixed positive continuous probability density \(\rho\) relative to area \(dS\), and intersect the corresponding outer supporting halfspaces with a fixed enclosing cube containing \(K\) in its interior. We optimize only the leading \(N^{-2/(d-1)}\) expected error coefficients, not the finite-sample errors. Each coefficient is divided by its own separately attainable minimum. Böröczky–Reitzner [2, Theorems 1 and 3] give the curvature weights \(\kappa^{1/(d-1)}\) and \(\kappa^{d/(d-1)}\), respectively, in integrals against \(\rho^{-2/(d-1)}dS\), where \(\kappa\) is Gauss curvature. Put
\[
p=\frac{d+1}{d-1},\qquad f=\frac{\kappa^{1/(d+1)}}{\int_{\partial K}\kappa^{1/(d+1)}dS},\qquad
g=\frac{\kappa^{d/(d+1)}}{\int_{\partial K}\kappa^{d/(d+1)}dS}.
\]
Hölder's inequality gives \(f,g\) as the separate optimizers. The normalized risks are \(R_V(\rho)=\int_{\partial K}f^p\rho^{1-p}dS\) and \(R_W(\rho)=\int_{\partial K}g^p\rho^{1-p}dS\). Define
\[
w_\lambda=\lambda f^p+(1-\lambda)g^p,\qquad H_K(\lambda)=\int_{\partial K}w_\lambda^{1/p}dS.
\]
The formula \(\mathcal Q(K)=\min_\rho\max\{R_V,R_W\}=\max_{0\le\lambda\le1}H_K(\lambda)^p\) is a two-law instance of the Rényi capacity–radius theorem [3, Definition 2 and Theorem 1]. The individual risks are the exponentials of \((p-1)\) times the order-\(p\) Rényi divergences to \(\rho\,dS\). For clarity, a direct argument in the present setting also verifies that the center belongs to the admissible density class. Hölder applied to \(\int(w_\lambda\rho^{1-p})^{1/p}\rho^{(p-1)/p}dS\) shows that the smallest \(\lambda R_V+(1-\lambda)R_W\) is \(H_K(\lambda)^p\), uniquely attained at \(\rho_\lambda=w_\lambda^{1/p}/H_K(\lambda)\). This gives a lower bound on \(\mathcal Q(K)\) for every \(\lambda\). If \(f\ne g\), the function \(H_K\) is strictly concave (its second derivative has strictly negative integral), and its endpoints both equal one, so it has a unique interior maximizer. There \(R_V(\rho_\lambda)-R_W(\rho_\lambda)=pH_K(\lambda)^{p-1}H'_K(\lambda)=0\); hence the lower bound is attained and the minimax density is unique by the equality case of Hölder. If \(f=g\), the common separate optimizer gives \(\mathcal Q=1\). The equal-weight bound studied in [1] is \(L(K)=H_K(1/2)^p\).

## Proof of the sixth-order gap

For \(h_t\) above, the curvature radius is \(r_t=h_t+h_t''=1+t\cos(2\theta)>0\), so it defines a smooth strictly convex oval. The angle is the outer-normal angle, \(dS=r_t\,d\theta\), and \(\kappa=1/r_t\). Write \(\langle\cdot\rangle\) for the average over \([0,2\pi]\) and set \(U=\langle r_t^{2/3}\rangle^{-3}\), \(V=\langle r_t^{1/3}\rangle^{-3}\). Since \(p=3\), substitution of the normalized densities gives
\[
H_t(\lambda)=\big\langle r_t^{1/3}[\lambda U r_t+(1-\lambda)V]^{1/3}\big\rangle.
\]
For small \(t\) these functions and their \(\lambda\)-derivatives are analytic uniformly near \([0,1]\); shifting the angles by \(\pi/2\) shows they are even in \(t\). Put \(x=t\cos(2\theta)\), so \(\langle x^2\rangle=t^2/2\), \(\langle x^4\rangle=3t^4/8\), with all odd moments zero. The binomial expansion gives
\[
U=1+\frac{t^2}{6}+\frac{11t^4}{216}+O(t^6),\qquad
V=1+\frac{t^2}{6}+\frac{7t^4}{108}+O(t^6).
\]
At \(\lambda=1/2\), write \(S=(Ur_t+V)/2\), \(D=Ur_t-V\). The first derivative is \(\frac13\langle r_t^{1/3}S^{-2/3}D\rangle\). Factor \(S=((U+V)/2)(1+Ux/(U+V))\), where \(U/(U+V)=1/2+O(t^4)\). For the coefficient through fourth order in the product with \(D\), the needed angular factor is
\[
(1+x)^{1/3}(1+x/2)^{-2/3}=1-\frac{x^2}{12}+\frac{x^3}{12}+O(x^4).
\]
Thus the fourth-order coefficient of \(H_t'(1/2)\) is \(\frac13[-1/72+(3/8)/12]=5/864\). The second derivative is \(-\frac29\langle r_t^{1/3}S^{-5/3}D^2\rangle\), with \(D=x+O(t^3)\), so \(H_t''(1/2)=-t^2/9+O(t^4)\). In particular \(H_t'(1/2)=5t^4/864+O(t^6)\), by evenness.

The derivative \(H_t'(\lambda)/t^2\) extends analytically in \(t^2\) at zero, since \(H_0(\lambda)=1\) and \(H_t\) is even. Its zero at \((1/2,0)\) has \(\lambda\)-derivative \(-1/9\). The implicit-function theorem and strict concavity for \(t\ne0\) give the maximizing weight \(1/2+(5/96)t^2+O(t^4)\). Taylor expansion in \(\lambda\) gives
\[
H_t(\lambda_*)-H_t(1/2)=\frac{H_t'(1/2)^2}{-2H_t''(1/2)}+O(t^8)=\frac{25}{165888}t^6+O(t^8).
\]
Indeed \(H_t^{(3)}(\lambda)=O(t^3)\) uniformly and \(\lambda_*-1/2=O(t^2)\); the errors in slope, curvature and weight affect the gap only at order eight or higher. Both values of \(H_t\) are \(1+O(t^2)\). Taking the difference of their cubes proves the asserted coefficient. This expansion concerns this specified family, not a universal sixth-order law.

## Reproducibility and prior work

The rational Taylor coefficients are reproducible from the displayed angular moments, binomial factors and derivatives. The accompanying standard-library `verify_circumscribed_tradeoff.py` gives finite midpoint-quadrature checks and solves the weight condition by bisection. It also evaluates both risks independently; it does not prove the expansion or remainder.

Hoehner [1, Proposition 3.5 and Theorem 3.6] gives the average optimizer and the corresponding lower bound for the maximum; Remark 3.7 expressly does not claim that the bound is exact. The general minimax reduction is from [3], not an originality claim here. Related inscribed-polytope minimax results (Resultary records `179adc1046b6`, `20a687e8594a`, and `4e45a188ddc4`) use analogous methods or near-sphere expansions for different curvature risks. The contribution here is the specified oval's strictly positive sixth-order separation from the circumscribed equal-weight bound. The comparison is not a claim of exhaustive historical priority.

## References

1. S. Hoehner, *Simultaneous random polytope approximation characterizes the Euclidean ball*, [arXiv:2602.18547v2](https://arxiv.org/html/2602.18547v2), §3.
2. K. Böröczky, Jr. and M. Reitzner, *Approximation of smooth convex bodies by random circumscribed polytopes*, Annals of Applied Probability 14 (2004), 239–273, [DOI 10.1214/aoap/1075828053](https://doi.org/10.1214/aoap/1075828053).
3. B. Nakiboğlu, *The Rényi Capacity and Center*, [arXiv:1608.02424](https://arxiv.org/abs/1608.02424), Definition 2 and Theorem 1.
