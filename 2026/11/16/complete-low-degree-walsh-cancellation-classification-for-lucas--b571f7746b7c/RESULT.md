# Complete low-degree Walsh cancellation classification for Lucas cubes

## Finding
For every integer \(n\ge3\), let \(\mathcal L_n\subset\mathbb F_2^n\) be the incidence vectors of independent vertex sets of the simple cycle \(C_n\). For a frequency support \(S\subseteq\{0,\ldots,n-1\}\), let
\[
W_n(S)=\sum_{x\in\mathcal L_n}(-1)^{\sum_{i\in S}x_i}.
\]
Among all frequencies of Hamming weight at most three, the **only zero multipliers** are:

- \(n=3\), \(|S|=2\): all three two-vertex supports;
- \(n=6\), \(|S|=3\): precisely the 12 three-vertex supports whose three successive circular gaps, in some order, are \(1,2,3\).

In particular, for every \(n\ge7\), every unnormalized Walsh multiplier supported on at most three vertices is nonzero. The three-coordinate exception at \(n=6\) occurs even though every one- and two-coordinate multiplier at that length is nonzero.

## Assumptions and scope
Vertices of \(C_n\) are the residues modulo \(n\), \(n\ge3\), with edges between consecutive residues. Independent means no two adjacent selected vertices, including the wrap-around edge. Frequencies are binary characters, not normalized covariances. For \(|S|=3\), its cyclic gaps are the three strictly positive distances encountered on a clockwise traversal of the marked vertices; their sum is \(n\). Nothing here asserts a classification at Fourier degree four or higher, or a classification for a non-cycle graph.

## Proof
A transfer automaton records whether the preceding vertex is occupied. Its signed transfer matrix, for a vertex with character sign \(z=\pm1\), is
\[
M(z)=\begin{pmatrix}1&z\\1&0\end{pmatrix},\qquad A=M(1),\qquad B=M(-1).
\]
The periodic boundary condition is a trace, so for a frequency supported at \(k\) distinct marked vertices with successive cyclic gaps \(g_1,\ldots,g_k\ge1\),
\[
W_n(S)=\operatorname{tr}\bigl(B A^{g_1-1}B A^{g_2-1}\cdots B A^{g_k-1}\bigr). \tag{1}
\]
This follows bijectively by summing the weights of all closed state walks; forbidden consecutive occupations have transfer weight zero. In particular \(A^2=A+I\). Thus the trace in (1), as a function of any one gap with the other gaps fixed, satisfies the positive recurrence
\[
F(\ldots,g+2,\ldots)=F(\ldots,g+1,\ldots)+F(\ldots,g,\ldots). \tag{2}
\]

For zero marked vertices the sum is the positive Lucas count \(L_n\). For one marked vertex (1) is \(\operatorname{tr}(BA^{n-1})=F_n\), the positive Fibonacci number, with \(F_0=0,F_1=1\).

For two marked vertices write \(H(d,e)=\operatorname{tr}(BA^{d-1}BA^{e-1})\), with \(d+e=n\). Exact multiplication gives
\[
H(1,2)=0,\quad H(1,3)=H(1,4)=-1,
\]
\[
H(2,2)=H(2,3)=H(3,2)=3,\quad H(3,3)=2.
\]
By (2), \(H(1,e)<0\) for every \(e\ge3\). Starting from the positive \(2\times2\) block at \(d,e\in\{2,3\}\) and applying (2) in each coordinate proves \(H(d,e)>0\) for every \(d,e\ge2\). Symmetry covers \(H(d,1)\). Therefore the only degree-two zeros are at \(n=3\).

For three marked vertices set \(J(a,b,c)=\operatorname{tr}(BA^{a-1}BA^{b-1}BA^{c-1})\). The following **exact finite sign certificate** uses the four classes \(1,2,3,H\), where \(H\) means an integer at least four. For every \(H\) coordinate, evaluate both initial values \(4\) and \(5\). Direct integer multiplication gives one strict sign for every resulting seed in each of the 64 boxes, except the six indicated zero boxes. Each row below is indexed by the second gap \(b=1,2,3,H\), each column by the third gap \(c=1,2,3,H\); the four blocks correspond to \(a=1,2,3,H\), respectively:

```text
a=1       a=2       a=3       a=H
- - - -   - + 0 +   - 0 - -   - + - -
- + 0 +   + + + +   0 + + +   + + + +
- 0 - -   0 + + +   - + + +   - + + +
- + - -   + + + +   - + + +   - + + +
```

The six zeros appear only for permutations of \((a,b,c)=(1,2,3)\). To see why this finite certificate suffices for *every* triple of positive gaps, fix any box and hold its low coordinates fixed. Every high coordinate has two consecutive initial values of the same strict sign. Recurrence (2) extends that sign to every larger value; apply the recurrence successively in each high coordinate. Thus no further zero is possible. The six zero gap triples each sum to six and describe exactly the indicated three-vertex supports of \(C_6\). Rotations and reflections give 12 distinct supports, completing the classification.

## Verification
Run `python3 CHECKER.py` with Python 3.8 or newer. The checker uses only integer operations: it verifies every one of the 64 sign-region certificates (including all \(4,5\) corners), checks the two-gap and one-gap identities, and independently enumerates all cyclic independent-set vectors and their Walsh characters of degrees one through three at every \(3\le n\le12\). Its success marker is `LUCAS_CYCLE_CUBIC_WALSH_PASS`. The enumeration is a cross-check; the arbitrary-size conclusion is proved by the positive recurrences and finite seed sign certificate. No numerical floating point tolerances are used.

## Relationship to prior work
Codara and D'Antona (2012; expanded 2014) describe independent subsets of cycle powers, Lucas cubes, and their Hasse edge enumerators. The established Lucas-number count and the identification of Lucas-cube vertices are background, not the new result. A closely related public mathematical record studies centered first-degree Fourier Gram matrices and their precision for Lucas cubes, providing information about one- and two-coordinate moments but not the three-coordinate nullity classification above. Transfer-matrix methods are classical; the claim is the exact all-length degree-three zero classification, not the invention of those methods.

## Limitations
The theorem is limited to Fourier support size at most three, and neither implies nor claims full convolution invertibility. Other Fourier zeros exist at higher support degrees, for example on longer cycles. Historical-priority review is bounded: unpublished or unindexed higher-order correlation formulas may exist, and the closest public first-degree study was available in searchable summary rather than full source text. No independent external mathematical audit has been performed.

## References
1. P. Codara and O. M. D'Antona, *On the independent subsets of powers of paths and cycles*, arXiv:1210.5561v1, first public 2012-10-19, https://arxiv.org/abs/1210.5561.
2. P. Codara and O. M. D'Antona, *Generalized Fibonacci and Lucas cubes arising from powers of paths and cycles*, arXiv:1410.4080v1, first public 2014-10-15, https://arxiv.org/abs/1410.4080.
3. *Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-lucas-cube-fourier-precision-and-parity-split-sharp-frame--159f7c631a3c (comparison accessible in searchable abstract only).
