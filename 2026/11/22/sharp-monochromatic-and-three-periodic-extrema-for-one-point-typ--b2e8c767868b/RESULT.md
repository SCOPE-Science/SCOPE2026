# Sharp monochromatic and three-periodic extrema for one-point types over rainbow-free coloured paths

## Finding
Let \(\mathcal K\) be the class of finite simple graphs whose edges, when present, carry exactly one of three named colours \(1,2,3\), with no triangle whose three edges have distinct colours. Nonedges are allowed. Let \(M\) be its countable homogeneous Fraïssé limit. Individually name the vertices \(v_1,\ldots,v_n\) of an induced path, whose edge \(v_iv_{i+1}\) has colour \(c_i\in\{1,2,3\}\). Write \(N(c_1,\ldots,c_{n-1})\) for the number of complete nonalgebraic singleton types over this named path, counting different assignments of edge colours and nonedges to the new vertex as different types.

**Theorem (all orders and all equality cases).** For every \(n\ge3\), the unique maximizing edge-colour words are the three monochromatic words, while the unique minimizing words are the six words in which every consecutive three edge colours are all distinct. Equivalently, a minimizing word repeats a permutation of \((1,2,3)\) periodically, truncated to length \(n-1\). At \(n=1,2\), the count is independent of the word.

Let \(U_n\) and \(L_n\) denote the maximum and minimum. The maxima are characterized exactly by
\[
U_1=4,\quad U_2=14,\qquad U_{n+2}=3U_{n+1}+2U_n\quad(n\ge1).
\]
For an explicit formula for every minimum, index rows and columns by \(0,1,2,3\), where \(0\) means no edge, and let \(T_c\) be the \(4\)-by-\(4\) zero-one matrix with
\[
(T_c)_{ab}=0\quad\Longleftrightarrow\quad
\{a,b,c\}=\{1,2,3\},
\]
and all remaining entries equal to \(1\). Set \(Q=T_1T_2T_3\), and \(R_0=I\), \(R_1=T_1\), \(R_2=T_1T_2\). For \(n-1=3q+r\), with \(0\le r\le2\),
\[
\boxed{L_n=\mathbf 1^{\mathsf T}Q^qR_r\mathbf 1.}
\]
Here \(Q\) has characteristic polynomial \(\lambda(\lambda^3-42\lambda^2-23\lambda+1)\). If \(\rho\) is the largest real root of \(\lambda^3-42\lambda^2-23\lambda+1\), then \(\rho\approx42.54011357\) and
\[
L_n=\Theta(\rho^{n/3}),\qquad
U_n=\Theta\!\left(\left(\frac{3+\sqrt{17}}2\right)^n\right).
\]
Consequently, \(U_n/L_n\) grows exponentially. The two per-vertex exponential bases are approximately \(3.49086362\) and \(3.56155281\), respectively.

The first separation occurs already for three old vertices: \(L_3=49\), \(U_3=50\). The respective numbers for four, five, and six old vertices are \((171,178)\), \((597,634)\), and \((2084,2258)\).

## Assumptions and scope
The language has three symmetric, irreflexive, pairwise disjoint binary relations, and all pairs outside these relations are nonedges. The only forbidden configurations are fully present rainbow triangles. A free amalgam over any common substructure adds no cross-relations, so cannot create such a triangle; hence \(\mathcal K\) is a free-amalgamation Fraïssé class. Its limit \(M\) is homogeneous with quantifier elimination. Every admissible one-point pattern occurs, and by free duplication occurs infinitely often, so is nonalgebraic. The old path is induced: there are no edges between nonconsecutive named vertices. The parameter vertices are pointwise named, not quotiented by reversal or colour permutations.

For \(n=1\), there are four possible relations from the new point to the sole parameter. For \(n=2\), every old edge colour forbids precisely two of the sixteen ordered two-state assignments, hence \(N=14\).

