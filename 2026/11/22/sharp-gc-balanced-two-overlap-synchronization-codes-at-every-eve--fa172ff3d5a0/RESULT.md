# Sharp GC-balanced two-overlap synchronization codes at every even length

## Finding

Let \(\Sigma=\{A,T,C,G\}\), and put \(G=\{C,G\}\). For every even integer \(n\ge4\), let \(M_n\) be the maximum size of a code \(\mathcal C\subseteq\Sigma^n\) such that each word has exactly \(n/2\) letters in \(G\), and no prefix of length one or two of any codeword is the suffix of length one or two of any (possibly identical) codeword. Then

\[
\boxed{M_n=2^{n-4}\left[20\binom{n-4}{(n-4)/2}+16\binom{n-4}{(n-6)/2}\right],}
\]

where a binomial coefficient with a negative lower index is zero. Exactly twelve labeled codebooks attain this maximum, for every such \(n\). In particular, \(M_4=20\), \(M_6=224\), \(M_8=2944\), and \(M_{10}=40960\). Relative to the total \(2^n\binom{n}{n/2}\) GC-balanced words, the optimal code density converges to \(9/64\).

## Assumptions and scope

Words and codebooks are indexed and labeled, not quotiented by rotations, reversal, or Watson–Crick complementation. GC balance is an *exact global count*, not a sliding-window constraint. Only overlaps of lengths \(1\) and \(2\) are forbidden. For \(n>4\), longer overlaps may remain. The statement does not require strand closure, homopolymer avoidance, or any error-correcting Hamming distance.

Use the coding \(A=0,T=1,C=2,G=3\), so symbols \(2\) and \(3\) contribute one GC unit. A two-letter prefix set \(P\subseteq\Sigma^2\) and suffix set \(S\subseteq\Sigma^2\) are *compatible* if \(P\cap S=\varnothing\), and the sets \(I\) of first letters of \(P\) and \(J\) of last letters of \(S\) are disjoint. The saturated code for \((P,S)\) comprises every exactly balanced word whose first and last two symbols belong respectively to \(P\) and \(S\).

## Proof

**1. Exhaustive boundary reduction.** Any nonempty admissible code determines disjoint sets \(I\) and \(J\) of first and last symbols (from the forbidden length-one overlap), and disjoint sets \(P\) and \(S\) of its two-letter prefixes and suffixes (from the forbidden length-two overlap). Saturating \(P\times\Sigma^{n-4}\times S\) with all balanced completions cannot create a forbidden overlap and cannot reduce the code size. For fixed nonempty disjoint \(I,J\), every prefix-only eligible pair in \(I\times\Sigma\setminus(I\times J)\) and every suffix-only eligible pair in \(\Sigma\times J\setminus(I\times J)\) can be added to its corresponding boundary set. Each of the \(|I||J|\) shared pairs in \(I\times J\) can be assigned to prefixes or suffixes, never both; an unused shared pair can also be assigned without decreasing size. Thus every code is dominated by one of exactly 280 elementary templates, indexed by a three-way assignment of each of the four symbols to \(I\), \(J\), or neither, with \(I,J\ne\varnothing\), and a binary assignment of each shared pair.

**2. A finite, parameter-independent certificate.** For each template define \(f_j\), \(0\le j\le4\), as the number of quadruples \((a,b,c,d)\in P\times S\) having exactly \(j\) GC symbols. Direct exhaustion of the 280 assignments establishes all three inequalities

\[
f_2\le20,\qquad f_1+f_2+f_3\le36,\qquad\sum_{j=0}^{4}f_j\le36.
\]

The complete finite enumeration, with exact integer assertions and no external solver, is in `verify.py`. This is a finite certificate for four-letter *boundaries*, not an unverified extrapolation over input lengths. It also finds exactly twelve templates with \(f_2=20\) and \(f_1+f_2+f_3=36\), all having \((f_0,f_1,f_2,f_3,f_4)=(0,8,20,8,0)\). These twelve have different saturated balanced codebooks (checked directly at lengths four and six). Their profiles have \(f_0=f_4=0\), so every permitted boundary quadruple can be completed to a balanced word at every larger even length; thus distinct boundaries stay distinguishable.

**3. All-length bound.** Put \(L=n-4\), \(h=L/2\). Each internal word of length \(L\) with exactly \(k\) GC letters has \(2^L\binom{L}{k}\) realizations. Consequently a template with profile \((f_j)\) has exactly

\[
N_n(f)=2^L\sum_{j=0}^{4} f_j\binom{L}{n/2-j}
\]

