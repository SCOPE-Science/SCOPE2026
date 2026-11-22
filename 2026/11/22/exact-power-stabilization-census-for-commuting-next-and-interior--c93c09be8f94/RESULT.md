# Exact power-stabilization census for commuting next and interior on finite chains

## Finding
Let \(C_n=\{0,1,\ldots,n-1\}\), \(n\geq1\), carry the Alexandrov topology of upper sets. Write \(\Box\) for interior and \(\bigcirc\) for a deterministic next-time operator induced by an endomap \(f:C_n\to C_n\). Require the **two-sided commutation scheme**
\[
\bigcirc\Box p\leftrightarrow\Box\bigcirc p
\]
at every point for every valuation of the atom \(p\). Such maps are precisely the nondecreasing maps with \(f(n-1)=n-1\) and \(f(i+1)-f(i)\in\{0,1\}\).

Let \(r=n-|f(C_n)|\) be the **image defect** and let
\[
\tau(f)=\min\{t\geq0:f^{t+1}=f^t\}
\]
be the least time at which every nested-next formula stabilizes (uniformly for all valuations). The exact joint count \(A(n,r,t)\) of these maps with defect \(r\) and index \(t\) obeys, for every \(n\geq1\), \(0\leq r<n\), and integer \(t\),
\[
A(n,0,t)=\mathbf1_{\{t=0\}},\qquad
A(n,r,t)=\begin{cases}
0,&r>0,\ t<1,\\
\displaystyle\sum_{s=0}^{\min(r,n-r-1)}\binom rs A(n-r,s,t-1),&r>0,\ t\geq1.
\end{cases}
\]
(The second line is the defining rule only when \(r>0\).) This finite downward recursion determines every coefficient without reference to maps of larger size. It satisfies
\[
\sum_{t\ge0}A(n,r,t)=\binom{n-1}{r}.
\]
For \(1\leq r<n\), the possible stabilization indices at that defect are **exactly** \(1,2,\ldots,n-r\). The upper bound is sharp; the number of maps at the upper endpoint is
\[
A(n,r,n-r)=\begin{cases}r,&n-r\geq2,\\1,&n-r=1.\end{cases}
\]
In particular, the exact index histogram for \(n=8\), from time zero through time seven, is \((1,7,46,42,20,8,3,1)\). These counts refer to the repeated power of a **single fixed** map, not to products of independently sampled maps.

## Assumptions and scope
The underlying topological space is the finite \(T_0\) Alexandrov chain with **upper-set** topology, not the discrete topology. Interior is \(\operatorname{int}(P)=\{i:[i,n-1]\subseteq P\}\). The next operator is \(\bigcirc P=f^{-1}(P)\), where a valuation is an arbitrary subset \(P\subseteq C_n\). The displayed commutation is required in both directions for all valuations. Powers use ordinary function composition, with \(f^0\) the identity; \(\tau(f)=0\) if and only if \(f\) is identity. The image defect \(r\) lies in the closed integer range \(0\leq r\leq n-1\); \(n-r\) is its image cardinality, not a group-theoretic rank. Counts concern labelled chains and maps, without quotienting by isomorphism. For \(n=1\), only the identity exists.

## Proof
**1. A topological characterization.** For any arbitrary subset \(P\) and point \(i\), membership in \(f^{-1}(\operatorname{int}P)\) says \([f(i),n-1]\subseteq P\), whereas membership in \(\operatorname{int}(f^{-1}P)\) says \(f([i,n-1])\subseteq P\). Two set-inclusion predicates agree for every \(P\) if and only if the included sets coincide. Consequently, the commutation scheme is equivalent to
\[
 f([i,n-1])=[f(i),n-1]\quad\text{for all }0\leq i<n.
\]
This forces \(f\) to be nondecreasing, its image to be a final interval, and \(f(n-1)=n-1\). By monotonicity, a jump of at least two across consecutive inputs would omit a point of the final image, so all adjacent increments belong to \(\{0,1\}\). Conversely, a nondecreasing map with those increments and fixed top vertex maps each input suffix onto the full output suffix by discrete intermediate values, proving commutation.

**2. Defect and a canonical binary encoding.** Put \(\varepsilon_i=f(i+1)-f(i)\in\{0,1\}\) for \(0\leq i<n-1\). Every binary word of length \(n-1\) gives exactly one commuting map by
\[
 f(i)=(n-1)-\sum_{j=i}^{n-2}\varepsilon_j
      =i+\#\{j\geq i:\varepsilon_j=0\}.
\]
The number \(r\) of zero increments equals \(n-|f(C_n)|\), and \(f(C_n)=[r,n-1]\). Thus the number of maps with defect \(r\) is the previously known \(\binom{n-1}{r}\), with identity the unique case \(r=0\).

**3. A surjective restriction gives the full time recurrence.** Suppose \(r>0\), set \(k=n-r\), and restrict \(f\) to its image: \(g=f|_{[r,n-1]}\), translated down by \(r\) to a map of \(C_k\). It remains a commuting map because the upper endpoint and step restriction are inherited. Write \(s\) for its zero-increment count, necessarily \(0\leq s\leq\min(r,k-1)\). For fixed \(g\), exactly \(\binom{r}{r-s}=\binom{r}{s}\) binary words extend it to a map \(f\) with total defect \(r\): prescribe the \(k-1\) final increments from \(g\), and choose the other \(r-s\) zeros among the first \(r\) increment slots.

