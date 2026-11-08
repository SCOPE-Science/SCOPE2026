# Almost-everywhere escape on the negative singular slice of a four-partition planar map

## Finding

For every real \(a\ge1\), consider the continuous piecewise-affine map
\[
T_a(x,y)=(|x|+ay-1,\ x-a|y|-1), \qquad (x,y)\in\mathbb R^2.
\]
Every forward orbit either escapes in the strong sense \(\lVert T_a^n(x,y)\rVert\to\infty\), or eventually lands on one of the following finite orbits:

* the fixed point \(P_a=(2+1/a,1/a)\), for every \(a\ge1\);
* when \(1\le a<2\), the unique primitive two-cycle consisting of \((q_a,q_a)\) and \(((1+a)q_a-1,(1-a)q_a-1)\), where \(q_a=(a+2)/(a(2-a))\).

Conversely, every point eventually landing on these finite orbits has a bounded forward orbit. The set of all such initial points is contained in a countable union of affine lines and isolated points and therefore has two-dimensional Lebesgue measure zero. Consequently, almost every initial condition escapes to infinity. In particular, this singular parameter family has no bounded forward orbit that is not eventually periodic. The fixed point is a repeller; the two-cycle, when present, has one zero multiplier and one multiplier \(1+2a-a^2>1\).

## Assumptions and scope

The parameter \(a\) is any real number satisfying \(a\ge1\); the second coefficient in the original four-partition family is set to \(c=-a\), rather than \(c=a\). The dynamics are discrete time on the entire real plane, with ordinary absolute values and no bounding or invariant-domain restriction. "Eventually lands" means equality after finitely many iterations, not asymptotic convergence. Escape means divergence of the Euclidean norm, not merely unbounded limsup. All statements include points on switching axes.

## Proof

**A one-step half-plane collapse.** For any \((x,y)\), subtracting the second output from the first gives
\[
T_a(x,y)_1-T_a(x,y)_2=|x|-x+a(y+|y|)=2\max\{-x,0\}+2a\max\{y,0\}\ge0.
\]
Thus every orbit lies, from time one on, in \(H=\{x\ge y\}\). Partition \(H\) into \(C_1=\{x\ge y\ge0\}\), \(C_3=\{y\le x\le0\}\), and \(C_4=\{x\ge0\ge y\}\), including shared boundaries.

**The negative cone is trapping and expanding.** On \(C_3\),
\[
T_a(x,y)=J_3(x,y)^\top-(1,1)^\top,\qquad
J_3=\begin{pmatrix}-1&a\\1&a\end{pmatrix}.
\]
Since \(-x+ay\le(a-1)x\le0\) on \(C_3\), the next first coordinate is at most \(-1\). The half-plane inequality gives the next second coordinate no larger than the first; hence \(T_a(C_3)\subset C_3\). The characteristic polynomial of \(J_3\) is \(z^2-(a-1)z-2a\). Its values at \(1\) and \(-1\) are \(2-3a<0\) and \(-a<0\), respectively; its two real eigenvalues therefore lie strictly beyond \(1\) and \(-1\). The unique affine fixed point of this branch is \((1/(3a-2),3/(3a-2))\), outside \(C_3\). Thus every trajectory entering \(C_3\) diverges in norm.

**No bounded trajectory can remain in the positive cone except the fixed point.** On \(C_1\) the affine matrix is
\[
J_1=\begin{pmatrix}1&a\\1&-a\end{pmatrix},
\]
with fixed point \(P_a=(2+1/a,1/a)\in C_1\) and characteristic polynomial \(z^2+(a-1)z-2a\). The values at \(1,-1\) are \(-a<0,2-3a<0\), so both eigenvalue moduli are strictly larger than one. Any trajectory that stays in \(C_1\) forever either equals \(P_a\) or diverges in norm.

**Every excursion through the fourth quadrant reduces to a scalar affine return.** For \(x\ge0\ge y\),
\[
T_a(x,y)=(t,t),\qquad t=x+ay-1.
\]
When \(t\le0\), this point belongs to \(C_3\). When \(0<t\le1/(1+a)\), the next iterate belongs to \(C_3\), except possibly at the switching boundary \(x=0\), whose following iterate lies in \(C_3\). Otherwise \(t>1/(1+a)\), and
\[
(t,t)\mapsto ((1+a)t-1,(1-a)t-1)\in C_4
\mapsto \bigl(m_at-(a+2),\,m_at-(a+2)\bigr),
\quad m_a=1+2a-a^2.
\]
For \(a\ge2\), \(m_a\le1\): every positive return strictly decreases until it enters \(C_3\), unless the sequence has already escaped in norm (which is incompatible with staying bounded). For \(1\le a<2\), \(m_a>1\); the sole fixed scalar return is \(q_a=(a+2)/(a(2-a))>1/(1+a)\). If \(t<q_a\), iterates decrease and eventually enter \(C_3\); if \(t>q_a\), they grow to \(+\infty\); if \(t=q_a\), they form the announced two-cycle. Thus every bounded orbit visiting \(C_4\) eventually reaches this two-cycle.

