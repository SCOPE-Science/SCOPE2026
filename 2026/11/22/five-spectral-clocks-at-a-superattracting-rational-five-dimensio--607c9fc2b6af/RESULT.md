# Five spectral clocks at a superattracting rational five-dimensional map

## Finding

Consider the five-dimensional positive map defined by the recurrence
\[
 z_{n+1}=\frac{z_{n-1}z_{n-2}z_{n-4}+z_{n-1}+z_{n-2}+z_{n-4}+b}
 {z_{n-1}z_{n-2}+z_{n-1}z_{n-4}+z_{n-2}z_{n-4}+1+b},\qquad n\ge0.
\]
For every \(b\ge0\) and strictly positive initial history \(z_{-4},\ldots,z_0\), none of whose entries is \(1\), set
\[
 r_n=\frac{z_n-1}{z_n+1},\qquad u_n=-\log|r_n|,\qquad c=\log(1+b/4).
\]
Let \(P(t)=t^5-t^3-t^2-1\). Its roots are the simple real Perron root \(\rho=1.429108319838\ldots\), a conjugate pair \(\lambda,\bar\lambda\) of modulus \(1.125407111123\ldots>1\), and a conjugate pair \(\xi,\bar\xi\) of modulus \(0.743289112141\ldots<1\). Define for each root \(t\)
\[
 \ell_t=(1,t,t^2-1,t^{-2},t^{-1}),\quad
 S_t=3-t^{-2}+2t^{-5},\quad
 W=(u_0+c/2,u_{-1}+c/2,u_{-2}+c/2,u_{-3}+c/2,u_{-4}+c/2)^T,
\]
\[
 \varepsilon_k=\log\!\left(1+\frac b4\prod_{j\in\{1,2,4\}}(1-r_{k-j})\right),
 \qquad d_k=\varepsilon_k-c,
 \qquad A_t=\frac{\ell_t W+\sum_{k=0}^\infty t^{-k-1}d_k}{S_t}.
\]
All five series defining \(A_t\) converge absolutely, and **the following full spectral expansion holds** for some \(\gamma>0\):
\[
 \boxed{u_n=-\frac c2+\sum_{P(t)=0}A_t t^n+O(e^{-\gamma\rho^{n-4}}).}
\]
The coefficients of conjugate roots are conjugate. In particular, \(L=A_\rho>0\), and
\[
 u_n=L\rho^n+2\operatorname{Re}(A_\lambda\lambda^n)-\frac c2+O(|\xi|^n).
\]
Thus \(\log|z_n-1|=-L\rho^n+O(|\lambda|^n)\), and the first subleading oscillatory term in its logarithm **can grow exponentially** even though the absolute population deviation decays super-exponentially. At \(b=0\), the full five-mode formula is exact for every \(n\ge0\) (with \(c=0\)).

The leading amplitude is explicitly positive:
\[
 L=\frac{\ell_\rho (u_0,u_{-1},u_{-2},u_{-3},u_{-4})^T
 +\sum_{k=0}^\infty\rho^{-k-1}\varepsilon_k}{S_\rho}.
\]
If \(L_0\) denotes its first (initial-data) summand, then
\[
 0<L_0\le L\le L_0+\frac{\log(1+2b)}{S_\rho(\rho-1)}.
\]
Furthermore, with the initial history held fixed, its right derivative at \(b=0\) is strictly positive:
\[
 \boxed{\left.\frac{dL}{db}\right|_{b=0+}
 =\frac1{4S_\rho}\sum_{k=0}^\infty\rho^{-k-1}
 \prod_{j\in\{1,2,4\}}(1-r^{(0)}_{k-j})>0,}
\]
where \(r^{(0)}\) is the exactly computable orbit at \(b=0\).

## Assumptions and scope

