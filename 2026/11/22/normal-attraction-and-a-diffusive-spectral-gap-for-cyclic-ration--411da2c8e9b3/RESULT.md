# Normal attraction and a diffusive spectral gap for cyclic rational-delay two-cycles

## Finding

For each integer \(k\ge2\), consider the cyclic rational recurrence
\[
 x^{(i)}_{n+1}=1+\frac{x^{(i+1)}_{n-1}}{x^{(i+1)}_n},\qquad
 i\in\mathbb Z/k\mathbb Z,
\]
with strictly positive current and previous states. Its **complete positive period-dividing-two set** is the one-parameter synchronous family
\[
 X_{2m}=r\mathbf1,\qquad X_{2m+1}=s\mathbf1,\qquad
 s=\frac{r}{r-1},\quad r>1.
\]
The member \(r=2\) is a fixed state; the other members have primitive period two. Every member is locally attracting **to the family** under the two-step return map, with exactly one neutral tangent multiplier and \(2k-1\) strictly contracting transverse multipliers. Thus a neighboring trajectory converges exponentially to a possibly different member of the family, rather than necessarily to the prescribed member.

Set
\[
 d=\frac{r-1}{r^2}\in(0,1/4],\qquad
 q_j=e^{2\pi i j/k},\quad 0\le j<k.
\]
The complete characteristic polynomial of the \(2k\)-dimensional two-step Jacobian at that member is
\[
 \boxed{\prod_{j=0}^{k-1}
 \left[\lambda^2-(q_j+q_j^2d)\lambda+q_j^2d\right].}
\]
The \(j=0\) factor is \((\lambda-1)(\lambda-d)\). Both roots of every other factor lie strictly inside the open unit disk, for **every** finite \(k\ge2\) and every \(r>1\).

Let \(\rho_k(d)\) be the maximum modulus of all the transverse multipliers (all but the sole unit multiplier). For each fixed \(d\in(0,1/4]\), the **sharp spatial-size slowdown** is
\[
 \boxed{1-\rho_k(d)=\frac{2\pi^2d(1-3d)}{(1-d)^3k^2}+O_d(k^{-4})\quad(k\to\infty).}
\]
For each fixed finite \(k\), the limiting small-\(d\) behavior is
\[
 1-\rho_k(d)=(1-\cos(2\pi/k))d+O_k(d^2).
\]
Consequently there is no normal exponential-contraction factor bounded away from one uniformly over ring size or over all cycle amplitudes, although every individual finite-ring cycle is normally attracting.

## Assumptions and scope

The phase space is \((0,\infty)^{2k}\) with state \((X_n,X_{n-1})\), and the one-step shift is
\[
 \mathcal T(U,V)=(\mathbf1+SV/SU,\ U),
\]
where \(S\) is the cyclic forward shift and division is componentwise. The formula above concerns the derivative of \(\mathcal T^2\) at the state \((r\mathbf1,s\mathbf1)\). It is an exact-real local dynamical statement. The result does not assert global convergence of all positive initial states to the two-cycle manifold, nor that any individual cycle is an asymptotically stable isolated orbit.

## Proof

**1. Exhaustion of positive two-cycles.** Write the even and odd values as \(a_i,b_i>0\). The recurrence gives
\[
 a_i-1=\frac{a_{i+1}}{b_{i+1}},\qquad
 b_i-1=\frac{b_{i+1}}{a_{i+1}}.
\]
Hence \((a_i-1)(b_i-1)=1\), so \(b_i=a_i/(a_i-1)\). Substituting this identity at index \(i+1\) into the first equation yields \(a_i-1=a_{i+1}-1\). By cyclicity, all \(a_i\) equal \(r>1\), and all \(b_i\) equal \(s=r/(r-1)\). Conversely these values satisfy both recurrence equations. The two parameter values \(r,s\) represent opposite time phases of the same primitive cycle; \(r=s\) only at \(r=2\).

**2. Exact return spectrum.** The derivative of one step at a synchronous state with current coordinate \(u\) and previous coordinate \(v\) is
\[
 D\mathcal T_{(u\mathbf1,v\mathbf1)}=
 \begin{pmatrix}-(v/u^2)S&(1/u)S\\I&0\end{pmatrix}.
\]
At the two phases, put \(A_e=1/s\), \(B_e=-r/s^2\), \(A_o=1/r\), and \(B_o=-s/r^2\). A spatial Fourier eigenvector of \(S\) with eigenvalue \(q\) reduces the return derivative to the product of the two companion blocks
\[
 M_o(q)=\begin{pmatrix}qB_o&qA_o\\1&0\end{pmatrix},\qquad
 M_e(q)=\begin{pmatrix}qB_e&qA_e\\1&0\end{pmatrix}.
\]
The product order does not alter its trace or determinant. Direct simplification gives
\[
 A_o+A_e=1,\quad A_oA_e=B_oB_e=d,
\]
so the two-step Fourier trace is \(q+q^2d\), and its determinant is \(q^2d\), proving the factored polynomial. At \(q=1\) the roots are \(1,d\); the first is simple and tangent to the parameterized fixed curve of \(\mathcal T^2\).

