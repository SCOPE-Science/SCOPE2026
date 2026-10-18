# Exact endpoint norms for the \(n-2,2\) Fourier block of symmetric groups

## Finding
For every integer \(n\ge4\), the full regular-representation Fourier projector \(P_n\) associated with the partition \((n-2,2)\) of the symmetric group \(S_n\) has the sharp endpoint norm
\[
\boxed{\|P_n\|_{\ell^1\to\ell^1}=\|P_n\|_{\ell^\infty\to\ell^\infty}=n(n-3)\left(r_{n-1}+\tfrac12r_{n-2}\right).}
\]
Here \(r_m\) is the proportion of permutations in \(S_m\) with no 1-cycles and no 2-cycles, and \(r_0=1\). The norm has the asymptotic \(\|P_n\|\sim\tfrac32e^{-3/2}n(n-3)\). Its irreducible character is negative exactly when there are one or two fixed points and no 2-cycles; it equals \(-1\) in both cases and is nonnegative everywhere else.

## Assumptions and scope
The group \(G=S_n\) has counting-measure sequence spaces \(\ell^p(G)\). The formula for the operator norm is unchanged by consistently choosing normalized counting measure, since domain and codomain receive the same scaling. The representation \(V^{(n-2,2)}\) has dimension \(d_n=n(n-3)/2\) for \(n\ge4\). The subspace projected onto is the full left-regular isotypic summand of dimension \(d_n^2\) inside \(\ell^2(G)\); this is not a projection on 2-element subsets of \(\{1,\ldots,n\}\). The character \(\chi_n\) is real and invariant under inversion. We define \(R_m\) to count permutations of \(m\) points with all cycles of lengths at least three, taking \(R_0=1\), and define \(r_m=R_m/m!\).

## Proof
**1. Character and isotypic kernel.** The permutation representation on unordered 2-subsets decomposes as the direct sum of the trivial representation, the standard representation, and \(V^{(n-2,2)}\). If \(F(\sigma)\) is the number of fixed points and \(T(\sigma)\) the number of 2-cycles, the 2-subset permutation character is \(\binom{F(\sigma)}2+T(\sigma)\). Subtracting the trivial character \(1\) and the standard character \(F(\sigma)-1\) gives
\[
\chi_n(\sigma)=\frac{F(\sigma)(F(\sigma)-3)}2+T(\sigma).
\]
The hook-length/dimension identity gives \(d_n=\chi_n(e)=n(n-3)/2\). The central primitive idempotent for this irreducible character is \(e_n(\sigma)=d_n\chi_n(\sigma)/n!\). Consequently \((P_nf)(g)=\sum_{h\in G}e_n(gh^{-1})f(h)\), an orthogonal idempotent with range dimension \(d_n^2\).

**2. Character sign rigidity and sharp norm.** For nonnegative integers \(F,T\), \(F(F-3)/2\) equals \(0\) for \(F=0,3\), \(-1\) for \(F=1,2\), and a nonnegative integer for \(F\ge4\). Thus \(\chi_n(\sigma)<0\) if and only if \(F(\sigma)\in\{1,2\}\) and \(T(\sigma)=0\), and each negative value is exactly \(-1\). Since \(\chi_n\) is a nontrivial irreducible character, character orthogonality with constants yields \(\sum_{\sigma\in G}\chi_n(\sigma)=0\). Therefore
\[
\sum_{\sigma\in G}|\chi_n(\sigma)|
=2\#\{\sigma\in G:\chi_n(\sigma)<0\}.
\]
Every row and column of the convolution matrix \(e_n(gh^{-1})\) has absolute sum \(d_n\sum_G|\chi_n|/n!\); these row and column sums are the exact \(\ell^\infty\)- and \(\ell^1\)-operator norms, respectively, with equality attained by the matching sign function or a point mass.

