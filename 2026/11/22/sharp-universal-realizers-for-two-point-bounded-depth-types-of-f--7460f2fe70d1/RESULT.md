# Sharp universal realizers for two-point bounded-depth types of finite permutations

## Finding
For every integer \(d\ge 1\), in the first-order language consisting of equality and one unary function \(f\), restrict attention to finite nonempty structures in which \(f\) is a bijection. A **two-point term-equality type of depth \(d\)** is the truth-value assignment to every equality between the \(2(d+1)\) formal terms
\[
 x,f(x),\ldots,f^d(x),\quad y,f(y),\ldots,f^d(y)
\]
realized by an ordered pair \((x,y)\) in some such structure. Distinct types differ on at least one of these equalities. A permutation is **depth-\(d\) universal** if all types possible in any finite permutation are realized by its ordered pairs.

Exactly
\[
 T_d=2d^2+5d+2
\]
distinct types exist. The smallest depth-\(d\) universal finite permutation has exactly
\[
 U_d=\frac{(d+1)(5d+2)}{2}
\]
vertices. Up to isomorphism, **the unique minimizer** has two cycles of each length \(1,2,\ldots,d\), together with one cycle of every length \(d+1,d+2,\ldots,2d+1\). This statement classifies every type, not only the extremal size.

## Assumptions and scope
The vocabulary contains no predicates or constants beyond equality and the total unary operation. The operation is interpreted as a bijection. All universes are finite and nonempty, and all ordered pairs are allowed, including coincident points. The depth bound applies to **unary-term iteration**, not to quantifier rank. Only equality atoms are considered, so Boolean combinations do not distinguish any further pair profiles. There are no bound variables or quantifiers in the type language. The parameter \(d\) is any positive integer; the claim does not cover arbitrary nonbijective unary functions, additional operations, or unbounded term depth.

## Proof
**1. Unique interpretation of short visible cycles.** Every element of a finite permutation belongs to a directed cycle of some least length \(L\ge1\). Equalities among the terms of \(x\) alone reveal \(L\) exactly when \(L\le d\): the first positive return among shifts at most \(d\) is \(L\). When \(L>d\), all the first \(d+1\) terms of \(x\) are distinct. The same holds for \(y\). Record the **visible period** as \(L\in\{1,\ldots,d\}\), or as the symbol \(\infty\) for every larger actual period.

**2. Disconnected patterns.** When no cross-equality \(f^i(x)=f^j(y)\) occurs for \(0\le i,j\le d\), the complete type is specified by the ordered pair of visible periods. All \((d+1)^2\) possibilities occur by taking \(x\) and \(y\) from different cycles of the prescribed actual periods. We call these *no-cross* types. Note that these are observational types: a no-cross type may sometimes also occur with two points of a sufficiently large common cycle, but that observation does not change its truth pattern.

**3. Short common cycles.** Any cross-equality places \(x,y\) in the same cycle, hence gives them the same actual period \(L\). If \(L\le d\), each \(y=f^h(x)\), \(0\le h<L\), gives a distinct cross-equality pattern and visible period \(L\). Therefore the small-cycle cross types number
\[
 \sum_{L=1}^d L=\frac{d(d+1)}2.
\]

**4. Long common cycles.** If \(L>d\), write \(y=f^h(x)\) modulo \(L\), and define
\[
 D=\{i-j:\ 0\le i,j\le d,\ f^i(x)=f^j(y)\}.
\]
Then \(D=([-d,d]\cap (h+L\mathbb Z))\cap\mathbb Z\). Each signed difference in \([-d,d]\) occurs as \(i-j\), and the truth value for every pair of indices with the same difference is identical. Because \(L>d\), the interval \([-d,d]\) contains at most two integers in a single residue class modulo \(L\). Thus \(D\) is empty, a singleton, or a two-element set. The empty case has already been counted in step 2.

For \(|D|=2\), the two differences differ by exactly \(L\), uniquely recovering \(L\). This forces \(d+1\le L\le2d\). In that range exactly \(2d+1-L\) residue classes meet \([-d,d]\) twice. Consequently, the two-difference cross types number
\[
 \sum_{L=d+1}^{2d}(2d+1-L)=\frac{d(d+1)}2.
\]
For \(|D|=1\), the unique difference is any \(t\in[-d,d]\cap\mathbb Z\). All \(2d+1\) such singleton types occur with a common cycle of length \(2d+1\), taking \(h\) to be the residue of \(t\). These types are pairwise distinct, and no two coincide with the preceding classes, which have different self-equalities or numbers of cross-difference values. Adding the four disjoint classes yields
\[
 (d+1)^2+\frac{d(d+1)}2+\frac{d(d+1)}2+(2d+1)=2d^2+5d+2.
\]
Here 'four classes' refers to no-cross, short-cycle, double-difference, and singleton-difference types; each includes the stated number of types.

