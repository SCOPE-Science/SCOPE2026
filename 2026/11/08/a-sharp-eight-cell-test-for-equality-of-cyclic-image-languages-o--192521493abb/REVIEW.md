# Scientific review

## Correctness — PASS

The local rule is normalized to Wolfram bit index \(4a+2b+c\). Closed labeled paths in the four-vertex binary de Bruijn graph represent exactly the outputs of cyclic inputs, including rings of sizes one and two. Boolean relation products recognize those paths. The self-contained verifier checks the independent direct-forward construction for all 256 rules and each length through eight, and fully explores all 156 finite synchronized automaton products needed to prove within-class equality for every positive length. The explicit Rule 57/Rule 99 witness confirms sharpness. Files `verify.py` and `classes.json` are complete; no exhaustive infinite search is claimed.

## Originality — PASS, qualified

The closest classifications in Wolfram (1983), Martínez (2013), and Schüle–Stoop (2011/2012) concern dynamical behavior or symmetry equivalence, not equality of complete indexed cyclic one-step image languages. Salo (arXiv:1804.03913, §6.3) calculates image-subshift forbidden words for selected rules, but does not present the 100-class all-rule classification or universal sharp length-eight discriminator. Castillo-Ramírez and Gadouleau (arXiv:1510.00197) classify an unrelated invariant, ranks of cyclic cellular-automaton semigroups. The online Elementary CA Zoo finite-length orphan-count census identifies equivalent rules under output relabeling, and its numerical tables do not determine exact language equality at arbitrary lengths. Query matches in the research index concerned different quantities. Unindexed historical tabulations remain an uncertainty.

## Value — PASS

The result gives a natural complete classification of a global reachability invariant for all 256 elementary rules, rather than a selected-rule numerical sequence. The sharp uniform cutoff supplies an efficient finite observational test for exact equality at every cyclic ring length. It distinguishes actual reachable output configurations from equality of image sizes, eventual dynamics, and symmetry up to relabeling. The bound is sharp and all equality classes are explicitly available for reuse.

## Limits

Only one update, indexed cyclic binary rings, and radius-one elementary rules are included. Neither uniqueness among all historical literature nor independent certification is claimed. Comparison with prior literature is qualified by possible unindexed equivalence tables.

Self-review: passed. Independent audit: not yet performed.
