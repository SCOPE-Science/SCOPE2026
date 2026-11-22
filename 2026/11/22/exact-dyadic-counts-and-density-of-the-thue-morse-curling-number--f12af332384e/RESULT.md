# Exact dyadic counts and density of the Thue–Morse curling-number transform

## Finding
Let \(\mathbf t=t_0t_1\cdots\) be the Thue–Morse word, \(t_j=s_2(j)\bmod 2\), and let \(c_j\) be the curling number of the nonempty prefix \(t_0\cdots t_j\). Thus \(c_j=2\) precisely when the prefix ends in a nonempty square, and otherwise \(c_j=1\). Define
\[
A(N)=\#\{0\le j<N:c_j=1\}.
\]
For every integer \(r\ge2\), the exact dyadic count is
\[
\boxed{A(2^r)=\frac{2^r+9r-4-(r\bmod2)}{6}}.
\]
For arbitrary positive integers \(N\),
\[
A(N)=\frac N6+O((1+\log N)^2),\qquad
\lim_{N\to\infty}\frac{A(N)}N=\frac16.
\]
This proves the frequency previously suggested, without proof, for the number of ones in OEIS A093914 (allowing for that entry's single initial-term offset). The dyadic identity additionally gives an exact parity-sensitive logarithmic correction.

## Assumptions and scope
The alphabet is \(\{0,1\}\); indices begin at zero. The curling number of a nonempty word \(v\) is the largest positive integer \(k\) for which \(v=xy^k\), with \(y\ne\epsilon\). The Thue–Morse word is overlap-free, so each \(c_j\) belongs to \(\{1,2\}\). Set \(U(j)=\mathbf{1}_{\{c_j=1\}}\), so \(A(N)=\sum_{j=0}^{N-1}U(j)\).

We use the established Pansiot–Brlek classification, stated as Theorem 4.1 and localized by Lemma 4.2 in Brown–Rampersad–Shallit–Vasiga [2]: every square factor of \(\mathbf t\) is the image under some \(\mu^k\) of one of \(00,11,010010,101101\), where \(\mu(0)=01\), \(\mu(1)=10\); for \(k\ge1\), occurrences are aligned at multiples of \(2^k\) and descend to corresponding base-square occurrences. The proof below explicitly uses these published results rather than treating finite testing as a proof of the classification.

## Proof
**1. Square-suffix recursion.** Every occurrence of one of the four base squares starts at an odd index: \(00\) and \(11\) cannot begin at an even index because every even-aligned two-letter block is \(01\) or \(10\); \(010010\) and \(101101\) contain an equal-letter even-aligned pair if placed at an even index. Thus base squares end at even indices. For \(k\ge1\), the cited alignment lemma places every higher-level square at an even starting index, and its even length makes its ending index odd. Desubstituting such a square ending at \(2m+1\) gives a square ending at \(m\), and conversely morphing a square ending at \(m\) gives one ending at \(2m+1\). Therefore
\[
U(2m+1)=U(m)\qquad(m\ge0).
\]
At an even endpoint \(2m\), only the four unscaled base squares are possible. For \(m\ge1\), the two-letter square condition is
\[
t_{2m-1}=t_{2m}\iff t_{m-1}\ne t_m.
\]
For \(m\ge3\), the six-letter square condition becomes
\[
(t_{m-3},t_{m-2},t_{m-1},t_m)\in\{0011,1100\}.
\]
These conditions are disjoint, since the latter forces \(t_{m-1}=t_m\). Consequently \(U(0)=1\), and for \(m\ge1\), \(U(2m)=1\) exactly when \(t_{m-1}=t_m\) and the indicated four-letter pattern does not occur (the four-letter condition is void for \(m<3\)). These are pointwise statements, not statistical assumptions.

**2. Exact dyadic counts.** For each integer \(s\ge0\), let \(Q_s\) be the number of equal adjacent pairs completely contained in the length-\(2^s\) Thue–Morse prefix. The identities \(t_{2j}=t_j\), \(t_{2j+1}=1-t_j\) show that equal adjacent pairs begin only at odd positions, and their desubstituted pair must be unequal. Thus \(Q_0=0\) and
\[
Q_s=2^{s-1}-1-Q_{s-1}\qquad(s\ge1),
\]
which solves to
\[
Q_s=\begin{cases}(2^s-1)/3,&s\text{ even},\\(2^s-2)/3,&s\text{ odd}.\end{cases}
\]
Let \(J_s\) count occurrences of either \(0011\) or \(1100\) entirely inside the length-\(2^s\) prefix, \(s\ge2\). Each such occurrence begins at an odd position \(2j+1\), corresponding exactly to an alternating triple \(010\) or \(101\) beginning at \(j\) in the length-\(2^{s-1}\) prefix. An alternating triple begins at either \(2h\) or \(2h+1\) precisely when \(t_h=t_{h+1}\). The two possible starts both fit whenever the original equal pair fits in the length-\(2^{s-2}\) prefix. Hence
\[
J_s=2Q_{s-2}\qquad(s\ge2).
\]
Splitting the \(2^r\) endpoints into odd and even endpoints gives, for \(r\ge3\),
\[
A(2^r)=A(2^{r-1})+1+Q_{r-1}-J_{r-1}
=A(2^{r-1})+1+Q_{r-1}-2Q_{r-3}.
\]
The increment equals \((2^{r-1}+10)/6\) when \(r\) is even and \((2^{r-1}+8)/6\) when \(r\) is odd. Since \(A(4)=3\), induction yields the boxed exact identity for every \(r\ge2\).

**3. Density and effective error.** For any integer \(M\ge1\), let \(Q(M)\) count equal adjacent pairs in the first \(M\) letters, and let \(J(M)\) count factors \(0011\) or \(1100\) entirely contained there. The same parity argument gives
\[
Q(2L)=L-1-Q(L),\qquad Q(2L+1)=L-Q(L+1),
\]
for \(L\ge1\). Iterating these halving recurrences proves \(Q(M)=M/3+O(1+\log M)\). The alternating-triple correspondence in Step 2 implies \(J(M)=2Q(\lfloor M/4\rfloor)+O(1)=M/6+O(1+\log M)\) for arbitrary \(M\), where the \(O(1)\) term accounts for at most two partial boundary blocks. Let \(E(M)\) count the indices \(m<M\) for which \(U(2m)=1\). The pointwise characterization of Step 1 gives exactly
\[
E(M)=1+Q(M)-J(M)=M/6+O(1+\log M).
\]
Odd-endpoint desubstitution then gives the exact relation
\[
A(N)=A(\lfloor N/2\rfloor)+E(\lceil N/2\rceil)
=A(\lfloor N/2\rfloor)+N/12+O(1+\log N).
\]
Iterating over at most \(1+\lfloor\log_2N\rfloor\) halvings proves \(A(N)=N/6+O((1+\log N)^2)\), and hence the stated natural density.

## Verification
The standalone `verify.py` computes the exact square-suffix indicator via the above pointwise recursion for \(2^{20}\) positions. As an independent finite check, it compares each of the first 2048 positions against a direct all-period square-suffix search that does **not** use the recursion. It matches the first 32 entries of the historical curling-number table after correcting for its leading extra \(1\), and verifies the exact dyadic formula for every integer \(2\le r\le20\). `verification-output.txt` contains the actual deterministic output. These finite checks corroborate, but do not replace, the infinite proof and its cited square classification.

## Relationship to prior work
The original Thue–Morse curling-number transform was listed by van de Bult et al. [3, §5.2], who left its properties for investigation. OEIS A093914 [4] recorded on March 3, 2017 the observation that the density of ones *seems* to be \(1/6\), without a proof. Brown et al. [2, §§3–4] classify square factors and develop automata/counts for squares **beginning** at a given position; their results are used in Step 1 but do not state the density or the displayed dyadic count for squares **ending** at prefixes. Caveney–Dong–Shallit [1] study repetition avoidance under curling-number transforms and fix the direct-prefix convention, without deriving this frequency law. The exact counted invariant is neither a beginning-position square frequency nor an Abelian-square frequency.

## Limitations
The result concerns only the standard binary Thue–Morse word and its direct-prefix curling transform, not arbitrary overlap-free words, binary substitutions, or other automatic words. The arbitrary-length error bound is \(O((1+\log N)^2)\), not a claimed sharp discrepancy order. The proof depends on the established Pansiot–Brlek square-factor classification as documented in [2]. An equivalent unpublished or unindexed derivation cannot be excluded by literature searches alone.

## References
[1] G. Caveney, H. Dong, J. Shallit, *Repetition Avoidance in Curling-Number Transforms*, arXiv:2608.15670, first public August 16, 2026. https://arxiv.org/abs/2608.15670

[2] S. Brown, N. Rampersad, J. Shallit, T. Vasiga, *Squares and overlaps in the Thue–Morse sequence and some variants*, RAIRO 40 (2006), 473–484, especially Theorem 4.1 and Lemma 4.2. https://doi.org/10.1051/ita:2006030

[3] F. J. van de Bult, D. C. Gijswijt, J. P. Linderman, N. J. A. Sloane, A. R. Wilks, *A Slow-Growing Sequence Defined by an Unusual Recurrence*, Journal of Integer Sequences 10 (2007), Article 07.1.2, §5.2. https://cs.uwaterloo.ca/journals/JIS/VOL10/Sloane/sloane55.html

[4] OEIS A093914, *Curling-number transform of the Thue–Morse sequence*, including the March 3, 2017 density observation. https://oeis.org/A093914
