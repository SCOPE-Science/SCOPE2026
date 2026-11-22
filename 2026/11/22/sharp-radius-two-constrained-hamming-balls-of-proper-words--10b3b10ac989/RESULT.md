# Sharp radius-two constrained Hamming balls of proper words

## Finding
Fix integers \(q\ge3\) and \(n\ge5\). Let \(\Sigma\) be a labeled alphabet of size \(q\), and let \(\mathcal P_{q,n}=\{x\in\Sigma^n:x_i\ne x_{i+1}\ (1\le i<n)\}\). For each \(x\in\mathcal P_{q,n}\), put
\[
B_2(x)=\{y\in\mathcal P_{q,n}:d_H(x,y)\le2\}.
\]
Then the following bounds are sharp simultaneously for every such \(q,n\):
\[
\boxed{\frac{(q-3)^2n(n-1)}2+(4q-11)n+14-3q
\ \le\ |B_2(x)|\ \le\
\frac{(q-2)^2n(n-1)}2+3q-5.}
\]
Equality on the left holds **exactly** for period-three words, \(x_i=x_{i+3}\) for \(1\le i\le n-3\), with their first three letters pairwise different; there are \(q(q-1)(q-2)\) such labeled words. Equality on the right holds **exactly** for period-two words \(x_i=x_{i+2}\) for \(1\le i\le n-2\); there are \(q(q-1)\) of them. In particular, for \(q=3\) the minimum is \(n+5\) while the maximum is \(\binom n2+4\); for every fixed \(q\ge4\) both extrema have quadratic growth in \(n\). This ternary-versus-larger alphabet difference is exact, not an asymptotic approximation.

An exact center-specific local formula holds without needing to enumerate the other words. Put \(u_i=q-|\{x_i\}\cup\{x_{i-1}:i>1\}\cup\{x_{i+1}:i<n\}|\). For \(1\le i<n\), put \(L_i=\mathbf1_{i>1}\), \(R_i=\mathbf1_{i+1<n}\), and let \(d_i\) be the number of distinct symbols in \(x_i,x_{i+1}\), together with \(x_{i-1}\) when \(i>1\) and \(x_{i+2}\) when \(i+1<n\). Define
\[
v_i=(q-1-L_i)(q-1-R_i)-q+d_i.
\]
Then
\[
\boxed{|B_2(x)|=1+\sum_{i=1}^n u_i+\sum_{\substack{1\le i<j\le n\\j\ge i+2}}u_iu_j+\sum_{i=1}^{n-1}v_i.}
\]
The middle sum is over all unordered pairs of nonadjacent positions; equivalently, \(1\le i<j\le n\) with \(j\ge i+2\). This formula evaluates a radius-two ball in linear time using a running suffix sum.

## Assumptions and scope
The alphabet is labeled; no quotient by alphabet permutations is taken. Distance is ordinary Hamming distance on words of the **same length**, and the constraint is only the absence of equal *adjacent* symbols, not a GC-content, complement, or long-hairpin restriction. Every admissible center is counted, including periodic centers. The sharp-extrema assertion assumes \(q\ge3,n\ge5\). The center-specific local formula is valid for \(q\ge2,n\ge2\).

## Proof
**Exact sphere decomposition.** There is one distance-zero output. At distance one, changing position \(i\) must avoid its old symbol and its one or two unchanged neighboring symbols. Their forbidden set has the size appearing in \(u_i\); thus there are exactly \(u_i\) outputs. For two nonadjacent changed positions \(i,j\), the constraints on replacement symbols are independent, giving \(u_iu_j\). For two adjacent changed positions \(i,i+1\), the left replacement has \(q-1-L_i\) possibilities after excluding its old symbol and (when present) the unchanged outer neighbor; the right has \(q-1-R_i\). Precisely \(q-d_i\) of those pairs assign equal replacement symbols, and must be removed. The resulting count is \(v_i\). Each resulting word has a uniquely determined changed-position set, so no output is double counted. This proves the center-specific formula for every \(q,n\) in its scope.

**Local comparisons.** Write \(b=q-3\), and define \(e_i=\mathbf1\{x_{i-1}=x_{i+1}\}\) for interior positions \(2\le i\le n-1\). Then \(u_1=u_n=b+1\) and \(u_i=b+e_i\) for interior \(i\). At the two boundary edges, \(v_1=(b+1)^2+1-e_2\) and \(v_{n-1}=(b+1)^2+1-e_{n-1}\). For an internal edge \(2\le i\le n-2\), let \(h_i=|\{x_{i-1},x_i,x_{i+1},x_{i+2}\}|-2\). Then \(v_i=b(b+1)+h_i\), and the elementary four-letter constraints give
\[
1-e_i e_{i+1}\le h_i\le (1-e_i)+(1-e_{i+1}).
\]
Indeed, two matching distance-two equalities force the pattern \(abab\) and two distinct symbols; exactly one such equality forces three distinct symbols; without either equality there are three or four distinct symbols.

