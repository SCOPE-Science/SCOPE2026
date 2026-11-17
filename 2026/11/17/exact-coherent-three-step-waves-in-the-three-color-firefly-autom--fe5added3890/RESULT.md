# Exact coherent three-step waves in the three-color firefly automaton on cyclic rings

## Finding
For every integer \(n\ge3\), put three-color inhibitory firefly oscillators on the labelled cycle \(C_n\), with simultaneous updating. Let \(F_n\) denote their update and let \(S_n\) be the one-site spatial shift \((S_nx)_i=x_{i+1}\). The exact number of **coherent three-step traveling-wave configurations** satisfying at least one of the equations
\[
F_n^3x=S_nx,\qquad F_n^3x=S_n^{-1}x
\]
is
\[
\boxed{W_n=2a_n-3,}
\]
where the integer sequence is defined by
\[
a_3=3,\ a_4=7,\ a_5=18,\ a_6=39,\qquad
\boxed{a_n=3a_{n-1}-3a_{n-2}+a_{n-3}+a_{n-4}\quad(n\ge7).}
\]
The count of genuinely nonuniform coherent waves is \(W_n-3=2a_n-6\). Each configuration in this set is already temporally periodic, with period dividing \(3n\), and there are no transient steps required.

The sequence begins as follows:

| Ring length \(n\) | One direction \(a_n\) | Both directions \(W_n\) | Nonuniform waves |
|---:|---:|---:|---:|
| 3 | 3 | 3 | 0 |
| 4 | 7 | 11 | 8 |
| 5 | 18 | 33 | 30 |
| 6 | 39 | 75 | 72 |
| 7 | 73 | 143 | 140 |
| 8 | 127 | 251 | 248 |
| 9 | 219 | 435 | 432 |
| 10 | 388 | 773 | 770 |

Let \(\rho=1.819172513396\ldots\) be the unique real root greater than one of
\[
\rho(\rho-1)^3=1.
\]
Then \(W_n\sim2\rho^n\): the population of coherent traveling waves grows exponentially, although its fraction of all \(3^n\) initial states tends to zero.

## Assumptions and scope
The graph is a simple cyclic ring with \(n\ge3\) individually labelled sites, indices modulo \(n\). Each state \(x_i\) is in \(\{0,1,2\}\). The blinking state is \(1\). The single-site update is
\[
(F_nx)_i=\begin{cases}
2,&x_i=2\ \text{and}\ (x_{i-1}=1\ \text{or}\ x_{i+1}=1),\\
x_i+1\pmod3,&\text{otherwise}.
\end{cases}
\]
All sites use old neighbors' states. The spatial shift is chosen as \((S_nx)_i=x_{i+1}\); reflection interchanges the two displayed wave equations. All counts concern labelled configurations, not classes modulo spatial rotation or color cycling. In this theorem “coherent” is **defined** by the displayed three-step translation condition; no claim is made that it contains every periodic configuration of this automaton.

## Proof
**1. Finite-window representation.** The local rule has spatial radius one, hence the color at site \(i\) after three iterations depends only on the seven initial sites \(i-3,\ldots,i+3\). Let \(h(a,b,c)\) be the displayed local rule and let \(H(w_0,\ldots,w_6)\) be its exact three-step composition at the center \(w_3\). Explicitly, take
\[
b_j=h(w_{j-1},w_j,w_{j+1})\ (1\le j\le5),\quad
c_j=h(b_j,b_{j+1},b_{j+2})\ (1\le j\le3),\quad
H(w)=h(c_1,c_2,c_3).
\]
The condition \(F_n^3x=S_nx\) is equivalent to requiring \(H(x_{i-3},\ldots,x_{i+3})=x_{i+1}\) at every site \(i\).

Construct a directed graph whose vertices are all six-letter words over \(\{0,1,2\}\). For each seven-letter word \(w\), place an edge from \((w_0,\ldots,w_5)\) to \((w_1,\ldots,w_6)\) exactly when \(H(w)=w_4\). The graph has 729 possible vertices and 1,179 edges. An indexed ring configuration satisfying the positive-direction equation corresponds uniquely to a closed directed walk of length \(n\) in this graph, by the standard overlapping-window bijection. This remains true for \(3\le n<7\): a closed walk automatically imposes exactly the necessary repetitions under modulo-\(n\) indexing. If \(A\) is the adjacency matrix, the number of such configurations is \(\operatorname{tr}(A^n)\).

**2. Exact finite graph certificate.** The self-contained code `check_transfer.py` enumerates all \(3^7\) seven-letter words directly from the three-fold local rule, computes strongly connected components by Tarjan's algorithm, and checks that precisely one component contains a directed cycle. This cyclic component has **65 vertices and 118 edges**. Every closed walk is contained in it. If \(B\) is its explicitly generated integer adjacency matrix, its characteristic polynomial is exactly
\[
\boxed{\det(\lambda I-B)=\lambda^{61}(\lambda^4-3\lambda^3+3\lambda^2-\lambda-1).}
\]
This identity is checked without a numerical eigenvalue routine: the program computes the first 65 exact integer walk traces and reconstructs all 65 characteristic coefficients by Newton's identities, verifying each required integer divisibility and every coefficient. Thus the displayed determinant is an exhaustive finite certificate, not a numerical extrapolation.

Write \(a_n=\operatorname{tr}(B^n)\). Newton's identities give the initial power sums \(a_1=a_2=a_3=3\), \(a_4=7\), and the quartic characteristic factor yields the four-term recurrence for all \(n\ge5\). Restricting to actual rings \(n\ge3\) gives the asserted starting values and recurrence. Reflection of the ring conjugates the rule with itself and exchanges \(S_n\) with \(S_n^{-1}\), so the negative-direction equation has exactly the same number \(a_n\) of solutions.

