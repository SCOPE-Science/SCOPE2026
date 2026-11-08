# Scientific review: census of optimal length-four DNA deletion codes

## Correctness — PASS

The domain is precisely four-symbol, length-four, Watson--Crick-reverse-complement-closed, self-reverse-complement-free codes whose deletion shadows are disjoint for distinct strands. The direct orbit decomposition gives 120 eligible pairs. A clique corresponds bijectively to a code. The finite C++ search enumerates all size-12 cliques (zero) and size-11 cliques (44), using an explicitly justified, safe greedy-coloring upper bound. An independently written Python Bron--Kerbosch search regenerates 44 maxima and confirms no larger maximal clique. Both verify the full 44-row certificate, all nine symmetry classes, and the exact two compulsory strand pairs. Computation is a complete finite proof here, not extrapolation from bounded examples.

## Originality — PASS, qualified

The published 2005 work of D'yachkov et al. already asserts the optimal code size 22 and displays one example. It does not give a complete labeled-codebook census, a nine-class symmetry partition, or the two compulsory reverse-complement pairs in the inspected sections and searchable full text. The 2003 Exordium sets up the model; King 2003 treats a different Hamming/GC formulation. Searches of published research records for length-four DNA deletion codes, 44 maxima, nine symmetry types, and the mandatory homopolymer pairs returned related but non-covering ternary/binary deletion-coding classifications. This supports, but cannot guarantee, historical priority. A 2006 one-page remark was identifiable but inaccessible in full; it remains a specific risk.

## Value — PASS

The original model asks for selective DNA hybridization through constrained deletion similarity, and its paper-sized literature already identifies the 22-strand optimum as noteworthy. A complete classification of all designs attaining this sharp optimum is a natural finite structural question. The result identifies the entire 44-element design space, nine genuine symmetry types rather than one known example, and unavoidable homopolymer pairs. Those exact properties are useful to anyone comparing feasible maximum codes against additional design restrictions, although no laboratory or thermodynamic performance is inferred.

## Scope and limitations

The old 22-size optimum is not claimed as new. The new classification is limited to length four and one deletion; it does not establish higher-length optima, error robustness beyond this channel, or biochemical practicality. Independent scientific and historical-priority audits are outstanding. The full 2006 remark was unavailable, so it cannot be declared not covering.

Self-review: passed. Independent audit: not yet performed.