**Lower bound and rigidity.** In the period-three reference word all interior \(e_i=0\) and all internal \(h_i=1\). Let \(E=\sum_{i=2}^{n-1}e_i\), let \(M=\sum_{i=3}^{n-2}e_i\), and let \(A=\sum_{i=2}^{n-2}e_ie_{i+1}\). An interior position has \(n-3\) nonadjacent partners, among them \(k_i=1\) endpoint if \(i=2\) or \(n-1\), and \(k_i=2\) endpoints otherwise. Expanding all nonadjacent products from the reference case and using \(h_i\ge1-e_ie_{i+1}\) gives
\[
|B_2(x)|-B_{\min}\ge E+b(n-3)E+\sum_{i=2}^{n-1}k_ie_i+\sum_{\substack{2\le i<j\le n-1\\j\ge i+2}}e_ie_j-e_2-e_{n-1}-A.
\]
Since \(\sum k_ie_i=e_2+e_{n-1}+2M\), the right side is \(E+2M-A+b(n-3)E\) plus a nonnegative sum. If \(E>0\), the number of consecutive pairs of ones in the binary word \(e_2\cdots e_{n-1}\) is at most \(E-1\), so the difference is strictly positive. If \(E=0\), equality requires \(h_i=1\) for every internal edge, hence \(x_{i-1}=x_{i+2}\) throughout. Those words are precisely the period-three words with three different initial symbols, and they attain the lower expression by substitution into the exact ball formula.

**Upper bound and rigidity.** In the period-two reference word all \(e_i=1\), hence every \(u_i=q-2\), while both boundary \(v\)'s equal \((q-2)^2\) and all internal \(v\)'s equal \((q-3)(q-2)\). For a general word put \(z_i=1-e_i\), \(Z=\sum z_i\), and retain \(k_i\) from above. Each missing interior equality loses one distance-one output, and loses at least \((q-2)k_i\) nonadjacent-pair outputs with the endpoints. All losses from nonadjacent pairs of interior positions are nonnegative: their contributions drop by \((q-2)(z_i+z_j)-z_iz_j\ge0\). The two boundary edges together can gain at most \(z_2+z_{n-1}\), and all internal adjacent edges together at most \(\sum_{i=2}^{n-2}(z_i+z_{i+1})\), by the upper bound on \(h_i\); the total gain is at most \(2Z\). Thus
\[
B_{\max}-|B_2(x)|\ge(q-2)\sum_{i=2}^{n-1}k_i z_i-Z.
\]
For \(q\ge4\), this is positive whenever \(Z>0\). For \(q=3\), it is at least \(\sum_{i=3}^{n-2}z_i\); if this is zero but \(Z>0\), at least one of \(z_2,z_{n-1}\) equals one. Since \(n\ge5\), these two interior positions are nonadjacent. Their joint nonadjacent-pair contribution falls strictly (by one when at least one is defective), giving the omitted strictly positive loss. Thus for all \(q\ge3,n\ge5\) equality occurs exactly when \(Z=0\), i.e., for a period-two word. Substitution yields the claimed upper expression.

**Evaluation and counts.** Evaluating the local formula at these two periodic patterns, with \(\binom{n-1}{2}\) nonadjacent position pairs, gives the displayed closed forms. Choosing the first three different symbols yields \(q(q-1)(q-2)\) minima; choosing the first two different symbols yields \(q(q-1)\) maxima. No other equality cases survive the strict inequalities above.

## Verification
The standalone `verify.py` independently enumerates output words obtained through exactly zero, one, or two changed coordinates and tests their adjacency constraint; it does not generate outputs using the local formula. It compares that count with the local expression for every proper labeled word for \((q,n)\) in \(q=3,2\le n\le9\); \(q=4,2\le n\le8\); \(q=5,2\le n\le7\); and \(q=6,2\le n\le6\). This covers **65,376** centers. For all tested \(n\ge5\), it independently checks both sharp extrema and the exact number and periodic form of equality cases. Running `python verify.py` prints `VERIFIED 65376 source words` on success. The finite tests check the formulas and equality cases on their stated finite ranges; the symbolic argument above proves the all-length result.

## Relationship to prior work
Zhu's 2024 treatment of error-correcting codes made from proper colorings studies asymptotic packing on spectral expanders and works with colorings up to relabeling. It does not determine the center-dependent radius-two ball volume on a path of labeled colors, nor its sharp period-two/period-three equality cases. The 2023 DNA-storage work of Rasool and coauthors investigates optimization of codebooks satisfying no-runlength and Hamming-distance constraints, rather than exact counts of nearby still-valid sequences. The unrestricted Hamming radius-two formula \(1+n(q-1)+\binom n2(q-1)^2\) does not imply the constrained result because forbidden adjacent repetitions create center-dependent terms. Exact local constrained-ball counts can be used, for example, as a sphere-packing input for minimum-distance-five codebooks: disjointness gives \(|C|B_{\min}\le q(q-1)^{n-1}\). This corollary is an application, not a separate theorem of optimal code size.

## Limitations
The result does not determine optimal code sizes or an entire radius-two ball-size frequency distribution, nor does it model DNA synthesis errors or guarantee biochemical properties. The full novelty search cannot rule out unindexed equivalent formulations. There is no independent mathematical audit. For \(n=2,3,4\), the exact local formula remains valid but the simultaneous uniqueness-of-extrema statement is not asserted.

## References
1. Honglin Zhu, *Sphere packing proper colorings of an expander graph*, arXiv:2405.20368, first public 2024-05-30, https://arxiv.org/abs/2405.20368.
2. A. R. Rasool et al., *Evolutionary approach to construct robust codes for DNA-based data storage*, Frontiers in Genetics 14 (2023), published 2023-03-20, https://doi.org/10.3389/fgene.2023.1158337.
3. *MSC2020, 94B25: Combinatorial codes*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?s=94B05.
