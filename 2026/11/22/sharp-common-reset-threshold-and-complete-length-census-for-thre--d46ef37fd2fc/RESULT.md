# Sharp common-reset threshold and complete length census for three binary three-state automata

## Finding

Let each of three complete deterministic semiautomata have the state set \(Q=\{0,1,2\}\) and a common ordered alphabet \(\Sigma=\{0,1\}\). Suppose each is synchronizing. Write \(\rho(A,B,C)\) for the length of a shortest word taking the full state set to a singleton in each component, under the same sequence of letters. Then

\[
\max_{A,B,C}\rho(A,B,C)=7.
\]

Exactly \(549\) of the \(729\) ordered transition-table pairs define synchronizing three-state binary semiautomata. The exact distribution among their \(549^3=165{,}469{,}149\) ordered triples is:

| Shortest common reset length | Number of ordered labeled triples |
|---:|---:|
| 1 | 1,062,153 |
| 2 | 48,991,068 |
| 3 | 66,420,432 |
| 4 | 35,524,872 |
| 5 | 10,653,120 |
| 6 | 2,651,616 |
| 7 | 165,888 |

There are \(28\) distinct signatures of reset behavior through length \(7\) among the \(549\) synchronizing component automata.

## Assumptions and scope

State labels are independent for the three components, while the letters \(0\) and \(1\) are shared. A labeled automaton is specified by two length-three tuples, \((\delta(0,0),\delta(1,0),\delta(2,0))\) and \((\delta(0,1),\delta(1,1),\delta(2,1))\), with each entry in \(Q\). Every such table pair is included; components need not be accessible from a designated initial state and repeated components are allowed. A word resets an automaton if its image of all three states is a singleton. Empty words do not reset a three-state automaton.

For example, choose the three machines, in order, with transitions

| Component | Letter `0` | Letter `1` |
|---|---|---|
| A | (0,0,1) | (0,2,2) |
| B | (0,0,2) | (0,2,1) |
| C | (0,0,2) | (2,0,1) |

The word `0010110` resets all three. No word of length at most \(6\) resets all three simultaneously. In fact, there are exactly six common reset words of length \(7\) for this witness triple.

## Proof

Represent nonempty subsets of \(Q\) by masks \(1,\ldots,7\), with full-state mask \(7\). A letter tuple \(t\in Q^3\) acts on mask \(S\) via

\[
T_t(S)=\{t_i:i\in S\}.
\]

There are exactly \(3^3=27\) possible maps for each letter, hence \(27^2=729\) labeled automata. Their synchronization can be completely decided by the finite subset graph. Its vertices are the seven nonempty subsets of \(Q\) and its two directed edges at each vertex are induced by the two letter transformations. Whenever a singleton is reachable from \(Q\), a simple shortest path has length at most \(6\), so a length-seven zero-reset signature cannot conceal a synchronizing automaton.

For each of the \(729\) table pairs, compute the bit vector \(R_\ell(A)\) of all binary words of length \(\ell\) resetting \(A\), for \(1\le\ell\le7\); bit position is the lexicographically ranked binary word. A reset word can be extended on the right without losing synchronization. Consequently, a triple has a common reset word of length at most \(7\) exactly when at least one of the seven intersections \(R_\ell(A)\cap R_\ell(B)\cap R_\ell(C)\) is nonempty. Its shortest common reset length is the first such \(\ell\).

The exhaustive calculation (reproduced in `triple_catalogue.py`) finds \(549\) machines with nonempty seventh-level signature and \(180\) with none. The seven-component signature tuple takes exactly \(28\) distinct values on the \(549\) synchronizing machines. Because all membership decisions through length seven depend only on this tuple, replacing each machine by its signature and recording its positive multiplicity is an **exact quotient of the entire labeled census**, not a statistical sampling step. Exhaustively intersecting all \(28^3\) ordered signature triples and weighting each by the product of its three multiplicities yields the seven counts displayed above. They sum exactly to \(549^3\), and every signature triple has a nonempty intersection at some length no greater than \(7\), proving the universal upper bound.

For the displayed witness, direct enumeration shows zero common reset words at each of lengths \(1,\ldots,6\), and six at length \(7\). Thus the upper bound is attained. This completes the finite exhaustive proof. A second implementation (`triple_bfs.py`) independently constructs image-set transitions and performs shortest-path breadth-first searches in the three-component subset product for each signature triple. It reproduces the same seven weighted counts, without relying on the bit-vector-intersection decision rule.

## Verification

Run the two standalone Python 3 scripts from the directory containing this document:

```bash
python3 triple_catalogue.py
python3 triple_bfs.py
```

The first produces `catalogue_output.txt`; the second produces `bfs_output.txt` (their exact stdout text is embedded alongside the source programs). The script runs exhaustively over all \(729\) possible binary transition-table pairs and all \(28^3\) ordered signature-class triples. The two implementations use different reset tests (explicit word masks versus direct subset-product BFS). The weighted count sum and the witness are asserted in the code and compared to the recorded outputs.

## Relationship to prior work

Fernau and Rystsov, *Shortest Synchronizing Words on Product Automata* (arXiv:2611.09136, first publicly submitted November 6, 2026), identify product synchronization with intersection of component reset-word languages (Lemma 3.1) and give the general sum/max reset-threshold inequalities (Proposition 3.4). They do not give the sharp three-component binary three-state value \(7\) or this \(549^3\)-triple distribution. Szykuła, *Synchronizing Automata: Open Problems* (arXiv:2608.24245, first publicly submitted August 25, 2026), reviews the single-automaton landscape; it does not determine this simultaneous finite census.

A separate finite pair census established threshold \(6\) and a distribution on \(549^2\) ordered pairs of binary three-state machines. That pair result does not imply the sharp three-component bound or any of the triple counts; the displayed witness needs \(7\) letters despite every component pair being subject to the six-letter guarantee.

## Limitations

The theorem only concerns ordered triples of complete binary semiautomata on exactly three states each, with repeated components allowed. It is a computer-assisted finite proof, not a theorem for arbitrary state counts, tuple sizes, or alphabets. The source programs and independently reproduced outputs provide a reproducible exhaustive certificate; they do not constitute a separate independent scholarly audit. As with other finite-classification claims, unindexed equivalent earlier enumerations remain a possible priority risk.

## References

1. H. Fernau and I. Rystsov, *Shortest Synchronizing Words on Product Automata*, arXiv:2611.09136, first submitted November 6, 2026. https://arxiv.org/abs/2611.09136
2. M. Szykuła, *Synchronizing Automata: Open Problems*, arXiv:2608.24245, first submitted August 25, 2026. https://arxiv.org/abs/2608.24245