**3. Intersection and temporal periodicity.** If both wave equations hold then \(S_nx=S_n^{-1}x\), so \(S_n^2x=x\). For odd \(n\), this forces spatial uniformity. For even \(n\), it forces alternating colors \((a,b,a,b,\ldots)\). There are only nine ordered alternating pairs \((a,b)\). The two-site quotient has an explicit three-update table: for the six unequal pairs, the unordered pairs \(\{0,1\}\), \(\{1,2\}\), \(\{0,2\}\) each collapse respectively to the constant pairs \((0,0)\), \((1,1)\), \((2,2)\). Thus none of the six unequal cases can satisfy \(F_n^3x=S_nx\). The other three are the uniform configurations, which each perform an unimpeded three-color clock and satisfy both equations. Therefore the two direction sets intersect in exactly three configurations for every \(n\ge3\), giving \(W_n=2a_n-3\) by inclusion-exclusion.

Because the rule commutes with spatial shifts, any positive-direction coherent state obeys \(F_n^{3n}x=S_n^nx=x\); the negative direction is identical. Hence all counted states are genuinely recurrent and their least temporal periods divide \(3n\). The three spatially uniform configurations are the only coherent states counted in both directions.

**4. Exponential law.** The unique cyclic component is strongly connected and contains a self-loop, so its nonnegative adjacency matrix is primitive. Perron–Frobenius theory gives a unique spectral radius \(\rho>1\) that strictly dominates all other eigenvalues. Its nonzero eigenvalues are exactly the four roots of \(\lambda(\lambda-1)^3=1\). The positive dominant root lies in the interval \((1.819,1.820)\). The exact trace formula implies \(a_n=\rho^n+o(\rho^n)\), hence \(W_n\sim2\rho^n\). Since \(\rho<3\), coherent waves form an exponentially small fraction of all \(3^n\) labelled states.

## Verification
Run `python3 check_transfer.py` and `python3 check_direct.py` using only the Python standard library. The first program exhaustively enumerates the finite-radius local constraints, verifies the 65-state directed-cycle graph, and reconstructs the characteristic polynomial from 65 exact Newton identities. The second program independently implements the simultaneous firefly update on every labelled three-color ring of sizes three through ten; it checks both directional populations, their intersection and their inclusion-exclusion total, and directly confirms the predicted temporal periodicity. It also checks the six nonconstant alternating color pairs separately. Captured outputs appear in `check_transfer.out` and `check_direct.out`.

The exhaustive local constraint certificate proves the formula for every ring size. The direct finite-ring enumeration is a cross-check, not an extrapolation from small sizes. The characteristic-polynomial certificate and full source are included rather than relying on logs alone.

## Relationship to prior work
The local firefly rule was introduced by Lyu (2014), whose author-posted primary text defines the rule and analyzes synchronization on paths and trees, with qualitative remarks on cycles, but does not state the all-circumference coherent-wave counting formula. Lyu and Sivakoff (2017) develop its particle-system representation on the infinite integer line and prove stochastic clustering estimates; the accessible full text, especially the model and particle-expansion sections and main theorems, does not state the finite-ring three-step translation count or the quartic spectral polynomial.

Published exact studies of the same three-color rule on star and crown graphs classify synchronization and basin behavior on different graph families; those results do not entail the cyclic-ring wave count. A published exact rotating-wave census for a row-constant cyclic-dominance torus uses a different update (successor-contact growth, rather than inhibitory blinking) and different geometry. Standard de Bruijn transfer and Perron–Frobenius methods are credited as tools, not new inventions. The specific finite-ring wave population and quartic reduction are the contribution here.

## Limitations
The result concerns only initial configurations satisfying the explicit coherent three-step translation equation. It is not a classification of every recurrent configuration, its least temporal period, its basin, or its approach to recurrence. For \(n\le10\), direct experiments suggest a broader recurrence classification, but no such general theorem is asserted or used. The claim concerns the original three-color blinking rule, synchronous updates, and simple spatial cycles; changing the update convention or network changes the objects being counted. Although the original author-posted work, relevant later full text, and mathematical records were consulted, historical priority cannot be certified against every unindexed earlier calculation. Independent mathematical validation has not been performed.

## References
1. H. Lyu, “Synchronization of finite-state pulse-coupled oscillators,” original preprint publicly dated 2014-07-04, https://arxiv.org/abs/1407.1103; author-posted original text https://www.researchgate.net/publication/263699436_A_Self-stablizing_Cellular_Automata_Model_For_Pulse-coupled_Biological_Oscillators.
2. H. Lyu and D. Sivakoff, “Synchronization of finite-state pulse-coupled oscillators on \(\mathbb Z\),” public preprint 2017, https://www.researchgate.net/publication/312031282_Synchronization_of_finite-state_pulse-coupled_oscillators_on_mathbbZ.
3. “Exact seven-layer synchronization census for three-color firefly stars,” mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-exact-seven-layer-synchronization-census-for-three-color-firefly--08a45788815d.
4. “Crown-graph firefly dynamics: sharp transient cutoff and exact period basins,” mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-crown-graph-firefly-dynamics-sharp-transient-cutoff-and-exact-pe--a1379f43d361.
5. “Exact winding basins and complete temporal-cycle census for striped cyclic-dominance tori,” mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-winding-basins-and-complete-temporal-cycle-census-for-stri--d6a7948b82ed.
