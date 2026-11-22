# All nearly Frobenius coproducts on finite-poset incidence algebras

## Finding

Let \(P\) be any nonempty finite poset and \(k\) any field. Write \(A=I(P,k)\) for its incidence algebra, with basis \(e_{xy}\) indexed by \(x\le y\) and multiplication \(e_{xy}e_{uv}=\mathbf 1_{y=u}e_{xv}\). A *nearly Frobenius coproduct* is a \(k\)-linear map \(\Delta:A\longrightarrow A\otimes_k A\) that is an \(A\)-bimodule map for the outer actions and is coassociative. The zero map is included when discussing the vector space of all such coproducts.

Let \(\mathcal B(P)\) be the set of connected components of the undirected comparability graph of \(P\) having both a least element \(s_C\) and a greatest element \(t_C\). Then **every** nearly Frobenius coproduct, uniquely, has the form

\[
\Delta_{\boldsymbol\lambda}(e_{xy})=\begin{cases}
\lambda_C\,e_{x,t_C}\otimes e_{s_C,y},&x,y\in C\in\mathcal B(P),\\
0,&x,y\text{ in an unbounded component},
\end{cases}
\qquad \lambda_C\in k.
\]

In particular, the space of all such coproducts has dimension \(|\mathcal B(P)|\), with one canonical basis coproduct per bounded connected component. The map \(\Delta_{\boldsymbol\lambda}\) is injective **if and only if** every component of \(P\) is bounded and every \(\lambda_C\ne0\). If \(P\) is an antichain and all \(\lambda_C\ne0\), its coproduct admits a counit; conversely no other coproduct in this classification admits a counit.

For \(k=\mathbb F_q\), let \(d_C=|\{(x,y)\in C^2:x\le y\}|\). The complete linear-image-rank enumerator of coproducts is

\[
\boxed{\sum_{\Delta}T^{\operatorname{rank}_k\Delta}
=\prod_{C\in\mathcal B(P)}\bigl(1+(q-1)T^{d_C}\bigr).}
\]

Consequently there are \(q^{|\mathcal B(P)|}\) coproducts including zero, and exactly \((q-1)^{|\mathcal B(P)|}\) injective ones if every connected component is bounded, otherwise none. Here \(\operatorname{rank}_k\Delta\) means the rank of the *linear map*, not the tensor rank of \(\Delta(1)\).

A notable explicit example is the four-element diamond \(s<a<t\), \(s<b<t\), with \(a,b\) incomparable. Its incidence algebra is the connected bound-quiver algebra of the branching diamond with the single **binomial** relation equating the two length-two paths. The relation ideal contains no nonzero monomial path. Yet the nonzero coproduct \(\Delta(e_{xy})=e_{x,t}\otimes e_{s,y}\) is injective, has rank \(9\), and exists over **every** field. Therefore the literal unrestricted 'no monomial relations implies a straight type-A path' conclusion of Theorem 4.3 of Artenstein--González--Lanzilotta (2013) cannot include such a binomially related incidence algebra. This observation concerns the literal scope of that theorem and does not assert that its intended restricted setting was as broad.

## Assumptions and scope

No restriction on characteristic or algebraic closure is used. The poset is finite, nonempty and may be disconnected. A connected component is taken in the *undirected comparability graph*. 'Bounded' means the existence of an element less than or equal to all vertices and an element greater than or equal to all vertices **within that component**, not merely maximal and minimal vertices. The tensor product carries the outer \(A\)-bimodule action: \(a\cdot(u\otimes v)\cdot b=(au)\otimes(vb)\). No counit is presumed.

## Proof

**1. Diagonal idempotent restriction.** Set \(c=\Delta(1)\). The bimodule identity implies \(\Delta(a)=(a\otimes1)c=c(1\otimes a)\) for every \(a\in A\). For each vertex \(i\), the equality

\[
\Delta(e_{ii})=(e_{ii}\otimes1)\Delta(e_{ii})=\Delta(e_{ii})(1\otimes e_{ii})
\]

forces a unique expansion

\[
\Delta(e_{ii})=\sum_{b\le i\le a}\gamma_i(a,b)\,e_{ia}\otimes e_{bi}.
\]

For any fixed ordered pair \((a,b)\) of vertices, extend \(\gamma_i(a,b)\) by zero unless \(b\le i\le a\). This extension is essential for the boundary cases.

**2. Comparable vertices have the same coefficient.** For \(i\le j\), compute the bimodule identity for the basis element \(e_{ij}\) in two ways:

\[
(e_{ij}\otimes1)\Delta(e_{jj})=\Delta(e_{ii})(1\otimes e_{ij}).
\]

Compare coefficients of the tensors \(e_{ia}\otimes e_{bj}\), for all \(a,b\) for which either side can contribute. One gets \(\gamma_j(a,b)=\gamma_i(a,b)\), including zero-padded cases: a coefficient on one side without a term on the other must be zero. Hence \(\gamma_i(a,b)\) is constant along each undirected comparability edge and therefore on each connected component.

**3. Exact support.** Suppose a coefficient for the fixed pair \((a,b)\) is nonzero on a component \(C\). By constancy, it is nonzero at every \(i\in C\), forcing \(b\le i\le a\) for every \(i\in C\). Since \(b\le i\le a\), both \(a,b\) belong to \(C\). Thus \(b=s_C\) is the unique least element and \(a=t_C\) the unique greatest element. No nonzero coefficients are possible on a component lacking either extremum. Conversely, a bounded component permits exactly one free coefficient \(\lambda_C\). Substituting into the diagonal expansion and the identity \(\Delta(e_{xy})=\Delta(e_{xx})(1\otimes e_{xy})\) gives the displayed formula. This proves **exhaustiveness and uniqueness**, not just existence of an example.

