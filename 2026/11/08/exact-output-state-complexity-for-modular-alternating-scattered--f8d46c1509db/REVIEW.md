# Scientific review: modular alternating scattered-triple output complexity

## Correctness — PASS

The accepted theorem is that the smallest residue-output Moore machine for the scattered \(010\)-count has \(m^3/\gcd(m,2)\) states for each integer \(m\ge2\). Its counter coordinates track the modular numbers of \(0\), \(01\), and \(010\) subsequences. A direct integer identity proves the only reachable-state restriction, namely \(c\equiv(a-1)b\pmod{\gcd(m,2)}\). Two explicit commutator maps provide a constructive inverse to that restriction, including at even composite moduli. The outputs after \(\varepsilon\), \(0\) and \(10\) separate any two distinct triples, proving minimality. The checker supplies independent finite comparisons against direct index counting and complete state-space searches. There is no appeal to finite experimentation for the infinite quantifier.

## Originality — PASS, with historical-priority risk

The closest currently examined publications involve binary Parikh-matrix universality and probability (Fazekas–Huang–Mercaş, 2026), general Parikh mapping algebra (Černý, 2010), trie automata counting scattered subwords (Alazemi–Černý, 2011), and regularity of comparisons between contiguous subword counts (Colbourn–Dougherty–Lidbetter–Shallit, 2018). Their inspected results do not state or imply an exact minimum output-state count with the even-modulus parity factor. The strongest overlap risk is the inaccessible full text of the 2011 trie-automaton paper, which could contain an implicit construction; its available abstract does not settle reachability and minimization. The distinction from a Boolean single-residue recognizer is explicitly preserved.

## Value — PASS

The alternating length-three pattern is the smallest binary scattered pattern with a return to its initial letter. Its modular counter machine has a natural three-coordinate upper bound, but the exact reachable orbit is unexpectedly smaller by two for even moduli. The theorem resolves a complete all-modulus, natural automaton-complexity invariant, supplies constructive witnesses for all attainable coordinates, and gives a constant-size set of suffixes separating states. It establishes a structural parity boundary rather than a numerical improvement in an arbitrary parameter slice.

## Limitations and next evidence

The result is about minimal deterministic **output** machines for the two alternating binary length-three patterns; it does not determine individual target-residue Boolean DFA sizes. A complete historical-priority examination of the 2011 trie-automaton article and independent mathematical validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
