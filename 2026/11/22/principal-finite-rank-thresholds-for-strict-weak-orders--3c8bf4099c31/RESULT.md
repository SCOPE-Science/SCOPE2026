# Principal finite rank thresholds for strict weak orders

## Finding
Let \(\mathcal W\) be the hereditary class of all finite strict weak orders, including the empty order, in the language with one irreflexive binary relation \(<\). A strict weak order is an ordinal sum of nonempty antichains. Write a finite host as \(W(a_1,\ldots,a_h)\), where the positive integers \(a_i\) are the antichain-level sizes in increasing order.

For an induced finite substructure \(F\subseteq W\), let \(\operatorname{rk}_W(F)\) denote the one-point-extension rank relative to \(\mathcal W\), as defined precisely below. Define a finite positive-integer word recursively by
\[
B_0=(),\qquad B_t=(B_{t-1},t,B_{t-1})\quad(t\ge1),
\]
where parentheses in the second expression mean concatenation. Thus \(B_1=(1)\), \(B_2=(1,2,1)\), and \(B_3=(1,2,1,3,1,2,1)\).

**Principal witness theorem.** For every finite strict weak order \(W(a_1,\ldots,a_h)\) and integer \(t\ge0\),
\[
\operatorname{rk}_W(\varnothing)\ge t
\quad\Longleftrightarrow\quad
W(B_t)\text{ embeds as an induced substructure of }W
\quad\Longleftrightarrow\quad
\exists\,i_1<\cdots<i_{2^t-1}:\ a_{i_j}\ge (B_t)_j\ (1\le j\le 2^t-1).
\]
The empty pattern for \(t=0\) is universally embeddable. A finite strict weak order has a unique ordered level-size word up to isomorphism, so this supplies a complete structural decision criterion for all finite ranks.

**Exact sharp size law.** For every integer \(t\ge0\),
\[
\min\bigl\{|W|:\operatorname{rk}_W(\varnothing)\ge t\bigr\}
=2^{t+1}-t-2.
\]
The unique isomorphism type achieving that minimum is \(W(B_t)\). The first nonzero rank thresholds require respectively \(1,4,11,26,57,120\) elements. In particular, the largest rank on \(n\) elements is exactly the largest integer \(t\ge0\) satisfying \(2^{t+1}-t-2\le n\).

For \(h\ge1\), if all \(h\) levels have the same size \(a\ge1\), then
\[
\operatorname{rk}\bigl(W(\underbrace{a,\ldots,a}_{h\text{ levels}})\bigr)
=\min\left\{a,\left\lfloor\log_2(h+1)\right\rfloor\right\}.
\]
Thus height alone does not force growing one-point-extension rank in this hereditary class.

## Assumptions and scope
The order is strict, transitive, and has transitive incomparability: distinct elements are incomparable exactly when they belong to the same antichain level. Every two different levels are fully comparable, in the prescribed increasing direction. Embeddings preserve and reflect the strict order, so they are induced-substructure embeddings. A prime extension adds exactly one vertex and must belong to \(\mathcal W\). It can either join one of the existing incomparable levels of the marked structure or form a new level in one of its ordered gaps.

