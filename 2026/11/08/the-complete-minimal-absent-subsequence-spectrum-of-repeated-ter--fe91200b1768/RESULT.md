# The complete minimal-absent-subsequence spectrum of repeated ternary permutations

## Finding

Fix the ordered alphabet \(\Sigma=\{0,1,2\}\), and let \(W_k=(012)^k\) for every integer \(k\ge1\). A **minimal absent scattered subsequence** of \(W_k\) is a nonempty word not embedded in \(W_k\), each of whose single-letter deletions is embedded. Let \(m_{k,\ell}\) denote the number of distinct such words of length \(\ell\); distinct words, not their different embeddings, are counted.

**Structural classification.** For a word \(v=v_1\cdots v_\ell\) of length \(\ell\ge2\), define its weak-descent count
\[
D(v)=\sum_{i=2}^{\ell}\mathbf1_{\{v_i\le v_{i-1}\}}.
\]
Then \(v\) is a minimal absent scattered subsequence of \(W_k\) **if and only if** all three conditions hold:
\[
D(v)=k,\qquad v_2\le v_1,\qquad v_\ell\le v_{\ell-1},
\]
and, for each \(2\le i\le\ell-1\),
\[
\mathbf1_{\{v_i\le v_{i-1}\}}+
\mathbf1_{\{v_{i+1}\le v_i\}}-
\mathbf1_{\{v_{i+1}\le v_{i-1}\}}=1.
\]
In particular, \(m_{k,\ell}=0\) outside \(k+1\le\ell\le2k\).

**Complete length spectrum.** With \(y\) marking candidate length and \(z\) marking the number of repeats,
\[
F(y,z)=\sum_{k\ge1}\sum_{\ell\ge2}m_{k,\ell}y^\ell z^k=\frac{N(y,z)}{Q(y,z)},
\]
where
\[
\begin{aligned}
N(y,z)=y^2z\big(&6-8yz+6y^2z+3y^2z^2+6y^3z^2+y^4z^2\\
&-9y^4z^3+6y^5z^3+9y^6z^4-y^7z^4-3y^8z^5\big),
\end{aligned}
\]
\[
\begin{aligned}
Q(y,z)={}&1-3yz+3y^2z^2-y^3z^2-y^3z^3-3y^4z^3\\
&+3y^5z^4-y^6z^4-3y^7z^5+y^9z^6.
\end{aligned}
\]
Thus the total number \(M_k=\sum_\ell m_{k,\ell}\) has rational generating function
\[
\sum_{k\ge1}M_kz^k=
\frac{z(6-2z+10z^2-3z^3+8z^4-3z^5)}
{1-3z+2z^2-4z^3+2z^4-3z^5+z^6}.
\]
The first ten exact totals are \(6,16,46,127,349,960,2640,7264,19989,54999\).

## Assumptions and scope

Every quantified word is over the **fixed ordered** ternary alphabet. Scattered subsequence means an order-preserving, not necessarily contiguous, selection of positions. The length and the number of repeated blocks vary independently over the indicated positive integers. A word is minimal absent if all immediate predecessors in the subsequence order, equivalently all single-letter deletions, occur; it need not be of shortest possible absent length. The result addresses these exact hosts and does not assert an all-alphabet generating function.

## Proof

**1. Exact greedy position.** Number positions in \((012)^\omega\) from one. For a nonempty candidate \(v=v_1\cdots v_\ell\), its greedily selected position for the first symbol is \(v_1+1\). The gap from symbol \(a\) to symbol \(b\), when greedily selecting \(b\) strictly after \(a\), is
\[
b-a+3\mathbf1_{\{b\le a\}}.
\]
Summing these gaps telescopes. The final greedy position is precisely
\[
1+v_\ell+3D(v).
\]
Since \(0\le v_\ell\le2\), this is at most \(3k\) exactly when \(D(v)\le k-1\). Thus \(v\) is **absent** from \(W_k\) exactly when \(D(v)\ge k\).

**2. All deletion conditions.** Deleting one letter removes at most one from \(D(v)\). For either endpoint the decrease is the single corresponding weak-descent indicator. At an interior position with neighboring letters \(a,b,c\), the decrease is
\[
\delta(a,b,c)=\mathbf1_{\{b\le a\}}+\mathbf1_{\{c\le b\}}-\mathbf1_{\{c\le a\}}.
\]
An inspection of the relative-order cases (including ties) gives \(\delta\in\{0,1\}\). Every deletion of an absent word must have fewer than \(k\) weak descents; hence necessarily \(D(v)=k\) and every endpoint indicator and interior \(\delta\) equals one. Conversely these conditions make every single-letter deletion have exactly \(k-1\) weak descents, so every deletion embeds, proving the equivalence. They also force both endpoint pairs to descend and prohibit two consecutive strict ascents. A string of length \(\ell\) satisfying them has at least \(\lceil\ell/2\rceil\) weak descents and at most \(\ell-1\); therefore \(k+1\le\ell\le2k\).

