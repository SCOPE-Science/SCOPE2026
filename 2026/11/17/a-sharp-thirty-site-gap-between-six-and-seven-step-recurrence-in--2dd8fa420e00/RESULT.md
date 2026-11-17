# A sharp thirty-site gap between six- and seven-step recurrence in Rule 110

## Finding
For the synchronous elementary cellular automaton Rule 110 acting on a labelled binary ring of circumference \(n\ge3\), let \(C_7(n)\) count distinct temporal orbits of **least period seven**. There are no primitive temporal six-cycles on any ring. Primitive temporal seven-cycles exist **exactly** when
\[
 n\in\{9,11,14,17,18,20,22,23,25,26,27,28,29\}\ \cup\ \{n\ge31\}.
\]
Thus circumference 30 is the largest excluded ring size. At circumferences \(9,11,14,17,18,20\), the respective seven-cycle counts are \(9,11,2,17,9,60\).

There is also an exact count for every size: construct the 128-column, 16,384-vertex directed graph \(G_7\) below; let \(A\) be the adjacency matrix on its unique nontrivial strongly connected component, whose 63 vertex labels are ordered increasingly. Then
\[
 C_7(n)=\frac{1}{7}\operatorname{tr}(A^n)\qquad(n\ge3).
\]
The formula requires no unlisted numerical data: all entries of \(A\) are determined by the local Rule 110 truth table in the proof, and a standalone checker constructs them.

## Assumptions and scope
Write each binary ring as \((x_0,\ldots,x_{n-1})\), with indices modulo \(n\). The local rule is
\[
 f(a,b,c)=\left\lfloor\frac{110}{2^{4a+2b+c}}\right\rfloor\bmod2,
 \qquad (F_nx)_i=f(x_{i-1},x_i,x_{i+1}).
\]
Updates are synchronous. Ring positions are labelled: rotations are **not** identified. A temporal orbit is identified up to time-shift along its own trajectory, so seven different phase states form one primitive seven-cycle. All claims are for finite rings; no claim is made about arbitrary infinite spatial configurations, attraction basin sizes, or periods above seven.

## Proof
For any positive temporal height \(T\), encode the history at spatial site \(i\) as a column \(p_i\in\{0,1\}^T\), with time interpreted modulo \(T\). Form a directed graph \(G_T\) on ordered pairs \((a,b)\) of such columns. Draw \((a,b)\to(b,c)\) precisely when, for every \(0\le t<T\),
\[
 b_{t+1\bmod T}=f(a_t,b_t,c_t).
\]
Every labelled configuration fixed by \(F_n^T\) corresponds bijectively to a rooted closed walk of length \(n\) in \(G_T\), and conversely, because the successive spatial columns uniquely prescribe the complete periodic history. The count is therefore the trace of the \(n\)-th adjacency power. Vertices outside a directed cyclic strongly connected component cannot occur on such a walk.

The exhaustive integer-only finite graph certificate establishes: \(G_1\) has only the zero-column recurrent vertex; \(G_6\) has 4,097 edges and recurrent components consisting of one loop, one directed 4-cycle and one directed 9-cycle; and \(G_7\) has 16,385 edges and precisely two cyclic components, an isolated zero loop and a 63-vertex, 84-edge strongly connected component. These statements are verified by the included full graph reconstruction and independent strongly connected component algorithm; no random sampling enters the proof.

The sixth-return fixed configurations correspond to the same spatial 4- and 9-cycle components already present for temporal heights two and three; hence every configuration fixed by \(F_n^6\) is fixed by \(F_n^2\) or \(F_n^3\). No least-period-six temporal orbit can exist.

For height seven, let \(A\) denote the 63-by-63 zero-one adjacency matrix of the nontrivial component. Since \(G_1\) has only the zero recurrent configuration and seven is prime, every other state fixed by \(F_n^7\) has least temporal period seven. Therefore its count of primitive temporal orbits is exactly \(\operatorname{tr}(A^n)/7\).

For existence, a Boolean closed-walk calculation on the *complete* 63-vertex component proves that the positive lengths through 30 are exactly
\[
 9,11,14,17,18,20,22,23,25,26,27,28,29.
\]
Furthermore vertex \(193\), interpreted as the ordered pair of columns \((1,65)\), supports a closed walk of length nine and a closed walk of every length from 31 through 39 inclusive. Concatenating the length-nine walk with each of the latter walks proves the existence of a closed walk for **every** length at least 31: reduce the given length modulo nine to one of 31 through 39 and append enough length-nine loops. These two finite tests give the exact claimed circumference spectrum, with 30 the largest exclusion.

## Verification
Run `python3 verify_transfer.py` in Python 3.8 or newer. This program generates all graphs from the Rule 110 truth table, performs iterative Kosaraju decomposition of every vertex, verifies the complete recurrent-component sizes and edge populations, enumerates every closed-walk *existence* through length 40, and certifies the common-root 9-step extension. For the displayed six orbit counts it also separately computes integer walk multiplicities rather than confusing reachability with counting.

Compile `verify_direct.cpp` using `g++ -std=c++17 -O3 verify_direct.cpp -o verify_direct` and run `./verify_direct`. The separately written direct state enumerator compares the Rule 110 sixth- and seventh-return claims for every labelled binary configuration at all ring sizes from three through twenty. Its scope is a finite cross-check, not a substitute for the transfer-graph proof. Recorded standard output from both executables accompanies the source programs.

## Relationship to prior work
Cook (2004) established Rule 110 computational universality and introduced a detailed glider-system analysis. Martínez and collaborators (2007) use de Bruijn diagrams to encode glider phases, and Martínez, Adamatzky and McIntosh (2016) list stationary glider families with temporal period seven and spatial sizes including nine, eleven and seventeen. Those examples account for some early members of the spectrum but do **not**, as stated there, determine all permitted circumferences, prove the sharp 30-site exclusion or count the full primitive-seven population for every labelled ring. Distinguish also earlier published one-step-image spatial zeta calculations: a spatial shift on images is not the seventh temporal return map. The present graph uses a complete seven-time-layer constraint, rather than selected glider configurations.

## Limitations
The result is a self-review supported by reproducible, finite exhaustive graph checks, not an independent mathematical audit. A historical database or older glider catalogue may contain an equivalent seven-return classification not located in the inspected materials; no absolute priority claim is made. The formula \(\operatorname{tr}(A^n)/7\) is an effective matrix formula, not an explicitly expanded scalar linear recurrence. No claims are made for spatially infinite configurations or higher temporal periods.

## References
- Matthew Cook, *Universality in Elementary Cellular Automata*, Complex Systems 15 (2004), 1–40, DOI: 10.25088/ComplexSystems.15.1.1.
- G. J. Martínez, H. V. McIntosh, J. C. Seck Tuoh Mora, and S. V. Chapa Vergara, *Determining a regular language by glider-based structures called phases \(f_{i1}\) in Rule 110* (arXiv:0706.3348, first posted 2007-06-22).
- G. J. Martínez, A. Adamatzky, and H. V. McIntosh, *A Computation in a Cellular Automaton Collider Rule 110* (arXiv:1609.05240, first posted 2016-09-16).
