# Reverse border-Parikh ordering of letter frequencies in single-word avoidance

## Finding

Let \(\Sigma\) be a finite alphabet of \(q\ge3\) symbols, and let \(w\in\Sigma^m\) be a nonempty word. For each integer \(n\ge1\), let \(A_n(w)\) be all length-\(n\) words with no contiguous occurrence of \(w\). For \(a\in\Sigma\), define
\[
 p_a(w)=\lim_{n\to\infty}\frac{1}{n|A_n(w)|}\sum_{v\in A_n(w)} |v|_a.
\]
These limits exist. Let \(B(w)\) be the set of lengths \(\ell\in\{1,\ldots,m\}\) for which the prefix of \(w\) of length \(\ell\) equals its suffix of length \(\ell\); the full length \(m\) belongs to \(B(w)\). For any two distinct symbols \(a,b\), put \(d_\ell=|w_{1:\ell}|_a-|w_{1:\ell}|_b\). If every \(d_\ell\) for \(\ell\in B(w)\) vanishes, then \(p_a(w)=p_b(w)\). Otherwise, let \(\ell_*\) be the **greatest** border length with \(d_{\ell_*}\ne0\). Then
\[
 \operatorname{sgn}\bigl(p_a(w)-p_b(w)\bigr)
 =-\operatorname{sgn}(d_{\ell_*}).
\]
In particular, all \(q\) limiting frequencies equal \(1/q\) if and only if **every nonempty border prefix has equally many occurrences of every alphabet symbol**. The ordering is the reverse of the lexicographic ordering of the border-prefix Parikh vectors when the borders are read from longest to shortest.

For instance, for the ternary forbidden word `011220`, the full border has two copies of each symbol, but its length-one border is `0`. Thus \(p_0<p_1=p_2\), and the approximate values are \((0.333329517865,0.333335241068,0.333335241068)\).

## Assumptions and scope

The alphabet is finite with \(q\ge3\); symbols are drawn uniformly **conditional on avoiding one fixed contiguous forbidden word**, not stopped at the first appearance of that word. The occurrence count \(|v|_a\) is taken over the entire allowed length-\(n\) word. The statement includes constant words, singleton forbidden words, ties, and letters absent from the target. It does not assume the forbidden word is primitive or unbordered. Results for a binary alphabet, biased base measures, or multiple forbidden words are not asserted.

## Proof

**1. Weighted avoidance identity.** Set \(T(\mathbf t)=\sum_{a\in\Sigma}t_a\), \(W(\mathbf t)=\prod_{i=1}^m t_{w_i}\), and
\[
 C(z,\mathbf t)=\sum_{\ell\in B(w)}z^{m-\ell}\prod_{i=\ell+1}^{m}t_{w_i}.
\]
The full-length border contributes \(1\). Let
\[
 F(z,\mathbf t)=\sum_{n\ge0}z^n\sum_{v\in A_n(w)}\prod_{i=1}^n t_{v_i}.
\]
The marked-cluster decomposition for one forbidden word expresses a marked word as a sequence of isolated letters and overlapping clusters. A cluster begins with one marked copy of \(w\), of weight \(-z^mW\), and each subsequent marked copy overlaps the preceding copy along a proper border, contributing \(-z^{m-\ell}\prod_{i=\ell+1}^m t_{w_i}\). Summing cluster extensions gives cluster weight \(-z^mW/C\). The sequence construction therefore yields the formal power-series identity
\[
 F(z,\mathbf t)=\frac{C(z,\mathbf t)}{D(z,\mathbf t)},\qquad
 D(z,\mathbf t)=(1-zT(\mathbf t))C(z,\mathbf t)+z^mW(\mathbf t).
 \tag{1}
\]
This derivation uses ordinary overlap inclusion-exclusion; no independence assumption is made among overlapping factors.

