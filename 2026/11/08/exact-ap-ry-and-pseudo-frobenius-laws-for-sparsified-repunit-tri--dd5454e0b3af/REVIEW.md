# Scientific review: sparsified repunit triples

## Correctness — PASS
The equalities \(R_{n+2}=a+u\) and \(R_{n+6}=a+mu\) are exact. With denominations \(1,m\), quotient–remainder minimization proves \(c(t)\), and the strict wrap inequality \(W(t+ha)>W(t)\) gives the entire Apéry set. The generator-order comparison leaves exactly the terminal positions \(a-1\) and, for \(n\geq5\), \(km-1\) as pseudo-Frobenius positions. A residue calculation and endpoint comparison yield the Frobenius formula; Selmer's Apéry sum yields the genus; the two maximal Apéry elements characterize nonsymmetry. These are all-integer arguments valid for every stated base/index. The finite Dijkstra checker compares independently computed Apéry values, Frobenius, genus, pseudo-Frobenius set, and symmetry on 18 separate instances. The proof, not the checker, handles infinite quantifiers.

## Originality — PASS within investigated sources
Liu, Xin, Ye and Yin (arXiv:2306.03459, first public 2023-06-06) supply a general coin-minimization framework and explicit conclusions for complete generator sequences; they do not state the present sparse triple's Apéry, maximal-element, type or closed invariant laws. Branco, Colaço and Ojeda (arXiv:2112.01106, 2021-12-02) solve the *fully generated* generalized repunit family, which contains missing intermediate generators and therefore is not equivalent. Moscariello (arXiv:1608.06137) offers generic finite minimization, not the present index-classified explicit formulas. Targeted published mathematical index searches for the precise sparse offsets, aliases, Frobenius and pseudo-Frobenius formulas returned no covering claim; indexed numerical-semigroup findings inspected concern unrelated generating sets. The broad general Apéry framework is acknowledged, not rebranded as novel.

## Mathematical value — PASS
Removing intermediate recurrence generators fundamentally changes the Apéry set and changes the embedding dimension and type relative to fully generated repunit semigroups. The result completely classifies the Apéry set, Frobenius number, genus, pseudo-Frobenius set and symmetry for the natural sparse-offset family at every integer base and admissible index. The two-boundary Apéry structure and dependence on index modulo six are the motivating structural contributions, rather than a numerical parameter slice.

## Closest literature, scientific limitations and residual risks
The closest source is the broad coin-model Lemma 2.4 of arXiv:2306.03459. The present proof explicitly evaluates its optimization in a skipped-offset semigroup and derives further invariants. A differently parameterized or unindexed specialized formula may exist. The computation covers finite cases and does not independently validate the infinite theorem. Even indices have common factors and are excluded.

Self-review: passed. Independent audit: not yet performed.
