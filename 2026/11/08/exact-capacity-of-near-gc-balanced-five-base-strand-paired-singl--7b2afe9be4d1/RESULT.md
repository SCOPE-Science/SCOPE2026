# Exact capacity of near-GC-balanced five-base strand-paired single-deletion codes

## Finding

The maximum number of length-five DNA words obeying simultaneously nearest-to-half GC composition, reverse-complement closure, and correction of one deletion is **\(44\)**. Equivalently, the maximum number of full Watson–Crick strand pairs is **\(22\)**. A concrete optimum appears in `example_code.txt`; the matching upper bound is an exact rational certificate in `certificate.json`, checked by `verify.py`.

## Assumptions and scope

Let \(\Sigma=\{A,C,G,T\}\) and \(w_{GC}(x)=|\{i:x_i\in\{C,G\}\}|\). For \(x=x_1\cdots x_5\), define \(D(x)=\{x_1\cdots x_{i-1}x_{i+1}\cdots x_5:1\le i\le5\}\) (a set; repeated deletion outputs are counted once). Write \(\rho(x)\) for reversing the word then exchanging \(A\leftrightarrow T\) and \(C\leftrightarrow G\). A code \(C\subseteq\Sigma^5\) is admissible if

* \(w_{GC}(x)\in\{2,3\}\) for every \(x\in C\); these are exactly the two closest possible GC counts to half of an odd length of five;
* \(\rho(C)=C\), treating both oriented strands as codewords; and
* \(D(x)\cap D(y)=\varnothing\) for every **distinct** \(x,y\in C\).

Thus a receiver who knows the length is four after exactly one deletion uniquely identifies the original oriented five-base word. No substitution, strand reversal of the read, or biochemical constraint is assumed. The last condition is equivalent to longest common subsequence length at most three for distinct five-base codewords.

## Proof

Because no nucleotide is self-complementary, \(\rho\) has no fixed points on odd-length words. There are \(2\binom{5}{2}2^5=640\) words with GC count two or three; they form \(320\) reverse-complement pairs. Among these, exactly \(260\) pairs \(\{x,\rho(x)\}\) have disjoint deletion sets for their two strands. The checker independently generates these pairs directly from definitions, using no precomputed graph data.

Construct a graph \(G\) on those \(260\) pairs: two vertices are adjacent precisely when some single-deletion output of a strand in the first pair equals one from a strand in the second pair. The generated graph contains \(4948\) edges. Every admissible code corresponds bijectively to an independent vertex set of \(G\), and its size is twice that independent set's cardinality.

For an exact upper bound, `certificate.json` contains four rational clique-cover dual certificates at the leaves of a complete binary branch tree, plus the cliques themselves. At each internal node the branch is over whether a specified vertex is selected. A selected vertex excludes all its graph neighbors; an omitted vertex is also unavailable. For each feasible leaf the certificate lists nonnegative rational weights on cliques of the residual graph. Every surviving vertex receives total weight at least one. Since an independent set meets each clique at most once, its remaining cardinality is at most the total weight. Adding the already selected vertices gives the verified upper bounds \(36880/1623\), \(436/19\), \(47255/2068\), and \(597/26\); all are strictly below \(23\). The four branches exhaust every independent set, and therefore \(\alpha(G)\le22\).

The \(22\) pair lines in `example_code.txt` specify \(44\) different words. The verifier checks their compositions, pairing and **all pairwise disjoint deletion shadows**; exactly \(166\) different length-four outputs occur. Hence \(\alpha(G)\ge22\). Consequently the maximum admissible code size is \(2\alpha(G)=44\).

## Verification

Run `python3 verify.py` from the directory containing `verify.py`, `certificate.json`, and `example_code.txt`. The checker uses only Python's standard library and exact `fractions.Fraction` arithmetic. It rebuilds the candidate list and conflict graph from their definitions, validates each listed clique, validates every branch and every rational coverage inequality, and verifies the lower witness by direct deletion-output comparison. It prints `EXACT_CERTIFICATE_OK` upon success. The proof is a finite exhaustive certificate, rather than a heuristic search or an appeal to solver status.

## Relationship to prior work

D'yachkov's *Lectures on DNA Codes* (arXiv:1401.7492v1, first posted 2014-01-29), particularly §§2–4 and Examples 3.2–3.3, formulates reverse-complement-invariant deletion-similarity codes and gives length-four examples and general asymptotic bounds; Remark 3.2 expressly notes the lack of higher-length generalization of the illustrated exact short-code optima. Bennenni–Guenda–Gulliver, *Greedy Construction of DNA Codes and New Bounds* (arXiv:1505.06262v1, 2015-05-23), §§3–4, studies GC constraints, reverse complements, edit-metric codes and general bounds, but does not give this length-five nearest-balance **single-deletion** capacity. The 2009 Jing Sun thesis, *Bounds on Edit Metric Codes with Combinatorial DNA Constraints* (Brock University, handle 10464/2938), is highly relevant: its abstract reports small-parameter tables and fixed-GC and reverse-complement constraints. The accessible abstract does not permit a decisive examination of its tables, and its full text remains an explicit historical-priority risk.

This theorem makes a **specific exact finite capacity** claim, not a general construction, new channel definition, or claim that earlier authors did not study related parameters. A fixed-GC edit-metric table is not automatically an equality for the two-layer GC restriction and one-deletion-only channel used here; nevertheless its uninspected results could potentially constrain novelty.

## Limitations

Only length five, GC counts two or three, full reverse-complement **closure**, and the exact one-deletion channel are covered. Codebooks for unequal GC ranges, repeated deletions, additional substitution errors, and chemical performance are not addressed. The result is based on a rigorously replayable finite graph certificate and has no independent external scientific audit. A related dissertation's full text was not accessible for historical comparison.

## References

1. A. G. D'yachkov, *Lectures on DNA Codes*, arXiv:1401.7492v1 (2014-01-29), https://arxiv.org/abs/1401.7492.
2. N. Bennenni, K. Guenda, T. A. Gulliver, *Greedy Construction of DNA Codes and New Bounds*, arXiv:1505.06262v1 (2015-05-23), https://arxiv.org/abs/1505.06262.
3. J. Sun, *Bounds on Edit Metric Codes with Combinatorial DNA Constraints*, master's thesis, Brock University (2009), https://hdl.handle.net/10464/2938. (Accessible abstract; full text not inspected.)
