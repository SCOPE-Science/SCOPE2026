# Sharp depth-bounded model-size cutoff for basic modal logic

## Finding

Fix integers \(k\ge 0\) and \(d\ge 1\). In the ordinary Boolean unimodal language with exactly \(k\) available propositional letters, let modal depth count the maximum nesting of \(\Diamond\) or \(\Box\). All Kripke frames are permitted, including self-loops and empty successor sets. Define integers \(h_0=2^k\) and \(h_{j+1}=2^k 2^{h_j}\) for \(j\ge0\).

**Theorem.** Every satisfiable formula of modal depth at most \(d\) has a pointed Kripke model on at most \(h_{d-1}\) worlds. This is the **least** uniform cardinality bound: some formula of depth exactly \(d\) has no model on fewer than \(h_{d-1}\) worlds. At depth zero the least bound is one world.

In particular the exact bounds for \(k=0\) are \(1,2,4,16\) at depths \(1,2,3,4\); for \(k=1\) they are \(2,8,512\) at depths \(1,2,3\). These are finite-model cutoffs, not statements about complexity in formula length. The bound permits cycles and loops; no corresponding optimality is asserted for irreflexive, acyclic, transitive, or serial frames.

## Assumptions and scope

A Kripke model consists of a nonempty finite or infinite carrier \(W\), arbitrary relation \(R\subseteq W^2\), and arbitrary valuation of the \(k\) letters. Satisfaction is classical at each world, with \(w\models\Diamond\varphi\) iff some \(R\)-successor of \(w\) satisfies \(\varphi\), and \(\Box\) its dual. Formula satisfiability means satisfaction at one distinguished world in some (possibly infinite) model. A formula may use fewer than \(k\) of the letters.

A **complete depth-\(j\) type** is defined recursively. Set \(\mathcal T_0=\{0,1\}^k\), viewed as the set \(C\) of Boolean colors. For \(j\ge0\), set \(\mathcal T_{j+1}=C\times\mathcal P(\mathcal T_j)\). At a world, the type \(\tau_0\) is its color, and \(\tau_{j+1}(w)=(\operatorname{col}(w),\{\tau_j(v):wRv\})\). Thus \(|\mathcal T_j|=h_j\).

For \(j\ge1\), define the truncation map \(\pi_j:\mathcal T_j\to\mathcal T_{j-1}\) by \(\pi_1(c,S)=c\), and for \(j\ge2\), \(\pi_j(c,S)=(c,\{\pi_{j-1}(u):u\in S\})\). These maps are surjective, since \(\pi_1\) is, and any set of predecessor types has a set of preimages. The constructed models below realize every stated type, so no formally defined but unrealizable type is counted.

## Proof

**(1) Depth types describe exactly what formulas see.** Induction on formulas shows that agreement of depth-\(j\) types implies agreement on formulas of modal depth at most \(j\). Conversely define characteristic formulas recursively. For a color \(c\), let \(\chi_0(c)\) be the conjunction specifying exactly which of the \(k\) variables hold. Given \(t=(c,S)\in\mathcal T_{j+1}\), define
\[
\chi_{j+1}(t)=\chi_0(c)\wedge\bigwedge_{u\in S}\Diamond\chi_j(u)\wedge\Box\bigvee_{u\in S}\chi_j(u).
\]
Empty conjunctions are \(\top\), and empty disjunctions are \(\bot\). By induction, \(\chi_j(t)\) holds at exactly the worlds of type \(t\). In particular distinct depth-\(j\) types are mutually exclusive. Every formally defined type is realizable: start with finite representatives for its prescribed successor types, take disjoint copies, and add a fresh root with precisely those representative roots as successors.

**(2) A universal carrier of previous-depth types.** Fix an arbitrary target \(t=(c,S)\in\mathcal T_d\). Let \(W=\mathcal T_{d-1}\), a carrier of size \(h_{d-1}\), and label each node \(v\in W\) with its own abstract type \(v\). Choose the distinguished root \(r=\pi_d(t)\in W\). Give each node the valuation indicated by its label's color. Make the root's successor set **exactly** \(S\subseteq W\).

For \(d=1\), this fully specifies the root's depth-one type and no other edges matter. For \(d\ge2\), choose one section \(\sigma:\mathcal T_{d-2}\to\mathcal T_{d-1}\) of \(\pi_{d-1}\). For every nonroot node with label \(v=(c_v,A_v)\in\mathcal T_{d-1}\), make its successor set \(\{\sigma(u):u\in A_v\}\). There is no constraint against an edge to the root or to itself.

