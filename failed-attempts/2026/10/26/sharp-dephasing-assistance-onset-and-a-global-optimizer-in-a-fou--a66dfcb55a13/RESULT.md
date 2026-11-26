# Sharp dephasing-assistance onset and a global optimizer in a four-site tilted quantum chain

## Finding

For the four-site boundary-driven, linearly tilted XX chain defined below, set \(G=\Gamma>0\) and \(W=U^2\). Exactly one positive number \(W_c(G)\) solves \(P_G(W)=0\), where

\[
\begin{aligned}
P_G(W)={}&5308416W^5+(460800G^2+3538944)W^4\\
&+(14608G^4+513024G^2+9547776)W^3\\
&+(200G^6+16128G^4+157696G^2+5603328)W^2\\
&+(G^8+128G^6-1536G^4+90112G^2+2293760)W\\
&-192G^2(G^2+16)^2.
\end{aligned}
\]

The exact stationary spin current \(I_4(G,\gamma,U,f)\) has initial dephasing response

\[
\operatorname{sgn}\left.\frac{\partial I_4}{\partial\gamma}\right|_{\gamma=0}
=\operatorname{sgn}(U^2-W_c(G))
\qquad(G>0,\ U\ge0,\ 0<f<1).
\]

The critical tilt \(U_c(G)=\sqrt{W_c(G)}\) has opposite boundary-coupling asymptotics:

\[
U_c(G)\sim\sqrt{\frac3{140}}G\quad(G\downarrow0),\qquad
U_c(G)\sim\frac{8\sqrt3}{G}\quad(G\to\infty).
\]

Thus both very weak and quantum-Zeno-strong boundary coupling have vanishing onset tilt; the onset is strictly positive at every finite positive coupling and therefore attains a positive maximum at an intermediate coupling (uniqueness of that maximum is not claimed).

For the natural equal-rate section \(G=1\), the conclusion is global: if \(0\le U\le U_c(1)\), the stationary current is strictly decreasing for \(\gamma>0\). If \(U>U_c(1)\), the current has exactly one positive stationary point, a strict global maximum. Its threshold is

\[
U_c(1)=0.148539003114375\ldots,
\quad
5308416W^5+3999744W^4+10075408W^3+5777352W^2+2382465W-55488=0,
\quad W=U_c(1)^2.
\]

Writing \(\gamma_*(U)\) for the unique optimizer when it exists,

\[
\lim_{U\to\infty}\frac{\gamma_*(U)}{U}=1,
\qquad
\lim_{U\to\infty}U\frac{I_4(1,\gamma_*(U),U,f)}{f}=\frac43.
\]

## Assumptions and scope

Take a four-spin open chain, \(\hbar=J=1\), Hamiltonian

\[
H=\sum_{j=1}^3(\sigma_j^x\sigma_{j+1}^x+\sigma_j^y\sigma_{j+1}^y)
-U\sum_{j=1}^4 j\sigma_j^z,
\qquad U\ge0.
\]

Each site has a dephasing Lindblad jump \(\sqrt{\gamma/2}\sigma_j^z\), \(\gamma\ge0\). At the first site the raising and lowering jump rates are \(G(1+f)/2\) and \(G(1-f)/2\); at the last site they are reversed. Assume \(G>0\) and \(0<f<1\). The spin current observable is \(2(\sigma_j^x\sigma_{j+1}^y-\sigma_j^y\sigma_{j+1}^x)\), independent of the link in the stationary state. The response is the one-sided derivative at the physically allowed boundary \(\gamma=0\).

The exactly closed two-point stationary equations follow from the Lindblad generator; they determine this current without assuming any tridiagonal truncation. The result is finite-chain transport, not a thermodynamic phase transition. The total potential drop is \(3U\).

## Proof

The full stationary two-point system has exactly sixteen real unknowns. Introduce \(h_j^{(r)}\) for \(1\le r\le4,\ 1\le j\le5-r\), and \(b_j^{(r)}\) for \(2\le r\le4\) with the same site range. Symbols outside these ranges and all \(b_j^{(1)}\) are zero. Its boundary and continuity equations are

\[
G(1+h_1^{(1)})-4b_1^{(2)}=0,\quad
G(1-h_4^{(1)})-4b_3^{(2)}=0,\quad
b_j^{(2)}-b_{j-1}^{(2)}=0\ (j=2,3).
\]

For \(2\le r\le4\) and \(1\le j\le5-r\), put \(d_{jr}=\gamma+\frac G4(\mathbf{1}_{j=1}+\mathbf{1}_{j+r-1=4})\); the remaining equations are

\[
\begin{aligned}
0&=h_j^{(r-1)}-h_{j+1}^{(r-1)}+h_j^{(r+1)}-h_{j-1}^{(r+1)}+(r-1)U h_j^{(r)}+d_{jr}b_j^{(r)},\\
0&=b_j^{(r-1)}-b_{j+1}^{(r-1)}+b_j^{(r+1)}-b_{j-1}^{(r+1)}+(r-1)U b_j^{(r)}-d_{jr}h_j^{(r)}.
\end{aligned}
\]

The stationary current is exactly \(I_4=4f b_1^{(2)}\). Put \(F_4=I_4/f\). Cramer's rule on the full sixteen-dimensional matrix (reconstructed in `verify.py`) gives the following two exact expressions, without suppressing long-distance coherences:

\[
F_4(G,0,U)=\frac{64G(G^2+36U^2+16)}{(G^2+64U^2+16)(G^2U^2+4G^2+36U^4+48U^2+64)}.
\]

\[
\left.\partial_\gamma F_4\right|_{0}=
\frac{8P_G(U^2)}{(G^2+64U^2+16)^2(G^2U^2+4G^2+36U^4+48U^2+64)^2}.
\]

