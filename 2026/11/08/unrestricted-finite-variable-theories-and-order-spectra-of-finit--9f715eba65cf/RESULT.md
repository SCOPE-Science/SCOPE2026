# Unrestricted finite-variable theories and order spectra of finite weak orders

## Finding
Let \(W(n_1,\ldots,n_h)\) be the strict partial order formed as the ordinal sum of \(h\ge1\) nonempty finite antichains of respective sizes \(n_i\ge1\): elements of an earlier level are strictly below every element of a later level, while elements of one level are mutually incomparable. These are the nonempty finite *strict weak orders*. Work in the language consisting only of equality and the strict relation \(<\), without counting quantifiers, and permit arbitrary quantifier depth.

For every integer \(k\ge2\), the following is an exact equivalence criterion:
\[
W(n_1,\ldots,n_h)\equiv_{\mathrm{FO}^{k}}W(m_1,\ldots,m_j)
\quad\Longleftrightarrow\quad
h=j\ \text{and}\ \min(n_i,k)=\min(m_i,k)\ \text{for all }1\le i\le h.
\]
All nonempty finite strict weak orders are equivalent with one variable. For fixed height \(h\), exactly \(k^h\) different theories occur at each width \(k\ge2\). Each theory has a unique minimum-order representative within the family, up to isomorphism, given by truncating every level size at \(k\). The sharp maximum size of such a minimum representative at fixed height \(h\) is \(hk\). The least distinguishing width of a particular structure relative to all finite strict weak orders is \(1+\max_i n_i\). The width hierarchy is strict at every step from one to two variables onward.

There are two different natural enumerations. Let \(r_k(N)\) be the number of theories having a minimum representative of exactly \(N\) elements, and let \(u_k(N)\) be the number of theories **realized** by at least one strict weak order of exactly \(N\) elements. Put \(A_k(z)=z+\cdots+z^{k-1}\) and \(B_k(z)=z+\cdots+z^k\). Then
\[
1+\sum_{N\ge1}r_k(N)z^N=\frac{1}{1-B_k(z)},
\qquad
\sum_{N\ge1}u_k(N)z^N
=\frac{A_k(z)}{1-A_k(z)}
+\frac{1}{1-z}\left(\frac{1}{1-B_k(z)}-\frac{1}{1-A_k(z)}\right).
\]
For \(k=2\), the first twelve values of \(u_k(N)\), beginning with \(N=1\), are \(1,2,4,8,15,27,47,80,134,222,365,597\). These are different from the minimum-representative spectrum, whose corresponding entries are \(1,2,3,5,8,13,21,34,55,89,144,233\).

## Assumptions and scope
All structures are finite and nonempty. The signature has equality and one strict binary order relation; no level labels, successor predicates, extra linear order, or counting operators are available. For a strict weak order, incomparability (including equality) is an equivalence relation whose classes are canonically linearly ordered. The levels are antichains and no orientation reversal is admitted when comparing structures. The meaning of \(\equiv_{\mathrm{FO}^k}\) is agreement on every first-order sentence using at most \(k\) *distinct reusable variable names*, with no bound on nesting depth.

## Proof
**1. Definability of each level with two variables.** Let \(P_0(x)\) abbreviate \(x=x\). Inductively form \(P_{i+1}(x)\) by \(\exists y\,(y<x\land P_i(y))\), using only the two variable names \(x,y\) and alternating their roles in nested occurrences. This is a legitimate pair of mutually recursive syntactic translations: at each step the inner formula has only its displayed parameter free, and other occurrences of a variable name are bound locally. The formula \(P_i(x)\) holds at exactly the levels whose zero-based index is at least \(i\). Indeed, a predecessor has at least \(i\) predecessor levels exactly when the current vertex has at least \(i+1\). Therefore \(L_i(x):=P_i(x)\land\neg P_{i+1}(x)\) isolates level \(i\). The height is detected by the family of sentences \(\exists x\,P_i(x)\).

**2. Detection of each truncated level size.** For any integer \(t\) with \(1\le t\le k\), a \(k\)-variable sentence expresses that at least \(t\) distinct vertices satisfy \(L_i\): quantify \(x_1,\ldots,x_t\), require pairwise distinctness, and conjoin \(L_i(x_j)\) for every \(j\). Inlining \(L_i(x_j)\) needs only \(x_j\) and one *locally bound* auxiliary name from the same available pool. Such inner binding does not capture the free occurrences in the other conjuncts. This sentence distinguishes any two corresponding level sizes with unequal truncations at \(k\). Different heights are likewise distinguished by the \(P_i\) sentences. This proves necessity.

