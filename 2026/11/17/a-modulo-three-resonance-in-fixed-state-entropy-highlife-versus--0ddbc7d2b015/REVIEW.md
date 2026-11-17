# Scientific comparison and review

## Correctness — PASS

The original local rule is encoded by the exact neighbor count \(N_r(a,b,c)=|a|+|b|+|c|-b_r\), valid for all \(n\ge3\). A configuration is fixed if and only if its periodic sequence of columns describes a length-\(n\) closed walk in the specified sixty-four-vertex graph. The supplied integer certificate checks all 512 local triples, both cyclic-component decompositions, the complete size-thirty and size-twenty-seven characteristic polynomials, and strict rational Collatz-Wielandt bounds. The common \(1,1,2\) family is also counted directly, and a separate exhaustive Moore-update program tests the predicted results through circumference seven. The all-size argument uses exact finite graph identities and primitivity, not the small-size tests. Remaining correctness risk is a possible implementation error shared by finite computations, mitigated by the explicitly stated graph definition and independent direct checker.

## Originality — PASS, with residual priority risk

The exact claim is a comparison of labelled fixed-state sequences for B36/S23 and B3/S23 on every \(\mathbb Z_3\times\mathbb Z_n\) Moore torus, together with two distinct asymptotic regimes depending on divisibility by three. Eppstein's 2009 full preprint discusses HighLife pattern growth, not this exact census. Bell's original HighLife discussion and McIntosh's Life still-life chapter are the closest historical sources, but their full contents were not obtainable; this is explicitly a priority risk, not evidence of their absence. An accessible prior three-row Conway Life fixed-state result already provides the complete Life-side characteristic polynomial and the common resonance family; neither this nor related results for other rules implies the newly computed HighLife spectrum or the cross-rule contrast. No exact matching sequence or table was identified by the searches performed. The Conway Life-only formula, ordinary transfer technique and known inclusion of HighLife still lifes in Life still lifes are prior facts, not independent claims to priority.

## Mathematical value — PASS

HighLife differs from Life by a single birth condition; that perturbation deleting just one cyclic transition has an exponential effect on off-resonance fixed-state counts while leaving a common, asymptotically overwhelming family on resonant widths. The exact invariant and the split asymptotic are natural diagnostics for a canonical pair of well-known cellular automata. The theorem is not merely a computation at arbitrary small sizes: it covers all circumferences and determines complete recurrent transfer spectra with a structural explanation of the arithmetic effect. No claim is made for wider strips or the infinite-plane stationary-state measure.

## Literature and verification limitations

Primary full text consulted: D. Eppstein, *Growth and Decay in Life-Like Cellular Automata*, arXiv:0911.2890, sections on Life-like rules and HighLife; and Eppstein's author-authored HighLife replicator account. Bell's 1994 author-hosted compressed archive was located but not read; McIntosh's pertinent chapter was only available as bibliography and abstract. Two standalone programs and their actual stdout records accompany the proof. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
