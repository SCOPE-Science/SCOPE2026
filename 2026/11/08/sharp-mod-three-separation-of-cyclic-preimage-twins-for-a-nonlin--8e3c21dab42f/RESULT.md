# Sharp mod-three separation of cyclic preimage twins for a nonlinear five-neighbor automaton

## Finding
For each integer \(N\ge 1\), let \(F_N\) act on binary words indexed cyclically modulo \(N\), with all algebra in \(\mathbb F_2\), by
\[
(F_N(x))_i=x_{i+1}+x_{i+2}+x_i(1+x_{i+2})x_{i+3}+x_{i+1}(1+x_{i+3})x_{i+4}.
\]
This is the second two-to-one, diameter-five rule in the Appendix B table of Haugland--Larsen--Omland--Rustad (2026). Every nonempty fiber of \(F_N\) has exactly two members, and its image has size \(2^{N-1}\). Most importantly, the *minimum Hamming distance between distinct members of the same fiber*, over all nonempty fibers, is exactly
\[
\boxed{\delta_N=\lfloor N/3\rfloor+\begin{cases}0&N\equiv0\pmod3,\\1&N\equiv1\pmod3,\\2&N\equiv2\pmod3.\end{cases}}
\]
The formula holds for all positive lengths, including the repeated-index cases \(N<5\). In particular, the two predecessors of any attainable output differ on at least one third of the ring, and the exact sharp correction has period three.

## Assumptions and scope
All indices are modulo \(N\); the zero/one symbols are elements of \(\mathbb F_2\), so addition is exclusive-or. Define the cyclic difference \((D_Nu)_i=u_i+u_{i+1}\), the shift \((\sigma_Nu)_i=u_{i+1}\), and the nonlinear marker map
\[
(K_Nx)_i=x_i+x_{i-1}(1+x_{i+1})x_{i+2}.
\]
For a map \(F_N\), a *preimage twin* is an unordered pair of distinct words \(x,z\) with \(F_N(x)=F_N(z)\). Hamming distance is the number of sites where the inputs differ. The theorem concerns a single synchronous iteration on finite periodic rings, not whether the bi-infinite automaton is locally eventually onto or how its arbitrary iterates behave.

## Proof
**Factorization and exact twin multiplicity.** Direct expansion gives \(F_N=D_N\circ\sigma_N\circ K_N\). Write \(t_i=x_{i-1}(1+x_{i+1})x_{i+2}\). If \(t_i=1\), then \(t_{i\pm1}=t_{i\pm2}=0\) (the needed zero and one conditions at a shared guard site contradict). Thus simultaneous toggling at all indices with \(t_i=1\) cannot change the guard terms of any toggle. Consequently \(K_N^2=\mathrm{id}\) for every \(N\); for \(N=1,2\), all guards are automatically zero and the conclusion remains true. The shift is bijective. The kernel of \(D_N\) consists of the two constant words, and its image is exactly the even-parity subspace. Therefore each nonempty fiber has exactly two points, the image has \(2^{N-1}\) points, and the twin of \(x\) is uniquely
\[
J_N(x)=K_N(\mathbf1+K_N(x)).
\]
Equivalently, \(x,z\) form a twin pair precisely when \(K_N(x)+K_N(z)=\mathbf1\).

**Finite weighted graph for *all* ring lengths.** Encode the two input words sitewise by a four-symbol word \(s_i=x_i+2z_i\in\{0,1,2,3\}\), where the latter expression is an integer encoding, not addition in \(\mathbb F_2\). For \(a,b,c,d\in\{0,1,2,3\}\), put \(a_x=a\bmod2\), \(a_z=\lfloor a/2\rfloor\), and likewise for the other symbols, and define \(k(a,b,c,d)=b_x+a_x(1+c_x)d_x\) and its \(z\)-analogue. Construct a directed graph on \(64\) vertices, each encoded as \(u=a+4b+16c\). Include the edge
\[
(a,b,c)\longrightarrow (b,c,d)
\]
exactly when the two values of \(k\) for that quadruple differ. Give this edge weight \(w=b_x+b_z\in\{0,1\}\). The graph has exactly \(128\) edges. Closed walks of length \(N\) correspond exactly to ordered cyclic twin pairs, and their total weight is the Hamming distance; this remains valid when \(N=1,2,3\), using cyclic repeated indices.

