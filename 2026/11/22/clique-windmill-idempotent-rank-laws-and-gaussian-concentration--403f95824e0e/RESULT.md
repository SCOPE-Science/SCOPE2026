# Clique-windmill idempotent rank laws and Gaussian concentration

## Finding
Let \(m\ge1\) and \(s_1,\ldots,s_m\ge1\) be integers. Write \(G=K_1\vee\bigl(\bigsqcup_{i=1}^m K_{s_i}\bigr)\), a graph with one hub joined to disjoint complete peripheral blades; put \(S=\sum_i s_i\). Let \(\operatorname{MR}(G)\) be its Margolis–Rhodes monoid of inverse-simplex-continuous partial vertex maps, including the empty map. Define the rank-refined idempotent polynomial
\[
 E_G(z)=\sum_{\substack{f\in\operatorname{MR}(G)\\ f^2=f}}z^{|\operatorname{im}f|},\qquad B_s(z)=(1+z)^s+s(s-1)z.
\]
Then the **exact formula for every heterogeneous blade-size vector** is
\[
 \boxed{E_G(z)=\prod_{i=1}^m B_{s_i}(z)
 +z\sum_{i=1}^m s_i\prod_{j\ne i}B_{s_j}(z)
 +z(1+z)^S+Sz.}
\]
For \(m\) equal blades of size \(s\), write \(b_s=2^s+s(s-1)\); then
\[
 \boxed{E_{m,s}(z)=B_s(z)^m+mszB_s(z)^{m-1}+z(1+z)^{ms}+msz,}
\]
with exact total number of idempotents \(b_s^m+msb_s^{m-1}+2^{ms}+ms\). In particular, for friendship graphs (triangular blades, \(s=2\)),
\[
 \boxed{E_{m,2}(z)=(1+4z+z^2)^m+2mz(1+4z+z^2)^{m-1}+z(1+z)^{2m}+2mz,}
\]
and the total is \(6^m+2m6^{m-1}+4^m+2m\).

**Gaussian rank law.** Fix any \(s\ge2\). If \(R_m\) is the image rank of a uniformly chosen idempotent from \(\operatorname{MR}(K_1\vee mK_s)\), define
\[
\mu_s=\frac{s2^{s-1}+s(s-1)}{b_s},\qquad
\sigma_s^2=\frac{s(s-1)2^{s-2}}{b_s}+\mu_s-\mu_s^2>0.
\]
As \(m\to\infty\),
\[
\boxed{\frac{R_m-\mu_s m}{\sigma_s\sqrt m}\ \Longrightarrow\ N(0,1).}
\]
The full rank law is within total variation distance \(O_s(m^{-1})\) of the law of \(1+X_1+\cdots+X_{m-1}\), where the \(X_i\) are independent and have probability-generating polynomial \(B_s(z)/b_s\). For friendship graphs \(\mu_2=1\) and \(\sigma_2^2=1/3\): typical idempotents have rank \(m+O(\sqrt m)\).

## Assumptions and scope
A finite simple graph is regarded as its one-dimensional simplicial complex: its faces are the empty set, single vertices and edges; a triangle is **not** a two-dimensional simplex. A partial function \(f\) is graph-continuous if the full inverse image of every single vertex or edge is empty or a face. Rank is image cardinality; an undefined source vertex is not in any inverse image. The hub and the peripheral cliques are labelled vertex sets. The product over an empty index set equals one. This theorem counts actual idempotent partial functions, not isomorphism classes of maps or arbitrary graph endomorphisms. The CLT fixes \(s\ge2\) and sends the number of blades \(m\) to infinity.

## Proof
**1. Established idempotent fiber criterion, recalled for clarity.** Every idempotent partial transformation has as image its set \(F\) of fixed points. If a vertex \(y\notin F\) is in the domain and \(f(y)=x\in F\), continuity of the singleton preimage forces \(\{x,y\}\) to be an edge and excludes a second nonfixed vertex mapping to \(x\). If \(x\) had a distinct neighbor \(w\in F\), the inverse image of the target edge \(\{x,w\}\) would contain \(x,y,w\), forbidden. Thus only isolated vertices of \(G[F]\) may receive one adjacent nonfixed source, with each such source used at most once. Conversely, any such assignments produce a continuous idempotent: singleton preimages are vertices or edges, and each target-edge preimage is also a vertex or edge, since two adjacent fixed targets cannot receive extras. This criterion is previously established in the cited double-star work; its general form is **not** claimed as novel here.

**2. Hub not fixed, and hub not assigned.** Choose the fixed set \(F\) independently inside the \(m\) blades. In blade \(i\), choosing zero fixed vertices contributes one. Choosing at least two contributes only the subset choice \(\binom{s_i}{k}z^k\), because no chosen point is isolated within its complete blade. Choosing exactly one fixed vertex \(x\) contributes \(s_i^2z\): there are \(s_i\) choices for \(x\), and its fiber is either \(\{x\}\) or \(\{x,y\}\) for one of the \(s_i-1\) other blade vertices \(y\). Other fixed vertices in different blades are not adjacent, so the choices are independent. This gives \(B_{s_i}(z)=(1+z)^{s_i}+s_i(s_i-1)z\) and the product \(\prod_i B_{s_i}(z)\). Here the hub is genuinely undefined.

**3. Hub not fixed, but assigned.** The hub may be mapped to a fixed peripheral point \(x\) only if \(x\) is isolated in \(G[F]\): its blade must have precisely one fixed point. Once a blade \(i\) and a single fixed \(x\) are chosen, the hub occupies the unique permitted extra preimage of \(x\), excluding any other extra from that blade. This contributes \(s_i z\) for blade \(i\); all other blades retain their independent \(B_{s_j}(z)\) options. The hub is a unique source vertex and cannot be assigned twice. Hence the second term \(z\sum_i s_i\prod_{j\ne i} B_{s_j}(z)\). These cases are disjoint from Step 2.

