# Scientific review: exact two-leader inverse-square coherence on weighted friendship graphs

## Correctness — PASS

The object is the unnormalized weighted combinatorial Laplacian on \(F_m(t)=K_1\vee(mK_2)\), with integer \(m\ge2\), real \(t>0\), unit hub edges, and exactly two perfectly grounded leaders. Grounding retains edge-to-leader diagonal weights. Positive definiteness follows from connectedness and a nonempty grounded set. All candidate pairs fall into exactly three exhaustive symmetry orbits.

For each orbit, block inversion gives the full trace of the squared inverse, not the trace of the first inverse. The critical block identity uses \(s=d-u^{\mathsf T}B^{-1}u\) and \(q_j=u^{\mathsf T}B^{-j}u\), yielding \(\operatorname{tr}(M^{-2})=\operatorname{tr}(B^{-2})+(1+q_2)^2/s^2+2q_3/s\). The exact comparisons are \(J_2(S)-J_2(H)=m^2+m-7/4-(1+t)^{-2}>0\) and \(J_2(D)-J_2(H)=Q_m(t)/[4(1+2t)^2]\), with \(Q_m(t)=(4m^2+4m-39)t^2+(8m^2-46)t+4m^2+4m-11\). For \(m\ge3\), all polynomial coefficients are strictly positive; for \(m=2\), the polynomial is \(13-14t-15t^2\), with its sole positive root \((2\sqrt{61}-7)/15\). These facts prove every strict case and all equality cases for the full infinite family. The stated first-order comparison was checked against the accessible earlier theorem.

The enclosed `verify.py` executed successfully with SymPy 1.14, testing independent exact rational grounded inverses and the algebraic identities. Its 4,362 checks corroborate, but do not replace, the proof for all admissible parameters.

## Originality — PASS on inspected scientific evidence, with residual priority risk

The directly matching published weighted friendship theorem (`published-finding corpus/2026`, 2026-11-02) addresses \(\operatorname{tr}(L_{FF}^{-1})\), **not** \(\operatorname{tr}(L_{FF}^{-2})\). Its three-triangle transition is explicitly contradicted as an optimizer prediction for the second-order objective. The broader weighted clique-windmill theorem covers the friendship graph as a structural special case, but also optimizes only the first inverse. A finite-gain friendship result again treats the first-inverse criterion. An accessible second-order wheel theorem has the squared-inverse criterion but a non-isomorphic underlying graph. Patterson and Bamieh provide the second-order spectral moment, while Fitch and Leonard provide a general first-order leader framework; neither inspected manuscript states the weighted friendship inverse-square classification. The evidence establishes a non-implied new mathematical classification, not absolute priority.

The close specialist source, Sun, Li and Liu (2020), *Noisy consensus dynamics in windmill-type graphs*, was inspectable only through its abstract. That abstract cannot establish whole-document noncoverage. A stronger hidden theorem or unindexed equivalent would affect originality and requires later specialist assessment; the inaccessible full text is not silently declared negative evidence.

## Value — PASS

The result concerns a canonical graph family in pinned stochastic consensus, a physically motivated second-order coherence objective, and an exact continuous conductance parameter. It classifies all optimal pairs and every tie for all graph sizes and weights, not a numerical sample or an arbitrary finite slice. Its nontrivial square-root threshold at five vertices and the complete loss of the earlier three-triangle first-order transition give a mathematical boundary of practical leader-design relevance. In particular, whole open parameter intervals have opposite first- and second-order optimal leader classes, so the exact distinction cannot be deduced by reusing the first-order optimizer. General downstream conjectures and heterogeneous extensions are not claimed.

## Prior-work limits and reproducibility

See `RESULT.md` for the complete statement, normalization, proof and references, and `VERIFICATION.md` and `verify.py` for exact checks. An inaccessible relevant windmill-specific manuscript remains an explicit novelty risk; no independent mathematical or publication-priority audit has been completed.

Self-review: passed. Independent audit: not yet performed.