**An all-length lower certificate.** Define an integer potential \(p\) on vertex numbers \(0,\ldots,63\): set \(p=-2\) at vertices \(24,36,52,56\), set \(p=-1\) at \(16,19,27,32,35,39,48,51,55,59\), and set \(p=0\) elsewhere. On every allowed edge \(u\to v\) its reduced cost
\[
r(u,v)=3w(u,v)-1+p(u)-p(v)
\]
is nonnegative, by checking the finite list of \(128\) locally defined edges. Hence for a closed walk of length \(N\) and weight \(h\), \(3h-N=\sum r\ge0\), so \(h\ge\lceil N/3\rceil\). The graph has exactly \(16\) edges of reduced cost one. For **each** of these \(16\) edges \(u\to v\), there is no path from \(v\) back to \(u\) using only zero-cost edges. This finite statement is checked exhaustively by the standalone program `verify.py`, which constructs the entire graph from the Boolean rule and uses a terminating reachability search. Therefore no closed walk has total reduced cost one. For \(N=3k+2\), a hypothetical twin at distance \(k+1\) would give total reduced cost \(3(k+1)-(3k+2)=1\), impossible. This strengthens the bound to \(k+2\) in exactly that congruence class.

**Sharp witnesses for every length.** Use the four-symbol encoding above. If \(N=1\), the cyclic symbol word `2` is a twin pair of weight one. For \(k\ge1\), `302` repeated \(k\) times gives length \(3k\) and weight \(k\). For \(k\ge1\), `3132` followed by `302` repeated \(k-1\) times gives length \(3k+1\) and weight \(k+1\). For \(k\ge0\), `12` followed by `302` repeated \(k\) times gives length \(3k+2\) and weight \(k+2\). In each family every cyclic four-symbol window satisfies the displayed edge condition. This is a finite substitution check: arbitrarily many copies of `302` add no new length-four windows after two repetitions; the possible windows, including the short exceptional cycles, are generated and checked by the standalone program. These witnesses attain the lower bounds, completing the exact formula.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter and no third-party dependencies. It reconstructs all \(64\) vertices and \(128\) edges from scratch; checks every potential inequality; counts all \(16\) unit-reduced-cost edges and proves that no zero-reduced-cost return path exists; checks witness templates and their cyclic windows; and independently enumerates complete maps and twin distances for lengths \(1\) through \(12\). The program reports `VERIFY_OK checks=57769 edges=128 ones=16`. The infinite-length conclusion follows from the exact graph certificate and repeating-word construction, **not** from finite-length sampling.

## Relationship to prior work
Haugland--Larsen--Omland--Rustad (arXiv:2610.33131v1, Appendix B, row two of the three unresolved two-to-one five-neighbor rules) identify the local rule and its two-to-one bi-infinite dynamics. Haugland--Omland (arXiv:2411.00721; subsequently published in 2026) already give the primitive-landscape mechanism for reversible marker maps; it is **not** claimed here as a new construction. Haugland--Omland (arXiv:2407.11931) address cyclic almost-liftings and collision differences, providing the closest quantitative conceptual precedent. The new claim is the exact **minimum positional separation** of the twin precursors in this specific nonlinear second rule, including the sharp \(N\bmod3\) anomaly; the cited works' multiplicity, marker reversibility, and collision-frequency statements do not themselves state this invariant. The publicly reported first/third-rule image characterization is distinct: it does not classify twin distances for the second rule.

## Limitations
The proved formula is specific to the displayed second diameter-five rule, single-step fibers and finite periodic boundaries. It does not answer its locally-eventually-onto status, generalize automatically to the other two rules, classify the full distance distribution or claim cryptographic security. The graph certificate has been reviewed within the present mathematical development but has not received an independent audit. Although relevant full texts and searchable records were compared, unlocated earlier specialized distance-spectrum work may affect historical priority.

## References
1. J. K. Haugland, N. S. Larsen, T. Omland, H. G. Rustad, *Locally eventually onto cellular automata*, arXiv:2610.33131v1 (first submitted 2026-10-23), Appendix B, https://arxiv.org/html/2610.33131v1.
2. J. K. Haugland, T. Omland, *New classes of reversible cellular automata*, arXiv:2411.00721v1 (first submitted 2024-11-01), https://arxiv.org/abs/2411.00721; open-access full text https://doi.org/10.1007/s10623-026-01869-z.
3. J. K. Haugland, T. Omland, *Shift-invariant functions and almost liftings*, arXiv:2407.11931 (first submitted 2024-07-16), https://arxiv.org/abs/2407.11931; later published as *Shift-invariant transformations and almost liftings*, https://doi.org/10.1007/s12095-025-00848-w.
