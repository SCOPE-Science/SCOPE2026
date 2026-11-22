# Resonant period-two manifolds and sharp transverse attraction in a quadratic three-map

## Finding

A normalized quadratic three-dimensional diffeomorphism can have an *entire real line* of primitive two-periodic points, even though the generic coefficients yield at most one primitive two-cycle. On this resonant line, normal attraction need not be all-or-nothing: an exact finite band is normally attracting while the outer tails are transversely unstable.

For the concrete quadratic diffeomorphism
\[
L(x,y,z)=\left(\frac z4+\frac{5y}4+\frac{x^2+xy}2,x,y\right),
\]
the complete nontrivial period-two set is
\[
(u,-u,u)\longleftrightarrow(-u,u,-u),\qquad u\in\mathbb R\setminus\{0\}.
\]
Every such two-cycle has the full return spectrum
\[
\left\{1,\lambda_+(u),\lambda_-(u)\right\},\quad
\lambda^2-\left(\frac32-\frac{u^2}4\right)\lambda+\frac1{16}=0.
\]
Its two normal multipliers have modulus strictly less than \(1\) **if and only if**
\[
\boxed{\frac74<u^2<\frac{41}4}.
\]
At the inner endpoint one normal multiplier equals \(+1\); at the outer endpoint one equals \(-1\). Compact subarcs strictly inside the band are normally attracting invariant sets of the second iterate, whereas sufficiently small nonzero points and the large-amplitude tails have a transverse unstable direction.

## Assumptions and scope

Work over the real numbers with the five-independent-parameter normalized companion family
\[
L(x,y,z)=\bigl(\delta z+\alpha-\sigma y+Q(x,y),x,y\bigr),
\quad Q(x,y)=a x^2+bxy+c y^2,
\]
subject to \(a+b+c=1\) and \(\delta\ne0\). The latter guarantees a globally invertible polynomial map. Here \(a,b,c,\alpha,\sigma,\delta\) are fixed real parameters, and a primitive two-cycle consists of exactly two distinct real points exchanged by \(L\). No restriction to a trapping box or anti-integrable limit is imposed. Let
\[
S=1+\sigma-\delta,\quad B=1+\sigma+\delta,\quad d=a-c,\quad e=b-a-c=2b-1.
\]

## Proof

**1. Exhaustive reduction.** For a two-periodic scalar sequence taking alternating values \(u,v\), the companion-state points must be \((u,v,u)\) and \((v,u,v)\). Their exchanges are equivalent to
\[
(1+\sigma)v-\delta u=\alpha+Q(u,v),\qquad
(1+\sigma)u-\delta v=\alpha+Q(v,u).
\]
Subtracting and adding respectively give, exactly,
\[
(v-u)\bigl(B+d(u+v)\bigr)=0,\qquad
S(u+v)=2\alpha+(a+c)(u+v)^2+2euv.\tag{1}
\]
Conversely both identities together imply the original exchange equations. In every primitive cycle \(u\ne v\), so \(B+d(u+v)=0\). This reduction is necessary and sufficient, not merely a search ansatz.

**2. Complete real census.** If \(d\ne0\) and \(e\ne0\), put
\[
t=-B/d,\qquad h=\frac{St-2\alpha-(a+c)t^2}{2e},\qquad \Delta=t^2-4h.
\]
Then exactly one primitive two-cycle exists up to cyclic permutation when \(\Delta>0\), namely \(u,v=(t\pm\sqrt\Delta)/2\); none exists when \(\Delta\le0\). If \(d\ne0\) and \(e=0\), the sum equation becomes independent of the difference, and infinitely many primitive two-cycles exist **exactly when**
\[
\alpha=\frac{St}2-\frac{t^2}4,\qquad t=-B/d.
\]
Their states are \((u,t-u,u)\leftrightarrow(t-u,u,t-u)\), with \(u\ne t/2\). Off that resonance there are none. If \(d=0\) and \(B\ne0\), no primitive two-cycle exists. Finally, if \(d=B=0\), write \(t=u+v\) and \(w=u-v\ne0\). Since \(a=c\) and \(a+b+c=1\), the complete condition is
\[
e w^2=t^2-2St+4\alpha.\tag{2}
\]
This has a real solution with \(w\ne0\) for every \(\alpha\) if \(e>0\), exactly when \(\alpha\le S^2/4\) if \(e=0\), and exactly when \(\alpha<S^2/4\) if \(e<0\). In any of these nonempty cases a continuum of primitive two-cycles exists, parameterized by equation (2). These four alternatives exhaust all parameter choices and all real primitive two-cycles.