We verify *simultaneously* that every node's actual depth-\((d-1)\) type is its label. At depth zero this holds by the chosen valuation. Assume actual depth-\(j\) types equal the \((d-1-j)\)-fold truncations of labels. For a nonroot node, the set of successors' depth-\(j\) types is exactly the truncation of \(A_v\) to depth \(j\), by the section property. For the root the same holds because \(r=\pi_d(c,S)\), whose successor-type set at depth \(d-2\) is \(\{\pi_{d-1}(u):u\in S\}\); further truncations commute with taking sets. Thus the induction goes through every \(j\le d-2\). The root therefore sees precisely the full depth-\((d-1)\) type set \(S\), and its actual depth-\(d\) type is \(t\).

Every satisfiable depth-at-most-\(d\) formula has some realized type \(t\); the constructed \(h_{d-1}\)-world pointed model has the same type and satisfies it.

**(3) Sharpness.** Let
\[
\Phi_{k,d}=\bigwedge_{u\in\mathcal T_{d-1}}\Diamond\chi_{d-1}(u).
\]
This formula has modal depth exactly \(d\) and is satisfiable by step (2) with \(S=\mathcal T_{d-1}\). Every model of it must have a distinct successor for each \(u\), because distinct characteristic formulas cannot hold at the same world. Thus every model has at least \(h_{d-1}\) worlds. Step (2) supplies equality. For \(d=0\), any satisfiable propositional formula has a single-world model and some satisfiable formulas require a nonempty carrier. This proves the theorem.

## Verification

Run `python3 checker.py` with Python 3 and no external dependencies. It constructs every target type for \((k,d)=(0,1),(0,2),(0,3),(0,4),(1,1),(1,2),(2,1)\) and independently recomputes the successive semantic types at every world of each constructed frame. It also checks 200 reproducibly sampled depth-three target types when \(k=1\), whose predecessor universe has 512 worlds. The expected terminal line is `MODAL_SHARP_DEPTH_CUTOFF_OK` and the expected total is 66,342 checked cases.

This finite checker is a consistency test, **not** a substitute for the universally quantified proof in steps (1)–(3); in particular, it does not enumerate the \(2^{513}\) depth-three types for one letter.

## Relationship to prior work

The finite-tree-model and filtration theorems give model-existence bounds, normally dependent on formula subexpressions and commonly using tree unravellings or quotient types. The present statement instead fixes only the number of letters and modal depth, obtains the **exact least possible** uniform world count, and attains it by reusing lower-depth type representatives within a possibly cyclic graph.

Lück (2019), Section 4, proves the same exact recurrence for the **number of depth types** (Proposition 4.7) and constructs a canonical model realizing all depth-\(d\) types simultaneously (Lemma 4.8). Its canonical carrier must contain at least \(h_d\) worlds and the construction uses stages. The present assertion concerns a *different and smaller* model for **each selected pointed type**, with the exact optimum \(h_{d-1}\); the type-count recurrence alone and the canonical construction do not assert this optimization. This is the closest inspected prior source and a genuine priority caveat.

Schröder and Pattinson's shallow-model construction gives a size bound \(3^n\) with \(n\) the number of subformulas, but no claimed sharp fixed-depth, fixed-vocabulary cutoff. Anttila, Häggblom and Yang use standard finite-depth Hintikka types for modal inclusion logic; this gives the characteristic-formula ingredient but not the sharp cyclic model compression as stated here. Alpay and Basaran's recent small-frame computational investigation concerns a finite formula corpus and examples of bounded indistinguishability; its accessible abstract does not state this uniform exact bound. An equivalent result in standard model-theory folklore or inaccessible full text remains a historical-priority risk.

## Limitations

No claim is made for frame classes excluding self-loops: the construction may use them, and its sharp bound can fail under additional frame conditions. The complete-type characteristic formulas grow very rapidly; the result does not bound formula length or give an efficient general decision algorithm. For depth \(d=0\) the special cardinality is one. Full-text access to the 2026 motivating paper was unavailable during the comparison; the priority assessment uses its dated abstract and publicly accessible technical overview and remains qualified.

## References

- Faruk Alpay and Baris Basaran, *GPU-Accelerated Search and Certification of Bounded Indistinguishability in Finite Kripke Semantics*, arXiv:2606.15437, first posted 13 June 2026, https://arxiv.org/abs/2606.15437.
- Lutz Schröder and Dirk Pattinson, *PSPACE Bounds for Rank-1 Modal Logics*, arXiv:0706.4044, 2007; ACM Transactions on Computational Logic 10(2), 2009. Full text: https://arxiv.org/abs/0706.4044.
- Aleksi Anttila, Matilda Häggblom, and Fan Yang, *Axiomatizing modal inclusion logic and its variants*, Archive for Mathematical Logic 64 (2025), 755–793, https://doi.org/10.1007/s00153-024-00957-y; see Section 3 on Hintikka formulas.
- Martin Lück, *Canonical Models and the Complexity of Modal Team Logic*, Logical Methods in Computer Science 15(2), 2019, Section 4, arXiv:1709.05253, https://arxiv.org/abs/1709.05253.
