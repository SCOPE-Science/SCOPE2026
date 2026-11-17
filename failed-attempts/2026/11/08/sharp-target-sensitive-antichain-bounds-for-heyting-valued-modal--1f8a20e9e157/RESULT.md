# Sharp target-sensitive antichain bounds for Heyting-valued modal certificates

## Finding

Let \(L\) be any finite Heyting algebra, \(P=J(L)\) its poset of nonzero join-irreducible elements, and \(I(a)=\{j\in P:j\le a\}\). Define the **missing-boundary number**
\[
 b_L(a)=\bigl|\operatorname{Min}(P\setminus I(a))\bigr|,
 \qquad w_L=\operatorname{width}(P).
\]
The minimum of an empty set is understood to be empty, so \(b_L(1)=0\). For every (possibly empty) family \(S\subseteq L\), with \(m=\bigwedge S\), one can select \(S_0\subseteq S\) with \(\bigwedge S_0=m\) and \(|S_0|\le b_L(m)\le w_L\). **For each possible target \(m\), the target-dependent bound \(b_L(m)\) is the least universal bound**: some family meeting to \(m\) requires that many members. In particular the global meet breadth of \(L\) equals \(w_L\).

Under the ordinary crisp-accessibility semantics of Fitting's finite Heyting-valued modal logic, a boxed formula \(\Box\psi\) with value \(m\) at a world has an exact-value witness among at most \(b_L(m)\) of its successors. If \(\varphi\) has modal depth \(d\) and \(s\) distinct boxed subformulas, then a labelled, rooted, edge-pruned tree of depth at most \(d\) preserves the root's **exact** \(L\)-value of \(\varphi\) and has at most \(s w_L\) children at each node. More precisely, at a copy of a world \(x\) at depth \(t\), the bound is the sum of \(b_L(\llbracket\Box\psi\rrbracket_M(x))\) over boxed subformulas whose modal depth is at most \(d-t\). For each tuple \(m_1,\ldots,m_s\in L\), this sum is **sharp already on one-step stars** for simultaneously preserving the specified box values; using exact-value tests, a single depth-one formula can force all these witnesses to remain under edge pruning with valuations inherited from the source.

## Assumptions and scope

A finite Heyting algebra is a finite bounded distributive lattice equipped with its Heyting implication. The poset \(P\) is finite, and Birkhoff's downset representation identifies \(L\) with the lattice of downsets of \(P\). The notation \(\operatorname{Min}\) means minimal elements in the induced partial order, not smallest integers. Meets of empty families equal \(1\).

A Kripke model is \(M=(W,R,V)\) with an arbitrary nonempty set \(W\), a **crisp** binary relation \(R\), and atomic values in \(L\). Formula values are evaluated by the Heyting operations, exact tests \(T_a\), and
\[
\llbracket\Box\psi\rrbracket_M(x)=\bigwedge_{xRy}\llbracket\psi\rrbracket_M(y).
\]
The empty successor meet equals \(1\). A certificate here is a tree of copies of source worlds, with every tree edge mapped to an actual source edge and valuations inherited through the copying map. It is **not** claimed that such a certificate minimizes world count among all unrelated models or after arbitrary changes to valuations.

## Proof

**1. Exact local lattice compression.** Write \(D_a=I(a)\). Birkhoff representation gives \(D_{\bigwedge S}=\bigcap_{a\in S}D_a\). Let \(m=\bigwedge S\) and \(Q=\operatorname{Min}(P\setminus D_m)\). The complement of the downset \(D_m\) is an upset, and every element outside \(D_m\) lies above an element of \(Q\). For each \(q\in Q\), choose \(a_q\in S\) such that \(q\notin D_{a_q}\). Such an element exists, since otherwise \(q\in\bigcap_{a\in S}D_a=D_m\). Since \(D_{a_q}\) is a downset omitting \(q\), it also omits every element above \(q\). Thus the intersection of the chosen \(D_{a_q}\)'s excludes all of \(P\setminus D_m\). It contains \(D_m\) because each chosen member belongs to \(S\). Hence this intersection equals \(D_m\). The chosen family has cardinality at most \(|Q|=b_L(m)\). When \(S=\varnothing\), \(m=1\) and \(Q=\varnothing\), so the same proof holds.

**2. Sharpness for each target.** Fix \(m\in L\), let \(Q=\operatorname{Min}(P\setminus D_m)\), and for every \(q\in Q\) take the downset \(D_q^*=P\setminus\mathord{\uparrow}q\). Its corresponding lattice element is \(a_q^*\). Because \(P\setminus D_m\) is generated upward by \(Q\), the intersection of all \(D_q^*\) equals \(D_m\). If \(a_q^*\) is omitted, then \(q\) belongs to every remaining downset: distinct elements of \(Q\) are incomparable. The remaining meet therefore strictly exceeds \(m\). Exactly \(|Q|\) members are indispensable, including the vacuous zero-member case \(m=1\). As \(Q\) is an antichain, \(b_L(m)\le w_L\). Conversely, any maximum antichain \(A\subseteq P\) can occur as \(Q\), by choosing the target downset \(P\setminus\mathord{\uparrow} A\). Therefore the global optimum is exactly \(w_L\).

**3. Sharp simultaneous selection.** For \(s\ge1\) fixed targets \(m_i\in L\), set \(Q_i=\operatorname{Min}(P\setminus D_{m_i})\). Given arbitrary collections of successor-value vectors \(\bigl(v_1(y),\ldots,v_s(y)\bigr)\in L^s\) with coordinatewise meets \(m_i\), apply step 1 to each coordinate. The union of the selected successor sets has at most \(\sum_{i=1}^{s}|Q_i|\) members and preserves all coordinatewise meets. Adding other original successors cannot change those meets, because the full meet is already attained.

