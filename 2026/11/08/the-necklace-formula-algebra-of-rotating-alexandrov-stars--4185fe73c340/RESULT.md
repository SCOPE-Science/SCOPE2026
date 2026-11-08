# The necklace formula algebra of rotating Alexandrov stars

## Finding
For every integer \(k\ge 0\) and \(m\ge1\), the full Boolean dynamic-topological formula algebra on a rooted Alexandrov star whose \(m\) leaves rotate cyclically has exactly
\[
2^{\,Q^m+Q N_m(Q)-Q}
\quad\text{elements},\qquad
Q=2^k,\qquad
N_m(Q)=\frac1m\sum_{j=0}^{m-1}Q^{\gcd(m,j)}
=\frac1m\sum_{d\mid m}\varphi(d)Q^{m/d}.
\]
Here formula equivalence means agreement at every world of the fixed dynamical system under **every** Boolean valuation of the \(k\) propositional variables. The count is valid with spatial closure, next, and eventually all available; removing eventually does not alter it. There are \(Q^m+Q N_m(Q)-Q\) distinguishable pointed valuation types and explicit formulas defining them one by one. The same theorem holds with spatial interior in place of closure, since the languages are Boolean.

## Assumptions and scope
Fix \(k\ge0\), \(m\ge1\), and a \(Q=2^k\)-element set \(A\) of atomic colors. The poset \(P_m=\{r\}\cup\{0,\ldots,m-1\}\) has precisely the strict comparisons \(r<i\) for each leaf \(i\); equip it with the Alexandrov topology of upsets. Let the homeomorphism \(f\) fix \(r\) and send leaf \(i\) to \(i+1\pmod m\). An arbitrary valuation assigns a Boolean value to each of the \(k\) propositional variables at every point (no persistence restriction). These values define the atomic color \(c(x)\in A\).

Formulas are built using propositional variables, Boolean constants \(\top,\bot\), negation, conjunction, disjunction, and the operations \(\Diamond\), \(\bigcirc\), \(\mathsf F\). The latter have the precise interpretations
\[
\begin{aligned}
x\models\Diamond\phi&\iff (\exists y\ge x)\ y\models\phi,\\
x\models\bigcirc\phi&\iff f(x)\models\phi,\\
x\models\mathsf F\phi&\iff (\exists j\ge0)\ f^j(x)\models\phi.
\end{aligned}
\]
The first is topological closure for the chosen upsets topology. Let \(\Box\phi:=\neg\Diamond\neg\phi\). The Boolean constants make the zero-variable case meaningful.

Two formulas are identified only if they agree on this single fixed frame across **all** color assignments and all points. The theorem does not assert equivalence for arbitrary Alexandrov systems.

## Proof
**1. The candidate semantic types.** For a leaf \(i\), record its marked cyclic word
\[
 w_i=(c(i),c(i+1),\ldots,c(i+m-1))\in A^m,
\]
with indices modulo \(m\). For the root, record \((a,[w])\), where \(a=c(r)\) and \([w]\) is the necklace (rotation-orbit) of the leaf-color word. At a leaf, \(\Diamond\) is the identity and \(\bigcirc\) rotates its marked word. At the root, \(\bigcirc\) fixes the root; \(\Diamond\) tests the root and **all** leaves, and the set of marked leaf words depends only on the necklace. In addition, \(\mathsf F\) at the root is the identity, and at a leaf it tests the entire cyclic orbit of the marked word. An induction on formulas therefore shows that all leaves with equal marked words are indistinguishable and all roots with equal pairs \((a,[w])\) are indistinguishable.

There is one overlap: if the entire leaf word is constant \(a^m\) and the root has color \(a\), then every point has the same atomic color. Every operation preserves this common truth value across points, so the root type \((a,[a^m])\) is equivalent to the leaf type \(a^m\). These are \(Q\) collisions.

**2. Explicit defining formulas (no further collisions).** For \(a\in A\), let \(C_a\) be the conjunction of the \(k\) signed propositional literals prescribing color \(a\), with \(C_a=\top\) when \(k=0\). For a marked word \(w=(w_0,\ldots,w_{m-1})\) put
\[
 E_w:=\bigwedge_{j=0}^{m-1}\bigcirc^j C_{w_j}.
\]
Define the root-only color-disagreement detector
\[
\Delta:=\bigvee_{\ell=1}^k
 \bigl[(p_\ell\wedge\Diamond\neg p_\ell)
 \vee(\neg p_\ell\wedge\Diamond p_\ell)\bigr],
\]
with an empty disjunction interpreted as \(\bot\). It is false at every leaf, and at the root it is true precisely when some leaf's color differs from the root's color.

