# Exact second-image entropy of synchronous Rule 110

## Finding
Let \(F\) be elementary synchronous binary Rule 110 on the bilateral full shift \(\{0,1\}^{\mathbb Z}\), and let \(Y_t=F^t(\{0,1\}^{\mathbb Z})\), with the **spatial translation** acting on each \(Y_t\). The exact second-image topological entropy is
\[
\boxed{h_{\mathrm{top}}(\sigma|_{Y_2})=\log\lambda_2,}
\]
where \(\lambda_2\in(1.85911,1.85912)\) is the largest real zero of
\[
\begin{aligned}
P_{17}(x)={}&x^{17}-5x^{16}+10x^{15}-10x^{14}+x^{13}+14x^{12}\\
&-23x^{11}+17x^{10}+x^9-16x^8+18x^7-8x^6\\
&-3x^5+6x^4-4x^3+x-1.
\end{aligned}
\]
Numerically, \(\lambda_2=1.85911406906531\ldots\) and \(h_{\mathrm{top}}(\sigma|_{Y_2})=0.62010006730078\ldots\) nats per site (\(0.89461529194976\ldots\) bits per site).

In contrast, the first image has entropy \(\log\lambda_1\), with \(\lambda_1=1.89717940106539\ldots\) the largest real root of \(x^4-2x^3+x^2-x-1\). Consequently the **second synchronous update causes a strict spatial-entropy loss**,
\[
h_{\mathrm{top}}(\sigma|_{Y_1})-h_{\mathrm{top}}(\sigma|_{Y_2})
=\log(\lambda_1/\lambda_2)=0.02026819011643\ldots>0.
\]
If \(p_t(n)\) denotes the number of distinct length-\(n\) words in \(Y_t\), the two image languages agree at every length \(0\le n\le9\), but \(p_1(10)=769\) and \(p_2(10)=768\). More generally, a fully specified twenty-state nonnegative integer matrix \(A_2\), reproducibly constructed by the included checker, satisfies \(p_2(n)=e^{\mathsf T}A_2^n\boldsymbol1\) **for every integer \(n\ge0\)**.

## Assumptions and scope
Rule 110 uses the standard Wolfram convention, with \(f(a,b,c)\) equal to bit \(4a+2b+c\) of the integer \(110\). Thus \(f=1\) on `001`, `010`, `011`, `101`, `110`, and \(f=0\) on `000`, `100`, `111`. The global map is \((Fx)_i=f(x_{i-1},x_i,x_{i+1})\). The source comprises **all two-sided binary configurations**; no spatial periodicity, finite-ring boundary condition, or probability distribution is imposed. Words are counted as distinct admissible strings, not by predecessor multiplicities. All logarithms in the theorem are natural. Entropy concerns the **spatial shift on a finite-time image**, not the entropy of the temporal map \(F\).

## Proof
**1. Exact five-input presentation.** Two synchronous steps compose to the radius-two local function
\[
g(a,b,c,d,e)=f\bigl(f(a,b,c),f(b,c,d),f(c,d,e)\bigr).
\]
For each five-letter input word \(abcde\), draw an edge from its four-letter prefix \(abcd\) to its four-letter suffix \(bcde\), labeling the edge \(g(a,b,c,d,e)\). This gives sixteen input-state vertices and exactly thirty-two labeled edges. A binary word of length \(n\) is in the language of \(Y_2\) if and only if it labels a path of \(n\) edges in this graph. Indeed, overlapping input windows are precisely the windows in an arbitrary input block of length \(n+4\); such a block always extends to a two-sided full-shift configuration. This equivalence holds for every \(n\), not just sampled lengths.

**2. Determinization and minimization.** Represent any set \(S\) of the sixteen input vertices by a sixteen-bit mask. For \(b\in\{0,1\}\), define \(\Delta(S,b)\) to be the union of the terminal vertices of all edges labeled \(b\) beginning in \(S\). Begin with the full vertex set, explore both label transitions breadth-first, and omit the empty set. Exactly **41** nonempty subsets are reachable. Every such state is accepting. Repeated refinement by the two successor-class signatures, treating a missing transition as a rejecting sink, gives precisely **20** right-language equivalence classes. The included `verify.py` reconstructs both entire transition tables from the eight bits of Rule 110, checks every class transition, and builds their \(20\)-by-\(20\) adjacency matrix \(A_2\). Each entry counts the number of distinct labels leading between two classes. The graph has 38 labeled edges, is strongly connected, and has self-loops; hence \(A_2\) is primitive. The initial state is the class containing the full input-vertex set.

**3. Infinite-word counting and entropy.** Determinism ensures that every accepted output word reaches exactly one state, so
\[
p_2(n)=e^{\mathsf T}A_2^n\boldsymbol1\qquad(n\ge0).
\]
Strong connectivity and Perron–Frobenius theory then imply \(\lim_{n\to\infty}p_2(n)^{1/n}=\rho(A_2)\), even though some states have just one outgoing label. Exact integer characteristic-polynomial computation gives
\[
\det(xI-A_2)=x^2(x-1)P_{17}(x).
\]
To isolate \(\rho(A_2)\) *without floating-point inference*, put \(v=A_2^{60}\boldsymbol1\), a strictly positive integer vector, and verify componentwise
\[
\frac{185911}{100000}v<A_2v<\frac{185912}{100000}v.
\]
Collatz–Wielandt therefore places the spectral radius strictly in this rational interval. Exact Sturm root counting finds one root of the characteristic polynomial in that interval and none above it. The Perron eigenvalue is consequently the specified largest real root of \(P_{17}\). All these finite exact checks are performed by `verify.py`, rather than assumed from the decimal approximation.

