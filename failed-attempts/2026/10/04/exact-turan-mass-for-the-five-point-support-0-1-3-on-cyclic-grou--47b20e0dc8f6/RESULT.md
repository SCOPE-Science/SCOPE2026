# Exact Turan mass for the five-point support {0, ±1, ±3} on cyclic groups
## Finding
For every integer \(N\ge 7\), let \(G=\mathbb Z_N\) and \(\Omega_N=\{0,\pm1,\pm3\}\). Define
\[
\tau_N=\sup\left\{\sum_{x\in G}f(x): f(0)=1,\ f\text{ is positive definite on }G,\ \operatorname{supp}f\subseteq\Omega_N\right\}.
\]
Then the exact value is
\[
\tau_N=
\begin{cases}
2,&N\text{ even},\\
1+\sec(3\pi/N),&N\text{ odd and }3\mid N,\\
1+\dfrac{A+2C-D}{AD+C^2},&N\text{ odd and }3\nmid N,
\end{cases}
\]
where in the last case \(\varepsilon=1\) for \(N\equiv1\pmod 6\), \(\varepsilon=-1\) for \(N\equiv-1\pmod 6\), \(A=\cos(\pi/3-\varepsilon\pi/(3N))\), \(C=\cos(\pi/N)\), and \(D=\cos(3\pi/N)\). In the last case the extremal coefficients are \(f(\pm1)=(C-D)/(2(AD+C^2))\) and \(f(\pm3)=(A+C)/(2(AD+C^2))\).

The three regimes are arithmetically distinct. Even grids contain the antipodal character and force the continuous value \(2\). Odd grids miss that contact. If \(3\mid N\), the third harmonic alone is extremal and gives \(1+\sec(3\pi/N)\). For \(N\equiv\pm1\pmod 6\), the optimum uses both allowed nonzero frequencies and is controlled by two adjacent grid contacts around one sixth of the circle together with the last grid point before \(\pi\).

## Assumptions and scope
The group is \(G=\mathbb Z_N\) with counting measure, and \(N\ge7\) so that the five elements of \(\Omega_N=\{0,\pm1,\pm3}\) are distinct. Positive definiteness is in the standard finite-abelian sense: the discrete Fourier transform is nonnegative at every character. The normalization is \(f(0)=1\).

Taking the real part preserves positive definiteness, support, \(f(0)\), and the total mass. Hence an extremizer may be taken real and even. Write
\[
a=f(1)=f(-1),\qquad b=f(3)=f(-3).
\]
Then positive definiteness is equivalent to
\[
P_k=1+2a\cos(2\pi k/N)+2b\cos(6\pi k/N)\ge0
\]
for every \(k\in\mathbb Z_N\), while the objective is \(\tau_N=1+2a+2b\).

## Proof
If \(N\) is even, the constraint at \(k=N/2\) is \(1-2a-2b\ge0\), so \(\tau_N\le2\). Equality is attained by \(a=0\) and \(b=1/2\), because \(1+\cos(6\pi k/N)\ge0\) for all \(k\).

Now suppose that \(N\) is odd and \(3\mid N\). Put
\[
C_1=\cos(\pi/N),\qquad C_3=\cos(3\pi/N),\qquad A_0=\cos(\pi/3-\pi/N).
\]
At \(k=(N-3)/6\) and \(k=(N-1)/2\), respectively, feasibility gives
\[
1+2A_0a-2C_3b\ge0,\qquad 1-2C_1a-2C_3b\ge0.
\]
Multiply these inequalities by the positive numbers \(C_1-C_3\) and \(A_0+C_3\). The coefficients of \(a\) cancel, yielding \(a+b\le1/(2C_3)\). Equality is attained by
\[
a=0,\qquad b=\frac1{2C_3},
\]
because the sampled third harmonic has minimum \(-C_3\). Thus \(\tau_N=1+\sec(3\pi/N)\).

