# Self-review of an explicit finite-field toric code equivalence

## Correctness — PASS

For \(k=\mathbb F_8\), the group \(k^*\) has order \(7\), so \(x^6=x^{-1}\). The Laurent section spaces read directly from the two published polygons are \(L_4=\langle1,x,x^2,x^3,y,y^{-1}\rangle\) and \(L_5=\langle1,x,x^2,x^3,y,x^{-1}y^{-1}\rangle\). The map \(\phi(x,y)=(x^{-1},x^{-3}y)\) permutes all \(49\) torus points and squares to the identity. Multiplying by \(x^3\) gives a nonzero coordinate weight. The explicit calculation \(x^3f(\phi(x,y))=a_3+a_2x+a_1x^2+a_0x^3+by+cx^{-1}y^{-1}\) proves an invertible row reversal and hence the desired monomial equivalence. The finite verifier checks the generator ranks, bijective coordinate permutation, and exact matrix identity on all \(49\) points. The source pictures and explicit normalized areas confirm that the polygons are lattice-inequivalent: their boundary counts are \(4\) and \(3\). General claims follow symbolically rather than from a sampled numerical search.

## Originality — PASS, qualified

Luo–Yau–Zhang–Zuo, arXiv:1402.0060 (2014) and the published 2015 version, explicitly identify equality of the full weight enumerators but leave the precise \(\mathbb F_8\) pair \(P_6^{(4)},P_6^{(5)}\) open as Conjecture 1.1. The new 49-coordinate involution is not contained in those statements: equal enumerators do not imply equivalence. Their explicit \(\mathbb F_7\) equivalence concerns a different pair. The 2020 dimension-seven classification by overlapping authors concerns seven-point polygons and does not provide the missing six-point monomial map. Targeted source and mathematical-record searches did not locate an equivalent direct construction. A possible unindexed specialist resolution remains a historical-priority risk, not an algebraic uncertainty in the proof.

## Mathematical value — PASS

This is the explicitly named outstanding equivalence in a published classification of all six-dimensional toric surface codes. Settling it removes the final ambiguity in that classification. Its involution explains how finite-field reduction of exponent vectors modulo the order \(7\) of \(\mathbb F_8^*\) can identify codes on inequivalent lattice polygons. The precise geometric/coding-theoretic question is independently motivated by the source's conjecture and its sharp classification scope.

## Closest sources and scientific limits

The 2014 arXiv preprint, 2015 journal version, and the 2020 dimension-seven sequel were examined for exact-claim and stronger-coverage comparisons. The result concerns this pair over \(\mathbb F_8\) only; its displayed map does not assert equivalence over other fields, nor resolve the 2020 dimension-seven open cases. The stated proof is self-reviewed and finite-field-replayed, but independent scientific validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
