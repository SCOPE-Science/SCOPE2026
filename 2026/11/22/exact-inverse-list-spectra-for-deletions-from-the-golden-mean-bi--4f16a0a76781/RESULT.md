# Exact inverse-list spectra for deletions from the golden-mean binary language

## Finding
Let \(m,d\ge0\). For each binary received word \(y\) of length \(m\), let \(P_d(y)\) be the number of **distinct** binary length-\(m+d\) parent words that avoid the contiguous factor `11` and have \(y\) as a scattered subsequence. Write \(k=|y|_1\), let \(r\) be the number of adjacent occurrences of `11` (counted with overlaps), and set \(a=m-2k+r+1\), which is a nonnegative integer. Then, as a formal power series,

\[
\sum_{d\ge0}P_d(y)t^d=\frac{t^r(1+t)^a}{(1-t)^k(1-t-t^2)}.
\]

The right side depends only on \((m,k,r)\), not on the positions of the runs. Hence the entire fixed-deletion inverse-list spectrum can be computed by a quadratic-size enumeration of integer parameter pairs. In particular, a received word is feasible after exactly \(d\) deletions **if and only if** \(r\le d\), and it has exactly one admissible parent **if and only if** \(r=d\). These are statements about distinct parent strings, not the number of embeddings or deletion masks.

More precisely, for \(k\ge1\), the number of received words with parameters \((m,k,r)\) is

\[
H_{m,k,r}=\binom{k-1}{r}\binom{m-k+1}{k-r},
\]

where invalid binomial coefficients are zero. At \(k=0\), there is one received word and \(r=0\). Thus these binomial multiplicities together with the displayed coefficient formula specify the complete inverse-list-size distribution for every \(m,d\).

Let \(S_{m,d}\) be the number of uniquely invertible received words and \(R_{m,d}\) the number of feasible received words. With the convention that empty words are included in the generating series, define

\[
G(z,u)=\frac{1+z-uz}{1-z-z^2-uz+uz^2}.
\]

Then

\[
\sum_{m,d\ge0}S_{m,d}z^mu^d=G(z,u),\qquad
\sum_{m,d\ge0}R_{m,d}z^mu^d=\frac{G(z,u)}{1-u}.
\]

For fixed \(d\ge1\), as \(m\to\infty\), among the feasible length-\(m\) received words, the fraction uniquely invertible satisfies

\[
\frac{S_{m,d}}{R_{m,d}}=1-\frac{(3\varphi+1)d}{m}+O_d(m^{-2}),\qquad \varphi=\frac{1+\sqrt5}{2}.
\]

## Assumptions and scope
All words are indexed, linear, binary words; there is no circular wraparound. A parent avoids `11` in consecutive positions and can yield \(y\) after deleting exactly \(d\) positions. Distinct deletion masks yielding the same parent count only once. The variable \(t\) records inserted (equivalently, deleted) source symbols. The claims include \(m=0\) and \(d=0\); the ratio statement assumes a fixed positive \(d\) and \(m\to\infty\). The self-review does not imply independent validation.

## Proof
**Step 1: Canonical greedy decomposition.** Fix \(y=y_1\cdots y_m\). For every parent containing \(y\), embed \(y\) greedily from left to right, matching each required bit at its *earliest* possible occurrence. This uniquely writes the parent as \(v_1y_1v_2y_2\cdots v_my_ms\), where \(v_i\) consists only of repetitions of the bit opposite to \(y_i\), and \(s\) is the free suffix. Conversely, each such decomposition satisfying the `11` constraint yields one distinct admissible parent, with the indicated greedy embedding. This is a bijection, and avoids counting multiple deletion masks.

**Step 2: Local insertion factors.** For each required `1`, the preceding \(v_i\) is a block of zeros; its series is \((1-t)^{-1}\), except after a preceding required `1`, when at least one zero must be inserted and the series is \(t(1-t)^{-1}\). Therefore the \(k\) required ones contribute \(t^r(1-t)^{-k}\). For each required `0` preceded by a required `0` (or occurring first), the preceding \(v_i\) can be empty or contain one `1`, contributing \(1+t\); when preceded by a required `1`, it must be empty. After a final `0`, the unrestricted admissible suffix has series \((1+t)/(1-t-t^2)\). After a final `1`, that suffix has series \(1/(1-t-t^2)\), since a nonempty suffix must start with `0`. There are exactly \(m-k-(k-r-\mathbf 1_{\{y_m=1\}})+\mathbf 1_{\{y_m=0\}}=m-2k+r+1=a\) factors of \(1+t\). Their product proves the formula. For \(m=0\), the entire parent is a free suffix, giving the same formula with \(a=1\).

