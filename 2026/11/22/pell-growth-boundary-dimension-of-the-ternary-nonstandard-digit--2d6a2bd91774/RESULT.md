# Pell-growth boundary dimension of the ternary nonstandard digit scaling set

## Finding

Let \(\mathscr S\) be the set of nonnegative integers representable as finite sums \(\sum_{j\ge0}\varepsilon_j3^j\) with digits \(\varepsilon_j\in\{0,1,5\}\). For \(N\ge1\), set
\[
E_N=\bigcup_{\substack{0\le m<3^N\\m\in\mathscr S}}[m/3^N,(m+1)/3^N).
\]
The indicators \(\mathbf 1_{E_N}\) stabilize almost everywhere to a measurable limit \(\mathbf 1_E\). Define its **essential boundary** by
\[
\partial_{\rm ess}E=\{x\in[0,1]:\text{every relative open neighborhood of }x\text{ intersects both }E\text{ and }[0,1]\setminus E\text{ in positive Lebesgue measure}\}.
\]
This definition is invariant under modifications of \(E\) on null sets. The exact Hausdorff dimension is
\[
\boxed{\dim_{\rm H}(\partial_{\rm ess}E)=\frac{\log(1+\sqrt2)}{\log3}=0.8022608122\ldots.}
\]
More precisely, a ternary prefix is called *undetermined* if there exist two finite lower-order continuations that ultimately give different membership outcomes. Writing \(a_n\) for the number of undetermined prefixes of length \(n\), including the empty word, one has the exact ordinary generating function
\[
\boxed{\sum_{n\ge0}a_nz^n=\frac{1}{(1-z)(1-2z-z^2)}.}
\]
Thus \(a_0,a_1,\ldots=1,3,8,20,49,119,288,696,1681,\ldots\); the same dimension is the Hausdorff and both box dimensions of the closed survivor set of infinite undetermined prefixes.

## Assumptions and scope

All integer representations are finite (eventually zero digit sequences). Ternary prefixes are read most-significant digit first, while integer representability is tested least-significant digit first. The statement concerns the measurable scaling limit of the *fixed* digit set \(\{0,1,5\}\); it is not asserted for every digit set or every Hausdorff-topological representative of an almost-everywhere equivalence class. Endpoints of ternary intervals form a countable exceptional set for the symbolic identification. Dimensions refer to subsets of the real interval \([0,1]\).

## Proof

**1. Carry test and reachable states.** Let \(d_0=0,d_1=1,d_2=5\), and for a standard ternary input digit \(a\in\{0,1,2\}\) define the integer carry map
\[
h_a(c)=\frac{a+c-d_{(a+c)\bmod3}}3.
\]
An integer belongs to \(\mathscr S\) exactly when iterating these maps on its standard ternary digits from least to most significant, starting at carry \(0\), terminates in carry \(0\). This follows by subtracting at each place the unique allowed digit congruent to the current integer modulo three; a remaining negative carry cannot be removed by leading zero input digits. The reachable carry set is exactly \(C=\{-2,-1,0\}\): for these states, the rows \((h_0,h_1,h_2)\) are respectively \((-1,-2,0)\), \((-2,0,0)\), and \((0,0,-1)\). Each state is attainable from initial carry \(0\) by a finite lower-order input.

**2. Reverse subset automaton.** For a most-significant prefix \(u=a_1\cdots a_n\), put
\[
B_u=\{c\in C:h_{a_1}\circ\cdots\circ h_{a_n}(c)=0\}.
\]
Here the rightmost map acts first. Thus \(B_{\emptyset}=\{0\}\) and \(B_{ua}=h_a^{-1}(B_u)\cap C\). The sets \(\emptyset\) and \(C\) are absorbing and imply uniform exclusion/inclusion on the entire corresponding ternary cylinder at every later scale. The remaining states, in the order
\[
A=\{0\},\quad B=\{-1,0\},\quad F=\{-2,-1\},\quad D=\{-2,0\},\quad U=\{-2\},\quad V=\{-1\},
\]
form an invariant six-state transient graph. Its transitions on symbols \(0,1,2\), with \(\star=C\) and \(\varnothing=\emptyset\), are:

| State | 0 | 1 | 2 |
|---|---|---|---|
| \(A\) | \(A\) | \(B\) | \(F\) |
| \(B\) | \(D\) | \(B\) | \(\star\) |
| \(F\) | \(F\) | \(U\) | \(A\) |
| \(D\) | \(B\) | \(\star\) | \(F\) |
| \(U\) | \(V\) | \(U\) | \(\varnothing\) |
| \(V\) | \(U\) | \(\varnothing\) | \(A\) |

Each of the six transient states has a finite extension to \(C\) and another to \(\emptyset\) (e.g. use graph search on the displayed transition table). Consequently every undetermined cylinder contains smaller open cylinders with full inclusion and full exclusion; both have positive Lebesgue measure in the limit.

