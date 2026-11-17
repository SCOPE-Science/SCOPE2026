# Exact cyclic inverse fibers of elementary Rule 18

## Finding
For every integer \(n\ge1\), define the synchronous binary cellular automaton on the indexed ring \(\mathbb Z/n\mathbb Z\) by
\[
T_n(x)_i=1\quad\Longleftrightarrow\quad (x_{i-1},x_i,x_{i+1})\in\{(0,0,1),(1,0,0)\}.
\]
The indices are interpreted modulo \(n\), including when \(n=1\) or \(n=2\). Write \(d_n(y)=|T_n^{-1}(y)|\). Let \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\), and let \(L_0=2,L_1=1,L_{k+2}=L_{k+1}+L_k\).

For the all-zero output, \(d_n(0^n)=L_n+1\). A nonzero output with odd Hamming weight has no predecessor. For any output \(y\) of positive even Hamming weight \(2m\), list its marked positions in cyclic order as \(p_1,\ldots,p_{2m}\), with a fixed starting point, and put \(p_{2m+1}=p_1+n\) and
\[
q_j=p_{j+1}-p_j-1\quad(1\le j\le2m).
\]
Then its exact one-step predecessor count is
\[
\boxed{d_n(y)=\prod_{j=1}^{m}F_{q_{2j-1}}+\prod_{j=1}^{m}F_{q_{2j}}.}
\]
The expression is independent of which marked position is chosen first. Empty factors are not used because \(m\ge1\). The image criterion for nonzero outputs is consequently: the number of ones is even, and at least one of the two alternating families of gaps is entirely positive. Finally, for **every** \(n\ge1\), the all-zero output is the unique maximizer of \(d_n\), with maximum \(L_n+1\).

## Assumptions and scope
The domain and codomain are each the set of \(2^n\) indexed binary rings, not rotation classes. Different rotations are counted as distinct inputs when they differ as indexed configurations. Only one synchronous update is considered. The convention for the zero-length gap is \(F_0=0\). Both small rings are included by the specified modular neighborhood rule, without assuming three different neighbor sites.

## Proof
**Run-boundary observation.** For a nonconstant cyclic input, each maximal zero-run of length at least two gives exactly two output ones: at its first and last zero. These are respectively the triples \(100\) and \(001\). A zero-run of length one gives no output one. No other sites produce a one. The two output markers of each long zero-run are different, so the positive output weight is even.

**Two possible directed arc pairings.** Let \(y\ne0^n\) have \(2m\) marked sites. Every preimage induces oriented arcs between the output markers forming the endpoints of its long zero-runs. Since such runs cannot overlap or nest, the cyclic markers admit precisely two alternating choices of those oriented arcs (even with two markers, the two possible directions are distinguished): \((p_1,p_2),(p_3,p_4),\ldots\), or \((p_2,p_3),(p_4,p_5),\ldots,(p_{2m},p_1+n)\). In the first pairing, the arcs between the paired endpoints are forced zero-runs, and the other arcs contain exactly \(q_2,q_4,\ldots,q_{2m}\) intervening sites. Each intervening arc must have length at least one, with its first and last input symbols equal to one, and it must contain no \(00\). The second pairing exchanges odd and even gaps.

**Fibonacci gap enumeration.** Let \(c_g\) be the number of binary words of length \(g\) that start and end with one and avoid \(00\). Then \(c_1=c_2=1\), and, by partitioning according to the next symbol or by the usual two-state transfer recurrence, \(c_{g+2}=c_{g+1}+c_g\). Thus \(c_g=F_g\) for \(g\ge1\). Set \(c_0=0\) because an empty intervening arc joins two zero-runs into a single run and is not allowed. Once the pairing and the intervening words are chosen, every remaining input site is forced to zero; the resulting input has exactly the stated long zero-runs and returns \(y\). Different pairings cannot yield the same input, because its maximal zero-runs determine the pairing uniquely. Multiplication over disjoint arcs and summation over the two pairings prove the displayed formula and its positivity criterion.