The parameter satisfies \(b\ge0\). Every initial state belongs to \((0,\infty)\setminus\{1\}\), so that all logarithms are finite; the positive denominator makes all forward states positive. A history containing \(1\) is excluded from the logarithmic theorem: the Cayley product then propagates exact zeros, giving eventually stationary solutions. Complex eigenvalues are used only to resolve real logarithmic trajectories. The roots, amplitudes and expansion are defined for each fixed finite parameter and history. The error constant and \(\gamma\) may depend on them.

## Proof

**1. Exact nonlinear conjugacy.** Let \(x,y,z\) denote the three lagged inputs. Subtract the recurrence's denominator from its numerator: the difference is \((x-1)(y-1)(z-1)\). Their sum is \((x+1)(y+1)(z+1)+2b\). Consequently, the output Cayley coordinate equals
\[
 \frac{r_x r_y r_z}{1+\frac b4(1-r_x)(1-r_y)(1-r_z)}.
\]
For positive input states, each \(r\in(-1,1)\); hence the denominator is at least one, and every output Cayley coordinate is nonzero if all input coordinates are. Taking negative logarithms of absolute values yields the *exact* forced linear recurrence
\[
 u_{n+1}=u_{n-1}+u_{n-2}+u_{n-4}+\varepsilon_n,
 \quad 0\le\varepsilon_n\le\log(1+2b).
\]
For any admissible initial history all \(u_j>0\).

**2. Growth and forcing convergence.** Put \(U_n=(u_n,u_{n-1},u_{n-2},u_{n-3},u_{n-4})^T\). Then
\[
 U_{n+1}=TU_n+\varepsilon_ne_1,\qquad
 T=\begin{pmatrix}0&1&1&0&1\\1&0&0&0&0\\0&1&0&0&0\\0&0&1&0&0\\0&0&0&1&0\end{pmatrix}.
\]
Direct multiplication shows \(T^8\) has all entries strictly positive. Its characteristic polynomial is \(P\), so Perron–Frobenius theory gives a unique positive dominant root \(\rho>1\), strictly positive left and right eigenvectors and \(u_n\ge a\rho^n\) for sufficiently large \(n\), where \(a>0\) depends on the history. Because \(|r_n|=e^{-u_n}\), all Cayley coordinates vanish super-exponentially.

