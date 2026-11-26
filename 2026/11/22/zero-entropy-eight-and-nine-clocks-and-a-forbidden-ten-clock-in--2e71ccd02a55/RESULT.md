# Zero-entropy eight- and nine-clocks and a forbidden ten-clock in Rule 110

## Finding
Consider the simultaneous elementary binary cellular automaton Rule 110 on a labelled cyclic ring with \(n\ge3\) sites. For \(t\in\{8,9,10\}\), let \(C_t(n)\) be the number of distinct **primitive temporal orbits** of least period \(t\), identifying the \(t\) phases of an orbit but **not** identifying spatial rotations. Then the complete all-circumference census is
\[
\boxed{\begin{aligned}
 C_8(n)&=\mathbf1_{8\mid n},\\
 C_9(n)&=2\mathbf1_{6\mid n}+4\mathbf1_{12\mid n}+2\mathbf1_{18\mid n},\\
 C_{10}(n)&=0.
\end{aligned}}
\]
In particular, there is precisely one eight-cycle if and only if the ring length is a multiple of eight. Nine-cycles exist precisely at multiples of six: their orbit population is two, four, six or eight depending on additional divisibilities by twelve and eighteen. **No cyclic Rule 110 system has a primitive ten-cycle**, at any ring size. The temporal eight- and nine-cycle populations are bounded and positive along infinitely many circumferences, so \(\limsup_{n\to\infty}n^{-1}\log C_t(n)=0\) for \(t=8,9\), with \(\log 0=-\infty\). This contrasts with the positive entropy of the primitive temporal-five and temporal-seven classes. Written in increasing site order, time-zero words witnessing periods eight and nine are `00101111` and `000111`, respectively. For the former, the successive words before the first return are `01111001`, `11001011`, `01011110`, `11110010`, `10010111`, `10111100`, and `11100101`.

## Assumptions and scope
The spatial alphabet is \(\{0,1\}\), each site is indexed by \(\mathbb Z/n\mathbb Z\), and every site updates simultaneously via
\[
 F_n(x)_i=f(x_{i-1},x_i,x_{i+1}),\qquad
 f(a,b,c)=\text{bit}_{4a+2b+c}(110).
\]
Thus \(f\) is one on neighborhoods `001`, `010`, `011`, `101`, `110` and zero on `000`, `100`, `111`. Cyclic boundary conditions apply also to overlapping neighborhood indices. Temporal period refers to the least positive \(t\) satisfying \(F_n^t(x)=x\) **from the specified initial configuration**; the theorem does not count states that first enter such an orbit after a transient. The theorem is written for \(n\ge3\), although the transfer identities extend to the standard indexed periodic convention at one and two sites. Spatial shifts do not identify distinct temporal orbits. By reflection, the corresponding cycle census is identical for Rule 124, but the stated graph and checks use Rule 110.

## Proof
For each temporal height \(t\), encode the \(t\) time bits at each spatial site as a column \(h\in\{0,1\}^t\), with time indexed modulo \(t\). Form a directed graph \(G_t\) on ordered pairs of columns \((a,b)\). Put an edge \((a,b)\to(b,c)\) if and only if
\[
 b_{j+1\bmod t}=f(a_j,b_j,c_j)\qquad(0\le j<t).
\]
There is a bijection between \(n\)-step closed walks in this spatial de Bruijn graph (with a specified starting site) and original labelled ring configurations fixed by \(F_n^t\). Indeed, a closed walk identifies a consistent temporally circular space-time diagram satisfying the local update at every site and time. Conversely, the time histories of any fixed-by-\(t\) configuration determine exactly this walk. Hence if \(A_t\) is the adjacency matrix,
\[
 T_t(n):=|\operatorname{Fix}(F_n^t)|=\operatorname{tr}(A_t^n).
\]
Only strongly connected components containing directed cycles contribute to this trace. There is no inference from a finite sample of ring lengths: the adjacency graph is constructed *in full* for each fixed height \(t\), then its cyclic components exhaust every closed walk at **all** ring lengths.