**Step 3: Feasibility and uniqueness.** In any admissible parent, each original adjacent `11` in \(y\) requires at least one inserted zero between the two ones, and these distinct adjacencies require distinct inserted positions. Thus \(d\ge r\) is necessary; the rational series also shows it is sufficient. If \(d=r\), its coefficient is exactly one. If \(d>r\), write \(j=d-r\ge1\). Since \(a+k=m-k+r+1\ge1\), the coefficient of \(t\) in \((1+t)^a(1-t)^{-k}\) is positive. Multiplying by the positive Fibonacci series \((1-t-t^2)^{-1}\) shows every coefficient in positive degree is at least two. This proves uniqueness precisely at \(d=r\).

**Step 4: Multiplicity of parameter types.** For \(k\ge1\), the \(k\) ones form \(k-r\) nonempty runs. Splitting \(k\) into these run lengths can be done in \(\binom{k-1}{r}\) ways. Distributing the \(m-k\) zeros into the outer gaps and the \(k-r-1\) nonempty inner gaps can be done in \(\binom{m-k+1}{k-r}\) ways. This gives the stated binomial multiplicity.

**Step 5: Joint output series and asymptotics.** The weighted enumeration of binary words by length and adjacent `11` occurrences is obtained from a two-state last-bit transfer matrix and equals \(G(z,u)\). Equivalently, with \(B(z)=1-z-z^2\), its coefficient of \(u^0\) is \((1+z)/B(z)\), while for every \(j\ge1\)

\[
[u^j]G(z,u)=\frac{z^{j+1}(1-z)^{j-1}}{B(z)^{j+1}}.
\]

By Step 3, the coefficient of \(u^d\) counts single-parent outputs, whereas summing the coefficients of \(u^0,\ldots,u^d\) counts all feasible outputs; this proves the two bivariate series. For fixed \(j\ge0\), with \(\alpha=\varphi^{-1}\), singularity analysis at the simple positive root \(\alpha\) of \(B(z)\) gives

\[
[z^m u^j]G(z,u)=c_jm^j\varphi^m(1+O_j(m^{-1})),\quad c_j=\frac{\alpha^{3j-1}}{j!(1+\alpha^2)^{j+1}}.
\]

For \(j=0\), the same leading coefficient follows directly from \((1+z)/B(z)\). For fixed \(d\ge1\), only the \(j=d\) and \(j=d-1\) layers contribute through relative order \(1/m\). Their constants have ratio \(c_{d-1}/c_d=(3\varphi+1)d\), proving the final expansion.

## Verification
The standalone Python checker `verify.py` independently constructs every admissible parent of lengths through thirteen, enumerates all possible received subsequences, and compares distinct parent counts against the closed formula in 3,066 cases covering \(0\le m\le8\), \(0\le d\le5\). It independently checks the length/weight/adjacency type multiplicities and the binary adjacent-pair generating function through length twelve. Run `python verify.py` using Python 3 standard library only. These finite calculations corroborate but do not replace the all-parameter bijective proof above.

## Relationship to prior work
Atashpendar et al. (2018, arXiv:1802.00703) develop supersequence clustering in the *unrestricted* binary deletion channel, where the number of distinct length-constrained supersequences is independent of the received word; their `singletons` mean a unique **embedding** within a parent, not a unique **parent**. The present inverse-list law imposes the golden-mean `11` prohibition and reveals exact dependence on both received-word weight and adjacent `11` count. Takemoto and Nozaki (2020, arXiv:2012.13536) develop maximum-run-limited insertion/deletion correcting code constructions, rather than counting every admissible inverse channel fiber for arbitrary deletion count. The result is therefore distinct in its object and quantified formula. It is not asserted to resolve optimal deletion-correcting code size, and it may have an equivalent formulation in uncatalogued constrained-language or subsequence-enumeration literature.

## Limitations
The rule is specific to the binary language avoiding adjacent ones; different forbidden factors require a different decomposition. The formula counts distinct potential source words, not deletion-mask multiplicities, posterior probabilities, or the optimal error-correcting code size. The asymptotic is for fixed deletion count, not for a deletion count growing with length. Search coverage cannot establish absolute novelty, and no independent mathematical audit has been performed.

## References
- A. Atashpendar, M. Beunardeau, A. Connolly, R. Géraud, D. Mestel, A. W. Roscoe, P. Y. A. Ryan, *From Clustering Supersequences to Entropy Minimizing Subsequences for Single and Double Deletions*, arXiv:1802.00703, first posted February 2, 2018. https://arxiv.org/abs/1802.00703
- R. Takemoto and T. Nozaki, *Construction and Encoding Algorithm for Maximum Run-Length Limited Single Insertion/Deletion Correcting Code*, arXiv:2012.13536, first posted December 25, 2020. https://arxiv.org/abs/2012.13536
- M. Kovačević and D. Vukobratović, *Asymptotic Behavior and Typicality Properties of Runlength-Limited Sequences*, arXiv:2105.04617, first posted May 10, 2021. https://arxiv.org/abs/2105.04617
