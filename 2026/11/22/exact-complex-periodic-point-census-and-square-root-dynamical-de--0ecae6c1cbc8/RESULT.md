# Exact complex periodic-point census and square-root dynamical degree in a quadratic delay map

## Finding

For the polynomial plane map
\[
F_{a,b}(x,y)=\left(ax+\frac32y,\,bx(1-x)\right),\qquad b\ne0,
\]
there is a complete **complex** all-period intersection census even though the real dynamics may undergo bifurcations. For every integer \(n\ge1\), the scheme of complex affine fixed points of \(F_{a,b}^{n}\) is finite and has total local intersection multiplicity exactly \(2^n\). The equality holds for every complex \(a\) and every nonzero complex \(b\); in particular it holds throughout the source's real domain \(ab\ne0\).

The exact iterate degrees and dynamical degrees are
\[
\deg(F_{a,b}^n)=2^{\lceil n/2\rceil},\qquad
\lambda_1(F_{a,b})=\sqrt2,\qquad \lambda_2(F_{a,b})=2.
\]

For every fixed \(n\), outside a proper algebraic subset of the parameter plane, all \(2^n\) complex fixed points are simple. The simultaneous complement of the countably many exceptional subsets is dense and of full planar Lebesgue measure among real \((a,b)\) with \(ab\ne0\). For these simultaneous-generic parameters, the **distinct complex** primitive-period point and orbit counts are
\[
P_n=\sum_{d\mid n}\mu(n/d)2^d,
\qquad C_n=\frac1n\sum_{d\mid n}\mu(n/d)2^d.
\]
The resulting complex Artin--Mazur zeta function is \(\zeta_F(t)=(1-2t)^{-1}\). For any exceptional parameter, the same rational formula applies only to the *multiplicity-weighted* generating function; it is not asserted for the distinct-point zeta function.

## Assumptions and scope

The state space in the periodic-point theorem is \(\mathbb C^2\), not a bounded real invariant region. All multiplicities are local complex algebraic intersection multiplicities of the two coordinate equations for \(F_{a,b}^{n}(x,y)=(x,y)\), in the affine plane. Parameters may be real or complex; the sole essential condition is \(b\ne0\). The zero-drift value \(a=0\), outside the motivating paper's stated domain, is used solely as a legitimate auxiliary parameter for proving generic simplicity and is not claimed to be an allowed parameter in that paper. For generic simplicity at every \(n\), “generic” means a countable intersection of dense Zariski-open real-parameter sets, not one uniform Zariski-open set for all periods.

## Proof

**1. Companion form.** Let \(u=x\), \(v=ax+\frac32y\), and \(c=\frac32b\ne0\). This is an invertible linear coordinate change for all \(a\), and conjugates the map to
\[
G_{a,c}(u,v)=\left(v,\,a v+c u(1-u)\right).
\]
Write \(p_0(u,v)=u\), \(p_1(u,v)=v\) and
\[
p_{j+2}=a p_{j+1}+c p_j(1-p_j),\qquad j\ge0.
\]
Then \(G_{a,c}^n(u,v)=(p_n,p_{n+1})\) for every integer \(n\ge0\).

**2. Leading forms and degree growth.** Set \(D_m=2^m\) and \(k_m=(-c)^{D_m-1}\), for \(m\ge0\). We claim by induction that \(p_{2m}\) and \(p_{2m+1}\) both have exact total degree \(D_m\), that the highest homogeneous form of \(p_{2m}\) equals \(k_m u^{D_m}\), and that the highest homogeneous form \(H_m\) of \(p_{2m+1}\) obeys \(H_m(0,v)=k_m v^{D_m}\). At \(m=0\), these assertions are \(p_0=u\), \(p_1=v\). The quadratic term in \(p_{2m+2}\) has degree \(2D_m\), strictly exceeding that of its linear predecessor, and gives leading form \(-c k_m^2u^{2D_m}=k_{m+1}u^{D_{m+1}}\). In \(p_{2m+3}\) the two possible highest-degree contributions have the common degree \(D_{m+1}\). Restriction to \(u=0\) kills the one from \(a p_{2m+2}\), leaving \(-c H_m(0,v)^2=k_{m+1}v^{D_{m+1}}\ne0\). This proves both the odd-degree assertion and the induction. As the highest degree of \(G^n\) is that of \(p_{n+1}\), we obtain \(\deg G^n=2^{\lceil n/2\rceil}\) and hence \(\lambda_1=\lim_{n\to\infty}(\deg G^n)^{1/n}=\sqrt2\). Each generic target \((U,V)\) has exactly two preimages, by setting \(v=U\) and solving \(c u(1-u)=V-aU\). Thus the topological degree \(\lambda_2=2\).

**3. No periodic intersections at infinity.** The fixed-point equations are
\[
p_n(u,v)-u=0,\qquad p_{n+1}(u,v)-v=0.
\]
For even \(n=2m\), the leading form of the first equation is \(k_m u^{D_m}\), whose only projective zero at infinity has \(u=0\); the second leading form is \(H_m\), and \(H_m(0,v)=k_m v^{D_m}\ne0\) for \(v\ne0\). For odd \(n=2m+1\), the second leading form is \(k_{m+1}u^{D_{m+1}}\) while the first restricts at \(u=0\) to \(k_m v^{D_m}\ne0\). Therefore in either parity the homogeneous projective closures have **no common point on the line at infinity**, and hence no common curve component. Bézout's theorem applies to two projective plane curves whose degrees are respectively \((2^m,2^m)\) for even \(n=2m\), and \((2^m,2^{m+1})\) for odd \(n=2m+1\). All their intersections lie in the affine plane and their total local intersection multiplicity equals \(2^n\). In particular, the affine fixed-point scheme is zero-dimensional and finite, without relying on any finite numerical enumeration.

