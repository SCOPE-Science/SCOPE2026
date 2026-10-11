# Constant-depth finite-frame validity barrier for elementary modal logics
## Finding

Let \(L\) be a finitely axiomatizable elementary unimodal logic. Encode an \(n\)-point Kripke frame \(F=([n],R)\) by its \(n^2\) adjacency bits. Then the finite-frame validity problem
\[
\operatorname{Val}_n(L)=\{R\subseteq[n]^2:([n],R)\models L\}
\]
is decidable by a family of unbounded-fan-in Boolean circuits of constant depth and polynomial size. Equivalently, under this canonical dense encoding,
\[
\operatorname{Val}_{\mathrm{fin}}(L)\in\mathsf{AC}^0.
\]

Hence any finitely axiomatizable modal logic whose finite-frame validity language is outside \(\mathsf{AC}^0\) is non-elementary. In particular, an \(\mathsf{AC}^0\)-many-one reduction from parity to finite-frame validity yields an unconditional non-elementarity proof, using the classical lower bound that parity is not in \(\mathsf{AC}^0\).

## Assumptions and scope

The logic is ordinary unimodal propositional modal logic and is finitely axiomatizable. “Elementary” means that the class of all Kripke frames validating the logic is definable by a first-order theory in the language with one binary relation symbol. The circuit statement uses the standard labeled adjacency-matrix encoding: the universe is \([n]\), and the input bit indexed by \((i,j)\) records whether \(R(i,j)\) holds.

The claim is representation-sensitive. It does not assert the same circuit bound for arbitrary compressed or sparse encodings of frames. It also does not claim that every finitely axiomatizable modal logic has an \(\mathsf{AC}^0\) finite-validity problem; elementarity is the hypothesis that forces the bound.

## Proof

Takahashi proves the following finite reduction. If \(L\) is finitely axiomatizable and elementary, then there is a *single fixed first-order sentence* \(\alpha\) in the frame language such that, for every finite Kripke frame \(F\),
\[
F\models L\quad\Longleftrightarrow\quad F\models\alpha.
\]
The point is stronger than merely having a first-order theory: finite axiomatizability of \(L\), compactness, and the elementary-frame hypothesis yield one finite first-order description that agrees with the validating frames on all finite structures.

Now fix such an \(\alpha\). First-order model checking for one fixed sentence on a labeled finite relational structure is computable by constant-depth polynomial-size circuits. The direct construction is elementary. For every assignment to the finitely many variables occurring in \(\alpha\), atomic formulas are either input bits \(R(i,j)\) or hardwired equality bits. Boolean connectives become constant-fan-in gates, while a quantifier becomes one unbounded OR or AND over the \(n\) possible values of its variable. Because \(\alpha\) is fixed, its quantifier nesting and number of variables are constants independent of \(n\). Unrolling the syntax therefore gives constant depth and polynomial size. More quantitatively, if \(\alpha\) has quantifier rank \(q\) and uses at most \(w\) variables, the standard construction has depth \(O(q+1)\) and size \(O(n^w)\).

Thus the adjacency-matrix language of finite frames satisfying \(\alpha\), and hence the finite-frame validity language of \(L\), is in nonuniform \(\mathsf{AC}^0\).

The contrapositive is immediate: if the finite-frame validity language is not in \(\mathsf{AC}^0\), then no such fixed first-order \(\alpha\) exists, so \(L\) cannot be elementary under Takahashi's finite reduction. If parity reduces to the validity language by an \(\mathsf{AC}^0\) many-one reduction and the validity language were itself in \(\mathsf{AC}^0\), closure of \(\mathsf{AC}^0\) under composition would put parity in \(\mathsf{AC}^0\), contradicting the classical constant-depth lower bound.

## Verification

The argument was checked at both interfaces.

First, the modal-to-first-order step was compared against Takahashi's actual finite-reduction lemma and the subsequent polynomial-time theorem. The lemma supplies one first-order sentence whose finite models are exactly the finite validating frames of \(L\); the later polynomial-time statement evaluates that same fixed sentence by brute force.

Second, the first-order-to-circuit step was reconstructed directly from the syntax of a fixed first-order sentence. Quantifiers expand to unbounded AND/OR layers and atoms read adjacency bits. No complexity-theoretic assumption such as \(\mathsf P\ne\mathsf{NP}\) enters. The only lower-bound input in the parity corollary is the unconditional theorem that parity is not in \(\mathsf{AC}^0\).

The result concerns data complexity for a fixed sentence, not combined complexity in which the first-order sentence is also part of the input.

## Relationship to prior work

Takahashi's 2026 paper proves that finite-frame validity is in polynomial time whenever a finitely axiomatizable modal logic is elementary, and uses this to obtain conditional non-elementarity results from coNP-hardness [1]. The proof passes through a stronger intermediate statement: on finite frames, validation by the logic is exactly satisfaction of one fixed first-order sentence. Combining that intermediate statement with the standard descriptive-complexity translation from fixed first-order sentences to constant-depth circuits sharpens the upper bound from polynomial time to \(\mathsf{AC}^0\).

The first-order-to-\(\mathsf{AC}^0\) translation is standard; Rossman's exposition gives the quantitative dependence on quantifier rank and variable width for fixed first-order model checking [2]. The new point is the modal consequence: elementary finite axiomatizability forces *constant-depth* finite-frame validity, yielding circuit lower bounds as unconditional obstructions to elementarity.

This criterion is different from a random-frame zero-one-law obstruction. A zero-one argument rules out first-order definability from asymptotic probabilities, whereas the present criterion rules it out from constant-depth circuit complexity. Neither test requires the modal logic itself to have a difficult theoremhood problem.

## Limitations

The theorem uses the canonical adjacency-matrix encoding of labeled finite frames. A change to a compressed representation can change circuit complexity and is outside the claim. The theorem is an upper-bound obstruction: it does not by itself provide an \(\mathsf{AC}^0\) lower bound for any particular modal logic. To apply the parity corollary one must separately construct an \(\mathsf{AC}^0\) reduction.

The originality search found no publication explicitly stating this modal \(\mathsf{AC}^0\) strengthening. Because it combines Takahashi's finite first-order reduction with a standard descriptive-complexity fact, an equivalent observation could exist as folklore or in unindexed notes.

## References

[1] Tenyo Takahashi, “Non-elementary modal logics, assuming \(\mathsf P\ne\mathsf{NP}\),” arXiv:2609.10872, first version September 9, 2026.

[2] Benjamin Rossman, “An improved homomorphism preservation theorem from lower bounds in circuit complexity,” *ACM SIGLOG News* 3(4) (2016), 33–46. DOI:10.1145/3026744.3026746.

[3] Johan Håstad, “Almost optimal lower bounds for small depth circuits,” *Proceedings of STOC 1986*, 6–20.
