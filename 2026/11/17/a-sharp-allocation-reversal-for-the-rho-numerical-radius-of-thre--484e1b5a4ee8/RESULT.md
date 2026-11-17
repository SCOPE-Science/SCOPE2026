# A sharp allocation reversal for the \(\rho\)-numerical radius of three-site shifts

## Finding
Let \(W_{a,b}\in M_3(\mathbb C)\) have entries \((W_{a,b})_{12}=a\), \((W_{a,b})_{23}=b\), all others zero. For every \(\rho>0\) and nonnegative \(a,b\), the exact unitary-dilation operator radius is
\[
\omega_\rho(W_{a,b})=\frac1\rho\sqrt{\frac{a^2+b^2+\sqrt{(a^2-b^2)^2+4(\rho-1)^2a^2b^2}}{2}}.
\]
If \(s=a^2+b^2>0\) is prescribed, the minimizing allocation is uniquely \(a=b=\sqrt{s/2}\) when \(0<\rho<2\), but the maximizing allocation is exactly either \((\sqrt s,0)\) or \((0,\sqrt s)\). When \(\rho>2\), the minimizing and maximizing allocations exchange places. At \(\rho=2\), every allocation has radius \(\sqrt{s}/2\). Thus the classical numerical-radius parameter is the exact boundary of a global optimizer reversal. All statements allow complex weights after a diagonal unitary phase adjustment.

## Assumptions and scope
For a bounded operator \(T\) on a complex Hilbert space, the radius \(\omega_\rho(T)\) is the infimum of \(t>0\) for which \(T/t\) admits a unitary \(\rho\)-dilation: there are a larger Hilbert space, its unitary \(U\), and an orthogonal projection \(P\) such that \((T/t)^n=\rho PU^n\vert_H\) for all integers \(n\ge1\). We use the standard equivalent operator-valued Herglotz positivity criterion. The finite matrix may be regarded as acting on a larger Hilbert space by zero extension. The fixed budget \(s\) is the squared Hilbert–Schmidt norm. We make no assertion for the zero operator beyond the obvious radius zero.

## Proof
**Step 1: dilation positivity.** For any nilpotent \(T\) with \(T^3=0\), the positive-definite moment criterion for a unitary \(\rho\)-dilation is equivalent to positivity on the unit circle of
\[
H_{\rho,t}(z)=\rho I+zT/t+\bar zT^*/t+z^2T^2/t^2+\bar z^2(T^*)^2/t^2.
\]
Indeed the analytic operator-valued Herglotz function is \(I+(2/\rho)\sum_{k\ge1}z^k(T/t)^k\), and the series truncates. Its positive real part is equivalent to positive-definiteness of the Toeplitz moment sequence; an operator-valued Herglotz representation and a Naimark unitary dilation give the stated equivalence. Positivity on the unit circle is equivalent to positivity inside by the scalar harmonic minimum principle applied to each vector state. Diagonal unitary conjugation removes the phase of \(z\) and both weight phases, so only the positive matrix
\[
H=\begin{pmatrix}\rho&a/t&ab/t^2\\a/t&\rho&b/t\\ab/t^2&b/t&\rho\end{pmatrix}
\]
remains to be tested.

**Step 2: exact root.** Put \(u=t^{-2}\), \(s=a^2+b^2\) and \(p=ab\). Direct determinant expansion yields
\[\det H=\rho^3-\rho s u+(2-\rho)p^2u^2.\]
For \(p>0\) its smallest positive zero is
\[u_*=\frac{2\rho^2}{s+\sqrt{(a^2-b^2)^2+4(\rho-1)^2p^2}}=\frac{\rho^2}{L},\]
where \(L\) is the largest eigenvalue of the Hermitian matrix
\[Q=\begin{pmatrix}a^2&(\rho-1)ab\\(\rho-1)ab&b^2\end{pmatrix}.\]
The formula remains valid when \(p=0\), as follows by the explicit diagonal form or continuity.

