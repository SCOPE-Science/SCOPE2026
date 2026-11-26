# Fixed-radius hyperbolic-ball diameter tails and curvature identification

## Finding

The contribution is the extension of the fixed-radius diameter-tail and curvature-recovery laws from disks to dimensions \(n\ge3\), together with an exact upper-half distance law in dimension three. The disk case, including its conditional limit, is already known [1] and is included below for a uniform formula.

Fix a dimension \(n\ge2\), a geodesic radius \(T>0\), and a curvature parameter \(\kappa>0\). Sample \(X,Y\) independently from normalized hyperbolic volume in a ball of radius \(T\) in sectional curvature \(-\kappa^2\). Let \(D=d(X,Y)\), \(p=(n-1)/2\), and set
\[
I=\int_0^T(\sinh(\kappa s)/\kappa)^{n-1}\,ds,\qquad
f=(\sinh(\kappa T)/\kappa)^{n-1}/I,\qquad c=\tanh(\kappa T)/(4\kappa).
\]
As \(\varepsilon\downarrow0\) with these parameters fixed,
\[
\Pr(D>2T-\varepsilon)=C_{n,\kappa,T}\varepsilon^{p+2}+O_{n,\kappa,T}(\varepsilon^{p+3}),\qquad
C_{n,\kappa,T}=\frac{\Gamma(n/2)}{2\sqrt\pi\,\Gamma(p+3)}f^2c^{-p}.
\]
At the Euclidean endpoint \(\kappa=0\), set \(f=n/T\), \(c=T/4\); then
\[
C_{n,0,T}=\frac{n^2 2^{n-2}\Gamma(n/2)}{\sqrt\pi\,\Gamma((n+5)/2)T^{(n+3)/2}}.
\]
For fixed \(n,T\), the coefficient is continuous and strictly increasing in \(\kappa\ge0\) onto \([C_{n,0,T},\infty)\). Thus one near-diameter tail coefficient determines \(\kappa\) when \(n,T\) are known.

Let \(A=T-d(0,X)\), \(B=T-d(0,Y)\), and \(\delta=\pi-\angle X0Y\), where \(0\) denotes the ball center. Conditional on \(D>2T-\varepsilon\),
\[
\left(A/\varepsilon,B/\varepsilon,c\delta^2/\varepsilon,1-(A+B+c\delta^2)/\varepsilon\right)
\Longrightarrow \operatorname{Dirichlet}(1,1,p,1).
\]
The last coordinate need not be nonnegative before taking the limit.

For \(n=3\), \(\kappa>0\), and \(T\le L\le2T\), set \(J=\int_0^T\sinh^2(\kappa s)\,ds\). The exact finite-deficit law is
\[
\Pr(D>L)=\frac1{4J^2}\int_L^{2T} [\cosh(\kappa u)-\cosh(\kappa L)]
\left[(2T-u)\cosh(\kappa u)-\frac{\sinh(\kappa(2T-u))}{\kappa}\right]du.
\]

## Proof

The radii \(s,t\) are independent with density \((\sinh(\kappa r)/\kappa)^{n-1}/I\). The independent angle \(\theta\) has density \(a_n\sin^{n-2}\theta\), where \(a_n=\Gamma(n/2)/(\sqrt\pi\Gamma(p))\), and \(U=(1+\cos\theta)/2=\sin^2(\delta/2)\) has the beta law with parameters \((p,p)\). The hyperbolic cosine law gives
\[
\cosh(\kappa D)=\cosh(\kappa(s+t))-2\sinh(\kappa s)\sinh(\kappa t)U.
\]
In particular the diameter is \(2T\), attained by antipodal boundary points. For \(L=2T-\varepsilon\), the event \(D>L\) is contained in \(A+B<\varepsilon\). On that triangle, it is exactly \(U<Q\), with
\[
Q=\frac{\cosh(\kappa(s+t))-\cosh(\kappa L)}{2\sinh(\kappa s)\sinh(\kappa t)}
=\frac{\varepsilon-A-B}{4c}(1+O(\varepsilon)).
\]
The relative estimate is uniform by factoring the numerator by \(s+t-L\) before estimating the resulting smooth quotient. For sufficiently small \(\varepsilon\), \(0\le Q<1\); the beta probability is \(Q^p/(p\mathrm B(p,p))(1+O(Q))\). Both radial densities are \(f(1+O(\varepsilon))\) uniformly. Integrating these relative estimates over the radial triangle gives a relative error \(O(\varepsilon)\) in the tail probability.