**3. Resonant example and transverse spectrum.** Choose
\[
(a,b,c,\delta,\sigma,\alpha)=\left(\frac12,\frac12,0,\frac14,-\frac54,0\right).
\]
Here \(d=1/2\), \(e=0\), \(B=0\) and \(t=0\). Direct substitution yields \(L(u,-u,u)=(-u,u,-u)\), and vice versa; Step 2 proves there are no other primitive two-cycles. The one-step derivative is
\[
DL(x,y,z)=\begin{pmatrix}2ax+by & bx+2cy-\sigma & \delta\\1&0&0\\0&1&0\end{pmatrix}.
\]
The exact two-step matrix \(P(u)=DL(-u,u,-u)DL(u,-u,u)\) has characteristic polynomial
\[
\det(\lambda I-P(u))=(\lambda-1)\left[\lambda^2-\left(\frac32-\frac{u^2}4\right)\lambda+\frac1{16}\right].\tag{3}
\]
The \(1\)-eigenvector is tangent to the fixed curve of \(L^2\). Let \(T=3/2-u^2/4\). For the remaining quadratic \(\lambda^2-T\lambda+1/16\), the exact real quadratic Schur inequalities are \(1/16<1\), \(1-T+1/16>0\), and \(1+T+1/16>0\), equivalently \(-17/16<T<17/16\). Solving gives precisely \(7/4<u^2<41/4\). At the endpoints the transverse characteristic polynomial has a factor \(\lambda-1\) or \(\lambda+1\), respectively. Outside the closed interval the quadratic takes a negative value at one of \(\lambda=\pm1\), so there is a real multiplier beyond the unit circle. The local normal-attraction assertion on compact interior subarcs follows from the standard normally attracting invariant-manifold contraction argument applied to the smooth curve of fixed points of \(L^2\), with both normal multipliers uniformly smaller than one there.

## Verification

The accompanying standalone \`checks/check_period_two.py\` uses exact SymPy algebra to test both identities (1) symbolically, evaluate 160 rational coefficient cases, and rederive (3) for 43 explicit cycle amplitudes. It prints PASS on completion. These computations check the derivation; the necessity, sufficiency and inequalities in the proof do not depend on finite sampling. A direct calculation also gives \(\det DL=\delta\) and \(\det P=\delta^2=1/16\), consistent with equation (3).

## Relationship to prior work

Hampton and Meiss (2022, arXiv:2107.09776, §3) identify period-two families of the *singular anti-integrable correspondence*, particularly when the quadratic coefficients satisfy \(a=c\). Their 2023 continuation study (arXiv:2305.06302, §§1, 5) studies the **finite** quadratic diffeomorphism and numerical low-period bifurcations. The present result concerns an exact finite-parameter resonance with \(a\ne c\), \(b=1/2\), and an amplitude-dependent *normal stability interval*; neither follows from the anti-integrable period-two statement. A publicly indexed result titled “Two-parameter Floquet rigidity and a sharp two-cycle sink window in a three-dimensional quadratic map” reports a generic isolated-cycle discriminant and stability law; that generic component is not asserted here as the novelty. Its complete text could not be inspected, so possible coverage of some nongeneric cases remains a priority limitation. The motivation and novelty claim here center on the finite-parameter period-two manifold and its sharp normal stability boundaries.

## Limitations

The result concerns only real primitive period-two points of the specified normalized family. It does not classify higher periods, global basins, or dynamics near the nonhyperbolic normal thresholds. Normal attraction describes contraction transverse to a *continuum* of cycles, not exponential convergence to a preselected phase point on that continuum. Mathematical priority should be reassessed if complete versions of relevant indexed statements become available. Independent review is not claimed.

## References

1. A. E. Hampton and J. D. Meiss, *Anti-Integrability for Three-Dimensional Quadratic Maps*, SIAM J. Applied Dynamical Systems 21 (2022), 650–675, arXiv:2107.09776, https://arxiv.org/abs/2107.09776, DOI 10.1137/21M1433289.
2. A. E. Hampton and J. D. Meiss, *Connecting Anti-integrability to Attractors for Three-Dimensional Quadratic Diffeomorphisms*, arXiv:2305.06302 (first submitted 2023-05-10), SIAM J. Applied Dynamical Systems 23 (2024), 616–640, https://arxiv.org/abs/2305.06302, DOI 10.1137/23M1571897.
3. “Two-parameter Floquet rigidity and a sharp two-cycle sink window in a three-dimensional quadratic map”, available published finding summary, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-two-parameter-floquet-rigidity-and-a-sharp-two-cycle-sink-window--9d694fa2e0cd. Full text not accessible at inspection.
