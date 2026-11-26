# Complete two-cycle census and a one-third damping crossover in axial quadratic maps

## Finding

Consider the axially symmetric quadratic diffeomorphism
\[
F_{\alpha}(x,y,z)=(y,\,n x+m y+yz,\,r z+\alpha y^2),
\qquad 0<n<1,\quad 0<r<1,\quad m\in\mathbb R,\quad \alpha\in\{-1,1\}.
\]
Write \(A=1-n\). A **primitive two-cycle** is an unordered orbit \(\{p,F_\alpha(p)\}\) with \(F_\alpha^2(p)=p\) and \(F_\alpha(p)\ne p\). The complete number of real primitive two-cycles is
\[
\boxed{N_2=\mathbf1_{\{\alpha(A+m)<0\}}+
2\mathbf1_{\{\alpha m<-2rA/(1-r)\}}.}\tag{1}
\]
The first term is the unique, centrally switching **symmetric** cycle, when it exists; the second is an exactly paired family of **asymmetric** cycles exchanged by the axial reflection \((x,y,z)\mapsto(-x,-y,z)\). No other primitive two-cycles exist.

Every asymmetric cycle is unstable. More precisely, if its consecutive points are \((a,b,z_0)\) and \((b,a,z_1)\), with \(a^2\ne b^2\), its two-step derivative \(P=D F_\alpha(b,a,z_1)\,D F_\alpha(a,b,z_0)\) satisfies
\[
\boxed{\det(P-I)=\frac{2r}{1+r}(a^2-b^2)^2>0.}\tag{2}
\]
Consequently \(P\) has a real eigenvalue strictly greater than one, so neither of the paired asymmetric cycles can be an attracting sink.

For \(\alpha=1\), the order of the two cycle-creation thresholds reverses at the **sharp damping ratio** \(r=1/3\). Let \(m_*= -2rA/(1-r)\). As \(m\) decreases:

- When \(0<r<1/3\), the exact counts are \(0\), then \(2\) in \(-A\le m<m_*\), then \(3\) for \(m<-A\); the two asymmetric cycles exist without any symmetric cycle in the middle regime.
- When \(1/3<r<1\), the counts are \(0\), then \(1\) for \(m_*\le m<-A\), then \(3\) for \(m<m_*\).
- At \(r=1/3\), the count jumps directly from \(0\) for \(m\ge-A\) to \(3\) for \(m<-A\).

For \(\alpha=-1\), the counts are \(0\) for \(m\le-A\), \(1\) for \(-A<m\le2rA/(1-r)\), and \(3\) above that second threshold. Endpoints throughout use the indicated strict inequalities; degenerate fixed or two-cycle collisions are not counted as distinct asymmetric cycles.

## Assumptions and scope

All parameters and orbits are real, \(0<n<1\), \(0<r<1\), and \(\alpha=\pm1\). The map is globally invertible, with constant Jacobian \(-nr\). The theorem counts least-period-two orbits across all of \(\mathbb R^3\), not just an invariant box or an attracting region. There are no assumptions about boundedness or existence of strange attractors.

The asymmetric cycles have an explicit algebraic parameterization. Set
\[
B=\frac{A(1+r)}\alpha,\qquad
S=-\frac{m(1-r^2)}{\alpha r}.
\]
They exist precisely when \(S>2|B|\). In that event define \(u=(S+\sqrt{S^2-4B^2})/2\), \(v=(S-\sqrt{S^2-4B^2})/2\). Choose \(a=\sqrt{u}\), \(b=B/a\), and
\[
z_0=\frac{\alpha(a^2+r b^2)}{1-r^2},\qquad
z_1=\frac{\alpha(b^2+r a^2)}{1-r^2}.
\]
One primitive cycle is \((a,b,z_0)\leftrightarrow(b,a,z_1)\), the other is its reflection \((-a,-b,z_0)\leftrightarrow(-b,-a,z_1)\). The symmetric cycle, when present, is
\[
(t,-t,z)\leftrightarrow(-t,t,z),\qquad
t^2=-\frac{(A+m)(1-r)}\alpha,\qquad z=\frac{\alpha t^2}{1-r},
\]
where the two square-root choices of \(t\) belong to the same orbit.

## Proof

**All two-cycles reduce to two scalar equations.** Let \((a,b,z_0)\mapsto(b,a,z_1)\mapsto(a,b,z_0)\). The last component gives uniquely
\[
z_0=\frac{\alpha(a^2+r b^2)}{1-r^2},\qquad
z_1=\frac{\alpha(b^2+r a^2)}{1-r^2}.
\]
The second component at the two points is equivalent to
\[
A a=b(m+z_0),\qquad A b=a(m+z_1).\tag{3}
\]
If one of \(a,b\) vanishes, both vanish by \(A>0\), and the only possibility is the origin, which is fixed. If \(a=b\), the point is fixed; if \(a=-b\ne0\), the equations give precisely the symmetric two-cycle condition in (1).

