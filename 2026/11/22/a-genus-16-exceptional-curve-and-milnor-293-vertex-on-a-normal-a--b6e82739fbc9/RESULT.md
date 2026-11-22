# A genus-\(16\) exceptional curve and Milnor-\(293\) vertex on a normal abelian nonic

## Finding
Let \(P=(X^3-Y^3)(Y^3-Z^3)(Z^3-X^3)\) over \(\mathbb C\). Suppose the smooth conic \(Q(X,Y,Z)=0\) avoids the twelve ordinary triple points of \(P=0\) and meets each of its nine lines transversely. On the normal degree-nine surface
\[
S_Q=\{[W:X:Y:Z]\in\mathbb P^3:W^3Q(X,Y,Z)^3=P(X,Y,Z)\},
\]
the distinguished singularity \(v=[1:0:0:0]\) has a minimal good resolution whose **entire exceptional divisor is one smooth genus-\(16\) curve** \(D'\). It satisfies
\[
(D')^2=-6,\qquad N_{D'/\widetilde S_Q}\cong\rho^*\mathcal O_{\mathbb P^1}(-2),
\]
where \(\rho:D'\to\mathbb P^1\) is a connected degree-three cyclic cover totally ramified over eighteen distinct points. The local Milnor number of \(v\) equals
\[
\boxed{\mu(S_Q,v)=293.}
\]
Moreover \(e(S_Q)=70\), and the sum of the Milnor numbers of all thirteen singularities is \(389\). The other twelve singularities, already identifiable as simple elliptic cones, each contribute Milnor number \(8\). The new geometric content is the **vertex resolution curve, its normal bundle and the vertex Milnor number**, not a new count of the other singularities.

## Assumptions and scope
All varieties and Euler characteristics are over \(\mathbb C\); \(e\) denotes topological Euler characteristic. The hypothesis on \(Q\) is a nonempty Zariski-open condition. Indeed \(Q_0=X^2+2Y^2+3Z^2\) is smooth, avoids the three coordinate and nine noncoordinate triple points, and cuts each line \(X=\zeta^aY\), \(Y=\zeta^bZ\), or \(Z=\zeta^cX\) in two simple points for \(\zeta^3=1\). At noncoordinate triple points scaled as \((\zeta^a:\zeta^b:1)\), the real part of \(Q_0\) is at least \(3/2\); the nine line restrictions are nonsingular diagonal binary quadratics. The intersection \(\{Q=0\}\cap\{P=0\}\) therefore consists of eighteen distinct smooth points of the line arrangement.

A *minimal good resolution over \(v\)* means a proper birational morphism from a smooth surface with reduced simple-normal-crossings exceptional support, with no further exceptional \((-1)\)-curve contractible over \(v\). A single smooth curve of genus \(16\) and square \(-6\) meets this definition. The local Milnor number refers to the isolated complex hypersurface germ at \(v\), not to the geometric genus of that germ.

## Proof
**1. Branch geometry and the cyclic model.** The nine components of \(P=0\) form three pencils of three lines. Their singular support consists of the three pencil centers and nine points where one line from each pencil meets, all ordinary triple crossings, with no other intersections: \(12\binom32=\binom92\). Consider
\[
\pi:V=\{T^3=P(X,Y,Z)\}\subset\mathbb P(1,1,1,3)\longrightarrow\mathbb P^2.
\]
The cover is normal and singular only above these twelve triple points, with local model \(t^3=uv(u+v)\). Each is resolved by a single blowup whose exceptional divisor is a smooth elliptic plane cubic of square \(-3\). The curve \(D=\pi^{-1}(Q=0)\) avoids these singularities. Its finite morphism \(\rho:D\to Q\simeq\mathbb P^1\) is totally ramified at each of the eighteen transverse branch intersections. The cover is connected because a local meridian has nontrivial order-three monodromy. Riemann--Hurwitz gives
\[
2g(D)-2=3(-2)+18(3-1)=30,\qquad g(D)=16.
\]

**2. The morphism and its exceptional locus.** The four sections \([T:XQ:YQ:ZQ]\) define a birational map \(V\dashrightarrow S_Q\). Its base locus consists exactly of the eighteen reduced points \(\{T=Q=0\}\subset D\). They are smooth points of \(V\), with \(T,Q\) regular local coordinates. Resolve the twelve unrelated triple-point singularities of \(V\) and blow up these eighteen points. The resulting smooth surface \(\widetilde S_Q\) maps properly and birationally to \(S_Q\). Off \(Q=0\) and the twelve triple points, the map is an isomorphism because \([X:Y:Z]\) and \(T\) are recovered on that chart. Over \(Q=0\), the proper transform \(D'\) is contracted to \(v\); each exceptional \(\mathbb P^1\) of the eighteen basepoint blowups maps *isomorphically* onto a line joining \(v\) to its distinct point \([0:X:Y:Z]\). Thus none of these eighteen curves is contracted. The twelve exceptional elliptic curves from step 1 map to the twelve other isolated singular points. Consequently the entire exceptional support over \(v\) is \(D'\) alone. As it is smooth of genus \(16\), this is the minimal good resolution over \(v\).

**3. Intersection and normal bundle.** Let \(H=\pi^*\mathcal O_{\mathbb P^2}(1)\); then \(H^2=3\) and \(D\equiv2H\), so \(D^2=12\). The vanishing divisor \(R\) of \(T|_D\) consists of the eighteen simple basepoints, and \(R\sim(3H)|_D\). Blowing up those points gives \((D')^2=12-18=-6\) and
\[
N_{D'/\widetilde S_Q}\cong\mathcal O_D(D-R)
\cong\mathcal O_D(-H)
\cong\rho^*\mathcal O_{\mathbb P^1}(-2).
\]
In particular the exceptional intersection matrix is the one-by-one matrix \((-6)\). An additional cohomological signature of this normal bundle is
\[
\rho_*\mathcal O_D\cong
\mathcal O_{\mathbb P^1}\oplus\mathcal O_{\mathbb P^1}(-6)
\oplus\mathcal O_{\mathbb P^1}(-12),
\]
whence the dimensions \(h^1(D,\mathcal O_D(-kD'))\) for \(k=0,1,2,3,4,5\) are respectively \(16,12,8,5,3,1\), and vanish for \(k\ge6\). This describes normal-bundle cohomology, not by itself all formal-neighborhood extension maps.

**4. Euler characteristic and the Milnor number.** Let \(B=\{P=0\}\subset\mathbb P^2\). By the twelve ordinary triple points,
\[
e(B)=9e(\mathbb P^1)-12(3-1)=18-24=-6.
\]
Put \(C=\{Q=0\}\), so \(e(C)=2\) and \(\#(B\cap C)=18\). Projection \(S_Q\setminus\{v\}\to\mathbb P^2\) has three-point fibers over \(\mathbb P^2\setminus(B\cup C)\), one-point fibers over \(B\setminus C\), no fibers over \(C\setminus B\), and affine-line fibers over the eighteen points \(B\cap C\). Euler additivity therefore gives
\[
\begin{aligned}
e(\mathbb P^2\setminus(B\cup C))&=3-(-6+2-18)=25,\\
e(S_Q)&=1+3(25)+(-6-18)+18=70.
\end{aligned}
\]
A smooth degree-nine surface in \(\mathbb P^3\) has Euler characteristic \(9(9^2-4\cdot9+6)=459\). For a complex surface with isolated hypersurface singularities, a smoothing changes \(e\) by the sum of local Milnor numbers (the Milnor fiber has Euler characteristic \(1+\mu\)). Thus \(\sum\mu=459-70=389\). Each of the twelve homogeneous cubic cones \(t^3=uv(u+v)\) has \(\mu=(3-1)^3=8\), since its gradient is a homogeneous regular sequence of three quadrics. Subtraction yields
\[
\mu(S_Q,v)=389-12\cdot8=293.
\]

As an independent Euler consistency check, \(e(V)=3(3-e(B))+e(B)=21\). Resolving the twelve elliptic cones changes this to \(9\), and blowing up eighteen basepoints changes it to \(27\). Replacing twelve singular points by elliptic curves and one by a genus-\(16\) curve changes Euler characteristic by \(-12+(2-32-1)=-43\), giving \(27-(-43)=70\), as above.

## Verification
The accompanying standalone `verify.py` enumerates the nine arrangement lines over \(\mathbb F_{13}\), checks all \(36\) line pairs group into twelve triple points, and checks that \(Q_0\) avoids them and is transverse to every line. It exactly recomputes the Riemann--Hurwitz and intersection arithmetic, the Euler calculations by two independent decompositions, the Milnor subtraction, and the normal-bundle cohomology sequence. It is a reproducible finite algebra/arithmetic witness; the genus, contraction and infinite-field assertions are established by the proof above and not inferred from finite-field enumerations.

## Relationship to prior work
Chen--Lazarsfeld--Moretti construct this normal degree-nine projective model and give its cyclic-cover map (Proposition A and Proposition 1.6), while their Remark 1.10 identifies its dual-Hesse branch arrangement via the classical Roulleau--Urzúa geometry. An earlier singularity calculation for the *same* nonic already determines the twelve simple elliptic singularities, the vertex multiplicity \(6\), its tangent cone and its local geometric genus \(45\). These facts do **not** determine the vertex resolution curve, its degree-three ramification and normal bundle, or its Milnor number; those are the new claims established here. The sequence \(16,12,8,5,3,1\) has sum \(45\), consistent with the previously determined vertex geometric genus, but the normal-bundle computation is not used as an unsupported substitute for the formal-cohomology proof of that earlier fact.

## Limitations
The theorem concerns this specific normal nonic and only smooth conics satisfying the stated transverse/open conditions. It does not classify exceptional parameter choices, the full analytic equivalence class or the deformation space of the vertex germ, nor does it establish a simultaneous resolution for all conics. Local Milnor number and local geometric genus are different invariants. The search for equivalent published formulations is not an absolute proof of publication priority.

## References
1. N. Chen, R. Lazarsfeld, F. Moretti, *Some normal abelian surfaces in \(\mathbb P^3\)*, arXiv:2611.09613v1, first public 2026-11-06, Proposition A, Proposition 1.6 and Remark 1.10. https://arxiv.org/html/2611.09613v1
2. X. Roulleau, G. Urzúa, *Chern slopes of simply connected complex surfaces of general type are dense in \([2,3]\)*, Annals of Mathematics 182 (2015), 287--306, especially the classical dual-Hesse arrangement. https://doi.org/10.4007/annals.2015.182.1.6
