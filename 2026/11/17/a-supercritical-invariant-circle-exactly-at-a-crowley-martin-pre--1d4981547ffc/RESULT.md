# A supercritical invariant circle exactly at a Crowley–Martin prey-nullcline vertex

## Finding

For the positive Crowley–Martin predator–prey vector field
\[
 f_1(x,y)=3x\left(1-\frac{x}{3}\right)-\frac{4xy}{(1+x)(1+y/2)},\qquad
 f_2(x,y)=\frac{4xy}{(1+x)(1+y/2)}-y,
\]
consider the forward-Euler family \(F_h(x,y)=(x,y)+h(f_1,f_2)(x,y)\), with \(h>0\). The coexistence fixed point \(P=(1,2)\) lies precisely at the unique maximum of the positive prey nullcline. It is a locally exponentially attracting fixed point for \(0<h<1\) and a repelling fixed point for \(h>1\). At \(h=1\), the family undergoes a **nondegenerate supercritical Neimark–Sacker bifurcation**, with exact first radial coefficient \(-1/4\) in the normalization below. Consequently, for \(h>1\) sufficiently close to \(1\), there is a locally attracting invariant closed curve around \(P\), wholly contained in the positive quadrant. In the complex coordinate \(w\) normalized by the right eigenvector \(q=(1,(1-i\sqrt7)/2)^T\), its leading radius is
\[
 |w|=\sqrt{h-1}+O(h-1).
\]
Thus one may parametrize the curve, at leading order, by
\[
 x=1+2\sqrt{h-1}\cos\phi+O(h-1),\qquad
 y=2+\sqrt{h-1}(\cos\phi+\sqrt7\sin\phi)+O(h-1).
\]
The error terms are uniform in \(\phi\). This is a local statement, not a global positivity theorem for the Euler map.

## Assumptions and scope

Both state variables are positive, and the parameters are fixed exactly as displayed. Only the Euler step \(h>0\) varies. The rational vector field and the map are smooth near \(P\). A Neimark–Sacker invariant curve means a smooth, invariant, locally attracting Jordan curve in a neighborhood of \(P\); its dynamics need not be an irrational rotation at every parameter. The bifurcation statements concern an arbitrarily small but nonzero one-sided interval of \(h\) around \(1\).

## Proof

