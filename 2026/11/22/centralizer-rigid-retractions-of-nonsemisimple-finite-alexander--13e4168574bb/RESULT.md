# Centralizer-rigid retractions of nonsemisimple finite Alexander quandles

## Finding
Let \(p\ge3\) be prime, \(d\ge2\) and \(m\ge1\) integers, and \(\lambda\in\mathbb F_p\setminus\{0,1\}\). Let
\[
R=\mathbb F_p[\varepsilon]/(\varepsilon^d),\qquad M=R^m,
\qquad T(x)=(\lambda+\varepsilon)x.
\]
Put \(Q=(M,*)\), the connected Alexander quandle with \(x*y=Tx+(1-T)y\). An endomorphism is a set map preserving this operation, not presumed linear. Let \(\mathcal E\) be its composition-idempotent endomorphisms, and let \(\operatorname{Cent}(f)=\{g\in\operatorname{End}(Q):gf=fg\}\), **including noninvertible maps**. Define the Gaussian binomial coefficient
\[
{m\brack r}_p=\prod_{j=0}^{r-1}\frac{p^{m-j}-1}{p^{r-j}-1}.
\]

**Theorem.** The \(\operatorname{Aut}(Q)\)-conjugacy classes of \(\mathcal E\) are exactly the \(m+1\) classes indexed by \(0\le r\le m\), with representatives the coordinate projections \(P_r:R^r\oplus R^{m-r}\to R^r\), and respective cardinalities
\[
\boxed{N_r=p^{d(m-r)+(2d-1)r(m-r)}{m\brack r}_p.}
\]
Every member of class \(r\) has image cardinality \(p^{dr}\) and exactly
\[
\boxed{Z_r=p^{d(r^2+(m-r)^2+r)}}
\]
commuting quandle endomorphisms. These \(m+1\) centralizer cardinalities are pairwise distinct. Consequently, **two quandle retractions are automorphism-conjugate if and only if their full composition-centralizers have the same cardinality**, and the complete centralizer-size spectrum is the list \((N_r,Z_r)\) above. In particular,
\[
\#\{(f,g):f\in\mathcal E,\ g\in\operatorname{End}(Q),\ fg=gf\}
=\sum_{r=0}^mN_rZ_r.
\]

The hypothesis that all Jordan blocks have the same length is structural: for the connected Alexander quandle on \(R_2\oplus\mathbb F_p^2\), where \(R_2=\mathbb F_p[\varepsilon]/(\varepsilon^2)\), \(T=\lambda+\varepsilon\) on \(R_2\) and \(T=\lambda\) on the other summands, projections onto \(R_2\) and onto \(\mathbb F_p^2\) are **not** conjugate, yet both have image cardinality \(p^2\) and exactly \(p^8\) commuting endomorphisms.

## Assumptions and scope
The quandle operation acts on the additive elementary-abelian \(p\)-group underlying \(M\). The scalar \(\lambda\ne0,1\) makes \(T\) and \(1-T\) invertible (they have invertible constant coefficients in \(R\)); hence the quandle is connected and latin. Since \(d\ge2\), multiplication by \(T\) on the \(\mathbb F_p\)-space \(M\) has nontrivial Jordan blocks and is **not semisimple**. The variable \(m\) is the multiplicity of an equal-length Jordan block, not the dimension of \(M\), which is \(dm\) over \(\mathbb F_p\). The counts are of labeled maps, and conjugacy uses the **full quandle automorphism group**. The boundary example uses the mixed-length primary module \(R_2\oplus R_1^2\), with \(R_1=\mathbb F_p\).

