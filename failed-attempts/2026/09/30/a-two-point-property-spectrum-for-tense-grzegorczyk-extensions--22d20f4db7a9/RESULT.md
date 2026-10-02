# A two-point property spectrum for tense Grzegorczyk extensions
## Finding
Fix the deterministic two-register Minsky machine \(\mathcal M\) and start configuration \(c_0\) used by Chen and Takahashi. Let \(\mathcal R\) be the set of configurations reachable from \(c_0\), and let \(L(c)\) be their computably constructed finitely axiomatized extension of \(\mathsf{Grz}_t\) associated with a configuration \(c\).

Consider, in this order, the seven properties
\[
\text{tabularity},\quad \text{local tabularity},\quad \text{FMP},\quad \text{decidability},\quad \text{elementarity},\quad \text{canonicity},\quad \text{Kripke completeness}.
\]
Their truth-value vector on \(L(c)\) takes only the two extreme values:
\[
c\in\mathcal R\Longleftrightarrow (1,1,1,1,1,1,1),
\]
\[
c\notin\mathcal R\Longleftrightarrow (0,0,0,0,0,0,0).
\]
Thus all seven properties are equivalent when restricted to this single computable family, even though they are distinct properties of tense logics in general.

A useful strengthening is a Boolean closure statement. Let \(B:\{0,1\}^7\to\{0,1\}\) be any fixed Boolean function satisfying
\[
B(1,1,1,1,1,1,1)\neq B(0,0,0,0,0,0,0).
\]
Then deciding the property obtained by applying \(B\) to the seven truth values is undecidable even under the promise that the input belongs to the family \(\{L(c):c\text{ a configuration of }\mathcal M\}\).

Equivalently, there is no algorithm for the following promised distinction on this family: either the input is the fixed tabular logic
\[
T=\mathsf{Grz}_t\oplus\{\mathsf{bd}_2,\mathsf{bw}_2,\mathsf{bw}^{\partial}_5,\mathsf{br}_7\},
\]
or the input logic is simultaneously Kripke-incomplete and undecidable; determine which case holds.

## Assumptions and scope
The logic \(\mathsf{Grz}_t\) is the tense Grzegorczyk logic from the cited paper. The family \(L(c)\) is exactly the finite-axiom construction in its Definition 0.4.31, built from the fixed deterministic Minsky machine and fixed initial configuration whose reachability set \(\mathcal R\) is undecidable.

The seven properties are interpreted exactly as in the source. The finite model property is abbreviated FMP. The Boolean statement concerns a fixed Boolean function \(B\); it does not assert that arbitrary semantic properties are effectively reducible to these seven.

The result is a statement about the source's particular reduction family. It does not assert that the seven properties are globally equivalent throughout \(\mathop{\mathsf{NExt}}\mathsf{Grz}_t\).

## Proof
Define
\[
T=\mathsf{Grz}_t\oplus\{\mathsf{bd}_2,\mathsf{bw}_2,\mathsf{bw}^{\partial}_5,\mathsf{br}_7\}.
\]
Chen and Takahashi prove that the map \(c\mapsto L(c)\) is computable and establish two cases.

If \(c\in\mathcal R\), their Lemma 0.4.32 gives
\[
L(c)=T.
\]
Their Theorem 0.2.4 makes \(T\) tabular, and the proof of their Corollary 0.4.2 explicitly observes that \(T\) consequently has all seven properties listed above. Hence the property vector is \((1,1,1,1,1,1,1)\).

If \(c\notin\mathcal R\), their Lemma 0.4.34 proves that \(L(c)\) is Kripke-incomplete, and their Lemma 0.4.35 proves that \(L(c)\) is undecidable. The proof of Corollary 0.4.2 also records that each of tabularity, local tabularity, the FMP, elementarity, canonicity, and Kripke completeness implies Kripke completeness, while the decidability property implies decidability. Therefore none of the seven properties can hold for such \(L(c)\), so its vector is \((0,0,0,0,0,0,0)\).

This proves the two-point spectrum.

Now fix a Boolean function \(B\) with different values on the two vectors. If
\[
B(1,1,1,1,1,1,1)=1\quad\text{and}\quad B(0,0,0,0,0,0,0)=0,
\]
then \(B\) holds of \(L(c)\) exactly when \(c\in\mathcal R\). If the two displayed Boolean values are reversed, then \(B\) holds exactly when \(c\notin\mathcal R\). In either case, a decision procedure for \(B\) on the promised family would decide \(\mathcal R\) or its complement, and therefore would decide \(\mathcal R\), contradicting its undecidability.

Finally, the promised fixed-logic-versus-bad-logic distinction is the special case obtained directly from the two source lemmas: reachable configurations produce exactly \(T\), whereas non-reachable configurations produce logics that are both Kripke-incomplete and undecidable.

## Verification
The argument was reconstructed directly from the reduction, not inferred from the paper's list of seven undecidable properties. The reachable direction uses the exact identity \(L(c)=T\). The non-reachable direction uses both negative lemmas simultaneously, which is essential for forcing every coordinate of the seven-bit vector to zero.

The Boolean closure was checked by the two possible endpoint orientations of \(B\). No assumption is made about the behavior of \(B\) on the other \(126\) seven-bit vectors, because those vectors never occur on this family.

The conclusion was also compared with the authors' earlier transitive-tense reduction. That earlier construction has an analogous hard-core mechanism over \(\mathsf{K4}_t\), but it does not subsume the present statement inside the stronger base logic \(\mathsf{Grz}_t\).

## Relationship to prior work
Chen and Takahashi state separate undecidability results for tabularity, local tabularity, the FMP, decidability, elementarity, canonicity, and Kripke completeness in extensions of \(\mathsf{Grz}_t\). Their detailed proof uses one common reduction \(c\mapsto L(c)\): the reachable case collapses to one fixed tabular logic, and the non-reachable case is simultaneously Kripke-incomplete and undecidable.

The present result extracts the joint consequence of those proof ingredients: the seven properties do not merely have separate undecidability reductions; they synchronize perfectly on the same computable family. This yields the promise formulation and the Boolean-separator closure, neither of which is stated as a theorem or corollary in the source.

The authors' June 2026 work on transitive tense logics develops an analogous Minsky-machine method over \(\mathsf{K4}_t\). That work is the closest methodological precedent. The August 2026 source is needed for the stronger \(\mathsf{Grz}_t\) setting, where reflexivity prevents the earlier point-defining technique and necessitates their good-valuation construction.

## Limitations
This is a proof-architecture extraction from a recent undecidability construction, not a new simulation of Minsky machines. Its originality is the synchronized two-point spectrum, the resulting promise problem, and the Boolean-separator closure.

The result gives no separation among the seven properties: on this family they are intentionally indistinguishable. Any example separating two of them inside \(\mathop{\mathsf{NExt}}\mathsf{Grz}_t\) must therefore lie outside this reduction family.

The source assumes only that \(\mathcal R\) is undecidable. No stronger arithmetical-hierarchy completeness claim is made here.

## References
Qian Chen and Tenyo Takahashi, “Most properties are undecidable even in \(\mathop{\mathsf{NExt}}\mathsf{Grz}_t\),” arXiv:2608.30816, first public version 2026-08-31.

Qian Chen and Tenyo Takahashi, “Most Properties are Undecidable for Transitive Tense Logics,” Advances in Modal Logic 2026, EPTCS 447 (2026), 189–202, DOI 10.4204/EPTCS.447.11.

Alexander Chagrov and Michael Zakharyaschev, Modal Logic, Oxford Logic Guides 35, Oxford University Press, 1997.
