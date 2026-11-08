# A single missing rung amplifies minority fixed states on cyclic ladders by \(3/\sqrt5\)

## Finding

Removing one rung edge from a cubic circular or Möbius ladder changes the number of synchronous binary minority fixed points by a common, nontrivial asymptotic factor, while preserving Fibonacci growth and leaving an explicit periodic topology correction.

Let \(n\ge3\), and let \(H_{n,0}\) be the prism \(C_n\square K_2\) with the rung between its two vertices in column zero removed. Let \(H_{n,1}\) have the same missing rung but a crossed (Möbius) pair of horizontal seam edges. Both have \(2n\) labelled vertices, two of degree two and all others of degree three. Under synchronous binary minority update, each vertex chooses the less frequent bit among its neighbors, **retaining its current bit in a tie**. Let \(V_{n,\delta}\) count labelled fixed configurations of this update, with \(\delta=0\) for the circular case and \(\delta=1\) for the Möbius case.

Write \(F_0=0\), \(F_1=1\), \(F_{n+2}=F_{n+1}+F_n\) for Fibonacci numbers. Then for every \(n\ge3\),
\[
V_{n,0}=3F_n+a_{n\bmod6},\qquad
V_{n,1}=3F_n+b_{n\bmod6},
\]
where the periodic coefficients, indexed by residues \(0,1,2,3,4,5\), are
\[
(a_0,a_1,a_2,a_3,a_4,a_5)=(6,-3,1,4,-1,-1),
\qquad
(b_0,b_1,b_2,b_3,b_4,b_5)=(-2,3,3,-4,5,1).
\]
In particular,
\[
V_{n,0}-V_{n,1}=
\begin{cases}
8,&n\equiv0\pmod3,\\
-6,&n\equiv1\pmod3,\\
-2,&n\equiv2\pmod3.
\end{cases}
\]
Let \(U_{n,\delta}\) be the corresponding minority fixed-point count *before* deleting the rung. Then the previously known circular-ladder majority full-flip census, together with the elementary complement relation on cubic graphs, gives \(U_{n,\delta}=\varphi^n+O(1)\), where \(\varphi=(1+\sqrt5)/2\). Therefore the exact common one-defect susceptibility is
\[
\boxed{\lim_{n\to\infty}\frac{V_{n,\delta}}{U_{n,\delta}}=\frac3{\sqrt5}},
\qquad \delta\in\{0,1\}.
\]
Thus a single local bond deletion causes approximately a \(34.16\%\) increase in the number of fixed states for arbitrarily long rings. The graph's topology changes only the bounded periodic correction, not this leading amplification.

## Assumptions and scope

The vertices are \((i,s)\), for \(0\le i<n\) and \(s\in\{0,1\}\). For each \(1\le i<n\), a vertical rung edge joins \((i,0)\) to \((i,1)\); the vertical edge in column zero is absent. Along both rows, edges join consecutive columns. The two horizontal seam edges join \((n-1,s)\) to \((0,s)\) for \(\delta=0\) and to \((0,1-s)\) for \(\delta=1\). All graphs are simple for \(n\ge3\), including the smallest cases. The minority opinion is the bit held by fewer neighbors; if a degree-two vertex observes one neighbor of each bit, it retains its old opinion. Counts are exact labelled fixed configurations, not orbit classes or transient basins.

## Proof

**Local transfer representation.** Encode each column's two bits by \(a\in\{0,1,2,3\}\), where bit \(r\) of \(a\) is the opinion of row \(r\). For triple columns \((a,b,c)\), define
\[
q_r(a,b,c)=\mathbf1_{\{a_r\ne b_r\}}+\mathbf1_{\{c_r\ne b_r\}},\qquad r\in\{0,1\}.
\]
At a normal column, vertex \(r\) stays fixed exactly when
\[
q_r(a,b,c)+\mathbf1_{\{b_{1-r}\ne b_r\}}\ge2.
\]
At the defective column zero, where the rung is missing and the degree is two, the tie-retaining fixed-state condition is instead \(q_r(a,b,c)\ge1\). Both conditions must hold for both rows.

Index the sixteen ordered pairs of successive columns by \(i=4a+b\). Define integer \(16\times16\) matrices \(T\) and \(B\) by
\[
T_{4a+b,4b+c}=\mathbf1_{\{\text{both normal-column conditions hold}\}},\qquad
B_{4a+b,4b+c}=\mathbf1_{\{q_0(a,b,c)\ge1,\ q_1(a,b,c)\ge1\}},
\]
with all other entries zero. Define the involution \(\sigma\) on the four column states by swapping their two bits, and let \(D\) be the permutation matrix with \(D_{4a+b,4\sigma(a)+\sigma(b)}=1\). Every fixed spin assignment corresponds bijectively to a closed transfer path through \(n-1\) normal local tests and one defective-column test. A crossed seam closes the transfer path only after swapping both rows. Hence
\[
V_{n,0}=\operatorname{tr}(T^{n-1}B),\qquad
V_{n,1}=\operatorname{tr}(T^{n-1}BD).
\]
These identities include the small case \(n=3\), since every local triple corresponds to the three distinct columns, with the row permutation imposed precisely at the seam.

