# Missing maximal individual periods in one-sided majority waves on binary rings

## Finding
For every integer \(n\ge5\), take a labelled cyclic binary ring with simultaneous local rule
\[
(F_n x)_i=\operatorname{maj}(x_{i-1},x_{i-2},x_{i-3}),\qquad i\in\mathbb Z/n\mathbb Z.
\]
Let \(L_0=2\), \(L_1=1\), and \(L_{d+2}=L_{d+1}+L_d\). Write
\[
K(d)=L_d+2\cos(\pi d/3),\qquad d\ge1.
\]
**Theorem.** Every configuration eventually becomes periodic. Its initially periodic states are exactly all cyclic words without isolated symbols (every maximal constant-color cyclic run has length at least two), plus the two alternating words when \(n\) is even. For every integer \(k\ge1\), the *entire exact periodic-point census* is
\[
\boxed{\#\operatorname{Fix}(F_n^k)=K(\gcd(n,2k))+2\mathbf1_{\{2\mid n\}}\mathbf1_{\{2\mid k\}}.}
\]
The exact number of distinct primitive temporal cycles of length \(k\) is
\[
\boxed{C_n(k)=\frac1k\sum_{d\mid k}\mu(k/d)\left[K(\gcd(n,2d))+2\mathbf1_{\{2\mid n\}}\mathbf1_{\{2\mid d\}}\right].}
\]
The global period of the recurrent restriction satisfies
\[
\boxed{\operatorname{ord}(F_n|_{\mathrm{Rec}})=
\begin{cases}n,&n\text{ odd or }n\equiv2\pmod4,\\ n/2,&4\mid n.\end{cases}}
\]
**Nonattainment phenomenon.** In the infinite family \(n\equiv2\pmod4\), no *individual* configuration has period \(n\), even though the global recurrent map has order \(n\). Instead, the global order is the least common multiple of an actual period \(n/2\) and an independent actual period two.

## Assumptions and scope
The ring is finite, has \(n\ge5\) indexed sites, and uses simultaneous deterministic updates of the three preceding *distinct* sites. A configuration is initially periodic if \(F_n^k(x)=x\) for some \(k\ge1\). Every state is counted separately with its labelled locations; there is no spatial-rotation or bit-complement quotient. The global recurrent order is the smallest positive integer that fixes *every* initially periodic state. It is not defined as the largest individual orbit length. Define the right rotation \((Sx)_i=x_{i-1}\), the standard three-site centered majority \((Mx)_i=\operatorname{maj}(x_{i-1},x_i,x_{i+1})\), and the cyclic wall variable \(e_i=x_i\oplus x_{i+1}\).

## Proof
**Step 1: rotation and Lyapunov reduction.** All spatial shifts commute with \(M\). By coordinate inspection, \(F_n=S^2M=MS^2\), so for each \(k\ge1\), \(F_n^k=S^{2k}M^k\). A centered-majority update changes the bit at position \(i\) exactly when its two incident walls are both one. Thus its new wall word obeys
\[
e_i'=e_i(1\oplus e_{i-1}\oplus e_{i+1}),
\]
with all algebra in \(\mathbb F_2\). In particular walls cannot be created, and the total count of walls is nonincreasing under \(F_n\) (a spatial rotation merely permutes the walls). If a state is periodic, it cannot lose any wall over a complete orbit. At that state, every one-wall therefore has equal neighboring wall values. A cyclic binary wall word with this property has either no adjacent one-walls (hence the underlying color word has no isolated color) or consists entirely of ones. The latter is compatible with a cyclic color word precisely when \(n\) is even; it gives the two alternating words.

Conversely, on the set \(\mathcal W_n\) of words without isolated colors, the centered majority fixes every bit and \(F_n=S^2\); hence every state in \(\mathcal W_n\) is periodic. If \(n\) is even, the two alternating words are interchanged by \(M\), preserved by the even spatial shift \(S^2\), and form a genuine period-two orbit. Thus these and only these states recur. A deterministic map on a finite state space eventually enters some periodic orbit, proving the assertion about all other states.

**Step 2: transfer enumeration.** A cyclic word lies in \(\mathcal W_d\) precisely when none of its consecutive triples is \(010\) or \(101\). In the ordered pair states \(00,01,10,11\), adjoining the next bit gives the adjacency matrix
\[
B=\begin{pmatrix}1&1&0&0\\0&0&0&1\\1&0&0&0\\0&0&1&1\end{pmatrix}.
\]
Closed length-\(d\) paths correspond bijectively to labelled cyclic admissible words, including \(d=1,2\), so \(|\mathcal W_d|=\operatorname{tr}(B^d)\). Direct determinant expansion gives
\[
\det(zI-B)=(z^2-z-1)(z^2-z+1).
\]
The first quadratic contributes the Lucas number \(L_d\) to the trace, and the roots of the second, \(e^{\pm i\pi/3}\), contribute \(2\cos(\pi d/3)\). Thus \(|\mathcal W_d|=K(d)\).

**Step 3: fixed times.** A recurrent nonalternating configuration is fixed by \(F_n^k\) exactly when it is invariant under the spatial shift \(S^{2k}\). Such a word on an \(n\)-ring is the repetition of a unique word on a \(d=\gcd(n,2k)\)-ring, and avoiding isolated colors is equivalent under this repetition. There are exactly \(K(d)\) such states. The alternating pair exists when \(n\) is even and is fixed by \(F_n^k\) exactly when \(k\) is even. This proves the first boxed formula. For any finite transformation, every state fixed by its \(k\)-th iterate has least period dividing \(k\), so ordinary Möbius inversion gives the second boxed formula, with division by \(k\) because each length-\(k\) temporal orbit contains \(k\) distinct states.

**Step 4: global order and missing maximal individual period.** For \(n\ge5\), the cyclic word of exactly two consecutive zeros and \(n-2\) consecutive ones is in \(\mathcal W_n\) and has minimal *spatial* period exactly \(n\): it has one zero block of length two. Its temporal period under \(S^2\) is \(n/\gcd(n,2)\), the maximal possible among states in \(\mathcal W_n\). When \(n\) is odd the alternating states do not exist, so the global period equals \(n\). When \(n\) is even, the additional alternating orbit has period two. Therefore the global order is \(\operatorname{lcm}(n/2,2)\), equal to \(n/2\) when \(4\mid n\) and equal to \(n\) when \(n\equiv2\pmod4\). In the latter case every nonalternating state has period dividing the odd number \(n/2\), while alternating states have period two; neither type can have period \(n\). This establishes nonattainment without assuming that a global order must occur as an individual orbit length.

## Verification
The standalone dependency-free script `verify_oneway.py` independently constructs the full functional graph for every size \(5\le n\le14\), identifies its cycles, and checks the periodic membership, fixed-time formula at every \(1\le k\le n\), exact global order, and nonattainment when \(n\equiv2\pmod4\). It checks \(2^5+\cdots+2^{14}=32736\) labelled initial states, printing `ALL FINITE CHECKS PASSED`. Sample checks: at \(n=6\) there are 22 periodic states and temporal periods \(1,2,3\), never six; at \(n=10\) there are 124 periodic states with periods \(1,2,5\), never ten. These finite enumerations corroborate the unbounded proof but do not replace it.

## Relationship to prior work
Fukś (1997) analyzes the centered symmetric majority Rule 232 as part of cellular-automaton density classification. Lemoy and coauthors (2013) study a noisy version of centered majority, while Nakar and Ron (2022) analyze the recurrent structures for centered one-dimensional majority. The known centered rule and its stable patterns are inputs here, not claimed as novel.

The directly relevant published result *Sharp last-entry mass in a rotating majority-feedback ring* counts a different feedback map, shifting the state by one site while applying a majority gate to a single site per update; it also uses the classical no-isolated-word population \(K(d)\) and already gives the temporal orbit count for **one-site** rotation of that stable set. This establishes useful antecedents but does not give the present *fully parallel directed* map, its doubled spatial shift, its separate alternating two-cycle, or the missing-maximal-individual-period phenomenon. *Exact entrance-time census and logarithmic settling for cyclic majority dynamics* provides all temporal entry layers for the centered rule, but its initially periodic states are either fixed or alternating; no full directed-orbit classification follows without analyzing the shift factor. The statements of these results and their implications were compared, not just their titles.

## Limitations
The graph is a directed cyclic dependency network; the rule is not the usual open-neighbor majority on an undirected graph. The transfer matrix counts a classical forbidden-pattern language, which is not independently novel; originality and motivation concern its directed temporal interpretation, arithmetic orbit census, and nonattainment of the global period. For broader generalizations \(F=S^aM\), a related prior formula may specialize immediately. The theorem does not provide a detailed basin-size or first-entry-time distribution for the directed system, or stochastic robustness. A historical paper using an equivalent shift-centered-rule decomposition could supersede its priority; the searched records are not a complete uniqueness guarantee.

## References
1. H. Fukś, *Solution of the Density Classification Problem with Two Cellular Automata Rules*, first public arXiv version March 7, 1997, https://arxiv.org/abs/comp-gas/9703001 .
2. R. Lemoy et al., *Transfer matrix analysis of one-dimensional majority cellular automata with thermal noise*, first public arXiv version November 18, 2013, https://arxiv.org/abs/1311.4388 .
3. Y. Nakar and D. Ron, *The Structure of Configurations in One-Dimensional Majority Cellular Automata: From Cell Stability to Configuration Periodicity*, 2022, https://arxiv.org/abs/2205.08972 .
4. *Sharp last-entry mass in a rotating majority-feedback ring*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-last-entry-mass-in-a-rotating-majority-feedback-ring--08f53e11cf2e .
5. *Exact entrance-time census and logarithmic settling for cyclic majority dynamics*, public result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-entrance-time-census-and-logarithmic-settling-for-cyclic-m--380fba13c913 .
