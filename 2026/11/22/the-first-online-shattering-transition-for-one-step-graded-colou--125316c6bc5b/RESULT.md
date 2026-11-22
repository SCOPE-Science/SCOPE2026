# The first online-shattering transition for one-step graded colour tests

## Finding
Fix any integer \(q\ge2\) of mutually exclusive successor colours. Let \(X_{q,d}=\{(c_1,\ldots,c_q)\in\mathbb N^q:\sum_i c_i\le d\}\) be the possible colour-count vectors of finite rooted stars with at most \(d\) terminal successors. For each nonempty \(S\subseteq[q]\) and integer \(1\le t\le d\), consider the root classifier
\[
 h_{S,t}(c)=\mathbf 1\!\left\{\sum_{i\in S}c_i\ge t\right\},
\]
plus the constantly true and constantly false classifiers. In description-logic notation these are exactly the one-restriction concepts \((\ge t\,r.\bigvee_{i\in S}P_i)\), together with \(\top\) and \(\bot\), evaluated at roots of these stars. Write \(\mathcal H_{q,d}\) for this finite hypothesis class.

The exact static (VC) and adaptive (Littlestone) shattering dimensions for the first three successor caps are
\[
 \boxed{\operatorname{VCdim}(\mathcal H_{q,d})=q\quad (d=1,2,3),\qquad
 \operatorname{Ldim}(\mathcal H_{q,d})=\begin{cases}q,&d=1,2,\\q+1,&d=3.\end{cases}}
\]
Thus allowing two successors rather than one does not increase worst-case adaptive depth; allowing three does, and creates a sharp one-level gap between adaptive and nonadaptive shattering for every number of colours \(q\ge2\). This is a threshold for **one qualified counting restriction**, not a claim about unrestricted description-logic formulas.

## Assumptions and scope
A rooted star has a distinguished root, no loops, and a finite collection of terminal successors, each assigned **exactly one** of the named unary concepts \(P_1,\ldots,P_q\). The root has no other relevant features. All finite rooted stars whose outdegree is at most \(d\) are admitted as examples; two stars are identified as examples if their successor-colour count vectors agree. The role \(r\) is the single root-to-leaf relation. The only permitted hypotheses are the displayed single graded test, \(\top\), and \(\bot\); disjunction occurs **inside** the one counting restriction, and arbitrary combinations of graded tests are excluded. Counts are of distinct successor worlds. Degrees \(d\in\{1,2,3\}\); colours \(q\ge2\).

A set of \(k\) examples is VC-shattered when every binary labeling is realized by a hypothesis. A complete Littlestone tree of depth \(k\) has an example at each internal node and, for every binary path of length \(k\), at least one hypothesis whose predictions match the path. At different internal nodes, examples may be chosen adaptively. This is the finite-class, realizable, adversarial online-learning notion of Littlestone dimension.

## Proof
**1. Exact number of different hypotheses.** For every \(q\ge2\) and positive cap \(d\), the \(d(2^q-1)\) tests \(h_{S,t}\) are pairwise distinct, and differ from the two constants. Indeed, if \(S\ne T\), choose a colour belonging to one of the two sets but not the other, and take \(d\) successors of that colour; the test using that colour is true for any allowed positive threshold, while the other is false. For fixed \(S\) with different thresholds, take exactly the smaller threshold's number of successors of a colour in \(S\). The all-empty star and a suitable full-colour star separate the constants. Therefore
\[
 |\mathcal H_{q,d}|=d(2^q-1)+2.
\]
Every complete binary mistake tree of depth \(k\) needs at least \(2^k\) different hypotheses, because a fixed hypothesis follows only one complete outcome path. Hence \(\operatorname{Ldim}\le\lfloor\log_2|\mathcal H_{q,d}|\rfloor\).

**2. Static lower bound.** The \(q\) one-successor examples \(e_1,\ldots,e_q\) are shattered by tests \(h_{S,1}\): the trace is exactly \(S\), with the empty trace supplied by \(\bot\). In particular both dimensions are at least \(q\) for all three caps.