**3. Exact word counts.** Omitting absorbing destinations gives the nonnegative adjacency matrix
\[
T=\begin{pmatrix}
1&1&1&0&0&0\\
0&1&0&1&0&0\\
1&0&1&0&1&0\\
0&1&1&0&0&0\\
0&0&0&0&1&1\\
1&0&0&0&1&0
\end{pmatrix}.
\]
The graph is strongly connected and right resolving. With the first standard basis row \(e_A^{\mathsf T}\) and the all-ones column \(\mathbf1\), the exact count is \(a_n=e_A^{\mathsf T}T^n\mathbf1\). Direct inversion over rational functions gives
\[
e_A^{\mathsf T}(I-zT)^{-1}\mathbf1=\frac{1}{(1-z)(1-2z-z^2)}.
\]
Equivalently \(a_n=3a_{n-1}-a_{n-2}-a_{n-3}\) for \(n\ge3\), with initial values \((1,3,8)\). The characteristic polynomial of \(T\) is \((t-1)^3(t+1)(t^2-2t-1)\). By irreducibility its Perron root is \(\lambda=1+\sqrt2\), and \(a_n\asymp\lambda^n\).

**4. Scaling limit and fractal boundary.** The union \(U_n\) of the \(a_n\) undetermined ternary cylinders has measure \(a_n3^{-n}\to0\), and \(U_{n+1}\subseteq U_n\). Outside \(\bigcap_nU_n\), a finite prefix reaches an absorbing state and determines every subsequent membership value. This proves pointwise stabilization almost everywhere and identifies the measurable limit \(E\). Let \(K\) be the compact set of real numbers with at least one infinite ternary coding that stays in the transient six-state graph. Outside the countable set of ternary endpoints, the neighborhood criterion above implies \(\partial_{\rm ess}E=K\). In full generality their symmetric difference is contained in that countable endpoint set; it does not affect Hausdorff dimension.

The upper bound \(\dim_{\rm H}K\le\log_3\lambda\) follows by covering \(K\) with \(a_n\) intervals of length \(3^{-n}\). For the converse, take a strictly positive right Perron eigenvector \(r\) of \(T\); assign each edge from state \(i\) to \(j\) transition probability \(r_j/(\lambda r_i)\). Because distinct outgoing edges carry distinct ternary digits, each level-\(n\) cylinder then receives probability \(r_j/(\lambda^nr_A)\le C\lambda^{-n}\). Every interval of length at most \(3^{-n}\) meets a bounded number of level-\(n\) ternary cylinders, so the associated measure obeys the Frostman bound \(\mu(I)\ll |I|^{\log_3\lambda}\). The mass distribution principle proves the matching lower Hausdorff bound. The same cylinder counts and measure yield both box dimensions for \(K\). Removing or adding the countable endpoint exceptions preserves the claimed essential-boundary Hausdorff dimension.

## Verification

Run the accompanying Python 3 standard-library program `verify_boundary.py`. It computes the carry transitions directly from the digit set, independently constructs the six-state reverse subset automaton, checks all rows of \(T\), tests that every transient state reaches both absorbing classes, independently enumerates all prefix words through length seven, and verifies the exact recurrence by matrix multiplication through length 110. It reports `TERNARY_BOUNDARY_CERTIFICATE_OK` if all assertions pass. The infinite generating-function identity, Perron-root computation, and Frostman argument are established algebraically in the proof; finite tests are supporting checks rather than substitutes.

## Relationship to prior work

Zhou's November 5, 2026 manuscript establishes measurable scaling convergence and a carry-synchronization criterion, and explicitly exhibits the digit set \(\{0,1,5\}\) in Section 6.1; it does not state this boundary-dimension theorem or the six-state ambiguity-prefix generating function. Tangjai (2020), on the *same* digit set, establishes Pell/Pell-Lucas laws for numbers of maximal consecutive represented-number blocks over specified finite integer ranges (Theorems 3.13 and 3.15). Those laws are a substantial related antecedent, not an independent novelty claim here: they concern finite integer blocks rather than the essential boundary of the measurable scaling limit, and do not themselves supply the required two-sided cylinder and fractal dimension argument. Abram and Lagarias supply the general symbolic path-set entropy framework; the special boundary automaton and spectral invariant here are not computed there.

## Limitations

No independent mathematical validation has been performed. The theorem is restricted to the indicated digit set; the topological boundary of an arbitrary measurable representative is not intrinsic, hence the essential boundary is used. The specific Pell growth constant was already present in Tangjai's block-count work, so the distinct contribution is the exact ambiguity-prefix law and its verified geometric interpretation. Equivalence to an unindexed boundary theorem cannot be categorically excluded. The proof does not determine the exact Hausdorff measure of the boundary or generalize its dimension to all nonstandard digit systems.

## References

1. Nian Hong Zhou, *Periodic counting, carry synchronization, and primes in nonstandard numeration systems*, arXiv:2611.07446v1 (public November 5, 2026), Theorems 1.3 and 1.5 and Section 6.1. https://arxiv.org/html/2611.07446v1
2. Wipawee Tangjai, *A Non-standard Ternary Representation of Integers*, Thai Journal of Mathematics, special issue (2020), 269–283, Theorems 3.13 and 3.15. https://thaijmath.com/index.php/thaijmath/article/download/970/976/1000
3. William Abram and Jeffrey C. Lagarias, *Path sets in one-sided symbolic dynamics*, Advances in Applied Mathematics 56 (2014), 109–134, arXiv:1207.5004, Theorem 1.13. https://arxiv.org/html/1207.5004v5
