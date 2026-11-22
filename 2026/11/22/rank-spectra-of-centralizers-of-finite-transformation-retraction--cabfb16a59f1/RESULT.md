# Rank spectra of centralizers of finite transformation retractions

## Finding
Let \(e\) be an idempotent full transformation of a nonempty finite set \(X\), with \(n=|X|\), \(r=|\operatorname{im}e|\), kernel blocks of sizes \(b_1,\ldots,b_r\), and \(N=n-r\). The following two finite-sum polynomials count **all transformations commuting with \(e\)** and, separately, those commuting transformations that are themselves idempotent, by image cardinality. They work for arbitrary, unequal kernel-block sizes. Their rank-one and rank-two coefficients are independent of the block-size partition once \(n\) and \(r\) are fixed, although higher coefficients need not be.

For integers \(b\geq1\), \(M\geq0\), put
\[
W_{b,M}(z)=z\sum_{h=0}^{b-1}\binom{b-1}{h}\left(\sum_{a=0}^{h}(-1)^a\binom{h}{a}(h+1-a)^M\right)z^h.
\]
For \(M\geq b-1\), put
\[
V_{b,M}(z)=z\sum_{h=0}^{b-1}\binom{b-1}{h}(h+1)^{M-h}z^h.
\]
For a map \(g:[r]\to[r]\), define \(M_j(g)=\sum_{i:g(i)=j}(b_i-1)\) and \(S(g)=\operatorname{im}g\). Then
\[
F_e(z)=\sum_{g:[r]\to[r]}\prod_{j\in S(g)}W_{b_j,M_j(g)}(z),
\]
\[
I_e(z)=\sum_{\substack{g:[r]\to[r]\\g^2=g}}\prod_{j\in S(g)}V_{b_j,M_j(g)}(z).
\]
For each \(k\in\{1,\ldots,n\}\), the coefficients \([z^k]F_e\) and \([z^k]I_e\) count, respectively, elements of \(C_{\mathcal T_X}(e)\) and idempotents in that centralizer having image size \(k\).

The low-rank laws are
\[
[z]F_e=[z]I_e=r,
\]
\[
[z^2]F_e=\binom r2(2^r-2)+N(2^N-1),
\qquad
[z^2]I_e=\binom r2 2^{r-2}+N2^{N-1}.
\]
Here any term with zero prefactor and a negative exponent is defined to be zero. Equivalently, the first term in the idempotent formula is used only when \(r\geq2\) and the second only when \(N\geq1\).

## Assumptions and scope
A full transformation is any map \(f:X\to X\); multiplication is composition. An idempotent is a map satisfying \(e^2=e\). Index the fixed roots \(\rho_j\in\operatorname{im}e\), and write \(B_j=e^{-1}(\rho_j)\). Every block \(B_j\) contains exactly one distinguished root \(\rho_j\), so \(b_j=|B_j|\geq1\) and \(\sum_jb_j=n\). The formulas are for every \(n\geq1\), every \(1\leq r\leq n\), every positive integer block composition, and every finite set of those cardinalities; no field or asymptotic assumption is imposed. Empty products equal one. Since \(g^2=g\), any \(j\in S(g)\) is fixed by \(g\), ensuring \(M_j(g)\geq b_j-1\) and nonnegative exponents in \(V\).

## Proof
**Step 1: centralizer normal form.** For any \(x\in B_i\), the equation \(fe=ef\) gives \(e(f(x))=f(e(x))=f(\rho_i)\). Applying this at \(\rho_i\) shows \(f(\rho_i)\) is a fixed root, say \(\rho_{g(i)}\), and then all \(f(B_i)\subseteq B_{g(i)}\). Conversely, any map assembled from a root map \(g:[r]\to[r]\), the forced values \(f(\rho_i)=\rho_{g(i)}\), and arbitrary nonroot values \(f(B_i\setminus\{\rho_i\})\subseteq B_{g(i)}\), commutes with \(e\). The decomposition is unique.

**Step 2: ordinary ranks.** For a fixed \(g\), the target block \(B_j\) is hit only if \(j\in S(g)\). When hit, its root is in the image, and \(M_j(g)\) independent input nonroot points may map arbitrarily into the \(b_j\) points of that target block. To have exactly \(h\) nonroot points in its image, first choose those points in \(\binom{b_j-1}{h}\) ways and apply inclusion-exclusion to the \(h\) prescribed nonroot targets, leaving \(\sum_{a=0}^h(-1)^a\binom ha(h+1-a)^{M_j(g)}\) functions. Images in different target blocks are disjoint, so image sizes add and their polynomials multiply. Summation over every \(g\) proves \(F_e\).

