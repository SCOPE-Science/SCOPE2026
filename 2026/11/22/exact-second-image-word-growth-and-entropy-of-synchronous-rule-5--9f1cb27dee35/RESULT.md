# Exact second-image word growth and entropy of synchronous Rule 54

## Finding
Let \(F\colon\{0,1\}^{\mathbb Z}\to\{0,1\}^{\mathbb Z}\) be the synchronous elementary cellular automaton Rule 54, with local function
\[
f(a,b,c)=\left\lfloor\frac{54}{2^{4a+2b+c}}\right\rfloor\bmod2.
\]
For each integer \(n\ge0\), let \(c_n\) count the distinct length-\(n\) spatial words appearing in \(F^2(\{0,1\}^{\mathbb Z})\), and set \(C(z)=\sum_{n\ge0}c_nz^n\). Then
\[
\boxed{C(z)=\frac{1-2z+2z^2-z^3-z^5+2z^7-2z^8-3z^9+5z^{10}-2z^{11}-2z^{12}+3z^{13}}{1-4z+6z^2-5z^3+2z^4+2z^5-5z^6+6z^7-2z^8-4z^9+8z^{10}-4z^{11}-2z^{12}+5z^{13}-4z^{14}+z^{15}}.}
\]
In particular,
\[
h_{\mathrm{top}}(F^2(\{0,1\}^{\mathbb Z}),\sigma)=\log\lambda,
\]
where \(\lambda\in(1.827684,1.827685)\) is the Perron root of
\[
\begin{aligned}
P(t)={}&t^{15}-4t^{14}+6t^{13}-5t^{12}+2t^{11}+2t^{10}-5t^9\\
&+6t^8-2t^7-4t^6+8t^5-4t^4-2t^3+5t^2-4t+1.
\end{aligned}
\]
The entropy is approximately \(0.60304968288\) nats per site. The counts begin
\[
(c_0,\ldots,c_{15})=(1,2,4,8,16,29,53,100,187,344,635,1172,2155,3959,7271,13336).
\]

## Assumptions and scope
The lattice is bilateral, indexed by all integers; every cell is updated **simultaneously** at each of two time steps. The input is the full binary shift. The image \(F^2(\{0,1\}^{\mathbb Z})\) is a closed shift-invariant set. These are *spatial* word counts, not counts of indexed periodic-ring outputs, temporal orbits, or spacetime histories. The empty word is counted once. Entropy uses the natural logarithm.

## Proof
**Local two-step rule.** For every five-symbol input \(a_0a_1a_2a_3a_4\), define
\[
g(a_0,\ldots,a_4)=f\bigl(f(a_0,a_1,a_2),f(a_1,a_2,a_3),f(a_2,a_3,a_4)\bigr).
\]
Represent a four-bit word by its binary integer \(u\in\{0,\ldots,15\}\). From \(u\), appending \(b\in\{0,1\}\) moves to \((2u+b)\bmod16\) and emits \(g(u_3,u_2,u_1,u_0,b)\), where \(u_3u_2u_1u_0\) are the bits of \(u\). All 16 vertices are possible starting states. A finite output word labels a path if and only if it is the image under \(g\) of some finite input word four symbols longer. Every such finite input word extends to a bilateral input, so this is precisely the block language of the second image.

**Finite all-word certificate.** Starting from the set of all sixteen vertices, determinize by the subset update \(S\mapsto\bigcup_{u\in S}E_a(u)\), where \(E_a(u)\) comprises successor vertices on edges labeled \(a\). Exact closure has 39 reachable subsets, including the rejecting empty subset. The following complete eighteen-state deterministic automaton is equivalent to the subset construction: the initial state is 17; state 0 rejects and has a self-loop on each symbol; every state 1 through 17 accepts. The two columns are destinations after reading 0 and 1.

| State | 0 | 1 |
|---:|---:|---:|
| 0 | 0 | 0 |
| 1 | 0 | 9 |
| 2 | 14 | 0 |
| 3 | 2 | 1 |
| 4 | 2 | 11 |
| 5 | 2 | 12 |
| 6 | 6 | 3 |
| 7 | 8 | 3 |
| 8 | 16 | 3 |
| 9 | 7 | 4 |
| 10 | 8 | 5 |
| 11 | 6 | 10 |
| 12 | 7 | 13 |
| 13 | 8 | 13 |
| 14 | 15 | 6 |
| 15 | 15 | 9 |
| 16 | 16 | 10 |
| 17 | 16 | 13 |

The independent finite-state equivalence check in `verify_rule54.py` explores the complete reachable product of this automaton and the unminimized subset automaton; it checks accepting/rejecting agreement and closure for **every** reachable pair, not merely for finitely many output word lengths. There are exactly 39 such pairs, covering every subset state and all eighteen table states.

