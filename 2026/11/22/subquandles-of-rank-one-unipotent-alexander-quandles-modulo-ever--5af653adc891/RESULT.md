# Subquandles of rank-one unipotent Alexander quandles modulo every ambient automorphism

## Finding

Let \(p\) be any prime, \(f\ge 1\), \(V=\mathbb F_p^f\), and \(q=p^f\). On \(Q=V\times V\), use the finite Alexander quandle operation
\[
(a,b)\triangleright(c,d)=(a+b-d,b).
\]
Let \(\mathscr Z_{p,f}(z)=\sum_{[S]}z^{|S|}\), where \([S]\) ranges over orbits of **nonempty embedded subquandles** under the **full ambient quandle automorphism group**. This is not an enumeration of abstract subquandle isomorphism classes or of labeled subquandles.

Define, for any finite vector space \(H\) and invertible linear transformation \(M:H\to H\),
\[
\mathscr T_H(M;t)=\frac1{|H|}\sum_{\eta\in H}
\left[\prod_{C\in\operatorname{Cyc}(x\mapsto Mx+\eta)}
 (1+t^{|C|})-1\right].\tag{1}
\]
Here \(\operatorname{Cyc}\) is the complete set of disjoint permutation cycles of the indicated affine bijection of \(H\). The polynomial \(\mathscr T_H\) has nonnegative integer coefficients: it counts translation-classes of nonempty subsets of \(H\) fixed by the induced action of \(M\), by subset cardinality.

For each nonempty \(B\subseteq V\), put \(W_B=\operatorname{span}_{\mathbb F_p}\{b-d:b,d\in B\}\). For an affine bijection \(h=(L,v)\in\operatorname{AGL}(V)\) satisfying \(h(B)=B\), the space \(W_B\) is \(L\)-stable. Let \(\bar L_B\) be the linear map induced on \(V/W_B\). **The complete orbit polynomial** is
\[
\boxed{\displaystyle
\mathscr Z_{p,f}(z)=
\frac1{q\,|\operatorname{GL}_f(p)|}
\sum_{(L,v)\in\operatorname{AGL}(V)}
\sum_{\substack{\varnothing\ne B\subseteq V\\(L,v)(B)=B}}
\prod_{C\in B/\langle(L,v)\rangle}
\mathscr T_{V/W_B}\!\left(\bar L_B^{\,|C|};\ z^{|W_B|\,|C|}\right).
}\tag{2}
\]
The inner product is over the cycles of the affine map on its invariant support \(B\). Every term in (2) is explicitly determined by finite linear algebra and finite permutation cycles, for **all** primes and extension degrees.

The ambient automorphism group itself has the exact normal form
\[
\operatorname{Aut}(Q)=\left\{(a,b)\mapsto(L(a)+u(b),L(b)+v):
L\in\operatorname{GL}_f(p),\ v\in V,\ u:V\to V\right\},
\qquad |\operatorname{Aut}(Q)|=q^{q+1}|\operatorname{GL}_f(p)|.\tag{3}
\]
The standalone new claim is the orbit polynomial (2), its explicit consequences, and the reduction in its proof. The existence of general Alexander-quandle automorphism-group descriptions and the labeled fiber classification are prior mathematical ingredients, not claimed as independently new.

For \(f=1\) there is a compact closed formula. Let
\[
\mathscr B_p(t)=\frac{(1+t)^p+(p-1)(1+t^p)
+p\!\sum_{\substack{d\mid p-1\\d>1}}\!\varphi(d)(1+t)(1+t^d)^{(p-1)/d}}{p(p-1)}.\tag{4}
\]
This is the cycle-index polynomial of subsets of \(\mathbb F_p\) under \(\operatorname{AGL}_1(p)\). Then
\[
\boxed{\mathscr Z_{p,1}(z)=\mathscr B_p(z)+\mathscr B_p(z^p)-2-z^p.}\tag{5}
\]
Consequently the number of ambient-automorphism classes is \(2\mathscr B_p(1)-3\), asymptotic to \(2^{p+1}/[p(p-1)]\) along primes tending to infinity.