**4. Generic simplicity for all periods.** For every fixed \(n\), nonsimplicity is characterized by the simultaneous equations \(p_n-u=p_{n+1}-v=0\) and \(\det(I-DG^n)=0\). Because the fixed-point family above is finite with no intersections at infinity for all \(c\ne0\), the discriminant is algebraic in the parameters and its exceptional locus is Zariski closed (equivalently, eliminate \(u,v\) from the projective incidence equations). To show it is a **proper** locus, use the auxiliary parameters \(a=0\), \(c=4\), where \(G(u,v)=(v,L(u))\) with \(L(t)=4t(1-t)\). The change \(z=1-2t\) conjugates \(L\) to the degree-two Chebyshev polynomial \(T_2(z)=2z^2-1\). For every \(j\ge1\), each root of \(L^j(t)=t\) is simple: after writing \(z=(w+w^{-1})/2\), the fixed equation factors into \(w^{2^j-1}=1\) or \(w^{2^j+1}=1\); at nonendpoint roots the derivative of \(T_{2^j}\) is \(\pm2^j\), and at the two possible endpoints its derivative has magnitude \(2^{2j}\), never \(1\).

For even \(n=2j\), \(G^{2j}(u,v)=(L^j(u),L^j(v))\), so its fixed points are products of simple scalar fixed points and \(\det(I-DG^{2j})\ne0\) there. For odd \(n=2j+1\), \(G^{2j+1}(u,v)=(L^j(v),L^{j+1}(u))\); its fixed points correspond bijectively to roots of \(L^{2j+1}(u)=u\), with \(v=L^{j+1}(u)\), and \(\det(I-DG^{2j+1})=1-(L^{2j+1})'(u)\ne0\). The witness therefore proves properness for every \(n\), and its exceptional subset remains proper on the open domain \(a c\ne0\). The complement of the countable union of proper real algebraic sets is dense and has full two-dimensional Lebesgue measure. For every such parameter, all complex points fixed by every iterate are simple, so the actual counts equal the intersection counts \(2^n\).

**5. Primitive counts and zeta.** For simultaneously simple parameters, the exact-period partition of \(\operatorname{Fix}(F^n)\) gives \(2^n=\sum_{d\mid n}P_d\). Möbius inversion yields the displayed \(P_n\) and \(C_n=P_n/n\). By the formal identity \(\sum_{n\ge1}2^n t^n/n=-\log(1-2t)\), the Artin--Mazur zeta is \((1-2t)^{-1}\). For arbitrary parameters, define the multiplicity-weighted zeta directly from the locally counted fixed schemes; the same identity holds but the distinct-period Möbius formula need not.

## Verification

The companion conjugacy and induction are symbolic identities for every \(n\), verified in the proof. The supplied independent finite algebra checker `checker.py` reproduces all odd/even leading-form and degree-product identities for \(1\le n\le7\) at \(a=1/3,c=2\), including the crucial absence of a shared direction at infinity. It also checks exact squarefreeness of \(L^j(t)-t\) for \(1\le j\le6\). These tests support implementation fidelity only; the infinite all-period result follows from the analytic/algebraic induction and Bézout's theorem, not from finite tests. Run using `python checker.py` with Python and SymPy installed.

## Relationship to prior work

Liu and Zhong's 2024 article introduced this precise two-parameter quadratic map and studied fixed-point stability and local Naimark–Sacker, transcritical, and flip bifurcations, with numerical observations. The theorem here is an all-period count over the **complex affine plane**, not a reinterpretation of their real fixed-point stability calculations. The standard Bézout theorem and Chebyshev conjugacy are used as classical tools. General work on polynomial endomorphism dynamical degrees and the known all-period counts of holomorphic **projective-space** self-maps give context but do not directly yield the asserted target-map affine count: the present map is not a holomorphic quadratic endomorphism of \(\mathbb P^2\), and its iterate degrees are not \(2^n\). This work makes no claim to a new general theorem about every polynomial plane endomorphism.

## Limitations

The theorem counts complex periodic solutions, not real periodic orbits or attractors; the complex count is compatible with arbitrary changes in real stability and bifurcations. The auxiliary simple-witness parameter \(a=0\) is outside the original article's \(a\ne0\) domain and is used only in a polynomial parameter-continuation argument. The common simultaneous-simple parameter set has full real Lebesgue measure but is not asserted to contain a nonempty Zariski-open set independent of \(n\). No explicit complete enumeration of the exceptional parameter curves is given. More general polynomial-map literature might imply related fixed-point formulas; no independent publication-priority certification is claimed.

## References

1. L. Liu and X. Zhong, *Research on Stability and Bifurcation for Two-Dimensional Two-Parameter Squared Discrete Dynamical Systems*, Mathematics **12** (2024), article 2423, first publicly dated 4 August 2024, DOI: https://doi.org/10.3390/math12152423 ; full open text: https://www.mdpi.com/2227-7390/12/15/2423 .
2. Bézout's theorem for two projective plane curves without a common component (standard algebraic-geometric intersection theorem).
3. Chebyshev polynomial identity \(T_d((w+w^{-1})/2)=(w^d+w^{-d})/2\) (classical formula).
4. General contextual discussion of dynamical degrees for Hénon-like and polynomial-like maps: https://doi.org/10.1090/tran/9225 . The listed paper is not taken to assert the present fixed-point count.
