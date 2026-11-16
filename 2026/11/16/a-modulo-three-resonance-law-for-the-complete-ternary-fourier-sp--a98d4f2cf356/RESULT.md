# A modulo-three resonance law for the complete ternary Fourier spectrum of cycle colourings

## Finding

For every integer \(n\ge3\), let \(C_n\) denote the simple cycle with vertex set \(\{1,\ldots,n\}\), including the edge joining \(n\) and \(1\). Let \(G_n=(\mathbb Z/3\mathbb Z)^n\), and let \(f_n:G_n\to\{0,1\}\) indicate the proper three-colourings of \(C_n\). Write \(\omega=\exp(2\pi\mathrm i/3)\). The unnormalized Fourier multiplier at frequency \(k=(k_1,\ldots,k_n)\in G_n\) is
\[
W_n(k)=\sum_{x\in G_n}f_n(x)\,\omega^{\sum_{j=1}^n k_jx_j}.
\]

When \(\sum_j k_j\not\equiv0\pmod3\), the multiplier is zero. For balanced frequencies \(\sum_jk_j\equiv0\pmod3\), define \(b_i=\sum_{j=i+1}^n k_j\pmod3\), including \(b_n=0\), and put \(c_r=|\{i:b_i=r\}|\) for \(r\in\{0,1,2\}\). Then the **complete Fourier formula** is
\[
\boxed{W_n(k)=(-1)^n\bigl((-2)^{c_0}+(-2)^{c_1}+(-2)^{c_2}\bigr).}
\]
The histograms are nonnegative triples with \(c_0+c_1+c_2=n\) and \(c_0\ge1\). Each such ordered triple produces exactly
\[
\frac{(n-1)!}{(c_0-1)!\,c_1!\,c_2!}
\]
balanced frequencies. Therefore the formula specifies the complete Fourier multiplier multiset, with coincident numeric values counted by addition of their multiplicities.

**Exact resonance and rank.** In the balanced sector, \(W_n(k)=0\) holds **if and only if** the multiset \(\{c_0,c_1,c_2\}\) has form \(\{a,a,a+1\}\) for an integer \(a\ge1\). Equivalently, additional zeros exist exactly when \(n\equiv1\pmod3\). The number of these extra balanced zeros is
\[
Z_n=\begin{cases}
\displaystyle\frac{(3a+1)!}{(a+1)!\,(a!)^2},&n=3a+1,\quad a\ge1,\\[4pt]
0,&n\not\equiv1\pmod3.
\end{cases}
\]
Consequently, counting convolution \(T_n:g\mapsto f_n*g\) on \(G_n\) has exact rank
\[
\boxed{\operatorname{rank}(T_n)=3^{n-1}-Z_n.}
\]
Equivalently, it is invertible on the globally colour-translation-invariant subspace precisely when \(n\not\equiv1\pmod3\). Along the resonant subsequence its fractional balanced nullity satisfies
\[
\frac{Z_n}{3^{n-1}}\sim\frac{9\sqrt3}{2\pi n}\qquad(n\to\infty,\ n\equiv1\pmod3).
\]

## Assumptions and scope

The group law and characters are those of \(\mathbb Z/3\mathbb Z\), not the labels of three unstructured colours. The colouring constraint means every pair of adjacent vertices has distinct colours. Frequency balance and the suffix sums are taken modulo three; the exponent of \((-2)\) is an ordinary integer. Fourier transforms and convolution are **unnormalized**; the stated rank does not depend on a nonzero common transform normalization. The rank is over \(\mathbb C\) (and equals the real rank of the real counting-convolution matrix). A balanced frequency is precisely a character invariant under diagonal translation \(x\mapsto x+t(1,\ldots,1)\).

## Proof

**Step 1: global colour translation.** A diagonal shift by \(t\in\mathbb Z/3\mathbb Z\) preserves proper colourings. It multiplies the character at \(k\) by \(\omega^{t\sum_j k_j}\), so a nonbalanced character sum vanishes.

**Step 2: introduce edge increments.** For a proper colouring, put \(d_i=x_{i+1}-x_i\) for \(i<n\) and \(d_n=x_1-x_n\), all modulo three. Every \(d_i\) belongs to \(\{1,-1\}\), and \(\sum_i d_i=0\). Conversely, any such closed increment word and one choice of \(x_1\) determine a unique proper colouring. For balanced \(k\), the character exponent becomes \(\sum_{i=1}^{n-1}b_i d_i\), with \(b_n=0\). The three initial colours contribute a factor of three. Insert the identity
\[
\mathbf1_{\{\sum_i d_i=0\}}=\frac13\sum_{t=0}^2\omega^{t\sum_i d_i}.
\]
The two factors of three cancel, giving
\[
W_n(k)=\sum_{t=0}^2\prod_{i=1}^n\bigl(\omega^{b_i+t}+\omega^{-(b_i+t)}\bigr).
\]
The parenthesis is \(2\) when \(b_i+t=0\) and \(-1\) otherwise. The product is therefore \((-1)^n(-2)^{c_{-t}}\), proving the displayed Fourier formula. For balanced \(k\), the map \(k\mapsto(b_1,\ldots,b_{n-1})\) is bijective onto \((\mathbb Z/3\mathbb Z)^{n-1}\), because \(k_1=-b_1\) and \(k_i=b_{i-1}-b_i\) for \(i\ge2\). Since \(b_n=0\), the multinomial multiplicity follows.