Direct finite enumeration from the eight-entry rule table gives the following **complete inventory of cyclic strongly connected components**. The notation \((\ell,e;p)\) means \(\ell\) vertices, \(e\) directed internal edges, and least simultaneous temporal period \(p\) of the two columns at every vertex of that component. Multiplicity is written as a prefix.

| Temporal height | Cyclic components \((\ell,e;p)\) |
|---|---|
| \(1\) | \((1,1;1)\) |
| \(2\) | \((4,4;2), (1,1;1)\) |
| \(3\) | \((9,9;3), (1,1;1)\) |
| \(4\) | \((4,4;2), (1,1;1)\) |
| \(5\) | \((25,30;5), (1,1;1)\) |
| \(8\) | \((8,8;8), (4,4;2), (1,1;1)\) |
| \(9\) | \((18,18;9), 3(12,12;9), (9,9;3), 3(6,6;9), (1,1;1)\) |
| \(10\) | \((25,30;5), (4,4;2), (1,1;1)\) |

Every component with \(e=\ell\) is a simple directed cycle; for height ten, the sole non-simple component has simultaneous column period five at all its vertices. To check the table reproducibly, `verification/verify_short_clocks.py` constructs all temporal graphs from the truth table, prunes vertices with zero indegree or outdegree, finds cyclic strongly connected components in the remaining graph, counts the internal edges, and checks each vertex's smallest temporal divisor. It asserts the complete inventory, including the non-simple 25-vertex component.

For \(t=8\), a directed \(\ell\)-cycle has \(\ell\) closed walks of spatial length \(n\) exactly when \(\ell\mid n\). Therefore the table implies
\[
 T_8(n)=1+4\mathbf1_{4\mid n}+8\mathbf1_{8\mid n},\qquad
 T_4(n)=1+4\mathbf1_{4\mid n}.
\]
All periods dividing eight divide four or equal eight. Their primitive-eight configuration count is \(T_8(n)-T_4(n)=8\mathbf1_{8\mid n}\); dividing by eight counts temporal orbits.

Similarly, the nine-step graph yields
\[
 T_9(n)=1+9\mathbf1_{9\mid n}+18\mathbf1_{18\mid n}
       +36\mathbf1_{12\mid n}+18\mathbf1_{6\mid n},\quad
 T_3(n)=1+9\mathbf1_{9\mid n}.
\]
Since periods dividing nine are one, three, and nine, subtraction and division by nine give exactly the stated \(C_9(n)\). Each of the three contributions left after subtraction has a *primitive temporal-nine history* by the listed column-period tests; the multiples of six represent genuine temporal-nine cycles even though the spatial circumference may be six.

Finally every closed walk in \(G_{10}\) is contained within a cyclic component whose columns have temporal period either two, five, or one. Therefore each original configuration fixed after ten updates is fixed after two or five updates. Conversely, both fixed-by-two and fixed-by-five sets are fixed after ten updates. Thus
\[
 \operatorname{Fix}(F_n^{10})=\operatorname{Fix}(F_n^2)\cup\operatorname{Fix}(F_n^5),
\]
whose intersection is exactly \(\operatorname{Fix}(F_n)\) because \(\gcd(2,5)=1\). Equivalently, by inclusion–exclusion, \(T_{10}-T_5-T_2+T_1=0\), proving the universal nonexistence of primitive ten-cycles. This completes the full theorem, including every circumference and the zero-entropy consequences.

## Verification
The packaged `verification/verify_short_clocks.py` requires only Python 3's standard library. It generates temporal graphs for heights \(1,2,3,4,5,8,9,10\) from the local rule, and checks each cyclic component against the inventory above. The most expensive tenth-height case has 215,232 vertices with outgoing edges. Degree pruning leaves 31 vertices, of which 30 belong to cyclic strongly connected components. The script checks the arithmetic formulas for the first 400 circumferences as an additional consistency test and finishes with `FULL_SPECTRAL_COUNTS_OK`.

