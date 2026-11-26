# Embedding potentialism equals inclusion potentialism on every isomorphism-closed class

## Finding

Let \(\mathcal K\) be any class of \(L\)-structures closed under isomorphism. Form two potentialist systems on exactly the same worlds:

\[
\operatorname{Inc}(\mathcal K): \text{all literal substructure inclusions},
\qquad
\operatorname{Emb}(\mathcal K): \text{all }L\text{-embeddings}.
\]

Then the pointed-world relation

\[
(M,\bar a)\sim(N,\bar b)
\iff
\exists h:M\cong N\text{ with }h(\bar a)=\bar b
\]

is a **bitotal bisimulation**. Therefore the two systems agree on every formula of Adam-Day's infinitary modal language \(L^\Diamond_\infty\), and hence have the same finitary modal theory.

In particular, for every first-order theory \(T\) and every class \(C\) of cardinals, the inclusion and embedding systems restricted to

\[
\{M\models T:|M|\in C\}
\]

are bitotally bisimilar. Exact-cardinality layers \(|M|=\kappa\) are a special case. The conclusion actually needs no theory \(T\): any isomorphism-invariant class of structures works.

## Assumptions and scope

The class \(\mathcal K\) is assumed to contain every structure isomorphic to one of its members. Arrows in \(\operatorname{Inc}(\mathcal K)\) are literal substructure inclusion maps, while arrows in \(\operatorname{Emb}(\mathcal K)\) are arbitrary structure embeddings. Both systems contain identities and compositions.

The conclusion asserted here is an ordinary **bitotal bisimulation**. Adam-Day proves a stronger iso-bisimulation for the full class \(\operatorname{Mod}(T)\), but an arbitrary isomorphism-closed subclass need not come equipped with a globally coherent choice of isomorphism for every related world-pair. No such stronger claim is made here.

## Proof

Relate pointed worlds precisely when some isomorphism carries the distinguished tuple to the distinguished tuple. Bitotality is immediate from identity isomorphisms. The atomic and element back-and-forth clauses are immediate from the witnessing isomorphism and its inverse.

For the modal **forth** clause, suppose \(h:M\cong N\) witnesses \((M,\bar a)\sim(N,h(\bar a))\), and suppose the inclusion system has an arrow \(M\subseteq M'\). In the embedding system use

\[
\rho:N\longrightarrow M',\qquad \rho=\iota\circ h^{-1},
\]

where \(\iota:M\hookrightarrow M'\) is the inclusion. The two target worlds can be related by the identity isomorphism of \(M'\), and \(\rho(h(\bar a))=\bar a\).

For the modal **back** clause, suppose instead that the embedding system has \(\rho:N\to N'\). We build an isomorphic copy \(M'\cong N'\) whose underlying set literally contains \(M\), and whose isomorphism to \(N'\) extends \(\rho\circ h\). Choose a disjoint copy of the complement \(N'\setminus\rho h[M]\) and put

\[
D=M\sqcup\bigl((N'\setminus\rho h[M])\times\{*\}\bigr).
\]

Let \(j:D\to N'\) equal \(\rho h\) on \(M\) and send the tagged complement bijectively to the remaining points of \(N'\). Pull the entire \(L\)-structure of \(N'\) back along \(j\). Then \(j:M'\cong N'\). Because \(j|_M=\rho h\) is an embedding, the old \(M\) is literally a substructure of \(M'\). Because \(\mathcal K\) is isomorphism-closed and \(N'\in\mathcal K\), also \(M'\in\mathcal K\). Thus \(M\subseteq M'\) is an allowed inclusion arrow and the targets are related by \(j\).

These are exactly the back-and-forth clauses for a potentialist bisimulation. Adam-Day's Fundamental Theorem of Bisimulations then transfers every \(L^\Diamond_\infty\)-formula.

## Verification

The proof is a direct structural argument, so it does not depend on finite computation. As a separate exact replay, the bundled verifier exhaustively checks both local constructions for every simple graph of source size at most three and target size at most four, over every source isomorphism and every relevant embedding. It verifies that the pulled-back target contains the old source literally as an induced subgraph, that the transport map is an isomorphism, and that the required commuting equations hold.

Running `python3 artifacts/verify_replete_bisimulation.py` returns:

`VERIFY_OK 149691 exact assertions`

This finite replay checks the construction mechanics; the general theorem follows from the set-theoretic pullback-of-structure argument above, not by extrapolation from the computation.

## Relationship to prior work

Sam Adam-Day proves that for every first-order theory \(T\), the system of all models of \(T\) under substructure inclusions and the system of all models under arbitrary embeddings are bitotally bisimilar, in fact via a stronger iso-bisimulation (Theorem 28 of *Bisimulations of potentialist systems*). The same paper proves invariance of \(L^\Diamond_\infty\) under bisimulation and records that its renaming bisimulation restricts to the subclasses of models of size less than an arbitrary cardinal \(\lambda\) (Lemma 49).

The present observation removes the hypothesis that the world class be all models of a first-order theory, or even elementary at all. Closure under isomorphism alone is enough for ordinary bitotal bisimulation. This immediately supplies exact-cardinality restrictions and arbitrary cardinal spectra, as well as other isomorphism-invariant slices, without a Löwenheim--Skolem argument.

Candidate-specific published-finding corpus searches, exact web searches under “isomorphism-closed”, “embedding potentialism”, “inclusion potentialism”, and “bitotal bisimulation”, plus the current and prior cumulative owned ledgers, found Adam-Day's full-model theorem and its \(<\lambda\) restriction but no equivalent arbitrary-isomorphism-closed-class statement.

## Limitations

The new step is short and may be specialist folklore: it is essentially the observation that an embedding can always be turned into a literal inclusion after replacing its codomain by a suitably renamed isomorphic copy. The originality claim is therefore deliberately limited to the explicit general theorem and its exact-cardinality corollary as not located in the inspected sources.

The theorem requires genuine closure under all isomorphic copies. A subclass given by presentation-dependent conditions on the underlying set can fail this hypothesis. Also, only ordinary bitotal bisimulation is asserted; the stronger globally coherent iso-bisimulation from Adam-Day's full \(\operatorname{Mod}(T)\) theorem is not claimed for arbitrary \(\mathcal K\).

## References

1. Sam Adam-Day, *Bisimulations of potentialist systems*, arXiv:2206.10359, first posted 21 June 2022. Primary MSC 03B45. In particular: Definitions 11--12, Theorem 21, Theorem 28, and Lemma 49.
2. Joel David Hamkins and Wojciech Aleksander Wołoszyn, *Modal model theory*, arXiv:2009.09394; later published in *Notre Dame Journal of Formal Logic*. This supplies the broader model-potentialist setting in which inclusion and embedding semantics are compared.