## Proof
**1. Extension states and transfer.** At each named vertex assign the state \(0\) (nonedge to the new point), or \(1,2,3\) (the edge colour to the new point). Because the old graph is an induced path, the only triangles involving the new point consist of that point and two consecutive old vertices. For an old edge of colour \(c\), the two new states are forbidden exactly when they are the other two distinct nonzero colours. Thus the exact count for any word is
\[
N(c_1,\ldots,c_{n-1})=
\mathbf1^{\mathsf T}T_{c_1}\cdots T_{c_{n-1}}\mathbf1.
\]
Let \(v=(v_0,v_1,v_2,v_3)\) count admissible prefixes ending in each state, and set \(S=\sum_i v_i\). Appending an old edge of colour \(c\), with other colours \(a,b\), yields
\[
v'_0=v'_c=S,\quad v'_a=S-v_b,\quad v'_b=S-v_a,\quad
S'=4S-v_a-v_b.
\]

**2. A sorted-deficit comparison principle.** For the three nonzero colours define \(\delta_i=S-v_i\), and write their increasing rearrangement as \(d_1\le d_2\le d_3\). Always \(0\le d_i\le S\). If the appended old-edge colour is excluded from this triple, and the two retained deficits are \(a\le b\), substitution into the preceding recurrence gives
\[
\boxed{
(S';d'_1,d'_2,d'_3)=
(2S+a+b;\ S+a+b,\ 2S+a,\ 2S+b).}
\]
The claimed order of the three new deficits is valid because \(a,b\le S\), hence \(S+a+b\le2S+a\le2S+b\). The displayed map is coordinatewise nondecreasing in \(S,a,b\).

Among the three ways to choose a pair of retained deficits, \((d_1,d_2)\) is coordinatewise smallest and \((d_2,d_3)\) is coordinatewise largest. Therefore the next *entire sorted state*, not just its total, is minimized by excluding the largest deficit and maximized by excluding the smallest. Both greedy maps are coordinatewise monotone on ordered states. Starting from the same initial state, induction gives universal lower and upper bounds on the state after every number of edges, under every colour word. These bounds are attained by the respective greedy choices, so they are global and not merely one-step optima.

**3. All equality cases.** Before any old edge, \(S=4\) and \((d_1,d_2,d_3)=(3,3,3)\), so the first colour is arbitrary. After the first edge, \(S=14\) and \((d_1,d_2,d_3)=(10,11,11)\). The smallest deficit belongs uniquely to the most recent edge colour. Hence every maximizing continuation must repeat that colour. Repeating it preserves this strict minimum by the formula in step 2, proving that all maximizers are monochromatic.

