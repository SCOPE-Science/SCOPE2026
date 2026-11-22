# Retraction images and exact rank census for rank-one unipotent Alexander quandles

## Finding
Let \(p\) be a prime, \(f\ge 1\), \(q=p^f\), and let \(K=\mathbb F_q\) be regarded solely as an \(f\)-dimensional additive vector space over \(\mathbb F_p\). Define the Alexander quandle \(Q=K^2\) by
\[
 (a,b)\triangleright(c,d)=(a+b-d,b).
\]
A **retraction** means any set-theoretic quandle endomorphism \(F:Q\to Q\) satisfying \(F^2=F\). Its rank is the cardinality of its image, **not** its linear rank. No additivity of \(F\) is assumed.

Write \({f\brack r}_p\) for a Gaussian binomial coefficient. Then the exact cardinality generating polynomial of all retractions is
\[
\boxed{R_{p,f}(z)=\sum_{r=0}^f {f\brack r}_p\,
 p^{r(f-r)+(f-r)+(f-r)p^r+r(p^f-p^r)}\,z^{p^{2r}}.}
\]
In particular, the possible image cardinalities are **exactly** \(p^{2r}\) for \(0\le r\le f\); there are no others. Every image of rank \(p^{2r}\) is a subquandle isomorphic to the same rank-one unipotent Alexander quandle on \((\mathbb F_p^r)^2\) (the one-point quandle for \(r=0\)).

More precisely, the distinct embedded images of rank \(p^{2r}\) are exactly the subsets
\[
S_{B,t}=\bigcup_{b\in B}\big((t(b)+U)\times\{b\}\big),
\]
where \(U\le_{\mathbb F_p}K\) has dimension \(r\), \(B\) is an affine coset of \(U\) in \(K\), and \(t:B\to K/U\) is **any set map** (the coset \(t(b)+U\) is independent of representative). The number of distinct such images and the number of retractions onto each specified image are respectively
\[
\boxed{I_{p,f,r}={f\brack r}_p\,p^{(f-r)+(f-r)p^r},\qquad
M_{p,f,r}=p^{r(f-r)+r(p^f-p^r)}.}
\]
Thus \(I_{p,f,r}M_{p,f,r}\) is the coefficient displayed above. For \((p,f)=(2,2)\),
\[
R_{2,2}(z)=16z+192z^4+z^{16},
\]
with 24 distinct four-point retraction images, eight retractions per image. In comparison, subquandles of this 16-point quandle can have other cardinalities (e.g. two), so being a subquandle is not sufficient to be a retract.

## Assumptions and scope
The field multiplication of \(K\) is unused; only its elementary abelian additive group matters. The linear operator \(T(a,b)=(a+b,b)\) is invertible, satisfies \((T-I)^2=0\) and \(T\ne I\), and has a single length-two Jordan block over \(K\). For \(f>1\), the additive \(\mathbb F_p\)-linear endomorphisms of \(K\) can be non-scalar. The theorem counts every labeled set map preserving the quandle operation, not just affine or field-linear maps.

## Proof
**1. Normal form for unrestricted endomorphisms.** Let \(F(a,b)=(F_1(a,b),F_2(a,b))\) preserve the displayed operation. The second coordinate of \(x\triangleright y\) equals the second coordinate of \(x\), so
\[
 F_2(a+b-d,b)=F_2(a,b)
\]
for every \(a,b,d\in K\). Since \(b-d\) runs through \(K\), there is a set map \(g:K\to K\) with \(F_2(a,b)=g(b)\). The first-coordinate homomorphism equation becomes
\[
 F_1(a+b-d,b)-F_1(a,b)=g(b)-g(d).
\]
For fixed \(b\), its left side is a translation difference independent of \(a\). Therefore the function \(h\mapsto g(b)-g(b-h)\) is additive in \(h\), by applying two translations successively. Fixing one \(b\) shows that \(g\) is affine-additive: \(g(b)=u(b)+v\) for a unique additive endomorphism \(u:K\to K\) and \(v\in K\). Every additive map is \(\mathbb F_p\)-linear. The first-coordinate equation reduces to
\[
 F_1(a+h,b)-F_1(a,b)=u(h),
\]
so \(F_1(a,b)=u(a)+h(b)\) with an arbitrary set map \(h:K\to K\). Conversely every
\[
\boxed{F(a,b)=(u(a)+h(b),\ u(b)+v)}
\]
with \(u\) additive, \(v\in K\), and \(h\) any set map satisfies the quandle homomorphism identity. The parameters are unique.