For \((p,f)=(2,2)\), the polynomial (2) is
\[
\mathscr Z_{2,2}(z)=z+z^2+z^3+2z^4+z^6+z^8+z^{12}+z^{16}.
\]
There are exactly \(9\) ambient orbits of nonempty subquandles, compared with \(119\) labeled subquandles. For \((p,f)=(3,2)\) there are exactly \(39\) ambient orbits among \(10{,}933\) labeled subquandles. In the prime-field cases \(p=2,3,5,7\), the orbit totals are \(3,5,9,17\), respectively.

## Assumptions and scope

Everything uses the **additive group** of \(V\), not its possible multiplicative field structure. Subquandles are nonempty subsets closed under the displayed binary operation (equivalently under both quandle operations, since they are finite). The full ambient automorphism group acts on **embedded** subquandles, preserving their cardinalities. In (1), the empty subset is excluded by subtraction of \(1\). In (2), the empty base support is excluded. \(\mathscr T_H\) for the zero-dimensional space \(H=0\) is \(t\), so boundary supports with \(W_B=V\) are included. All sums and products are finite; no genericity, odd-characteristic, or semisimplicity assumptions are imposed.

## Proof

**1. Exact ambient automorphism action.** Each right translation fixes the second coordinate and translates first coordinates by \(b-d\). As \(d\) varies over \(V\), the inner permutation group acts transitively on every row \(V\times\{b\}\) and never moves between rows. Thus every quandle automorphism \(g\) permutes these rows: \(g(a,b)=(F_b(a),h(b))\), with a permutation \(h\) of \(V\). Preservation of the operation gives, for all \(a,b,d\in V\),
\[
F_b(a+b-d)=F_b(a)+h(b)-h(d).\tag{6}
\]
For any fixed \(b\), as \(d\) varies, equation (6) says that \(F_b\) is additive-affine, with a bijective additive slope \(L_b\in\operatorname{GL}_f(p)\). It also implies \(h(d)=L_b(d)+h(b)-L_b(b)\) for every \(d\). This expression for the **same** function \(h\) for different \(b\) forces all slopes \(L_b\) equal to a single invertible additive \(L\), and \(h(d)=L(d)+v\). Writing \(u(b)=F_b(0)\) yields (3). Conversely, every displayed map preserves the operation and is bijective. Its parameters are unique, hence the group order.

**2. Subquandle fibers.** For \(\varnothing\ne S\subset Q\), set \(B=\{b:S_b\ne\varnothing\}\) and \(S_b=\{a:(a,b)\in S\}\). Closure gives \(S_b+(b-d)\subseteq S_b\) for every \(b,d\in B\). Finiteness makes this equality. Thus each \(S_b\) is an arbitrary **nonempty union of \(W_B\)-cosets**. Conversely all such independent choices preserve the operation. This labeled fiber classification and its labeled cardinality enumerator were published previously; the contribution below takes the quotient by the full, larger ambient automorphism group.

**3. Quotient by independent row shears.** The normal subgroup of (3) with \(L=I\) and \(v=0\) consists of all row-dependent translations \(u:V\to V\). Fix \(B\). The subgroup acts independently on the fibers \(S_b\). Upon passing to \(H_B=V/W_B\), a fiber corresponds uniquely to a nonempty subset \(A_b\subseteq H_B\), of size \(s_b\), with original size \(|W_B|s_b\). Row shears identify two choices exactly when they differ by a translation of \(H_B\), independently at each \(b\). Therefore, after quotienting by the shears, the data are \(B\) together with one **translation-class of a nonempty subset of \(H_B\)** for each \(b\in B\). This is a bijection of finite sets, preserving total size \(|W_B|\sum_b s_b\).