**Zero output.** An input yields \(0^n\) iff it is all zero, or it avoids cyclic occurrences of \(00\). Indeed, a nonconstant input with any \(00\) belongs to a maximal zero-run of length at least two, hence produces at least two output ones. The number of indexed binary cyclic words avoiding \(00\) is \(\operatorname{tr}(Q^n)\) for \(Q=\begin{pmatrix}0&1\\1&1\end{pmatrix}\), which is \(L_n\) by the characteristic polynomial and initial traces. The extra all-zero input contributes one. This argument holds for \(n=1\) and \(n=2\) as well.

**Strict maximum.** Set \(\varphi=(1+\sqrt5)/2\). The elementary Fibonacci inequality \(F_g\le\varphi^{g-1}\) holds for all integers \(g\ge1\). For a positive alternating product with \(m\) factors, all selected gaps are positive, so their sum is at most \(n-2m\), because there are \(2m\) marked sites. Its value is at most \(\varphi^{n-3m}\le\varphi^{n-3}\). Consequently, every nonzero output has \(d_n(y)\le2\varphi^{n-3}<\varphi^n\), or has no preimage at all. On the other hand \(L_n+1=\varphi^n+(-\varphi)^{-n}+1>\varphi^n\) for every \(n\ge1\). This establishes uniqueness of the maximum, including the smallest rings.

## Verification
Run `python3 direct_check.py` to enumerate all indexed configurations and compare all output fibers against the formula for every \(1\le n\le18\). Run `python3 transfer_check.py` for an independently implemented four-state de Bruijn trace counter: it compares every output for \(1\le n\le12\), plus predetermined and pseudorandom outputs through length \(180\). Both commands require only Python's standard library. These finite calculations test the proof; they do not substitute for its all-length arguments.

The four-state transfer check uses state labels \(00,01,10,11\), with an edge from \(ab\) to \(bc\) labelled by \(T(abc)\); the predecessor count is the trace of the product of matrices indexed by the output. This representation is already standard in the literature and is not claimed as new.

## Relationship to prior work
Shreim, Grassberger, Nadler, Samuelsson, Socolar and Paczuski (2007) identify the all-zero configuration as the Rule 18 hub from numerical investigation and give its transfer-matrix counting framework and asymptotic exponent. Neither the hub identification nor the generic trace formula is claimed as new here. Jen (1989) gives general one-dimensional preimage recurrences and Fibonacci-block expressions for related rule analyses, primarily for unrestricted boundaries; the cited discussion does not state this particular indexed cyclic, all-output two-alternating-product identity. Fukś (2003) studies sequences of preimage counts for elementary rules. The contribution assessed here is the explicit cyclic inverse-fiber factorization, the exact image test, and a standalone all-length proof of strict maximality. A general matrix algorithm could of course compute each individual fiber, and historical priority of the closed form is not independently certified.

## Limitations
No claim is made about multiple time steps, different boundary conventions, other cellular automata or the complete frequency distribution of possible nonzero fiber sizes. The historical-priority comparison is limited to the checked accessible primary material and published finding search, not a proof of exhaustive bibliographic coverage. No independent scientific audit has been performed.

## References
1. A. Shreim, P. Grassberger, W. Nadler, B. Samuelsson, J. E. S. Socolar, and M. Paczuski, “Network Analysis of the State Space of Discrete Dynamical Systems,” *Physical Review Letters* **98** (2007), 198701. https://doi.org/10.1103/PhysRevLett.98.198701 (published May 8, 2007).
2. E. Jen, “Enumeration of Preimages in Cellular Automata,” *Complex Systems* **3** (1989), 421–456. https://content.wolfram.com/sites/13/2018/02/03-5-2.pdf
3. H. Fukś, “Sequences of Preimages in Elementary Cellular Automata,” *Complex Systems* **14** (2003), 29–43. https://doi.org/10.25088/ComplexSystems.14.1.29
4. “Limit dynamics of elementary cellular automaton 18,” *Ergodic Theory and Dynamical Systems* (2026), https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/limit-dynamics-of-elementary-cellular-automaton-18/8D236BAA96D6BB0F894ABCFEF3C1312B (later treatment of Rule 18 language and defect dynamics; not used to establish the archive source date).
