# Chromatic parity and a uniform modulo-sixteen Fourier law for four-colour bicliques

## Finding

Let \(G=(V,E)\) be a finite simple graph with \(|V|=d\ge1\). Give the four colours the additive structure \(H=\mathbb F_2^2\). Write \(\mathcal C_G\subset H^V\) for the proper vertex colourings, and define the **unnormalized** Fourier coefficients
\[
W_G(\xi)=\sum_{c\in\mathcal C_G}(-1)^{\sum_{v\in V}\langle\xi_v,c_v\rangle},\qquad \xi\in H^V,
\]
where the bracket is the binary dot product. Let \(P_G(q)=\sum_{j\ge0}a_j q^j\) be the ordinary chromatic polynomial, and let \(P_G(4)=|\mathcal C_G|\).

**Chromatic parity–Fourier principle.** Every frequency with \(\sum_v\xi_v\ne0\) has \(W_G(\xi)=0\); every frequency with \(\sum_v\xi_v=0\) satisfies
\[
\boxed{W_G(\xi)\equiv P_G(4)\pmod {16}.}
\]
In particular, if \(a_1\) is odd, then the Fourier support is **exactly** the \(4^{d-1}\) balanced frequencies. In this case the convolution operator on \(\ell^2(H^V)\) defined by the indicator \(1_{\mathcal C_G}\) has rank \(4^{d-1}\), and its smallest nonzero multiplier magnitude is at least four.

**Complete-bipartite consequence.** For every pair of integers \(m,n\ge2\), putting \(G=K_{m,n}\) gives the explicit universal residue law
\[
\boxed{W_{K_{m,n}}(\xi)\equiv4(-1)^{m+n}\pmod {16}\quad\text{whenever}\quad\sum_v\xi_v=0.}
\]
Thus the nonzero spectrum is supported at **all and only** balanced frequencies, the exact convolution rank is \(4^{m+n-1}\), its nullity is \(3\cdot4^{m+n-1}\), and \(\|C_{m,n}^{\dagger}\|_{2\to2}\le1/4\). The last bound is not asserted to be equality in every dimension.

## Assumptions and scope

The colour group is specifically the Klein four-group with its standard two-bit pairing; this is not a statement about four colours considered as the cyclic group \(\mathbb Z/4\mathbb Z\). Graphs are finite, simple, and nonempty. The general congruence holds even if the graph is disconnected or not four-colourable; the exact-support conclusion requires an odd coefficient \(a_1\). The complete-bipartite residue formula requires both part sizes at least two. There are no probabilistic, asymptotic, or unproved assumptions.

## Proof

**Step 1: translation and orbit reduction.** Translation by a fixed \(t\in H\) of every colour preserves properness. It multiplies the character at \(\xi\) by \((-1)^{\langle t,\sum_v\xi_v\rangle}\). If \(\sum_v\xi_v\ne0\), summing the character over this four-element translation group gives zero. If \(\sum_v\xi_v=0\), choose one root vertex \(v_0\). Each translation orbit has exactly one representative satisfying \(c(v_0)=0\), and its four elements have the same character value. Hence
\[
W_G(\xi)=4\sum_{\substack{c\in\mathcal C_G\\c(v_0)=0}}(-1)^{L_\xi(c)},\qquad
L_\xi(c)=\sum_v\langle\xi_v,c(v)\rangle\pmod 2.
\]
The root-fixed set has size \(N=P_G(4)/4\).

**Step 2: evenness of negative phases.** Permuting the three nonzero elements of \(H\) while fixing zero preserves the root-fixed colouring set: every permutation of the four colour names preserves all equality and inequality constraints. For a nonroot vertex \(v\), the numbers of root-fixed colourings with \(c(v)=a\) are therefore equal for all three nonzero \(a\in H\). Since precisely two of these three colours have either given binary coordinate equal to one, each coordinate bit at each nonroot vertex is one an even number of times over the root-fixed colouring set. The root bits are always zero. Because \(L_\xi\) is a binary-linear sum of these bits, the number \(M\) of root-fixed colourings with \(L_\xi(c)=1\) is even. Consequently
\[
W_G(\xi)/4=N-2M\equiv N\pmod 4,
\]
which is the claimed congruence modulo sixteen. This step uses only the full colour-permutation symmetry and the character's linearity; it does not assume symmetry of the graph.

