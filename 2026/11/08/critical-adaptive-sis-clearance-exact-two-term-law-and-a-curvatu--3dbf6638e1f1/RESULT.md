# Critical adaptive SIS clearance: exact two-term law and a curvature sign transition

## Finding

At the exact reproduction threshold of a prevalence-responsive SIS contact network, monotone risk responses force **global disease clearance**, but clearance is only algebraic. Every initially infected solution has the same two leading asymptotic coefficients:

\[
\frac{1}{y(t)}=K t+B\log t+C_{y(0),z(0)}+o(1),\qquad t\to\infty.
\]

The leading coefficient \(K\) depends on the first derivatives of the risk-response functions; the logarithmic coefficient \(B\) also depends on their second derivatives. An explicit positive, monotone link-breaking family has \(K=3/2\) for all its members but \(B=\kappa/3-1/4\), whose sign switches exactly at \(\kappa=3/4\).

## Assumptions and scope

Time is the nondimensionalized time of the original adaptive SIS equations. Let \(y(t)\in[0,1]\) denote prevalence and \(z(t)\in[0,1]\) denote mean link density. Study

\[
\dot y=-y+\tau y(1-y)z,\qquad
\dot z=-\zeta z b(y)+\xi(1-z)c(y).
\]

Assume \(\xi,\zeta>0\), \(b,c\in C^3([0,1])\), \(b(y),c(y)>0\) for all \(y\in[0,1]\), and \(b'(y)\ge0\), \(c'(y)\le0\) there. The names \(b\) and \(c\) mean respectively link breaking and link creation. Define

\[
L_0=\zeta b(0)+\xi c(0),\qquad z_0=\frac{\xi c(0)}{L_0}\in(0,1),\qquad \tau=\frac{1}{z_0}.
\]

Thus the basic reproduction number is exactly \(\mathcal R_0=\tau z_0=1\). Initial conditions are **all** \(y(0)\in(0,1]\) and \(z(0)\in[0,1]\). Neither strict initial positivity of contact density nor monotonicity of the actual trajectory is needed. Define the response jets at zero:

\[
\begin{aligned}
L_1&=\zeta b'(0)+\xi c'(0),\\
A_1&=\xi(1-z_0)c'(0)-\zeta z_0b'(0),\\
A_2&=\tfrac12[\xi(1-z_0)c''(0)-\zeta z_0b''(0)],\\
h_1&=\frac{A_1}{L_0},\quad K=1-\tau h_1,\\
h_2&=\frac{A_2+(K-L_1)h_1}{L_0},\quad B=\frac{\tau(h_1-h_2)}{K}.
\end{aligned}
\]

The monotonicity assumptions imply \(A_1\le0\) and therefore \(K\ge1\). All constants \(L_0,z_0,L_1,A_1,A_2,h_1,h_2,K,B\) are determined solely by the model parameters and functional responses. Only the finite constant \(C_{y(0),z(0)}\) depends on the initial state.

## Proof

**1. Invariance and a global upper bound.** At \(y=0\), \(\dot y=0\); at \(y=1\), \(\dot y=-1\). At \(z=0\) the link derivative is positive, and at \(z=1\) it is negative. Hence the unit square is invariant, and uniqueness preserves \(y(t)>0\) for every finite \(t\) if \(y(0)>0\). Monotonicity of \(b\) and \(c\) implies

\[
\dot z\le-\zeta b(0)z+\xi c(0)(1-z)
=-L_0(z-z_0).
\]

Consequently \(z(t)-z_0\le [z(0)-z_0]_+e^{-L_0t}\), where \([u]_+=\max\{u,0\}\). Using \(\tau z_0=1\) and \(1-y\in[0,1]\),

\[
\dot y=-y^2+\tau y(1-y)(z-z_0)
\le-y^2+g(t)y,\qquad
 g(t)=\tau[z(0)-z_0]_+e^{-L_0t}.
\]

Set \(G(t)=\int_0^t g(s)\,ds\), which is uniformly bounded, and \(v(t)=y(t)e^{-G(t)}\). Then \(\dot v\le-e^{G(t)}v^2\le-v^2\), so \(v(t)\le [v(0)^{-1}+t]^{-1}\). In particular \(y(t)=O(t^{-1})\to0\), without assuming any a priori local attraction.

**2. Recovery of link equilibrium and slow variation.** Write \(L(y)=\zeta b(y)+\xi c(y)\). The link equation is \(\dot z+L(y(t))z=\xi c(y(t))\). Since \(y(t)\to0\), \(L(y(t))\to L_0>0\) and \(\xi c(y(t))\to\xi c(0)\), scalar variation of constants gives \(z(t)\to z_0\). Hence

\[
\frac{\dot y(t)}{y(t)}=-1+\tau(1-y(t))z(t)\longrightarrow0.
\]

For every fixed \(\epsilon>0\), the relative variation of \(y\) eventually obeys \(e^{-\epsilon(t-s)}\le y(t)/y(s)\le e^{\epsilon(t-s)}\) for \(t\ge s\) sufficiently large. This also makes every exponentially decaying transient \(o(y(t)^j)\) for every fixed integer \(j\ge1\).

**3. Stable-response expansion.** Put \(w=z-z_0\). It satisfies the exact equation

\[
\dot w=A(y)-L(y)w,
\quad A(y)=\xi(1-z_0)c(y)-\zeta z_0b(y),
\]

where \(A(0)=0\), \(A(y)=A_1y+A_2y^2+O(y^3)\) and \(L(y)=L_0+L_1y+O(y^2)\). The stable variation-of-constants formula and slow variation from Step 2 first give \(w=O(y)\); substituting in the prevalence equation gives \(\dot y=O(y^2)\). Subtracting \(h_1y\), where \(L_0h_1=A_1\), produces a stable linear equation with forcing \(O(y^2)\), hence

