# Sharp conjugate-zero frontier for odd-jet penalized Gaussian Fock kernels

## Finding
For each odd integer \(m\ge3\) and each \(\tau>0\), the first zeros of the singly penalized Gaussian Fock reproducing kernel form one nonreal conjugate pair. Their exact radius is determined by a uniquely solvable real phase equation and a strictly monotone scalar function. This gives an exact zero-free observation bidisk and a sharp comparison with the usual radial reverse-triangle estimate:
\[
K_{m,\tau}(z,w)=e^{z\overline w}-q(z\overline w)^m,\qquad q=\frac{\tau}{1+\tau m!}.
\]
For every \(r>0\), define \(\theta_m(r)\) as the unique solution in \(((m-1)\pi/m,\pi)\) of
\[
m\theta-r\sin\theta=(m-1)\pi.
\]
Then \(C_m(r)=r^{-m}\exp(r\cos\theta_m(r))\) decreases strictly from infinity to zero; let \(r_*\) be the unique positive solution \(C_m(r_*)=q\). The only scalar zeros at the minimal modulus \(r_*\) are \(r_*e^{\pm i\theta_m(r_*)}\), both simple. Hence \(K_{m,\tau}\) has no zero with \(|z|,|w|<R\) exactly when \(R^2\le r_*\). If \(\rho\) is defined by \(e^{-\rho}=q\rho^m\), then \(\rho<r_*\), and, putting \(L=\log(1/q)\),
\[
r_*-\rho=\frac{\pi^2}{2L}+O_m\!\left(\frac{\log L}{L^2}\right)\quad(q\downarrow0).
\]

## Assumptions and scope
The Fock space consists of entire functions \(f(z)=\sum_{n\ge0}a_n z^n\) with norm \(\|f\|_{m,\tau}^2=\sum_{n\ge0}n!|a_n|^2+\tau|f^{(m)}(0)|^2\), where \(m=3,5,7,\ldots\), \(0<\tau<\infty\). The angle is taken in \((0,\pi)\). A zero-free bidisk refers to all pairs with both moduli strictly less than \(R\), not to a positive lower bound on the entire-plane kernel. The limiting \(\tau=0\) kernel is \(e^{z\overline w}\), zero-free everywhere.

## Proof
The monomials are orthogonal. Their norms are \(n!\) except the \(m\)-th monomial, which has norm squared \(m!(1+\tau m!)\). Summing inverse squared norms proves the displayed kernel with the stated coefficient \(q\).

Put \(t=s e^{i\theta}\) with \(s>0\), \(0\le\theta\le\pi\). Zeros of \(e^t-q t^m\) satisfy both
\[
q=s^{-m}e^{s\cos\theta},\qquad m\theta-s\sin\theta=2\pi j,\quad j\in\mathbb Z.
\]
For fixed \(s\), set \(F_s(\theta)=m\theta-s\sin\theta\). It is strictly convex on \((0,\pi)\), with \(F_s(0)=0\), \(F_s(\pi)=m\pi\). Because \(m\) is odd, the largest possible nonnegative integral phase level is \((m-1)\pi>0\). The corresponding equation has exactly one solution \(\theta_m(s)\in((m-1)\pi/m,\pi)\). All solutions of any allowed phase level, including negative levels, satisfy \(\theta\le\theta_m(s)\): above \(\theta_m(s)\), the convex function \(F_s\) is strictly increasing and greater than \((m-1)\pi\). Since cosine decreases on \([0,\pi]\), every zero of modulus \(s\) must satisfy
\[
q\ge s^{-m}e^{s\cos\theta_m(s)}=C_m(s),
\]
with equality only at the conjugate pair of angles \(\pm\theta_m(s)\).

Implicit differentiation gives \(\theta_m'(s)=\sin\theta_m(s)/(m-s\cos\theta_m(s))>0\), and
\[
\frac{d}{ds}\log C_m(s)=\cos\theta_m(s)-\frac m s-\frac{s\sin^2\theta_m(s)}{m-s\cos\theta_m(s)}<0.
\]
At zero \(\theta_m(s)\to(m-1)\pi/m\), and at infinity \(\theta_m(s)\to\pi\), so \(C_m\) decreases continuously from infinity to zero. Let \(C_m(r_*)=q\). No zero can have \(s<r_*\), while the two conjugate values at \(s=r_*\) are zeros. Any other phase level at the same modulus has \(\theta<\theta_m(r_*)\), giving a strictly larger coefficient than \(q\), hence no additional minimal-modulus zeros. A repeated zero would solve \(e^t=q t^m\) and \(e^t=qm t^{m-1}\), forcing \(t=m>0\), so both nonreal minimal zeros are simple.

Any complex scalar product of modulus smaller than \(R^2\) can be represented as \(z\overline w\) with \(|z|,|w|<R\); at equality the minimal zeros are attained only on the closed boundary of the bidisk. This yields the exact open-bidisk threshold.

Let \(\rho>0\) solve \(e^{-\rho}=q\rho^m\). Since \(\theta_m(s)<\pi\), \(C_m(s)>s^{-m}e^{-s}\). The latter is strictly decreasing, which proves \(r_*>\rho\). Set \(L=\log(1/q)\). The phase equation at large \(r\) gives \(\pi-\theta_m(r)=\pi/(r+m)+O_m(r^{-3})\). Therefore
\[
\log C_m(r)=-r-m\log r+\frac{\pi^2}{2r}+O_m(r^{-2}).
\]
The defining equations imply \(\rho=L-m\log L+O_m(\log L/L)\) and \(r_*=\rho+\pi^2/(2L)+O_m(\log L/L^2)\), as claimed.

## Verification
The companion `verify.py` recomputes \(r_*\), the phase and the nearest Lambert-W roots independently for multiple odd orders and finite penalties; it asserts the two descriptions agree and checks the defining complex equation. These tests are finite diagnostics. The theorem for all odd orders and every positive penalty follows from the convexity and monotonicity argument above.

## Relationship to prior work
The Gaussian Fock reproducing kernel and monomial norm formulas are classical. Escudero–Haimi–Romero (2021) study multiple sampling with derivatives in weighted Fock spaces, motivating precise zero control in jet-related reproducing kernels; their sampling-density results do not imply this nearest-zero classification. Cho–Choe–Koo (2013) study globally weighted Fock-Sobolev spaces rather than one isolated Taylor-jet penalty. The published even-jet minimum-modulus result at `https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-minimum-modulus-profile-for-even-jet-fock-kernels--5341e28cb9dd` uses attainment on the negative real axis, and expressly excludes odd orders. The present conjugate-pair phase construction addresses that different parity; no novelty is claimed for Lambert-W inversion itself.

## Limitations
The result concerns one odd Taylor-jet penalty at the origin, not arbitrary coupled jets, other weighted spaces, or Gram-matrix conditioning. The exact minimum-modulus profile beyond the first zero-free radius is not classified. No claim of independent review or global historical priority is made.

## References
1. L. A. Escudero, A. Haimi, J. L. Romero, *Multiple Sampling and Interpolation in Weighted Fock Spaces of Entire Functions*, Complex Analysis and Operator Theory 15 (2021), article 35, first publicly available 2021-02-16, https://pmc.ncbi.nlm.nih.gov/articles/PMC7886767/ .
2. H. R. Cho, B. R. Choe, H. Koo, *Fock-Sobolev spaces of fractional order*, arXiv:1307.2670 (2013), https://arxiv.org/abs/1307.2670 .
3. *Sharp minimum-modulus profile for even-jet Fock kernels*, published record 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-sharp-minimum-modulus-profile-for-even-jet-fock-kernels--5341e28cb9dd .
