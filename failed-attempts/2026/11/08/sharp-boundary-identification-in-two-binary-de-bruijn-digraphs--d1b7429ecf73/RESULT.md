# Sharp boundary identification in two binary de Bruijn digraphs

## Finding

Let \(\vec B(2,n)\) be the directed binary de Bruijn graph on the indexed words \(\{0,1\}^n\), with arcs from \(x_1\cdots x_n\) to \(x_2\cdots x_n a\), for each \(a\in\{0,1\}\). For a nonnegative integer \(t\), a radius-\(t\) identifying code is a set \(S\) of vertices such that the **closed incoming-ball signatures**
\[
 I_{t,S}(v)=S\cap\{u:\text{there is a directed path of length at most }t\text{ from }u\text{ to }v\}
\]
are nonempty and pairwise different as \(v\) ranges over all vertices. Write \(\gamma_t(\vec B(2,n))\) for the minimum cardinality of such a set.

The following two exact boundary values hold:
\[
 \boxed{\gamma_4(\vec B(2,7))=64,\qquad \gamma_5(\vec B(2,9))=256.}
\]
Thus, at radii four and five, the general prefix-class lower bound is attained even at the exceptional length boundary \(n=2t-1\). This is a **two-parameter finite statement**, not a claim for all radii.

## Assumptions and scope

Every graph vertex is an indexed binary word; a loop is permitted, and closed balls include their centers. Directed distances use paths ending at the observed vertex, not outgoing paths from the observed vertex. The alphabet is exactly binary, with no additional symmetry quotient or adversarial sensor failure. The asserted pairs are precisely \((n,t)=(7,4)\) and \((9,5)\).

## Proof

**Universal lower bound.** For every binary prefix \(p\) of length \(n-1\), consider vertices \(p0\) and \(p1\). For every \(k\ge1\), their sets of directed \(k\)-step predecessors coincide, since both vertices have the same first \(n-k\) symbols. Consequently their closed radius-\(t\) incoming balls have the form \(A_p\cup\{p0\}\) and \(A_p\cup\{p1\}\) for a common set \(A_p\). If an identifying code contained neither \(p0\) nor \(p1\), the corresponding signatures would be equal. Thus at least one word must be selected from each of the \(2^{n-1}\) disjoint two-element prefix classes, so
\[
 |S|\ge 2^{n-1}.
\]
This argument makes no assumption of uniform ball sizes or independence of the signatures.

**Explicit attaining codes.** The self-contained `witnesses.tsv` stores two positive integers \(F_n\) in hexadecimal, with the row fields `n t hex`. For each row, define
\[
 S_n=\left\{\,2p+\left(\left\lfloor F_n/2^p\right\rfloor\bmod2\right):0\le p<2^{n-1}\,\right\},
\]
where \(0\le x<2^n\) represents its usual length-\(n\) zero-padded binary word. Hence exactly one of the words \(2p\) and \(2p+1\) is selected for each \(p\); in particular \(|S_7|=64\) and \(|S_9|=256\). The hexadecimal literals are the full explicit constructive certificates, not hashes or pseudorandom seeds.

To check all signatures without any graph optimization package, for each vertex number \(v\) calculate the integer set
\[
 B^-_t(v)=\{v\}\cup\bigcup_{k=1}^t\left\{\;a\,2^{n-k}+\left\lfloor v/2^k\right\rfloor:0\le a<2^k\;\right\}.
\]
Indeed, a length-\(k\) path ending at \(v\) has exactly \(k\) free leading symbols in its initial word, followed by the length-\((n-k)\) prefix of \(v\). For each of the two rows, the supplied `check_formula.py` exhausts all \(2^n\) vertices, forms the intersection \(B^-_t(v)\cap S_n\), and asserts that all these intersections are nonempty and mutually distinct. The checks return exactly 128 distinct signatures for the 128 vertices of \(\vec B(2,7)\), and 512 distinct signatures for the 512 vertices of \(\vec B(2,9)\). Therefore the two explicit codes achieve the lower bound.

A separate `check_graph.cpp` constructs the directed adjacency lists directly from the shift-and-append edges, performs reverse breadth-first search of depth \(t\) at each vertex, and checks the signatures against the same literal codeword witnesses. This independently verifies the critical in-ball formula by computing balls from the graph rather than from the formula.

Together, the lower bound and two finite constructive checks prove the displayed equalities. Every verification loop has a concrete finite bound; no evidence from the finite checks is extrapolated to other radii.

## Verification

From the directory containing the three accompanying files `witnesses.tsv`, `check_formula.py`, and `check_graph.cpp`, run

```sh
python3 check_formula.py
g++ -std=c++17 -O2 -Wall -Wextra check_graph.cpp -o check_graph
./check_graph
```

The two verifier outputs must report `FORMULA_OK` and `GRAPH_BFS_OK` for both \((7,4)\) and \((9,5)\). The source and data files are embedded in the same deliverable as this document. The C++ program uses only standard-library facilities. Both methods check exactly one selected word per prefix class, coverage, and pairwise separation of all vertex signatures. Replacing either hexadecimal witness invalidates the theorem unless the checks are repeated.

## Relationship to prior work

Boutin, Horan Goliber, and Pelto [1], initially publicly posted December 18, 2014, establish the general \((d-1)d^{n-1}\) lower bound and construct size-optimal codes when \(n\ge2t\). Their Theorem 3.9 handles the boundary \(n=2t-1\) with a larger construction and explicitly leaves the minimum-size problem open there. That paper also records the previously known smaller binary radius-two boundary exception, which is not part of this finding. For the two pairs considered here, the boundary construction from Theorem 3.9 has respectively \(80\) and \(288\) vertices, whereas the explicit witnesses have \(64\) and \(256\); the reductions are \(16\) and \(32\) sensors. The present result supplies optimal explicit codes at these two radii without asserting a new lower-bound mechanism.

Horan [2] studies **undirected** de Bruijn graphs; that observation model is not equivalent to the directed incoming-ball definition above. The new claims concern neither covering codes under Hamming distance nor non-overlapping word codes.

## Limitations

The equalities cover only the two pairs \((n,t)=(7,4)\) and \((9,5)\), only binary alphabets, and only noiseless directed incoming-ball identification. They do not imply that the bound is achievable for every \(t\ge3\), classify all optimum codebooks, or settle nonbinary boundary cases. The computations are finite exhaustive proof checks, not a claim of independent external certification; publication priority outside the inspected sources requires further independent review.

## References

[1] D. Boutin, V. Horan Goliber, M. Pelto, *Identifying Codes on Directed De Bruijn Graphs*, arXiv:1412.5842, first posted 2014-12-18; full preprint, especially Definition 3.4, Theorems 3.5 and 3.9. https://arxiv.org/abs/1412.5842

[2] V. Horan, *On the Existence of \(t\)-Identifying Codes in Undirected De Bruijn Graphs*, arXiv:1508.00403, first posted 2015-08-03. https://arxiv.org/abs/1508.00403
