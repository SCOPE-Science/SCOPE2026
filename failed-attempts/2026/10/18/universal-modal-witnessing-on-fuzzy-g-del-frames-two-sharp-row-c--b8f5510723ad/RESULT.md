# Universal modal witnessing on fuzzy Gödel frames: two sharp row criteria

## Finding
Let \(F=(W,R)\) be a nonempty standard Gödel–Kripke frame, where \(R:W\times W\to[0,1]\). For \(w\in W\), write \(S_w=\{v:R(w,v)>0\}\). Call the row at \(w\) *superlevel-finite* if, for every real \(\varepsilon>0\), the set \(\{v:R(w,v)\ge\varepsilon\}\) is finite.

The following conditions are exact, with the quantifier ranging over **all** propositional valuations \(e:W\times\mathrm{Var}\to[0,1]\) and all modal formulas \(\varphi\):

1. Every \(\Box\)-infimum at \(w\) is attained if and only if \(S_w\) is finite.
2. Every \(\Diamond\)-supremum at \(w\) is attained if and only if the row is superlevel-finite.

For either modality, requiring attainment only for the one propositional variable \(p\) already gives its equivalent criterion. Consequently every valuation makes the **entire model** witnessed in both modalities if and only if every world has finitely many positive-weight successors. Yet the \(\Diamond\)-only condition admits genuinely infinite branching, for example an infinite row with accessibility weights \(1/n\), \(n\ge1\).

## Assumptions and scope
All results hold in ordinary set theory for an arbitrary nonempty set \(W\), including uncountable sets, and arbitrary fuzzy accessibility weights in the real unit interval. The language is the usual propositional Gödel bimodal language with at least one propositional variable. Valuations are completely unrestricted; no continuity or measurability condition is imposed. The frame criterion concerns attainment of modal infima/suprema **uniformly across every valuation**, not merely the existence of some witnessed valuation, and is not a formula-definability statement.

The standard Gödel implication is \(a\Rightarrow b=1\) when \(a\le b\), and \(a\Rightarrow b=b\) otherwise. Modal truth values are
\[
e(w,\Box\varphi)=\inf_{v\in W}(R(w,v)\Rightarrow e(v,\varphi)),\qquad
e(w,\Diamond\varphi)=\sup_{v\in W}\min\{R(w,v),e(v,\varphi)\}.
\]
Witnessing means that the displayed numerical infimum or supremum is equal to one of its constituent values at some \(v\in W\), including the case \(R(w,v)=0\). This is the convention in the motivating 2026 source.

## Proof
**Box sufficiency.** Fix \(w\), any valuation, and any formula \(\varphi\). For every \(v\notin S_w\) the implication term is \(1\). If \(S_w\) is finite and nonempty, the minimum over \(S_w\) exists and is a global minimum. If \(S_w\) is empty, every term is \(1\); since \(W\ne\varnothing\), any world witnesses it. Thus finiteness of \(S_w\) forces attainment for every \(\varphi\).

**Box necessity, already for an atom.** If \(S_w\) is infinite, take pairwise distinct \(v_n\in S_w\), \(n\ge1\). Set
\[
e(v_n,p)=\min\{R(w,v_n)/2,1/(n+1)\}>0,
\]
and assign \(e(v,p)=1\) at every other world. On the selected worlds \(R(w,v_n)\Rightarrow e(v_n,p)=e(v_n,p)>0\) and the values tend to \(0\); at every unselected world the implication term is \(1\). Hence \(e(w,\Box p)=0\) without a witnessing world.

**Diamond sufficiency.** Assume the row is superlevel-finite. For an arbitrary \(\varphi\), put \(g(v)=\min\{R(w,v),e(v,\varphi)\}\), and \(d=\sup_{v\in W}g(v)\). If \(d=0\), every world witnesses it. Otherwise the set \(F_d=\{v:R(w,v)\ge d/2\}\) is finite and nonempty. For \(v\notin F_d\), \(g(v)<d/2\), so every value approaching the positive supremum \(d\) must occur in \(F_d\). The supremum is therefore the maximum of finitely many values on \(F_d\), and is attained.

