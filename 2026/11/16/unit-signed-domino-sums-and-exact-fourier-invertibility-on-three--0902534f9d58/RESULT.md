# Unit signed domino sums and exact Fourier invertibility on three-row strips

## Finding
For every integer \(m\ge1\), let \(G_m=P_3\square P_{2m}\) be the grid graph with three rows and \(2m\) columns. Its perfect matchings \(\mathcal T_m\) are the domino tilings of a \(3\times 2m\) rectangle. Identify a matching with its edge-incidence vector in \(\mathbb F_2^{E(G_m)}\). For a frequency \(b\) on the edge set, put
\[
W_m(b)=\sum_{T\in\mathcal T_m}(-1)^{\sum_{e\in T}b_e}.
\]
Then **every** coefficient is odd, and the smallest absolute Walsh coefficient is exactly one:
\[
\boxed{\min_b|W_m(b)|=1.}
\]
More explicitly, let \(b_*\) equal one on the two vertical edges in every **odd-numbered** column (columns numbered \(1,\dots,2m\)) and zero on all other edges. Then
\[
\boxed{W_m(b_*)=(-1)^{\lceil m/2\rceil}.}
\]
The unnormalized convolution operator \(C_m f=\mathbf1_{\mathcal T_m}*f\) on \(\ell^2(\mathbb F_2^{E(G_m)})\) is therefore invertible, with exact inverse norm \(\|C_m^{-1}\|_{2\to2}=1\) and exact spectral condition number
\[
\boxed{\kappa_2(C_m)=A_m,\quad A_0=1,\ A_1=3,\ A_m=4A_{m-1}-A_{m-2}\ (m\ge2).}
\]
In particular \(A_m=\tfrac12[(1+1/\sqrt3)(2+\sqrt3)^m+(1-1/\sqrt3)(2-\sqrt3)^m]\), so the condition number grows exponentially while the exact inverse norm remains one.

## Assumptions and scope
Coordinates of the ambient binary group correspond to individual, undirected grid edges; the two vertical edges in an odd column both receive a minus sign under \(b_*\). The Walsh transform and convolution use counting measure and **no normalization factor**. The operator acts on complex- or real-valued functions of all edge-sign configurations in the ambient binary group. The empty board is included only as an auxiliary initial condition \(A_0=1\).

## Proof
**Four profile states.** Process columns left to right. After filling the current column, let \(a\) be the signed count leaving no right-protruding horizontal domino; \(u\) the signed count for each of the two symmetric singleton protrusions (top and bottom); \(c\) the count for all three protrusions; and \(v\) the count for each of the two adjacent-row double protrusions. The state is \((a,u,c,v)\), initially \((1,0,0,0)\). For a column whose two vertical edges share sign \(t\in\{-1,1\}\), and with horizontal edges of sign \(+1\), enumerating the ways to cover all presently unoccupied cells gives the exact transfer
\[
(a,u,c,v)\mapsto(2tu+c,\;ta+v,\;a,\;u).\tag{1}
\]
This recurrence is an equality of signed matching partition functions, not an asymptotic or experimental assertion.

**An explicit unit Walsh coefficient.** Apply (1) successively with \(t=-1\) in the odd column and \(t=+1\) in the subsequent even column. The resulting two-column map is
\[
(a,u,c,v)\mapsto(-a+2v,\;c-u,\;c-2u,\;v-a).\tag{2}
\]
Starting at \(u=c=0\), equation (2) preserves \(u=c=0\). On the remaining pair \((a,v)\), it acts by
\[
M_- =\begin{pmatrix}-1&2\-1&1\end{pmatrix},\qquad M_-^2=-I.
\]
Therefore after \(m\) pairs the signed complete-tiling count, which is its first coordinate, is \(a_m=(-1)^{\lceil m/2\rceil}\). This proves \(|W_m(b_*)|=1\).