**2. The idempotence equations.** Composition gives
\[
F^2(a,b)=\big(u^2(a)+u(h(b))+h(u(b)+v),\ u^2(b)+u(v)+v\big).
\]
Hence \(F^2=F\) if and only if
\[
 u^2=u,\qquad u(v)=0,\qquad h(b)=u(h(b))+h(u(b)+v)\quad (b\in K).
\]
Put \(U=\operatorname{im}u\) of dimension \(r\) and \(W=\ker u\) of dimension \(f-r\). As \(u\) is idempotent, \(K=U\oplus W\) and \(v\in W\). Write \(h=h_U+h_W\) according to this splitting and let \(B=v+U\). Taking the \(U\)- and \(W\)-components of the final equation yields respectively
\[
 h_U\big(u(b)+v\big)=0,\qquad h_W(b)=h_W\big(u(b)+v\big).
\]
Thus \(h_U\) vanishes on \(B\) but is arbitrary outside \(B\), whereas \(h_W\) is determined by **arbitrary** values on \(B\), extended to all \(b\in K\) through the projection \(b\mapsto u(b)+v\).

**3. Rank and exact map count.** On any fixed second-coordinate fiber of the image, \(u(a)\) runs through \(U\) while \(h_W(b)\) is fixed. The second-coordinate image is precisely \(B=v+U\). Every fiber above \(B\) is a full affine \(U\)-coset in the first coordinate, so \(|\operatorname{im}F|=|U|^2=p^{2r}\). There are \({f\brack r}_p\) choices of \(U\), then \(p^{r(f-r)}\) complementary kernels \(W\), then \(p^{f-r}\) choices of \(v\in W\). For fixed \(u,v\), there are \(p^{r(q-p^r)}\) choices of \(h_U\) off \(B\) and \(p^{(f-r)p^r}\) choices of \(h_W\) on \(B\). Multiplying proves \(R_{p,f}(z)\). All exponents \(r=0,\ldots,f\) occur since projections of all ranks exist.

**4. Embedded-image classification.** For any retraction, \(B=v+U\) and the first fiber above \(b\in B\) is \(h_W(b)+U\); hence its image has the asserted form. Conversely, choose any \(U,B,t\) as in the finding. Choose any complement \(W\) of \(U\), let \(u\) be the projection onto \(U\) along \(W\), and choose the unique \(v\in W\cap B\). Lift the values of \(t\) uniquely to \(W\), define \(h_W\) by the extension rule in step 2, and set \(h_U=0\). This constructs a retraction onto \(S_{B,t}\). For a prescribed image, \(U\) is intrinsically recovered as the direction of its projected second-coordinate support \(B\), while \(t(b)\) is recovered from its first-coordinate fibers; no distinct \((U,B,t)\) represent the same image. Count \(U\), the \(p^{f-r}\) cosets \(B\), and the \(p^{(f-r)p^r}\) functions \(t\) to get \(I_{p,f,r}\).

**5. Multiplicity per image and intrinsic type.** For fixed \(S_{B,t}\), each of the \(p^{r(f-r)}\) complementary kernels gives precisely one \(v\) and one constrained \(h_W\). The free values of \(h_U\) outside \(B\) contribute \(p^{r(q-p^r)}\), proving \(M_{p,f,r}\). Choose a translation \(B=b_0+U\) and an arbitrary representative function \(\widehat t:B\to K\). Under \((\widehat t(b)+a,b)\mapsto(a,b-b_0)\) with \(a\in U\), the induced quandle operation is \((a,s)\triangleright(c,d)=(a+s-d,s)\). Thus every image is isomorphic to the rank-\(r\) model, independently of \(t\).