To evaluate the leading constant and conditional law, put \(x=A/\varepsilon,\ y=B/\varepsilon,\ z=\sqrt{c/\varepsilon}\,\delta\). The cutoff for \(z^2\) converges to \(1-x-y\) by the formula for \(Q\) and \(\sin^2(\delta/2)=\delta^2/4+O(\delta^4)\). The scaled density after division by \(\varepsilon^{p+2}\) tends to \(f^2a_nc^{-p}z^{n-2}\) on \(x+y+z^2<1\), with bounded support and an integrable majorant proportional to \(z^{n-2}\). The integral of \(z^{n-2}\) over this region is
\[
\tfrac12\int_0^1 z^{n-2}(1-z^2)^2\,dz=\tfrac14\mathrm B(p,3)=\frac{\Gamma(p)}{2\Gamma(p+3)}.
\]
This gives the stated constant. After normalization, changing variable from \(z\) to \(z^2\) gives the Dirichlet law with the fourth coordinate supplied by the simplex slack. At \(\kappa=0\), the Euclidean cosine law gives the same calculation with \(Q=((s+t)^2-L^2)/(4st)\), Euclidean radial density and \(c=T/4\).

For \(0<r<T\), \(\sinh(\kappa r)/\sinh(\kappa T)\) decreases strictly in \(\kappa\) since \(x\coth x\) increases for \(x>0\). Thus \(f^{-1}=\int_0^T[\sinh(\kappa r)/\sinh(\kappa T)]^{n-1}dr\) decreases strictly. Also \(c\) decreases strictly since \(\tanh x/x\) does so. The limits of \(f,c\) at zero follow from their definitions. As \(\kappa\) increases without bound, \(c\to0\) while \(f\ge n/T\), so \(C_{n,\kappa,T}\to\infty\) since \(p>0\). This proves the identifiability claim.

For \(n=3\), \(U\) is uniform. When \(s+t>L\ge T\ge |s-t|\), the exact conditional probability is \(Q\in[0,1]\), except for null degenerate radii where the quotient can be undefined. Otherwise the probability is zero when \(s+t\le L\). Multiplying \(Q\) by the radial densities gives \([\cosh(\kappa(s+t))-\cosh(\kappa L)]\sinh(\kappa s)\sinh(\kappa t)/(2J^2)\). Under \(u=s+t, v=s-t\), the Jacobian is \(1/2\), the bounds are \(L\le u\le2T\), \(|v|\le2T-u\), and \(2\sinh(\kappa s)\sinh(\kappa t)=\cosh(\kappa u)-\cosh(\kappa v)\). Integration in \(v\) yields the claimed integral, with zero tail at \(L=2T\).

## Verification and scope

The accompanying `checker.py` uses Python 3, NumPy and SciPy and checks the exact radial/angular integration numerically against the endpoint asymptotic and the dimension-three formula at finitely many parameter choices; it also tests finitely many monotonicity comparisons. These tests are supplementary. The proof concerns true normalized volume and intrinsic geodesic distance (equal to ambient distance by convexity), not coordinate-uniform model sampling or graph distance. The remainder is not asserted to be uniform in radius, curvature or dimension. No nonconstant-curvature inference, arbitrary-dimensional full distance law, or absolute priority claim is made.

## Relationship to prior work

[1] *Sharp near-diameter geodesic tails and curvature recovery for constant-curvature disks*, 2026-11-17, [Finding and Proof](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-sharp-near-diameter-geodesic-tails-and-curvature-recovery-for-co--5ffce32d084b/RESULT.md). That result gives the same \(n=2\) tail, remainder, curvature monotonicity and conditional limit: in that case \(f=\kappa\coth(\kappa T/2)\) and the angular parameter is \(p=1/2\). The disk result also describes angular marks not needed here.

[2] *Three-regime radial–angular distance-deficit laws in expanding hyperbolic balls*, 2026-11-08, [Finding and Assumptions](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-three-regime-radial-angular-distance-deficit-laws-in-expanding-h--a5d5220f2e29/RESULT.md). It takes radius to infinity before the limiting deficit tail, and does not supply a fixed-radius coefficient.

[3] M. Kiwi and D. Mitsche, *A Bound for the Diameter of Random Hyperbolic Graphs*, [arXiv:1408.2947](https://arxiv.org/abs/1408.2947), gives sampling and cosine-law inputs for a random-graph problem. G. Alanis-Lobato and A. Andrade-Navarro, *Distance Distribution between Complex Network Nodes in Hyperbolic Space*, Complex Systems 25 (2016), 223–236, [original paper](https://content.wolfram.com/sites/13/2018/02/25-3-3.pdf), uses a large-radius approximation to the distance. Neither is asserted as a source of the present fixed-radius conclusions for \(n\ge3\).
