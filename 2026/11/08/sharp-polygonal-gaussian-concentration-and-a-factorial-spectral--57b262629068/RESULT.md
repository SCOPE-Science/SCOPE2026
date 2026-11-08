# Sharp polygonal Gaussian concentration and a factorial spectral correction

## Finding

Fix \(A>0\). Let \(\Pi_{N,A}\) be the centered regular \(N\)-gon of area \(A\), oriented with one side midpoint at angle zero, \(N\ge3\). For the normalized Gaussian \(\varphi(t)=2^{1/4}e^{-\pi t^2}\), let \(P_N=V_\varphi^*\mathbf1_{\Pi_{N,A}}V_\varphi\) and \(\Lambda_N=\|P_N\|\). Put \(h=\pi/N\) and define its Gaussian test value
\[
 a_N=1-\frac12\int_{-1}^1\exp[-A h\cot h\sec^2(hu)]\,du.
\]
For all sufficiently large \(N\), the top eigenvalue is simple, and its exact optimization gain has the sharp **factorial** law
\[
 \boxed{\lim_{N\to\infty}\frac{N^4N!}{A^{N+2}}(\Lambda_N-a_N)=\frac{4e^{-2A}}{1-e^{-A}}.}
\]
The corresponding deficit from the equal-area disk optimum has the expansion
\[
\begin{aligned}
1-e^{-A}-\Lambda_N=e^{-A}\bigg[&\frac{2A^2}{45}h^4+\frac{4A^2(15-2A)}{2835}h^6\\
&+\frac{2A^2(5A^2-28A+63)}{14175}h^8+O_A(h^{10})\bigg].
\end{aligned}
\]
In particular its leading coefficient is \(2\pi^4A^2e^{-A}/45\) at inverse-fourth-power scale, despite second-order radial boundary displacement.

Under the normalized Bargmann transform, let \(e_k(z)=\pi^{k/2}z^k/\sqrt{k!}\) be the Fock orthonormal basis. The unit top eigenfunction \(F_N\), normalized to have positive vacuum coefficient, obeys in Fock norm
\[
 \boxed{F_N=e_0-\frac{2e^{-A}}{1-e^{-A}}\frac{A^{N/2+1}}{N^2\sqrt{N!}}e_N
 +o_A\left(\frac{A^{N/2+1}}{N^2\sqrt{N!}}\right).}
\]
Thus symmetry forces the first optimizer adjustment to Hermite degree \(N\), and the benefit of that adjustment is smaller than every algebraic order.

## Assumptions and scope

The area \(A>0\) is fixed while the integer \(N\to\infty\); no uniformity in \(A\) is asserted. The underlying Fock norm is \(\|F\|^2=\int_{\mathbb C}|F(z)|^2e^{-\pi|z|^2}dA(z)\). Polygon orientation determines the sign of the displayed degree-\(N\) coefficient; rotation changes its phase. The disk reference value \(1-e^{-A}\) is the known global bound for Gaussian STFT concentration, but its polygonal rate and the factorial correction are proved below.

## Proof

**Exact area and vacuum integral.** Set \(h=\pi/N\). The inradius \(r\) satisfies \(Nr^2\tan h=A\). On each angular sector the endpoint in the variable \(t=\pi|z|^2\) is \(S_N(u)=Ah\cot h\sec^2(hu)\), \(-1\le u\le1\). Exact area normalization gives \(\frac12\int_{-1}^1 S_N(u)du=A\), and polar integration gives the displayed \(a_N\).

**Disk gap and simplicity.** For the equal-area disk, Fock monomials diagonalize localization with eigenvalues \(d_k=(k!)^{-1}\int_0^Ae^{-t}t^kdt\). The largest eigenvalue is \(d_0=1-e^{-A}\), and the next is \(d_1=1-(1+A)e^{-A}\), leaving gap \(Ae^{-A}>0\). The reproducing-kernel inequality \(e^{-\pi|z|^2}|F(z)|^2\le\|F\|^2\) bounds the operator-norm difference between two indicator masks by the measure of their symmetric difference. Since the polygon differs from the disk in area by \(O_A(N^{-2})\), its top eigenvalue is eventually simple with a uniform positive gap to the remaining spectrum.

