# Exact coexistence wedge in a normalized rational fear competition system

## Finding

Consider the two-competitor system
\[
\dot u=u(1-u-v),\qquad
\dot v=v\left(\frac{2}{1+ku}-bv-u\right),\qquad
3/2<b<2,\quad k>0.
\]
Write \(\tau=b-1\), \(\rho=\sqrt{2(1-\tau)}\), and define
\[
k_f(b)=\frac{2\tau}{(2-\rho)^2}\in(1/2,1).
\]
The strictly positive equilibria are exactly as follows:

| Fear parameter | Positive equilibria |
|---|---|
| \(0<k<k_f(b)\) | None |
| \(k=k_f(b)\) | One ordinary saddle-node |
| \(k_f(b)<k<1\) | Two: a sink at smaller \(v\) and a saddle at larger \(v\) |
| \(k\geq 1\) | One saddle |

The boundary equilibrium \((0,2/b)\) is a hyperbolic sink throughout. The boundary equilibrium \((1,0)\) is a saddle for \(k<1\), locally attracting relative to the nonnegative quadrant at \(k=1\), and a hyperbolic sink for \(k>1\).

Thus the interval containing a positive sink is exactly \((k_f(b),1)\). Its width and endpoint expansion are
\[
1-k_f(b)=\frac{2(1-\rho)^2}{(2-\rho)^2}
=2\eta^2-2\eta^3+O(\eta^4),\qquad \eta=b-3/2\downarrow0.
\]
In particular the exact fold meets the boundary-invasion line quadratically.

## Assumptions and scope

The domain is the invariant nonnegative quadrant with strictly positive parameters in the displayed slice. Coexistence means both populations are strictly positive. The census concerns equilibria only; the stability statements are local. No complete basin boundary or long-time behavior away from the boundary neighborhood is asserted. The lower endpoint of the slice is where the critical-boundary quadratic center term vanishes, and the upper endpoint is where the other competitor's boundary invasion eigenvalue vanishes.

## Proof

An interior equilibrium has \(u=1-v\), with \(0<v<1\). Its second per-capita rate along this nullcline is
\[
H(v,k)=\frac{2}{1+k(1-v)}-1-\tau v.
\]
On the physical interval, the equation \(H=0\) is equivalent to
\[
k=K_\tau(v)=\frac{1-\tau v}{(1-v)(1+\tau v)},\qquad
K_\tau'(v)=-\frac{\tau^2v^2-2\tau v+2\tau-1}{(1-v)^2(1+\tau v)^2}.
\]
The numerator of the derivative before the minus sign has roots \((1\pm\rho)/\tau\). It is positive at \(v=0\) and negative at \(v=1\), so exactly the smaller root \(v_f=(1-\rho)/\tau\) lies in \((0,1)\); the plus branch lies above 1 and does not yield coexistence. The sign changes strictly at this simple root. Consequently \(K_\tau\) decreases from 1 at \(v=0\) to its unique nondegenerate minimum and increases thereafter to infinity as \(v\uparrow1\). Substitution of \(v_f\) gives \(k_f(b)\). The identity \(2\tau=2-\rho^2\) gives the width formula and \(k_f(b)-1/2=(4\rho-3\rho^2)/(2(2-\rho)^2)>0\). The stated counts follow by horizontal intersection with the two monotone branches. At \(k=1\) the smaller intersection is no longer positive: it is \(v=0\); the remaining intersection has \(v=(2\tau-1)/\tau\in(0,1)\).

At an interior equilibrium the Jacobian has trace \(-u-bv<0\) and determinant \(-uv\,\partial_v H\). Also \(\partial_k H=-2(1-v)/(1+k(1-v))^2<0\), and differentiating \(H(v,K_\tau(v))=0\) shows that \(\partial_vH\) has the sign of \(K_\tau'\). These signs prove the stated sink and saddle classification. At the minimum the trace is nonzero and \(\partial_{vv}H=-\partial_k H\,K_\tau''\ne0\). Eliminating the first equilibrium equation is regular since its \(u\)-derivative at the positive equilibrium is \(-u\ne0\). Together with \(\partial_kH\ne0\), the nonzero second derivative gives the ordinary saddle-node.

The eigenvalues at \((0,2/b)\) are \(1-2/b,-2\), and at \((1,0)\) they are \(-1,(1-k)/(1+k)\). At \(k=1\) the center eigendirection of the latter is \((-1,1)\). On the center manifold \(u=1-v+O(v^2)\), substitution into the second vector field gives \(\dot v=-(b-3/2)v^2+O(v^3)\). This attracts on the positive side. The local stable-fiber projection preserves the side: the fiber of the boundary equilibrium is the invariant \(v=0\) axis and the projection is transverse to it. Hence sufficiently near nonnegative trajectories also converge there.

Finally, substituting \(\rho=\sqrt{1-2\eta}=1-\eta-\eta^2/2+O(\eta^3)\) into the exact width yields its expansion. For an exact example inside the wedge take \((b,k)=(8/5,99/100)\); the two positive values of \(v\) are \((17\pm2\sqrt{31})/99\), in increasing order with the minus sign first.

## Verification

Run `python3 verify.py` (Python 3 with SymPy). It verifies the polynomial elimination, the two stationary branches and their fold values, the calibrated width expansion, the normalized critical-boundary quadratic term and the exact two-root witness. The proof, not the computation, supplies the allowed domain, branch ordering, stability classification and all-parameter quantifiers.

## Relationship to prior work and limitations

Srivastava, Takyi and Parshad give the same rational fear model, its general coexistence quadratic, sufficient regimes and qualitative saddle-node behavior. In the arXiv version these are Eq. (2), Eqs. (3)–(4), and Remark 3. Their formal Theorem 2.19 treats the opposite fear orientation. In particular the sufficient two-root regime with \(b_1b_2>2c_1c_2\) does not cover this slice. Here the comparison is the complete phase diagram in the physical interval \(0<v<1\), including its exact two boundaries and their separation; the general quadratic is not new.

Saputra, van Veen and Quispel show generic saddle-node–transcritical tangency for a different model; qualitative tangency is not new. Chen, Chen, Srivastava and Parshad give the related degenerate \((1,0)\) reduction in the allelopathic model (Eqs. (16)–(17)). Its coefficients can be specialized continuously to zero toxin release, accounting for the boundary cubic and quadratic coefficients; no originality is claimed here for those normal-form coefficients or their scalar critical-decay consequences. The prior calculations do not give this specific global-in-\(k\) physical equilibrium classification. Earlier equivalent calculations outside the inspected sources cannot be excluded.

## References

- V. Srivastava, E. M. Takyi and R. D. Parshad, *The effect of “fear” on two species competition*, arXiv:2210.10280, DOI: 10.3934/mbe.2023388.
- K. V. I. Saputra, L. van Veen and G. R. W. Quispel, *The saddle-node-transcritical bifurcation in a population model with constant rate harvesting*, arXiv:1002.4150, DOI: 10.3934/dcdsb.2010.14.233.
- S. Chen, F. Chen, V. Srivastava and R. D. Parshad, *Dynamical Analysis of an Allelopathic Phytoplankton Model with Fear Effect*, arXiv:2309.08383.