**Generating series identity.** Define the integer matrix \(M\in\mathbb Z^{18\times18}\) by \(M_{ij}=\#\{a\in\{0,1\}:\delta(i,a)=j\}\), and let \(v=(0,1,\ldots,1)^\top\). Then the number of admitted words of length \(n\) is exactly \(c_n=e_{17}^{\top}M^n v\). Direct integer matrix arithmetic gives the all-state vector identity \(P(M)v=0\), for the polynomial \(P\) displayed above. This proves the order-fifteen recurrence \(\sum_{k=0}^{15}[t^k]P(t)\,c_{n+k}=0\) for *all* \(n\ge0\). Substitution of the first fifteen exactly enumerated values yields the displayed rational function \(C(z)=N(z)/(z^{15}P(1/z))\). The checker evaluates each of the eighteen entries of \(P(M)v\) exactly as an integer and checks the numerator coefficients.

**Entropy.** Table states 1 through 16 form a strongly connected directed component of the accepting automaton; it is aperiodic because state 6 has a self-loop labeled 0. State 17 leads into that component on the first output symbol; state 0 is rejecting. Let \(K\) be the adjacency matrix on states 1 through 16, retaining each transition internal to that component. Its characteristic polynomial is \(tP(t)\); its Perron root \(\lambda\) is therefore a positive root of \(P\). Primitivity and the Perron--Frobenius theorem give \(c_n=\Theta(\lambda^n)\). The exact rational inequalities \(1.827684< (K w)_i/w_i<1.827685\) hold for every component \(i\), where \(w=K^{80}\mathbf1>0\). Collatz--Wielandt bounds \(\lambda\) strictly between those two decimals. The topological entropy of a subshift is \(\lim_{n\to\infty}n^{-1}\log c_n\), establishing the formula.

## Verification
Run `python3 verify_rule54.py` in the directory containing this document. The checker uses the Python standard library only. It reconstructs the 32 labeled five-block transitions, saturates all 39 subset states, checks equivalence with the 18-state table over the entire reachable product, verifies \(P(M)v=0\) entrywise, checks initial coefficients, enumerates all input words independently for output lengths 1 through 9, establishes strong connectivity and aperiodicity, and checks rational Perron bounds. Neither finite enumeration nor numerical root approximation is used as a substitute for the all-length matrix identities.

## Relationship to prior work
Pita (2026) develops a forward tiling-transducer description of causal coupling in elementary cellular automata, but not second-image spatial word growth. De Oliveira and collaborators (2015/2016) give finite-time process-graph descriptions (including first and second images of Rule 126), and Kassardjian, Balbi and Ruivo (2024/2025) develop that approach further; the finite-state starting method is therefore classical, while the explicit Rule-54 **second**-image reduced automaton, degree-fifteen word-count series, and exact entropy are the particular invariant established here. The accessible material does not permit a definitive exclusion of an identical uninspected table in those works.

Published related results include the one-step Rule-54 image counts and entropy (published-finding corpus, 2 November 2026), and a universal short-witness threshold for strict second-update image loss across elementary rules (published-finding corpus, 26 October 2026). The one-step image invariant and the existence of a short witness do not imply this exact second-image count sequence or spectral polynomial. The present calculation concerns two synchronous updates, not the distinct reversible, staggered, or asynchronous systems often also called Rule 54.

## Limitations
No formula is asserted for the third or later images, the limiting image, or periodic-ring image counts. The claimed historical originality is based on accessible inspected literature and searches, not an exhaustive literature census. The complete text of the relevant Kassardjian--Balbi--Ruivo work was unavailable through attempted lawful access, so an exact prior tabulation is a residual historical-priority risk. Independent mathematical review has not been conducted.

## References
- M. Pita, *How local rules generate emergent structure in cellular automata*, arXiv:2604.00273v1 (first publicly submitted 31 March 2026), https://arxiv.org/html/2604.00273v1.
- P. P. B. de Oliveira, E. L. P. Ruivo, W. L. Costa, F. T. Miki and V. V. Trafaniuc, *Advances in the study of elementary cellular automata regular language complexity*, *Complexity* 21 (2016), 267–279 (first online 6 May 2015), https://doi.org/10.1002/cplx.21686.
- L. Kassardjian, P. P. B. de Oliveira, and E. L. P. Ruivo, *Extensions on the Analysis of Elementary Cellular Automata with Process Graphs*, Journal of Cellular Automata 18 (2024), 127--155; reprinted in *Advances in Cellular Automata* (2025), 77--107. https://doi.org/10.1007/978-3-031-78757-7_4.
- *Periodic lifting and exact one-step image enumeration for Rule 54*, published published-finding corpus research, 2 November 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-periodic-lifting-and-exact-one-step-image-enumeration-for-rule-5--3615c2fb7c1d.
- *A sharp twelve-symbol threshold for second-update image loss in elementary cellular automata*, published published-finding corpus research, 26 October 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-a-sharp-twelve-symbol-threshold-for-second-update-image-loss-in--5742d176c6e4.