Write \(c=\log(1+b/4)\). Since \(r_j\to0\), the expression for \(\varepsilon_n\), with its smooth positive logarithm, implies
\[
 \varepsilon_n=c+d_n,\qquad
 |d_n|\le C e^{-a'\rho^{n-4}}
\]
for sufficiently large \(n\) and some \(a',C>0\). At \(b=0\), \(\varepsilon_n=d_n=c=0\) identically. The preceding inequalities also give global existence and attraction to the fixed point \((1,1,1,1,1)\), but neither fact is claimed as a new qualitative theorem.

**3. Spectral projectors.** Algebra gives
\[
 Tv_t=tv_t,\quad \ell_tT=t\ell_t,\quad
 v_t=(1,t^{-1},t^{-2},t^{-3},t^{-4})^T,\quad
 \ell_tv_t=S_t=3-t^{-2}+2t^{-5}.
\]
The polynomial \(P\) has five distinct roots (\(\gcd(P,P')=1\)), so \(S_t\ne0\) and the five spectral projectors are \(v_t\ell_t/S_t\). Its roots have the stated modulus split: this can be certified by Rouché's theorem in radius \(10^{-3}\) disks around \(1.42911\), \(-0.92456\pm0.64166i\), and \(0.21001\pm0.71300i\), using rational-center evaluations \(|P(q)|<10^{-3}\), \(|P'(q)|>4\), and the Taylor remainder \(<10^{-4}\) on each circle; these disks are disjoint and contain all five roots. (The bound \(|P'(q)|>4\) also holds at the final pair of centers.) The Perron root is the largest in modulus, and the two nonreal pairs straddle the unit circle as given.

The vector \(W_n=U_n+(c/2){\bf1}\) satisfies \(W_{n+1}=TW_n+d_ne_1\) because \(T{\bf1}={\bf1}+2e_1\). The spectral decomposition of its exact variation-of-constants formula is
\[
 u_n+\frac c2=\sum_{P(t)=0}\frac{t^n}{S_t}
 \left(\ell_t W+\sum_{k=0}^{n-1}t^{-k-1}d_k\right).
\]
The super-exponential bound on \(d_k\) proves absolute convergence of every series, including those with \(|t|<1\), and bounds all omitted tails by \(O(e^{-\gamma\rho^{n-4}})\) after decreasing \(\gamma>0\). This proves the full five-mode expansion. Grouping conjugate roots gives the stated secondary oscillatory term and the smaller stable-mode remainder.

**4. Positive leading amplitude and parameter response.** The Perron left eigenvector \(\ell_\rho\) has strictly positive entries. Apply it to the unshifted recurrence and sum the scalar forced equation to obtain the displayed positive formula and bound for \(L\); the upper bound uses \(\sum_{k\ge0}\rho^{-k-1}=1/(\rho-1)\). For fixed \(k\), each \(r_k^{(b)}\) depends continuously on \(b\ge0\). Moreover
\[
 0\le\frac{\varepsilon_k^{(b)}}b\le2\quad(b>0),
\]
so dominated convergence in the Perron series yields the displayed right derivative. Every summand of this derivative is positive since \(1-r_j^{(0)}>0\). This completes the proof.

## Verification

The companion polynomial, spectral eigenvectors, Cayley identity and positive eighth matrix power are exact symbolic checks. Distinct-root and modulus conditions admit the rational-center root isolation described in the proof; numerical root values merely display the isolated roots. A reproducible diagnostic script checks exact algebraic identities and several different positive histories while iterating in logarithmic coordinates to avoid floating-point underflow. Additional high-precision evaluation tests the five-mode formula against direct recurrences. Finite numerical tests are not used as proofs of an infinite limit.

## Relationship to prior work

Zhang and Shen (2024) explicitly study the identical five-lag rational recurrence for \(b\ge0\), establish global asymptotic stability and describe its sign semi-cycle structures. Importantly, the more general Xi–Sun (2006) rational family **already contains this exact recurrence** as the three-input case with lags \(1,2,4\), and proves global attraction as well as qualitative sign laws. Accordingly, neither the recurrence, global convergence, superattracting linearization, nor sign periodicity is asserted as new. Their inspected statements and proofs do not establish the complete quantitative five-mode logarithmic asymptotic, the explicit convergent coefficient sums or the nonzero parameter-sensitivity formula obtained here. General linear spectral theory supplies a proof tool, but without the exact nonlinear Cayley identity and super-exponential forcing estimate it does not by itself imply the conclusion.

## Limitations

No claim is made of new global stability, global existence, or sign-cycle classification. Initial histories with any coordinate exactly \(1\) are excluded because their logarithmic coordinates are undefined. This fixed-parameter asymptotic is not uniform in unbounded parameters or in initial histories approaching \(1\). Non-leading spectral amplitudes can vanish for special histories; the theorem does not assert nonzero oscillation for every trajectory. The coefficient series may require truncation bounds for high-precision implementation. Independent mathematical validation remains to be performed.

## References

- Q. Zhang and L. Shen, *Global asymptotic stability and trajectory structure rules of high-order nonlinear difference equation*, AIMS Mathematics 9 (2024), 28256–28272; first public date 29 September 2024, DOI: https://doi.org/10.3934/math.20241370. Full article: https://www.aimspress.com/aimspress-data/math/2024/10/PDF/math-09-10-1370.pdf.
- H. Xi and T. Sun, *Global behavior of a higher-order rational difference equation*, Advances in Difference Equations (2006), article 27637, DOI: https://doi.org/10.1155/ADE/2006/27637. Full article: https://link.springer.com/content/pdf/10.1155/ADE/2006/27637.pdf.
