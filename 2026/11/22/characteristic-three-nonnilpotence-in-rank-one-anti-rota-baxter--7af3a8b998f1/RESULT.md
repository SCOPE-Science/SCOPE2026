# Characteristic-three nonnilpotence in rank-one anti–Rota–Baxter maps on matrix algebras

## Finding

Let \(k\) be any field, let \(n\ge 2\), and let \(A=M_n(k)\). Classify all nonzero linear operators \(R:A\to A\) of linear rank one satisfying the anti–Rota–Baxter identity
\[
R(X)R(Y)=-R\bigl(R(X)Y+XR(Y)\bigr)\qquad(X,Y\in A).
\]
Write \(R(X)=\operatorname{tr}(VX)U\) with \(U,V\in A\) nonzero. Every solution belongs uniquely to exactly one of these types, up to the scalar ambiguity \((U,V)\sim(cU,c^{-1}V)\):

1. **Square-zero image:** \(U^2=0\) and \(UV=VU=0\). This type exists in every characteristic and all of its operators are strong anti–Rota–Baxter operators, meaning \(R(X)R(Y)Z=XR(Y)R(Z)\) for all \(X,Y,Z\).
2. **Idempotent image in characteristic two:** after normalizing \(U=E\) with \(E^2=E\ne0\), either \(V=EV(I-E)\ne0\) or \(V=(I-E)VE\ne0\). These operators are not strong.
3. **Idempotent image in characteristic three:** after normalizing \(U=E\) with \(E^2=E\ne0\), \(V=EVE\ne0\). These operators are not strong, and satisfy \(R^2=\operatorname{tr}(V)R\). In particular \(R^2\ne0\) occurs exactly in characteristic three.

For a finite field \(k=\mathbb F_q\) of characteristic \(p\), define the Gaussian binomial coefficient \({n\brack r}_q\), and \(g_s(q)=\lvert\mathrm{GL}_s(\mathbb F_q)\rvert=\prod_{i=0}^{s-1}(q^s-q^i)\). Define
\[
S_n(q)=\sum_{s=1}^{\lfloor n/2\rfloor}
{n\brack s}_q {n-s\brack s}_q\frac{g_s(q)}{q-1}\bigl(q^{(n-s)^2}-1\bigr),
\]
\[
T_n^{(2)}(q)=2\sum_{r=1}^{n-1}{n\brack r}_q q^{r(n-r)}\bigl(q^{r(n-r)}-1\bigr),
\]
\[
T_n^{(3)}(q)=\sum_{r=1}^{n}{n\brack r}_q q^{r(n-r)}\bigl(q^{r^2}-1\bigr).
\]
The **exact number of nonzero linear-rank-one anti–Rota–Baxter operators** is
\[
\boxed{S_n(q)+\mathbf1_{p=2}T_n^{(2)}(q)+\mathbf1_{p=3}T_n^{(3)}(q).}
\]
The number of strong operators is exactly \(S_n(q)\). In characteristic three, for every specified \(\beta\in\mathbb F_q^\times\), the number with \(R^2=\beta R\) is
\[
\boxed{B_n(q)=\sum_{r=1}^{n}{n\brack r}_q q^{r(n-r)+r^2-1}.}
\]
Consequently \((q-1)B_n(q)\) of the maps have nonzero square, and exactly \(B_n(q)\) are composition-idempotent \(R^2=R\). All counts are of distinct labeled operators, not conjugacy classes, and exclude the zero map.

## Assumptions and scope

The operator identity is the *anti* identity, with the minus sign above; it is not the usual weight-zero Rota–Baxter identity. No strongness condition is imposed for the primary classification. The algebra is the unital full matrix algebra, with \(n\ge2\); all characteristics and nonprime finite fields are included. Operator rank means rank as a linear map on the \(n^2\)-dimensional vector space \(A\); the matrix ranks of \(U\) and \(E\) are denoted \(s\) and \(r\), respectively. The ordinary matrix trace gives a nondegenerate pairing over *every* field, without restrictions on \(p\mid n\).

## Proof