Since \(f:C_n\to[r,n-1]\) is onto, for each integer \(j\geq1\),
\[
 f^{j+1}=g^{j}\circ f,\qquad f^j=g^{j-1}\circ f,
\]
where the restriction \(g\) is interpreted on the image. Surjectivity proves that \(f^{j+1}=f^j\) if and only if \(g^j=g^{j-1}\). As \(f\neq\operatorname{id}\), the first equality occurs at \(j=1+\tau(g)\). Therefore \(\tau(f)=1+\tau(g)\). Multiplying the extension counts by the smaller-chain counts proves the stated binomial recursion. The initial case \(r=0\) gives the identity, and repeated reduction strictly decreases chain size, so the recursion terminates. Summing over all \(t\) counts the binary words of defect \(r\), proving its binomial marginal.

**4. Exact support, sharp endpoint, and multiplicity.** For \(r>0\), the first image is \([r,n-1]\) of size \(k=n-r\). Because \(f(i)\geq i\), every subsequent image is a final interval. If the current least image point is not fixed, its image strictly advances by at least one, so at most \(k-1\) more steps are required. Thus \(1\leq\tau(f)\leq k\).

When \(k\geq2\), equality at \(k\) requires the least image point to visit \(r,r+1,\ldots,n-1\) with no skipped vertex; equivalently \(f(i)=i+1\) for every \(r\leq i<n-1\). By the binary formula this forces exactly one zero in the suffix, at increment position \(n-2\), and the other \(r-1\) zeros arbitrarily among the first \(r\) slots. There are exactly \(\binom{r}{r-1}=r\) choices. When \(k=1\) there is just one constant-top map and it has index one.

To realize every index, choose all \(r\) zero increments among the first \(r\) slots; then \(f\) is already idempotent and \(\tau=1\). For each \(2\leq t\leq k\), choose any \(r-1\) zeros among those first \(r\) slots and place the remaining zero at \(j=r+t-2\); then \(0\mapsto r\mapsto r+1\mapsto\cdots\mapsto r+t-1\) is the strictly moving minimum orbit and its last point is fixed. Hence \(\tau=t\). All assertions, including end cases, follow.

**5. Logical interpretation.** For any map on a finite set, the equivalence of \(\bigcirc^{t+1}p\) and \(\bigcirc^t p\) for *every* valuation holds exactly if the functions \(f^{t+1}\) and \(f^t\) coincide, since a singleton valuation distinguishes any unequal images. Accordingly \(\tau\) is the exact uniform modal stabilization depth, rather than just the stabilization time of a selected point or a chosen valuation.

## Verification
The standalone standard-library Python program `verify.py` has two independent paths. First, for \(n\leq5\) it enumerates *all* \(n^n\) total endomaps and all \(2^n\) Boolean valuations, directly computing both sides of the modal commutation scheme, and compares the resulting set to the binary normal form. Second, for \(n\leq12\) it enumerates each binary normal-form map, directly composes its powers, and compares its defect-index frequency to the independently programmed recurrence, binomial rank marginals, full attainable-index interval and exact extremal multiplicity. The complete program prints `VERIFY_OK 8158` on success. These are finite corroborating checks; the preceding proof, not the finite enumeration, establishes all-size claims.

## Relationship to prior work
Vooijs and Fernández-Duque (2026) develop dynamic topological logic on Alexandrov spaces and prove computable enumerability/axiomatizability. The present statement focuses instead on the finer subclass where next commutes **in both directions** with the topological interior, and on the exact finite power-index count by image defect. The paper's topological/temporal semantics motivate the object but do not supply the displayed census.

Fernandes (2024), Section 3, identifies the increasing interval-image maps and proves their known cardinality \(2^{n-1}\) and rank counts; the 2013 Adeshola–Umar treatment proves stronger joint initial-rank/fixed-point counts for all monotone contractions. These facts are expressly **not** claimed as new. They do not determine \(\tau\): for example, on \(C_5\) the commuting maps with value vectors \(\bigl(2,3,3,4,4\bigr)\) and \(\bigl(2,3,4,4,4\bigr)\) both have image defect \(2\) and fixed-point set \(\{4\}\), but their stabilization indices are respectively \(3\) and \(2\). The novelty claim is the joint defect/time recurrence, full time support and extremal time-fiber count, combined with the exact modal-commutation characterization.

Closest later comparisons include a logarithmic typical power-stabilization law for uniformly random monotone finite-chain contractions (published mathematical record dated November 2026) and exact initial-versus-eventual image-rank fibers for directed-path weak endomorphisms. Neither statement provides the joint **exact finite** image-defect/power-index histogram for the strict top-fixed (open) submonoid. An independent-products Bernoulli convolution theorem concerns products of *different independently sampled* transformations rather than repeated powers of a single map. The present theorem does not claim novelty for the established asymptotic logarithmic scale or for any of those enumerations.

## Limitations
Only upper-set finite chains and simultaneous continuity/openness (the two-sided commutation scheme) are treated, not arbitrary Alexandrov preorders, all continuous monotone maps, or the entire directed-path weak-endomorphism monoid. No asymptotic fluctuation theorem, limiting distribution for centered \(\tau\), or general temporal-model complexity bound is asserted. The recursion is an exact finite answer, not a simple closed binomial form for every coefficient. Although the most relevant accessible primary results and nearby records were compared by mathematical implication, a broader transformation-semigroup iterate-enumeration theorem could conceivably subsume the recurrence. Literature priority and correctness have not undergone independent mathematical validation.

## References
1. N. C. Vooijs and D. Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, LIPIcs 380, article 81 (first verified public release July 9, 2026), https://doi.org/10.4230/LIPIcs.LICS.2026.81 .
2. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, arXiv:2407.05084v1 (first public July 6, 2024), https://arxiv.org/html/2407.05084v1 .
3. A. D. Adeshola and A. Umar, *Combinatorial results for certain semigroups of order-preserving full contraction mappings of a finite chain*, arXiv:1303.7428v2 (first public March 29, 2013), https://arxiv.org/html/1303.7428v2 .