**5. Mandatory cycles in any universal permutation.** Fix \(1\le L\le d\). The no-cross type with both visible periods equal to \(L\) requires two *distinct* cycles of length exactly \(L\): a common cycle would yield cross-equalities, and any longer cycle would have the wrong visible period. Thus at least two cycles of each such length are needed. For each \(d+1\le L\le2d\), any double-difference type with differences separated by \(L\) forces a common cycle of length exactly \(L\). Finally, the singleton difference \(D=\{d\}\) forces a common cycle of length \(L\ge2d+1\): if \(L\le d\) the self-return is visible, while for \(d<L\le2d\) the additional difference \(d-L\) lies in \([-d,-1]\) and would also be present. These forced cycles are disjoint, so any universal model has at least
\[
 2\sum_{L=1}^d L+\sum_{L=d+1}^{2d}L+(2d+1)
 =\frac{(d+1)(5d+2)}2
\]
points.

**6. Attainment and uniqueness.** Build a permutation with exactly two cycles of every length through \(d\), and one of every length from \(d+1\) through \(2d+1\). Steps 3 and 4 show that it realizes every cross type: short cycles cover their offsets, lengths \(d+1\) to \(2d\) cover all double-difference cases, and the \((2d+1)\)-cycle covers every singleton. For each no-cross ordered visible-period pair, choose distinct cycles with those periods: use the two prescribed copies if both periods are the same short \(L\); use the appropriate short and long cycles for mixed periods; and, if both are \(\infty\), use the distinct long cycles of lengths \(d+1\) and \(2d+1\), present because \(d\ge1\). This realizes all types on exactly \(U_d\) points. At equality in the lower bound every forced cycle must have its minimum allowed length, with no spare points; therefore the cycle multiset is uniquely fixed. This proves all claims.

## Verification
The accompanying `verify_perm_pair.py` independently constructs the literal equality matrix of all \(2(d+1)\) evaluated terms for ordered pairs, compares the extremal cycle union with an overcomplete universal enumerator, and verifies the formulas for \(1\le d\le5\). It also checks that deleting any cycle of the proposed witness loses a type and exhaustively enumerates every permutation cycle partition of smaller order at depths \(d=1\) and \(d=2\). The recorded execution concludes `VERIFY_OK 1305`; the five predicted type counts are \(9,20,35,54,77\) and minimum orders are \(7,18,34,55,81\). These finite checks do not establish the infinitely quantified assertion; the proof above does.

## Relationship to prior work
Kuželka's recent paper (arXiv:2608.30580, first posted August 31, 2026) develops model counting with unary function symbols, finite functional digraph decompositions, and automorphism marking. Its permutation discussion (Section 4.2 and its later permutation-axiom extension) does not give an all-depth two-point equality-profile spectrum or the sharp universal permutation size and rigidity. Albert, Bouvel and Féray (arXiv:1808.05459) study first-order logics of permutations through different encodings and quantifier properties, not this bounded-term two-point saturation invariant. Campercholi, Tellechea and Ventura (arXiv:2303.17017) give general algorithms for quantifier-free definability and tuple isomorphism types in finite algebras, without these exact formulas. General unrestricted-depth finite-variable logical classifications do not directly imply the truncated term-equality enumeration. The result specializes familiar cycle decomposition to a precise optimal simultaneous-realization question; no blanket claim of priority beyond inspected material is made.

## Limitations
The result pertains only to finite permutations, the pure equality/function vocabulary, ordered two-point types, and finite positive term depth. It is not a formula-size or complexity lower bound, and it does not extend automatically to noninjective functions or additional relations. Finite computations are corroborative, not proof. Priority remains provisional against older results under alternative terminology; no independent audit or external certification has been performed.

## References
- Ondřej Kuželka, *Unary Functions, Automorphisms, and Unlabeled First-Order Model Counting*, arXiv:2608.30580 (2026), https://arxiv.org/abs/2608.30580. First publicly submitted 2026-08-31 UTC.
- Michael Albert, Mathilde Bouvel and Valentin Féray, *Two first-order logics of permutations*, arXiv:1808.05459 (2018), https://arxiv.org/abs/1808.05459.
- Miguel Campercholi, Mauricio Tellechea and Pablo Ventura, *Two algorithms to decide Quantifier-free Definability in Finite Algebraic Structures*, arXiv:2303.17017 (2023), https://arxiv.org/abs/2303.17017.
