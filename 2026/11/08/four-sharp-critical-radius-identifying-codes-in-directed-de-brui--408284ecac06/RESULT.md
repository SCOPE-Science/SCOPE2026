# Four sharp critical-radius identifying codes in directed de Bruijn graphs

## Finding

Let \(\vec B(q,n)\) be the directed de Bruijn graph whose vertices are all words in \((\mathbb Z/q\mathbb Z)^n\) and whose arcs shift left one position and append one symbol. Let \(\gamma_t(q,n)\) denote the minimum cardinality of a set \(S\) for which the sets \(B_t^-(v)\cap S\), indexed by all vertices \(v\), are nonempty and pairwise distinct. Here \(B_t^-(v)\) includes all vertices with a directed path to \(v\) of length at most \(t\), including length zero.

**Theorem.** For every \((q,t)\in\{(3,3),(4,3),(3,4),(4,4)\}\), at the critical word length \(n=2t-1\),

\[
\gamma_t(q,2t-1)=(q-1)q^{2t-2}.
\]

In order of \((q,t)=(3,3),(4,3),(3,4),(4,4)\), the exact values are \(162,768,1458,12288\), respectively. Each value is attained by the explicit modular-checksum code

\[
S_{q,t}=\left\{x\in(\mathbb Z/q\mathbb Z)^{2t-1}:\sum_{i=t+1}^{2t-1}x_i\not\equiv\sum_{i=1}^{t-1}x_i\pmod q\right\}.
\]

## Assumptions and scope

Words are **labeled**, not identified up to rotation. Alphabet digits are the residues \(0,\ldots,q-1\), with addition modulo \(q\), including for composite \(q=4\). A radius is measured in the direction of the incoming de Bruijn arcs. The four parameter pairs above, and no larger family, are asserted.

## Proof

**Lower bound.** Fix a length-\((n-1)\) word \(w\). The \(q\) vertices \(wa\), for symbols \(a\), have identical incoming balls with the self-vertex removed, in the sense relevant to code intersections when neither of two such vertices belongs to the code: every positive-length predecessor set depends on the common prefix, not on the final symbol. Hence omitting two members of this prefix class would give two equal identifying sets. Every identifying code consequently contains at least \(q-1\) vertices for each of the \(q^{n-1}\) prefix classes, and its size is at least \((q-1)q^{n-1}\).

**Matching size.** For each fixed \((n-1)\)-letter prefix, the checksum congruence defining the complement of \(S_{q,t}\) has exactly one possible final symbol, since the final symbol occurs with coefficient \(+1\). Thus each prefix class contains exactly \(q-1\) code vertices and \(|S_{q,t}|=(q-1)q^{n-1}\).

**Identification.** The remaining assertion is a finite but exhaustive verification, not a random test or an extrapolation. `verify.py` enumerates every word \(v\) for each of the four parameter pairs. At exact positive path length \(r\le t\), every incoming predecessor is uniquely of the form \(zv_1\cdots v_{n-r}\), where \(z\) ranges over **all** \(q^r\) words of length \(r\). Including \(v\) itself and taking the union over \(1\le r\le t\) therefore enumerates the complete closed incoming ball. The program separately computes each ball by iterating the one-step reverse-edge formula \(v\mapsto av_1\cdots v_{n-1}\) and checks that the two constructions agree for every vertex. It intersects every complete ball with the explicit code and checks that all \(q^n\) resulting sets are nonempty and pairwise distinct. These exhaustive finite checks establish that \(S_{q,t}\) is an identifying code in each stated case. The lower bound then proves all four exact optima. The complete deterministic verification procedure and its output are included as `verify.py` and `results.txt`.

## Verification

Run `python3 verify.py` using Python 3 and only its standard library. The program checks all \(243,1024,2187,16384\) vertices of the respective graphs, every predecessor at every radius up to the stated \(t\), every equality between independently constructed balls, the number of selected vertices in each prefix class, and exact uniqueness of all identification signatures. The checked output is recorded in `results.txt`, ending with `VERIFY_OK cases=4`; it contains a canonical SHA-256 fingerprint for the complete sequence of signatures in each case. Hashes document reproducibility, but correctness follows from the exhaustive enumeration and its transparent loops, not from the hashes alone.

## Relationship to prior work

Boutin, Horan Goliber and Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842 (first publicly posted 2014-12-18), prove the general prefix-class lower bound and optimal constructions when \(n\ge2t\). Their Theorem 3.12 supplies a larger construction at \(n=2t-1\), and the following discussion explicitly identifies critical-length optimality as an open problem. The present finite theorem attains the lower bound at four new nonbinary critical-length parameter pairs by a different, elementary modular-checksum construction. The 2015 work on **undirected** de Bruijn identification concerns different graphs and does not imply these directed minima.

## Limitations

The proof covers exactly the four specified pairs. Exhaustive checking of finitely many parameters is not a proof of the same construction for arbitrary alphabet size or arbitrary radius; neither a general theorem nor a classification of all optimal identifying sets is asserted. Priority outside indexed sources, including mathematically equivalent statements under alternative monitoring terminology, cannot be fully excluded. No independent mathematical audit has been performed.

## References

1. D. Boutin, V. Horan Goliber and M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, first posted 2014-12-18, https://arxiv.org/abs/1412.5842 . Especially Definitions 3.3 and 3.7, Theorems 3.8, 3.9 and 3.12, and the discussion after Theorem 3.12.
2. V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403, first posted 2015-08-03, https://arxiv.org/abs/1508.00403 . Undirected comparison only.