**Step 3: classify cancellations.** Sort the three nonnegative histogram exponents as \(a\le b\le c\). If \(a<b<c\), then \(2^c\ge2^{b+1}>2^b+2^a\), so their signed powers cannot sum to zero. If \(a<b=c\), the two largest powers have the same sign and exceed the third in magnitude. If \(a=b=c\), three equal signed powers do not cancel. Thus cancellation requires \(a=b<c\), and the equation \(2(-2)^a+(-2)^c=0\) forces \(c=a+1\). Conversely those exponents do cancel. Because \(n\ge3\), this requires \(a\ge1\) and \(n=3a+1\).

**Step 4: count the zero frequencies.** If \(n=3a+1\), the histograms in the order \((c_0,c_1,c_2)\) are permutations of \((a+1,a,a)\). The case with \(c_0=a+1\) contributes \((3a)!/(a!)^3\) frequencies. The two cases with \(c_0=a\) contribute \(2(3a)!/((a-1)!a!(a+1)!)\). Adding and simplifying gives \(Z_n=(3a+1)!/((a+1)!(a!)^2)\). If \(n\not\equiv1\pmod3\), the classification gives no balanced zeros. Standard diagonalization of convolution by the finite abelian Fourier basis gives rank equal to the number of nonvanishing multipliers, hence \(3^{n-1}-Z_n\).

**Step 5: asymptotic.** Stirling's factorial formula gives \((3a)!/(a!)^3\sim\sqrt3\,3^{3a}/(2\pi a)\). Multiplying by \((3a+1)/(a+1)\) and dividing by \(3^{3a}\) yields \(Z_n/3^{n-1}\sim3\sqrt3/(2\pi a)\sim9\sqrt3/(2\pi n)\).

## Verification

Two independently structured exact-arithmetic programs are provided. `verify_colours.py` exhaustively enumerates proper three-colourings and computes every Fourier coefficient in the Eisenstein integer basis \(1,\omega\) for \(3\le n\le7\). `verify_transfer.py` independently computes coefficients by a three-state trace transfer, accumulating exponent residues in integer triples, for the same complete range. Both compare every result with the formula and verify the exact balanced-zero count. Run both using Python 3: `python3 verify_colours.py` and `python3 verify_transfer.py`. The finite computations corroborate but are not the proof of the all-order statement; the algebraic proof above supplies all quantifiers.

The basic checks include \(n=3\): six proper colourings and rank \(9\); \(n=4\): eighteen colourings, twelve additional balanced zeros and rank \(15\); \(n=5\): thirty colourings and rank \(81\); \(n=6\): sixty-six colourings and rank \(243\); \(n=7\): 126 colourings, 210 additional balanced zeros and rank \(519\).

## Relationship to prior work

The zero-field chromatic/Potts relation and the unweighted cyclic count \(2^n+2(-1)^n\) are classical. Sokal (2005) presents Potts and flow representations and explicitly treats cycles; Ellis-Monaghan and Moffatt (2010) formulate vertex-dependent Potts external fields; Babson and Beck (2012) use Fourier analysis to count group-valued graph colourings. The present statement is the **explicit entire vertex-character Fourier multiset**, its cancellation histogram, and exact convolution rank, rather than a total-colouring count or general evaluation framework. A published study titled *Sharp universal Fourier sampling stability on proper colourings of cycles* determines the degree-one **sampling Gram** spectrum and explicitly restricts its scope to that first band; it does not imply the full characterwise zero classification and rank of counting convolution. Such problems use different matrices even though both start from the same colouring set.

## Limitations

The statement treats only the three-colour alphabet and a single simple cycle. The formula does not imply corresponding resonance for larger palettes, arbitrary graphs, or nonabelian colour spaces. There may be prior unindexed vertex-weighted chromatic formulas equivalent to the simple three-power cancellation criterion; the literature comparison is bounded and historical priority remains subject to independent scrutiny. No independent mathematical validation is asserted.

## References

1. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1 (first submitted 2005-03-25), https://arxiv.org/abs/math/0503607.
2. J. A. Ellis-Monaghan and I. Moffatt, *The Tutte-Potts connection in the presence of an external magnetic field*, arXiv:1005.5470v1 (first submitted 2010-05-29), https://arxiv.org/html/1005.5470v2.
3. E. Babson and M. Beck, *Counting Group Valued Graph Colorings*, arXiv:1204.1283v1 (first submitted 2012-04-05), https://arxiv.org/abs/1204.1283.
4. R. Shrock and Y. Xu, *Exact Results on Potts Model Partition Functions in a Generalized External Field and Weighted-Set Graph Colorings*, arXiv:1009.1182v1 (first submitted 2010-09-07), https://arxiv.org/abs/1009.1182.
5. *Sharp universal Fourier sampling stability on proper colourings of cycles*, publicly available research note, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-sharp-universal-fourier-sampling-stability-on-proper-colourings--8dc8f90856db (read for the exact claim and its explicit degree-one scope).
