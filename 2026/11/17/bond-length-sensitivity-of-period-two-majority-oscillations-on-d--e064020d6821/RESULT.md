# Bond-length sensitivity of period-two majority oscillations on defective squared cycles

## Finding

For every integer \(n\ge7\), let \(C_n^2\) have vertex set \(\mathbb Z/n\mathbb Z\), with an edge between two distinct vertices precisely when their cyclic distance is one or two. For \(d\in\{1,2\}\), remove only the undirected edge \(\{0,d\}\), obtaining \(G_{n,d}\). Run synchronous binary majority dynamics with ties resolved by retaining the vertex's existing bit. Let \(\mathcal C_{n,d}\) denote the number of *distinct, unordered temporal orbits* of least period two. Then

\[
\boxed{\mathcal C_{n,1}=2\mathbf 1_{4\mid n}+2\mathbf 1_{6\mid n}},
\qquad
\boxed{\mathcal C_{n,2}=2\mathbf 1_{4\mid n}+2\mathbf 1_{6\mid n}+\mathbf 1_{n\equiv3\pmod4}}.
\]

In particular, deleting a distance-two edge creates a primitive two-cycle on every ring of length congruent to three modulo four, whereas deleting a nearest-neighbor edge does not. The number of primitive two-cycles never exceeds four for either deletion type, independently of ring length.

## Assumptions and scope

All graphs are finite, simple and labelled, with vertex set \(\{0,\ldots,n-1\}\); no quotient by spatial rotations or reflections is taken. When counting a temporal orbit \(\{x,y\}\), configurations \(x\ne y\) and \(y\ne x\) count as the *same* temporal two-cycle.

The update \(F_{n,d}\) is defined for a configuration \(x\in\{0,1\}^n\) and each vertex \(i\) by

\[
F_{n,d}(x)_i=
\begin{cases}
1,&2\sum_{j\in N(i)}x_j>|N(i)|,\\
0,&2\sum_{j\in N(i)}x_j<|N(i)|,\\
x_i,&2\sum_{j\in N(i)}x_j=|N(i)|.
\end{cases}
\]

Here \(N(i)\) is the open neighborhood in \(G_{n,d}\). The two endpoints of the removed edge have degree three and every other vertex has degree four. The restriction \(n\ge7\) avoids small-ring neighborhood coincidences; nothing is claimed about smaller sizes. No convergence-time bound or attraction-basin count is claimed.

## Proof

**1. Closed-walk encoding.** Given two configurations \(x,y\), let the four-symbol letter \(p_i=(x_i,y_i)\in\{0,1\}^2\). A temporal state has period dividing two precisely if simultaneously

\[y=F_{n,d}(x),\qquad x=F_{n,d}(y).\]

Encode a four-letter window \((p_{i-2},p_{i-1},p_i,p_{i+1})\) as one of \(4^4=256\) directed-graph states. There is an edge to its one-site shift \((p_{i-1},p_i,p_{i+1},p_{i+2})\) if both update equations hold at the center \(i\), tested on the five-letter window. Denote the \(256\)-square zero-one adjacency matrices for an ordinary vertex by \(A\), and for endpoints \(0,d\) of the missing bond by \(L_d,R_d\), respectively. At the endpoints the neighbor offset \(+d\) or \(-d\) is omitted; elsewhere the offsets are \(-2,-1,+1,+2\). This explicitly defines every matrix entry, including tie behavior.

For a cyclic word of length \(n\ge7\), the successive overlapping four-letter windows form a unique closed walk, and conversely. Consequently, writing \(P_{n,d}\) for the number of labelled configurations satisfying \(F_{n,d}^2(x)=x\),

\[
P_{n,1}=\operatorname{tr}(L_1R_1A^{n-2}),\qquad
P_{n,2}=\operatorname{tr}(L_2AR_2A^{n-3}).
\]

There are no orbit multiplicities hidden in these traces: fixing the vertex labels fixes the starting window, so each periodic configuration gives exactly one counted closed walk.

**2. Fixed-state subtraction.** Restrict all letter states to diagonal pairs \((0,0)\) and \((1,1)\). The same construction has \(2^4=16\) states and matrices \(A_f,L_{d,f},R_{d,f}\). Its trace \(H_{n,d}\) counts exactly the fixed configurations \(F_{n,d}(x)=x\). Thus

\[
D_{n,d}:=P_{n,d}-H_{n,d}=2\mathcal C_{n,d}.
\]

**3. Finite certificate extended to every size.** The standalone script `code/transfer_certificate.py` constructs each of the six relevant local adjacency matrices directly from all possible five-letter windows, for alphabets of four and two symbols. Its arithmetic is exact, using ordinary unbounded Python integers. For every \(n\) from \(7\) through \(290\), it calculates both traces, verifies the two claimed formulas, and verifies

