# Scientific review

**Correctness — PASS.** Summing bits by read offset gives \(c_{t+1}-c_t=w_{t+r}-w_t\). These signed differences identify all nonconstant residue chains. When \(n\ge4r-1\), every constant residue chain has length at least four except at most one of length three; known weight three determines them. At the boundary \(r=\lceil(n+2)/4\rceil\), two or more cyclic phases of one marker per period each have weight three and identical length-\(k\) decks. The proof handles the exact \(n\ge8\) range. The standalone enumerator confirms the prediction on finite instances; it does not substitute for the proof.

**Originality — PASS against examined sources.** Angal et al. study *scattered* length-\(k\) decks, not contiguous-window multisets. Piña–Uzcátegui study equalities of *all* factor decks below a cutoff, not a single length. Indexed cyclic three-marker read thresholds concern necklaces and differ in both the object and numerical bound. The two-marker linear result in accessible prior records concerns a different fixed-weight family, and short fixed-trigram results do not imply a sharp variable-read-length theorem. None of these inspected claims entails the combined exact threshold and offset-marginal reconstruction. An unindexed equivalent remains a priority risk.

**Value — PASS.** Exact maximum ambiguous read lengths are natural zero-error reconstruction invariants, and the proof identifies a very small sufficient statistic (read-offset marginals) for all long reads. The phase-collision construction matches this sufficient regime sharply and exposes a reason sparse linear strings behave differently from circular strings. The result is not merely a finite table or routine arithmetic specialization.

**Scientific limitations.** The new theorem does not classify all shorter-read fibers or general Hamming weights; only a self-review was carried out. The relevant preliminary literature comparison is not a guarantee of historical priority.

Self-review: passed. Independent audit: not yet performed.