**3. Arbitrarily long \(k\)-pebble strategy.** Suppose heights and capped size sequences agree. Maintain an injective correspondence between currently pebbled vertices, preserving each level index and equality. Such a map preserves all strict-order atoms because their truth depends only on the two level indices. When one pebble is moved, at most \(k-1\) other pebbles remain. If the chosen level has size below \(k\), its counterpart has exactly the same size, so an unused vertex exists precisely when needed. If it has size at least \(k\), both structures have at least \(k\) vertices on that level; among at most \(k-1\) occupied vertices, an unused reply always exists. Repeated source vertices are answered by their existing mates. The invariant is thus maintained indefinitely, proving sufficiency at unrestricted quantifier depth.

**4. Minimum representatives and width.** The capped sequence uniquely identifies an isomorphism class of minimum possible size inside its theory. Any larger entry can be reduced to \(k\) without changing the theory, and decreasing a capped entry below its value changes the theory by Step 2. At fixed height there are \(k\) independent choices per level, giving \(k^h\). For a structure with largest level size \(M\), width \(M+1\) recovers every level size; width at most \(M\) cannot distinguish it from the structure obtained by adding one element to a largest level. Width one sees no strict relation between distinct elements and cannot distinguish any nonempty structures. This also proves strictness: antichains of sizes \(k\) and \(k+1\) agree at width \(k\) and disagree at width \(k+1\), for every \(k\ge2\), while heights one and two distinguish widths one and two.

**5. Exact order spectrum.** A minimum representative is a nonempty finite word on the alphabet \(\{1,\ldots,k\}\), where the letters record capped level sizes; its size is the letter sum. This proves the first ordinary generating function. A word with every letter below \(k\) occurs on **exactly one** total vertex number, its own letter sum. A word containing at least one letter equal to \(k\) occurs at **every** vertex number at least its minimum sum, by increasing the corresponding original level size. The generating series for words with no capped letter \(k\) is \((1-A_k)^{-1}-1\), and for words with a capped letter \(k\) is \((1-B_k)^{-1}-(1-A_k)^{-1}\). Taking a cumulative sum of the latter coefficients (equivalently multiplying by \((1-z)^{-1}\)) proves the displayed series for \(u_k(N)\).

## Verification
Two standalone Python programs, `weakorder_verify.py` and `weakorder_spectrum_verify.py`, use only the Python standard library. The first computes stable Boolean \(k\)-tuple-extension colors across finite weak orders, comparing their exact finite-variable logical equivalence with the capped-word criterion. It also checks minimum-representative counts. The second enumerates compositions and checks the exact-order realization series. Reproduce using `python3 weakorder_verify.py` and `python3 weakorder_spectrum_verify.py`. Saved outputs accompany the source programs. The finite computations are corroborative; the unrestricted theorem is proved by the preceding definitions and indefinite pebble strategy.

## Relationship to prior work
Grohe and Schweikardt (2005) study expressiveness and succinctness of finite-variable logic on **linear orders**, not ordinal sums of variable-sized antichains. Mwesigye and Truss (2010) analyze **bounded quantifier-rank** equivalence of colored linear orders. Schwentick and Zeume (2011) analyze decidability and complexity of two-variable satisfiability with total preorders plus further order relations, rather than the exact unrestricted-depth equivalence classes in the pure strict language. Grohe and Otto (2012) provide general plain-pebble-game methods. Earlier bounded-rank computations for weak orders and published weak-order homotopy or mapping-space results also do not imply the full statement. No matching theorem was identified in the cited material; neither a finite set of searches nor the present mathematical proof establishes historical priority.

## Limitations
The theorem applies to the entire class of finite strict weak orders but not to arbitrary posets, infinite weak orders, richer relational signatures, counting logic, or a uniformly bounded quantifier-rank regime. The minimum-representative size and distinguishing width are **relative to this family**, not global invariants among all finite relational structures. No independently conducted mathematical audit has occurred. A more general previously published finite-variable composition theorem could subsume some or all of this result.

## References
1. M. Grohe and N. Schweikardt, *The Succinctness of First-Order Logic on Linear Orders*, *Logical Methods in Computer Science* **1** (2005), article 1:6; first preprint arXiv:cs/0502047 (9 February 2005), https://arxiv.org/abs/cs/0502047 .
2. F. Mwesigye and J. K. Truss, *Classification of Finite Coloured Linear Orderings*, *Order* **28** (2011), 387–397, first online 7 September 2010, https://doi.org/10.1007/s11083-010-9178-9 .
3. T. Schwentick and T. Zeume, *Two-Variable Logic with Two Order Relations*, *Logical Methods in Computer Science* **8** (2012), article 1:15; preprint submitted 7 October 2011, https://arxiv.org/abs/1110.1439 .
4. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, *CSL* (2012), 289–304; preprint first publicly available 9 April 2012, https://arxiv.org/abs/1204.1990 .
