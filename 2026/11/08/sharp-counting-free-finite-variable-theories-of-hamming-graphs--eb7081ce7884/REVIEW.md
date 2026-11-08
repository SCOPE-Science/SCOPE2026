# Scientific review: finite-variable theories of Hamming graphs

## Correctness — PASS

For all positive dimensions and alphabet sizes at least two, the proof gives a permanent coordinatewise equality-pattern pebble strategy above the alphabet cutoff, exact three-variable formulas for bounded graph distance, and clique formulas for the alphabet cutoff. Separate one- and two-variable arguments handle low widths. Boundaries at alphabet size exactly \(k\), dimension one, and two-variable noncomplete graphs were independently checked in the proof reconstruction. The accompanying orbit game calculation tests 14 finite instances with zero discrepancies but is not a proof for all parameters.

## Originality — PASS, qualified

The closest accessible primary texts are Klavžar–Peterin (2005; DOI:10.1002/jgt.20084), Pikhurko–Verbitsky (2010; arXiv:1003.4865), Kotek–Makowsky (2013; arXiv:1308.3654), and Adler–Benediktsson–Macpherson (2020; arXiv:2007.16042). Their inspected statements concern embeddings, general logical complexity, graph-parameter composition, or VC invariants and do not themselves give the proposed exact all-dimensional criterion. The dimension-two special case is covered by an earlier rectangular rook-graph result and is *not* claimed as new. A more general unidentified graph-product composition result could dominate the claim, so historical priority remains provisional.

## Mathematical value — PASS

The complete family-level classification determines exactly which of the two independent structural parameters remain visible at every variable width. Three reusable variables recover arbitrarily large dimension, whereas every bounded variable count loses all alphabet distinctions beyond its cutoff. The derived unique minimum representatives and dimension-independent sharp relative defining width are natural structural information about the entire Hamming family, not a small isolated computation.

## Limitations

Only pure-adjacency, counting-free first-order logic over finite uniform-alphabet Hamming graphs is treated. Defining width and smallest representatives are relative to this family. Nonuniform Cartesian products, enriched signatures, counting quantifiers, and optimal formula depth are not classified. Proof and code are separate forms of evidence; the finite program cannot establish unbounded logical equivalence. Originality priority is not exhaustive.

Self-review: passed. Independent audit: not yet performed.
