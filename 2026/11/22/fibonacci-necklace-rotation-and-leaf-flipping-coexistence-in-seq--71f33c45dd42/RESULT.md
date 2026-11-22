# Fibonacci-necklace rotation and leaf-flipping coexistence in sequential bi-threshold sunlets

## Finding
For each integer \(n\ge3\), the sequential \((1,3)\) bi-threshold map on the sunlet \(C_n\circ K_1\), with the rim vertices updated consecutively and then all private leaves updated, has an explicitly described **invariant set consisting entirely of periodic states**. It is the union of (i) a copy of the cyclic golden-mean (no-adjacent-ones) binary shift of length \(L=n-1\), on which one complete update acts as one cyclic rotation, and (ii) all states with the entire rim occupied, on which one update complements the leaf vector. This constructed union contains exactly
\[
  2^n+\mathcal L_{n-1}-2\mathbf 1_{\{n\text{ odd}\}}
\]
distinct periodic configurations, where \(\mathcal L_0=2\), \(\mathcal L_1=1\), and \(\mathcal L_{j+2}=\mathcal L_{j+1}+\mathcal L_j\) are Lucas numbers. **This is an exact count for the constructed invariant union, not an assertion that it exhausts all periodic configurations.**

Within this union the number of primitive period-two orbits is exactly \(2^{n-1}\); there is one fixed point, the all-zero state; and for every divisor \(d\mid n-1\) with \(d\ge3\), the number of primitive period-\(d\) orbits is exactly
\[
  \frac1d\sum_{e\mid d}\mu(d/e)\,\mathcal L_e.
\]
All other primitive periods are absent *within the constructed union*. In particular, a period-\(n-1\) orbit exists for every \(n\ge4\). The union therefore contains exponentially many periodic points together with arbitrarily long periods.

## Assumptions and scope
Write the sunlet's rim vertices as \(v_0,\dots,v_{n-1}\) in cyclic order, with a pendant vertex \(u_i\) attached to \(v_i\). Each vertex has a state in \(\{0,1\}\). At each elementary update, count occupied vertices in the **closed** neighborhood (including the vertex itself). A zero changes to one when the count is at least one; a one stays one when the count is at least three and otherwise becomes zero. The full deterministic permutation-sequential map \(F_n\) updates \(v_0,\ldots,v_{n-1}\), then \(u_0,\ldots,u_{n-1}\). No parallel update is being used.

Put \(L=n-1\) and let
\[
\mathcal I_L=\{s\in\{0,1\}^L:s_j s_{j+1}=0\text{ for every }j\pmod L\}.
\]
Define the encoded configuration \(E_n(s)\) by, for all \(0\le i\le n-1\), using \(j=i\bmod L\),
\[
  a_i=s_j\lor s_{j-1},\qquad b_i=s_j,
\]
where \(a_i\) is the rim state, \(b_i\) the private-leaf state and all subscripts on \(s\) are cyclic modulo \(L\). Thus the final rim-leaf pair repeats the first one. Write \(\rho(s)_j=s_{j+1}\) (left cyclic rotation). Let \(U_n(b)\) have all rim states one and the arbitrary leaf vector \(b\in\{0,1\}^n\).

