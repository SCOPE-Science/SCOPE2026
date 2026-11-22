# A gcd phase transition in the deterministic complexity of one-branch modular-marker automata

## Finding

For any positive integers \(r,s\), define the binary language
\[
L_{r,s}=\bigl\{w\in\{a,b\}^*:w=ubv\text{ for some }u,v,\ |u|_a\equiv0\pmod r,\ |v|_a\equiv0\pmod s\bigr\}.
\]
Here \(|x|_a\) is the number of occurrences of \(a\) in \(x\), not its length. The distinguished occurrence of \(b\) can be any occurrence, and there must be at least one.

Write \(g=\gcd(r,s)\). There is an epsilon-free nondeterministic finite automaton with \(r+s\) states, a single initial state, a single final state, and one branching transition, whose language is \(L_{r,s}\). Its ordinary reachable subset determinization has exactly \(r2^{s/g}\) states, but its **minimal complete deterministic automaton has exactly**
\[
\boxed{\operatorname{sc}(L_{r,s})=r\bigl(2^{s/g}-1\bigr)+g.}
\]
All its right-language identifications are classified below. In particular, for coprime \(r,s\) the answer is \(r(2^s-1)+1\), whereas for \(r=s\) it drops to \(2r\). Thus a divisibility relation between the two independent modular guards produces an exact arithmetic transition between exponential and linear deterministic complexity.

## Assumptions and scope

Throughout, \(r,s\ge1\), the input alphabet is precisely \(\{a,b\}\), and the deterministic complexity counts all states of a complete DFA. Congruences always refer to counts of \(a\), not to absolute positions. The empty word and every word without a \(b\) are rejected. No claim is made that \(r+s\) is the minimum nondeterministic size. The theorem applies to *all* input lengths and all positive parameter pairs.

Construct the epsilon-free NFA with disjoint states \(C_i\) for \(i\in\mathbb Z/r\mathbb Z\), and \(D_j\) for \(j\in\mathbb Z/s\mathbb Z\). Its initial state is \(C_0\); its sole final state is \(D_0\). The letter \(a\) rotates both cycles forward by one. The letter \(b\) is a self-loop everywhere, except at \(C_0\) its successors are both \(C_0\) and \(D_0\). This is the only nondeterministic choice. Following the \(C\) run counts \(a\)-letters before the chosen \(b\), and following the \(D\) run counts them afterwards, so the NFA recognizes precisely \(L_{r,s}\).

## Proof

**1. Shape of reachable subsets.** At every prefix, the surviving \(C\)-states consist of one state \(C_i\), where \(i\) is the total \(a\)-count modulo \(r\). Denote the set of surviving \(D\)-indices by \(S\subseteq\mathbb Z/s\mathbb Z\); write the subset state as \((i,S)\). Every \(D\)-branch was created at a prefix with an \(a\)-count \(t\equiv0\pmod r\). If the total \(a\)-count is \(T\), its final index is \(T-t\pmod s\). Consequently every such index is congruent to \(i\) modulo \(g\). Set
\[
J_i=\{j\in\mathbb Z/s\mathbb Z:j\equiv i\pmod g\}.
\]
Every reachable state is of the form \((i,S)\) with \(S\subseteq J_i\), and \(|J_i|=s/g\). The transitions are exactly
\[
(i,S)\xrightarrow{a}(i+1,S+1),\qquad
(i,S)\xrightarrow{b}
\begin{cases}(i,S\cup\{0\}),&i=0,\\ (i,S),&i\ne0,\end{cases}
\]
with cyclic indices. A state accepts if and only if \(0\in S\).

**2. Every admissible subset is reachable.** Fix \(i\in\mathbb Z/r\mathbb Z\) and \(S\subseteq J_i\). Choose a sufficiently large integer \(T\ge0\) with \(T\equiv i\pmod r\). For each \(j\in S\), the simultaneous congruences
\[
t_j\equiv0\pmod r,\qquad t_j\equiv T-j\pmod s
\]
are solvable by the generalized Chinese remainder theorem, since \(j\equiv T\pmod g\). By increasing \(T\) in multiples of \(r\), choose distinct representatives \(t_j\) in \([0,T]\). Place one \(b\) at each corresponding position in a word with exactly \(T\) letters \(a\), and no other \(b\). The resulting reachable state is precisely \((i,S)\). This includes \(S=\varnothing\), realized by \(a^T\). Hence the reachable determinization has exactly
\[
\sum_{i=0}^{r-1}2^{|J_i|}=r2^{s/g}
\]
states.

