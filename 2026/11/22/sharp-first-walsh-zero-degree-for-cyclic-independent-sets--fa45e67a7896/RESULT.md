# Sharp first Walsh-zero degree for cyclic independent sets

## Finding
For every integer \(n\ge3\), let \(\mathcal L_n\subseteq\mathbb F_2^n\) contain exactly the incidence vectors of all independent vertex sets of the labelled cycle \(C_n\), including the empty set. For a frequency \(S\subseteq\{1,\ldots,n\}\), define the unnormalized Walsh multiplier
\[
 W_n(S)=\sum_{x\in\mathcal L_n}(-1)^{\sum_{j\in S}x_j}.
\]
The **first vanishing Walsh degree at each singular cycle length** is exactly
\[
 \boxed{\min\{|S|:W_{3k}(S)=0\}=k+1,\qquad k\ge1.}
\]
Thus, for every \(n=3k\), convolution with \(\mathbf 1_{\mathcal L_n}\) is injective on the full space of Walsh polynomials of degree at most \(k\), but not on the space of degree at most \(k+1\). At lengths not divisible by three, all Fourier multipliers are nonzero; that known mod-three boundary is recalled for context and re-proved by parity below, not claimed as new. This is a statement about *frequency Hamming weight*, not the number of nonzero coefficients of a general signal.

## Assumptions and scope
The cycle is simple, the ambient group is \(\mathbb F_2^n\) with componentwise XOR, and the Fourier transform and convolution are unnormalized. Each position of the length-\(n\) sign word receives \(-\) if it belongs to \(S\) and \(+\) otherwise. Fourier degree means \(|S|\). The claimed new sharp first-zero degree concerns all lengths \(n=3k\); it neither determines total Fourier nullity nor identifies every zero-frequency sign word. An \(n\)-cycle has \(n\) distinct labelled vertices, including at \(n=3\).

## Proof
**1. Exact transfer identity and parity.** Write
\[
 A_+=\begin{pmatrix}1&1\\1&0\end{pmatrix},\qquad
 A_-=\begin{pmatrix}1&-1\\1&0\end{pmatrix}.
\]
For a sign word \(s_1\cdots s_n\), the closed binary nearest-neighbour transfer expansion gives
\[
 W_n(S)=\operatorname{tr}(A_{s_1}\cdots A_{s_n}).\tag{1}
\]
Indeed, the matrix multiplication traces all cyclic \(0/1\) choices with no adjacent ones; choosing a one at position \(j\) multiplies the term by \(s_j\). Modulo two, both matrices coincide with \(F=\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\), which has order three in \(\mathrm{GL}_2(\mathbb F_2)\). Thus if \(3\nmid n\), the trace of every product is odd and cannot vanish. If \(3\mid n\), every product \(M\) is congruent to the identity modulo two. If additionally \(\operatorname{tr}M=0\), then \(M=I+2B\) for an integral matrix \(B\) with \(\operatorname{tr}B=-1\). Hence \(\det M=-1+4\det B\), whereas \(\det M\in\{-1,1\}\); therefore \(\det M=-1\). Cayley--Hamilton gives \(M^2=I\). This also shows that the number \(p\) of plus signs is odd, as \(\det M=(-1)^p\).

**2. A free-product reduction.** Put \(R=A_-\), \(T=A_+R^{-1}=\bigl(\begin{smallmatrix}-1&2\\0&1\end{smallmatrix}\bigr)\). On the real projective line, \(R(t)=1-1/t\), \(T(t)=2-t\), \(R^3=-I\), and \(T^2=I\). The two domains \(U=(-\infty,1)\) and \(V=(1,\infty)\) obey \(R(V)\subset U\), \(R^2(V)\subset U\), and \(T(U)\subset V\). The standard ping-pong argument (apply an alternating reduced word to its appropriate domain) therefore proves that the images of \(R,T\) generate the free product \(C_3*C_2\) in \(\mathrm{PGL}_2(\mathbb R)\). In a free product of two finite cyclic groups, every finite-order element is conjugate to an element of one of the factors, as is immediate by cyclically reducing its syllable word. Consequently, a product with trace zero is conjugate, projectively, to \(T\): it is a nonidentity involution with determinant \(-1\), while the other factor \(R\) has order three. Conversely a projective conjugate of \(T\) has trace zero.

