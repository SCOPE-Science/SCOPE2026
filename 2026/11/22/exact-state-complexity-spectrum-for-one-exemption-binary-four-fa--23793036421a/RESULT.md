# Exact state-complexity spectrum for one-exemption binary four-factor monitors

## Finding

For a binary pattern \(p\in\{0,1\}^{4}\), let \(L_p\) consist of every finite binary word containing **all fifteen** length-four contiguous factors other than \(p\). The factor \(p\) is permitted but not required. Let \(\kappa(L_p)\) be the number of states in the minimal **complete** deterministic finite automaton (DFA) for \(L_p\), including any required sink.

The exact classification is below. The second column lists both members of a complement-pair; \(\overline p\) denotes bitwise complementation.

| Pattern \(p\) | Complement \(\overline p\) | \(\kappa(L_p)=\kappa(L_{\overline p})\) | Sharp distinguishing suffix length |
|---|---|---:|---:|
| `0000` | `1111` | 8435 | 17 |
| `0001` | `1110` | 11121 | 18 |
| `0010` | `1101` | 9670 | 18 |
| `0011` | `1100` | 10152 | 18 |
| `0100` | `1011` | 9956 | 18 |
| `0101` | `1010` | 9537 | 18 |
| `0110` | `1001` | 8524 | 18 |
| `0111` | `1000` | 11746 | 18 |

Thus the exact spectrum consists of eight values; the minimum \(8435\) is attained exactly when \(p\) is constant, and the maximum \(11746\) exactly when \(p\in\{0111,1000\}\). Reversal need not preserve complete-DFA size: \(\kappa(L_{0001})=11121\), whereas \(\kappa(L_{1000})=11746\), a difference of \(625\), even though reversing every input word interchanges the two languages.

## Assumptions and scope

The alphabet is exactly \(\Sigma=\{0,1\}\); factors are *contiguous*, not scattered subsequences. All sixteen patterns \(p\) of length exactly four are covered; no limit is imposed on the length of recognized input words. A complete DFA has one transition for each symbol at every state. These results concern the language in which one **specified** pattern is optional; they do not concern the different language in which any unspecified one of the sixteen may be absent.

## Proof

**A finite automaton recognizing the exact language.** Number the sixteen binary four-factors from \(0\) to \(15\) by their binary numerical values. A state is \((M,s)\), where \(M\subseteq\{0,\ldots,15\}\) records all factors seen, and \(s\) is the current suffix of length \(\min(3,|w|)\). The initial state is \((\varnothing,\varepsilon)\). On reading a bit \(b\), append \(b\) to \(s\), add the resulting four-factor to \(M\) if the concatenation has length four, and retain only its last three bits as the new suffix. For a fixed excluded index \(e\), declare a state accepting if and only if \(\{0,\ldots,15\}\setminus\{e\}\subseteq M\). This invariant is immediate by induction on the input length, so the resulting DFA recognizes precisely \(L_p\).

**Exhaustive reachable state generation.** Breadth-first enumeration from the initial state applies each of the two explicit transitions exactly once to every newly generated state and stops when no new state remains. Both supplied implementations use a lossless encoding of \((M,s)\), and both enumerate exactly \(19{,}205\) states, independently of the excluded pattern. This procedure is exhaustive by induction on the length of a shortest word reaching a state: its predecessor has shorter length and must have been dequeued. The computation is finite and does not truncate input word length.

**Exact Myhill–Nerode quotients.** For a fixed \(p\), initially partition the reachable states by accepting status; call this partition \(\mathcal P_0\). Refine recursively: states are in the same class of \(\mathcal P_{d+1}\) exactly when they are in the same class of \(\mathcal P_d\) and their respective successors on both input letters are in the same classes of \(\mathcal P_d\). Inductively, two states share a class of \(\mathcal P_d\) if and only if they agree on acceptance for every suffix of length at most \(d\). Once refinement stabilizes, induction on the length of arbitrary suffixes shows no longer word can distinguish states in the same class. Distinct classes have witnessing suffixes by the previous induction. Therefore the stable partition is *exactly* the Myhill–Nerode partition; its class count is both a constructive DFA upper bound and a rigorous lower bound for any DFA recognizing \(L_p\).