**4. Compatibility and coassociativity.** Conversely, for each bounded component, the displayed formula satisfies the bimodule equations on basis products by \(e_{xy}e_{uv}=\mathbf1_{y=u}e_{xv}\); terms from distinct components multiply to zero. More explicitly, both iterated coproducts on an interval in a bounded component equal

\[
(\Delta\otimes1)\Delta(e_{xy})
=(1\otimes\Delta)\Delta(e_{xy})
=\lambda_C^2\,e_{x,t_C}\otimes e_{s_C,t_C}\otimes e_{s_C,y}.
\]

On unbounded components both are zero. Therefore every displayed map is a coassociative nearly Frobenius coproduct, and the displayed family is exactly the full space.

**5. Image rank, injectivity and counitality.** In one bounded component \(C\), the tensors \(e_{x,t_C}\otimes e_{s_C,y}\), indexed by \(x\le y\), are distinct tensor-product basis elements. Thus the restriction of \(\Delta\) has rank \(d_C\) if \(\lambda_C\ne0\), and rank zero if \(\lambda_C=0\). Images supported in distinct components are disjoint, so ranks add and the product enumerator follows by choosing, independently, a zero or one of \(q-1\) nonzero coefficients for each component. This also proves the injectivity criterion. A counit would force injectivity. If \(s_C\ne t_C\), applying a hypothetical left counit to \(\Delta(e_{t_C,t_C})=\lambda_C e_{t_C,t_C}\otimes e_{s_C,t_C}\) cannot yield \(e_{t_C,t_C}\), as these are different basis vectors. Thus a counital map forces each component to be a singleton. Conversely, for an antichain and all nonzero coefficients, setting \(\varepsilon(e_{ii})=\lambda_{\{i\}}^{-1}\) yields both counit identities.

**6. Diamond witness.** For \(P=\{s,a,b,t\}\) with relations \(s<a<t\), \(s<b<t\), there are nine comparable ordered pairs. The Hasse quiver has arrows \(s\to a\to t\) and \(s\to b\to t\), and the incidence algebra identifies their two length-two path products. The relation ideal is exactly the one-dimensional span of their difference, containing no monomial. This is a non-path-type-A connected quiver, while step 5 gives a nonzero *injective* coproduct. In this example the rank polynomial is \(1+(q-1)T^9\).

## Verification

A standalone Python 3 checker `incidence_noncounital_checker.py` assembles the **original linear equations** for \(c=\Delta(1)\), rather than assuming the classification. Over the prime fields \(\mathbb F_2\) and \(\mathbb F_3\) it checks all topologically labeled transitive posets with \(1\le |P|\le5\): respectively \(1,2,7,40,357\) posets at sizes \(1,2,3,4,5\), for a total of **814 field-poset computations**. In every instance the kernel dimension equals the number of bounded connected components. The program additionally substitutes the explicit basis tensors, tests their bimodule equations, checks image injectivity per component, and checks the diamond dimension/rank. Run with `python3 incidence_noncounital_checker.py`; the expected final line starts `INCIDENCE_COPRODUCT_CLASSIFICATION_OK` and ends with the field-by-size counts. These finite checks are **not** a proof of the all-poset theorem; steps 1--6 above are the proof.

## Relationship to prior work

Ocal (2026), arXiv:2611.16024v1, identifies injective non-counital Frobenius coproducts with QF-3 algebras and establishes the general Hochschild-centralizer framework. The present result **specializes to incidence algebras but goes further in that family**, exhaustively classifying each bimodule coproduct, its image rank, finite-field count and counitality; no new general QF-3 equivalence is claimed.

Artenstein, González and Lanzilotta (2013), arXiv:1306.3964, proved a one-parameter result for straight oriented type-A path algebras, described other quiver families, and stated a stronger no-monomial-relations obstruction in Theorem 4.3. The chain case here is old. The diamond with a **binomial** commutativity relation is not a path algebra and witnesses why the literal broad reading of that obstruction needs qualification. The 2020/2022 work on nearly Frobenius dimension concerns general Frobenius algebras, not this complete incidence-poset classification. This is a statement-by-statement comparison, not an inference from title differences.

## Limitations

The classification applies only to **finite-poset incidence algebras**, not arbitrary bound-quiver or category algebras. Neither uniqueness of previous publication nor independent peer validation is established. The observation regarding the 2013 statement relies on its literal phrase 'no monomial relations'; it is not a claim about any narrower intended hypotheses. The finite checker verifies only characteristic 2 and 3 at poset sizes through 5; arbitrary characteristic and size are justified symbolically. The 2026 paper's tensor rank of \(\Delta(1)\) is not the linear image rank enumerated here. Zero is included in the enumeration but is not termed a nonzero non-counital Frobenius structure.

## References

1. P. S. Ocal, *Non-counital Frobenius algebras and QF-3 algebras*, arXiv:2611.16024v1, first submitted 11 November 2026, https://arxiv.org/html/2611.16024v1 (especially §§2--4 and Theorem 20).
2. D. Artenstein, A. González and M. Lanzilotta, *Constructing nearly Frobenius algebras*, arXiv:1306.3964, 2013, https://arxiv.org/abs/1306.3964 (especially §4.1, Theorem 4.3).
3. D. Artenstein, A. González and G. Mata, *Nearly Frobenius dimension on Frobenius algebras*, arXiv:2011.09790v1, 2020, https://arxiv.org/abs/2011.09790; journal edition *Communications in Algebra* 50 (2022), https://doi.org/10.1080/00927872.2022.2077953.
