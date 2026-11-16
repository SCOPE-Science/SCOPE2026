# Complete Walsh recovery and sharp projection constant for regular seven-vertex tournaments

## Finding
Let \(G=\mathbb F_2^{21}\) be indexed by the lexicographically ordered edges \((i,j)\), \(0\le i<j\le6\), of \(K_7\). Encode a tournament by \(x_{ij}=0\) for \(i\to j\) and \(x_{ij}=1\) for \(j\to i\). Write \(R\subseteq G\) for the regular tournaments, with outdegree three at all seven vertices. For every \(s\in G\), define the unnormalized Walsh multiplier
\[
W(s)=\sum_{x\in R}(-1)^{\langle s,x\rangle}.
\]
The complete distribution of absolute multipliers is as follows. These are exact integer counts, with \(2^{21}=2,097,152\) frequencies.

| \(|W(s)|\) | Number of frequencies |
| ---: | ---: |
| 0 | 1,543,168 |
| 16 | 241,920 |
| 32 | 26,880 |
| 48 | 87,360 |
| 80 | 40,320 |
| 96 | 80,640 |
| 112 | 23,040 |
| 176 | 40,320 |
| 240 | 6,720 |
| 528 | 6,720 |
| 2,640 | 64 |

Thus counting convolution \(T f=1_R*f\) on \(G\) has
\[
\operatorname{rank}T=553984,\qquad \dim\ker T=1543168.
\]
Every nonzero multiplier is divisible by \(16\), and magnitude \(16\) occurs. On its Hilbert-space range, the inverse has norm \(\|(T|_{\operatorname{ran}T})^{-1}\|_{2\to2}=1/16\) and condition number \(165\). Exactly \(494592\) even-weight frequencies vanish beyond the \(2^{20}\) odd-weight zeros explained by global tournament reversal.

Writing \(V=\operatorname{ran}T\) as a subspace of real or complex functions on \(G\), the least norm among **all** linear projections onto \(V\) is, at either endpoint,
\[
\Lambda_1(V)=\Lambda_\infty(V)=\frac{11155}{256}.
\]

## Assumptions and scope
Edges are indexed in increasing lexicographic order and each edge contributes one binary coordinate. A regular tournament has all indegrees and outdegrees equal to three. Convolution and the Fourier transform are unnormalized: \((f*g)(x)=\sum_y f(y)g(x-y)\), and \(\widehat f(s)=\sum_x f(x)(-1)^{s\cdot x}\). All \(\ell^p\) spaces use counting measure; the norm of a convolution operator is independent of a common scaling of input/output measures. The restricted inverse means the inverse of \(T\) on its range, not on all of \(\ell^2(G)\). No statement about larger tournament orders is asserted.

## Proof
**1. An exact six-coordinate reduction.** Write \(a_v=x_{0v}\) for \(1\le v\le6\), and let \(z\in\mathbb F_2^{15}\) consist of the orientations \(x_{ij}\) on the fifteen edges \(1\le i<j\le6\). The outgoing-degree equation at vertex \(v\), reduced modulo two, gives
\[
a_v\equiv v+1+\sum_{\substack{1\le i<j\le6\\v\in\{i,j\}}}z_{ij}\pmod2.\]
Hence a regular tournament is uniquely determined by its internal coordinates \(z\), and the set \(A\subseteq\mathbb F_2^{15}\) of those coordinates has exactly \(2640\) elements. For any original Walsh frequency \(s=(b,c)\), with \(b\in\mathbb F_2^6\) on the star edges and \(c\in\mathbb F_2^{15}\) on internal edges, define \(r_{ij}=c_{ij}+b_i+b_j\) over \(\mathbb F_2\). Then
\[
W(s)=(-1)^{\sum_{v=1}^6(v+1)b_v}\sum_{z\in A}(-1)^{\langle r,z\rangle}.
\]
Each \(r\) has precisely \(2^6=64\) preimages \(s\), so the absolute multiplier spectrum is the sixty-fourfold lift of the exact fifteen-coordinate transform \(F(r)=\sum_{z\in A}(-1)^{r\cdot z}\).

**2. A finite exact coefficient certificate.** A second, independent enumeration generates all \(2^{21}\) full orientation masks and retains exactly those with seven outgoing degrees equal to three. Both independent constructions give \(|R|=2640\). Applying integer butterfly steps \((u,v)\mapsto(u+v,u-v)\) to the indicator of \(A\) yields the absolute multiplier histogram displayed above after the sixty-fourfold lift; no floating-point computation is used. The fifteen-coordinate transform has exactly \(8656\) nonzero entries, whose lift gives rank \(64\cdot8656=553984\). Its smallest nonzero absolute value is \(16\), and its maximum is \(2640\). The separate full-cube computation agrees at every summarized invariant. The exact quotient calculation has
\[
\sum_{r\in\mathbb F_2^{15}}F(r)^2=2^{15}\cdot2640,
\]
which also checks the Parseval normalization. The complete executable enumerations are in `verify_k7.py` and `verify_k7_full.cpp`; `SPECTRUM_CERTIFICATE.json` records the replay targets. Finite exhaustiveness follows from the explicit recursions over all possible edge choices and exhaustive butterfly loops, not from a statistical sample.