**3. Strict transverse stability.** For a quadratic \(z^2-Tz+D\), the Schur–Cohn quadratic criterion states that both roots lie in \(|z|<1\) exactly when \(|D|<1\) and \(|T-\overline T D|<1-|D|^2\). Here \(T=q+q^2d\), \(D=q^2d\), \(q=e^{i\theta}\), and direct expansion gives the *exact strictness identity*
\[
 (1-d^2)^2-|T-\overline T D|^2
 =2d(1-\cos\theta)\bigl[1-2d-(1+2\cos\theta)d^2\bigr].
\]
For \(q\ne1\), the right side is positive because \(0<d\le1/4\) and the bracket is at least \(1-2d-3d^2\ge5/16\). The second Schur condition follows, and \(|D|=d<1\). All nonzero spatial modes are strictly stable. Since the lone tangent eigenvalue \(1\) is simple and all other eigenvalues have modulus less than one, a smooth local coordinate splitting into one tangential parameter and \(2k-1\) normal coordinates puts the return map in the form \(u'=u+O(\|v\|)\), \(v'=A(u)v+O(\|v\|^2)\). On a small compact parameter interval, a fixed adapted norm makes the normal update contract uniformly. Then \(\sum_n|u_{n+1}-u_n|<\infty\) and \(v_n\to0\) exponentially; hence each nearby orbit converges exponentially to some cycle in the family. This argument is local, and does not need invertibility of the full map.

**4. Sharp large-ring coefficient.** For \(q=e^{i\theta}\) near one, the characteristic equation has a unique analytic root \(\lambda_+(q)\) satisfying \(\lambda_+(1)=1\), as its derivative with respect to \(\lambda\) at \((1,1)\) is \(1-d>0\). Differentiating the equation twice in \(q\) gives
\[
 \lambda_+'(1)=\frac1{1-d},\qquad
 \lambda_+''(1)=\frac{2d(1-2d)}{(1-d)^3}.
\]
With \(q=e^{i\theta}\) this implies
\[
 |\lambda_+(e^{i\theta})|
 =1-\frac{d(1-3d)}{2(1-d)^3}\theta^2+O_d(\theta^4).
\]
The coefficient is positive on the entire stated range of \(d\). Other eigenvalues stay uniformly away from the unit circle outside any fixed neighborhood of \(q=1\); within that neighborhood the displayed expansion is strictly decreasing in \(|\theta|\) for sufficiently small nonzero \(|\theta|\). Therefore for sufficiently large \(k\), the two slowest modes are \(q=e^{\pm2\pi i/k}\), yielding the stated \(k^{-2}\) law and its \(O_d(k^{-4})\) remainder. Holding \(k\) fixed and expanding instead in \(d\downarrow0\) gives \(\lambda(q,d)=q+(q^2-q)d+O(d^2)\) for \(q\ne1\); maximizing the resulting modulus over the finite set of nontrivial roots of unity yields the small-\(d\) formula.

## Verification

Run `python verify_floquet.py` with Python 3 and NumPy. The supplied checker constructs the actual \(2k\)-dimensional two-step Jacobian, compares its computed eigenvalues with the Fourier factorization for multiple ring sizes and cycle amplitudes, checks strict contraction, tests the large-ring coefficient, and runs nearby positive trajectories. It passed 103 test groups in the preparation run. These finite checks are diagnostics; the Schur identity, Fourier reduction and analytic expansion above are the proof.

## Relationship to prior work

Quan, Lu, Wang, Zhou and Huang (2024) introduced the three-variable \(P\)-parameter ratio system, found its synchronous period-two family at \(P=1\), and classified its equilibrium stability for \(P\ne1\). The present result concerns the missing *transverse stability of that nonisolated period-two family*, its all-ring cyclic extension, and the exact slowdown constant as the number of variables increases. It neither reclaims the previously known existence of the two-cycles nor relies on generic stability statements alone. Classical Fourier and Schur–Cohn reductions are proof tools; the exact object-dependent spectral law is the result.

## Limitations

The result is local in the initial state near a chosen period-two member, and depends on the exact coefficient \(P=1\). It does not establish that every positive orbit converges to the family or determine which member an arbitrary distant orbit approaches. The convergence factor is a *two-step* (not one-step) multiplier. The asymptotic constant is for fixed cycle parameter \(d\) as \(k\to\infty\); the error is not claimed uniform as \(d\downarrow0\). The algebraic checker is not an independent proof or independent audit.

## References

1. W. Quan, X. Lu, L. Wang, J. Zhou and R. Huang, “Asymptotics and Periodicity of Positive Solutions on a Nonlinear Rational System of Difference Equations,” *Discrete Dynamics in Nature and Society* 2024, article 6565273, first published 2024-10-03, https://doi.org/10.1155/2024/6565273.
2. Classical Schur–Cohn quadratic unit-disk criterion and discrete Fourier diagonalization of cyclic shifts (standard results; explicit criterion and algebra appear above).
