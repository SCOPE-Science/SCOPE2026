# An all-time forbidden-basis law for synchronous traffic Rule 184

## Finding
Let \(F\) be elementary cellular automaton Rule 184 acting synchronously on the bilateral full binary shift \(\{0,1\}^{\mathbb Z}\), and put \(Y_t=F^t(\{0,1\}^{\mathbb Z})\) for each integer \(t\ge0\). Then, for every integer \(t\ge1\), the **complete and minimal forbidden-word set** of the spatial subshift \(Y_t\) is exactly
\[
\mathcal M(Y_t)=\{\,11(01)^j00:0\le j<t\,\}.
\]
Consequently every finite-time image is a shift of finite type, the images descend strictly at **every** time \(t\ge0\), and the shortest length at which the languages of \(Y_t\) and \(Y_{t+1}\) differ is exactly \(2t+4\). No eventual finite-time image stabilization occurs.

## Assumptions and scope
Positions range over the bilateral integer lattice, with no cyclic boundary or fixed density assumption. For any \(a,b,c\in\{0,1\}\), define
\[
f(a,b,c)=(a\wedge\neg b)\vee(b\wedge c),\qquad (Fx)_i=f(x_{i-1},x_i,x_{i+1}).
\]
The superscript on \(F\) denotes simultaneous temporal iteration. A finite word belongs to a subshift's language if it appears at some spatial position in some bilateral configuration in that subshift. A minimal forbidden word does not appear but all its proper contiguous subwords do. The all-time assertion quantifies over **every integer time**; the finite checker is supporting evidence and not the source of the all-time induction.

Set \(W_j=11(01)^j00\). For each \(t\ge0\), denote by \(X_t\) the bilateral shift avoiding \(W_j\) for all integers \(0\le j<t\), with \(X_0\) the full shift. We prove \(F(X_t)=X_{t+1}\) for all \(t\ge0\).

## Proof
**1. Bond defects and their exact local motion.** Place an \(A\)-defect at bond \(i\) if \(x_ix_{i+1}=11\), and a \(B\)-defect there if \(x_ix_{i+1}=00\). Other bonds are alternating. If an \(A\)-defect at \(a\) and a \(B\)-defect at \(b>a\) are consecutive among all defects, then the interval from them is necessarily \(11(01)^j00\), where \(b-a=2(j+1)\). Hence \(x\in X_t\) if and only if every consecutive \(A\)-to-\(B\) pair of defects has bond separation at least \(2(t+1)\). The condition is vacuous when there is no such pair.

Computing two adjacent output symbols from all sixteen four-bit input contexts gives the following complete list. The output has an \(A\)-defect at its bond \(i\) exactly for input four-bit contexts at positions \(i-1,\ldots,i+2\) equal to `0111`, `1011`, or `1111`; it has a \(B\)-defect there exactly for `0000`, `0001`, or `0010`. Equivalently, every input \(A\)-defect at bond \(a\) moves to \(a-1\), and every input \(B\)-defect at bond \(b\) moves to \(b+1\), except that an adjacent \(B,A\) pair at bond separation two (the four-symbol pattern `0011`) annihilates. No defects are created. This is a complete local truth-table identity, not a particle-model approximation.

**2. Forward inclusion.** Fix any \(t\ge0\) and \(x\in X_t\). Take consecutive \(A,B\)-defects at output bonds \(a',b'\). Their undeleted input ancestors are at \(a=a'+1\) and \(b=b'-1\). The input interval between \(a\) and \(b\) contains an input consecutive \(A,B\) pair: any intermediate defects that disappeared must have been disjoint \(B,A\) collision pairs, so the first \(B\) after the ancestral \(A\) is immediately preceded in defect order by an \(A\). Thus \(b-a\ge 2(t+1)\). Therefore
\[
b'-a'=(b+1)-(a-1)=(b-a)+2\ge 2(t+2).
\]
Every output consecutive \(A,B\) pair satisfies the defining bound of \(X_{t+1}\); therefore \(F(X_t)\subseteq X_{t+1}\).

**3. Exact inverse branch on the first image.** Define the reflected traffic map \(G\) (elementary Rule 226) by
\[
(Gy)_i=g(y_{i-1},y_i,y_{i+1}),\qquad
 g(a,b,c)=(c\wedge\neg b)\vee(b\wedge a).
\]
The complete thirty-two-case five-bit check for the center symbol of \(F(Gy)\) gives discrepancies only in the contexts `01100`, `11000`, `11001`, `11100`. Each contains `1100`. Consequently
\[
F(Gy)=y\quad\text{for all }y\in X_1.
\]
The sixteen four-bit contexts for \(G\) likewise show that every \(A\)-defect moves right by one bond and every \(B\)-defect moves left by one bond, with deletion possible only in the pattern `1100`. Specifically the four-bit input contexts giving output \(A\) are `1101`, `1110`, `1111`, and those giving output \(B\) are `0000`, `0100`, `1000`.