**Universal oddness and the unsigned count.** At the zero frequency \(b=0\), both column signs in (1) equal \(+1\). The corresponding two-column map preserves \(u=c=0\) and acts on \((a,v)\) by
\[
M_+=\begin{pmatrix}3&2\1&1\end{pmatrix}.
\]
Its first coordinate is \(A_m\). Since \(\operatorname{tr}M_+=4\), \(\det M_+=1\), Cayley–Hamilton gives \(A_m=4A_{m-1}-A_{m-2}\) with \(A_0=1,A_1=3\). Reducing this recurrence modulo two shows \(A_m\equiv1\pmod2\) for all \(m\ge0\). Every signed Walsh sum \(W_m(b)\) equals \(A_m-2N_b\) for an integer \(N_b\) counting tilings with odd signed edge-intersection. Hence \(W_m(b)\equiv1\pmod2\), and no Walsh coefficient vanishes. The explicit unit witness proves the minimum is precisely one.

**Exact operator norms.** Walsh characters diagonalize group convolution, and the eigenvalues of \(C_m\) are exactly \(W_m(b)\). The smallest absolute eigenvalue is one, so \(\|C_m^{-1}\|_{2\to2}=1\). The triangle inequality gives \(|W_m(b)|\le A_m\), attained at \(b=0\). Therefore the ratio of largest to smallest singular value is exactly \(A_m\). Solving the characteristic polynomial \(z^2-4z+1\) gives the stated formula and exponential growth.

## Verification
The standalone `verify.py` independently enumerates every perfect matching of \(G_m\) for \(m=1,2,3\), evaluates the prescribed signs directly on each matching, and checks the unsigned numbers against the transfer recurrence. It also constructs the entire edge-incidence indicator and runs an integer fast Walsh–Hadamard transform for \(m=1,2\), verifying **every** multiplier's oddness, nonvanishing, and exact extremal absolute values. Independent exact recurrence checks cover \(1\le m\le500\). Running `python3 verify.py` reports `THREE_ROW_DOMINO_FOURIER_EXACT_PASS`. These finite checks test, but do not substitute for, the preceding proof valid for every \(m\ge1\).

## Relationship to prior work
Propp, *A reciprocity theorem for domino tilings* (2001), develops arbitrary signed matching counts and transfer recurrences, including signed graphs related to **negative-width reciprocity**. This supplies general machinery and is not claimed new. His specific signed constructions concern modified grids and negative-width extrapolation, not the complete intact \(3\times2m\) grid with alternating-column vertical signs and an all-length unit Walsh evaluation.

Tenner, *Tiling parity results and the holey square solution* (2004), proves broader parity theorems for tilings and enumerates several odd-count rectangle families. The oddness ingredient here is elementary and is **not** the claimed original point. The specific unit signed Walsh witness simultaneously proves sharp, exact invertibility and conditioning of the full edge-incidence convolution family. The stated Fourier operator conclusion is not asserted in those inspected papers. Relevant related published mathematical results on a circular ladder's perfect matchings concern a **cyclic** prism rather than an open three-row grid; other indexed results concern noncrossing matchings or first-coordinate Fourier sampling, not this transform. This is a bounded comparison, not a proof of historical uniqueness.

## Limitations
Only the three-row open rectangular grid family and its complete perfect matchings are classified. The proof does not provide the complete distribution or multiplicities of all Walsh magnitudes, nor endpoint \(\ell^1\) inverse norms. The original signed-matching transfer formalism is classical; a prior equivalent alternating-edge identity in specialized dimer literature may exist. Independent mathematical validation has not been performed.

## References
- J. Propp, *A reciprocity theorem for domino tilings*, arXiv:math/0104011v1, 2001-04-01, Sections 2, 4 and 6. https://arxiv.org/pdf/math/0104011
- B. E. Tenner, *Tiling parity results and the holey square solution*, arXiv:math/0409105, first version 2004, especially Section 4. https://arxiv.org/pdf/math/0409105