Suppose now \(a^2\ne b^2\). Multiply (3) by \(a\) and \(b\), respectively, and subtract. Since \(z_0-z_1=\alpha(a^2-b^2)/(1+r)\), this gives
\[
ab=\frac{A(1+r)}\alpha=B.\tag{4}
\]
Multiplying (3) by \(b\) and \(a\), respectively, and subtracting yields
\[
0=(b^2-a^2)\left(m+\frac{\alpha r(a^2+b^2)}{1-r^2}\right),
\]
hence \(a^2+b^2=S\). Conversely, (4) and \(a^2+b^2=S\) imply (3) after substituting the displayed expressions for \(z_0,z_1\): for example, \(m+z_0=\alpha a^2/(1+r)=A a/b\). Therefore the asymmetric points correspond exactly to positive unequal roots \(u,v\) of \(X^2-SX+B^2=0\). Such roots exist if and only if \(S>2|B|\), equivalently \(\alpha m<-2rA/(1-r)\). Their only sign choices produce the two reflected primitive cycles given above; swapping \(u,v\) advances one step on the same cycle. This proves (1) without excluding any solutions by numerical search.

**Forced instability.** For an asymmetric orbit write \(q=a/b\). Relations (3) and (4) imply \(m+z_0=Aq\), \(m+z_1=A/q\), and \(\alpha b^2q=A(1+r)\). Thus the two derivatives are exactly
\[
J_0=\begin{pmatrix}0&1&0\\n&Aq&b\\0&2\alpha b&r\end{pmatrix},\qquad
J_1=\begin{pmatrix}0&1&0\\n&A/q&qb\\0&2\alpha qb&r\end{pmatrix}.
\]
Direct expansion gives
\[
\det(J_1J_0-I)=\frac{2\alpha b^2}{q}
\left[A r(q^4+1)+2Aq^2-2\alpha b^2q^3\right]
=\frac{2rA^2(1+r)(q^2-1)^2}{q^2},
\]
where the final step uses \(\alpha b^2q=A(1+r)\). Since \(a^2-b^2=b^2(q^2-1)\) and \(\alpha b^2q=A(1+r)\), this is precisely (2). For the monic characteristic polynomial \(p(t)=\det(tI-P)\), \(p(1)=-\det(P-I)<0\), whereas \(p(t)\to+\infty\) as \(t\to+\infty\). The intermediate value theorem gives a real multiplier greater than one.

**The damping crossover.** For \(\alpha=1\), the symmetric condition is \(m<-A\) and the asymmetric condition is \(m<m_*\). Their threshold difference has sign
\[
m_*+A=\frac{A(1-3r)}{1-r}.
\]
This changes sign only at \(r=1/3\), proving the stated phase order and counts. For \(\alpha=-1\), the respective conditions are \(m>-A\) and \(m>2rA/(1-r)\), in that order for all \(0<r<1\). At the asymmetric creation threshold, \(S=2|B|\) and the two roots coincide. The emerging squared-coordinate gap has the sharp law
\[
|a^2-b^2|=2\sqrt{\frac{A(1+r)(1-r^2)}r}\,
\sqrt{|m-m_*|}+O(|m-m_*|^{3/2})
\]
on the existence side (where \(m_*=-\alpha\,2rA/(1-r)\) for either sign). For \(\alpha=1\) the coincident points are fixed, whereas for \(\alpha=-1\) they form the symmetric two-cycle. This completes the proof.

## Verification

The standalone `verify.py` uses exact SymPy algebra for the determinant identity and Python rational arithmetic for 16 explicitly reconstructed nonzero asymmetric orbits across four damping values and both signs. It also tests the exact crossover identity on both sides of \(r=1/3\). Run from this package with `python verify.py` (Python 3, SymPy). The certificate is a reproducibility check, not a substitute for the analytic quantifier proof above.

## Relationship to prior work

The exact quadratic map, axial symmetry, constant-Jacobian property, and the basic fixed-point pitchfork/flip scenarios are established in the 2023 work of S. V. Gonchenko and A. S. Gonchenko and the 2024 continuation by the same authors. The open-access 2024 article by A. S. Gonchenko explicitly states the map, discusses duality of its second iterates, and analyzes the stability triangle and the primary origin bifurcations. The theorem here instead gives the **complete global least-period-two orbit census**, the off-symmetry pair threshold, the return-multiplier obstruction, and the precise damping-order reversal. No general Lorenz-attractor assertion follows from it.

## Limitations

The restriction \(0<n<1\) and \(0<r<1\) is essential to the stated classification and its ordering argument. The theorem does not classify period three or higher, global basins, invariant circles, or chaotic attractors. The instability conclusion is the existence of at least one real multiplier greater than one; it is not a complete three-multiplier classification. Some primary manuscripts were not fully accessible at comparison time, so equivalent unpublished or unindexed formulas cannot be excluded solely by the inspected sources. Independent validation has not been performed.

## References

1. S. V. Gonchenko and A. S. Gonchenko, *On discrete Lorenz-like attractors in three-dimensional maps with axial symmetry*, Chaos **33** (2023), 123104, DOI: https://doi.org/10.1063/5.0172243 (publicly dated 2023-12-04 in the indexed online record).
2. S. V. Gonchenko and A. S. Gonchenko, *Discrete Lorenz attractors of new types in three-dimensional maps with axial symmetry*, Partial Differential Equations in Applied Mathematics **11** (2024), 100904, DOI: https://doi.org/10.1016/j.padiff.2024.100904.
3. A. S. Gonchenko, *On discrete Lorenz attractors of various types*, Applied Nonlinear Dynamics **32** (2024), 832–857, DOI: https://doi.org/10.18500/0869-6632-003140. Lawful open-access full text: https://andjournal.sgu.ru/sites/andjournal.sgu.ru/files/text-pdf/en/2025/07/and_2024_6_gonchenko_en.pdf (available online 2024-11-25; used solely as supporting literature).