**2. Simple dominant pole and its location.** Suppose \(m\ge2\). The length-\((m-1)\) de Bruijn presentation has every \((m-1)\)-letter word as a vertex, and an edge labeled \(a\) appends \(a\), except when it completes \(w\). Choose a symbol \(c\) distinct from both the first and last symbols of \(w\), possible since \(q\ge3\). Between any two states \(x,y\), the append sequence \(c^m y\) is an allowed path: any length-\(m\) window crossing into the run of \(c\)'s ends in \(c\), while any window crossing from the run into \(y\) begins in \(c\); neither can equal \(w\). The state \(c^{m-1}\) has a self-loop. Hence the adjacency matrix is primitive. Perron–Frobenius theory gives a simple dominant positive eigenvalue \(\lambda\), a unique dominant pole \(\rho=1/\lambda\) of \(F(z,\mathbf1)\), and analytic dependence near \(\mathbf t=\mathbf1\). At \(\mathbf t=\mathbf1\), write \(C(z)=\sum_{\ell\in B(w)}z^{m-\ell}\) and \(D(z)=(1-qz)C(z)+z^m\). We have \(D(1/q)=q^{-m}>0\) and
\[
 D(1/2)=(1-q/2)C(1/2)+2^{-m}<0,
\]
because \(q\ge3\), \(C(1/2)\ge1\), and \(m\ge2\). Thus the positive root lies strictly within
\[
 1/q<\rho<1/2.
 \tag{2}
\]
Primitivity implies it is simple. Since \(F=C/D\) has nonnegative coefficients and a simple positive pole, \(D_z(\rho,\mathbf1)<0\). Weighted transfer-matrix asymptotics identify \(p_a(w)\) with the logarithmic derivative of \(\lambda(\mathbf t)\), equivalently with the root derivative
\[
 p_a(w)=\frac{D_{t_a}(\rho,\mathbf1)}{\rho D_z(\rho,\mathbf1)}.
 \tag{3}
\]
Indeed, differentiating \(D(\rho(\mathbf t),\mathbf t)=0\) gives \(-\partial_{t_a}\log\rho =D_{t_a}/(\rho D_z)\), and dividing expected symbol counts by \(n\) eliminates the bounded coefficient prefactor.

**3. Exact border sign expression.** From \(D(\rho,\mathbf1)=0\),
\[
 1-q\rho=-\frac{\rho^m}{C(\rho)}.
\]
For each \(\ell\in B(w)\), the number of \(a\)'s in the suffix \(w_{\ell+1:m}\) is \(|w|_a-|w_{1:\ell}|_a\). Differentiating (1) and simplifying yields
\[
 D_{t_a}(\rho,\mathbf1)
 =-\rho C(\rho)+\frac{\rho^m}{C(\rho)}
  \sum_{\ell\in B(w)}\rho^{m-\ell}|w_{1:\ell}|_a.
 \tag{4}
\]
Subtracting (4) for symbols \(a,b\), equations (3)–(4) give
\[
 p_a(w)-p_b(w)=
 \frac{\rho^{m-1}}{C(\rho)D_z(\rho,\mathbf1)}
 \underbrace{\sum_{\ell\in B(w)}\rho^{m-\ell}d_\ell}_{H_{a,b}(\rho)}.
 \tag{5}
\]
The scalar outside the summation is strictly negative.

**4. Longest distinguishing border dominates.** If all border differences vanish, equation (5) gives equality. Otherwise interchange \(a,b\) if necessary so that \(d_{\ell_*}\ge1\), where \(\ell_*\) is the longest border with nonzero difference. Any shorter prefix of length \(\ell_*-j\) differs from the prefix of length \(\ell_*\) by only \(j\) letters. Hence \(d_{\ell_*-j}\ge1-j\). At most one border has any fixed length. Longer border terms are zero. Dividing \(H_{a,b}\) by its strictly positive factor \(\rho^{m-\ell_*}\) therefore gives
\[
 \frac{H_{a,b}(\rho)}{\rho^{m-\ell_*}}
 \ge1-\sum_{j=2}^{\infty}(j-1)\rho^j
 =1-\frac{\rho^2}{(1-\rho)^2}>0,
 \tag{6}
\]
using (2). In (5) the negative prefactor reverses this sign, proving the claimed comparison. The uniform-frequency equivalence follows because all pairwise differences vanish exactly when all border-prefix counts are equal for all symbols; their sum is \(1\).

