# Scientific review: triple-plus-singleton Abelian-square theorem

**Correctness — PASS.** All possible distinct Abelian squares are partitioned by their number of occurrences of the sparse letter (zero, two, four). The proof derives exact necessary-and-sufficient half-length conditions and disjointness, including the \(j=0\) duplicate, then proves the sharp lower bound for every integer parameter triple via an exhaustive three-case inequality. Four residue-class families attain equality for every \(n\ge5\). The independent literal enumeration in `verify.py` passed 6,859 triples and all restricted lengths 4–40; it corroborates rather than substitutes for the proof.

**Originality — PASS, with residual risk.** Fazekas et al. (arXiv:2604.23188, Sections 3–5 and Theorem 12) obtain fixed-weight minima up through three occurrences and give an effective four-run example. A previously recorded general four-run enumeration covers the boundary \(k=0\); its hypotheses do not cover genuine five-run words \(i,j,k>0\), and its four-run sharp minimum does not supply the new factor-set formula or five-run lower bound. Actual published-record and literature queries found no implication-equivalent result for the three-plus-singleton five-run family. Priority outside the indexed or inspected literature remains unconfirmed.

**Value — PASS.** Four occurrences of a minority symbol are the first open fixed-weight case in the motivating source. The run-composition \((3,1)\) is a natural, non-arbitrarily chosen structural subfamily, not a numeric slice. The theorem gives the complete *literal* factor-language invariant for all parameters, proves the exact bound even when a fifth run is present, and isolates the remaining marker compositions to investigate for the unrestricted problem. The existence of four-run equality witnesses is not counted as a new contribution.

**Limits.** No conclusion is made for the other four-marker run compositions, higher weights or global optimality among unrestricted four-marker words. An equivalent unindexed treatment might exist. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