**Cyclic selection and first coupling.** In the orthogonal decomposition \(\mathbb Ce_0\oplus e_0^\perp\), write the operator as \(\begin{psmallmatrix}a_N&v_N^*\\v_N&B_N\end{psmallmatrix}\). Its \(N\)-fold rotational invariance forces \(\langle e_k,P_Ne_0\rangle=0\) unless \(N\mid k\). At the first allowed degree the exact formula, after subtracting the radial disk contribution, is
\[
 v_{N,N}=\frac1{2\sqrt{N!}}\int_{-1}^1\cos(\pi u)\int_A^{S_N(u)}e^{-t}t^{N/2}dt\,du.
\]
Uniformly in \(u\in[-1,1]\),
\[
 S_N(u)-A=\frac{A\pi^2}{N^2}(u^2-\tfrac13)+O_A(N^{-4}).
\]
Over these signed intervals, \(e^{-t}t^{N/2}\) varies by a relative \(O_A(N^{-1})\). Using \(\frac12\int_{-1}^1(u^2-1/3)\cos(\pi u)du=-2/\pi^2\) yields
\[
 v_{N,N}=-\frac{2e^{-A}A^{N/2+1}}{N^2\sqrt{N!}}(1+O_A(N^{-1})).
\]
For any fixed \(M_A>\sup_{N\ge N_0,u}S_N(u)\), the integral representation bounds the vacuum coupling at index \(k\) by \(M_A^{k/2+1}/\sqrt{k!}\). Consequently the total squared coupling in degrees \(2N,3N,\ldots\) is \(O_A(M_A^{2N}/(2N)!)=o_A(|v_{N,N}|^2)\). Hence \(\|v_N\|^2=|v_{N,N}|^2(1+o_A(1))\).

**Schur complement and first eigenvector coefficient.** The top eigenvalue satisfies
\[
 \Lambda_N-a_N=\langle v_N,(\Lambda_N-B_N)^{-1}v_N\rangle.
\]
The resolvent is uniformly bounded by the disk spectral gap. Since \(\|B_Ne_N\|\le d_N+O_A(N^{-2})\to0\) and \(\Lambda_N\to d_0\), we have \((\Lambda_N-B_N)^{-1}e_N=d_0^{-1}e_N+o_A(1)\) in norm. The first coupling dominates all later allowed degrees, so
\[
 \Lambda_N-a_N=\frac{|v_{N,N}|^2}{d_0}(1+o_A(1))
 =\frac{4e^{-2A}}{1-e^{-A}}\frac{A^{N+2}}{N^4N!}(1+o_A(1)).
\]
The orthogonal component of its normalized eigenvector is \((\Lambda_N-B_N)^{-1}v_N\) times the vacuum coefficient; the normalization changes the vacuum coefficient only by \(O_A(\|v_N\|^2)\). This proves the displayed sharp eigenfunction asymptotic.

**Disk deficit.** Taylor-expand \(S_N(u)/A=h\cot h\sec^2(hu)\), then the exponential in \(a_N\). Exact area conservation cancels the first moment. Integrating the polynomial coefficients over \(u\in[-1,1]\) produces the terms \(2A^2/45\), \(4A^2(15-2A)/2835\), and \(2A^2(5A^2-28A+63)/14175\) at orders \(h^4,h^6,h^8\). Uniform analyticity for sufficiently small \(h\) gives remainder \(O_A(h^{10})\). The factorial optimization gain is \(o_A(h^j)\) for every fixed positive \(j\), completing the expansion.

## Verification

`check_polygon.py` checks the exact mean-area identity and Taylor coefficients symbolically using SymPy, and checks the leading vacuum and Fock-coupling limits with high-precision mpmath quadrature. A two-mode matrix compression corroborates the factorial coefficient. The command `python check_polygon.py` prints `POLYGON_FOCK_CHECKS_PASS 73`. Numerical checks are finite tests and do not replace the analytic proof of the all-\(N\) limits.

## Relationship to prior work

Nicola and Tilli prove sharp global disk extremality and identify its Gaussian optimizer. Gómez, Guerra, Ramos, and Tilli establish the optimal stability exponent and a second-variation analysis for the signal component. These results imply neither the exact fourth-order polygonal coefficient nor the factorially small difference between the optimized value and the vacuum test, nor the explicit degree-\(N\) optimizer correction. A fixed-profile smooth-boundary Hessian does not by itself provide this uniform limit for a nonsmooth family with increasing angular frequency. Earlier spectral approximation results for Toeplitz operators remain a possible source of an equivalent formulation.

## Limitations

The theorem is asymptotic with fixed area and no effective universal minimum side count. It describes the top eigenvalue and eigenfunction only, not the remaining polygonal spectrum. The leading eigenfunction correction is orientation-dependent. The symbolic and quadrature checks test finitely many cases and do not establish historical priority.

## References

1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, Inventiones Mathematicae 230 (2022), 1–30. DOI: 10.1007/s00222-022-01119-8. First preprint: arXiv:2106.03423 (2021-06-07).
2. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber-Krahn inequality for the Short-time Fourier Transform*, Inventiones Mathematicae 236 (2024), 779–836. DOI: 10.1007/s00222-024-01248-2. First preprint: arXiv:2307.09304 (2023-07-18).
3. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Transactions on Information Theory 34 (1988), 605–612.
