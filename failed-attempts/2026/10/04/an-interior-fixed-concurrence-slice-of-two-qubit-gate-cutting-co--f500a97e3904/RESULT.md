# An interior fixed-concurrence slice of two-qubit gate-cutting cost is disconnected

## Finding
Consider the optimal quasiprobability-decomposition extent \(\gamma\) for an arbitrary two-qubit unitary, and fix its maximum product-input concurrence at
\[
C_{\max}=\frac12.
\]
The set of attainable \(\gamma\) values is not connected. More explicitly, no such gate can satisfy
\[
\Gamma_L<\gamma<\Gamma_H,
\]
where
\[
\Gamma_L=
\frac{9-2\sqrt3+\sqrt{129-36\sqrt3}}4
\approx 3.4249022488
\]
and
\[
\Gamma_H=
\frac{13+3\sqrt{21}}4
\approx 6.6869317712.
\]
The two sides are nonempty: the controlled Cartan gate with parameters \((\pi/12,0,0)\) has \(C_{\max}=1/2\) and \(\gamma=2\), whereas the iSWAP–SWAP gate with parameters \((\pi/4,\pi/4,\pi/6)\) has \(C_{\max}=1/2\) and \(\gamma=7\).

Thus an interior fixed-concurrence slice of the outer-envelope band in arXiv:2609.30141v1 has a certified forbidden interval. This supplies a concrete interior disconnected slice for the attainable-set topology question raised there.

## Assumptions and scope
Use the non-negative Cartan representative
\[
0\leq\theta_3\leq\theta_2\leq\theta_1\leq\frac\pi4.
\]
The source gives
\[
C_{\max}=
\begin{cases}
\sin[2(\theta_1+\theta_2)],&\theta_1+\theta_2<\pi/4,\\
1,&\theta_1+\theta_2\geq\pi/4,\;\theta_2+\theta_3\leq\pi/4,\\
\sin[2(\theta_2+\theta_3)],&\theta_2+\theta_3>\pi/4,
\end{cases}
\]
and gate typicality
\[
g_{\mathrm t}=\frac13\sum_{j=1}^3\sin^2(2\theta_j).
\]
The same source proves exact lower and upper envelopes for \(\gamma\) at fixed \(g_{\mathrm t}\). The claim uses those established envelopes and does not assert the exact endpoints of either connected component at \(C_{\max}=1/2\).

## Proof
Because \(C_{\max}=1/2\neq1\), no point lies in the perfect-entangler branch. There are therefore two cases.

In the identity-like branch,
\[
\sin[2(\theta_1+\theta_2)]=\frac12,
\qquad
\theta_1+\theta_2<\frac\pi4.
\]
Hence
\[
\theta_1+\theta_2=\frac\pi{12}.
\]
The chamber ordering gives
\[
\theta_1\leq\frac\pi{12},
\qquad
\theta_2\leq\frac\pi{24},
\qquad
\theta_3\leq\frac\pi{24}.
\]
Since \(\sin^2(2x)\) is increasing for \(0\leq x\leq\pi/4\),
\[
g_{\mathrm t}
\leq
\frac13\left[
\sin^2\!\left(\frac\pi6\right)
+2\sin^2\!\left(\frac\pi{12}\right)
\right]
=
\frac{5-2\sqrt3}{12}
=:g_L.
\]
Here \(g_L<4/9\). On \(0\leq g\leq4/9\), the source's exact upper envelope is
\[
F(g)=1+3g+3\sqrt{g(4-3g)}.
\]
The function \(F\) is increasing there, so
\[
\gamma\leq F(g_L)
=
\frac{9-2\sqrt3+\sqrt{129-36\sqrt3}}4
=\Gamma_L.
\]

In the SWAP-like branch,
\[
\sin[2(\theta_2+\theta_3)]=\frac12,
\qquad
\theta_2+\theta_3>\frac\pi4,
\]
so
\[
\theta_2+\theta_3=\frac{5\pi}{12}.
\]
Because \(\theta_2\leq\pi/4\),
\[
\theta_3\geq\frac\pi6.
\]
The chamber ordering then implies
\[
\theta_1\geq\theta_2\geq\theta_3\geq\frac\pi6.
\]
Consequently
\[
g_{\mathrm t}\geq\frac34.
\]
For \(2/3\leq g\leq1\), the source's exact lower envelope is the same function
\[
F(g)=1+3g+3\sqrt{g(4-3g)}.
\]
It is increasing on this interval as well. Indeed,
\[
F'(g)=3+\frac{3(2-3g)}{\sqrt{g(4-3g)}},
\]
and for \(1/3\leq g\leq1\),
\[
g(4-3g)-(3g-2)^2
=4(1-g)(3g-1)\geq0.
\]
Therefore
\[
\gamma\geq F\!\left(\frac34\right)
=
\frac{13+3\sqrt{21}}4
=\Gamma_H.
\]

The two bounds are strictly separated. For example, \(\Gamma_L<4\) and \(\Gamma_H>6\). The controlled family gives a point on the lower side:
\[
(\theta_1,\theta_2,\theta_3)=\left(\frac\pi{12},0,0\right),
\qquad
C_{\max}=\frac12,
\qquad
\gamma=2.
\]
The iSWAP–SWAP family gives a point on the upper side:
\[
(\theta_1,\theta_2,\theta_3)
=
\left(\frac\pi4,\frac\pi4,\frac\pi6\right),
\qquad
C_{\max}=\frac12,
\qquad
\gamma=7.
\]
Thus the attainable set at fixed \(C_{\max}=1/2\) meets both sides of a nonempty forbidden open interval and is disconnected.

## Verification
The proof is analytic. The accompanying `verify.py` recomputes \(g_L\), \(\Gamma_L\), and \(\Gamma_H\), checks the representative controlled and iSWAP–SWAP points, and checks the numerical separation. Its finite grid checks are included only as consistency tests and are not used as proof of the continuum statement.

## Relationship to prior work
Hart's arXiv:2609.30141v1 proves the sharp one-descriptor outer envelope
\[
1+2C_{\max}\leq\gamma\leq7,
\]
states explicitly that intervening values inside this band are not asserted attainable, and notes that at the endpoint \(C_{\max}=0\) only \(\gamma=1\) and \(\gamma=7\) occur. It also proves that at \(C_{\max}=1\) the full interval \([3,7]\) is attained. Its discussion identifies topology and connected components of attainable sets inside the one-descriptor outer-envelope bands as a complementary extension.

The present result supplies an interior slice: \(C_{\max}=1/2\) already has a large forbidden cost interval. The argument combines the source's concurrence-region geometry with its independent exact gate-typicality envelopes; the fixed-concurrence disconnection is not one of the source's stated envelope theorems.

The optimal single-gate cutting formula used by Hart is attributed there to Schmitt, Piveteau, and Sutter, *Quantum* 9, 1634 (2025). The present argument does not modify that formula; it constrains its attainable values under a fixed entangling-capacity condition.

## Limitations
The constants \(\Gamma_L\) and \(\Gamma_H\) are certified exclusion bounds, not claimed to be the exact endpoint costs of the two components. The result treats the single interior slice \(C_{\max}=1/2\), not all \(0<C_{\max}<1\). It concerns ideal two-qubit unitaries and the optimal single-gate QPD extent in the framework of the source paper.

## References
1. M. Hart, *Optimal Two-Qubit Gate-Cutting Cost and Measures of Nonlocality*, arXiv:2609.30141v1 (2026).
2. L. Schmitt, C. Piveteau, and D. Sutter, *Cutting circuits with multiple two-qubit unitaries*, Quantum 9, 1634 (2025).