For any \(y\in X_{t+1}\), the word `1100` is absent and so all the defects are retained by \(G\). Each consecutive \(A,B\) bond gap decreases by exactly two and each consecutive \(B,A\) bond gap increases by exactly two; gaps between equal-type defects are unchanged. Since the original consecutive \(A,B\) gaps are at least four, no defects cross and defect order is preserved. The new consecutive \(A,B\) gaps are therefore at least \(2(t+1)\). Thus \(Gy\in X_t\). Together with \(F(Gy)=y\), this proves \(X_{t+1}\subseteq F(X_t)\).

**4. Induction, strictness, and shortest obstruction.** Steps 2–3 prove \(F(X_t)=X_{t+1}\) for all \(t\ge0\). Starting with \(X_0=\{0,1\}^{\mathbb Z}\) proves \(Y_t=X_t\) by induction. No word \(W_j\) contains any other \(W_k\) as a contiguous subword: after the initial `11`, all interior symbols alternate until the unique final `00`. Thus the displayed finite list is a minimal forbidden basis, not merely a sufficient presentation. Every finite word avoiding the basis extends to a bilateral point of the subshift: append a left-infinite zero tail and a right-infinite one tail. The new boundary defects can only have the order \(B\) before \(A\), never a new \(A\)-before-\(B\) defect pair. Hence the word-avoidance automata compute the actual bilateral image languages, not just a nonextendible finite-word language. For each \(t\ge0\), the word \(W_t\) occurs in a bilateral configuration with alternating tails and exactly one \(A\)-defect and one later \(B\)-defect; this belongs to \(X_t\), whereas \(W_t\) is forbidden in \(X_{t+1}\). Since the only new forbidden basis word has length \(2t+4\), the shortest difference is exactly that length. Strictness holds at every time.

## Verification
Run `python3 verify.py` in a directory containing that standalone Python 3 standard-library file. The program exhaustively reconstructs both sixteen-case defect tables and the thirty-two-case composite table; checks the pointwise inverse relation on all relevant cyclic configurations through length thirteen; builds exact 1-, 2-, 3-, and 4-step de Bruijn subset automata with respectively 6, 17, 46, and 122 nonempty subset states; proves full finite-state language equivalence to the stated forbidden-word automata at each of those four depths by exhausting their reachable product state graphs; and separately checks all input blocks for selected short output lengths. It additionally reproduces the already-known first- and second-image transfer characteristic polynomials exactly via rational Newton identities; these low-time spectral checks are not claimed as new findings. Expected final output: `VERIFY_OK`. The all-time theorem follows from the local defect identities and the induction, **not** from the first four tested cases.

## Relationship to prior work
The November 2026 forbidden-word entropy framework of Wu and Zhang motivates explicitly computing generating forbidden languages and their effect on spatial entropy; its theorem is about maximal-entropy measures, not about this traffic automaton. The 2015 full-text study by de Oliveira and collaborators investigates process-graph growth for Rule 184, displays the first two time graphs, and analyzes limit behavior, but does not give the all-time minimal forbidden bases, the sharp \(2t+4\) first-loss law, or these exact first/second spatial entropy values. Fukś's 1997 traffic analysis explains annihilating traffic defects and density dynamics, but does not furnish the all-time finite-image language equality proved here. An openly accessible published exact one-step reachability study establishes the \(t=1\) case, including the reflected Rule-226 inverse; this is explicitly prior work and **is not claimed as a new special case**. The contribution is the all-time induction and sharp unbounded new-obstruction clock. The exact second-image forbidden pair and entropy were already obtained in an earlier calculation and are not claimed as new.

## Limitations
The result concerns images of the **bilateral full shift** under synchronous Rule 184 only, not image sets on every fixed finite cyclic ring, finite-word predecessor multiplicities, asynchronous traffic, stochastic traffic, or all elementary automata. Finite-state computations verify low times and the displayed polynomials; they do not replace the proof for arbitrary time. Although the most relevant accessible original texts and searchable published records were compared, unindexed older descriptions of Rule 184 or analyses of traffic-defect annihilation may contain logically equivalent formulations. The result has not undergone independent mathematical review.

## References
- X. Wu and X. Zhang, *Generating Forbidden Words and Measures of Maximal Entropy for Subshifts*, arXiv:2611.03758v1, publicly submitted 2026-11-02, https://arxiv.org/html/2611.03758v1.
- P. P. B. De Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki, and V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, first online 2015-05-06, https://doi.org/10.1002/cplx.21686, especially Section 4.1 and Figures 8–13.
- H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, *Physical Review E* 55 (1997), R2081–R2084, arXiv:comp-gas/9703001, https://arxiv.org/abs/comp-gas/9703001.
- *Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-one-step-reachability-inversion-and-density-spectrum-of-th--5a87e3038c99. The prior one-step claim is about cyclic rings; the shared inverse identity is used here on the bilateral shift.