**3. Sharp inverse and projection.** Every character is an eigenvector for \(T\) with eigenvalue \(W(s)\), hence rank, inverse norm, and condition number follow from Step 2. If \(S=\{r:F(r)\ne0\}\) and \(K_{15}(z)=2^{-15}\sum_{r\in S}(-1)^{r\cdot z}\), the same exact Walsh checker finds
\[
\sum_{z\in\mathbb F_2^{15}}\left|\sum_{r\in S}(-1)^{r\cdot z}\right|=1427840.
\]
The Fourier support of the full operator is the pullback of \(S\) along the linear map \((b,c)\mapsto(c_{ij}+b_i+b_j)\). Its inverse Fourier indicator kernel is therefore supported on the annihilator of this map's six-dimensional kernel and has the same \(\ell^1\)-norm as \(K_{15}\). Thus the canonical Fourier projection onto \(V\) has endpoint operator norm
\[
\|K_{15}\|_1=\frac{1427840}{32768}=\frac{11155}{256}.
\]
For any linear projection \(P\) onto the translation-invariant space \(V\), conjugate \(P\) by each group translation and average. Translations are isometries of both \(\ell^1\) and \(\ell^\infty\), so averaging cannot increase the norm. The average is a translation-invariant projection onto \(V\), necessarily the canonical Fourier projection with multiplier \(1_S\) on \(V\) and zero off it. Hence the displayed endpoint norm is optimal among unrestricted real and complex projections.

## Verification
From a directory containing the included source files, execute `python3 verify_k7.py`. It uses only the Python standard library. Independently compile `verify_k7_full.cpp` with `g++ -O3 -std=c++17 -o verify_k7_full` and run `./verify_k7_full`. The expected success messages are `REGULAR_K7_QUOTIENT_PASS` and `REGULAR_K7_FULL_PASS`. The quotient script independently derives the six-coordinate parity law and recursively enumerates all regular tournaments; the full checker enumerates all orientation masks directly. Both compute exact integer transforms and spectral invariants. The analytic projection-optimality step is given in the proof above.

## Relationship to prior work
Goodall (2008) develops finite Fourier and graph-polynomial techniques, including results involving graph orientations and flows, but does not give this particular regular-tournament signed character census or evaluated endpoint projection constant. Kühn, Osthus, and Treglown (2009) study Hamilton decompositions of regular tournaments, not their indicator-convolution Walsh rank. McKay's tournament catalogue records the three isomorphism classes at order seven and related counts; these classical enumeration facts are not claimed new. The published result *Integral tight Fourier sampling and tree-complement designs for regular tournaments* determines all first-degree edge-character covariance structure and joint independence of matching-edge signs, but explicitly restricts its spectral claims to the first-degree band. The present result instead counts zeros of all \(2^{21}\) Boolean characters of the indicator on the entire edge cube and evaluates the corresponding full-range endpoint projection norm. The published seven-vertex multipath-homology classification treats a different invariant of individual tournament representatives and does not imply the signed aggregate Fourier spectrum.

## Limitations
This is an exact finite theorem for regular tournaments on seven labelled vertices. The order-seven case is the first with three nonisomorphic regular tournament types, making it a canonical nontrivial benchmark, but no higher-order rank formula is asserted. Some vanishing modes follow from established reversal and matching-sign symmetries; the new contribution is the complete global spectrum and sharp unrestricted projection constant, not a claim that every zero is novel or unexplained. General graph-polynomial formulas may encode these values implicitly without having evaluated them. Independent mathematical audit and exhaustive historical-priority certification have not been performed.

## References
1. A. Goodall, *Graph polynomials and Tutte-Grothendieck invariants: an application of elementary finite Fourier analysis*, arXiv:0806.4848v1, first posted 2008-06-30, https://arxiv.org/abs/0806.4848.
2. D. Kühn, D. Osthus, A. Treglown, *Hamilton decompositions of regular tournaments*, arXiv:0908.3411v1, first posted 2009-08-24, https://arxiv.org/abs/0908.3411.
3. B. D. McKay, *Digraphs: Regular and Semi-regular Tournaments*, catalogue, https://users.cecs.anu.edu.au/~bdm/data/digraphs.html (retrieved 2026-11-12 UTC).
4. *Integral tight Fourier sampling and tree-complement designs for regular tournaments*, publicly available result https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-tight-fourier-sampling-and-tree-complement-designs-for--eaf6965e2c4a.
5. *Integral multipath homology classifies the three regular seven-vertex tournaments*, publicly available result https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-integral-multipath-homology-classifies-the-three-regular-seven-v--ad3787b8ca8f.