**4. Remaining affine action.** The quotient of the full automorphism group by the row shears is \(\operatorname{AGL}(V)\), acting on \(B\) by \(h=(L,v)\), and on its coset-label subset-classes through the induced linear map \(\bar L_B\). Indeed \(W_{h(B)}=L(W_B)\); the translation \(v\) on base rows does not create a translation of the first-coordinate quotient. If \(h(B)=B\), its cycles \(C\) on \(B\) are independent. All labels on a cycle of length \(\ell\) are determined from a single one; consistency after \(\ell\) steps says its translation-class must be fixed by \(\bar L_B^{\ell}\). Its weight is \(z^{|W_B|\ell s}\) for a label of size \(s\).

**5. Fixed translation-classes.** For any finite \(H\), \(M\in\operatorname{GL}(H)\), and size \(s\), the action of the translation group \(H\) on \(s\)-subsets commutes with \(M\) at the orbit level. The number of its orbits fixed by \(M\) is, by the twisted form of Burnside's lemma, \(1/|H|\) times the sum over \(\eta\in H\) of the number of \(s\)-subsets fixed by the affine permutation \(x\mapsto Mx+\eta\). Subsets fixed by a finite permutation are unions of its disjoint cycles; their ordinary size polynomial is the product in (1). This proves the precise interpretation and integrality of \(\mathscr T_H\).

**6. Burnside over supports and cycles.** Apply weighted Burnside to the residual \(\operatorname{AGL}(V)\) action on the shear-orbit data of step 3. A fixed configuration must have invariant nonempty support \(B\), and for each cycle \(C\) in step 4 its allowed labels contribute the factor \(\mathscr T_{H_B}(\bar L_B^{|C|};z^{|W_B||C|})\) of step 5. Multiplying factors, summing fixed invariant supports, and averaging over the \(q|\operatorname{GL}_f(p)|\) affine maps gives (2) with no overcounting. This completes the all-field theorem.

**7. Prime-field simplification and growth.** For \(f=1\), a singleton support gives \(W_B=0\), and the ambient automorphisms reduce its fiber subsets up to the full one-dimensional affine group. This contributes \(\mathscr B_p(z)-1\), including all nonempty fiber cardinalities. A support of at least two base rows gives \(W_B=V\), so every selected row must be full. These contribute \(\mathscr B_p(z^p)-1-z^p\). The cycle structures of the order-\(p(p-1)\) affine group are: the identity, \(p-1\) nonzero translations each with one \(p\)-cycle, and for every divisor \(d>1\) of \(p-1\), exactly \(p\varphi(d)\) elements with a fixed point and \((p-1)/d\) cycles of length \(d\). Thus (4)–(5) follow. Every nonidentity affine map has at most \((p+1)/2\) cycles when \(p\) is odd, so their total weighted fixed-subset contribution at \(t=1\) is \(O(p^2 2^{(p+1)/2})\), versus \(2^p\) from the identity. Hence \(\mathscr B_p(1)\sim2^p/[p(p-1)]\), yielding the announced asymptotic.

## Verification

The self-contained standard-Python program `verify.py` constructs the finite operation and automorphism action independently and checks the following:

- For \(p=2,3\) with \(f=1\), it enumerates **every permutation** of the \(p^2\)-point quandle, checks preservation of all products, and proves the calculated finite-group list matches exactly the normal form (3). It separately enumerates every nonempty subset and tests actual quandle closure.
- For \(p=5,7\) with \(f=1\), it directly computes orbits from explicit generators of the full group, comparing every cardinality coefficient with (5). It checks the affine-subset cycle index against direct affine-subset orbits for primes \(2,3,5,7,11,13,17,19\).
- For \(V=\mathbb F_2^2\) and \(\mathbb F_3^2\), it evaluates the complete independent nested Burnside sum (2) and constructs ambient orbits directly by finite permutation generators. Both computations agree in **every size coefficient**. For \(\mathbb F_2^2\), it additionally enumerates all \(2^{16}-1\) nonempty subsets and checks closure from the actual operation; it also directly checks the full \(6{,}144\)-element automorphism list.

The script prints `ALL_FIELD_BURNSIDE_CHECKS_PASSED`. Exhaustive checks are proofs for the stated **finite cases only**; the universally quantified result rests on steps 1–7.