**3. Nine-state exact enumeration.** Index states by ordered pairs \((a,b)\in\Sigma^2\). The row of initial pair weights, transition matrix and final-column mask are
\[
A_{a,b}=y^2z\mathbf1_{\{b\le a\}},\qquad
T_{(a,b),(b,c)}=
\begin{cases}
yz^{\mathbf1_{\{c\le b\}}},&\delta(a,b,c)=1,\\
0,&\text{otherwise},
\end{cases}\qquad
B_{a,b}=\mathbf1_{\{b\le a\}}.
\]
The matrix \(T\) has all unspecified entries zero. Every permitted word of length at least two is uniquely encoded by one initial pair and the subsequent symbols; the initial pair accounts for its first descent, while every transition supplies the next descent and validates the corresponding interior triple. The final mask imposes the last endpoint descent. This gives, as a **formal** power series in \(y,z\),
\[
F(y,z)=A(I-T)^{-1}B.
\]
The inverse is well-defined because \(T\) has zero constant term in \(y\).

**4. Exact rational certificate.** The separately supplied `certificate.json` contains integer coefficient lists of the displayed \(N,Q\), the nine fixed states, and nine polynomials \(H_{a,b}\). The supplied `verify.py` checks with exact integer polynomial arithmetic all nine identities
\[
H_{a,b}-\sum_{c:\,\delta(a,b,c)=1}
 yz^{\mathbf1_{\{c\le b\}}}H_{b,c}=QB_{a,b}
\]
and the final identity \(\sum_{a,b}A_{a,b}H_{a,b}=N\), together with \(Q(0,0)=1\). Thus \((I-T)H=QB\) and \(AH=N\), proving the displayed quotient identically; no numerical interpolation or finite cutoff is used for this step. Setting \(y=1\) and collecting terms yields the displayed total-count generating function.

## Verification

Run `python3 verify.py` with `certificate.json` alongside it; the verifier requires only the Python standard library. It checks each polynomial identity exactly, compares twelve entire transfer coefficient rows against independent formal-division coefficients, and directly enumerates 103,784 candidate words and their single-letter deletions over several alphabets and host lengths (including the ternary cases through four repeated blocks). The exact first four ternary length spectra are, respectively,
\[
\{2\mapsto6\},\quad
\{3\mapsto10,4\mapsto6\},\quad
\{4\mapsto15,5\mapsto30,6\mapsto1\},\quad
\{5\mapsto21,6\mapsto91,7\mapsto15\}.
\]
The finite comparisons are checks only; the proof for every \(k\) is the greedy argument and nine polynomial identities.

## Relationship to prior work

Kosche, Koß, Manea and Siemer define the repeated-increasing-permutation family \(B_k\) and establish polynomially many shortest absent subsequences, together with exponential growth of minimal absent subsequences in a specified range of alphabet and repeat parameters (their Proposition 3.8). Their stated classification and counting bounds do **not** give the present exact, length-refined ternary counts or rational generating function. Their shortest-absence subfamily corresponds here to the coefficient at length \(k+1\), namely \(\binom{k+3}{2}\), and is not claimed as new.

Other work determines extremal numbers of absent subsequences at fixed lengths or gives output-efficient algorithms for enumerating minimal absent subsequences of arbitrary finite words; these results provide useful context but do not state an all-\(k\), all-length formula for these ternary hosts. The binary repeated-permutation case is distinct and already has an exact description; this result does not re-claim it.

## Limitations

The exact enumerator is for ternary increasing-permutation repetitions only, not all alphabet sizes or arbitrary periodic words. A decidable finite algorithm for counting arbitrary words is not the same statement as the closed rational enumerator here. The reviewed primary literature and the accessible mathematical-record comparisons did not reveal an equivalent formula; this does not prove the absence of an unindexed equivalent. The full text of a plausibly relevant 2023 survey/chapter could not be accessed and remains a bibliographic risk. No independent audit of the result has been conducted.

## References

- M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words* (first public 2021-08-31), arXiv:2108.13968, especially §3 and Proposition 3.8. https://arxiv.org/abs/2108.13968
- D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn and M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences* (first public 2024-07-26), arXiv:2407.18599. https://arxiv.org/abs/2407.18599
- F. Manea, T. Ringleb, S. Siemer and M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String* (2025), arXiv:2504.21471. https://arxiv.org/abs/2504.21471
- Z. Troníček, *On Problems Related to Absent Subsequences* (2023), DOI:10.1007/978-3-031-49614-1_26. https://doi.org/10.1007/978-3-031-49614-1_26 (full text not inspected).