**Reduction to proportional multiplication functionals.** Because \(R\) has linear rank one, write \(R(X)=\varphi(X)U\) for \(0\ne U\in A\), \(0\ne\varphi\in A^*\). Trace nondegeneracy yields the unique \(V\in A\) with \(\varphi(X)=\operatorname{tr}(VX)\). Substitution into the defining identity gives
\[
\varphi(X)\varphi(Y)U^2
=-\bigl(\varphi(X)\varphi(UY)+\varphi(Y)\varphi(XU)\bigr)U.
\]
Choosing \(X,Y\) with \(\varphi(X)=\varphi(Y)=1\) shows \(U^2=\lambda U\) for some \(\lambda\in k\). Holding one of \(X,Y\) in \(\ker\varphi\) shows that \(Y\mapsto\varphi(UY)\) and \(X\mapsto\varphi(XU)\) both vanish on \(\ker\varphi\). Thus there are scalars \(a,b\in k\) with
\[
\varphi(UY)=a\varphi(Y),\quad\varphi(XU)=b\varphi(X),\quad \lambda+a+b=0.
\]
Using cyclicity and nondegeneracy of trace, the two proportionalities are equivalent to \(VU=aV\) and \(UV=bV\), respectively. They are also sufficient for the original identity.

**Square-zero branch.** If \(\lambda=0\), then \(U^2=0\). From \(VU=aV\), multiplication by \(U\) on the right yields \(0=a^2V\), hence \(a=0\); similarly \(b=0\). Thus \(UV=VU=0\). Conversely these identities imply the anti–Rota–Baxter identity. As \(R(X)R(Y)\) and \(R(Y)R(Z)\) are zero, strongness follows. Moreover \(R^2(X)=\operatorname{tr}(VU)R(X)=0\).