## Verification
The standalone `verify.py` enumerates actual maps on the quandle via independent additive linear maps and independent arbitrary-function values, and tests the operation law and composition-idempotence directly for every candidate. It compares both the image-rank census and the **set of actual embedded images** against the formulas. On the four-element quandle it also exhaustively enumerates all \(4^4\) set maps without using the normal form. The tests gave:

- \((p,f)=(2,1)\): 16 normal-form endomorphisms, retraction ranks \(\{1:4,4:1\}\).
- \((p,f)=(3,1)\): 243 normal-form endomorphisms, retraction ranks \(\{1:9,9:1\}\).
- \((p,f)=(2,2)\): 16,384 normal-form endomorphisms, retraction ranks \(\{1:16,4:192,16:1\}\) and embedded-image ranks \(\{1:16,4:24,16:1\}\).

The checker prints `UNIPOTENT_RETRACTION_CENSUS_VERIFIED`. These finite computations are consistency checks; steps 1–5 prove the formulas for all primes and extension degrees.

## Relationship to prior work
Higashitani and Kurihara, *Generalized Alexander quandles of finite groups and their characterizations* (arXiv:2210.16763, 2022), characterize **quandle isomorphism classes**, including for abelian groups. Their original paper does not provide the unrestricted nonbijective endomorphism normal form or retraction-image census here. Higashitani, Kamada, Kosaka and Kurihara (arXiv:2406.01074, 2024) expand this **isomorphism classification**, again without retraction counts. Singh (arXiv:2311.03708, 2023) proves qualitative residual-finiteness results for quandle endomorphism monoids; these do not enumerate their idempotents.

The published result *Complete subquandle size distribution for rank-one unipotent Alexander quandles* (published-finding corpus, 2026-10-18, identifier `288df6733df1`) classifies **all subquandles of precisely this \(Q\)**, including many which are not retracts. Its parameterization does not determine which subquandles admit a retraction or how many retractions target a given subquandle. That work's subquandle classification is acknowledged and not claimed anew. The published result *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks* (published-finding corpus, 2026-10-18, identifier `117335b68a3e`) gives a retraction census for semisimple operators; its squarefree-minimal-polynomial hypothesis fails for \(T=I+N\ne I\). In the present nonsplit case, component labels and fiber choices couple differently, and arbitrary functions remain in the endomorphism normal form. The new assertion is the exact **retract-only** image classification, prescribed-image multiplicity and full count for this nonsemisimple family.

## Limitations
Only the Jordan type \((2)\) over \(K\) is treated; the theorem does not classify general nonsemisimple Alexander quandles, other Jordan block lengths, or all their subquandles. A field-theoretic scalar restriction on \(u\) would give incorrect counts when \(f>1\); the base field of linearity is \(\mathbb F_p\). Previous subquandle enumeration is stronger on the different question of all embedded subquandles, and general implicit consequences or older equivalent quandle-homomorphism formulations cannot be ruled out solely by searches. No independent review is claimed.

## References
1. A. Higashitani and H. Kurihara, *Generalized Alexander quandles of finite groups and their characterizations*, arXiv:2210.16763v1 (2022-10-30), https://arxiv.org/abs/2210.16763.
2. A. Higashitani, S. Kamada, J. Kosaka, H. Kurihara, *Classification of generalized Alexander quandles*, arXiv:2406.01074v1 (2024-06-03), https://arxiv.org/html/2406.01074v1.
3. M. Singh, *Endomorphism monoid and automorphism group of residually finite and profinite quandles*, arXiv:2311.03708v1 (2023-11-07), https://arxiv.org/html/2311.03708v1.
4. *Complete subquandle size distribution for rank-one unipotent Alexander quandles*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-subquandle-size-distribution-for-rank-one-unipotent-ale--288df6733df1.
5. *Semisimple Alexander-quandle retractions: a transformation–affine factorization and exact image ranks*, published 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-semisimple-alexander-quandle-retractions-a-transformation-affine--117335b68a3e.
6. Y. Iijima and T. Murao, *On connected component decompositions of quandles*, arXiv:1704.07689v1 (2017-04-25), https://arxiv.org/abs/1704.07689.