Every denominator factor is strictly positive. As a polynomial in \(W\), all nonconstant coefficients of \(P_G\) are positive. In particular the coefficient of \(W\) factors as

\[
(G^2+16)(G^6+112G^4-3328G^2+143360)>0.
\]

The latter inequality follows because the quadratic \(112x^2-3328x+143360\) has negative discriminant and positive leading coefficient for \(x=G^2\ge0\). Also \(P_G(0)=-192G^2(G^2+16)^2<0\). Therefore \(P_G\) is strictly increasing on \([0,\infty)\) and has exactly one positive root. Balancing the constant term with the linear term as \(G\downarrow0\) gives \(W_c(G)\sim3G^2/140\); as \(G\to\infty\), balance \(-192G^6+G^8W\) to obtain \(W_c(G)\sim192/G^2\). Continuity of the simple root and vanishing at both ends give an interior maximizer.

For the global equal-rate classification, substitute \(G=1\) in the exact rational function and write \(F_4(1,\gamma,U)=N(\gamma,W)/D(\gamma,W)\). The two polynomials have nonnegative coefficients in \(\gamma,W\), with a strictly positive constant in the denominator, and \(D>0\). The numerator of its derivative, \(Q=N_\gamma D-ND_\gamma\), has degree twelve in \(\gamma\). Its coefficients in ascending \(\gamma\) powers have these signs: coefficients of degrees 5 through 12 are strictly negative for \(W\ge0\); the degree-4 coefficient is

\[
-256(8847360W^4-2954752W^3+18913120W^2+4417642W+7015467)<0,
\]

as the first three terms factor as \(W^2\) times a positive quadratic with negative discriminant. The coefficients of degrees 0 through 3 each change sign exactly once, in order, at \(W\)-values lying respectively in

\[
(0.022,0.023),\quad (0.072,0.074),\quad
(0.244,0.246),\quad (1.04,1.06).
\]

Each uniqueness statement follows from one Descartes sign change for the respective coefficient polynomial in \(W\) and opposite rational endpoint signs. The degree-zero coefficient is \(32P_1(W)\). Consequently below or at \(W_c(1)\), all positive-\(\gamma\) coefficients are negative; above it the ordered coefficients of \(Q\) have exactly one sign change. Descartes' rule, \(Q(0)>0\), and its negative leading coefficient force exactly one positive zero of \(Q\); the current increases before that zero and decreases afterward.

Finally, at fixed \(c>0\), exact highest-degree terms give

\[
\lim_{U\to\infty}UF_4(1,cU,U)=\frac{8c}{3(1+c^2)}.
\]

The scaled derivative has the sign of \(1-c^2\) for large \(U\), at any fixed \(c\ne1\); the just-proved uniqueness brackets the maximizing \(\gamma/U\) between any \(c_-<1<c_+\). This proves convergence to \(1\), then the limiting optimized current \(4/3\).

## Verification

Run `python verify.py` (SymPy) to reconstruct the exact matrix, calculate all determinant identities, check coefficient positivity, verify the strict ordering of the four positive root intervals with rational arithmetic, and verify strong-tilt scaling. Run `python crosscheck_lindblad.py` (NumPy, SciPy and SymPy) to compare the exact current against five independently solved full \(16\)-dimensional Hilbert-space Lindblad stationary states. Both programs were executed successfully. Numeric root isolation for \(G=1\) gives \(U_c(1)\) as above; this numerical value is illustrative, not the existence proof.

## Relationship to prior work

Jacob et al. (2024) established this boundary-driven, tilted XX-chain model, the full correlation equations, exact \(L=2,3\) currents, and a tridiagonal approximation for longer chains (Sec. 3 of journal version, Sec. 5 of arXiv HTML). Their article notes the difficulty of analytic exact evaluation for \(L>3\); it does not state the full exact four-site onset polynomial, its two reservoir-coupling endpoint laws, or global uniqueness of the four-site optimal dephasing rate. Žnidarič and Horvat (2012/2013) provided the general stationary correlation-matrix reduction for XX chains with disorder and dephasing, and studied thermodynamic disorder-dependent transport and periodic-disorder resonances. That broad methodology includes the underlying linear equations but does not explicitly solve the present four-site linear-gradient threshold. The result credits both the model and its linear-algebra method; novelty is limited to the exact boundary and optimizer classification extracted from them.

## Limitations

The full all-\(G\) classification is for the sign of the **initial** response at zero dephasing; global unimodality and the existence of a positive global optimum are established only for \(G=1\). At other \(G\), initial suppression does not exclude a nonlocal enhancement at a larger dephasing rate. No uniqueness is claimed for the coupling \(G\) that maximizes \(U_c(G)\). The result does not establish its conclusions for chains of length at least five, interacting systems, nonuniform disorder, or other bath models. Because the exact matrix formalism was already known, the algebraic threshold could be derivable from previously published general equations; no claim of a new method is made.

## References

1. S. L. Jacob, L. P. Bettmann, A. M. Lacerda, K. Zawadzki, S. R. Clark, J. Goold, and J. J. Mendoza-Arenas, *Dephasing-assisted transport in a tight-binding chain with a linear potential*, arXiv:2407.21715v1 (31 July 2024); Frontiers in Physics 12, 1474018 (2024), https://arxiv.org/html/2407.21715v3 .
2. M. Žnidarič and M. Horvat, *Transport in a disordered tight-binding chain with dephasing*, arXiv:1207.5952 (25 July 2012), Eur. Phys. J. B 86, 67 (2013), https://arxiv.org/abs/1207.5952 .
