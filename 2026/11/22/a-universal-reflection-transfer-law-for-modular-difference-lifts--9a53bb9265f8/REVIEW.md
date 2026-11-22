# Self-review

## Correctness — PASS

The bi-infinite lifting recurrence is a bijection between each length-\(n>h\) factor and an \(h\)-letter prefix plus an allowed length-\(n-h\) base factor. Under ordinary reversal its difference word becomes minus the reversed base word. For \(q\ge3\), the only allowed binary word surviving this sign transformation is the all-zero word. Counting the reversal involution on \(\mathbb Z/h\mathbb Z\) produces precisely \(q^{(h+f_h(n))/2}\) fixed words among \(q^h\) reversible factors. Full-language enumeration handles short factors; the noble-means specialization uses its familiar Sturmian complexity and run lengths. The standalone finite checker passed 48 parameter triples through length eight, including general periodic bases. The infinite claim is supported by the written proof, not extrapolated from tests.

## Originality — PASS within checked evidence

The September 2026 work of Kang and Jäger proves structural properties and strict ergodicity of permutative lifts, but the inspected text does not state this reflection transfer or the all-zero-word obstruction. The 2025 reflection-complexity paper gives the universal counting identity and the binary Rote case, not the specific modulus-\(q\ge3\) transfer across arbitrary memory and base subshifts. Published research records on reversal cutoffs for other sequences and on linear recurrence of lifts do not imply this all-base formula. Relevant older finite-group-extension and reflection-complexity literature may be under-indexed; no claim of exhaustive priority certification is made.

## Mathematical value — PASS

The formula determines a natural dynamical-language invariant for every binary base subshift and simultaneously reveals that only the zero-run availability, not the rest of the language, governs the complete reversal deficit. The concrete family consists of already-established strictly ergodic minimal extensions with sharply bounded reversal-pair windows and explicit length profiles. This is a structural transfer law, rather than a single arbitrary finite count or a relabeling of a previous theorem.

## Residual limitations

The law assumes ordinary reversal and modulus at least three. It does not treat generalized reversal/inversion, or calculate spectral invariants of the lifted dynamics. The first source establishes the strict ergodicity used as context; that property is not claimed as newly proved here. Historical equivalences remain possible.

Self-review: passed. Independent audit: not yet performed.
