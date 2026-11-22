# The exact two-step image and density spectrum of cyclic traffic Rule 184

## Finding
For each integer \(n\ge1\), let \(F_n\) be synchronous elementary cellular automaton Rule 184 on the indexed binary ring of length \(n\), and let \(R_{n,k}\) be the number of *distinct* outputs after two updates having \(k\) ones. The complete two-step image has the forbidden-factor description
\[
 F_n^2(\{0,1\}^n)=\{y\in\{0,1\}^n:\text{neither `1100' nor `110100' occurs cyclically in }y\}.
\]
If \(G_n\) is the reflected traffic Rule 226, then every such output has the explicit two-step predecessor \(G_n^2(y)\):
\[
 F_n^2(G_n^2(y))=y.
\]
Moreover, the entire length-and-particle-number distribution is
\[
\boxed{\sum_{n\ge1}\sum_{k=0}^nR_{n,k}z^nu^k
 =\frac{(1+u)z-4u^2z^4-6u^3z^6}{1-(1+u)z+u^2z^4+u^3z^6}.}
\]
For binomial coefficients outside their natural ranges interpreted as zero, the exact coefficient formula is
\[
\boxed{R_{n,k}=n\sum_{\substack{a,b\ge0\\4a+6b\le n}}(-1)^{a+b}
 \frac{(n-3a-5b-1)!}{a!\,b!\,(n-4a-6b)!}
 \binom{n-4a-6b}{k-2a-3b}.}
\]
The first totals \(\sum_kR_{n,k}\) for \(n=1,\ldots,12\) are \(2,4,8,12,22,34,58,100,170,294,508,882\). The first additional obstruction beyond the one-step image occurs at \(n=6\), excluding exactly the six cyclic rotations of `110100`.

Put \(\lambda=1.75487766624669\ldots\), the largest real root of \(\lambda^3-2\lambda^2+\lambda-1=0\). Then
\[
\sum_kR_{n,k}\sim\lambda^n,
\qquad \lim_{n\to\infty}\frac{\log_2\sum_kR_{n,k}}n=\log_2\lambda=0.81137046275\ldots.
\]
This is a strictly smaller finite-time spatial output rate than the one-step value \(0.87914642160\ldots\) bits per site.

## Assumptions and scope
All ring indices are in \(\mathbb Z/n\mathbb Z\), including when \(n<6\) so cyclic factors may revisit positions. A binary word is counted with its coordinate labels; rotating it generally gives a different word. With Boolean bits \(a,b,c\), define
\[
 f(a,b,c)=a(1-b)+bc,\quad g(a,b,c)=c(1-b)+ba,
 \qquad (F_nx)_i=f(x_{i-1},x_i,x_{i+1}),\quad (G_nx)_i=g(x_{i-1},x_i,x_{i+1}).
\]
The summands in each displayed local rule are disjoint, and updates occur simultaneously. \(F_n^2\) means exactly two updates from an arbitrary binary input, not an eventual attractor; \(u\) records the number of ones in a *distinct output*, not its number of predecessors. All formulas quantify over every \(n\ge1\) and \(0\le k\le n\).

## Proof
**1. One-step local inverse and obstruction.** Checking all \(32\) five-bit contexts \(abcde\) establishes the exact discrepancy set
\[
\{abcde:f(g(a,b,c),g(b,c,d),g(c,d,e))\ne c\}=
\{01100,11000,11001,11100\}.
\]
Each discrepancy contains `1100`, so \(F_nG_n(y)=y\) whenever \(y\) avoids cyclic `1100`. For necessity, checking all \(64\) six-bit inputs to the four consecutive instances of \(f\) shows that `1100` is not an output block. Hence every \(F_n\)-image avoids `1100`. These finite truth-table lemmas and their periodic reuse are also established in the prior one-step Rule-184 image literature, and are independently reproduced by `verify.py`.

**2. Necessity of the new six-bit obstruction.** Suppose \(y=F_n(F_n(x))\), and write \(w=F_n(x)\). Since \(y\) is an \(F_n\)-image it avoids cyclic `1100`. If \(y\) contains cyclic `110100`, then its eight-bit preimage context in \(w\) must be among precisely

`01110000`, `01110001`, `01110010`, `10110000`, `10110001`, `10110010`, `11110000`, `11110001`, `11110010`.

This is an exhaustive \(256\)-case local check using the displayed \(f\). Every listed context contains `1100`, contradicting the one-step image obstruction for \(w\). Therefore no two-step image contains either forbidden factor. Repeated-index windows when \(n<8\) are already included in the necessity argument.

**3. Constructive sufficiency.** A complete check of the \(64\) six-bit contexts in the reflected rule \(g\) proves that the four consecutive \(g\)-outputs are `1100` **if and only if** the six input bits are `110100` or `111000`. Since `111000` itself contains `1100`, any circular word \(y\) avoiding both stated factors has \(G_n(y)\) avoiding `1100` as well. Applying Step 1 first to \(y\) and then to \(G_n(y)\),
\[
 F_nG_n(y)=y,\qquad F_nG_n(G_n(y))=G_n(y),
\]
so \(F_n^2G_n^2(y)=y\). This gives an explicit full-ring antecedent for every allowed \(y\), including the short rings, and completes the exact-image characterization.

**4. Six-state weighted transfer and complete density spectrum.** The complete proper-prefix set for the forbidden factors is, in this order,

`ε`, `1`, `11`, `110`, `1101`, `11010`.

At each bit, update to the longest suffix equal to one of these prefixes, but reject any transition completing `1100` or `110100`. Give transitions labeled `0` weight \(1\), and those labeled `1` weight \(u\). The resulting transfer matrix is
\[
 T(u)=\begin{pmatrix}
 1&u&0&0&0&0\\
 1&0&u&0&0&0\\
 0&0&u&1&0&0\\
 0&0&0&0&u&0\\
 0&0&u&0&0&1\\
 0&u&0&0&0&0
 \end{pmatrix}.
\]
A cyclic forbidden-factor-avoiding word has one and only one periodic path in this deterministic suffix automaton: the current state is determined by at most five symbols immediately preceding the current cut in its two-sided periodic repetition. Conversely, every closed path avoids the forbidden factors. This remains true even for words shorter than the state-memory length because their periodic repetitions determine the state. Hence
\[
 \sum_{k=0}^nR_{n,k}u^k=\operatorname{tr}(T(u)^n),\quad n\ge1.
\]
Exact determinant expansion yields
\[
 D(z,u)=\det(I-zT(u))=1-(1+u)z+u^2z^4+u^3z^6.
\]
The formal identity \(-z\partial_z\log D=\sum_{n\ge1}\operatorname{tr}(T(u)^n)z^n\) proves the rational generating function. To extract coefficients, expand \(-\log D=\sum_{m\ge1}((1+u)z-u^2z^4-u^3z^6)^m/m\). Select \(a\) copies of \(-u^2z^4\), \(b\) copies of \(-u^3z^6\), and \(c=n-4a-6b\) copies of \((1+u)z\); then \(m=n-3a-5b\). Differentiating by \(z\), the multinomial factor is \(n(m-1)!/(a!b!c!)\), and extracting \(u^k\) gives the displayed exact finite double sum. No convergence or numerical extrapolation is used.

**5. Rate and sharp first loss.** At \(u=1\), the reciprocal characteristic polynomial is \(x^6-2x^5+x^2+1=(x^3-x-1)(x^3-2x^2+x-1)\). Its unique largest-modulus root is \(\lambda=1.7548776662\ldots\), strictly greater in modulus than the other five roots (whose moduli are below \(1.325\)); its multiplicity is one. The trace expression therefore gives \(\sum_kR_{n,k}\sim\lambda^n\) with leading coefficient one. The one-step growth constant is the larger tribonacci root \(1.8392867552\ldots\). For \(n<6\), cyclic `110100` cannot occur without already creating cyclic `1100`; for \(n=6\), its six rotations are distinct, allowed after one step, and forbidden after two. This proves the sharp first-loss statement.

## Verification
`verify.py` (Python 3 standard library) independently enumerates the 32 and 64 local contexts in the inverse tests, the 256 contexts in the second-step obstruction, and computes the entire six-by-six determinant exactly as a bivariate integer polynomial via a 720-permutation expansion. It directly groups \(F_n^2\)-outputs and tests the constructive \(G_n^2\) antecedent for every allowed circular word at lengths \(1\) through \(13\). It compares every fixed-density coefficient with independent transfer traces and the finite double sum through length \(15\), and checks exact symbolic recurrences through length \(23\). Execute `python3 verify.py` beside this file; success prints `VERIFY_OK`. These finite tests corroborate the complete local lemmas and transfer proof; finite enumeration alone is not a proof of the infinite-length formulas.

## Relationship to prior work
A prior one-step Rule-184 image theorem gives exact cyclic `1100` avoidance, a reflected Rule-226 section, and a complete one-step weight-resolved count. Those are reused as known inputs, not claimed as contributions. De Oliveira, Ruivo, Costa, Miki and Trafaniuc (2015/2016) published an **exact finite-state process graph for the second Rule-184 image** (their Figure 8), together with general methods for computing finite-time image languages and graph-complexity data. Thus the *existence of a full finite-state representation for the two-step infinite-configuration language is prior coverage* and one can in principle recover its finite factors from their graph. This does **not** automatically imply that every admissible periodic word has an antecedent of the **same period**: a finite labeled path need not lift to a closed predecessor walk. The explicit same-ring section above resolves that periodic-lifting issue for all lengths. The present claim is the explicit short forbidden-basis characterization with a uniform two-step local section and, most importantly, the closed **all-ring-length, particle-number-refined rational and binomial enumeration and its exact entropy decrease**, neither of which was supplied in their inspected statement. The generic transfer and determinant tools are not claimed to be new. There is a residual priority risk that algebraic simplification of the already published process graph, or another unindexed source, may give an equivalent exact enumeration.

A separate published exhaustive 256-rule result establishes that first and second image languages for Rule 184 differ already at length six; it does not give this all-length language, explicit inversion or mass-resolved generating function. Classical traffic-flow papers and finite-time CA complexity studies motivate the model but principally address dynamics, flux, growth of state graphs, or limiting language, rather than this precise enumerative invariant.

## Limitations
Only two synchronous steps on fully periodic indexed binary rings are considered. Nothing is claimed about open boundary conditions, stochastic traffic, arbitrary update depth, inverse-fiber sizes, or relaxation time distributions. The short forbidden-basis characterization of the bilateral image can in principle be computed from previously published process graphs; those graphs do not by themselves establish equal-period predecessor lifting, nor the exact ring density enumerator. Historical originality of the combined periodic theorem is nevertheless qualified, and independent assessment is still needed. All computations use the included reproducible script; the infinite-length theorem rests on the exact local and algebraic arguments, not finite tests.

## References
1. P. P. B. De Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki and V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, first online 2015-05-06, especially §§3–4 and Figures 8–12, https://doi.org/10.1002/cplx.21686 .
2. K. Higashi, J. Satsuma and T. Tokihiro, *Rule 184 fuzzy cellular automaton as a mathematical model for traffic flow*, arXiv:2004.05294, first public 2020-04-11, https://arxiv.org/abs/2004.05294 .
3. H. Fukś and S. Abeykoon Mudiyanselage, *Deterministic cellular automata resembling diffusion*, arXiv:2108.08353, first public 2021-08-18, https://arxiv.org/abs/2108.08353 .
4. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, arXiv:comp-gas/9703001, first public 1997-03-07, https://arxiv.org/abs/comp-gas/9703001 .
5. *Exact one-step reachability, inversion, and density spectrum of the cyclic traffic automaton* (2026), full mathematical statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-one-step-reachability-inversion-and-density-spectrum-of-th--5a87e3038c99 .
6. *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata* (2026), full mathematical statement, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4 .