\[D_{n+12,d}=D_{n,d}\qquad (7\le n\le278,\ d\in\{1,2\}).\]

These are **272 consecutive equalities for each defect type**, not a conjecture extrapolated from a few examples. For each fixed \(d\), the sequence \(P_{n,d}\) obeys the characteristic-polynomial recurrence of its constant \(256\)-state matrix \(A\) by Cayley–Hamilton, while \(H_{n,d}\) obeys that of the constant \(16\)-state matrix \(A_f\). Their difference \(D_{n,d}\) is therefore annihilated by the product recurrence, of order at most \(272\). The shifted difference \(D_{n+12,d}-D_{n,d}\) obeys this same product recurrence. The 272 verified consecutive zeros force it to vanish for **every** \(n\ge7\). Its twelve initial values, also computed and checked in the script, are exactly the residues specified by the boxed formulas. Period twelve and these initial values prove the assertions for all sizes.

**4. Distinguishing witness.** For \(n=7,d=2\), the strings \(0100110\) and \(1011001\), indexed left to right by vertices \(0,\ldots,6\), update to each other. They form the sole primitive two-cycle, whereas the nearest-neighbor deletion has none. The analogous size-eleven orbit has strings \(01001100110\) and \(10110011001\).

## Verification

Run with Python 3 and the standard library only:

```
python3 code/transfer_certificate.py
python3 code/direct_check.py
```

The first program constructs exact integer matrices afresh, checks all \(284\) sizes \(7\le n\le290\) for each of two deleted-bond types, and applies the stated Cayley–Hamilton finite-test argument. Its captured output is `evidence/transfer_run.txt`. The second program instead constructs the labelled graphs from vertex neighborhoods, independently updates every binary state twice and counts temporal orbits for \(7\le n\le16\). Its captured output is `evidence/direct_run.txt`; it checks \(261888\) labelled initial configurations across both defect types. The second program is a finite cross-check; it is not used as an infinite proof.

## Relationship to prior work

Goles and Olivos (1980, 1981) established the eventual period-at-most-two property for symmetric threshold networks. That does not enumerate the primitive two-cycles of these graphs. Tosic and Agha (2004) analyze synchronous and sequential one-dimensional threshold cellular automata, notably the uniform radius-one setting, but do not supply the two bond-deletion formulas. Benjamini et al. (first posted 2014-05-11) study convergence and disagreement in majority dynamics on general and random graphs, not exact one-edge-defect periodic-orbit enumerations.

A particularly close and stronger **uniform-ring** result is Nakar and Ron (first posted 2022-05-18), whose Section 1.4 explicitly classifies the periodic configurations of the radius-two majority cellular automaton on an intact cyclic ring: alternating patterns of spatial periods two, four and six, together with fixed runs of length at least three. Its intact-ring classification is prior work, not a new claim here. Removing an edge makes two local update neighborhoods different, so those uniform-ring classifications cannot simply be applied to the defective graphs. The new statement is the exact, distinct response to the two geometrically different single-bond deletions. The related count on a singly chorded **ordinary** ring concerns a different graph and local degree, and does not imply the present formulas.

## Limitations

The proof is computer-assisted via exact finite matrix arithmetic plus an elementary characteristic-polynomial recurrence; no independent audit has been performed. The source comparisons establish no known covering claim in the material inspected, but cannot exclude older results not found by targeted searches. The full historical Goles–Olivos articles were not read; their accessible published abstracts establish only general periodicity. The calculation is about configurations **already** on two-cycles, not their basins or transient entry times. Neither deletion-case formula should be inferred for multiple missing edges or for different tie rules.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1.
2. E. Goles and J. Olivos, *Comportement périodique des fonctions à seuil binaires et applications*, Discrete Applied Mathematics **3** (1981), 93–105, DOI: 10.1016/0166-218X(81)90034-2.
3. P. T. Tosic and G. Agha, *Characterizing Configuration Spaces of Simple Threshold Cellular Automata*, ACRI 2004, Lecture Notes in Computer Science **3305**, 861–870, DOI: 10.1007/978-3-540-30479-1_89, author PDF: https://osl.cs.illinois.edu/media/papers/tosic-2004-acri-characterizing_configuration_spaces_of_simple_threshold_cellular_automata.pdf.
4. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, preprint first posted May 11, 2014, https://arxiv.org/abs/1405.2486.
5. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, preprint first posted May 18, 2022, https://arxiv.org/abs/2205.08972, especially Theorem 1 and Section 1.4.
