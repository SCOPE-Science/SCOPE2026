# Scientific review

## Correctness — PASS

The theorem states the domain \(n\ge4\), both transition tables and the coordinatewise product. Every common reset word must reset \(C_n\). Counting effective collapses along trajectories yields \(|w|\ge(n-1)^2\), and equality forces the unique shortest word \(W_n\). The image-interval induction proves \(W_n\) resets \(C_n\). Its three-state action is controlled exactly by \(n\bmod3\). For all nonzero residues, the explicit length-\((n-1)^2+1\) word \(V_n\) is shown to reset each factor. Thus lower and upper bounds meet for each residue. Exhaustive subset-pair breadth-first search through \(n=16\) and a separate state-by-state witness replay through \(n=70\) corroborate, rather than replace, the proof.

## Originality — PASS subject to priority uncertainty

The closest all-pair census of simultaneous Černý resets covers only \(2\le m<n\le11\): it already includes the small examples for \(m=3\) and proves the zero-overhead condition when \(m\mid n\). These known cases are expressly not claimed as new. Fernau and Rystsov give a general product bound and study the single Černý factor, but do not furnish the all-size fixed-three-state modular formula. The all-length uniqueness and one-letter-slack studies of the individual Černý reset language constrain possible witnesses without deciding simultaneous resetting of \(C_3\). The remaining priority risk is an equivalent all-length proof outside the located indexed or accessible material.

## Value — PASS

A fixed three-state factor is the first nontrivial case not automatically synchronized by the first collapse letter. The theorem proves that its added synchronization latency is always **at most one**, not the general upper allowance of four, and pinpoints exactly when it vanishes. This solves a natural infinite-parameter subproblem motivated by the product reset-threshold question; it is not a single computed parameter, routine rewording or an unsupported extrapolation of the finite census.

## Limits

The proof does not enumerate all shortest common words, cover arbitrary pairs of Černý automata, or resolve the general product synchronization problem. The lower bound and uniqueness of the shortest single-factor Černý word, the zero-overhead divisible cases and every numerical example with \(n\le11\) were established earlier.

Self-review: passed. Independent audit: not yet performed.