**Diamond necessity, already for an atom.** If superlevel-finiteness fails, some \(\delta\in(0,1]\) has an infinite superlevel set \(\{v:R(w,v)\ge\delta\}\). Select distinct \(v_n\) in it and put
\[
e(v_n,p)=\delta\bigl(1-1/(n+1)\bigr),
\]
with \(e(v,p)=0\) everywhere else. Then \(\min\{R(w,v_n),e(v_n,p)\}=\delta(1-1/(n+1))<\delta\), whereas every unselected term is zero. The supremum is \(\delta\) but is not attained.

These four arguments prove both equivalences and the one-atom tests. Their simultaneous requirement reduces to finite positive supports, because finite support implies superlevel-finiteness. For separation, let \(W=\{w\}\cup\{v_n:n\ge1\}\), set \(R(w,v_n)=1/n\), and set all other accessibility weights to zero. All rows are superlevel-finite, so every valuation witnesses every \(\Diamond\)-supremum. The row at \(w\) has infinitely many positive entries, and the box countervaluation above shows that the frame is not uniformly \(\Box\)-witnessing. On a crisp frame, superlevel-finiteness is equivalent to finite branching, since every positive weight equals \(1\). This completes the proof.

## Verification
The standalone `verify.py` enumerates every pair of a finite accessibility row and atomic valuation with entries in \(\{0,1/3,2/3,1\}\) for row lengths \(1\) through \(4\), for a total of \(69{,}904\) cases, checking direct attainment of both extrema. It additionally checks exact rational finite-prefix patterns underlying the two infinite countervaluations. Run `python3 verify.py`; expected final marker: `GODEL_UNIFORM_WITNESSABILITY_CHECK_OK`. The genuine all-cardinality conclusions are proved above; finite enumeration and prefix calculations alone do not establish them.

## Relationship to prior work
Ferrari, Fiorentini, Giardini, and Rodriguez (2026) introduce exactly the witnessed semantics used here, give a non-witnessed infinite example, and prove a finite-model property for their logic. Their full text was inspected at the definition of witnessed models, the non-witnessed example, and main results; it does not state this classification of frame-uniform witnessing or the separate superlevel-finite condition for \(\Diamond\). Bílková, Frittella, and Kozhemiachenko (2022) discuss finite branching and frame definability in richer two-dimensional paraconsistent Gödel modal logics. Their Theorem 2 and surrounding proof are closely related to the **finite-branching** side of the result, which is not claimed as a wholly new phenomenon. Their theorem concerns a different formula-definability property and includes an additional fuzzy-weight gap condition; it does not give the present \(\Diamond\)-only characterization. The 2025 crisp witnessed-model paper is further background, not the source of the fuzzy row theorem.

## Limitations
The result is a criterion for **all valuations**, not a test for whether a given concrete infinite model happens to be witnessed. It does not prove a new axiomatization, completeness theorem, or complexity bound. The classification uses arbitrary atomic truth-value assignments and may change if valuations are constrained. While primary sources and mathematical research records were compared, historical priority cannot be guaranteed, especially against broader results in possibility theory or fuzzy aggregation that may imply the superlevel-finite characterization. No independent audit has been performed.

## References
1. M. Ferrari, C. Fiorentini, P. Giardini, R. O. Rodriguez, *A Gödel Modal Logic Over Witnessed Models* (2026), arXiv:2606.31906, https://arxiv.org/abs/2606.31906, DOI:10.4204/EPTCS.447.20. First public release: 2026-06-30.
2. M. Bílková, S. Frittella, D. Kozhemiachenko, *Paraconsistent Gödel Modal Logic* (2022), https://link.springer.com/chapter/10.1007/978-3-031-10769-6_26, especially Theorem 2.
3. M. Ferrari, C. Fiorentini, R. O. Rodriguez, *A Gödel Modal Logic over Witnessed Crisp Models* (2025), DOI:10.1007/978-3-032-06085-3_8.