**4. Hub fixed.** If the fixed set contains any peripheral vertex, the hub is adjacent to a fixed vertex and so cannot receive an extra. Every fixed peripheral vertex is adjacent to the hub, so none can receive an extra either. Thus all peripheral vertices are independently fixed or undefined, giving \(z(1+z)^S\), including the configuration with only the hub fixed and all peripheral vertices undefined. For that configuration alone, the hub is isolated in the fixed induced graph and may additionally receive exactly one of its \(S\) peripheral neighbors, contributing \(Sz\). All cases are mutually exclusive and exhaustive. Combining Steps 2–4 proves the heterogeneous polynomial and its equal-blade and friendship specializations.

**5. Gaussian limit and quantified approximation.** Fix \(s\ge2\), abbreviate \(b=b_s\), \(B=B_s\). The rank enumeration is the sum of four polynomials with nonnegative coefficients, and its dominant term \(mszB(z)^{m-1}\) has total mass \(msb^{m-1}\). Its normalized probability-generating function is \(z(B(z)/b)^{m-1}\), exactly the distribution of \(1+\sum_{i=1}^{m-1}X_i\) with independent \(X_i\) as stated. The remaining terms have mass \(b^m+2^{ms}+ms\). Their fraction is at most
\[
\frac{b^m+2^{ms}+ms}{msb^{m-1}}
=\frac{b}{ms}+\frac{b}{ms}\left(\frac{2^s}{b}\right)^m+\frac1{b^{m-1}}=O_s(m^{-1}),
\]
since \(b=2^s+s(s-1)>2^s\). This gives the claimed total-variation bound by a mixture coupling. The distribution defined by \(B(z)/b\) has mean \(B'(1)/b=\mu_s\), second factorial moment \(B''(1)/b=s(s-1)2^{s-2}/b\), and strictly positive variance \(\sigma_s^2\), since it assigns positive probability to \(X=0\) and \(X=1\). The standard independent-summands central limit theorem, the bounded shift between \(m\mu_s\) and \(1+(m-1)\mu_s\), and the total-variation approximation together prove the Gaussian statement.

## Verification
The standalone `verify_windmill.py` enumerates **every** partial vertex function (each source value either undefined or one vertex) for nine heterogeneous or homogeneous blade configurations: \((1)\), \((2)\), \((1,1)\), \((2,1)\), \((2,2)\), \((1,1,1)\), \((3,1)\), \((2,2,1)\), \((2,3)\). It tests \(f^2=f\) directly and checks the complete inverse images of every vertex and every edge without relying on the blade proof. The nine resulting image-rank coefficient lists agree coefficientwise with the theorem. For example, configurations \((2,2)\), \((2,2,1)\), and \((2,3)\) give \((1,17,38,18,5,1)\), \((1,20,59,74,31,7,1)\), and \((1,24,75,41,19,6,1)\). Reproduce with `python3 verify_windmill.py`; expected final output is `VERIFY_OK`. Exhaustive checks here are finite corroboration, not a proof of the all-parameter identities or the limit theorem.

## Relationship to prior work
Margolis and Rhodes established the inverse-simplex continuous transformation monoid and studied its basic structure, with enumerations for paths and cycles; the present result does not claim the monoid or continuity definition. The previously published **general idempotent fiber criterion** (fixed points plus one adjacent extra only at isolated fixed vertices) is likewise prior theory, explicitly used rather than renamed as a new lemma. Published formulae for stars are also prior results: setting all \(s_i=1\) recovers their rank enumeration and total \(2^{m+1}+m2^{m-1}+m\). Earlier exact Green-class spectra for generalized windmills concern the different **partial induced-subgraph automorphism inverse monoid**, whose idempotents are partial identities and not the noninjective graph-continuous maps counted here. The new mathematical content assessed is the all-blade-size explicit rank polynomial, its exact friendship specialization, and the sharp asymptotic Gaussian rank law with total-variation comparison. Absence of an indexed equivalent is not a guarantee of historical priority.

## Limitations
The exact enumerator is for one-hub disjoint-clique windmills, not arbitrary connected graphs or all clique-sums. The limit theorem fixes each peripheral clique size as the blade number tends to infinity; no result is asserted for varying clique sizes. The known universal fiber criterion and star enumeration are not original. Independent mathematical and publication-priority verification have not occurred. No semigroup-complexity or full-monoid-rank enumeration is claimed.

## References
1. S. Margolis and J. Rhodes, *The Margolis-Rhodes Monoid of a Graph*, arXiv:2609.39370v1 (first posted 2026-09-30), https://arxiv.org/abs/2609.39370 .
2. S. Margolis and J. Rhodes, *Degree 2 Transformation Semigroups as Continuous Maps on Graphs: Foundations and Structure*, arXiv:2005.02606 (first posted 2020-05-06), https://arxiv.org/abs/2005.02606 .
3. *Complete idempotent rank enumeration for double-star Margolis-Rhodes monoids* (2026-10-26), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-complete-idempotent-rank-enumeration-for-double-star-margolis-rh--59b10be0366d .
4. *Exact rank, idempotent and regularity profiles of continuous partial maps on finite stars* (2026-11-08), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-rank-idempotent-and-regularity-profiles-of-continuous-part--03034af7bf4f .
5. *Exact Green-class spectra of generalized windmill partial-automorphism monoids* (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-green-class-spectra-of-generalized-windmill-partial-automo--f7ff06cf4156 .