**Step 3: chromatic-coefficient criterion.** For any nonempty graph, the chromatic polynomial has zero constant coefficient. Hence
\[
P_G(4)/4=a_1+4a_2+4^2a_3+\cdots\equiv a_1\pmod2.
\]
If \(a_1\) is odd, the balanced \(W_G(\xi)/4\) are all odd, so no balanced coefficient vanishes. Their magnitudes are at least four. On the finite abelian group \(H^V\), convolution is diagonalized by the characters with eigenvalues \(W_G(\xi)\), so the rank is the number of nonzero coefficients.

**Step 4: explicit biclique residue.** Let \(S(m,k)\) denote Stirling numbers of the second kind, with \(S(m,k)=0\) for \(k>m\). Classifying the number \(k\) of colours actually used on the side containing \(m\) vertices gives the classical chromatic-polynomial identity
\[
P_{K_{m,n}}(4)=\sum_{k=1}^{3}(4)_k S(m,k)(4-k)^n
=4\cdot3^n+12S(m,2)2^n+24S(m,3),
\]
where \((4)_k\) is the falling factorial. For \(n\ge2\) it follows that
\[
P_{K_{m,n}}(4)/4\equiv3^n+2S(m,3)\pmod4.
\]
The standard recurrence \(S(m,3)=3S(m-1,3)+S(m-1,2)\), with \(S(m,2)=2^{m-1}-1\) and \(S(2,3)=0\), shows that \(S(m,3)\equiv m\pmod2\) for every \(m\ge2\). Since \(3^n\equiv(-1)^n\pmod4\), the last display equals \((-1)^{m+n}\) modulo four. Applying Step 2 completes the proof.

## Verification

The included standalone Python 3 checker `check.py` uses integer-valued Walsh butterflies on all proper colourings of each of the 75 labelled simple graphs on up to four vertices, checking 16,932 frequency values. It also checks all bicliques with \(2\le m,n\le4\), covering 28,224 balanced frequency values, comparing chromatic counts with an independent Stirling sum and 99 exact coefficients with direct signed sums. It prints `CHROMATIC_FOURIER_RESIDUE_PASS` on success. A separate direct signed enumeration for the five-cycle finds a balanced vanishing character at frequency \((2,1,2,1,0)\), illustrating why the odd-\(a_1\) hypothesis cannot simply be omitted. Finite tests do not prove the theorem for all graphs; Steps 1–4 do.

## Relationship to prior work

The ordinary chromatic polynomial, its Stirling expansion for complete bipartite graphs, and the correspondence between its linear coefficient and acyclic orientations with a fixed unique sink are classical. Gebhard and Sagan's 1999 preprint gives proofs of the Greene–Zaslavsky correspondence. Tarsi's 1999 paper treats a different weighted sum of proper colourings built from graph-polynomial coefficients and modular flows. The present claim is the congruence for **every additive binary character on the full space of four-colour assignments**, together with the resulting exact Fourier support and operator rank; neither inspected article states that congruence. A separately indexed work on first-coordinate Fourier sampling over proper complete-bipartite colourings concerns the degree-one Gram spectrum, not the whole convolution-multiplier spectrum; its full text was not available for direct comparison. Ordinary colour counts alone give the zero-frequency value and cannot determine whether arbitrary signed coefficients vanish without Step 2.

## Limitations

The parity criterion is sufficient, not necessary, for full balanced Fourier support; it says nothing decisive when \(a_1\) is even. For example, on the five-cycle a balanced frequency can have zero coefficient, as independently checked. The result does not determine the exact minimum nonzero multiplier above the guaranteed bound, the complete magnitude distribution, or analogous congruences for larger colour groups. The full text of one plausible specialized first-Fourier-band comparison was inaccessible; undiscovered earlier full-character results remain a priority risk. The proof and finite checker have not been independently certified.

## References

1. D. D. Gebhard and B. E. Sagan, *Sinks in Acyclic Orientations of Graphs*, arXiv:math/9907078v1, publicly dated 1999-07-12, Theorem 1.2 (Greene–Zaslavsky correspondence), https://arxiv.org/pdf/math/9907078 .
2. M. Tarsi, *The graph polynomial and the number of proper vertex coloring*, Annales de l'Institut Fourier 49 (1999), 1089–1093, DOI:10.5802/aif.1707, https://www.numdam.org/article/AIF_1999__49_3_1089_0.pdf .
3. OEIS A212084, chromatic-polynomial coefficients of \(K_{n,n}\), entered 2012-04-30, https://oeis.org/A212084 .
4. *Exact Fourier sampling spectra and a thin-side conditioning transition for bipartite colourings*, indexed repository record 2026/11/1, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-fourier-sampling-spectra-and-a-thin-side-conditioning-tran--2b34d08d2568 (abstract compared; full text unavailable).