\[
w=h_1 y+O(y^2),\qquad
\dot y=-K y^2+O(y^3),\qquad K=1-\tau h_1\ge1.
\]

The same stable-convolution estimate is valid for every forcing \(O(y^j)\): choose \(\epsilon<L_0/(2j)\) in the relative-variation inequality to bound its recent-time convolution by \(O(y(t)^j)\), and its old-time contribution is exponentially small. Now set \(R=w-h_1 y-h_2y^2\). Expanding the exact identity for \(\dot w\) and using \(\dot y=-K y^2+O(y^3)\), its terms of order \(y^2\) cancel precisely when

\[
-L_0h_2+A_2-L_1h_1=-K h_1,
\quad\text{i.e.}\quad h_2=\frac{A_2+(K-L_1)h_1}{L_0}.
\]

Thus \(\dot R=(-L_0+O(y))R+O(y^3)\). Stable convolution gives \(R=O(y^3)\), proving

\[
z=z_0+h_1y+h_2y^2+O(y^3).
\]

**4. Exact logarithmic coefficient and finite remainder.** Substitution into the prevalence equation yields

\[
\dot y=-K y^2+\tau(h_2-h_1)y^3+O(y^4).
\]

For \(r(t)=1/y(t)\),

\[
\dot r=K+\frac{\tau(h_1-h_2)}{r}+O(r^{-2}).
\]

Since \(y(t)\to0\) and \(\dot r\to K\), \(r(t)/t\to K\). Consequently \(r(t)=Kt+O(\log t)\). With \(B=\tau(h_1-h_2)/K\),

\[
\frac{d}{dt}[r(t)-Kt-B\log t]
=O\!\left(\frac{\log t}{t^2}\right).
\]

The derivative is absolutely integrable at infinity, so \(r-Kt-B\log t\) converges to a finite constant. This proves all asymptotics and the absence of an initial-condition-dependent leading or logarithmic coefficient.

**5. Exact curvature transition.** Choose

\[
 b(y)=1+y+\kappa y^2,\qquad c(y)=1,\quad
 \xi=\zeta=1,\quad\tau=2,\quad\kappa\ge0.
\]

These responses are positive and monotone on the entire physical interval. Direct differentiation gives \(z_0=1/2\), \(L_0=2\), \(L_1=1\), \(A_1=-1/2\), \(A_2=-\kappa/2\), \(h_1=-1/4\), \(K=3/2\), \(h_2=-\kappa/4-1/16\), and

\[
B=\frac{\kappa}{3}-\frac14.
\]

Thus the sign is negative when \(0\le\kappa<3/4\), zero at \(\kappa=3/4\), and positive when \(\kappa>3/4\). No lower-order constant or threshold changes with curvature.

## Verification

The standalone `verify.py` reproduces the symbolic cancellation of the first two stable-manifold coefficients for formal Taylor jets, evaluates the rational example exactly, and checks the sign-change threshold. As a separate diagnostic it integrates the full two-dimensional system at \(\kappa=0\) and \(\kappa=1\), comparing \(1/y(t)-(3/2)t-B\log t\) at two large times. The computed residuals approach finite values (approximately \(1.9506\) and \(1.7414\), respectively, for the stated initial condition). The proof above, not finite numerical integration, establishes the infinite-time statements. Run with `python verify.py` using Python, SymPy, SciPy and NumPy.

## Relationship to prior work

Achterberg and Sensi introduced these adaptive SIS equations (arXiv:2209.01224, equation (3)) and calculated the disease-free reproduction number and Jacobian eigenvalues. They explicitly leave the stability test unresolved at equality and study examples, equilibria and absence of cycles instead; their constant-response example is a decoupled special case. Achterberg, Sensi and Sottile (arXiv:2407.17639) generalize the dynamics to heterogeneous communities and prove disease-free global stability **strictly below** threshold. The present result supplies a **single-community monotone-response equality theorem** with a full second-order asymptotic and a curvature-controlled sign change, rather than claiming a new reproduction-number formula or qualitative SIS threshold. The zero-baseline-link-breaking multigroup critical asymptotic previously known in related work has \(b(0)=0\), whereas the theorem here assumes \(b(0)>0\) and resolves a different parameter region and the logarithmic term. Generic planar center-manifold arguments suggest algebraic relaxation but do not independently provide the global, response-jet-specific finite-remainder formula.

## Limitations

The theorem assumes strictly positive response functions, monotone breaking/creation, and three derivatives at the disease-free state. It concerns the deterministic mean-field ODE, not an exact stochastic network or an individual-level contact process. The error \(o(1)\) refers to the inverse prevalence after subtracting the displayed linear and logarithmic terms; it is not a uniform-in-parameters error. Only critical \(\mathcal R_0=1\) is analyzed, not the endemic side or transient peaks. The contact-density expansion is an asymptotic trajectory statement, not a globally invariant polynomial graph. Full novelty against unknown or unindexed literature is not provable by retrieval alone.

## References

1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224v1, first submitted 2022-09-02 UTC; published in *Nonlinear Dynamics* 111 (2023), 12657–12670, DOI:10.1007/s11071-023-08498-4. Primary full text: https://arxiv.org/abs/2209.01224 and https://link.springer.com/article/10.1007/s11071-023-08498-4.
2. M. A. Achterberg, M. Sensi, and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639v1 (2024-07-24); revised HTML text: https://arxiv.org/html/2407.17639v3.
