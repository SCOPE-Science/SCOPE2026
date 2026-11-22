# Review of the tournament-base extension spectrum

## Correctness — PASS

The finite-extension correspondence is justified by the strong amalgamation and ultrahomogeneity of the forbidden-independent-triple class. The proof partitions every extension according to its nonarc graph on the new labels, and checks every possible position of a forbidden triple. The local extension weight is precisely \(W(H)=\sum_{S\in\mathcal I(H)}2^{r-|S|}\), with no orientation constraint omitted. For the asymptotic statement, the maximal weights with zero, one, and at least two nonarc edges are obtained by direct ternary assignments. The two-edge patterns, and then all three-edge patterns, establish the sharp error base for fixed arity. The rare-event claim follows by dividing the corresponding nonarc contributions by the total, not by assuming independent nonarc events. Direct independent finite enumeration in `verify.py` matches the exact graph-sum for all tested \((n,r)\), including \((3,3)\). The infinite-family theorem rests on its symbolic proof, not on those tests.

## Originality — PASS, provisional

Aranda's full available 2015 preprint (arXiv:1505.00235, §§1–2, especially Remark 1.2, Proposition 1.3, Theorem 2.1 and the global counting argument), along with the original thesis chapter (§4), concerns *unconditioned* asymptotic counts of entire labelled digraphs and the generic limit's existence. Its counting estimates use the local eight-way choice for a nonarc pair, but do not state the finite-tournament-base, fixed-new-arity orbit spectrum or the full transfer-polynomial decomposition. Galanis et al. (arXiv:1105.5131, introduction) define the standard hard-core independent-set partition function, not model-theoretic orbit spectra. Searches for nonarc/independent-triple aliases, fixed-base tuple types, the exact two-point exponential signature, broader formulas, and nearby internal published results found no dominating statement. This is not a proof of historical priority. A hidden equivalent treatment of oriented complements of triangle-free graphs is the main remaining risk.

## Mathematical value — PASS

The theorem addresses a natural local-versus-global counting question in a homogeneous oriented structure: how do complete extension-type distributions change when an increasingly large *tournament* is named? The exact all-fixed-arity graph-sum and its three sharp spectral layers identify which configurations survive and give an explicit exponential scale \((8/9)^n\) for the first forbidden-tournament deviation. The conditional concentration on a unique nonarc is a structural rare-defect law not implied by the global result that unconditioned large digraphs are typically bitournaments. This is more than a finite tabulation or an arbitrary numerical slice, although it does not establish a growing-arity uniform law.

## Sources, comparison, and limitations

- Andrés Aranda, *Asymptotic Enumeration of \(I_3\)-free Digraphs* (2015), https://arxiv.org/abs/1505.00235. The statement \(|F(n)|/|T(n)|\to1\) has a different asymptotic regime, and the full formula here does not follow from it without counting conditioned finite extensions.
- Andrés Aranda López, *Omega-categorical simple theories*, 2013 thesis, publicly deposited 21 January 2015, https://etheses.whiterose.ac.uk/id/eprint/7838/. Chapter 4 supplies the relevant existence proof and nonarc-graph equivalence.
- Andreas Galanis et al., *Improved Inapproximability Results for Counting Independent Sets in the Hard-Core Model*, arXiv:1105.5131. Its independence-polynomial definitions are used as established background, not presented as new.

The result is restricted to tournament bases and fixed new tuple arity; uniform type sampling has no natural interpretation as uniform sampling of vertices in the infinite structure. Historical priority remains provisional and independent mathematical checking has not been performed.

Self-review: passed. Independent audit: not yet performed.