For a finite host \(W\), every induced \(F\subseteq W\) has rank at least zero. Recursively, \(\operatorname{rk}_W(F)\ge t+1\) means that **every** isomorphism type of prime extension \(F'\) in \(\mathcal W\) has some realization in \(W\), fixing \(F\) pointwise, with rank at least \(t\). This is the finite specialization of the López-Callejas–Navarro-Castillo rank. The rank of \(W\) means \(\operatorname{rk}_W(\varnothing)\); it is **not** the rank computed relative to the smaller class of linear orders or the class of pure equivalence relations.

For a possibly empty positive-integer word \(u=(u_1,\ldots,u_s)\), define
\[
\rho(())=0,\qquad
\rho(u)=\max_{1\le j\le s}
\min\left\{u_j,1+\rho(u_1,\ldots,u_{j-1}),1+\rho(u_{j+1},\ldots,u_s)\right\}.
\]
The formula is well founded because each recursive word is shorter. If \(F\) meets host levels \(i_1<\cdots<i_k\), write \(f_j=|F\cap A_{i_j}|\), \(b_j=a_{i_j}-f_j\), and let \(G_0,\ldots,G_k\) be the consecutive unmarked-level words strictly before, between and after those selected levels. The full relative-rank theorem is
\[
\boxed{\operatorname{rk}_W(F)=
\min\bigl(\{b_1,\ldots,b_k\}\cup\{\rho(G_0),\ldots,\rho(G_k)\}\bigr).}
\]
When \(F\) is empty, there is one gap, consisting of the entire level word, and the first set in the minimum is empty.

## Proof
**1. Classification of extension types.** The relation of incomparability (together with equality) is an equivalence relation, and its quotient is linearly ordered. In a prime extension of \(F\), the new vertex must either be incomparable with an existing selected class or comparable to all selected classes at a uniquely determined cut. Conversely each of these types is a finite weak order. Inside a host, joining selected class \(i_j\) consumes one of its \(b_j\) unused vertices; inserting a new class into gap word \(G_s\) chooses an unmarked host level of size \(u_j\), leaves \(u_j-1\) unused vertices of that new selected class, and splits the gap into its left and right subwords. No other resource changes.

**2. Relative-rank induction.** Simultaneously for all finite hosts, marked subsets and nonnegative integers \(t\), prove that rank at least \(t\) is equivalent to every selected-class capacity being at least \(t\) and every gap having \(\rho\)-value at least \(t\). At \(t=0\) this is automatic. Suppose it holds at \(t\). For a rank of at least \(t+1\), each selected-class extension type needs a reply of rank at least \(t\), forcing the corresponding capacity to be at least \(t+1\). Similarly, each gap-extension type needs a pivot with at least \(t\) unused same-level vertices after insertion and left and right gap values at least \(t\). Such a pivot exists exactly when that gap has \(\rho\)-value at least \(t+1\), by the displayed max–min recurrence. Conversely, if all original resources meet the \(t+1\) thresholds, reply to each requested type using its class or an appropriate gap pivot. The changed resource then meets threshold \(t\); all unchanged resources still do too, as the thresholds are monotone. The induction hypothesis gives a reply of rank at least \(t\). This closes both directions, including empty gaps and depleted classes. Taking the largest valid \(t\) proves the relative-rank formula and \(\operatorname{rk}_W(\varnothing)=\rho(a_1,\ldots,a_h)\).

**3. Recursive principal witness.** For any word \(u\), the recurrence yields
\[
\rho(u)\ge t\ (t\ge1)
\iff
\text{some position }j\text{ has }u_j\ge t,
\ \rho(u_{<j})\ge t-1,\ \rho(u_{>j})\ge t-1.
\]
Induct on \(t\). By the induction hypothesis the left and right subwords contain \(B_{t-1}\) as componentwise-bounded subsequences. Including the pivot of size at least \(t\) gives the word \(B_t\). Conversely, a subsequence witnessing \(B_t\) supplies a pivot and recursive witnesses on both sides. Thus \(\rho(u)\ge t\) if and only if \(B_t\) is embedded as a coordinatewise-bounded subsequence. Picking the required number of elements in each witness level realizes exactly the induced weak order \(W(B_t)\).

**4. Exact extremal count and uniqueness.** Let \(L_t\) be the length of \(B_t\), and \(N_t\) its sum. The recursion gives \(L_0=N_0=0\) and \(L_t=2L_{t-1}+1\), \(N_t=2N_{t-1}+t\). Hence \(L_t=2^t-1\) and \(N_t=2^{t+1}-t-2\). Every host of rank at least \(t\) contains \(W(B_t)\), so it has at least \(N_t\) vertices. At equality there are no other levels or extra vertices within selected levels, forcing exactly \(W(B_t)\); this host has rank at least \(t\), proving existence and uniqueness. When all level sizes equal \(a\), the pattern embeds precisely when its maximum letter \(t\) is at most \(a\) and its length \(2^t-1\) is at most \(h\), yielding the uniform-width formula.

**5. Decision procedure.** To test rank at least \(t\), construct \(B_t\) and greedily scan the host level sizes from left to right, matching each next pattern letter at the earliest host level at least that large. Greedy subsequence matching is complete by exchange: any later match can be moved to the earlier eligible level without invalidating subsequent matches. Testing all \(t\) up to \(\lfloor\log_2(h+1)\rfloor\) (and never beyond the maximum host level size) computes the exact rank using at most \(O(h\log(h+1))\) comparisons and \(O(h)\) working memory; the empty case has rank zero.

## Verification
The standalone standard-library program `weakorder_rank_verify.py` independently evaluates the extension-game minimax: at every marked state, it enumerates every possible prime-extension *type* and every available host reply. It compares the resulting game rank against the gap-and-capacity theorem, and separately compares whole-host ranks against the recursive word criterion and greedy canonical-pattern embedding test. All \(2{,}047\) positive compositions of sizes at most eleven, comprising \(627{,}231\) marked states, passed. An additional \(1{,}200\) randomized width words were compared; the unique minimal rank-two and rank-three words were confirmed by exhaustive enumeration at their sharp sizes. The program also checks the canonical patterns and sizes through rank six. Run `python3 weakorder_rank_verify.py` from a directory containing the extracted file. The included `verification_output.txt` records a successful run. Finite tests are corroboration, not the proof of the unbounded statement.

## Relationship to prior work
López-Callejas and Navarro-Castillo (2026) define this rank and compute it for finite **linear orders** relative to their own hereditary class; their formula is logarithmic in the number of points. Their linear-order interval method does not cover the new same-level extension type in weak orders. Kubiś and Shelah (2024 manuscript) introduce the general ordinal rank and show that, under amalgamation assumptions, finite rank thresholds admit finite witness lists; the principal **single** induced-witness characterization and its exact size sequence here are more specific and are not stated in the examined manuscript. A separately published classification of finite weak orders by unrestricted-depth finite-variable first-order theories studies pebble equivalence and capped level sizes; that is a different invariant from the one-point-extension rank considered here. Equality-relation ranks forget level order and likewise cannot determine this rank: the weak-order words \((2,1,1)\) and \((1,2,1)\) have identical unordered equivalence-class size multisets but respective weak-order ranks \(1\) and \(2\).

## Limitations
All quantifiers range over finite strict weak orders and finite induced marked substructures. The results do not determine transfinite ranks of countable weak orders, ranks relative to arbitrary posets, or ranks in a different signature or extension class. The historical comparison covers the identified and accessible sources, not every unpublished or unindexed result; a deeper priority audit may find a stronger earlier theorem. No independent mathematical validation is claimed.

## References
1. C. López-Callejas and J. Navarro-Castillo, *A rank function for Fraïssé classes and the rank property*, arXiv:2604.14461, first submitted 15 April 2026; https://arxiv.org/abs/2604.14461 and full text https://arxiv.org/html/2604.14461.
2. W. Kubiś and S. Shelah, *Evolution systems — an ordinal rank measuring universality*, manuscript dated 19 August 2024; https://users.math.cas.cz/kubis/pdfs/ranksEvasPS_ver2.pdf.
3. *Unrestricted finite-variable theories and order spectra of finite weak orders*, published 8 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-unrestricted-finite-variable-theories-and-order-spectra-of-finit--9f715eba65cf. This concerns finite-variable logic, not the ordinal rank.
