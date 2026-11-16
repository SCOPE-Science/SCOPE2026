# Sharp one-latitude lower frame bound for quartic harmonics on the three-sphere

## Finding
Let \(\mathcal H_4(S^3)\) be the 25-dimensional complex space of exact-degree-four spherical harmonics on the unit three-sphere, endowed with probability-normalized surface measure. For \(-1<t<1\) let
\[
(R_t f)(y)=f(\sqrt{1-t^2}\,y,t),\qquad y\in S^2,
\]
with probability-normalized surface measure on \(S^2\). Put \(u=t^2\) and \(T_t=R_t^*R_t\). The complete spectrum of \(T_t\), with multiplicities, is
\[
\begin{array}{c|c|c}
m&\lambda_m(u)&\text{multiplicity}\\\hline
0&(16u^2-12u+1)^2&1\\
1&\frac83 u(1-u)(8u-3)^2&3\\
2&\frac87(1-u)^2(8u-1)^2&5\\
3&\frac{128}{7}u(1-u)^3&7\\
4&\frac{128}{63}(1-u)^4&9
\end{array}
\]
where equal values from distinct sectors must have their multiplicities added.

There is precisely one squared latitude \(u\in[0,1]\) maximizing the least eigenvalue. It is \(u=\tau\), the unique real zero in \((6/25,1/4)\) of
\[
p(u)=640u^3-576u^2+114u-3.
\]
Consequently
\[
\max_{-1<t<1}\inf_{\|f\|_{L^2(S^3)}=1}\|R_tf\|_{L^2(S^2)}^2
=\lambda_1(\tau)=\lambda_2(\tau)
=0.5634502741800779818700\ldots,
\]
attained exactly at \(t=\pm\sqrt\tau\), with \(\tau=0.2405728168548298138694\ldots\). At each optimum, the least-eigenvalue eigenspace has complex dimension eight (the \(m=1\) and \(m=2\) sectors), and restriction is injective.

## Assumptions and scope
The spaces and restrictions are over \(\mathbb C\); the latitude measure and ambient measures are probability measures, not unnormalized areas. No radial derivative data are observed. The optimization is E-optimality (maximization of the *lower squared singular value*), not minimization of the singular-value condition number. At \(t=\pm1\), interpreted by continuous extension, some sectors vanish; at \(t=0\), the odd transverse orders vanish. The theorem makes no claim for bands involving multiple harmonic degrees, other ambient dimensions, or finitely sampled latitude spheres.

## Proof
Use spherical branching for \(S^3\) along the last coordinate. The direct sum \(\mathcal H_4(S^3)=\bigoplus_{m=0}^{4}\mathcal H_m(S^2)\) is orthogonal, with \(\dim\mathcal H_m(S^2)=2m+1\). If \(Y_{m,j}\) is an orthonormal spherical harmonic of degree \(m\) on \(S^2\), the normalized degree-four harmonic on \(S^3\) in that sector is
\[
\Phi_{m,j}(s,y)=N_m^{-1/2}(1-s^2)^{m/2}C_{4-m}^{(m+1)}(s)Y_{m,j}(y),
\]
where \(s\in(-1,1)\), \(x=(\sqrt{1-s^2}y,s)\), and \(C_k^{(a)}\) denotes the classical Gegenbauer polynomial. The scalar coordinate \(s\) under uniform spherical measure has density \(2\sqrt{1-s^2}/\pi\). Direct integration gives
\[
(N_0,N_1,N_2,N_3,N_4)=\left(1,6,\frac{63}{8},\frac72,\frac{63}{128}\right),
\]
and the five Gegenbauer factors are respectively
\[
16s^4-12s^2+1,\quad32s^3-12s,\quad24s^2-3,\quad8s,\quad1.
\]
The restrictions of these sectors remain mutually orthogonal on the latitude. The ratio of the squared restricted factor to \(N_m\) therefore gives the five eigenvalues in the table. Their trace identity is \(\sum_{m=0}^4(2m+1)\lambda_m(u)=25\), providing an independent normalization check.