Finally suppose that \(N\) is odd and \(3\nmid N\). Let \(\varepsilon=1\) when \(N\equiv1\pmod6\) and \(\varepsilon=-1\) when \(N\equiv-1\pmod6\), and set
\[
A=\cos\!\left(\frac\pi3-\frac{\varepsilon\pi}{3N}\right),\quad
C=\cos(\pi/N),\quad D=\cos(3\pi/N).
\]
For \(q=(N-\varepsilon)/6\) and \(h=(N-1)/2\), the two constraints are
\[
-Aa+Cb\le\frac12,\qquad Ca+Db\le\frac12.
\]
The positive multipliers
\[
\mu_1=\frac{C-D}{AD+C^2},\qquad
\mu_2=\frac{A+C}{AD+C^2}
\]
satisfy
\[
(1,1)=\mu_1(-A,C)+\mu_2(C,D).
\]
Therefore
\[
a+b\le\frac{A+2C-D}{2(AD+C^2)}.
\]
Equality in the two active constraints gives
\[
a_* = \frac{C-D}{2(AD+C^2)},\qquad
b_* = \frac{A+C}{2(AD+C^2)}.
\]
It remains to prove feasibility. With \(x=\cos(2\pi k/N)\), the corresponding polynomial is
\[
P(x)=1+2a_*x+2b_*(4x^3-3x)
     =8b_*(x+C)(x-A)(x-(C-A)).
\]
The only interval on which this cubic is negative between sampled cosine values is the open interval between the two positive roots \(A\) and \(R=C-A\). Put \(\delta=\pi/(3N)\), so \(C=\cos(3\delta)\).

If \(N\equiv1\pmod6\), then \(A=\cos(\pi/3-\delta)\) and the next smaller sampled cosine is \(B=\cos(\pi/3+5\delta)\). We have \(B<R<A\): the inequality \(R<A\) follows from \(C<2A\), while
\[
A+B=2\cos(\pi/3+2\delta)\cos(3\delta)<\cos(3\delta)=C
\]
gives \(B<R\). Hence no sampled cosine lies in \((R,A)\).

If \(N\equiv-1\pmod6\), then \(A=\cos(\pi/3+\delta)\) and the preceding larger sampled cosine is \(B=\cos(\pi/3-5\delta)\). Here \(A<R<B\). Indeed,
\[
C-2A=\sin\delta\left(\sqrt3-2\sin(2\delta)\right)>0,
\]
and
\[
A+B=2\cos(\pi/3-2\delta)\cos(3\delta)>\cos(3\delta)=C.
\]
Thus no sampled cosine lies in \((A,R)\). In either residue class every sampled value of \(P\) is nonnegative, so the upper bound is attained.

## Verification
The accompanying `verify.py` independently evaluates the closed formulas for every \(7\le N\le2000\), checks all sampled Fourier inequalities, checks the stated active contacts and objective values, and checks the root-gap inequalities used in the feasibility proof. The computation uses ordinary floating-point arithmetic only as a corroborative stress test; the proof above is analytic and does not rely on numerical tolerances.

## Relationship to prior work
Kolountzakis and Révész introduced the Turán constant on general locally compact abelian groups, explicitly use counting measure on discrete groups, and emphasize finite groups. Their Example 3 solves a different five-point support problem on \(\mathbb Z\), namely \(\{-M,-1,0,1,M}\), by reducing it to a nonnegative trigonometric polynomial with two frequencies. That example supplies the closest structural precedent, but it is a continuum-in-frequency positivity problem on \(\mathbb Z\), not the sampled finite-cyclic problem for the fixed support \(\{0,\pm1,\pm3}\). Their finite-group theorems provide packing and spectral upper bounds rather than the exact three-regime formula proved here. Révész's later survey develops the general locally compact abelian framework and packing bounds but does not, in the inspected material, give this exact cyclic five-point value.

The closest previously recorded local result checked for overlap optimizes the first Fourier coefficient while allowing a third-harmonic coefficient. Its objective is different from maximizing the total Turán mass \(1+2a+2b\), so neither its statement nor its dual certificate implies the present formula.

## Limitations
The claim is only for the canonical five-point support \(\{0,\pm1,\pm3}\) and \(N\ge7\). It does not classify arbitrary two-frequency supports \(\{0,\pm r,\pm s}\), nor does it assert a general formula for all five-point subsets of cyclic groups. The originality search found no covering statement, but sparse finite cyclic extremal calculations can be difficult to index and may exist under alternative trigonometric-polynomial terminology.

## References
1. M. N. Kolountzakis and S. Gy. Révész, *Turán's extremal problem for positive definite functions on groups*, arXiv:math/0312218v1, 2003. Primary MSC 43A35.
2. S. Gy. Révész, *Turán's extremal problem on locally compact abelian groups*, arXiv:0904.1824v1, 2009.