**3. Exact counting.** Permutations with exactly \(j\) fixed points and no 2-cycles are counted by \(\binom njR_{n-j}\) for \(j=1,2\). Dividing by \(n!\) gives probabilities \(r_{n-1}\) and \(r_{n-2}/2\), respectively. The preceding row-sum computation then gives
\[
\|P_n\|=2d_n\left(r_{n-1}+\tfrac12r_{n-2}\right)
=n(n-3)\left(r_{n-1}+\tfrac12r_{n-2}\right),
\]
with the asserted common endpoint value.

**4. Exact coefficients and asymptotics.** The exponential formula for permutations assembled from cycles of length at least three gives
\[
\sum_{m\ge0}\frac{R_m}{m!}z^m
=\exp\left(\sum_{j\ge3}\frac{z^j}{j}\right)
=\frac{e^{-z-z^2/2}}{1-z}
\]
for \(|z|<1\). Equivalently \(r_m=\sum_{a,b\ge0,\,a+2b\le m}(-1)^{a+b}/(a!\,2^b b!)\). As these are partial sums of the absolutely convergent double series for \(e^{-3/2}\), one gets \(r_m\to e^{-3/2}\). Substituting proves both claimed limits, including \(\|P_n\|/d_n\to3e^{-3/2}\).

## Verification
Run `python3 verify.py` using the self-contained file included with this result. Its standard-library exact-integer checks enumerate every cycle type through \(n=30\), verify the negative-support criterion, character mean zero and second moment one, and match the exact norm with two independent counts. Direct permutation enumeration for \(4\le n\le8\) independently checks the sign support. The local replay returned `VERIFY_OK exact_character_classes=28622 permutation_objects=46224 n=4..30`. These finite tests support but do not establish the all-\(n\) assertions, which follow from the displayed proof.

## Relationship to prior work
Barvinok and Stephen (2001), §6.4.2 and Proposition 7.5, explicitly give the same degree-two symmetric-group character polynomial and the no-1/2-cycle exponential generating function as separate ingredients for a quadratic-assignment value-distribution question. These inputs are **not claimed as new**. Their studied quantities concern extremal distributions of quadratic assignment functions, not the sharp \(\ell^1/\ell^\infty\) norm of the central isotypic Fourier projection; the present claim additionally identifies the complete negative character support and computes its weighted total variation. Scarabotti and Tolli (arXiv 2007; primary MSC 43A95) develop harmonic analysis of symmetric-group homogeneous spaces and explicitly decompose permutation modules involving \((n-2,2)\), but the inspected parts deal with projection formulas on coset spaces, not this regular-group isotypic norm. OEIS A214418 computes an *unweighted sum over character-table entries* and does not use conjugacy-class weights or single out the Fourier block studied here. A distinct related problem is the corresponding Johnson 2-subset projector on its much smaller homogeneous space, which has a different kernel and norm.

## Limitations
The exact formula is restricted to the full regular-representation isotypic block labeled \((n-2,2)\); it does not determine mixed-block truncations, other partitions, intermediate \(\ell^p\) operator norms, or projection norms on arbitrary homogeneous spaces. The two main combinatorial ingredients already occur in prior literature, so there is an originality risk that their endpoint-norm combination has been recorded elsewhere under Fourier-algebra or character-\(L^1\) terminology. Finite calculations are only corroborative; no claim of independent verification is made.

## References
1. A. Barvinok and T. Stephen, *The distribution of values in the quadratic assignment problem*, arXiv:math/0104229v1, first public 2001-04-24, §§6.4, 7.5, https://arxiv.org/abs/math/0104229.
2. F. Scarabotti and F. Tolli, *Harmonic analysis on a finite homogeneous space*, arXiv:math/0701533v1, first public 2007-01-19, primary MSC 43A95, §3.2, https://arxiv.org/abs/math/0701533.
3. OEIS A214418, *Sum of absolute values of the character table of the symmetric group*, https://oeis.org/A214418 (different table invariant).