For the global optimum, first note
\[
\lambda_1(u)-\lambda_2(u)=-\frac8{21}(u-1)p(u).
\]
The cubic satisfies \(p(6/25)=93/3125>0\), \(p(1/4)=-1/2<0\), and its derivative is strictly negative on \([6/25,1/4]\), by \(p'(u)=1920u^2-1152u+114\le120-1152(6/25)+114<0\). Thus the specified \(\tau\) is unique. On \([1/8,\tau]\), the branch \(\lambda_2\) is strictly increasing, since its derivative is \(16(1-u)(8u-1)(9-16u)/7\). On \([\tau,7/25]\), the branch \(\lambda_1\) is strictly decreasing, since
\[
\lambda_1'(u)=-\frac83(8u-3)(32u^2-30u+3)<0
\]
throughout \([6/25,7/25]\).

For the remaining intervals, obtain strict upper bounds without numerical optimization:
\[
\begin{array}{rcl}
0\le u\le1/32&:&\min_m\lambda_m(u)\le\lambda_3(u)\le29791/57344<11/20,\\
1/32\le u\le1/8&:&\min_m\lambda_m(u)\le\lambda_0(u)\le1681/4096<11/20,\\
7/25\le u\le1&:&\min_m\lambda_m(u)\le\lambda_4(u)\le1492992/2734375<11/20.
\end{array}
\]
The first inequality follows from monotonicity of \(u(1-u)^3\) to \(u=1/4\); the second follows because \(16u^2-12u+1\) decreases between the endpoints, where the larger absolute value is \(41/64\); the third follows from monotonicity of \((1-u)^4\). Meanwhile \(\lambda_2(6/25)=1527752/2734375>11/20\), so the common value \(H=\lambda_1(\tau)=\lambda_2(\tau)\) exceeds \(11/20\). These five subinterval bounds prove that the least eigenvalue is strictly below \(H\) except possibly at \(u=\tau\).

Finally, at \(\tau\in[6/25,1/4]\), the three inactive branches obey
\[
\lambda_0(\tau)\ge(599/625)^2,\qquad
\lambda_3(\tau)\ge324/175,\qquad
\lambda_4(\tau)\ge9/14.
\]
Each lower bound exceeds \(\lambda_1(6/25)=221616/390625>H\), because \(\lambda_1\) is strictly decreasing on \([6/25,1/4]\). Hence the least eigenvalue at \(\tau\) is exactly \(H\), and precisely the eight modes from sectors \(m=1,2\) attain it. Strict inequalities elsewhere show uniqueness in squared latitude, proving the stated two signed optima.

## Verification
Run `python verify_quartic_latitude.py` with Python 3, SymPy and NumPy installed. It reconstructs the Gegenbauer formulas from beta moments, checks the trace and rational interval certificates symbolically, independently constructs all 25 quartic harmonics as the kernel of the polynomial Laplacian, forms their spherical and latitude Gram matrices from exact rational monomial moments, and checks the entire generalized spectrum at six rational latitudes. It also prints the high-precision algebraic optimum. All tests passed; the continuous global assertion depends on the proof inequalities above, not on the six test latitudes.

## Relationship to prior work
General harmonic-expansion reconstruction by randomized point sampling on the full sphere is treated in Zandieh, Han and Avron (first posted February 25, 2022). Optimal-dimensionality multi-ring sampling for spin-weighted harmonics on the two-sphere is treated in Elahi, Khalid, Kennedy and McEwen (first posted September 5, 2018). Neither addresses the E-optimal continuous restriction of the *pure quartic* space on \(S^3\) to one embedded \(S^2\). Previously published exact-degree latitude calculations for quadratic and cubic harmonics, and nine-point quartic sampling on a latitude circle in \(S^2\), concern different harmonic degrees, ambient domains, or observation operators; they do not give the present five-branch spectrum and sharp cubic root optimum. The separated Gegenbauer basis itself is standard, and no priority is claimed for that basis.

## Limitations
Historical novelty is conditional on the searched literature; an unindexed equivalent sharp optimization may exist. The normalized lower bound refers to exact-degree-four harmonics only. It does not quantify reconstruction after finitely sampling the observation two-sphere or after adding other harmonic degrees. The numerical checks verify finite algebraic instances, whereas the proof establishes the continuous statement.

## References
- A. Zandieh, I. Han, H. Avron, *Near Optimal Reconstruction of Spherical Harmonic Expansions*, arXiv:2202.12995 (first public version February 25, 2022), https://arxiv.org/abs/2202.12995.
- U. Elahi, Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling for Spin-s Functions on the Sphere*, arXiv:1809.01321 (first public version September 5, 2018), https://arxiv.org/abs/1809.01321.
- NIST Digital Library of Mathematical Functions, Chapter 18, *Orthogonal Polynomials* (classical Gegenbauer-polynomial identities), https://dlmf.nist.gov/18.