**Step 3: positivity at the root and sharpness.** The eigenvalue \(L\) satisfies \(L\ge\max\{a^2,b^2\}\) and \(L\ge\rho ab\). For the second inequality, use \(s\ge2ab\) and \(\sqrt{(a^2-b^2)^2+4(\rho-1)^2a^2b^2}\ge2|\rho-1|ab\); for \(\rho\le1\) the first inequality alone suffices. Therefore at \(u=u_*\) all three order-two principal minors are nonnegative, the diagonal entries are positive, and \(\det H=0\). The principal-minor criterion proves \(H\succeq0\). For smaller \(t\), the matrix cannot remain positive: the determinant changes sign immediately beyond its first simple zero, except in the repeated-root case \(\rho=1,a=b\), when the neighboring two-by-two minors become negative instead. Since the admissible set of scales is an upper interval (from the defining Minkowski functional), this proves \(\omega_\rho(W_{a,b})=u_*^{-1/2}=\sqrt L/\rho\).

**Step 4: sharp weight allocation.** At fixed \(s>0\), write \(p=ab\in[0,s/2]\). Then
\[L=\frac{s+\sqrt{s^2-4\rho(2-\rho)p^2}}2.\]
For \(0<\rho<2\), this quantity is strictly decreasing in \(p\) away from \(p=0\); for \(\rho>2\), it is strictly increasing. The product \(p\) is maximized uniquely by balanced weights and vanishes precisely at one-zero-edge allocations. At \(\rho=2\), \(L=s\) for all allocations. This proves every equality case and the phase reversal. On the strictly positive two-weight domain, the zero-edge extrema become sharp but unattained suprema or infima.

## Verification
The identities for \(\det H\), its first positive zero, the principal minors, and the allocation derivative are exact algebraic calculations. A supplementary standalone checker (`CHECK.py`) tests the formula against all principal minors at and near the predicted boundary for a finite grid of weights and parameters; its finite tests are not the proof. Complex phases are removed by a diagonal unitary and hence do not change the radius. In particular, at \(\rho=1\) the formula reduces to \(\|W_{a,b}\|=\max(a,b)\), while at \(\rho=2\) it gives \(\omega_2(W_{a,b})=\sqrt{a^2+b^2}/2\). If \(ab=0\), the two-nilpotent identity gives \(\omega_\rho(W_{a,b})=\max(a,b)/\rho\).

## Relationship to prior work
The 2026 rank-one formula of Stanković supplies the operator-radius setting and the two-nilpotent boundary case; the present rank-two matrix has a genuinely nonzero second power when both weights are positive. Laurent Carrot's earlier results give estimates for three-nilpotent operators and normalized large-\(\rho\) laws, while his 2003 paper concerns truncated shifts. Those known results cover the general context and the equal-weight special geometry, but the accessible statements do not imply the two-weight exact formula and its sharp fixed-Hilbert–Schmidt allocation reversal. The relevant 2003 full text was not accessible, so priority of a different equivalent formulation has not been excluded.

## Limitations
The theorem is confined to three sites (nilpotency index at most three), unitary-dilation operator radii, and a fixed Hilbert–Schmidt budget. It does not classify all general three-nilpotent operators or infinite weighted shifts. The 2003 truncated-shift source was bibliographically located but not read in full; possible older equivalent formulas remain a publication-priority risk. Independent mathematical validation has not been performed.

## References
H. Stanković, *On the \(\rho\)-numerical radius of rank-one operators and parametrized Buzano-type inequalities*, arXiv:2609.00037v1 (publicly submitted 2026-08-29), https://borowiecki.dev/pdf/2609.00037.

L. Carrot, *\(\rho\)-Numerical Radius in Banach Spaces*, in *Recent Advances in Operator Theory, Operator Algebras, and their Applications*, Operator Theory: Advances and Applications 153 (2004), pp. 79–101, https://doi.org/10.1007/3-7643-7314-8_5.

L. Carrot, *Computation of the \(\rho\)-numerical radius for truncated shifts*, *Acta Scientiarum Mathematicarum* 69 (2003), pp. 311–322, https://acta.bibl.u-szeged.hu/15968/.

T. Ando and K. Nishio, *Convexity properties of operator radii associated with unitary \(\rho\)-dilations*, *Michigan Mathematical Journal* 20 (1973), pp. 303–307.
