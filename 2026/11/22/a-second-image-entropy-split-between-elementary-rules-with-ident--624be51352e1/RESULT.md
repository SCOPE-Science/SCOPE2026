# A second-image entropy split between elementary rules with identical first-image languages

## Finding
For the standard bilateral binary elementary cellular automata of Wolfram numbers \(22\) and \(104\), let \(F_r:\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be synchronous evolution, and put \(Y_{r,t}=F_r^t(\{0,1\}^{\mathbb Z})\). Then

\[
Y_{22,1}=Y_{104,1},\qquad
Y_{22,2}\not\subseteq Y_{104,2},\qquad
Y_{104,2}\not\subseteq Y_{22,2}.
\]

Explicit cross-image witnesses are the word `10111101`, admitted by \(Y_{22,2}\) and forbidden in \(Y_{104,2}\), and the word `1010111`, admitted by \(Y_{104,2}\) and forbidden in \(Y_{22,2}\). Thus two different deterministic dynamics with **identical one-step output languages** produce incomparable spatial languages after two steps.

Their second-image spatial entropies have a certified **strict separation**:

\[
\begin{gathered}
\frac{186746}{100000}<\exp h_{\mathrm{top}}(Y_{22,2})<\frac{186748}{100000},\\
\frac{183426}{100000}<\exp h_{\mathrm{top}}(Y_{104,2})<\frac{183428}{100000}.
\end{gathered}
\]

Numerically these are \(h_{\mathrm{top}}(Y_{22,2})\approx0.62458238\) and \(h_{\mathrm{top}}(Y_{104,2})\approx0.60664624\), a strict difference of approximately \(0.01793614\) nats per spatial site. The rational intervals, not the displayed decimals, certify the ordering.

There is also a short-versus-asymptotic reversal: relative to their common first image, Rule \(22\)'s first newly forbidden words appear at length \(7\) (`1010111`, `1110101`), while Rule \(104\)'s appear only at length \(8\) (`10111101`, `11011011`). Yet Rule \(104\)'s second image has the *smaller* entropy. This compares two known types of invariant at a new common-language pair; no originality is attributed to an isolated finite-length threshold. State complementation conjugates Rule \(22\) to Rule \(151\), and Rule \(104\) to Rule \(233\), so the same entropy split applies to these two complementary rule pairs.

## Assumptions and scope
Number the eight input triples \((a,b,c)\in\{0,1\}^3\) by \(4a+2b+c\), and define \(f_r(a,b,c)\) as that indexed binary digit (least significant bit is index zero) of \(r\). Let \((F_rx)_i=f_r(x_{i-1},x_i,x_{i+1})\) for every \(i\in\mathbb Z\). All two-sided initial configurations are allowed, with no periodic ring boundary or probability measure. Spatial topological entropy here is the natural-log exponential growth rate of distinct finite output blocks under *spatial translation*, not entropy of the temporal map.

## Proof
**1. Finite graph recognizing the complete infinite spatial language.** For an integer \(t\ge1\), use all \(2^{2t}\) possible input strings of length \(2t\) as graph vertices. Each input string of length \(2t+1\) gives a directed edge from its length-\(2t\) prefix to its length-\(2t\) suffix, with label equal to the central output obtained by applying the local rule synchronously \(t\) times to that length-\(2t+1\) string. Any output word of length \(n\) labels such a path of length \(n\) if and only if it arises from an input block of length \(n+2t\). Such an input block always extends to a bilateral configuration. This proves the language characterization for **all** finite \(n\), not just for bounded enumeration.

**2. Determinization and all-length language comparisons.** Start with the full set of predecessor vertices and, for each output symbol, propagate to the union of all successor vertices along edges of that symbol. Discard the empty subset; every nonempty reachable subset is an accepting state. This is a finite deterministic automaton (DFA) for the entire image language. Rule \(22\) and Rule \(104\) each yield \(15\) reachable nonempty subsets after one update. To decide inclusion between any two languages, search the finite product of their subset DFAs and their respective empty/rejecting states. A product word reaches acceptance only on the left precisely when it is a witness to non-inclusion. Exhausting the reachable product proves absence of all such words, including at unbounded lengths. Complete product searches give **both** inclusions for the one-step images and the two explicit witnesses of opposing non-inclusion for the two-step images.

**3. Entropy matrices.** For each reachable nonempty DFA state \(S\), let \(A_{S,T}\) be the number of letters whose transition takes \(S\) to \(T\). For the initial-state row \(e\) and all-ones column \(\mathbf1\), the number of permitted output words of length \(n\) is exactly \(eA^n\mathbf1\). Since every state is reachable and accepting, standard Perron–Frobenius matrix-growth theory gives \(h_{\mathrm{top}}=\log\rho(A)\). At time \(2\), the Rule \(22\) matrix has \(360\) states, with one irreducible leading strongly connected component (SCC) of \(350\) states. All other SCCs have size one and spectral radius at most \(1\). The Rule \(104\) matrix has \(418\) states, all in its irreducible leading SCC.

**4. Exact Perron certificates.** The accompanying `spectral_witnesses.json` provides a strictly positive *integer* vector on each leading SCC. The dependency-free `verify.py` independently reconstructs the full graphs and SCCs, and checks every coordinate of the **strict rational** inequalities
\[
\begin{aligned}
(186746/100000)v_{22}&<A_{22}^{\mathrm{SCC}}v_{22}<(186748/100000)v_{22},\\
(183426/100000)v_{104}&<A_{104}^{\mathrm{SCC}}v_{104}<(183428/100000)v_{104}.
\end{aligned}
\]
The Perron–Frobenius/Collatz–Wielandt inequalities imply the asserted spectral intervals. All arithmetic in this test uses exact arbitrary-precision integers; floating-point values are illustrative only. Since \(183428<186746\), strict entropy separation follows immediately.

**5. Complements and finite observations.** Direct substitution in the eight-entry truth tables shows \(F_{151}=C\circ F_{22}\circ C\) and \(F_{233}=C\circ F_{104}\circ C\), where \((Cx)_i=1-x_i\). This implies equality of entropies for each conjugate pair. Exhaustive direct initial-block enumeration, independent of the DFA construction, confirms the four new short forbidden words above and second-image counts \(1788\) and \(1770\) at length \(11\). That enumeration corroborates but is **not** the argument for infinite-language comparisons or entropy.

## Verification
In a directory containing the complete files `verify.py` and `spectral_witnesses.json`, run `python3 verify.py` (Python standard library only). The program reconstructs each relevant local rule and the one-step and two-step predecessor-subset DFA, exhaustively decides all four relevant language inclusions, checks the stated exact SCC decomposition, and verifies both inequalities at each of the \(768\) positive-vector coordinates constituting the two rational Perron sandwiches. It independently enumerates all input blocks for both rules and both times at each output length \(0\) through \(11\), checks each enumerated word against the DFA and its exact word count, verifies the first forbidden-word sets, and verifies the conjugate truth tables. It terminates with a PASS message only if all assertions succeed. The finite exhaustive product search certifies **all** output-word lengths; independent finite-block enumeration by itself would not.

## Relationship to prior work
The 2026 published catalog *Exact nineteen-value spatial image entropy spectrum of elementary cellular automata* determines the one-update entropy spectrum and shows that Rules \(22,104,151,233\) are exactly the four maximizers among nonsurjective elementary rules; it explicitly does not evaluate iterated-image entropy. The 2026 work *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata* evaluates each rule's earliest first-versus-second image-language discrepancy, but does not compare distinct rules' two-step languages or spectral radii. The 2026 *A sharp eight-cell test for equality of cyclic image languages of elementary cellular automata* already establishes equality for Rules \(22\) and \(104\) of their one-step **cyclic ring** output languages; that is relevant precedent for, rather than an independent novelty assertion about, their shared one-step image. All three records are publicly findable in the published-finding corpus repository listed below.

De Oliveira and collaborators (2015/2016) give general finite-time process-graph constructions for elementary rules and investigate state/edge complexity, rather than this evaluated second-image entropy comparison. Kassardjian, Balbi, and Ruivo (2024/2025) extend process-graph methods and may contain related finite-time structural data, though the accessible abstract alone cannot exclude an equivalent detailed calculation. Koller and Hudcová (2025) count initial configurations leading to short temporal attractors; that object is not the image-language entropy here. **Novelty asserted here is the conjunction of second-image incomparability and a certified strict two-step entropy split for a common one-step image,** not finite graph methodology, first-image entropy, cyclic one-step equality, or the individual first-loss cutoff.

## Limitations
The theorem concerns only the one-step and two-step *spatial* images of the named elementary rules. It does not determine asymptotic temporal limit sets, ergodic measures, third-step entropy, or optimized finite-ring dynamics. The rational certificates are finite but relatively large: the principal SCCs contain \(350\) and \(418\) states. An inaccessible full 2024/2025 process-graph chapter and a 2017 limit-behavior follow-up are residual historical-priority risks; the accessible descriptions do not resolve their full contents. The proof and certificates have not undergone independent mathematical audit.

## References
1. *Exact nineteen-value spatial image entropy spectrum of elementary cellular automata*, published research record (2026), published-finding corpus public repository: https://github.com/published-finding corpus/2026
2. *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata*, published research record (2026), same public repository: https://github.com/published-finding corpus/2026
3. *A sharp eight-cell test for equality of cyclic image languages of elementary cellular automata*, published research record (2026), same public repository: https://github.com/published-finding corpus/2026
4. P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki and V. V. Trafaniuc, *Advances in the Study of Elementary Cellular Automata Regular Language Complexity*, first published online 6 May 2015, *Complexity* 21 (2016), 267–279. https://doi.org/10.1002/cplx.21686
5. L. Kassardjian, P. P. Balbi and E. Ruivo, *Extensions on the Analysis of Elementary Cellular Automata with Process Graphs*, *Journal of Cellular Automata* 18 (2024), 127–155; book version (2025). https://www.oldcitypublishing.com/journals/jca-home/jca-issue-contents/jca-volume-18-number-2-3-2024/jca-18-2-3-p-127-155/
6. C. Koller and B. Hudcová, *Counting Short Trajectories in Elementary Cellular Automata using the Transfer Matrix Method*, arXiv:2508.09768, first posted 13 August 2025. https://arxiv.org/abs/2508.09768