**5. The length-one boundary.** If \(m=1\), avoidance excludes one symbol altogether and leaves all other \(q-1\) symbols uniformly represented. Hence its frequencies are \(0\) for the forbidden symbol and \(1/(q-1)\) for every other symbol. Its sole border is the word itself, so the same sign and uniformity conclusions hold directly.

## Verification

The included `checker.py` independently computes all symbol frequencies in two ways: numerical derivatives of the weighted border denominator and left/right Perron eigenvectors of the actual forbidden-word de Bruijn matrix. It compares the predictions for every ternary forbidden target through length five and every quaternary target through length four. The replay passed 703 targets and 3,129 symbol-pair checks, plus 135 separate finite-enumeration sanity tests. These finite tests are not offered as proofs of the universal assertion; the proof is (1)–(6). Run with `python3 checker.py` after installing the local dependencies from `requirements.txt`.

## Relationship to prior work

Bóna, Maga and Richey, *Letter frequency in shifts of finite type with one forbidden word* (first public preprint June 4, 2026), develop the forbidden-single-pattern frequency question for the **binary** alphabet using a border polynomial. A later separately available binary balanced-border resolution also concerns a single binary letter marginal. Neither reported statement gives the simultaneous rank and tie order of all \(q\) letter frequencies for \(q\ge3\). Their binary arguments are important precursors rather than being dismissed for using different terminology. The original preprint's full text was not retrievable for a final section-by-section comparison, so implicit earlier coverage remains a priority risk.

Chandgotia, Marcus, Richey and Wu, *Shifts of finite type obtained by forbidding a single pattern* (first public preprint September 13, 2024), analyze single-pattern avoidance via autocorrelation, entropy, finite graph presentations and Perron theory. Their results provide structural context and methods, but the inspected available text does not supply the pairwise reverse-border-Parikh frequency law. The Guibas–Odlyzko overlap polynomial and the Goulden–Jackson cluster method supply the standard rational enumeration tools; the new sign-dominance argument and the all-symbol ordering are the proposed extension. Earlier results for expected letter proportions **at the first occurrence** of a target concern a different stopping-time statistic, rather than the limiting frequency in long words conditioned on avoidance, and neither statement implies the other.

## Limitations

The proof needs an alphabet of size at least three; the binary case has special boundary phenomena and prior work. It assumes uniform weighting before conditioning, one forbidden contiguous pattern, and a length tending to infinity; it says nothing about nonuniform letter weights, several forbidden patterns, finite-length monotonicity, or detailed fluctuation statistics. The available full-text access to the central 2026 binary paper was incomplete, so novelty must still be independently checked before any historical-priority assertion. No independent mathematical audit is represented.

## References

1. M. Bóna, B. Maga and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655 (first public June 4, 2026). https://arxiv.org/abs/2606.06655
2. N. Chandgotia, B. Marcus, J. Richey and C. Wu, *Shifts of finite type obtained by forbidding a single pattern*, arXiv:2409.09024 (September 13, 2024); Discrete and Continuous Dynamical Systems, 48 (2026), 538–576. https://arxiv.org/abs/2409.09024
3. L. J. Guibas and A. M. Odlyzko, *String overlaps, pattern matching, and nontransitive games*, Journal of Combinatorial Theory A 30 (1981), 183–208. https://doi.org/10.1016/0097-3165(81)90005-4
4. I. P. Goulden and D. M. Jackson, *An inversion theorem for cluster decompositions of sequences with distinguished subsequences*, Journal of the London Mathematical Society, 20 (1979), 567–576. Standard cluster-method reference.
5. *Half letter frequency characterizes balanced borders*, online research dossier of a binary-only settlement; https://www.trureturing.org/research/bona-maga-richey-2026-half-frequency-balanced-borders/ (consulted November 5, 2026; claim priority remains subject to independent checking).