**3. Uniform static upper bound.** Enlarge the hypothesis class to all nonnegative-weight linear thresholds \(c\mapsto\mathbf1\{\sum_i w_i c_i\ge\theta\}\) with \(w_i\ge0\) and arbitrary real \(\theta\). No \(q+1\) examples can be shattered even by this larger class. To see this, let \(x^1,\ldots,x^{q+1}\in\mathbb R^q\) and form the square matrix \(M\) whose rows are \((x^j,-1)\). Let \(z=M(w_1,\ldots,w_q,\theta)^\top\); the positive label means \(z_j\ge0\) and the negative label means \(z_j<0\).

If \(M\) is singular, choose a nonzero vector \(a\) with \(a^\top M=0\). Since the final column of \(M\) is constant, \(\sum_j a_j=0\), so \(a\) has both positive and negative components. Prescribe positive labels where \(a_j>0\), and negative labels where \(a_j<0\). Any realization would satisfy \(a^\top z>0\), contradicting \(a^\top z=0\).

If \(M\) is nonsingular, fix any coordinate index \(i\le q\). The row \(b\) of \(M^{-1}\) recovering \(w_i=b^\top z\) is nonzero, and \(\sum_j b_j=0\): setting \(z\) equal to the all-ones vector corresponds to \(w=0\) and \(\theta=-1\). Thus \(b\) has positive and negative components. Prescribe positive labels wherever \(b_j<0\), negative labels wherever \(b_j>0\). Every realizing vector would give \(w_i=b^\top z<0\), contradicting \(w_i\ge0\). This proves \(\operatorname{VCdim}\le q\). Combining with step 2 gives the stated equality for all three caps.

**4. Exact online dimension at cap one.** The cardinality formula gives \(|\mathcal H_{q,1}|=2^q+1<2^{q+1}\). Thus online dimension is at most \(q\), with equality by step 2.

**5. The two-successor plateau.** At cap two, \(|\mathcal H_{q,2}|=2^{q+1}\). A complete depth-\(q+1\) mistake tree would have to split all hypotheses into exactly two halves, each of size \(2^q\), at its first query. Yet every example \(c\in X_{q,2}\) is one of: zero vector, one successor, two successors of the same colour, or two successors of distinct colours. The numbers of hypotheses positive on these four respective kinds of examples are
\[
 1,\qquad 2^{q-1}+1,\qquad 2^q+1,\qquad 2^q+1.
\]
The last number for distinct colours follows because the \(t=1\) tests count \(3\cdot2^{q-2}\) nonempty subsets meeting the two colours, while the \(t=2\) tests count \(2^{q-2}\) subsets containing both. None of the four positive counts is \(2^q\) when \(q\ge2\). Therefore the required balanced first split does not exist, and \(\operatorname{Ldim}\le q\). Step 2 gives equality.

**6. A sharp depth-\(q+1\) adaptive tree at cap three.** For brevity designate the last colour as \(q\), and use \(e_i\) for its standard count vectors. Ask first about \(2e_q\).

On the positive answer, restrict to the hypotheses \(h_{S,t}\) with \(q\in S\) and \(t\in\{1,2\}\). Next ask \(e_q\), distinguishing \(t=1\) from \(t=2\). In the \(t=1\) branch, ask \(e_i\) for each \(i<q\); the answer is exactly whether \(i\in S\). In the \(t=2\) branch, ask \(e_q+e_i\) for each \(i<q\), again recovering the independent membership bits. Both subtrees have \(q-1\) further levels, so the first positive branch has depth \(q\).