**Exhaustion of all orbits and escape, not merely unboundedness.** Once inside \(H\), any orbit that ever enters \(C_3\) escapes by the expanding affine dynamics. Any remaining orbit either visits \(C_4\), with the scalar alternatives just established, or remains in \(C_1\), with the alternatives established above. Each escaping alternative has norm tending to infinity. This proves the full dichotomy, including every switching boundary.

**Size of the bounded exceptional set.** On the initially excluded quadrant \(x\le0\le y\), the image has the form \((u,-u-2)\) with \(u\ge-1\). If \(u\le0\), it enters \(C_3\) immediately; if \(u>0\), the subsequent diagonal image equals \(((1-a)u-2a-1,(1-a)u-2a-1)\), again in \(C_3\). Hence that quadrant contains no bounded initial orbit. On \(C_4\), a bounded point must satisfy the single affine equation \(x+ay-1=q_a\), possible only for \(1\le a<2\). On \(C_1\) and \(C_3\), the affine branch matrices have nonzero determinants \(-2a\); inverse images of points or affine lines under these branches remain points or affine lines. Iterating this observation backwards from the fixed point and (when present) the two-cycle yields a countable union of affine lines and points containing all bounded initial conditions. This union has planar Lebesgue measure zero.

**Local multipliers.** The fixed point has the eigenvalues of \(J_1\), both outside the unit circle. At the two-cycle, the two-step derivative is \(J_4J_1\) with \(J_4=\begin{pmatrix}1&a\\1&a\end{pmatrix}\); its determinant is zero and its trace is \(m_a=1+2a-a^2>1\). This supplies the stated stability types.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. It reconstructs the exact branch matrices, their characteristic polynomials, the fixed point, two-cycle, scalar-return formula and spectra; rational and floating test cases check the cone reduction. The program's finite tests illustrate, but cannot substitute for, the all-parameter/all-orbit proof above. The check run ended with `VERIFY_OK symbolic_matrices=3 exact_2cycles=4 invariant_cone_grid=1844 diagonal_returns=1000 numerical_escape_samples={1: 1000, 1.5: 1000, 2: 1000, 2.5: 1000, 3: 1000}`.

## Relationship to prior work

Tikjha's four-partition map is precisely \(T_{a,c}(x,y)=(|x|+ay-1,x+c|y|-1)\), and the 2026 paper develops its fixed points, low-period cycles, bifurcation diagrams, and a distinct singular parameter line \(c=a\). The work here gives a complete forward-orbit classification on the **opposite** singular line \(c=-a\) for every \(a\ge1\); previously described isolated periodic orbits, where applicable, are not claimed as discoveries. Published analyses of discontinuous scalar returns on \(c=a\) and of other planar border-collision maps do not imply the global no-bounded-aperiodic-orbits conclusion on \(c=-a\). Historical priority has not been independently certified.

## Limitations

The result covers only \(a\ge1\) and \(c=-a\), not nearby parameter values or \(0<a<1\). It classifies forward boundedness but not the detailed geometry of every preimage curve or asymptotic escape speed. The exceptional bounded set can be nonempty and include full line segments; it need not be finite. The computation is a consistency check, not exhaustive verification. Independent scientific review and exhaustive literature priority assessment have not been performed.

## References

1. W. Tikjha, *Noninvertibility and Bifurcation Phenomena in a Four-Partitions Piecewise Linear Map*, arXiv:2607.13519v1, first public 2026-07-15, https://arxiv.org/abs/2607.13519 . Full text: https://www.researchgate.net/publication/410158976_Noninvertibility_and_Bifurcation_Phenomena_in_a_Four-Partitions_Piecewise_Linear_Map .
2. D. J. W. Simpson, *The stability of fixed points on switching manifolds of piecewise-smooth continuous maps*, 2016; general background on piecewise-smooth planar dynamics, not a source for the present global classification.
