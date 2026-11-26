# Greedy period-doubling attractors occur exactly at \(2^m-1\)
## Finding
Let \(\mathbf{pd}=101110101011\cdots\) be the fixed point of
\[
\tau(1)=10,\qquad \tau(0)=11.
\]
Use the greedy string-attractor rule of Schaeffer and Shallit: start from the empty set, and at each step add the smallest position \(j\) for which the current set fails to attract the prefix \(\mathbf{pd}[0..j]\).

The resulting infinite greedy attractor is exactly
\[
G=\{2^m-1:m\ge0\} = \{0,1,3,7,15,31,\ldots\}.
\]
Consequently, for every prefix length \(N\ge1\),
\[
|G\cap[0,N-1]|=1+\lfloor\log_2 N\rfloor.
\]
For \(N\ge2\), the optimal attractor size is the published constant \(2\). Thus the greedy construction on this linearly recurrent automatic word has an unbounded approximation ratio, asymptotic to \(\frac12\log_2 N\), even though every nontrivial prefix has a two-position optimum.

## Assumptions and scope
A string attractor of a finite word \(w\) is a set of positions such that every nonempty factor of \(w\) has an occurrence crossing at least one selected position. The greedy rule is the exact rule in Definition 19 of Schaeffer and Shallit: after positions have been selected, add the least endpoint \(j\) whose prefix is not attracted.

Positions are zero-based. The theorem concerns this particular greedy rule, not arbitrary greedy heuristics for the minimum-attractor problem.

## Proof
Write
\[
P_m=\tau^m(1),\qquad Q_m=\tau^m(0),
\]
so \(|P_m|=|Q_m|=2^m\). Since
\[
P_{m+1}=P_mQ_m,\qquad Q_{m+1}=P_mP_m,
\]
an induction shows that \(P_m\) and \(Q_m\) agree everywhere except at their last symbol. Let \(H_m\) be \(P_m\) with its final symbol deleted. It follows that
\[
H_{m+1}=P_mH_m.
\]

For \(m\ge0\), put
\[
G_m=\{2^i-1:0\le i\le m\}.
\]
We first prove by induction that \(G_m\) attracts every prefix whose length \(N\) satisfies
\[
2^m\le N\le2^{m+1}-1.
\]
For \(m=0\), the only such prefix has length one and is attracted by \(\{0\}\).

Assume the statement for \(m-1\), and write a prefix in the next range as
\[
P_mR,
\]
where \(R\) is a prefix of \(H_m\). By the induction hypothesis, \(G_{m-1}\) attracts \(H_m\), whose length is \(2^m-1\). Consider any factor occurrence in \(P_mR\). If it crosses position \(2^m-1\), it is attracted by the new point. If it lies wholly in the left copy \(P_m\) and avoids that boundary, it is a factor of \(H_m\), hence has an occurrence crossing \(G_{m-1}\). If it lies wholly in \(R\), the same occurrence appears in the prefix \(H_m\) of \(P_m\), and again has an occurrence crossing \(G_{m-1}\). Thus \(G_m\) attracts the entire interval of prefix lengths.

It remains to show that the next endpoint really forces a new point. We use an occurrence lemma. For every \(r\ge0\), the word \(P_r\) occurs in \(P_{r+2}\) exactly at positions
\[
0,\qquad 2^{r+1},\qquad 3\cdot2^r.
\]
For \(r=0\) this is immediate. For \(r\ge1\), every occurrence of \(P_r\) starts with \(10\). In a morphic image under \(\tau\), no \(10\) begins at an odd position, so every occurrence is aligned with a length-two morphism block. Desubstitution therefore gives a bijection between occurrences of \(P_r=\tau(P_{r-1})\) in \(P_{r+2}=\tau(P_{r+1})\) and occurrences of \(P_{r-1}\) in \(P_{r+1}\); induction doubles the three starting positions.

Now let \(k\ge2\), put \(r=k-2\), and set \(q=2^r\). In
\[
P_k=P_rQ_rP_rP_r,
\]
consider
\[
F_k=\operatorname{last}(P_r)P_r.
\]
The occurrence lemma gives only three possible starts of the \(P_r\) suffix within an occurrence of \(F_k\). The occurrence at position \(0\) has no predecessor. The one at position \(2q\) is preceded by the last symbol of \(Q_r\), which is the complement of the last symbol of \(P_r\). The occurrence at position \(3q\) is preceded by the last symbol of \(P_r\). Hence \(F_k\) occurs uniquely, starting at
\[
3q-1.
\]
This unique occurrence lies strictly to the right of every point of \(G_{k-1}\), whose largest point is \(2q-1\). Therefore \(G_{k-1}\) is not an attractor of \(P_k\). For \(k=1\), the same conclusion follows from the unique final \(0\) in \(P_1=10\).

The attraction interval and the unique escaping factor together show inductively that the greedy rule adds exactly the positions \(2^m-1\), and no others.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The verifier has three independent finite layers. First, it implements the greedy definition directly and obtains additions
\[
0,1,3,7,15,31,63,127,255
\]
through the first \(256\) symbols. Second, it verifies the morphic recurrences and attractor property of the truncated words through ten substitution levels. Third, it checks the exact three-occurrence lemma and the unique escaping factors through independent higher substitution levels.

These finite checks are stress tests. The infinite result follows from the induction and desubstitution argument in the proof above.

## Relationship to prior work
Schaeffer and Shallit introduced the greedy construction used here in Definition 19 and proved a general \(O(A_w\log N)\) upper bound for prefixes when the appearance constant \(A_w\) is finite. Earlier in the same paper they proved that every period-doubling prefix of length at least two has minimum attractor size exactly \(2\), and they gave explicit optimal pairs over ranges of prefix lengths. They did not state the exact greedy set for the period-doubling word.

Banbara, Bannai, Guo, Köppl, Mieno, and Okamoto later completely characterized the smallest attractors of the finite period-doubling words, finding exactly two minimum pairs in each sufficiently high substitution level. Their result concerns globally smallest attractors rather than the prefix-by-prefix greedy process and does not give the set \(\{2^m-1:m\ge0\}\).

The present theorem therefore identifies a sharp separation already inside one classical automatic word: the optimum remains constant while the natural greedy construction from the original paper grows exactly logarithmically.

## Limitations
The theorem is specific to the period-doubling fixed point and to the least-failing-prefix greedy rule of Definition 19. It does not classify greedy attractors for other automatic words or for alternative online heuristics.

The exact greedy sequence is elementary once the morphic decomposition is exposed, so independent rediscovery in an unindexed note or computation remains possible.

## References
1. L. Schaeffer and J. Shallit, “String Attractors for Automatic Sequences,” arXiv:2012.06840v1, first public version 2020-12-12; later revised through 2024.
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, and Y. Okamoto, “The Smallest String Attractors of Fibonacci and Period-Doubling Words,” arXiv:2602.16152v1, 2026-02-18; CPM 2026.
