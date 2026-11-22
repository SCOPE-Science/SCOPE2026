# Scientific review

## Correctness — PASS

The claim is an exact **finite exhaustive** result for two specified graphs, not a universal theorem inferred by extrapolation. Separate Python indegree-elimination and C++ successor-path methods construct every possible bit mask (8192 and 131072 states), independently generate quadratic-residue adjacency, implement tie-retaining majority and classify each component. Both fully agree at every statistic, including the complete six-level entry histograms, recurrent counts, exact basin-size spectra and consensus totals. The package contains the source, baseline outputs and a single command that rebuilds and compares all results. The sharp global six-update cutoff follows because all states enter recurrence by update six and explicitly counted states have entry time six. Remaining mathematical risk is software defect shared by implementations or misinterpretation of the update convention, mitigated by differing adjacency and traversal methods and explicit hypotheses.

## Originality — PASS, qualified

The 1980 Goles–Olivos theorem is stronger in graph generality but weaker in the **exact numeric conclusions**: limiting possible periods to one and two does not imply their counts or attraction-basin spectra. The 2013 Tamuz–Tessler and 2015 Kaaser–Mallmann-Trenn–Natale papers supply broad behavior and voting-time results, not exact Paley-13 and Paley-17 populations. Related published exact results concern different undirected graphs, while published Paley-tournament majority dynamics is directed and has different neighborhoods and order. Direct record and alias searches did not identify prior exact data for these two undirected graphs. Unindexed data, equivalent encodings and an uninspected Goles–Olivos full text are residual priority risks; absence from retrieval is not evidence of historical uniqueness.

## Value — PASS

The prime-order Paley graphs are canonical self-complementary strongly regular graphs; the 17-vertex member is the classical extremal Ramsey witness. A complete attractor and basin census is a motivated exact finite dynamical invariant of this natural graph, not an arbitrary fixed subset of configurations. The sharp change from zero to 1,530 oscillatory attractors between two adjacent available prime orders, the identical maximal relaxation depths, and the sharply concentrated yet nontrivial consensus basins create a reusable benchmark for majority dynamics on symmetric finite graphs. No general asymptotic or downstream theorem is claimed or needed for the value of these concrete invariant populations.

## Scope and residual risk

The two orders only are proved, with synchronous open-neighbor majority and incumbent tie retention; the result does not provide a phase transition across all prime orders. Programmatic exhaustive evidence is reproducible but is not an independent external validation. Priority may be affected by an unindexed equivalent computation.

Self-review: passed. Independent audit: not yet performed.