balanced codewords. Normalize by \(2^L\binom{L}{h}>0\), and let \(r_1=L/(L+2)\) and \(r_2=L(L-2)/((L+2)(L+4))\) (both zero where the corresponding lower binomial index is negative). For even \(L\ge0\), \(0\le r_2\le r_1<1\), and the normalized count equals

\[
\begin{aligned}
&f_2+r_1(f_1+f_3)+r_2(f_0+f_4)\\
&=(1-r_1)f_2+(r_1-r_2)(f_1+f_2+f_3)+r_2\sum_{j=0}^{4}f_j\\
&\le20(1-r_1)+36(r_1-r_2)+36r_2=20+16r_1.
\end{aligned}
\]

**4. Attainment.** Let

\[
P=(\{A\}\times\Sigma)\cup(\{T\}\times\{A,T\}),\qquad
S=\{T,C,G\}\times\{C,G\}.
\]

Then \(P\cap S=\varnothing\), its first symbols are \(\{A,T\}\), and its final symbols are \(\{C,G\}\). The boundary enumerator factors as \((4+2z)(2z+4z^2)=8z+20z^2+8z^3\), giving equality in the preceding bound at every even \(n\ge4\). The strict positive coefficient \(1-r_1\) and, when \(n>4\), \(r_1-r_2\), force every maximizing template to appear among the twelve identified in Step 2. Any optimal code must equal its saturated completion. These give exactly twelve labeled maxima.

Finally \(\binom{n-4}{(n-4)/2}/\binom n{n/2}\to1/16\) and \(r_1\to1\), so division by the total \(2^n\binom{n}{n/2}\) balanced words gives the asserted density limit \((1/16)(1/16)(36)=9/64\).

## Verification

Run `python3 verify.py` using Python 3 standard library. The checker enumerates every permitted boundary template, asserts the exact number 280 and all three coefficient maxima, identifies the twelve optimizer templates, verifies the formula for even lengths four through twenty-six, and independently counts actual balanced words for each template at lengths four and six. No extrapolation from these finite length checks is used: the all-length proof is the coefficient comparison in Step 3. Expected certificate summary: 280 templates; maxima \((20,36,36)\); twelve extremizers; all checks PASS.

## Relationship to prior work

Cai, Wang and Feng obtained the unrestricted \(q\)-ary two-overlap optimum \(S_1^2(q,n)\), which for \(q=4\) equals \(36\cdot4^{n-4}\); the global exact half-GC constraint is not present in that statement. Stanovnik discusses the unrestricted theory and the reduction from long blocks to four-letter boundaries, but does not state a sharp GC-balanced all-even-length value or equality census. Wang, Fang and Feng investigate balanced restricted-overlap codes and provide bounds and constructions in the accessible article material; the complete paper was not available for line-by-line comparison, so undiscovered coverage there is a residual priority risk. A known length-four GC-balanced non-overlapping optimum of twenty words, with twelve extremizers, agrees with the \(n=4\) case; the all-even-length \((1,2)\)-overlap theorem, including the values at \(n\ge6\), is not implied by that isolated four-mer result. The later Yang–Ding paper treats unbalanced construction sizes, not this global GC composition optimization.

## Limitations

This theorem addresses exact half-GC content and two short forbidden overlaps only. It does not supply bounds for full non-overlap at lengths greater than four, other weight proportions, arbitrary alphabets, reverse-complement requirements, or Hamming-error correction. Its novelty assessment is based on identifiable prior claims and inspected sources, not an independent priority certification; one closely related restricted-overlap article's entire full text was inaccessible.

## References

1. L. Stanovnik, *Codes with restricted overlaps: expandability, constructions, and bounds*, arXiv:2411.02899, first public version 2024-11-05. https://arxiv.org/abs/2411.02899
2. Q. Cai, X. Wang and T. Feng, *Constructions and bounds for q-ary (1,k)-overlap-free codes*, IEEE Transactions on Information Theory 70 (2024), 4439–4444. https://doi.org/10.1109/TIT.2023.3319010
3. X. Wang, Y. Fang and T. Feng, *q-ary (1,k)-overlap-free codes with given restrictions*, Discrete Mathematics 348 (2025), 114236. https://doi.org/10.1016/j.disc.2024.114236
4. H. Yang and Y. Ding, *Q-Ary (t1,t2)-Overlap-Free Codes*, IEICE Transactions on Fundamentals E109.A (2026), 757–762. https://doi.org/10.1587/transfun.2025EAL2050
