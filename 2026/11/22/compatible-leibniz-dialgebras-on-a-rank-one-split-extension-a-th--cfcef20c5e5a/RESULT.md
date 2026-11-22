# Compatible Leibniz dialgebras on a rank-one split extension: a three-summand classification

## Finding
Let \(K\) be a field, let \(V\) have dimension \(d\ge1\), and set \(L=V\oplus Kt\). On \(L\), fix the right Leibniz multiplication \(\dashv\) by \(v\dashv t=v\) for \(v\in V\) and all other basis-type products equal to zero. Then **all** compatible Leibniz dialgebra multiplications \(\vdash\) are
\[
 v\vdash t=P(v),\qquad t\vdash v=-E(v),\qquad V\vdash V=0,\qquad t\vdash t=0,
\]
where \(P,E:V\to V\) satisfy
\[P^2=P,\qquad E^2=E,\qquad PE=EP=0.\]
They are in canonical correspondence with ordered direct-sum decompositions
\[V=A\oplus B\oplus C,\quad A=\operatorname{im}P,\quad B=\operatorname{im}E,\quad C=\ker P\cap\ker E.\]
Two compatible products are isomorphic exactly when the ordered dimension triples \((a,b,c)=(\dim A,\dim B,\dim C)\) agree. Thus, **over every field**, the number of isomorphism types in dimension \(d+1\) is exactly \(\binom{d+2}{2}\).

For \(K=\mathbb F_q\), the number of distinct compatible bilinear products on the *fixed* vector space \(L\) with triple \((a,b,c)\) is
\[
 H_q(d;a,b,c)=\frac{|\mathrm{GL}_d(q)|}{|\mathrm{GL}_a(q)|\,|\mathrm{GL}_b(q)|\,|\mathrm{GL}_c(q)|},\qquad a+b+c=d.
\]
Consequently, writing \(N_d(q)=\sum_{a+b+c=d}H_q(d;a,b,c)\),
\[N_d(q)=\Theta_q\!\left(q^{\lfloor2d^2/3\rfloor}\right).\]
Under the uniform distribution on these labelled products, for any real \(t\ge0\),
\[
\Pr\!\left(\max\{|a-d/3|,|b-d/3|,|c-d/3|\}\ge t\right)\le C_q q^{-t^2/2},
\]
where \(C_q\) depends only on \(q\), not on \(d\).

## Assumptions and scope
The field is arbitrary for the structural classification and isomorphism theorem, including characteristic two. All vector spaces are finite-dimensional. For finite-field enumerations \(q\) is an arbitrary prime power; only those arguments use finite-field counting and asymptotics. A *Leibniz dialgebra* here means two bilinear products satisfying these **five** identities, for all \(x,y,z\in L\):
\[
\begin{aligned}
(x\dashv y)\dashv z&=(x\dashv z)\dashv y+x\dashv(y\dashv z),\\
(x\vdash y)\dashv z&=(x\dashv z)\vdash y+x\vdash(y\dashv z),\\
(x\vdash y)\vdash z&=(x\vdash z)\dashv y+x\vdash(y\vdash z),\\
x\dashv(y\dashv z)&=x\dashv(y\vdash z),\\
(x\dashv y)\vdash z&=(x\vdash y)\vdash z.
\end{aligned}
\]
These are precisely (LD1)–(LD5) of Uzakbaev's Definition 3 (reference [1]), not the associative-dialgebra identities. The scalar \(t\) is a chosen complement, not a variable or an assumption of a new unit.

## Proof
**Step 1 (forcing the support of the second product).** Write \(p:L\to V\) for the projection along \(Kt\), and \(\varepsilon:L\to K\) for the \(t\)-coordinate. Then \(x\dashv y=\varepsilon(y)p(x)\). This automatically satisfies (LD1). Since every \(y\dashv z\in V\), identity (LD4) says \(x\dashv(y\vdash z)=0\). Taking any nonzero \(x\in V\) forces \(\varepsilon(y\vdash z)=0\). Hence the entire image of \(\vdash\) lies in \(V\).

Taking \(z=t\) in (LD2) now gives
\[x\vdash y=p(x)\vdash y+x\vdash p(y).\]
If \(x,y\in V\), this identity is \(x\vdash y=2(x\vdash y)\); subtraction in any characteristic yields \(x\vdash y=0\). With \(x=y=t\), it yields \(t\vdash t=0\). There are therefore unique linear maps \(P,Q:V\to V\) such that \(v\vdash t=P(v)\) and \(t\vdash v=Q(v)\).

**Step 2 (all constraints and their sufficiency).** Substituting \((x,y,z)=(v,t,t)\) into (LD5) yields \(P^2=P\). Substituting \((t,v,t)\) into (LD5) yields \(PQ=0\). Substituting \((t,t,v)\) into (LD3) yields \(Q^2=-Q\). Substituting \((t,v,t)\) into (LD3) yields \(PQ=QP\), hence \(QP=0\). Set \(E=-Q\); then \(P^2=P\), \(E^2=E\), \(PE=EP=0\). Conversely, direct substitution of the four basic input types \((V,V),(V,t),(t,V),(t,t)\) into every (LD1)–(LD5), or multilinearity and the displayed four operator equations, proves all five identities. Thus no extra hypotheses are hidden.