**4. Comparison with the first image.** Repeat the same method using four two-bit input states for the one-step graph. It produces seven reachable subsets, five classes, and the exact characteristic polynomial
\[
\det(xI-A_1)=(x-1)(x^4-2x^3+x^2-x-1).
\]
The graph is primitive and a second exact Collatz–Wielandt/Sturm calculation places \(\rho(A_1)\) in \((1.89717,1.89719)\). These two disjoint rational intervals establish \(h_{\mathrm{top}}(\sigma|_{Y_2})<h_{\mathrm{top}}(\sigma|_{Y_1})\) rigorously. The same deterministic transfer formulas yield equality of \(p_1(n)\) and \(p_2(n)\) for \(0\le n\le9\) and the stated strict discrepancy at length ten.

## Verification
Run `python3 verify.py` with Python 3 and SymPy (tested with version 1.14.0). It rebuilds the automata, checks the complete 41-to-20 and seven-to-five state reductions, checks strong connectivity and aperiodicity, computes both exact characteristic polynomials, certifies both Perron brackets by integer inequalities, counts all real roots above the brackets by Sturm arithmetic, and matches direct input-block enumeration for every word length from one through ten. The program also asserts the first eighteen second-image word counts
\[
(1,2,4,8,16,31,59,112,213,405,768,1451,2732,5129,9608,17970,33572,62666).
\]
The separate `independent_forward.py` uses an unrelated Boolean expression for Rule 110 and literal one- or two-pass updates of every possible finite input block to check both image word populations for lengths one through twelve. It uses no graph, matrix, or minimization routine. Finite enumeration is corroboration: the **all-length** theorem follows from the exact labeled-path equivalence and Perron–Frobenius step above.

## Relationship to prior work
De Oliveira, Ruivo, Costa, Miki and Trafaniuc (2015/2016) give the general method of composing local rules, constructing the second-time de Bruijn graph, and minimizing its process graph. Their published state-count tables include Rule 110; that graph methodology and the existence of a finite-state representation are **not** claimed as new. Their concluding section specifically distinguishes such state counts from studying growth of recognized languages. The present result evaluates a specific new natural invariant: the exact degree-seventeen Perron polynomial and strict **second-time spatial entropy** loss for Rule 110.

The 2026 exact first/second-image comparison across all elementary rules determines whether, and how early, each rule's first and second languages differ. It does not determine the exponential second-image word-growth rate: strict language inclusion alone generally does not force strict entropy inequality. The 2026 one-step image-entropy spectrum gives the first-image quartic and root but does not evaluate any second-image entropy. The Rule-110 one-step spatial zeta function concerns spatial periodic points at time one, while the 2026 sequential-update Rule-110 entropy uses a different updating scheme. The 2026 work on function production through cellular-automaton orbits treats yet another invariant. All these distinctions concern mathematical statements and implication strength, not merely differing titles.

## Limitations
This is a result for **two** synchronous steps of **Rule 110** on the **bilateral full shift**. It does not describe arbitrarily long-time images, the limiting image, temporal dynamical entropy, measures of maximal entropy, or finite cyclic-ring populations. The exact characteristic polynomial is given via an executable finite certificate; its verification requires SymPy. An unindexed earlier evaluation of the same second-image entropy cannot be excluded; full text of a broadly related 2017 follow-up on inferred cellular-automaton limit behavior was not accessible. Independent mathematical audit has not been performed.

## References
1. P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki, V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279, first online 2015-05-06. https://doi.org/10.1002/cplx.21686
2. N. Castronuovo, A. Dennunzio, L. Margara, *Computing Functions Through the Orbits of Dynamical Systems: The Case of Cellular Automata*, arXiv:2610.34096v1, first public 2026-10-25. https://arxiv.org/abs/2610.34096
3. *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata*, public record 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4
4. *Exact nineteen-value spatial image entropy spectrum of elementary cellular automata*, public record 2026-10-27. https://github.com/published-finding corpus/2026/tree/main/2026/10/27/SCOPE-exact-nineteen-value-spatial-image-entropy-spectrum-of-elementar--d4f1725c3486
5. *Exact spatial dynamical zeta function and least periods of the Rule 110 one-step image*, public record 2026-10-26. https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-exact-spatial-dynamical-zeta-function-and-least-periods-of-the-r--9af6bc7e78bc
6. *Exact one-sweep image entropy of sequential Rule 110*, public record 2026-11-17. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-one-sweep-image-entropy-of-sequential-rule-110--564cee059c2a
7. E. L. P. Ruivo, P. P. B. de Oliveira, *Inferring the Limit Behavior of Some Elementary Cellular Automata*, *International Journal of Bifurcation and Chaos* 27 (2017), 1730028. https://doi.org/10.1142/S0218127417300282
