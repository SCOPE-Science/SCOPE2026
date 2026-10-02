# Sharp exponential constant for the AESZ 28 Apéry limit

## Statement

Let \(A_n,C_n\) be the two solutions of
\[
4n^2(16n^2-1)u_{n-1}
-(65n^4+130n^3+105n^2+40n+6)u_n
+(n+1)^4u_{n+1}=0
\]
with
\[
(A_0,A_1)=(1,6),\qquad (C_0,C_1)=(0,1).
\]
Bachmann proved the Apéry limit
\[
\frac{C_n}{A_n}\longrightarrow \frac{\zeta(3)}7.
\]
The convergence admits the sharp equivalent
\[
\boxed{
\frac{\zeta(3)}7-\frac{C_n}{A_n}
\sim \frac{\sqrt2\,\pi^3}{84}\,64^{-n}.
}
\]
Equivalently,
\[
\boxed{
64^n\left(\frac{\zeta(3)}7-\frac{C_n}{A_n}\right)
\longrightarrow \frac{\sqrt2\,\pi^3}{84}.
}
\]
The dominant solution itself has the explicit asymptotic
\[
\boxed{
A_n\sim \frac{2\sqrt6}{3\pi^2}\,\frac{64^n}{n^2}.
}
\]

Thus the characteristic-root prediction that the approximation is exponentially fast can be sharpened, for this recurrence, to an exact leading constant.

## Context

The recurrence is AESZ no. 28. Bachmann's 2026 paper records the integral binomial formula
\[
A_n=\sum_{i,j=0}^{n}
\binom ni^2\binom nj^2\binom{i+j}{n}^2,
\]
the exact Casoratian
\[
W_n:=A_nC_{n+1}-A_{n+1}C_n
=\frac{(4n+1)\binom{4n}{2n}\binom{2n}{n}}{(n+1)^4},
\]
and an independent proof that \(C_n/A_n\to\zeta(3)/7\). The result here combines those identities with a two-dimensional saddle analysis of the binomial sum.

## Proof

### 1. Asymptotic of \(A_n\)

Write \(i=nx\), \(j=ny\), \(s=x+y\), and
\[
H(t)=-t\log t-(1-t)\log(1-t).
\]
On the interior domain
\[
\mathcal D=\{(x,y):0<x<1,\ 0<y<1,\ x+y>1\},
\]
the exponential phase of the summand is
\[
F(x,y)=2H(x)+2H(y)+2sH(1/s).
\]
The Hessian is negative definite throughout \(\mathcal D\): after dividing by \(2\), its diagonal entries are
\[
-\frac1{x(1-x)}-\frac1{s(s-1)},\qquad
-\frac1{y(1-y)}-\frac1{s(s-1)},
\]
and the off-diagonal entry is
\[
-\frac1{s(s-1)}.
\]
Hence \(F\) is strictly concave. Its unique critical point is
\[
(x_0,y_0)=\left(\frac34,\frac34\right),
\]
where
\[
F(x_0,y_0)=\log 64
\]
and
\[
\operatorname{Hess}F(x_0,y_0)=
\begin{pmatrix}
-40/3&-8/3\\
-8/3&-40/3
\end{pmatrix},
\qquad
\det(-\operatorname{Hess}F)=\frac{512}{3}.
\]

Uniform Stirling expansion in a fixed neighborhood of the saddle gives
\[
\binom ni^2\binom nj^2\binom{i+j}{n}^2
\sim n^{-3}q(x,y)e^{nF(x,y)},
\]
where
\[
q(x,y)=
\frac{x+y}{(2\pi)^3x(1-x)y(1-y)(x+y-1)}.
\]
At the saddle,
\[
q(x_0,y_0)=\frac{32}{3\pi^3}.
\]
Outside any fixed neighborhood of the unique maximizer, strict concavity gives an exponentially smaller contribution. Applying the standard two-dimensional lattice Laplace method therefore yields
\[
A_n\sim
n^2\cdot n^{-3}\cdot \frac{2\pi}{n}
\frac{q(x_0,y_0)}{\sqrt{512/3}}\,64^n.
\]
The constant simplifies to
\[
\frac{2\pi\,(32/(3\pi^3))}{\sqrt{512/3}}
=\frac{2\sqrt6}{3\pi^2},
\]
so
\[
A_n\sim \frac{2\sqrt6}{3\pi^2}\frac{64^n}{n^2}.
\]

