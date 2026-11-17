# The complete prime-two census and an exact instability barrier in an axially symmetric quadratic map

## Finding
Let \(F_{b,c,\mu}:\mathbb R^3\to\mathbb R^3\) be
\[
F(x,y,z)=\bigl(y,-bx+\mu y+yz,cz+y^2\bigr),\qquad 0<b<1,\quad0<c<1,\quad \mu\in\mathbb R.
\]
Write \(P=(1+b)(1+c)\), \(\mu_a=-(1+b)\), and \(\mu_b=-2c(1+b)/(1-c)\). There are exactly
\[
N_2(b,c,\mu)=\mathbf1_{\{\mu<\mu_a\}}+2\mathbf1_{\{\mu<\mu_b\}}
\]
real primitive period-two orbits. Strict inequalities are essential: at either equality the corresponding solutions collapse to fixed points, not nontrivial two-cycles. For \(c<1/3\), the two off-antipodal orbits arise as \(\mu\) decreases before the antisymmetric orbit; for \(c>1/3\) this order reverses; at \(c=1/3\) both thresholds coincide.

All off-antipodal prime-two orbits have a positive real two-step Floquet multiplier greater than one, for every admissible parameter choice. In particular no such orbit is an attracting sink. No stability claim is made here about the remaining antisymmetric orbit.

## Assumptions and scope
All statements concern real points of the complete polynomial map on \(\mathbb R^3\), not a bounded absorbing region. The parameter bounds are strict \(0<b<1\), \(0<c<1\), with no restriction on \(\mu\). Distinct orbits are counted modulo cyclic exchange of the two points. The map commutes with the central symmetry \((x,y,z)\mapsto(-x,-y,z)\).

## Proof
Write a possible two-cycle as \((p,q,z_0)\mapsto(q,p,z_1)\mapsto(p,q,z_0)\). Necessarily
\[
(1+b)p=q(\mu+z_0),\quad (1+b)q=p(\mu+z_1),\quad
z_0=c z_1+p^2,\quad z_1=c z_0+q^2.
\]
If either \(p\) or \(q\) vanishes, both vanish and \(z_0=z_1=0\). Otherwise \(z_0=(p^2+cq^2)/(1-c^2)\) and \(z_1=(q^2+cp^2)/(1-c^2)\). Multiply the first of the displayed equations by \(p\), the second by \(q\), and subtract. The result is
\[
(p^2-q^2)\left(1+b-\frac{pq}{1+c}\right)=0.
\]
If \(p^2=q^2\), the possibility \(p=q\) is a fixed point. The possibility \(p=-q\ne0\) gives a single primitive orbit precisely for \(p^2=(1-c)(-\mu-1-b)>0\), equivalently \(\mu<\mu_a\).

If \(p^2\ne q^2\), the displayed factorization forces \(pq=P>0\). Substituting into either two-cycle equation yields
\[
p^2+q^2=-\frac{\mu(1-c^2)}c=:S.
\]
Since \(pq=P\), real unequal values \(p^2,q^2>0\) exist precisely when \(S>2P\), i.e. \(\mu<\mu_b\). The two distinct positive square roots of the roots of \(t^2-St+P^2\) determine a single orbit with \(p,q>0\), and changing both signs determines exactly one further orbit with \(p,q<0\). Swapping \(p\) and \(q\) only changes the starting phase. Thus all cases are exhausted.

For instability, the one-step Jacobian is
\[
J(y,z)=\begin{pmatrix}0&1&0\\-b&\mu+z&y\\0&2y&c\end{pmatrix}.
\]
At a non-antipodal two-cycle form \(K=J(p,z_1)J(q,z_0)\). Substituting \(pq=P\), the formulas for \(z_i\), and \(S=-\mu(1-c^2)/c\) gives the exact identity
\[
\det(I-K)=-\frac{2c}{1+c}(p^2-q^2)^2<0.
\]
For the real monic characteristic polynomial \(h(\lambda)=\det(\lambda I-K)\), we have \(h(1)<0\) and \(h(\lambda)\to+\infty\) as \(\lambda\to+\infty\). Hence a real eigenvalue exceeds one. Finally, comparing \(\mu_a\) and \(\mu_b\) reduces to comparing \(2c/(1-c)\) with 1, giving the crossing at \(c=1/3\). This completes the classification.

## Verification
The included `checker.py` independently substitutes a nondegenerate exact-rational example into both two-cycle relations and the Floquet determinant identity, and checks the fully symbolic polynomial identity for the determinant after elimination. The proof of completeness is algebraic and does not rely on numerical enumeration. Run `python checker.py` with Python and SymPy installed.

## Relationship to prior work
Gonchenko and Gonchenko (2023) introduce the axial-symmetry constant-Jacobian quadratic setting and its bifurcation phenomena. Gonchenko (2024), Sections 2.1–2.2, gives the universal normal form, a square-map duality, and local fixed-point and period-doubling scenarios. Those results are the structural starting point. The present statement is a global real prime-two *orbit census* for the \(\alpha=+1\) normal form, together with the strict obstruction \(\det(I-K)<0\) for the two symmetry-related off-antipodal orbits; it does not treat the local pitchfork/flip normal forms as new. A check against related indexed results did not identify the same census or determinant obstruction, but inaccessible or unindexed treatments may precede this calculation.

## Limitations
There is no classification here of periods three or higher, non-periodic invariant sets, the stable manifold of a saddle orbit, or global attractors. The 2023 originating full text was not available for direct inspection, so the possibility of equivalent formulas or implied results in it remains a specific priority risk. The 2024 source was inspected in its freely available PDF (especially Sections 2.1–2.2); publication precedence has not been independently adjudicated. No independent mathematical audit has been performed.

## References
- S. Gonchenko and A. Gonchenko, *On discrete Lorenz-like attractors in three-dimensional maps with axial symmetry*, Chaos 33 (2023), DOI: 10.1063/5.0172243, publicly dated 2023-12-01. https://pubmed.ncbi.nlm.nih.gov/38048253/
- A. Gonchenko, *On discrete Lorenz attractors of various types*, Applied Nonlinear Dynamics 32(6) (2024), pp. 832–857, DOI: 10.18500/0869-6632-003140. https://andjournal.sgu.ru/sites/andjournal.sgu.ru/files/text-pdf/en/2025/07/and_2024_6_gonchenko_en.pdf