The supplied Moore-refinement program calculates the stable quotient sizes for all sixteen excluded patterns and the first depth of stabilization. The independent Hopcroft-style partition-refinement implementation obtains the same sizes from reverse-transition predecessor lists. Both implementations additionally check that each final quotient is acceptance-uniform and transition-stable. Their exact results are the eight complement-paired rows in the table, and maximum required distinguishing suffix lengths are \(17\) for constant \(p\), \(18\) otherwise. The computation is a complete finite certificate for all input lengths, not extrapolation from a word sample.

**Symmetry and extrema.** Bitwise complement is a relabeling of the input alphabet and maps \(L_p\) bijectively to \(L_{\overline p}\), preserving minimal DFA size. The exhaustive sixteen-pattern classification gives both extremizers and shows the strict reversal separation \(11746-11121=625\).

## Verification

The included `verify_moore.py` builds the reachable automaton with string-valued suffixes, carries out recursive right-language refinement, and checks the class counts, distinguishing depths, transition-congruence conditions, direct input simulation for all words up to length ten, and an accepted length-eighteen witness for every omitted pattern. Run:

```text
python3 verify_moore.py
```

The separate `verify_hopcroft.cpp` encodes suffixes numerically, constructs all reverse transitions, and uses splitters in a Hopcroft-style partition algorithm. Its assertions check the sixteen expected quotient sizes, the \(19{,}205\)-state reachable graph, accepting-state uniformity and transition congruence. Run:

```text
g++ -O2 -std=c++17 verify_hopcroft.cpp -o verifier
./verifier
```

Both implementations were executed from these exact supplied source files. Their final messages were, respectively, `Moore refinement: ALL 16 EXACT COUNTS PASS` and `Hopcroft refinement: ALL 16 EXACT COUNTS PASS`. Assertions must remain enabled when rerunning (do not compile with `-DNDEBUG`). Each program computes its own graph and quotient rather than loading stored tables as proof.

## Relationship to prior work

Charalampopoulos, Mohamed, Pissis, Verbeek, and Zuba (first arXiv version dated May 6, 2026) study shortest absent substrings and give faster algorithms for finding them. Their inspected definitions and principal algorithms motivate the factor-coverage question but do not provide this minimal-state classification. The published OEIS sequence A375919, contributed by Jeffrey Shallit in 2024, already records \(13{,}212\) minimal complete-DFA states for the **different** language requiring all sixteen length-four factors; that result is credited as background, not claimed here. Published four-factor covering and three-factor spectrum enumerations address cyclic covers or length-wise counting rather than the prescribed-single-factor-exemption DFA quotient. Neither full-factor complexity, factor-presence counting, nor generic DFA-minimization algorithms directly yield the sixteen quotient values without the exhaustive right-language comparison given here.

## Limitations

This is a complete, exact finite classification only for binary factors of length four. It asserts no general formula for alphabet size, arbitrary factor length, or multiple exempt patterns. The finite certificate is replayable, but no formal proof assistant or independently commissioned audit has been used. A specialized equivalent classification not indexed in the inspected literature remains possible. Recomputing or inspecting the two verifiers is required to check the numerical certificate.

## References

1. P. Charalampopoulos, M. Mohamed, S. P. Pissis, H. Verbeek, W. Zuba, *Faster Algorithms for Shortest Unique or Absent Substrings*, arXiv:2605.04826v1 (public May 6, 2026), https://arxiv.org/abs/2605.04826.
2. J. Shallit, OEIS A375919, *Number of states in minimal deterministic finite automaton recognizing the language of binary strings that contain, as contiguous blocks, all binary strings of length n* (September 2, 2024), https://oeis.org/A375919.
3. *The sharp full-support threshold for binary three-factor spectra* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-the-sharp-full-support-threshold-for-binary-three-factor-spectra--e450d182bc9b.
4. *Exact shortest cyclic binary covers for all four-bit forbidden factors through order 15* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-shortest-cyclic-binary-covers-for-all-four-bit-forbidden-f--4c2a5e159cc3.