### 2. Casoratian asymptotic

From the exact identity above and Stirling's formula,
\[
\binom{4n}{2n}\sim \frac{16^n}{\sqrt{2\pi n}},
\qquad
\binom{2n}{n}\sim \frac{4^n}{\sqrt{\pi n}}.
\]
Hence
\[
W_n\sim \frac{2\sqrt2}{\pi}\frac{64^n}{n^4}.
\]
Put
\[
r_n=\frac{C_n}{A_n}.
\]
Then exactly
\[
r_{n+1}-r_n=\frac{W_n}{A_nA_{n+1}}.
\]
Using the asymptotic for \(A_n\), with
\[
K=\frac{2\sqrt6}{3\pi^2},
\]
we obtain
\[
r_{n+1}-r_n
\sim
\frac{2\sqrt2/\pi}{64K^2}\,64^{-n}
=\frac{3\sqrt2\,\pi^3}{256}\,64^{-n}.
\]

Bachmann proved that \(r_n\uparrow \zeta(3)/7\). Therefore
\[
\frac{\zeta(3)}7-r_n
=\sum_{j=n}^{\infty}(r_{j+1}-r_j).
\]
The positive summands have consecutive ratio tending to \(1/64\), so the tail is asymptotic to \(64/63\) times its first term. Consequently
\[
\frac{\zeta(3)}7-r_n
\sim
\frac{64}{63}\cdot
\frac{3\sqrt2\,\pi^3}{256}\,64^{-n}
=\frac{\sqrt2\,\pi^3}{84}\,64^{-n}.
\]
This proves the claim.

## Numerical verification

The accompanying standalone script regenerates \(A_n\) and \(C_n\) exactly from the recurrence, checks the AESZ binomial formula for \(0\le n\le12\), checks the exact Casoratian identity through \(n=99\), and compares the scaled quantities with the two predicted constants. For example,
\[
\frac{A_{100}\,100^2}{64^{100}}
=0.16446027992205028485\ldots,
\]
against
\[
\frac{2\sqrt6}{3\pi^2}=0.16545680003903806664\ldots,
\]
and
\[
64^{100}\left(\frac{\zeta(3)}7-\frac{C_{100}}{A_{100}}\right)
=0.51824410959648942835\ldots,
\]
against
\[
\frac{\sqrt2\pi^3}{84}=0.52201782142824562178\ldots.
\]
The convergence is monotone at the quotient level but no monotonicity claim is made for these scaled diagnostic sequences.

## Limitations

The result concerns this specific AESZ no. 28 recurrence and does not claim an analogous sharp constant for arbitrary Apéry limits, the root-of-unity \(q\)-recurrence, or the odd-weight extensions in Bachmann's paper. It does not improve any irrationality measure for \(\zeta(3)\). Originality is asserted only to the best of our knowledge. A closely relevant work of N. Sato and K. Tasaka, *Multivariate Apéry-like numbers, interpolations, and modular L-values*, is cited by Bachmann as in preparation and was not available for full inspection; because it supplies another proof of the underlying limit, it is the most plausible residual originality risk.

## References

1. H. Bachmann, *A q-recurrence for a finite Apéry limit*, arXiv:2609.18271 (2026). https://arxiv.org/abs/2609.18271
2. G. Almkvist, C. van Enckevort, D. van Straten, W. Zudilin, *Tables of Calabi-Yau equations*, arXiv:math/0507430. https://arxiv.org/abs/math/0507430
3. G. Almkvist, D. van Straten, W. Zudilin, *Apéry limits of differential equations of order 4 and 5*, Fields Institute Communications 54 (2008), 105–123. https://doi.org/10.1090/fic/054/05
4. M. Chamberland, A. Straub, *Apéry Limits: Experiments and Proofs*, Amer. Math. Monthly 128 (2021), 811–824. https://arxiv.org/abs/2011.03400
5. E. Panzer, K. Yeats, *Feynman symmetries of the Martin and c2 invariants of regular graphs*, Combinatorial Theory 5 (2025), no. 1, Paper 10. https://arxiv.org/abs/2304.05299