## Relationship to prior work

Higashitani and Kurihara (arXiv:2210.16763, first publicly posted 2022-10-30, primary MSC 20N02) classify generalized Alexander quandles from finite groups and motivate the underlying algebraic setting; their investigated isomorphism types of quandles are not ambient orbit counts of all embedded subquandles.

Jedlička, Pilitowska, Stanovský and Zamojska-Dzienio (arXiv:1708.02362, 2017) characterize **quasi-affine quandles** and their abstract isomorphism types, using semiregular extensions and Burnside calculations for abstract structures. Their embedding/isomorphism theory is relevant background, but abstract isomorphism of two subquandles does **not** imply they are conjugate under an automorphism of the *fixed ambient quandle*; their inspected main theorems do not give (2). Their earlier affine-mesh isomorphism theorem (arXiv:1409.8396, 2014) provides a general structural framework capable of recovering part of step 1.

Hou, *Automorphism groups of Alexander quandles* (Journal of Algebra 344, 2011, DOI 10.1016/j.jalgebra.2011.06.027), already determines automorphism groups in general; accordingly (3) is used as an independently proved *ingredient* rather than an automorphism-group novelty claim. Its full paper could not be materially inspected from an available lawful open version; no assertion is made that its group formula is new.

The previously published exact result *Complete subquandle size distribution for rank-one unipotent Alexander quandles* (2026-10-18) proves the embedded **labeled** subquandle fiber classification and the all-field labeled cardinality generating function for the **identical objects**; its RESULT.md was inspected in full and expressly excludes automorphism-orbit enumeration. Formula (2) is the further full-automorphism quotient, refining the distinction between labeled counts and symmetry classes; previous classification alone does not numerically specify this quotient. A separate known result on **retraction images** of the same quandle counts only the much smaller subclass of embedded retracts, not all nonempty subquandles.

Amsberry and collaborators (arXiv:2304.09747, 2023) study lattice complementation and strongly complemented subquandles, not (2). The ordinary affine-subset cycle index, translation Burnside lemma, and earlier labeled subquandle classification are credited as existing methods rather than new discoveries.

## Limitations

Equation (2) is a **finite explicit summation algorithm**, not a single rational product or complexity bound uniform in \(f\). It does not claim abstract subquandle isomorphism classification, the full subquandle-lattice incidence poset, or analogous formulas for arbitrary Jordan types. Its finite computations do not replace the all-field argument. The result is original relative to the specific sources compared but historical priority cannot be established solely from search; an unindexed general orbit-enumeration theorem could subsume this specialization. The paper by Hou on general Alexander-quandle automorphisms remains an access-limited comparison, but that earlier general automorphism result is credited rather than asserted to be outside coverage.

## References

1. A. Higashitani and H. Kurihara, *Generalized Alexander quandles of finite groups and their characterizations*, first posted 2022-10-30, arXiv:2210.16763. https://arxiv.org/abs/2210.16763
2. P. Jedlička, A. Pilitowska, D. Stanovský and A. Zamojska-Dzienio, *Subquandles of affine quandles*, arXiv:1708.02362 (2017). https://arxiv.org/abs/1708.02362
3. P. Jedlička, A. Pilitowska, D. Stanovský and A. Zamojska-Dzienio, *The structure of medial quandles*, arXiv:1409.8396 (2014). https://arxiv.org/abs/1409.8396
4. X.-D. Hou, *Automorphism groups of Alexander quandles*, Journal of Algebra 344 (2011), 373–385. https://doi.org/10.1016/j.jalgebra.2011.06.027
5. *Complete subquandle size distribution for rank-one unipotent Alexander quandles*, published 2026-10-18, full result: https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-complete-subquandle-size-distribution-for-rank-one-unipotent-ale--288df6733df1/RESULT.md
6. K. J. Amsberry, J. A. Bergquist, T. A. Horstkamp, M. H. Lee, D. N. Yetter, *Complementation of Subquandles*, arXiv:2304.09747 (2023). https://arxiv.org/abs/2304.09747