**Exact finite matrix identity.** Direct integer multiplication of the matrices defined above gives \(\sum_{ij}T_{ij}=20\), \(\sum_{ij}B_{ij}=36\), and
\[
\boxed{T^2(T^2-T-I)(T^6-I)=0.}
\]
The executable `checks/check_transfer.py` constructs those matrices from the displayed logical predicates and checks this equality **entry by entry using exact integers**. Thus each trace sequence satisfies, beginning at \(n=3\), the order-eight linear recurrence with characteristic annihilator \((z^2-z-1)(z^6-1)\). Every Fibonacci sequence and every sequence of period six satisfies this same recurrence.

It remains only to compare the eight successive initial values \(3\le n\le10\). The transfer traces give
\[
\begin{aligned}
(V_{3,0},\ldots,V_{10,0})&=(10,8,14,30,36,64,106,164),\\
(V_{3,1},\ldots,V_{10,1})&=(2,14,16,22,42,66,98,170).
\end{aligned}
\]
They agree term by term with the stated \(3F_n\)-plus-period-six expressions. The recurrence then proves both formulas for every \(n\ge3\), not merely for enumerated sizes.

**Asymptotic comparison.** The Fibonacci asymptotic \(F_n=\varphi^n/\sqrt5+O(\varphi^{-n})\) gives \(V_{n,\delta}=3\varphi^n/\sqrt5+O(1)\) for either seam. On intact cubic ladders, minority fixed states are exactly the configurations mapped to their bitwise complements by synchronous majority; the known full-flip counts are \(L_n\) plus a bounded residue correction and, for even \(n\), a two-state correction. Consequently \(U_{n,\delta}=\varphi^n+O(1)\). Dividing proves the common factor \(3/\sqrt5\). Subtracting the two explicit six-periodic corrections gives the stated three-periodic topology difference.

## Verification

The certificate `checks/check_transfer.py` uses only standard Python and exact integer arithmetic. It constructs the complete two distinct transfer matrices, checks the annihilating matrix identity, verifies the eight required initial values, and tests the closed forms through \(n=30\). The independent `checks/check_direct.py` builds every labelled graph and checks the degree-sensitive minority fixed-state criterion on every binary spin assignment for \(3\le n\le9\), testing 699008 configurations across the two seam types. Captured results are in the correspondingly named `.out` files. Direct simulations corroborate the proof, but are not substituted for the exact algebraic identity and the recurrence argument.

## Relationship to prior work

Ising-machine experiments on Möbius ladders and subsequent benchmarking on both circular and Möbius ladders motivate the search for local metastability counts; these studies primarily analyze ground-state optimization rather than exact all-size defective-graph fixed-state populations. Exact majority full-flip counts on *intact* cubic ladders are known, and are used solely as the comparison baseline, not claimed as a new discovery. The present object differs by a deleted edge and by tie-retaining degree-two boundary dynamics. Its defective local transition \(B\), exact Fibonacci amplification \(3/\sqrt5\), and explicit seam corrections do not follow from the intact-cubic count formulas alone. General metastability studies with random or weighted bonds concern different distributions or graph models, not this single-edge deletion and its two seam conditions.

## Limitations

Only fixed states after one synchronous update are classified. There is no assertion about temporal two-cycles, attraction basins, physical solver sampling or ground-state multiplicities. The matrix identity is a finite exact computation, transparently specified and accompanied by reproducible code; its verification does not require trusting an experimental sample. Historical priority is qualified because an obscure earlier defective-ladder Ising calculation might be equivalent. Independent audit has not been performed.

## References

1. K. Takata et al., *A 16-bit Coherent Ising Machine for One-Dimensional Ring and Cubic Graph Problems*, arXiv:1605.03847 (first submitted 2016-05-12), https://arxiv.org/abs/1605.03847.
2. Y. Cen, D. Das and X. Fong, *A tree search algorithm towards solving Ising formulated combinatorial optimization problems*, *Scientific Reports* **12** (2022), 14755, https://doi.org/10.1038/s41598-022-19102-x.
3. A. E. Jacobs and C. M. Coram, *Ferromagnetic random-bond Ising model: Metastable states and complexity of the energy surface*, *Physical Review B* **36** (1987), 3844, https://doi.org/10.1103/PhysRevB.36.3844.
4. A. Stroev et al., *Computational complexity continuum within Ising formulation of NP problems*, *Communications Physics* (2021), https://doi.org/10.1038/s42005-021-00792-0.