## Proof
**1. Every quandle endomorphism is affine.** Let \(f:Q\to Q\) preserve \(*\), set \(b=f(0)\), and \(h=f-b\). A translation preserves the Alexander operation, so \(h\) also preserves \(*\) and \(h(0)=0\). The identities \(x*0=Tx\) and \(0*y=(1-T)y\) give
\[
h(Tx)=Th(x),\qquad h((1-T)y)=(1-T)h(y).
\]
For any \(a,b'\in M\), choose \(x=T^{-1}a\) and \(y=(1-T)^{-1}b'\). Since \(x*y=a+b'\), the preservation identity implies \(h(a+b')=h(a)+h(b')\). Hence \(h\) is additive, thus \(\mathbb F_p\)-linear, and commutes with \(T\). It also commutes with \(\varepsilon=T-\lambda I\), hence is \(R\)-linear. Conversely, every \(f(x)=Ax+b\) with \(A\in M_m(R)\), \(b\in M\), preserves \(*\). Its composition law is
\[
(A,b)\circ(B,c)=(AB,Ac+b).
\]
It is invertible if and only if \(A\in\operatorname{GL}_m(R)\). This establishes all asserted classifications over **all set-theoretic quandle maps**, not merely selected linear maps.

**2. Retractions are affine module projections.** Squaring gives \(f^2=f\) if and only if \(A^2=A\) and \(Ab=0\). For an idempotent \(A\), the module decomposes as
\[
M=\operatorname{im}A\oplus\ker A.
\]
Both summands are finitely generated projective \(R\)-modules and thus free because \(R\) is local. Their free ranks are uniquely \(r\) and \(s=m-r\). A linear unit of \(M\) sends this ordered decomposition to \(R^r\oplus R^s\), conjugating \(A\) to \(P_r\). Moreover for \(b\in\ker A\), the translation \(h_b(x)=x+b\) satisfies \(h_b A h_b^{-1}(x)=Ax+(1-A)b=Ax+b\), so the translation parameter can be eliminated by conjugacy. Every retraction is therefore conjugate to exactly one \(P_r\). Distinct \(r\) have different image sizes \(p^{dr}\).

**3. Exact sizes of classes.** A projection of free image rank \(r\) is an ordered direct sum decomposition into ranks \(r,s\). The transitive \(\mathrm{GL}_m(R)\)-action has stabilizer \(\mathrm{GL}_r(R)\times\mathrm{GL}_s(R)\), so the number of projections of rank \(r\) equals
\[
\frac{|\operatorname{GL}_m(R)|}{|\operatorname{GL}_r(R)|\,|\operatorname{GL}_s(R)|}.
\]
Reduction modulo \(\varepsilon\) gives \(|\mathrm{GL}_t(R)|=p^{(d-1)t^2}|\mathrm{GL}_t(\mathbb F_p)|\). The familiar field identity \(|\mathrm{GL}_m(\mathbb F_p)|/(|\mathrm{GL}_r(\mathbb F_p)||\mathrm{GL}_s(\mathbb F_p)|)=p^{rs}{m\brack r}_p\) therefore yields \(p^{(2d-1)rs}{m\brack r}_p\) projections. Each such projection allows exactly \(|\ker A|=p^{ds}\) translations \(b\) satisfying \(Ab=0\). This proves \(N_r\), and these maps form the already identified single conjugacy class.

**4. Exact full composition-centralizers.** By conjugacy invariance it suffices to centralize \((P_r,0)\). For \(g=(B,c)\), equality \(gP_r=P_rg\) is equivalent to \(BP_r=P_rB\) and \(P_rc=c\). In the decomposition \(R^r\oplus R^s\), the first condition forces both off-diagonal matrix blocks to vanish, leaving arbitrary \(B_{11}\in M_r(R)\), \(B_{22}\in M_s(R)\). Thus there are \(p^{d(r^2+s^2)}\) linear parts and \(p^{dr}\) translation parts, proving \(Z_r\).

**5. The rigidity.** If \(Z_r=Z_t\), equality of exponents yields
\[
0=(r^2+(m-r)^2+r)-(t^2+(m-t)^2+t)
=(r-t)(2(r+t)-2m+1).
\]
The second factor is an odd integer, never zero. Therefore \(r=t\), proving that the centralizer size alone determines the automorphism class. Summing the disjoint strata proves the commuting-pair formula.

**6. Exact boundary under mixed Jordan lengths.** In \(M'=R_2\oplus R_1^2\), let \(E\) project onto the first summand and \(F\) onto the last two. Their images have equal \(\mathbb F_p\)-dimension two, but multiplication by \(\varepsilon\) has rank one on \(\operatorname{im}E\) and rank zero on \(\operatorname{im}F\). Every quandle automorphism has \(R\)-linear part, so conjugacy preserves this rank and cannot interchange \(E,F\). However, each has a complementary kernel with the other summand as underlying module. The module-linear centralizer of either projection has \(|\operatorname{End}_R(R_2)|\,|\operatorname{End}_R(R_1^2)|=p^2p^4=p^6\) elements, and the permitted translations form its image of cardinality \(p^2\). Thus both have full centralizer cardinality \(p^8\). This demonstrates the stated boundary without asserting a general classification for all mixed Jordan types.

## Verification
Run `python3 verify.py` in the directory containing this document. It implements arithmetic directly in \(\mathbb F_p[\varepsilon]/(\varepsilon^d)\), exhaustively scans \(m\times m\) ring matrices in the five cases \((p,d,m)=(3,1,2),(5,1,2),(3,2,1),(3,2,2),(3,3,1)\), determines idempotents and their reductions modulo \(\varepsilon\), and independently counts commuting matrix parts for each rank. The first two cases are semisimple controls, while the remaining three have nontrivial Jordan blocks. It separately exhausts every set map of the size-three and size-five connected quandles. For the nine-point nonsemisimple quandle, the two elements \(0,1\) generate under the quandle operation and its inverse; the checker verifies this closure and all \(81\) distinct affine homomorphisms, proving that this is the complete homomorphism set. Finally, linear commutation-equation ranks independently verify the mixed-Jordan counterexample over \(\mathbb F_3\) and \(\mathbb F_5\).

For \((p,d,m)=(3,2,2)\), the rank classes have sizes \((81,972,1)\) and full centralizers \((6561,729,531441)\). There are \(1054\) retractions and \(1771470\) ordered commuting pairs with first coordinate a retraction. The script ends with `JORDAN_ALEXANDER_RETRACTIONS_CHECKS_PASSED`. Finite enumeration checks the implementation on selected instances; the proof above, not those checks, establishes all parameter values.

## Relationship to prior work
Taniguchi (2023) classifies good involutions and automorphism-related structures for generalized Alexander quandles, including connectedness and group-automorphism rigidity, but not the present retraction or centralizer distributions. Higashitani and Kurihara (2022) classify *isomorphism types* of generalized Alexander quandles rather than these endomorphism-monoid invariants. Singh (2023) studies residual finiteness and profinite endomorphism monoids, not finite nonsemisimple centralizer spectra. Classical linear-centralizer and local-ring projective-module facts are used, not claimed as new.

The closest publicly indexed retraction result is *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks* (2026), whose explicit hypothesis is semisimplicity of \(T\), and whose stated limitation excludes nonsplit Jordan blocks. Its general normal-form methodology and Gaussian counts inform the present comparison, but it does not imply the formulas for \(d\ge2\) and the full composition-centralizer rigidity or the mixed-length counterexample. Related core-quandle retraction counts for exponent-\(p^2\) abelian groups concern an entirely different underlying module and do not give these centralizer statements. The new claim is the combined nonsemisimple equal-block full conjugacy/centralizer classification and its sharp mixed-block obstruction, not the elementary group-order identity in isolation.

## Limitations
The positive rigidity assertion requires a single primary Jordan block length repeated uniformly, \(\lambda\ne0,1\), and a prime field of odd characteristic; it does not claim the same law for arbitrary finite abelian quandles, mixed elementary divisors, or characteristic two. The exact mixed-length counterexample shows that extending the rigidity statement without hypotheses would be false. The present mathematical review is not an independent audit and does not establish absolute historical priority; an implicit general module-theoretic formula in older literature remains a residual risk. The checker is finite and is not offered as a proof for every parameter.

## References
1. Y. Taniguchi, *Good involutions of generalized Alexander quandles*, arXiv:2302.11138v1 (2023-02-22), https://arxiv.org/abs/2302.11138.
2. A. Higashitani and H. Kurihara, *Generalized Alexander quandles of finite groups and their characterizations*, arXiv:2210.16763v1 (2022-10-30), https://arxiv.org/html/2210.16763v1.
3. M. Singh, *Endomorphism monoid and automorphism group of residually finite and profinite quandles*, arXiv:2311.03708v1 (2023-11-07), https://arxiv.org/html/2311.03708v1.
4. M. E. Montoro, A. Roca and D. Mingueza, *The centralizer of an endomorphism over an arbitrary field*, arXiv:1909.06198v1 (2019-09-12), https://arxiv.org/abs/1909.06198.
5. *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks*, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e (inspected primary RESULT.md).