**Step 3 (orbits).** Because \(PE=EP=0\), the images \(A=\operatorname{im}P\) and \(B=\operatorname{im}E\) are disjoint, and \(P+E\) is an idempotent with image \(A\oplus B\). Its kernel is \(C=\ker P\cap\ker E\), proving the direct-sum decomposition. Conversely, any ordered decomposition yields the two coordinate projections. The square span \(\operatorname{span}\{x\dashv x:x\in L\}=V\), so any automorphism \(\phi\) of the fixed \(\dashv\)-algebra preserves \(V\). Write \(\phi(t)=\lambda t+u\) with \(u\in V\). Preservation of \(v\dashv t=v\) forces \(\lambda=1\), and preservation of \(t\dashv t=0\) forces \(u=0\). Thus \(\operatorname{Aut}(L,\dashv)=\mathrm{GL}(V)\). Its conjugation action is transitive on ordered decompositions with a fixed triple, and distinct dimension triples cannot lie in the same orbit. The number of nonnegative ordered triples adding to \(d\) is \(\binom{d+2}{2}\). The stabilizer of one decomposition is \(\mathrm{GL}(A)\times\mathrm{GL}(B)\times\mathrm{GL}(C)\), proving the exact finite-field formula.

**Step 4 (growth and concentration).** Put \(G_m(q)=|\mathrm{GL}_m(q)|=q^{m^2}\prod_{i=1}^m(1-q^{-i})\), with \(G_0(q)=1\), and \(\kappa_q=\prod_{i=1}^\infty(1-q^{-i})>0\). Then
\[
\kappa_q q^{d^2-a^2-b^2-c^2}\le H_q(d;a,b,c)\le\kappa_q^{-3}q^{d^2-a^2-b^2-c^2}.
\]
The maximum exponent is \(\lfloor2d^2/3\rfloor\), attained when \(a,b,c\) differ by at most one. Let \(\delta=a-d/3\), \(\eta=b-d/3\), \(\zeta=c-d/3\). Then \(\delta+\eta+\zeta=0\) and \(d^2-a^2-b^2-c^2=2d^2/3-(\delta^2+\eta^2+\zeta^2)\). The sum of \(q^{-(\delta^2+\eta^2+\zeta^2)}\) over the two-dimensional translated integer lattice is uniformly bounded above and below by positive constants depending only on \(q\) (the lower bound uses a balanced triple). This yields the stated \(\Theta_q\) growth. On the event \(\max(|\delta|,|\eta|,|\zeta|)\ge t\), the squared norm is at least \(t^2\), so split the weight as \(q^{-\lVert\delta,\eta,\zeta\rVert^2/2}\cdot q^{-\lVert\delta,\eta,\zeta\rVert^2/2}\); bound the first factor by \(q^{-t^2/2}\), sum the second over the translated lattice, and divide by the balanced-triple lower bound. This proves the displayed uniform tail inequality.

## Verification
The included `check.py` uses standard-library Python and can be run as `python check.py`. It explicitly enumerates every pair of orthogonal idempotents in matrices over \(\mathbb F_2\) and \(\mathbb F_3\) for the indicated small dimensions and compares rank multiplicities against the independent orbit–stabilizer formula. It checks each of the five axioms on every basis triple for every classified product in the displayed finite configurations, and it enumerates all bilinear second-product structure constants for the two-dimensional underlying algebra over the two prime fields. Expected run output is embedded in `CHECK_OUTPUT.txt`; the final line is `VERIFY_OK`. These are finite corroborations only; the four-step proof supplies the infinite statements. The executable checker handles **prime fields for its sampled configurations**, while the proof covers all finite fields.

## Relationship to prior work
Uzakbaev [1], Definition 3 and Theorem 7, classifies the three-dimensional complex case, including the six \(\mathcal L_8(1)\) types corresponding to \(d=2\). It does **not** assert a classification of all dimensions, all fields, or the finite-field cardinality and concentration laws above. Kurbanbaev and Uzakbaev [2] classify three-dimensional examples with a *one*-dimensional associated annihilator, a different stratum. Foundational general definitions and constructions of Leibniz dialgebras are acknowledged; the five identities and orbit method are not claimed new. The contribution is the complete arbitrary-dimensional decomposition theorem and its exact finite-field spectrum. The six types at \(d=2\) are expressly prior art.

## Limitations
Historical novelty beyond the specifically compared sources remains provisional; broadly formulated dialgebra classifications could subsume this statement through a different language. No independent audit was performed. The asymptotic constants depend on \(q\), so the limit is for fixed field order, not uniform as \(q\) varies. The work does not classify dialgebra structures on arbitrary Leibniz algebras or deform the prescribed \(\dashv\) product.

## References
[1] N. Uzakbaev, *Classification of three-dimensional Leibniz dialgebras with two-dimensional annihilator*, arXiv:2611.00109v1 (first submitted 2026-10-27), https://arxiv.org/abs/2611.00109. In particular Definition 3, Theorem 5, Remark 6, Theorem 7 and its proof.

[2] T. Kurbanbaev and N. Uzakbaev, *Classification of three-dimensional complex Leibniz dialgebras with one-dimensional annihilator*, Uzbek Mathematical Journal 70(1) (2026), 116–125, https://doi.org/10.29229/uzmj.2026-1-12.
