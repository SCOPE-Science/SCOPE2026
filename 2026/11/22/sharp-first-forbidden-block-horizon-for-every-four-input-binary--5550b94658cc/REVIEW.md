# Scientific review

## Correctness: PASS

The exact claim is an all-rule finite census of \(L(r)\), not an approximation. The eight-vertex binary de Bruijn graph recognizes all output blocks. Subset determinization establishes the necessary-and-sufficient empty-state test for **arbitrary** word lengths, and complete BFS on at most 256 states per rule makes the 65,536-rule enumeration exhaustive. Independent C++ and Python implementations reproduced all 18 finite histogram bins and the infinity bin; the Python checker also verified the four extremal rules, the eight absent 18-symbol words for each, their length-17 completeness, witness words, and direct short-block outputs. The proof of arbitrary-length correctness rests on the automaton invariant and compactness rather than finite experiments alone.

## Originality: PASS within checked evidence

The 2012 Fukś–Skelton table establishes the **previously known** 582 surjections among the 65,536 rules; the new claim is the complete first-forbidden-length census and sharp 18-symbol bound. Gravner–Kulhanek (2026) gives labeled de Bruijn and random-rule methods, not this finite exact distribution. The closest published 2026 comparisons cover either 256 elementary three-input rules or their second-update image loss, different statements and scopes. Searches for the four maximizers and semantic variants revealed no matching finite tabulation. Historical priority remains provisional because some historical datasets or inaccessible full texts could contain overlapping evidence; it is not claimed independently certified.

## Mathematical value: PASS

Four consecutive inputs are the first binary neighborhood size admitting nonpermutive surjective rules. A sharp uniform forbidden-word horizon provides a finite **complete** diagnostic for every nonsurjective rule of this natural size, while the full length distribution quantifies how early surjectivity fails and reveals the nontrivial length-15 gap. The 18-symbol bound is attained only by four exact rules, so it is not a weak arbitrary computational cutoff.

## Scope and risks

The statement concerns binary full-shift automata with four consecutive input sites, exactly **one** synchronous update and ordinary bi-infinite spatial images. It does not classify higher iterates, cyclic-ring images or longer neighborhoods. Standard algorithms are not claimed new. The C++ and Python scripts and their outputs are same-study reproducibility evidence, not independent external certification. Full-text access to some related published short-summary research records was unavailable; their stated domains were compared and reported distinctly. The 2012 surjectivity total is acknowledged as established prior work.

Self-review: passed. Independent audit: not yet performed.