**Quasi-idempotent branch.** If \(\lambda\ne0\), set \(E=\lambda^{-1}U\), and absorb \(\lambda\) into the representing functional to write the same map as \(R(X)=\operatorname{tr}(V'X)E\) with \(E^2=E\ne0\). Now \(V'E=\alpha V'\), \(EV'=\beta V'\), \(1+\alpha+\beta=0\). Since \(E^2=E\) and \(V'\ne0\), each of \(\alpha,\beta\) lies in \(\{0,1\}\). For characteristic two the two solutions are \((\alpha,\beta)=(1,0),(0,1)\), giving the two off-diagonal corners; for characteristic three the unique solution is \((1,1)\), giving \(V'=EV'E\). In all other characteristics no solution exists. A nonzero idempotent matrix is the unique idempotent generator of its image line, so the three families and every normalized pair \((E,V')\) are counted exactly once.

**Strongness.** The square-zero family was handled above. Suppose the image line has a nonzero idempotent \(E\). If the strong identity held, then choosing \(Y,Z\) with \(\varphi(Y)=\varphi(Z)=1\) and any \(X\in\ker\varphi\) would imply \(XE=0\). Thus \(\ker\varphi\subseteq\ker(X\mapsto XE)\). The left kernel has codimension one, but right multiplication by \(E\) has rank \(n\operatorname{rank}(E)\ge2\), a contradiction. Hence no idempotent-image operator is strong.

**Square-zero enumeration.** Fix \(s=\operatorname{rank}U\), \(1\le s\le\lfloor n/2\rfloor\). An endomorphism \(U\) with \(U^2=0\) and rank \(s\) is specified by its image \(W\) (\(s\)-plane), its kernel \(K\supset W\) (\((n-s)\)-plane), and an isomorphism \(k^n/K\to W\). This gives \({n\brack s}_q{n-s\brack s}_q g_s(q)\) nonzero matrices. Dividing by \(q-1\) counts output lines. For a fixed representative \(U\), the conditions \(VU=UV=0\) say \(V\) induces an arbitrary map \(k^n/W\to K\), a vector space of dimension \((n-s)^2\); remove the zero map. This gives \(S_n(q)\).

**Idempotent enumeration.** Rank-\(r\) idempotents \(E\) correspond bijectively to ordered decompositions \(k^n=\operatorname{im}E\oplus\ker E\), of which there are \({n\brack r}_q q^{r(n-r)}\). When \(p=2\), the two disjoint nonzero off-diagonal corners each have dimension \(r(n-r)\), and are nonempty only when \(1\le r<n\), giving \(T_n^{(2)}(q)\). When \(p=3\), the nonzero corner \(EM_n(k)E\simeq M_r(k)\) contributes \(q^{r^2}-1\), giving \(T_n^{(3)}(q)\).

**Composition square in characteristic three.** For normalized \(R(X)=\operatorname{tr}(VX)E\), \(R^2=\operatorname{tr}(VE)R\), and \(VE=V\), so the scalar is \(\operatorname{tr}(V)\). The trace map on \(M_r(\mathbb F_q)\) is surjective, with fibers of cardinality \(q^{r^2-1}\) even when \(p\mid r\), because individual diagonal matrix units have trace one. For a prescribed nonzero scalar this yields the formula for \(B_n(q)\). No other branch can give a nonzero composition square. This completes the classification and all counts.

## Verification

The standalone \(\texttt{verify.py}\) checks the **original bilinear operator identity on every ordered pair of matrix units**, independently of the trace-eigenvalue reduction, then compares against the normal forms and exact counts. It exhausts all nonzero factor pairs \((U,V)\) for \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), and \(M_2(\mathbb F_5)\), quotienting duplicate operator matrices. It also tests every canonical allowed factor pair in \(M_3(\mathbb F_2)\) against the original identity. Results (nonzero operators) are: \(15\) for \((n,q)=(2,2)\), \(112\) for \((2,3)\), \(24\) for \((2,5)\), and \(651\) for \((3,2)\). For \((2,3)\), exactly \(78\) have \(R^2\ne0\), and exactly \(39\) satisfy \(R^2=R\). The infinite-family theorem is proved symbolically above; these finite checks do not prove it by exhaustion.

Reproduce from an extracted package by running \(\texttt{python verify.py}\) with Python 3.11 or later; it requires only the standard library.

## Relationship to prior work

Gao–Liu–Bai [1] introduced the anti–Rota–Baxter identity and its stronger condition in their Definitions 2.15 and equation (23), working in characteristic zero. Their structural work motivates examining which anti-operators extend to positive-characteristic matrix algebras. Ordinary weight-zero Rota–Baxter operators, studied for full matrix algebras by Gubarev [2], satisfy the *opposite sign* and do not imply the present characteristic-three branch. Existing finite-field **ordinary** rank-one matrix-algebra Rota–Baxter classifications [3,4] cover a related, but different, identity: the square-zero and characteristic-two branches agree with ordinary results, while the characteristic-three \(EVE\) branch does not follow from that identity. The positive-characteristic dual-number anti–Rota–Baxter example [5] concerns a different commutative algebra. The full-rank-one trace calculation and characteristic-three nonnilpotence were not found in the inspected sources; this is a statement of the scope of inspection, not a proof of publication priority.

## Limitations

The result concerns only **linear rank-one** maps; it does not classify anti–Rota–Baxter operators of higher operator rank. The eigenvalue and counting arguments are exact for all specified fields and dimensions, but not independently audited. Prior publication searches cannot establish global novelty; some relevant ordinary Rota–Baxter published records were available only through indexed summaries, without source full text. The full matrix-algebra and anti–Rota–Baxter literature remains a residual priority risk. Strongness refers strictly to the additional identity from [1], not to invertibility or operator idempotence.

## References

[1] D. Gao, G. Liu and C. Bai, *Anti-dendriform algebras, new splitting of operations and Novikov type algebras*, arXiv:2209.08962, initially public 2022-09-19, https://arxiv.org/abs/2209.08962 (Section 2.2, Definitions 2.15 and 2.19).

[2] V. Gubarev, *Rota-Baxter operators on unital algebras*, arXiv:1805.00723, initially public 2018-05-02, https://arxiv.org/abs/1805.00723.

[3] *Rank-one Rota–Baxter operators on full matrix algebras: two matrix types and an exact finite-field census*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-rank-one-rota-baxter-operators-on-full-matrix-algebras-two-matri--dc84c4776379 (indexed scientific synopsis consulted; full document not inspected).

[4] *An exact rank-one Rota–Baxter census for full matrix algebras over finite fields*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-an-exact-rank-one-rota-baxter-census-for-full-matrix-algebras-ov--c47da0cfa606 (indexed scientific synopsis consulted; full document not inspected).

[5] *Characteristic-three phase transition for anti-Rota–Baxter operators on the dual numbers*, public research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/13/SCOPE-characteristic-three-phase-transition-for-anti-rota-baxter-opera--810eb43c0979 (indexed scientific synopsis consulted).