For any *nonconstant* marked leaf word \(w\), the formula \(E_w\) defines exactly that leaf type (it is false at a root because next fixes the root, hence a root's temporal color word is constant). For a constant word \(w=a^m\), the formula \(E_w\wedge\Box C_a\) defines exactly that leaf type **including** the indistinguishable diagonal root \((a,[a^m])\): at any other root with temporal color \(a\), some leaf differs and \(\Box C_a\) fails.

For a root type \((a,[w])\) with \([w]\ne[a^m]\), define
\[
 R_{a,[w]}:= C_a\wedge\Delta\wedge
 \Box\left(\Delta\vee\bigvee_{v\in[w]}E_v\right).
\]
This formula fails at every leaf because \(\Delta\) does. At a root, the root conjunct \(\Delta\) holds exactly when its leaf colors are not all \(a\); the box conjunct then requires every leaf to have marked word in \([w]\), hence requires the leaf necklace to be exactly \([w]\). Conversely, for any root with this color and necklace, the formula holds. Consequently the listed characteristic formulas are mutually exclusive and each semantic type is realized by a valuation and a world.

**3. Full algebra and count.** There are \(Q^m\) marked leaf words and \(Q N_m(Q)\) colored-root necklace pairs; exactly the \(Q\) diagonal pairs identified in Step 1 overlap. Thus the number of distinguishable types is
\[
 T_{k,m}=Q^m+QN_m(Q)-Q.
\]
Each characteristic formula denotes one of these types. The disjunction of finitely many characteristics denotes any desired subset of the \(T_{k,m}\) types. The invariant-type argument gives an injection from formula equivalence classes into the power set of types, and the characteristics give surjectivity. Hence the algebra is the full Boolean algebra of size \(2^{T_{k,m}}\). Burnside's lemma applied to cyclic shifts gives the displayed formula for \(N_m(Q)\).

Finally \(f^m=\operatorname{id}\), so
\[
\mathsf F\phi\equiv\bigvee_{j=0}^{m-1}\bigcirc^j\phi
\]
on this system. No extra classes arise by adding eventually.

## Verification
The self-contained `checker.py` enumerates every world and every Boolean valuation for \((k,m)=(0,1),(0,3),(1,1),(1,2),(1,3),(1,4),(1,5),(2,1),(2,2),(2,3),(3,1)\). It computes a modal partition by **independent iterative bisimulation refinement**, whose signatures record atomic colors, the successor class under next, and the set of closure-successor classes. It verifies the predicted \(T_{k,m}\) for all 11 cases (2022 pointed valuations total) and evaluates the explicit defining formulas for eight cases. It also tests representative nested formulas containing eventuality. Run `python3 checker.py`; expected final line: `DYNAMIC_ALEXANDROV_NECKLACE_ALGEBRA_OK`.

The mathematical proof, not the finite checker, establishes the theorem for every \(k,m\). At \(k=1\), the type counts for \(m=1,\ldots,5\) are \(4,8,14,26,46\), yielding formula-algebra sizes \(16,256,16384,2^{26},2^{46}\). For \(k=0\), there is one type and exactly two formulas classes for every \(m\).

## Relationship to prior work
Vooijs and Fernández-Duque (LICS 2026) supply the general syntax, semantics, and computable axiomatizability results for Alexandrov dynamic topological logic. Their general axiomatizability results are not the present exact fixed-dynamical-system formula algebra. The counting of cyclic necklaces by Burnside's lemma is classical; here it combines with explicit modal characteristic formulas and a non-obvious diagonal root/leaf identification. Contemporary work on dynamic polyhedral logic addresses a different ambient class and does not supply this exact algebra count in the material inspected. Exact equality, not just an upper bound, requires Step 2.

## Limitations
The frame must be the finite Alexandrov **rooted star**, and the dynamics must be the specified cyclic permutation fixing the root; arbitrary functions or higher-height posets are not covered. The result is formula equivalence across all unrestricted valuations on one fixed frame, not the number of syntactic formulas or a completeness theorem for a frame class. Boolean constants are part of the signature. Finite executable tests cannot replace the all-parameters proof. Historical priority is supported by the inspected sources, not certified against all unpublished or unindexed literature. No independent mathematical or historical-priority audit has occurred.

## References
- Niels C. Vooijs and David Fernández-Duque, *Axiomatizability of Alexandrov Dynamic Topological Logic*, LICS 2026, DOI: 10.4230/LIPIcs.LICS.2026.81, publicly dated July 9, 2026. https://doi.org/10.4230/LIPIcs.LICS.2026.81
- *Dynamic Polyhedral Logic* (2026), arXiv:2608.25691, relevant general dynamic-topological background; only metadata and abstract were accessible for this comparison. https://arxiv.org/abs/2608.25691
- Burnside's orbit-counting lemma, applied here directly to the action of cyclic rotations on words.
