# Review of a sharp five-site monomer-adsorption phenomenon

## Correctness — PASS

For any graph, conditioning on its first adsorption attempt yields an exact rational recursion over induced subgraphs. The finite domain through order five is completely enumerated. Every one of the 1,099 labeled graphs through order five has its recursive terminal mean independently cross-checked against its full permutation enumeration. Connected pregraph/missing-edge comparison yields exactly 180 strictly positive augmentations on five vertices, all of gain \(1/15\), partitioning into two marked isomorphism classes. Their conditional-prefix means give a common exact polynomial valid for all real times. Its cubic factor is strictly increasing because the derivative quadratic has negative discriminant; boundary signs give a unique positive crossover time. The `verify.py` source and its actual run were inspected and replayed.

## Originality — PASS on inspected evidence, subject to historical priority

The 2019 paper by Krivelevich and collaborators already proves nonmonotonicity *exists* and explicitly presents a six-vertex-and-larger family; that qualitative discovery is **not** claimed as novel. Material inspection of Section 8 and the concluding discussion found no sharp order-five classification or common temporal crossover. The 2015 Brightwell–Janson–Luczak preprint studies the asymptotic jamming law of random graphs with given degrees, not a smallest connected marked-augmentation census. Public scholarly searches and mathematical-result comparisons did not reveal a stronger statement determining these exact two five-vertex classes. The 1989 Pippenger article could only be checked at the abstract level: its full text was inaccessible through the attempted sources, leaving a historical-priority risk.

## Mathematical value — PASS

Whether adding an exclusion relation can *increase* terminal occupancy is a naturally motivated physical monotonicity question. A sharp minimum order and complete description of all smallest connected witnesses identify the precise local network structures where the paradox begins. The additional exact all-time law demonstrates that each beneficial exclusion bond initially suppresses occupation, yet improves the jammed mean, with one common threshold rather than unrelated finite counts. These facts are stricter than the known six-vertex qualitative witness and provide an exact finite benchmark for irreversible exclusion kinetics. Larger-graph classification and stochastic dominance are not established.

Self-review: passed. Independent audit: not yet performed.
