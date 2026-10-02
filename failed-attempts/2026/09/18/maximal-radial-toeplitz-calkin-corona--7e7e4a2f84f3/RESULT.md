# A logarithmic Fock weight has the full diagonal Calkin corona

## Statement

Fix \(n\ge 1\) and the radial weight
\[
h(r)=
\begin{cases}
0,&0\le r\le 1,\\[2mm]
\frac12(\log r)^{3/2},&r>1.
\end{cases}
\]
Let \(\mathcal A_h(\mathbb C^n)\) be the corresponding weighted Fock space and let
\[
\mathcal T_{\rm rad}(h)
=C^*(T_\varphi:\varphi\in L^\infty(\mathbb C^n)\text{ is radial}).
\]
Write
\[
\mathcal A_h(\mathbb C^n)=\bigoplus_{m\ge0}P^m(\mathbb C^n),
\qquad
D_c=\bigoplus_{m\ge0}c_m I_{P^m(\mathbb C^n)}
\quad(c\in\ell^\infty).
\]

Then for every \(c=(c_m)\in\ell^\infty\) there is a bounded radial symbol
\(\varphi_c\), with \(\|\varphi_c\|_\infty\le\|c\|_\infty\), such that
\[
T_{\varphi_c}-D_c\in\mathcal K(\mathcal A_h(\mathbb C^n)).
\]
Consequently, if \(q:B(\mathcal A_h)\to B(\mathcal A_h)/\mathcal K(\mathcal A_h)\)
is the Calkin quotient, then
\[
\boxed{q(\mathcal T_{\rm rad}(h))
      =q(\operatorname{End}_{U(n)}(\mathcal A_h))
      \cong \ell^\infty/c_0
      \cong C(\beta\mathbb N_0\setminus\mathbb N_0).}
\]
Equivalently,
\[
\mathcal T_{\rm rad}(h)/
(\mathcal T_{\rm rad}(h)\cap\mathcal K)
\cong \ell^\infty/c_0.
\]

Thus the logarithmic weight turns the radial Toeplitz algebra into the full
\(U(n)\)-intertwiner algebra modulo compact operators.

## Construction and proof

Bdarneh's spectral formula for a bounded \(U(n)\)-invariant symbol gives
\[
T_\varphi|_{P^m(\mathbb C^n)}=\lambda_{\varphi,m}I,
\qquad
\lambda_{\varphi,m}
=
\frac{\int_0^\infty a_\varphi(r)r^{2m+2n-1}e^{-2h(r)}\,dr}
{\int_0^\infty r^{2m+2n-1}e^{-2h(r)}\,dr}.
\]
Set
\[
a_m=2m+2n,\qquad
R_{-1}=0,\qquad
R_m=\exp\!\left[\frac49(a_m+1)^2\right],
\]
and, for \(c\in\ell^\infty\), define
\[
\varphi_c(z)=c_m
\quad\text{when}\quad
R_{m-1}\le |z|<R_m.
\]
This is bounded and radial.

Put
\[
A_m=\int_0^\infty r^{a_m-1}e^{-2h(r)}\,dr,\qquad
B_m=\int_0^{R_{m-1}}r^{a_m-1}e^{-2h(r)}\,dr,\qquad
C_m=\int_{R_m}^\infty r^{a_m-1}e^{-2h(r)}\,dr.
\]
On \(r>1\), after \(u=\log r\), the exponent is
\[
F_m(u)=a_mu-u^{3/2},
\]
whose maximum occurs at
\[
u_m=\frac49a_m^2.
\]
The interval \((\log R_{m-1},\log R_m)\) has endpoints
\[
\frac49(a_m-1)^2,\qquad \frac49(a_m+1)^2,
\]
so it contains \(u_m\). The concentration estimates used by Bdarneh for the
alternating sequence extend with \(2m+2\) replaced by \(a_m\):
\[
\frac{B_m}{A_m}\longrightarrow0,
\qquad
\frac{C_m}{A_m}\longrightarrow0.
\]
For completeness, the exponent drops at the two boundaries are exactly
\[
F_m\!\left(\frac49(a_m-1)^2\right)-F_m(u_m)
=-\frac4{27}(3a_m-2),
\]
\[
F_m\!\left(\frac49(a_m+1)^2\right)-F_m(u_m)
=-\frac4{27}(3a_m+2),
\]
which give exponential decay of both normalized tails, up to a polynomial
factor on the lower side.

Because \(\varphi_c=c_m\) throughout the \(m\)-th central annulus,
\[
|\lambda_{\varphi_c,m}-c_m|
\le
2\|c\|_\infty
\left(\frac{B_m}{A_m}+\frac{C_m}{A_m}\right)
\longrightarrow0.
\]
Hence the eigenvalue sequence of \(T_{\varphi_c}\) differs from \(c\) by an
element of \(c_0\).

