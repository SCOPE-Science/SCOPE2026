# Independent mathematical audit

## correctness

PASS

OEIS A023199 supplies the exact a_i representations used by the package. The A073751 b-file confirms the relevant prime-occurrence positions: 83 first at 37 and next at 572 with 2621 at 425; 149 first at 52 and next at 1500 with 4567 at 673; 127 first at 47 and next at 1145 with 8011 at 1072; and the inspected 1687--1727 segment contains 13633 once at 1687 and ends with 13999 at 1727. The rational correction factors do not contain the witness primes. Since q_i occurs exactly once, sigma(q_i)=q_i+1 divides sigma(a_i), and q_i+1 is divisible by i in every case. Thus i|sigma(a_i); minimality of a_i then gives g_i=a_i. The verifier reproduces these exact finite checks.

## originality

PASS

The four equalities are best-of-knowledge new statements relative to the inspected layered/abundancy source and Resultary corpus. Their numerical input is, however, entirely tabulated in OEIS A023199/A073751 and the proof applies the already-known prime-witness mechanism to four next entries. No source found states the four equalities themselves.

## value

FAIL

The contribution is only four next numerical instances obtained by applying the same one-prime witness to externally tabulated colossally-abundant factorizations. It adds no structural lemma, new infinite family, meaningful cutoff, or nontrivial classification, and the exact work is essentially table lookup plus sigma(q)=q+1. Under the stated value bar against known-table recomputation and tiny routine extensions, these four cases do not constitute a sufficiently motivated independent mathematical result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