For minimization, the second edge must differ from the first, with two equally optimal choices. With two different colours, the next state has \(S=49\) and deficits \((35,38,39)\), with the largest deficit attached to the one previously unused colour. The next minimizing step must choose that unused colour. The deficit formula then makes the colour three positions back the unique next maximizing deficit; the same rule continues indefinitely, forcing repetition of a permutation of the three colours. At any non-greedy choice with unequal relevant deficits, the new total \(S'\) increases (for minimization) or decreases (for maximization) strictly, and monotonicity retains the strict total inequality for every continuation. Thus there are no other equality cases.

**4. Closed forms and growth.** For a monochromatic word, symmetry identifies the two coordinates \(v_0,v_c\) and the two remaining coordinates. Their two-dimensional update matrix is
\[
\begin{pmatrix}2&2\\2&1\end{pmatrix},
\]
with characteristic polynomial \(\lambda^2-3\lambda-2\). This gives the stated recurrence for \(U_n\). For a minimizing word, the three transfer matrices recur periodically and yield \(L_n=\mathbf1^{\mathsf T}Q^qR_r\mathbf1\). Direct multiplication gives
\[
Q=\begin{pmatrix}
14&10&11&14\\
14&10&11&14\\
11&8&8&11\\
10&7&8&10
\end{pmatrix},
\]
whose characteristic polynomial is \(\lambda(\lambda^3-42\lambda^2-23\lambda+1)\). Since all entries of \(Q\) are strictly positive, Perron–Frobenius theory gives the claimed exponential growth for each of the three residue classes of \(n-1\). Its Perron root is \(\rho\). The cubic polynomial is negative at \(42\) and positive at \((7/2)^3=343/8\), whereas its other positive root lies between \(0\) and \(1\); hence \(\rho<(7/2)^3\). The maximum matrix has Perron root \((3+\sqrt{17})/2>7/2\), strictly greater than \(\rho^{1/3}\), proving exponential separation.

## Verification
The standalone Python 3 file `verify.py` contains two independently implemented finite counters: direct enumeration of all \(4^n\) extension-state words, and four-state transfer dynamic programming. It compares these for all \(364\) path edge-colour words through six vertices. It then enumerates all \(88{,}573\) old-edge-colour words through eleven vertices, checking extremal values and the full list of equality words. It independently evaluates the periodic matrix formula and monochromatic recurrence up to thirty-four vertices and checks the characteristic polynomial by exact integer matrix arithmetic. Its recorded output in `verify_output.txt` ends with `VERIFY_OK`.

Finite checks are illustrations, not the all-order proof; the all-order result follows from the sorted-deficit induction.

## Relationship to prior work
The free-amalgamation framework and finite-type realization principle lie in the general setting of Conant's 2015 paper. Earlier Gallai-colouring research, especially Hoppen–Lefmann–Odermann and Bastos–Benevides–Mota–Sau, studies rainbow-free edge colourings and their extension counts, primarily with complete old graphs or all edges of a prescribed host required to be coloured. Those theorems do not establish the sharp maximum/minimum or equality cases here, where the old graph is a sparsely coloured induced path and each new-to-old relation also permits a nonedge.

Several numerical sequences are independently recorded in OEIS under other combinatorial interpretations: the maximal values \(4,14,50,178,634,\ldots\) appear as a row of A285266 (also A255256), and the minimal values \(14,49,171,597,2084,\ldots\) occur in A251228. Accordingly, no novelty is claimed for those numerical sequences alone. The contribution claimed here is the all-length sharp extremal comparison over all old-edge colourings, its complete rigidity of equality cases and its interpretation for nonalgebraic singleton types.

## Limitations
The theorem requires exactly three named edge colours, allowed nonedges, rainbow-triangle prohibition, and old bases that are induced paths. It counts singleton types over *pointwise named* bases; automorphism-orbit counts, cyclic bases, additional forbidden configurations, extra colours and higher-arity types are not covered. The old literature may contain an equivalent path-constrained matrix-product extremum under different terminology; historical priority is not independently certified. No independent mathematical audit has been performed.

## References
1. Gabriel Conant, *An axiomatic approach to free amalgamation*, arXiv:1505.00762, first submitted 4 May 2015, https://arxiv.org/abs/1505.00762.
2. Carlos Hoppen, Hanno Lefmann and Knut Odermann, *On graphs with a large number of edge-colorings avoiding a rainbow triangle*, preprint and EuroComb 2015 precursor, https://www.tu-chemnitz.de/informatik/ThIS/downloads/publications/exact_rainbow_triangle_preprint.pdf.
3. Josefran de Oliveira Bastos, Fabrício Siqueira Benevides, Guilherme Oliveira Mota and Ignasi Sau, *Counting Gallai 3-colorings of complete graphs*, arXiv:1805.06805, submitted 17 May 2018, https://arxiv.org/abs/1805.06805.
4. OEIS A285266, *Words with adjacent elements differing by at most two*, https://oeis.org/A285266; OEIS A255256, *Binary rectangular arrays avoiding monochromatic-corner squares*, https://oeis.org/A255256; OEIS A251228, *Binary arrays avoiding a local diagonal pattern*, https://oeis.org/A251228.