**3. A cyclic syllable-length inequality.** Suppose a word has \(p\ge1\) plus positions and its product is conjugate to \(T\). Since cyclic rotation conjugates its product, rewrite its projective matrix word as
\[
 T R^{g_1}T R^{g_2}\cdots T R^{g_p},\qquad g_j\ge1,\quad\sum_j g_j=n.
\]
We claim
\[
 n\ge\frac{3(p+1)}2.\tag{2}
\]
The number \(p\) is odd. For \(p=1\), the word \(TR^n\) is conjugate to \(T\) only if \(3\mid n\), and then \(n\ge3\). For \(p\ge3\), if none of the gaps \(g_j\) is divisible by three, the displayed syllable word is cyclically reduced, with alternating nontrivial \(T\)- and \(R\)-syllables, so it has infinite order: a contradiction. Choose a gap divisible by three. If it is at least six, remove three occurrences of \(R\); this changes neither the projective group element nor \(p\), and strong induction on \(n\) gives (2) for the shortened word, hence also for the original. If the gap equals three, cancel the block \(TR^3T\), which is the identity in the projective group; its neighbouring positive \(R\)-gaps concatenate. The shorter cyclic word has \(p-2\) plus positions and \(n-3\) total \(R\)'s. Induction gives \(n-3\ge3((p-2)+1)/2\), which is exactly (2). These are all cases, establishing the inequality for every such word.

**4. Sharpness.** If \(n=3k\), let \(m=|S|\) be the number of minus signs, so \(p=3k-m\). Inequality (2) implies \(3k\ge3(3k-m+1)/2\), hence \(m\ge k+1\). To attain equality, begin with the three-letter cyclic word \(+--\), whose product has trace zero. The elementary exact matrix identity
\[
 A_+A_-A_-A_+=-A_-
\]
shows that replacing **any** minus character by the four-letter word \(+--+\) changes the total matrix product only by a sign. Each replacement increases the length by three and the number of minus symbols by one. Repeating this operation \(k-1\) times yields a length-\(3k\) word with exactly \(k+1\) minus symbols and trace zero. Thus the lower bound is sharp.

Finally, Walsh characters diagonalize unnormalized counting convolution, and each character has eigenvalue \(W_n(S)\), which proves the asserted low-degree injectivity and failure at the next degree. \(\square\)

## Verification
Two standalone programs in this package use independent computational routes. `verify_fwht.py` enumerates the cyclic independent-set indicator and computes its full exact-integer Walsh--Hadamard transform, confirming the first-zero degree for every \(3\le n\le18\). `verify_transfer.py` evaluates exact integer \(2\times2\) products and independently normalizes the reduced words of \(C_3*C_2\) for every frequency through \(n=15\); it checks the two key matrix identities. These finite computations reproduce the data but are not a substitute for the all-integer group-theoretic proof above. The proof needs no computer enumeration.

## Relationship to prior work
Levit and Mandrescu (arXiv:0904.4819, §2) determine the *uniform* specializations \(I(C_n;-1)\) of the cycle independence polynomial, not the mixed-sign Walsh-zero threshold. Radchenko and Rodriguez Villegas (2021, Proposition 5.1) give the multivariate cycle independence polynomial and an exact transfer-matrix trace representation; this supports equation (1), but their main theorem concerns hypergeometric reciprocal expansions, not the Hamming degree at which sign-specialized traces can first vanish. Previous results on the same Lucas-cube indicator had established its mod-three invertibility dichotomy, and characterized the zeros of degrees at most three. The present theorem adds an all-length sharp degree threshold, strictly beyond those low-degree statements starting at \(n=9\). A separate known result on the **restricted** Fourier interpolation matrix indexed by independent sets addresses a distinct square operator, not convolution on the entire Boolean group. The comparison does not establish absolute priority against unindexed work.

## Limitations
This theorem does not count all zero frequencies at singular lengths, compute the complete signed multiplier spectrum, or give quantitative conditioning on its nonzero modes. It applies to activity-one indicators of independent sets of simple cycles, not arbitrary hard-core activities or other graph families. Historical-priority assessment is bounded by the specifically inspected sources and available indexes; no independent audit has been performed.

## References
- V. E. Levit and E. Mandrescu, *The independence polynomial of a graph at -1*, arXiv:0904.4819v1, posted 2009-04-30, §2, especially Lemma 2.3. https://arxiv.org/html/0904.4819v1
- D. Radchenko and F. Rodriguez Villegas, *Independence polynomials and hypergeometric series*, Bull. London Math. Soc. **53** (2021), 1834--1848, Proposition 5.1 and §5. https://doi.org/10.1112/blms.12545
- *Exact Lucas-cube Fourier precision and parity-split sharp frame conditioning*, published 2026-11-01, especially Finding and Assumptions, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-lucas-cube-fourier-precision-and-parity-split-sharp-frame--159f7c631a3c
- *Graph-exclusion Fourier interpolation: universal invertibility and a mod-four inverse resonance*, published 2026-11-08, especially Finding and Assumptions, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-graph-exclusion-fourier-interpolation-universal-invertibility-an--0cb9494a16e7
