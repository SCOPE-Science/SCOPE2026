# Exact complete-DFA complexity for palindromic reduced words of dihedral Coxeter products

## Finding
Let \(r\ge1\), let \(p_1,\ldots,p_r\in\{2,3,\ldots\}\cup\{\infty\}\), and form the Coxeter system with disjoint standard generating pairs \(\{s_i,t_i\}\) and group
\[
W=\prod_{i=1}^r I_2(p_i),
\]
where the order of \(s_it_i\) is \(p_i\), and generators in different pairs commute. Let \(\mathcal P(W)\) be the language of all **nonempty, literally palindromic, Coxeter-reduced** words over the union of these pairs, read left to right. Its **complete deterministic state complexity** is the number of states in a smallest total-transition DFA, including a rejecting sink.

Write \(F=\{i:p_i<\infty\}\) and \(J=\{i:p_i=\infty\}\), and for \(i\in F\) let
\[
M_i=2\left\lceil\frac{p_i}{2}\right\rceil-1
\]
be the largest odd integer no greater than \(p_i\). Then the exact complexity is
\[
\boxed{\operatorname{sc}(\mathcal P(W))
=2+4|J|+2\sum_{i\in F}(M_i-1)+\mathbf{1}_{F\ne\varnothing}.}
\]
In particular, for \(r\) infinite-dihedral factors it is \(4r+2\), and for a single finite dihedral factor it is \(2M_1+1\). At finite Coxeter exponent \(p_i\), the contribution increases by four when \(p_i\) changes from an even exponent to the following odd exponent, and does not change when an odd exponent is increased by one.

## Assumptions and scope
The alphabet consists of \(2r\) distinct generator symbols. A word is *palindromic* only when its actual symbol sequence equals its reverse; it is *reduced* when its length is the Coxeter length of the group element it represents. The empty word is **not** in \(\mathcal P(W)\). All finite exponents satisfy \(p_i\ge2\). This concerns the complete DFA over the entire alphabet, not a partial DFA or a machine whose input is promised reduced.

## Proof
**1. Exact language.** In each dihedral factor, reduced words are the alternating words of lengths at most \(p_i\), or of arbitrary lengths when \(p_i=\infty\). Coxeter length in the product is additive over the factor projections. If a palindromic word uses generators from a factor not containing its central letter, its projection to that factor is a nonempty *even palindrome*. Its middle two projected letters are equal, so that projection is not reduced. Thus every reduced palindrome uses exactly one factor. As an odd alternating word is a palindrome, the language is the disjoint union
\[
\mathcal P(W)=\bigcup_{i=1}^r
\{[s_it_i]_{2k+1},[t_is_i]_{2k+1}:0\le k,\ 2k+1\le p_i\},
\]
where the final bound is omitted for \(p_i=\infty\), and \([xy]_j\) denotes the length-\(j\) alternating word beginning in \(x\).

**2. Upper bound, by an explicit total DFA.** Use one initial rejecting state and one absorbing rejecting sink. For each infinite factor use four continuation states, one for each pair of initial generator and positive-length parity. An initial generator enters the corresponding odd accepting state; the opposite generator switches parity, and any other generator goes to the sink. For each finite factor \(i\), maintain the initial generator and length for each positive alternating prefix shorter than \(M_i\), giving \(2(M_i-1)\) states. Accept the odd-length states. A transition that makes the length exactly \(M_i\) enters one **shared terminal accepting state**, whose every outgoing transition goes to the sink. All other invalid transitions go to the sink. The shared terminal state is used if and only if \(F\ne\varnothing\). This is a complete DFA for the exact language above, with the stated number of states.

**3. Matching Myhill--Nerode lower bound.** Every state in the construction is reached by an explicit prefix. The sink has empty right language. The initial state's one-letter accepted continuations are all \(2r\) generators, whereas every noninitial rejecting state has at most one such continuation (possibly none); thus the initial state is distinct. The shared finite terminal state has right language \(\{\varepsilon\}\), distinguishing it from every other accepting state, each of which admits a nonempty accepted continuation.

For a finite factor, a nonterminal reachable prefix of length \(k\), \(1\le k<M_i\), has accepted continuations with a **largest** length \(M_i-k\); two prefixes of different lengths are therefore inequivalent. At a fixed even length, appending the next required (opposite) generator produces an accepted word from one orientation and an invalid word from the other. At a fixed odd length, appending the forced two-letter continuation (opposite, then original generator) does the same; this continuation exists since the prefix is strictly shorter than the maximal odd length. Each such state's right language contains a nonempty word solely in its factor alphabet, distinguishing it from all states attached to different factors. For an infinite factor, the four right languages are pairwise distinct: accepting versus rejecting separates parity, and a one-letter or two-letter continuation separates the two orientations within a fixed parity. Each has unbounded accepted continuation lengths, distinguishing them from all finite-factor states. Infinite-factor states are distinguished across factors by a nonempty accepted continuation in one factor's own alphabet. These are all the states in the construction, and none merge. The upper and lower counts coincide.

## Verification
Run `python3 checker.py` in a directory containing the included checker. The checker constructs a larger explicit prefix/parity DFA without using the proposed minimized quotient, minimizes it by separately implemented partition refinement, and compares to the formula across 2,913 parameter tuples of up to five factors with finite exponents 2--5 and infinite factors. It also compares 1,121,923 directly enumerated words with the palindrome-and-reduction predicate, and verifies single-factor boundary values 3, 6, and 7. Such finite checks test the implementation and boundary cases; the infinite-parameter theorem follows from the proof above.

## Relationship to prior work
Bapat's September 24, 2026 preprint proves the complete regularity criterion for palindromic reduced-word languages and its Lemma 5.8 proves the direct-product union property. Proposition 4.1 discusses an automaton for one infinite dihedral factor, but does not give a Myhill--Nerode minimality theorem or the all-exponent product-state formula proved here. The explicit four-state diagram in that proposition cannot be a correct complete recognizer for the stated odd-alternating language: its transitions accept the nonreduced word `stt`; the lower bound here proves six states are necessary. This observation concerns that displayed recognizer, not the main regularity theorem.

Biagioli, Hohlweg and Sasso (February 18, 2026), Example 3.3, give the finite/infinite dihedral reflection words and their reflection prefixes, not the complete-DFA quotient complexity. In particular, their reflection count does not imply the exact Myhill--Nerode index without comparing all suffix languages. The new result is the complete all-factor *minimal* state count, including the cross-factor sharing of terminal right contexts.

## Limitations
The formula covers direct products of rank-two dihedral Coxeter systems with the **standard** generators, not products with arbitrary irreducible higher-rank finite Coxeter factors. It counts complete DFA states, not nondeterministic state complexity, reflection elements, partial automata or distinct reduced expressions per group element. Historical priority beyond the inspected documents and indexed results is not independently certified.

## References
1. A. Bapat, *On the language of palindromic reduced words in a Coxeter group*, first public September 24, 2026, arXiv:2609.29022, full author's version https://asilatabapat.org/assets/papers/2026-palindromic.pdf, especially Proposition 4.1, Lemma 5.8.
2. R. Biagioli, C. Hohlweg, E. Sasso, *On generating functions and automata associated to reflections in Coxeter systems*, first public February 18, 2026, arXiv:2602.16361, especially Example 3.3. https://arxiv.org/abs/2602.16361.
3. J. E. Hopcroft, R. Motwani, J. D. Ullman, *Introduction to Automata Theory, Languages, and Computation*, for standard complete-DFA and Myhill--Nerode definitions.