On the negative answer to \(2e_q\), next ask \(3e_q\). For the positive answer retain all \(h_{S,3}\) with \(q\in S\), and ask \(2e_q+e_i\) for \(i<q\) to recover the \(q-1\) independent membership bits. For the negative answer retain \(h_{S,1}\) with \(S\subseteq[q-1]\) and \(S\ne\emptyset\), together with \(\bot\), and ask \(e_i\) for \(i<q\). Thus this branch too contains \(q\) complete levels. Every query uses at most three successors. This is a full depth-\(q+1\) mistake tree, with an explicit different witness hypothesis for every one of its \(2^{q+1}\) leaves.

Finally \(|\mathcal H_{q,3}|=3\cdot2^q-1<2^{q+2}\), so no tree can have depth \(q+2\). Equality follows.

## Verification
The standalone exact-integer Python checker at `artifacts/check.py` enumerates all allowed count vectors and semantic hypotheses; it independently computes Littlestone dimensions by memoized exhaustive binary-query splitting for \(q=2,3,4\) and \(d=1,2,3\). It exhaustively computes static VC dimensions for \(q=2,3\) and these caps, checks pairwise hypothesis distinction, and verifies every outcome path of the explicit depth-\(q+1\) tree for all \(2\le q\le9\). Run `python3 artifacts/check.py` from the extracted package root. The checks terminate with `VERIFY_OK`; finite enumeration is supporting evidence, while the proofs above establish every allowed unbounded \(q\).

## Relationship to prior work
Funk, Jung, and Voellmer, *Bounded Fitting for Expressive Description Logics* (first arXiv version May 8, 2026), develop learning with \(\mathcal{ALCQ}\) qualified number restrictions, give general VC/Occam guarantees, and use thresholds up to three in their experiments. Their available full text and appendices do not state the exact online ranks of this one-restriction, exclusively coloured, bounded-degree star class. The earlier general work on finitely characterizing description-logic concepts by ten Cate, Koudijs, and Ozaki concerns example-based characterizations rather than this fixed hypothesis class's adaptive dimension. A published result titled *Sperner-optimal compression of positive graded modal stars and their exact two-variable spectrum* proves sharp successor compression and semantic-profile counting for a **positive multi-test language** on stars, not the single graded-threshold hypothesis class or its VC/Littlestone comparison. *Sharp value-sensitive successor budgets for finite Heyting-valued modal logic* addresses exact modal-value preservation and hitting sets, not classification shattering. The general cardinality argument for hypothesis classes and the matrix-based VC obstruction are standard methods and are not claimed new; the claimed contribution is their exact application together with the sharp two-to-three adaptive transition and the full adaptive witness tree.

## Limitations
This is a deliberately narrow **single counting test** hypothesis class. Allowing arbitrarily nested formulas, unrestricted Boolean combinations of counting tests, nonexclusive successor valuations, additional roles, or larger successor caps changes the problem and is not covered. In particular no claim about the learning dimension of all \(\mathcal{ALCQ}\) concepts is made. The all-parameter result covers all \(q\ge2\) but only the natural first three degree caps. Search and inspection cannot certify historical priority; an earlier equivalent result under the terminology of Boolean subset-sum thresholds or online learning remains possible. No independent mathematical audit has been performed.

## References
1. Maurice Funk, Jean Christoph Jung, Tom Voellmer, *Bounded Fitting for Expressive Description Logics*, arXiv:2605.07452v1, May 8, 2026, https://arxiv.org/html/2605.07452v1, especially sections 2, 4, 5 and appendices.
2. Balder ten Cate, Raoul Koudijs, Ana Ozaki, *On the Power and Limitations of Examples for Description Logic Concepts*, arXiv:2412.17345v1, December 23, 2024, https://arxiv.org/abs/2412.17345.
3. *Sperner-optimal compression of positive graded modal stars and their exact two-variable spectrum*, published mathematical record, October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sperner-optimal-compression-of-positive-graded-modal-stars-and-t--5cec5be4d532.
4. *Sharp value-sensitive successor budgets for finite Heyting-valued modal logic*, published mathematical record, October 18, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-value-sensitive-successor-budgets-for-finite-heyting-value--533e4477e12f.