## Proof
**Exact golden-mean conjugacy.** We prove
\[
F_n(E_n(s))=E_n(\rho(s))\quad(s\in\mathcal I_L).
\]
The initial rim bits satisfy \(a_i=s_i\lor s_{i-1}\) for indices modulo \(L\), with \(a_L=a_0\); the leaf bits are \(b_i=s_i\), with \(b_L=b_0\). We show inductively during the rim sweep that the freshly updated rim bit \(a_i'\) equals the initial bit \(a_{i+1}\) (indices modulo \(L\)). At \(i=0\), the left rim neighbor is \(a_L=a_0\), and the right is \(a_1\), so the occupied closed-neighborhood count is \(2a_0+a_1+s_0\). At each interior \(1\le i<L\), the already updated left neighbor is \(a_i\) by induction and the as-yet-unupdated right neighbor is \(a_{i+1}\); the count is again \(2a_i+a_{i+1}+s_i\). At the last site \(i=L\), both adjacent rim vertices have already been updated: their values are \(a_0\) and \(a_1\), while the old final rim/leaf pair is a repeat of pair zero. The count again has the same form as at \(i=0\).

For every such count, the local rule outputs precisely the indicated next rim bit: if \(a_i=0\) then \(s_i=0\) and the count is \(a_{i+1}\); if \(a_i=1,s_i=0\) the count is \(2+a_{i+1}\), passing the retention threshold three precisely when \(a_{i+1}=1\); and if \(s_i=1\) then cyclic independence forces \(s_{i+1}=0\), whence \(a_{i+1}=1\), and the count is four. Therefore the whole updated rim satisfies \(a_i'=a_{i+1}\). Every leaf has degree one, so the leaf sweep maps \(b_i\) to \(b_i'=a_i'(1-b_i)\). Consequently
\[
b_i'=(s_{j+1}\lor s_j)(1-s_j)=s_{j+1},
\]
using cyclic independence. These are exactly the bits of \(E_n(\rho(s))\). The map \(E_n\) is injective because its first \(L\) leaf bits recover \(s\). Thus it conjugates an invariant part of \(F_n\) to a bijective rotation, and every encoded state is periodic.

**Leaf-flipping component and overlap.** In \(U_n(b)\), each rim vertex counts at least itself and its two rim neighbors, so every rim bit remains one. Each leaf changes zero to one or one to zero. Hence \(F_n(U_n(b))=U_n(\mathbf1-b)\), giving exactly \(2^{n-1}\) distinct two-cycles. The encoded state \(E_n(s)\) lies in this component exactly when \(s_j\lor s_{j-1}=1\) at each position. Coupled with \(s_js_{j-1}=0\), this requires strict alternation, possible only for even \(L\), and then gives exactly two encoded states forming one of the already counted leaf-flipping two-cycles.

**Cardinalities and primitive periods.** Cyclic binary words of length \(L\ge2\) with no neighboring ones are counted by \(\operatorname{tr}(T^L)=\mathcal L_L\), for \(T=\begin{pmatrix}1&1\\1&0\end{pmatrix}\). Inclusion-exclusion of the overlap proves the displayed union cardinality. Rotation-fixed words at a divisor \(e\mid L\) are exactly periodic repetitions of an admissible cyclic length-\(e\) word, counted by \(\mathcal L_e\) (including \(\mathcal L_1=1\)). Möbius inversion gives the number of words with least rotation period \(d\) and division by \(d\) gives orbit numbers. The only period-one encoded word is the zero word; the two alternating encoded states at even \(L\) are already counted among \(U_n\)'s two-cycles. A cyclic word with a single one has least rotation period \(L\) for \(L\ge3\), proving the last assertion.

## Verification
The accompanying standard-library programs `verify_invariant.py` and `verify_full_small.py` independently implement the local permutation-sequential rule, coding, and orbit analysis. `verify_invariant.py` checked every cyclic independent word, the exact map conjugacy, overlap and divisor-period formulas for \(3\le n\le17\). `verify_full_small.py` exhaustively constructed the complete functional graphs for \(3\le n\le9\) (a total of \(349{,}504\) configurations). In those finite orders the constructed union actually equals the entire recurrent set; no such global completeness claim is made for arbitrary orders. These computations corroborate but are not substitutes for the all-size proof above.

The constructed union sizes for \(n=3,4,5,6,7,8,9\) are respectively \(9,20,37,75,144,285,557\). All required checks can be rerun with `python3 verify_invariant.py` and `python3 verify_full_small.py` in a directory containing the two attached scripts.

## Relationship to prior work
Kuhlman, Mortveit, Murrugarra and Kumar (2011), Proposition 3.6, exhibit a length-\(n-1\) periodic orbit for sequential \((1,3)\) bi-threshold dynamics on the **bare cycle**, and their Section 4 discusses graph constructions; they do not establish the pendant-leaf encoding above. A later result, *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, establishes a complete binary rotation on the undecorated cycle. A different result on majority dynamics of sunlets treats a synchronous majority rule, not this sequential hysteretic map. Those prior cyclic rotations and sunlet counts do not imply the explicitly proved additional leaf-flipping component, golden-mean admissibility, or the combined orbit counts on the decorated graph. Overlapping terminology does not establish statement implication.

## Limitations
The theorem counts a specified invariant periodic subsystem **exactly**, not all periodic points of the full map, and supplies no all-order transient bound or attraction-basin distribution. Although full state enumeration found no additional recurrent states for \(3\le n\le9\), extrapolating that finite observation would be unjustified. Independent mathematical validation has not been performed. Historical coverage outside the inspected sources and research records remains possible, including inaccessible full texts of closely related contemporary records.

## References
- C. J. Kuhlman, H. S. Mortveit, D. Murrugarra, and V. S. A. Kumar, *Bifurcations in Boolean Networks*, arXiv:1108.2974, first public preprint dated 2011-08-15. https://arxiv.org/abs/1108.2974
- Same work, open full text, *Discrete Mathematics & Theoretical Computer Science* proceedings, DOI:10.46298/dmtcs.2975, https://dmtcs.episciences.org/2975/pdf. See Sections 3.2 and 4, especially Proposition 3.6.
- *Binary-necklace attractors and triangular-run basins for sequential bi-threshold cycles*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-binary-necklace-attractors-and-triangular-run-basins-for-sequent--e79a108b9794 (indexed abstract consulted; full text inaccessible during comparison).
- *A parity-factorized periodic-orbit census for majority dynamics on sunlet graphs*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-parity-factorized-periodic-orbit-census-for-majority-dynamics--8a5efe3ce640 (indexed abstract consulted; full text inaccessible during comparison).
