# Sharp second-sweep positivity threshold for SOR on Stieltjes systems
## Finding
Let \(n\ge 1\). For every real symmetric positive-definite Stieltjes matrix \(A\in\mathbb R^{n\times n}\), every \(b\ge0\), and zero-start forward SOR with relaxation \(0<\omega<2\), the second iterate \(x^{(2)}\) is componentwise nonnegative for all such \(A,b\) if and only if \(\omega\le (n+1)/n\). The first iterate is componentwise nonnegative throughout \(0<\omega<2\). For every \(n\ge2\) and every \((n+1)/n<\omega<2\), the tridiagonal Stieltjes family \(A_\varepsilon=I-\varepsilon(S+S^{\mathsf T})\), where \(S_{i,i-1}=1\), with \(b=e_1\) and sufficiently small \(\varepsilon>0\), is positive definite, lies inside the classical SOR convergence range, and has \((x^{(2)})_n<0\). Thus the exact dimension-dependent universal cone-safety margin for the second SOR sweep is \(\omega-1\le1/n\).

Equivalently, among all convergent relaxation parameters, the first sweep is universally cone-preserving, while the second sweep is universally cone-preserving exactly for
\[
0<\omega\le 1+\frac1n.
\]
For \(n=1\), this covers the whole convergence interval \(0<\omega<2\).

## Assumptions and scope
Write a Stieltjes matrix as \(A=D-E-F\), where \(D\) is the positive diagonal and \(E,F\ge0\) are the strict lower and upper parts. Forward SOR is
\[
(D-\omega E)x^{(k+1)}=((1-\omega)D+\omega F)x^{(k)}+\omega b,
\qquad x^{(0)}=0.
\]
A positive diagonal similarity reduces the proof to unit diagonal without changing componentwise signs: with \(y=D^{1/2}x\), \(c=D^{-1/2}b\), and
\[
D^{-1/2}AD^{-1/2}=I-L-U,
\]
we have \(L,U\ge0\) and \(U=L^{\mathsf T}\). The theorem concerns exact arithmetic, the standard forward ordering, and the first two completed SOR sweeps. No claim is made for later sweeps, nonsymmetric \(M\)-matrices, block SOR, asynchronous SOR, or floating-point sign preservation.

## Proof
Let
\[
R=(I-\omega L)^{-1}=\sum_{j=0}^{n-1}\omega^jL^j\ge0,
\]
because \(L^n=0\). The normalized SOR iteration is
\[
y^{(k+1)}=T y^{(k)}+\omega Rc,
\qquad
T=R((1-\omega)I+\omega U).
\]
Hence \(y^{(1)}=\omega Rc\ge0\) for every \(\omega>0\). The second iterate is \(y^{(2)}=Q_2c\), where
\[
Q_2=\omega\bigl[R+(1-\omega)R^2+\omega RUR\bigr].
\]
Since
\[
R^2=\sum_{j=0}^{n-1}(j+1)\omega^jL^j,
\]
we obtain
\[
R+(1-\omega)R^2
=\sum_{j=0}^{n-1}\omega^j\bigl[(j+2)-(j+1)\omega\bigr]L^j.
\]
The scalar thresholds \((j+2)/(j+1)=1+1/(j+1)\) decrease with \(j\), so all coefficients are nonnegative exactly when \(\omega\le(n+1)/n\). Because \(L^j\ge0\) and \(RUR\ge0\), this proves \(Q_2\ge0\) and therefore \(y^{(2)}\ge0\) for every \(c\ge0\) throughout that range.

For sharpness, let \(S\) be the strict lower shift and set
\[
A_\varepsilon=I-\varepsilon(S+S^{\mathsf T}),\qquad b=e_1.
\]
If \(0<\varepsilon<1/2\), then \(A_\varepsilon\) is Stieltjes and positive definite because every eigenvalue is larger than \(1-2\varepsilon>0\). Here \(L=\varepsilon S\) and \(U=\varepsilon S^{\mathsf T}\). Direct path counting gives
\[
(RUR)_{n1}=(n-1)\omega^n\varepsilon^{n+1},
\]
and therefore
\[
(Q_2)_{n1}
=\omega^n\varepsilon^{n-1}
\left[(n+1)-n\omega+(n-1)\omega^2\varepsilon^2\right].
\]
For every \((n+1)/n<\omega<2\), choose
\[
0<\varepsilon<\min\!\left\{\frac12,
\sqrt{\frac{n\omega-(n+1)}{(n-1)\omega^2}}\right\}.
\]
Then \((Q_2)_{n1}<0\), so \((y^{(2)})_n<0\). The matrix remains SPD, and classical SOR therefore converges for every \(0<\omega<2\). This proves necessity and sharpness.

## Verification
The accompanying `verify.py` reconstructs the SOR second-iterate matrix in exact rational arithmetic for the witness
\[
n=3,\qquad \omega=\frac75,\qquad \varepsilon=\frac1{10},
\]
for which
\[
A=\begin{pmatrix}
1&-1/10&0\\
-1/10&1&-1/10\\
0&-1/10&1
\end{pmatrix},\qquad b=e_1.
\]
Its leading principal minors are \(1\), \(99/100\), and \(49/50\), while the second SOR iterate is
\[
x^{(2)}=
\begin{pmatrix}
10843/12500\\
14651/312500\\
-68943/15625000
\end{pmatrix},
\]
so the final component is strictly negative. The checker also verifies the closed endpoint-entry formula and the coefficient signs at the proposed boundary for several exact rational dimensions. Those finite checks supplement, but do not replace, the analytic proof for arbitrary \(n\).

## Relationship to prior work
Classical SOR theory focuses on convergence and the choice of relaxation factor. Vigna's work on step-asynchronous SOR for \(M\)-matrices proves weighted supremum-norm error contraction under a positive comparison vector; it does not state a componentwise finite-sweep cone threshold. Marek and Zítko study acceleration of SOR and classify the subject under MSC 65F10, while James and Riha study convergence criteria for relaxation on matrices with positive diagonal and nonpositive off-diagonal entries. Axelsson's treatment develops \(M\)-matrix splittings and SOR primarily through convergence-rate comparison. None of the inspected statements implies the exact second-sweep threshold \(1+1/n\), the endpoint coefficient identity above, or the sharp weak-coupling chain witness.

## Limitations
The theorem is deliberately finite-horizon: it gives the exact universal boundary at sweep two, not a classification of all later SOR iterates. The sharp witness is a weakly coupled tridiagonal chain and proves universal failure above the threshold; it does not assert that every SPD Stieltjes system loses positivity there. An unresolved literature risk is that older monotone-iteration or regular-splitting literature may encode the same two-sweep identity under different terminology, although focused searches for SOR, \(M\)-matrices, nonnegative iterates, componentwise monotonicity, and second-iterate positivity did not locate such a result.

## References
1. S. Vigna, *Supremum-Norm Convergence for Step-Asynchronous Successive Overrelaxation on M-matrices*, arXiv:1404.3327v1, first public submission 2014-04-12.
2. I. Marek and J. Zítko, *Ljusternik acceleration and the extrapolated S.O.R. method*, Aplikace matematiky 22 (1977), 116–133, DOI 10.21136/AM.1977.103683.
3. K. R. James and W. Riha, *Convergence Criteria for Successive Overrelaxation*, SIAM Journal on Numerical Analysis 12 (1975), 137–143, DOI 10.1137/0712013.
4. O. Axelsson, *M-Matrices, Convergent Splittings, and the SOR Method*, in *Iterative Solution Methods*, Cambridge University Press, 1994, DOI 10.1017/CBO9780511624100.007.
