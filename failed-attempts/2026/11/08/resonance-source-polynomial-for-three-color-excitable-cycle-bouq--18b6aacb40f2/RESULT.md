# Resonance-source polynomial for three-color excitable cycle bouquets

## Finding

Let \(G\) be a finite simple connected graph formed from \(m\ge2\) simple cycles of lengths \(\ell_1,\ldots,\ell_m\ge3\), all identified at exactly one common vertex \(o\), with otherwise disjoint vertices and edges. Any number of finite rooted trees may additionally be attached, each by identifying its root with any existing vertex. No additional identifications or edges are allowed. The resulting graph is a *tree-decorated cycle bouquet*.

For synchronous three-state, threshold-one Greenberg–Hastings dynamics \(U\) on \(\{0,1,2\}^{V(G)}\), define \(P_3(G)=|\{x:U^3x=x,\,Ux\ne x\}|\). Set
\[
 b_i=2\lfloor\ell_i/3\rfloor+1,\qquad
 a_i=2\mathbf{1}_{\{3\mid\ell_i\}}.
\]
For any initially primitive-three state \(x\), let \(J(x)\) count the petals having at least one of their two hub-adjacent vertices in the successor color; equivalently, it is the number of separate cycle petals independently able to advance the hub. Then the **complete resonance-source census polynomial** is
\[
 \boxed{R_G(t)=\sum_{U^3x=x,\,Ux\ne x}t^{J(x)}
 =3\left[\prod_{i=1}^m(b_i-a_i+a_i t)-\prod_{i=1}^m(b_i-a_i)\right].}
\]
In particular, the **complete immediate primitive-three population** and number of distinct primitive-three orbits are
\[
 \boxed{P_3(G)=R_G(1)=3\left(\prod_{i=1}^m b_i-\prod_{i=1}^m(b_i-a_i)\right),\qquad
 \#\mathcal O_3(G)=P_3(G)/3.}
\]
In particular, \(P_3(G)>0\) if and only if some bouquet cycle length is divisible by three. The formula is independent of the number, shapes, and attachment positions of the rooted trees. The all-zero state is the unique fixed point.

For the friendship graph with \(m\) triangular petals, \(R_G(t)=3[(1+2t)^m-1]\). Thus exactly \(3\binom{m}{j}2^j\) initial states have precisely \(j\) distinct cycle petals supporting the hub (\(1\le j\le m\)), and \(P_3=3(3^m-1)\), giving \(3^m-1\) distinct three-cycles. More generally, \(m\) petals of lengths \(3r_i\) contribute \(3[\prod_i(2r_i+1)-\prod_i(2r_i-1)]\) primitive-three states. This isolates the interaction between multiple independent sources of period-three excitation that share one hub. The source count has a deletion interpretation: after removing entire petal blocks (and any trees rooted on them), the restriction of a counted configuration remains fully cycling exactly when at least one of its supporting petals is retained.

## Assumptions and scope

A vertex in color \(1\) advances to \(2\), a vertex in color \(2\) advances to \(0\), and a vertex in color \(0\) advances to \(1\) precisely when at least one neighbor has color \(1\); otherwise it stays \(0\). Updates are simultaneous. Vertices are distinguished, and no quotient by graph automorphisms is taken. The count is for **initially periodic states of least period three**, not all states eventually entering a three-cycle. No assertions about higher-period or eventual-attractor populations are made.

The formula is meaningful even when no petal has length divisible by three, giving zero. For mathematical distinctness from the single-resonant-cycle situation, its principal new regime is at least two petals with lengths divisible by three. The case of two triangular petals also occurs as a special case of a separate triangular-chain enumeration; the formula covers arbitrary numbers and arbitrary lengths of petals, including mixed lengths, with optional tree decorations.

## Proof

**1. The periodic-state dichotomy.** If \(U^3x=x\), each vertex has either the static trace \((0,0,0)\) or cyclically advances at every update through all three colors. Indeed, the deterministic transitions \(1\to2\to0\) force any occurrence of \(1\) or \(2\) to complete a full three-step color cycle if its starting color returns after three steps. A vertex initially zero that ever advances likewise must advance in each of the three steps. Thus there are no other length-three traces.

If any vertex is cycling, each of its neighbors must cycle too: a static-zero neighbor would encounter the cycling vertex in color \(1\) during one of the three steps and would therefore advance. By connectivity, either every vertex cycles or every vertex is static zero. For a fully cycling configuration \(c\), every vertex \(v\) must have at least one neighbor of color \(c(v)+1\pmod3\) at time zero. This condition is also sufficient, since all colors then increase by one at every update. Thus \(P_3(G)\) equals the number of color assignments satisfying
\[
 \forall v\in V(G)\quad\exists w\sim v:\quad c(w)\equiv c(v)+1\pmod3.
\]
Every such assignment has least period exactly three. The sole fixed state is all zero because fixed colors \(1\) and \(2\) are impossible.

**2. Tree attachments are forced.** Consider one rooted attached tree. At each leaf, the only way to have a successor-colored neighbor is for the leaf to have color one less than its parent modulo three. Working from leaves toward the root, assume all descendants of a nonroot vertex have color one less than it. None can then provide its successor, so its parent must provide the successor; the vertex is consequently one less than its parent. This proves inductively that the unique compatible extension of a coloring at the attachment point assigns to a tree vertex at distance \(d\) from its root the root's color minus \(d\pmod3\). These tree neighbors never provide the successor color to their attachment point. Hence the trees contribute multiplicity one and change none of the cyclic support conditions at the bouquet vertices.

**3. Count one petal with the hub color fixed.** Choose any fixed hub color \(h\in\mathbb Z_3\). Number one petal's cycle vertices \(v_0=o,v_1,\ldots,v_{\ell-1},v_\ell=o\) in cyclic order, and put
\[
 d_i=c(v_i)-c(v_{i-1})\pmod3,\qquad 1\le i\le\ell.
\]
The return condition is \(\sum_i d_i\equiv0\pmod3\). At each interior vertex \(v_i\), its predecessor is successor-colored exactly when \(d_i=2\), and its next vertex is successor-colored exactly when \(d_{i+1}=1\). Therefore admissibility at every interior vertex is precisely \(d_i=2\) or \(d_{i+1}=1\) for \(1\le i<\ell\).

These transition restrictions show that every allowable difference word is **uniquely** of one of two forms:
\[
 (2^a,1^{\ell-a})\quad(0\le a\le\ell),\qquad
 (2^a,0,1^{\ell-a-1})\quad(0\le a<\ell).
\]
Here exponent notation within a word means repetition, including an empty repeated block. In the first family, the difference sum is \(\ell+a\), and in the second it is \(\ell+a-1\). There are, respectively, exactly the numbers of integers \(a\) in \([0,\ell]\) congruent to \(-\ell\pmod3\) and in \([0,\ell-1]\) congruent to \(1-\ell\pmod3\). Splitting into the three cases \(\ell\equiv0,1,2\pmod3\) gives \(2\lfloor\ell/3\rfloor+1\) assignments in each case. This is \(b(\ell)\), the number of petal phase assignments obeying all **non-hub** support conditions for a prescribed hub color.

The petal offers a successor-colored neighbor to the hub if and only if \(d_1=1\) or \(d_\ell=2\). Under the above word classification, these events occur only for the pure all-ones word and the pure all-twos word, respectively. Each has zero sum modulo three exactly when \(3\mid\ell\). Thus exactly \(a(\ell)=2\mathbf{1}_{\{3\mid\ell\}}\) of the \(b(\ell)\) petal assignments support the hub.

**4. Combine petals and check least periods.** Conditional on a fixed \(h\), the interiors of the petals are independent. A petal contributes \(a_i\) assignments that support the hub, each weighted by \(t\), and \(b_i-a_i\) that do not; hence its source-count factor is \(b_i-a_i+a_it\). Their product includes the configurations that fail to give the hub a successor in any petal, whose unweighted number is \(\prod_i(b_i-a_i)\). Subtracting those and multiplying by the three hub phases proves the resonance-source polynomial. Evaluation at \(t=1\) proves the total-population formula. Tree-extension uniqueness in step 2 gives the same result for decorated bouquets. Every counted state advances at each update, so its least period is exactly three; each orbit contains three different labelled states. Positivity follows since every \(b_i>0\) and \(b_i-a_i\ge1\), and strict product inequality holds exactly when at least one \(a_i=2\).

## Verification

Standalone programs `verify_local_counts.py` and `verify_orbits.py` accompany this result with their observed stdout. The first checks the petal phase count and hub-support count for each integer \(3\le\ell\le100\) with exact integer dynamic programming, and separately enumerates all anchored color assignments for \(3\le\ell\le11\). The second exhaustively evaluates three actual synchronous updates on 15 bouquets (some decorated by paths), inspecting 367,767 labelled states in total. It agrees with both the total count and the exact source-count coefficients in every tested instance, including two nonresonant petals, two or more resonant petals, mixed lengths, and decorated petals.

To reproduce: run `python verify_local_counts.py` and `python verify_orbits.py` using Python 3 (standard library only). These are finite checks; the all-length result follows from the proof, not the tests.

## Relationship to prior work

The three-state excitable-medium rule originates in Greenberg and Hastings (1978), and was developed in later work on spatial activity, including Durrett and Griffeath (1993). Gravner, Lyu and Sivakoff (first posted October 24, 2016; journal publication 2018) establish, for arbitrary finite connected graphs, an activity-versus-synchronization characterization in terms of a graph-derived 1-form. Their Theorems 3 and 5 concern limiting activity, synchronization, and probabilistic bounds, not this exact *initial* three-cycle population for bouquets.

Previous related enumerations for a cactus with exactly one resonant cycle, and for chains of triangles, cover important boundary cases but do not directly imply the multiple-resonant common-hub product-minus-product count. For example, three triangles meeting at one hub give \(P_3=78\), while a three-triangle chain has a different population because its cycles do not all meet at one hub. The source polynomial additionally distinguishes how many resonant petals sustain the common vertex; this redundancy profile is invisible to the mere oscillation criterion. The present count makes the gluing geometry explicit. The general framework of cyclic support conditions is elementary; no absolute priority claim is made.

## Limitations

This is only the immediate primitive-three census for bouquets and tree decorations, not a classification of other recurrent periods, non-bouquet cacti, or transient basins. The proof requires threshold one, exactly three colors, a single common petal hub, and attached components that are trees. External priority comparisons cannot exclude equivalent formulations in unindexed papers or inaccessible historical full texts. 

## References

1. J. M. Greenberg and S. P. Hastings, *Spatial Patterns for Discrete Models of Diffusion in Excitable Media*, SIAM Journal on Applied Mathematics 34 (1978), 515–523. DOI: 10.1137/0134040.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, preprint first submitted March 22, 1993, arXiv:patt-sol/9303002; Experimental Mathematics 2 (1993), 183–208.
3. J. Gravner, H. Lyu and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320 (first submitted October 24, 2016); Annals of Applied Probability 28 (2018), 3324–3357, DOI: 10.1214/17-AAP1350.
