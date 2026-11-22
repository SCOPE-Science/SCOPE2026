# Sharp co-lex width of the modular Fibonacci-word automata

## Finding

For each integer \(m\ge2\), define
\[
L_m=\{w\in\{0,1\}^{*}: 11\text{ is not a factor of }w,\ |w|\equiv0\pmod m\}.
\]
Fix the alphabet order \(0<1\). The unique minimal complete deterministic automaton for \(L_m\) has exactly \(2m+1\) states and co-lex width **exactly \(m+1\)**. Its trim partial version, obtained by deleting the rejecting sink, has \(2m\) states and co-lex width **exactly \(m\)**. In particular, completing this natural automaton incurs precisely one additional unit of co-lex width.

## Assumptions and scope

Co-lex width refers to the minimum antichain width of any partial order on the states satisfying the two standard co-lex axioms: (i) if \(u<v\), every incoming label of \(u\) is no greater than every incoming label of \(v\); (ii) strict order of distinct target states propagates backward along transitions with equal labels. The special start-of-word symbol \(\#\) precedes both binary letters. This is **automaton width**, not a claim that these automata minimize width over all possible automata recognizing \(L_m\). The partial automaton is accessible and coaccessible and permits undefined transitions. The complete automaton includes an absorbing rejecting sink. Width is computed using the stated alphabet order.

## Proof

For residues \(r\in\mathbb Z/m\mathbb Z\), let \(Z_r\) and \(O_r\) denote states remembering word-length residue \(r\) with most recent letter respectively \(0\) or \(1\). The start is \(Z_0\) (the empty word is permitted), and all and only \(Z_0,O_0\) are accepting. Define
\[
\delta(Z_r,0)=Z_{r+1},\quad \delta(Z_r,1)=O_{r+1},\quad \delta(O_r,0)=Z_{r+1},\quad \delta(O_r,1)=\bot,
\]
with residues modulo \(m\), and \(\delta(\bot,0)=\delta(\bot,1)=\bot\). This complete DFA recognizes precisely \(L_m\).

Each \(Z_r\) is reached by a sufficiently long all-zero word with length residue \(r\); each \(O_r\) by a sufficiently long word \(0^{\ell-1}1\) of length residue \(r\); \(\bot\) is reached by `11`. Distinct \(Z\)-residues are separated by a suitable all-zero suffix that makes exactly one final length divisible by \(m\). The same argument, using a positive-length all-zero suffix if necessary, separates \(O\)-residues. For any \(Z_r\) and \(O_s\), a suffix \(10^t\), with \(t\ge0\) chosen to make the length from \(Z_r\) divisible by \(m\), is accepted from \(Z_r\) and rejected from \(O_s\). Any nonsink state has an accepting all-zero continuation; the sink has none. Thus all \(2m+1\) states are pairwise right-language distinguishable. The trim partial DFA has the \(2m\) distinct nonempty residuals, so is also state-minimal in that category.

Every \(Z_r\) has incoming label \(0\) and every \(O_r\) has incoming label \(1\); \(Z_0\) additionally receives the start symbol \(\#\). Therefore the partial order with \(Z_r<O_s\) for every \(r,s\), and no other strict comparisons, satisfies both co-lex axioms: ordered targets have disjoint incoming binary labels, so backward propagation has no equal-label instances. Its width is \(m\) on the trim partial DFA.

This upper bound is sharp. Suppose some \(Z_r<Z_s\) with distinct residues. Each has a predecessor by a `0`-transition from \(Z_{r-1}\), respectively \(Z_{s-1}\). Repeated use of the backward-propagation axiom yields \(Z_{r-k}<Z_{s-k}\) for every \(k\ge0\), with residues modulo \(m\). These inequalities include a directed cycle (because the nonzero difference \(s-r\) has finite order), contradicting strict partial order. Thus the \(m\) states \(Z_r\) form an unavoidable antichain. The trim partial width equals \(m\).

For the complete DFA, \(\bot\) has incoming letters \(0\) and \(1\). The incoming-label axiom immediately forbids \(\bot<Z_r\). If \(Z_r<\bot\), use the `0`-predecessors \(O_{r-1}\to Z_r\) and \(\bot\to\bot\). The backward-propagation axiom would require \(O_{r-1}<\bot\), contrary to the incoming-label axiom, because \(O_{r-1}\) has incoming label \(1\), whereas \(\bot\) also has incoming label \(0\). Consequently \(\bot\) is incomparable with every \(Z_r\), giving an unavoidable antichain of size \(m+1\). Finally, the same displayed partial order \(Z_r<O_s\) with \(\bot\) incomparable to all other states is co-lex on the complete DFA and has width exactly \(m+1\). This establishes both sharp bounds.

## Verification

The included standalone `check_colex.py` implements the complete transition function and proposed co-lex relation, checks both defining axioms for all ordered pairs, refines the DFA state partition to minimality, and compares acceptance against direct factor/length testing on every binary word of lengths \(0\) through \(15\). It passed for each modulus \(2\le m\le12\), totaling 720,885 direct recognition checks. Finite verification corroborates, but does not replace, the all-modulus argument above. The analytic antichain proofs are essential for optimality.

## Relationship to prior work

Cotumaccio, D'Agostino, Policriti, and Prezza developed co-lex orders, their two axioms, and their automata width and indexing interpretations; the present result computes that invariant on a modular length-filtered run-limited family. The published exact prefix-sorting cost for avoiding a zero-run followed by one concerns a different forbidden-factor family without a modular length requirement, and does not imply this cycle-enforced antichain or its one-unit sink penalty. The standard product-state construction is not claimed to be new; the contribution is the exact co-lex width lower bound and its comparison under completion.

## Limitations

No claim is made about the least deterministic co-lex **language** width among arbitrary nonminimal DFAs, nor about nondeterministic co-lex width, information-theoretic encoding optimality, or error correction. Co-lex width depends on the alphabet order. Indexed records and inspected literature did not show an identical family, but unindexed, inaccessible or more general prior theorems could supersede this comparison. Independent audit has not been conducted.

## References

1. Nicola Cotumaccio, Giovanna D'Agostino, Alberto Policriti, Nicola Prezza, *Co-lexicographically Ordering Automata and Regular Languages — Part I*, arXiv:2208.04931v1 (first public 2022-08-09); J. ACM 70 (2023), article 27. https://arxiv.org/html/2208.04931v3
2. Published indexed work: *Exact prefix-sorting state cost for avoiding a binary zero-run factor*, record `2026/10/25/SCOPE-exact-prefix-sorting-state-cost-for-avoiding-a-binary-zero-run-f--294ac7d4ffb0` (different forbidden-factor family; full text not accessible for material review here).