**3. Complete Myhill--Nerode comparison.** If \((i,S)\) and \((k,U)\) have distinct second components, choose \(j\) in their symmetric difference. Appending \(a^t\), with \(t\equiv-j\pmod s\), makes exactly one shifted second component contain the final index \(0\). Such states are distinguishable regardless of their first components.

It remains to compare states with the same second component \(S\). If their first indices agree they are the same state. Suppose \(i\ne k\). If \(S\ne J_i\), choose \(j\in J_i\setminus S\). The generalized Chinese remainder theorem gives \(t\ge0\) such that
\[
t\equiv-i\pmod r,\qquad t\equiv-j\pmod s.
\]
After \(a^t\), neither second component contains \(0\), but the first state has first index \(0\) and the second has a nonzero first index. The suffix \(a^tb\) therefore distinguishes them. (For an empty \(S\), the same choice works regardless of whether \(i\equiv k\pmod g\).)

Finally suppose \(S=J_i\) is saturated. For a state with this second component, every future input preserves saturation of the current congruence class: an \(a\) rotates the full class and a \(b\) cannot add an index outside it. Thus acceptance from any such state depends only on the initial class \(i\pmod g\) and the future number of \(a\)'s. All \(r/g\) saturated states in each congruence class are equivalent. States belonging to different saturated classes have distinct second components and were already distinguished. These are the *only* quotient identifications.

There are \(r\bigl(2^{s/g}-1\bigr)\) unsaturated states, all distinct, and exactly \(g\) saturated equivalence classes. Adding gives the claimed minimal-state formula. The argument is an all-parameter Myhill--Nerode proof, not an inference from finite enumeration. \(\square\)

## Verification

Two separately organized Python programs accompany the result. The first constructs the original \(r+s\)-state NFA directly with bitsets, traverses every reachable subset, refines deterministic equivalence classes, and compares with the claimed counts for all \(1\le r,s\le7\). It also compares direct language recognition with the NFA on every binary word of length at most eight when \(r,s\le4\). The second builds the canonical two-component state space, constructs explicit reachable prefixes by congruence conditions, and constructs distinguishing suffixes for all non-equivalent state pairs for \(1\le r,s\le6\). Their saved exact outputs are included. These finite checks corroborate, but do not replace, the all-parameter proof above.

Run with Python 3 (standard library only): `python3 verify_subset.py` and `python3 verify_quotient.py`.

## Relationship to prior work

The 2026 preprint by Baburin and Cotterell motivates determining exact state complexity rather than using only generic subset-complexity upper bounds; its general hardness and complexity estimates do not give this two-modulus exact quotient. Their earlier 2024/2025 work explicitly analyzes Meyer--Fischer and Moore exponential witnesses, including an unconstrained-prefix modular suffix condition. The special case of a free prefix is therefore not claimed as a new exponential phenomenon. The present theorem concerns the joint \(r,s\)-parameter family, the \(\gcd(r,s)\) transition, and a complete classification of which reachable subsets merge. The separate multiple-concatenation bounds of Jirásek and Jirásková concern different deterministic concatenation witnesses and do not imply the present exact count. The permutation-language concatenation bounds of Hospodár and Mlynárčik apply to two permutation-language factors; the left factor here is not a permutation language, so that theorem does not directly subsume this formula (its abstract, not complete text, was accessible for the comparison). A mathematically equivalent, unindexed specialized treatment could still exist.

## Limitations

The NFA is a concrete witness with \(r+s\) states and one extra branch; the result does not assert that this is minimal among NFAs. It does not estimate typical determinization complexity or cover arbitrary NFAs with one nondeterministic transition. The two programs inspect finite parameter ranges; unrestricted \(r,s\) follow from the proof. The literature comparison is to the inspected primary results, not a claim of exhaustive global priority. Independent external validation has not been performed.

## References

1. I. Baburin and R. Cotterell, *Towards A Parametrized Complexity of Determinization*, arXiv:2611.10911v1, first public November 7, 2026. https://arxiv.org/abs/2611.10911
2. I. Baburin and R. Cotterell, *Blow-up in Non-Deterministic Automata*, arXiv:2407.09891v1 (later titled *A Close Analysis of the Subset Construction*), first public July 13, 2024. https://arxiv.org/abs/2407.09891
3. J. Jirásek and G. Jirásková, *State Complexity of Multiple Concatenation*, arXiv:2511.03814v1, November 5, 2025. https://arxiv.org/abs/2511.03814
4. M. Hospodár and P. Mlynárčik, *Operations on Permutation Automata*, Developments in Language Theory, 2020, DOI:10.1007/978-3-030-48516-0_10. https://doi.org/10.1007/978-3-030-48516-0_10