For the converse, form a finite star with one leaf \(y_{i,q}\) for each \(i\in\{1,\ldots,s\}\) and \(q\in Q_i\). At \(y_{i,q}\), assign \(V(p_i)=a_q^*\), and assign \(V(p_j)=1\) whenever \(j\ne i\). The root has an edge to every leaf and no other edges. Its value of \(\Box p_i\) is exactly \(m_i\). Deleting the edge to \(y_{i,q}\) causes \(\llbracket\Box p_i\rrbracket\) to strictly exceed \(m_i\), while other boxes cannot repair this. In the language with crisp exact-value tests, the depth-one formula
\[
 \Phi=\bigwedge_{i=1}^{s}T_{m_i}(\Box p_i)
\]
has root value \(1\) on the star and value \(0\) after deleting any nonempty set of its edges (since a deleted edge includes an indispensable leaf). Thus the bound \(\sum_i b_L(m_i)\) is exact even for preserving the value of one formula, provided valuations must be inherited and edges may only be pruned. The same construction gives sharp \(s w_L\) by taking targets whose missing-boundary antichains have width \(w_L\).

**4. Arbitrary modal depth.** Let \(d\) be the modal depth of \(\varphi\). At each copied world at tree depth \(t<d\), apply step 3 to all boxed subformulas \(\Box\psi\) of \(\varphi\) with modal depth at most \(d-t\), recording the actual source value of each box as its target. Introduce children corresponding to the union of chosen source successors; recursively process them until depth \(d\). The tree is finite, and the number of children at each node is bounded by the target-sensitive sum in the finding. A structural induction, restricted at tree depth \(t\) to subformulas of modal depth at most \(d-t\), shows preservation of their values: atoms and propositional operations are inherited, while each box's selected children attain its original meet; any extra selected children are also original successors, so they do not alter it. In particular \(\varphi\)'s exact value is preserved at the root. If \(B=s w_L\), the total number of tree nodes is at most \(1+B+\cdots+B^d\), interpreted as one node when \(B=0\). No finite-model assumption on the source is required because the truth-value algebra is finite and each selected witness set is finite.

## Verification

The independent Python checker `checker.py` implements downset lattices of small finite posets and tests the target-dependent bound against brute-force minimum-subfamily enumeration. It tests sharp constructions for all targets, and the indispensability of every edge in all two-box sharp stars for all naturally topologically labelled four-element posets generated by the code. Run:

```text
python3 checker.py
```

Expected deterministic output:

```text
LOCAL_MEET_BOUND_OK families_checked 10556 sharp_targets 406 small_ideals 49 observed_min_size_max 3
JOINT_STAR_SHARPNESS_OK
```

The family test is exhaustive for posets with at most three points and samples families for every generated four-point poset. This is computational corroboration only; steps 1–4 supply the proofs for all finite Heyting algebras and all depths.

## Relationship to prior work

Das, Ray and Mali (first public preprint August 6, 2026), Section 5, prove height-sensitive meet compression \(h(L)-1\) and the resulting formula-dependent exact-value tree certificates. The present statement **does not claim that finite certificates, Birkhoff's representation, or lattice breadth are new**. It identifies the exact target-sensitive witness number and shows a tight one-step modal obstruction requiring the sum of those numbers for simultaneous boxes. The sharp global constant is \(\operatorname{width}(J(L))\), not \(h(L)-1\). For an \(h\)-element chain, the earlier upper bound is \(h-1\), whereas the sharp constant here is \(1\), regardless of \(h\). For a Boolean truth-value algebra with \(r\) atoms, the sharp constant is \(r\). Birkhoff's classical representation and the older finite-valued modal framework are used as established ingredients.

## Limitations

This result concerns finite **distributive** truth-value lattices, crisp accessibility, an exact meet-based box and source-labelled edge-pruning certificates. Its sharpness is about retaining edges from a given model while inheriting valuations, not about minimum arbitrary countermodel size. For the single-formula lower bound, exact truth-value tests are part of the language. The model-free lattice compression result does not require such tests. The claim does not cover fuzzy-valued accessibility, non-distributive lattices or non-meet-based modalities. Historical-priority uncertainty remains for the combination of lattice breadth and finite-valued modal certificate bounds; independent expert assessment has not been performed.

## References

1. L. K. Das, K. S. Ray and P. C. Mali, *A Bitopological Approach to Finite Reduction and Bounded Exact-Value Certificates for Fitting's Finite Heyting-valued Modal Logic*, arXiv:2608.05550v1, August 6, 2026, especially Section 5. https://arxiv.org/abs/2608.05550
2. G. Birkhoff, *Lattice Theory*, classical finite distributive-lattice representation theorem (standard result); see also B. A. Davey and H. A. Priestley, *Introduction to Lattices and Order*, second edition, Cambridge University Press, 2002.
3. M. C. Fitting, *Many-Valued Modal Logics*, Fundamenta Informaticae 15 (1991), 235–254, https://doi.org/10.3233/FI-1991-153-404.
4. A. Kurz, W. Poiger and B. Teheux, *Many-valued coalgebraic logic over semi-primal varieties*, Logical Methods in Computer Science 20(3) (2024), arXiv:2308.14581, https://arxiv.org/abs/2308.14581 (background on a distinct coalgebraic framework).