**Nullcline geometry.** Dividing \(f_1=0\) by positive \(x\), the positive prey nullcline is \(y=g(x)\), where
\[
 H(x)=(3-x)(1+x)=3+2x-x^2,\qquad
 g(x)=\frac{H(x)}{4-H(x)/2}.
\]
On the physical prey interval \(0<x<3\), \(H(x)\le4\), so the denominator is positive; \(g\) has its unique positive maximum at \(x=1\), where \(g(1)=2\), \(g'(1)=0\), and \(g''(1)<0\). The predator equation also vanishes at \(P=(1,2)\).

**Spectral crossing.** The flow Jacobian and the Jacobian of the Euler map at the fixed point are
\[
 J=Df(P)=\begin{pmatrix}0&-1/2\\1&-1/2\end{pmatrix},\qquad
 A_h=I+hJ.
\]
The eigenvalues of \(A_h\) are
\[
 \lambda_\pm(h)=1-\frac h4\pm i\frac{\sqrt7h}{4},
\quad |\lambda_\pm(h)|^2=1-\frac h2+\frac{h^2}{2}.
\]
They are strictly inside the unit disk when \(0<h<1\), and strictly outside it when \(h>1\). At \(h=1\), \(\lambda=(3+i\sqrt7)/4\) has modulus one, \(\lambda^j\ne1\) for \(j=1,2,3,4\), and
\[
 \left.\frac{d}{dh}|\lambda_+(h)|\right|_{h=1}=\frac14>0.
\]
The equilibrium is therefore transversely crossing and free from low-order resonance.

**Exact cubic normal form.** Put \(A=A_1\), \(q=(1,2(1-\lambda))^T\), and \(\bar q\) for its complex conjugate. Let \(p^*\) be the left eigenrow of \(A\) for \(\lambda\), normalized so \(p^*q=1\). One explicit choice is
\[
 p^*=\frac{(1,\lambda-1)}{1+2(\lambda-1)(1-\lambda)}.
\]
Let \(B=D^2F_1(P)\), \(C=D^3F_1(P)\) be symmetric multilinear derivatives. Since \(F_1=\mathrm{id}+f\), these higher derivatives equal the derivatives of \(f\). The distinct second- and third-order components, ordered by differentiation in \(x,y\), are
\[
 \begin{array}{c|rrrrrrr}
 &xx&xy&yy&xxx&xxy&xyy&yyy\\
 f_1&-1&-1/4&1/4&-3/2&1/4&1/8&-3/16\\
 f_2&-1&1/4&-1/4&3/2&-1/4&-1/8&3/16
 \end{array}.
\]
The standard nonresonant map normal-form computation, with the convention that \(w\) multiplies \(q\) (not \(q/2\)), gives the cubic resonant term
\[
 G=\frac12p^*C(q,q,\bar q)
 +p^*B\big(q,(I-A)^{-1}B(q,\bar q)\big)
 +\frac12p^*B\big(\bar q,(\lambda^2I-A)^{-1}B(q,q)\big).
\]
Both inverses exist because \(\lambda\ne1\) and \(\lambda^2\notin\{\lambda,\bar\lambda\}\). Exact substitution and simplification yields
\[
 G=-\frac7{20}+i\frac{\sqrt7}{140},\qquad
 \ell_1=\operatorname{Re}(\bar\lambda G)=-\frac14.
\]
In the associated complex normal form, the radial update is
\[
 r_{n+1}=r_n\left(1+\frac{h-1}{4}-\frac{r_n^2}{4}
 +O((h-1)^2+|h-1|r_n^2+r_n^4)\right).
\]
Here the phase is eliminated through nonresonant near-identity coordinate changes. The nonzero negative cubic coefficient and positive transverse crossing meet the classical Neimark–Sacker theorem hypotheses: a locally attracting invariant curve is born for \(h>1\), with radial size \(r=\sqrt{h-1}+O(h-1)\). Transforming back with \((x,y)-P=wq+\bar w\bar q+O(|w|^2)\) gives the leading coordinate parametrization in the finding. Its distance from \(P\) tends to zero, so the entire curve is physical for sufficiently small \(h-1>0\).

## Verification

The attached standalone `verify_vertex_ns.py` uses exact rational and quadratic-field symbolic algebra to reconstruct the vector-field derivatives, nullcline curvature, both eigenvectors, normalized left eigenrow, both multilinear tensors, the cubic coefficient \(G\), the radial coefficient \(\ell_1\), low-order nonresonance, and crossing derivative. Executing `python verify_vertex_ns.py` with Python 3 and SymPy ends with `ALL EXACT CHECKS PASSED`. Its exact calculations are supplementary to the displayed derivation and the standard Neimark–Sacker theorem; finite iteration is not used as a proof of existence.

## Relationship to prior work

Chan-López, Martín-Ruiz and Castellanos, arXiv:2603.24418v2, establish a geometric localization principle and the exact linear Euler determinant identity for oscillatory bifurcations. Their revised Section 6 explicitly allows crossing the nullcline vertex at a step-size boundary. Therefore, the linear feasibility or existence of a **unit-modulus spectral crossing at a vertex is not claimed as new**. The added result here is a fully specified nonlinear crossing at that geometric boundary, with a rigorously negative exact cubic coefficient and the corresponding sharp first-order invariant-curve amplitude.

Zhang et al. (2018) study Neimark–Sacker bifurcations for Crowley–Martin discrete predator–prey models and obtain general bifurcation criteria. Their framework is related but the examined result does not give the above exact vertex-anchored coefficient or radius. Related earlier studies may subsume some qualitative conclusions, so priority for the specialized nonlinear calculation is subject to further historical checking.

## Limitations

The theorem is local to this particular parameter choice, not a classification for all Crowley–Martin models. It does not assert global positivity of the forward-Euler discretization, global attraction, or absence of other attractors; the invariant circle is confined to the positive quadrant only when \(h-1>0\) is sufficiently small. The normal-form radius depends on the declared eigenvector normalization. No independent mathematical audit has been performed.

## References

1. E. Chan-López, A. Martín-Ruiz and V. Castellanos, *Nullcline geometry constrains the location of oscillatory instabilities in planar predator–prey systems*, arXiv:2603.24418v2 (revised 17 August 2026; first publicly posted 25 March 2026). https://arxiv.org/html/2603.24418v2
2. H. Zhang et al., *Complex Dynamics on the Routes to Chaos in a Discrete Predator–Prey System with Crowley–Martin Type Functional Response*, *Discrete Dynamics in Nature and Society* (2018), Article 2386954. https://doi.org/10.1155/2018/2386954
3. J. Ren, L. Yu and S. Siegmund, *Bifurcations and chaos in a discrete predator–prey model with Crowley–Martin functional response*, *Nonlinear Dynamics* (2017). https://doi.org/10.1007/s11071-017-3643-6