The independently written `verification/check_direct.py` instead evolves every binary initial word on every ring length \(3\le n\le20\) using bit-parallel Boolean operations; it computes genuine primitive-period tests for eight, nine, and ten and compares every count against the three formulas. Its successful marker is `BRUTE_FORCE_OK`. The delivered `.out` files are recorded outputs; executable source and the exact finite-component proof are the actual verification evidence. Computational enumeration of a bounded collection of original ring lengths is *not* substituted for the all-length argument.

## Relationship to prior work
Wolfram's 2002 *A New Kind of Science* describes the Rule 110 space-time patterns and their periodic background, and Cook (2004) proves computational universality and gives period/displacement pairs of individual gliders, including A and B types. The A/B descriptions already motivate examples of temporal eight- and nine-periodic ring behavior; **existence of individual short glider waves is not claimed as new**. Martínez et al. (2007) study extended de Bruijn diagrams and glider languages through ten generations, including a zero-shift pattern plot, and Martínez et al. (2016) study engineered finite collider rings. Those works provide methods and examples but the inspected relevant sections do not specify these evaluated all-size primitive-eight, primitive-nine and primitive-ten counts, nor the complete component inventory that forces the forbidden ten-clock. Stricker (2023) surveys and numerically explores finite-ring period spectra, including Rule 110, and states that comprehensive initial-state enumeration reaches ring lengths at most 22; this does not constitute the all-circumference formulas.

Closest published temporal-return calculations for the same map give a positive-entropy period-five class and a complete period-seven spectrum, with period-six excluded. Neither subsumes the present arithmetic counts: the new height-nine component contains additional closed walks not implied by height-seven or height-five data, and the absence of ten-periodic orbits requires examining every height-ten cyclic component. A separate published one-step image zeta concerns spatial periodic words in the **output image** rather than temporal returns. Rule 124 is a spatial mirror of Rule 110 and is an equivalent formulation, not an additional distinct theorem.

## Limitations
The theorem describes temporal orbits of exact periods eight, nine and ten only; it does not classify all temporal periods, attraction basins, transient entry or full-spatial dynamical zeta functions at arbitrary temporal heights. Existing glider and finite-size literature may already contain some of the initial finite witnesses, so their priority is not claimed; the originality claim concerns the joint **all-size exact census** and its proof. Unindexed historical statements may still contain equivalent formulas.

## References
- S. Wolfram, *A New Kind of Science* (first published 2002-05-14), Wolfram Media. https://www.wolframscience.com/nks/citation/ .
- M. Cook, *Universality in Elementary Cellular Automata*, *Complex Systems* **15** (2004), 1–40. https://content.wolfram.com/sites/13/2023/02/15-1-1.pdf .
- G. J. Martínez, H. V. McIntosh, J. C. Seck Tuoh Mora, S. V. Chapa Vergara, *Determining a regular language by glider-based structures called phases in Rule 110*, arXiv:0706.3348 (first arXiv 2007-06-22). https://arxiv.org/pdf/0706.3348 .
- G. J. Martínez, A. Adamatzky, H. V. McIntosh, *A Computation in a Cellular Automaton Collider Rule 110*, arXiv:1609.05240 (first arXiv 2016-09-16). https://arxiv.org/pdf/1609.05240 .
- H.-P. Stricker, *Classification of Elementary Cellular Automata Based on Their Limit Cycle Lengths in Z/k*, *Complex Systems* **32** (2023), 229–251. https://content.wolfram.com/sites/13/2024/01/32-3-1.pdf .
- *Lucas arithmetic and the first exponential short-return class in elementary Rule 110*, prior published temporal-five census. [Record](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-lucas-arithmetic-and-the-first-exponential-short-return-class-in--6da91943e80a).
- *A sharp thirty-site gap between six- and seven-step recurrence in Rule 110*, prior published temporal-six/seven census. [Record](https://github.com/Resultary/2026/tree/main/2026/11/17/SCOPE-a-sharp-thirty-site-gap-between-six-and-seven-step-recurrence-in--2dd8fa420e00).
- *Exact spatial dynamical zeta function and least periods of the Rule 110 one-step image*, prior published image-language census. [Record](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-exact-spatial-dynamical-zeta-function-and-least-periods-of-the-r--9af6bc7e78bc).