Each \(P^m(\mathbb C^n)\) is finite dimensional. Therefore
\[
D_d=\bigoplus_m d_m I_{P^m}
\quad\text{is compact iff}\quad d_m\to0.
\]
It follows that \(T_{\varphi_c}-D_c\) is compact. Bdarneh also identifies
\(\operatorname{End}_{U(n)}(\mathcal A_h)\) with \(\ell^\infty\) through the
same homogeneous decomposition, so its compact ideal is exactly \(c_0\).
Every class in \(\ell^\infty/c_0\) is therefore represented by a radial
Toeplitz operator, proving the claimed Calkin equality.

## Consequences

1. For every subset \(S\subseteq\mathbb N_0\), choosing
   \(c_m=\mathbf1_S(m)\) produces a radial Toeplitz operator whose Calkin class
   is the projection \([\mathbf1_S]\). It is nontrivial exactly when both
   \(S\) and its complement are infinite.

2. For every nonempty compact set \(K\subset\mathbb C\), choose a bounded
   sequence \(c\) whose cluster set is \(K\). Then
   \[
   \sigma_{\rm ess}(T_{\varphi_c})=K.
   \]
   If \(K\subset\mathbb R\), the sequence and symbol may be chosen real, giving
   a self-adjoint example.

3. This sharply contrasts with the classical Gaussian Fock weight. There the
   radial Toeplitz algebra is \(C_{b,u}(\mathbb N_0,\rho)\), where
   \(\rho(j,k)=|\sqrt j-\sqrt k|\). Its quotient by \(c_0\) has only the two
   trivial projections. Indeed, if \(a\in C_{b,u}\) represents a projection
   modulo \(c_0\), then after taking the real part,
   \(a_m^2-a_m\to0\), so \(\operatorname{dist}(a_m,\{0,1\})\to0\).
   Uniform continuity and \(\rho(m,m+1)\to0\) imply
   \(a_{m+1}-a_m\to0\); hence the sequence cannot switch infinitely often
   between neighborhoods of \(0\) and \(1\). It therefore converges to one of
   them modulo \(c_0\).

The logarithmic weight consequently changes the radial corona from a
projectionless square-root-uniform quotient to the full Stone--Cech remainder
algebra.

## Relation to prior literature

Bdarneh (2026) proved the general radial eigenvalue formula above and, for
\(n=1\), used the same logarithmic weight with annuli centered at the Laplace
peaks to construct one symbol satisfying
\(\lambda_{\varphi,m}-(-1)^m\to0\). The stated conclusion there is that the
classical square-root-metric description fails for this weight. The present
result replaces the single alternating sequence by an arbitrary bounded
sequence, works in every complex dimension, and identifies the complete
Calkin image.

For the classical Gaussian Fock space, Esmeral--Maximenko (2016) proved that
the radial Toeplitz algebra is the algebra of bounded sequences uniformly
continuous for the square-root metric; Dewage--Olafsson (2022) extended this
description to quasi-radial symbols. These results provide the comparison
above, but do not imply the logarithmic-weight Calkin saturation.

Originality is asserted only to the best of our knowledge. Searches for
radial weighted-Fock Toeplitz Calkin algebras, \(\ell^\infty/c_0\) quotients,
Stone--Cech coronas, and arbitrary bounded eigenvalue interpolation did not
locate a prior statement of this theorem.

## Limitations

The theorem concerns the specific logarithmic weight above and bounded radial
symbols. It identifies the algebra only modulo compact operators; it does not
assert that the radial Toeplitz algebra itself equals the full
\(U(n)\)-intertwiner algebra in operator norm. No analogous assertion is made
for general radial weights or for nonradial Toeplitz algebras.

## References

- K. Bdarneh, *Toeplitz C*-algebras on Radially Weighted Fock Spaces:
  Commutativity and Spectral Representation*, arXiv:2609.20652v1 (2026).
  https://arxiv.org/abs/2609.20652
- K. Esmeral and E. A. Maximenko, *Radial Toeplitz Operators on the Fock Space
  and Square-Root-Slowly Oscillating Sequences*, Complex Analysis and Operator
  Theory 10 (2016), 1655--1677.
  https://doi.org/10.1007/s11785-016-0557-0
- V. Dewage and G. Olafsson, *Toeplitz Operators on the Fock Space with
  Quasi-Radial Symbols*, Complex Analysis and Operator Theory 16 (2022), 61.
  https://doi.org/10.1007/s11785-022-01208-9