**Step 3: retraction ranks.** If \(f^2=f\) then the root map also obeys \(g^2=g\). For each \(j\in S(g)\), exactly \(h\) of its \(b_j-1\) nonroot points are fixed image points, chosen in \(\binom{b_j-1}{h}\) ways. All other \(M_j(g)-h\) nonroot input points have unrestricted choices among those \(h+1\) fixed points. Conversely, making these choices gives \(f^2=f\), since every point of \(\operatorname{im}f\) is fixed, and there are no images in inactive blocks. This yields \(V_{b_j,M_j(g)}\) and \(I_e\).

**Step 4: rank-one and rank-two universality.** Rank-one centralizer maps must collapse everything onto one of the \(r\) roots; all are idempotent. An ordinary rank-two map has one of two disjoint types. (A) It has two root images and no nonroot image: choose the two roots and a surjection of the \(r\) source roots onto them, giving \(\binom r2(2^r-2)\). (B) It has one root image \(\rho_j\) and one nonroot image in \(B_j\): all roots go to \(\rho_j\), choose the nonroot image in \(b_j-1\) ways, then map the \(N\) nonroot inputs to the two available images, using the nonroot at least once, giving \((b_j-1)(2^N-1)\). Summing type (B) over \(j\) uses \(\sum_j(b_j-1)=N\).

If \(f\) is also idempotent, type (A) requires its two root images fixed, and each of the other \(r-2\) source roots may choose either, giving \(\binom r2 2^{r-2}\). Type (B) requires the chosen nonroot image itself fixed, and every other nonroot input freely chooses either of the two fixed image points, yielding \((b_j-1)2^{N-1}\). This proves both laws, including the stated zero cases.

## Verification
A self-contained standard-Python checker accompanies the result as `CHECK.py`. It independently lists all functions on sets up to six points for 22 block-size profiles, filters by direct equations \(f\circ e=e\circ f\) and \(f^2=f\), computes image size, and compares every coefficient with the two finite-sum polynomials. It also checks the low-rank laws for every integer partition up to eight points having at most five blocks. All assertions pass. These finite tests provide error detection; the four-step combinatorial bijection establishes the all-size theorem.

For instance, when \((b_1,b_2,b_3)=(3,2,1)\),
\[
F_e(z)=3z+39z^2+108z^3+80z^4+20z^5+2z^6,
\quad I_e(z)=3z+18z^2+31z^3+19z^4+7z^5+z^6.
\]
For \((2,2,2)\), the rank-one and rank-two coefficients remain \(3,39\) and \(3,18\), but the ordinary rank-three count is \(78\), rather than \(108\), and the idempotent rank-three count is \(19\), rather than \(31\). This exhibits a first *possible* profile-sensitive rank, not a claim that every two distinct profiles differ there.

## Relationship to prior work
The centralizer of a finite transformation idempotent has a known characterization as a kernel-partition preserving transformation monoid with its distinguished root section preserved. Araújo and Konieczny (2003) study its automorphisms, including its rank-one and rank-two characteristic subsets. André, Araújo and Konieczny (2011) classify regular elements in related centralizers. Dolinka and East's arXiv preprint, first public on 11 July 2014, enumerates idempotents in the monoid of transformations preserving **uniform partitions**, but without requiring that a distinguished root section map into itself. Its enumeration and generating-rank results do not directly give the image-rank coefficients for the smaller centralizer of a chosen retraction. The finite sums here refine an already understood structural normal form, and the asserted contribution is specifically the two complete rank-distribution formulas and their profile-independent low-rank coefficients, not the characterization of the centralizer or its unweighted cardinality.

## Limitations
The result concerns full transformations centralizing one idempotent, not partial transformations, centralizers of arbitrary transformations, or simultaneous centralizers. No asymptotic optimality, unique historical priority, or new characterization of Green's relations is claimed. Historical literature on centralizers and transformation submonoids is substantial, and an earlier implicit enumeration could exist, including in inaccessible original sources. Independent review has not been performed.

## References
1. J. Araújo and J. Konieczny, *Automorphism groups of centralizers of idempotents*, Journal of Algebra (2003), accessible full-text transcription: https://www.academia.edu/104001601/Automorphism_groups_of_centralizers_of_idempotents
2. J. André, J. Araújo and J. Konieczny, *Regular centralizers of idempotent transformations*, Semigroup Forum (2011), accessible transcription: https://www.academia.edu/23515318/Regular_centralizers_of_idempotent_transformations
3. I. Dolinka and J. East, *Idempotent generation in the endomorphism monoid of a uniform partition*, arXiv:1407.3312v1 (11 July 2014), https://arxiv.org/abs/1407.3312 ; accessible complete HTML version: https://arxiv.org/html/1407.3312v2
4. I. Dolinka, J. East and J. D. Mitchell, *Idempotent rank in the endomorphism monoid of a non-uniform partition*, arXiv:1504.02520 (9 April 2015), https://arxiv.org/abs/1504.02520
