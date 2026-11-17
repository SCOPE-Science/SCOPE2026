# A quartic oscillation entropy for majority dynamics on alternatingly whiskered cycles

## Finding

For every integer \(m\ge 2\), start with a labelled cycle \(C_{2m}\) and attach one distinct pendant leaf to every even-indexed cycle vertex. Call the resulting \(3m\)-vertex graph \(G_m\). Consider simultaneous binary open-neighbor majority with retention of the old bit in a tie. Let \(E_m\) count labelled fixed configurations, \(P_m\) count labelled configurations returning after two synchronous updates, and \(N_m\) count distinct primitive period-two temporal orbits (time phases identified, but vertex labels, global complementation and graph symmetries not identified).

The fixed-state population remains *exactly* that of the undecorated cycle:
\[
E_m=L_{2m}+2\cos(2\pi m/3),
\]
where \(L_0=2\), \(L_1=1\), and \(L_{r+2}=L_{r+1}+L_r\). By contrast, the complete two-step-return population is given by the exact recurrence \(P_m=\operatorname{tr}(B^m)\), where an explicit \(16\times16\) integer transfer matrix \(B=DU\) is defined in the proof and has characteristic polynomial
\[
\chi_B(z)=z^6(z-1)(z^2+1)(z^3+2z^2+4z+1)
(z^4-5z^3+4z^2-z-1).
\]
For all \(m\ge2\), the exact number of primitive two-cycle orbits is
\[
\boxed{N_m=\frac{P_m-E_m}{2}}.
\]
In particular, the quartic's unique dominant root \(\lambda=4.09798902562757\ldots\) gives
\[
P_m=\lambda^m+O(4^m),\qquad
N_m\sim\tfrac12\lambda^m,\qquad
\frac{P_m}{2^{3m}}\sim(\lambda/8)^m.
\]
The half-whiskered graph therefore has a genuinely intermediate recurrence entropy: a bare cycle has only \(E_m\asymp\varphi^{2m}\) initially periodic configurations up to a bounded correction, whereas the fully whiskered even cycle has \(E_m^2\asymp\varphi^{4m}\), with \(\varphi=(1+\sqrt5)/2\), and \(\varphi^2<\lambda<\varphi^4\). The stated comparison for the bare ring uses its known fixed states plus at most one primitive two-cycle. Every trajectory on \(G_m\) eventually has period one or two, so these formulas enumerate all recurrent orbits, though not their attraction basins.

## Assumptions and scope

Cycle vertices are labelled \(0,1,\ldots,2m-1\), with indices modulo \(2m\); leaf \(i^*\) is attached only to each even vertex \(i\). Every vertex updates in parallel, taking the strict majority of its neighbors, and retaining its own current bit exactly in the case of a tie. Thus an even cycle vertex has three neighbor votes, an odd cycle vertex has two neighbor votes plus tie retention, and a leaf copies its parent one step later. There are no self-loops, biases, weights, randomness, or asynchronous updates. Define \(F\) as the global update of all \(3m\) bits. The precise meaning of \(P_m\) is \(\#\{x:F^2(x)=x\}\), **not** the number of initial states eventually reaching a two-cycle. The lower bound \(m\ge2\) excludes the non-simple two-vertex cycle.

## Proof

**1. Only one- and two-periodic recurrent dynamics.** Write \(s_i(t)\in\{-1,1\}\). Form the symmetric matrix \(W\) whose off-diagonal entries are graph adjacency indicators, and whose only nonzero diagonal entries are \(W_{ii}=1\) for the degree-two (odd-index) cycle vertices. The specified majority with inertial ties is then the exact sign update
\[
s_i(t+1)=\operatorname{sgn}\Bigl(\sum_jW_{ij}s_j(t)\Bigr).
\]
Every local field is a nonzero *odd* integer: the external degree is one or three, or the degree is two with one diagonal input. Put \(\Phi_t=\sum_{ij}W_{ij}s_i(t+1)s_j(t)\). Symmetry implies
\[
\Phi_t-\Phi_{t-1}=\sum_i\bigl(s_i(t+1)-s_i(t-1)\bigr)\sum_jW_{ij}s_j(t)\ge0.
\]
Each nonzero summand is strictly positive, because the successor bit has the field's sign. Since \(\Phi_t\) is an integer bounded on a finite state space, it eventually stops increasing, at which point all bits satisfy \(s_i(t+1)=s_i(t-1)\). Hence eventual periods are one or two. This also supplies a self-contained version of the classical symmetric-threshold argument.

**2. Fixed-state count.** At a fixed state every leaf equals its parent. An even-indexed cycle vertex therefore retains its bit exactly when one of its two cycle neighbors has that bit. An odd-indexed vertex, with its two cycle neighbors and tie-retention, obeys precisely the same condition. Consequently the core cycle word has no isolated singleton runs. Let \(R\) be the \(4\times4\) zero-one transfer on adjacent-bit states \((p,q)\in\{0,1\}^2\): the transition \((p,q)\to(q,r)\) is permitted if and only if \(q=p\) or \(q=r\). Its characteristic polynomial is
\[
\det(zI-R)=(z^2-z-1)(z^2-z+1).
\]
Thus \(E_m=\operatorname{tr}(R^{2m})=L_{2m}+2\cos(2\pi m/3)\). The cyclic transfer trace counts labelled positions without dividing by rotations.

**3. A complete two-time-layer encoding.** For a configuration returning after two steps, write \(a_i\) and \(b_i\) for its cycle bits at times zero and one. Its leaf at time zero must be \(b_i\) for each even \(i\), since leaves copy parents and the state returns at time two. At an even cycle vertex, the two local return conditions become
\[
b_i\in\{a_{i-1},a_{i+1}\},\qquad
a_i\in\{b_{i-1},b_{i+1}\}.
\]
At an odd cycle vertex, the two return conditions instead read
\[
b_i=\operatorname{Maj}(a_{i-1},a_i,a_{i+1}),\quad
a_i=\operatorname{Maj}(b_{i-1},b_i,b_{i+1}),
\]
where \(\operatorname{Maj}\) is the binary median of three input bits. The difference between the even and odd conditions is crucial: replacing the undecorated condition by a neighbor-agreement condition would incorrectly yield the fully whiskered count.

These conditions are both necessary and sufficient. In particular, choosing an admissible pair of core words \((a,b)\) determines each initial leaf bit uniquely as \(b_i\); the next leaf bits are \(a_i\); and all core and leaf coordinates then return after the second update. There is no multiplicity or unaccounted initial leaf choice.

**4. Explicit transfer matrices.** Encode a two-time symbol by \(\sigma=(a,b)\in\{0,1\}^2\), and index the sixteen ordered symbol pairs \((p,q)\). For symbols \(p=(p_a,p_b)\), \(q=(q_a,q_b)\), and \(r=(r_a,r_b)\), define \(D_{(p,q),(q',r)}=0\) unless \(q'=q\); otherwise set
\[
D_{(p,q),(q,r)}=\mathbf1\{(q_b=p_a\ \text{or}\ q_b=r_a)
\ \text{and}\ (q_a=p_b\ \text{or}\ q_a=r_b)\}.
\]
Define the undecorated transfer at the same index by
\[
U_{(p,q),(q,r)}=
\mathbf1\{q_b=\operatorname{Maj}(p_a,q_a,r_a)
\ \text{and}\ q_a=\operatorname{Maj}(p_b,q_b,r_b)\}.
\]
Both are zero-one matrices with fully specified indices. In a closed transfer walk over the labelled \(2m\) sites, the center index alternates between even (matrix \(D\)) and odd (matrix \(U\)). Each admissible labelled two-time word generates precisely one closed walk. Therefore
\[
P_m=\operatorname{tr}((DU)^m),\qquad m\ge2.
\]
This is a finite, size-independent, constructive formula: the matrices' entries can be regenerated directly from the displayed Boolean conditions without hidden numerical data.

**5. Exact spectral law.** Direct symbolic expansion of the determinant of \(zI-DU\), which can be replayed with the bundled `transfer_check.py`, gives the factored characteristic polynomial displayed in the Finding. Thus the trace of its powers equals the sum of the eigenvalues' \(m\)-th powers with algebraic multiplicity, including if matrices are not diagonalizable. Let \(q(z)=z^4-5z^3+4z^2-z-1\). Its unique real root in \((4,4.2)\) is \(\lambda\); the other three roots have modulus less than one, as can be checked by factoring the polynomial numerically with certified algebraic isolation, or by the elementary argument below. In fact, dividing by \(z-\lambda\) gives
\[
q(z)/(z-\lambda)=z^3+(\lambda-5)z^2+(\lambda-1)(\lambda-4)z+1/\lambda.
\]
Since \(4<\lambda<4.2\), the last three coefficients have absolute values less than \(1,1,1\), respectively. For any \(|z|\ge2\), the leading cubic term has modulus at least \(8\), while the remaining three terms have sum of moduli strictly below \(4+2+1=7\). Hence the other quartic roots have modulus less than two. The roots of \(z^3+2z^2+4z+1\) all have modulus less than four, because at \(|z|\ge4\) its cubic term exceeds the sum of the moduli of the lower terms: \(64>32+16+1\). The factors \(z-1\), \(z^2+1\) and \(z^6\) have root moduli at most one. Therefore \(\lambda\) is the unique dominant eigenvalue, with multiplicity one, and \(P_m=\lambda^m+O(4^m)\). The fixed count is \(O(\varphi^{2m})\), with \(\varphi^2<4<\lambda\). Removing fixed configurations and dividing by two proves the orbit asymptotic.

## Verification

The bundled `transfer_check.py` constructs \(D,U,R\) directly from Boolean predicates, checks both characteristic polynomials exactly using SymPy, and prints \(E_m,P_m,N_m\) through \(m=12\). A separate `microscopic_check.cpp` implements the graph's original synchronous majority update at individual vertices and compares actual \(F(x)=x\) and \(F^2(x)=x\) for every initial bit assignment for each \(2\le m\le8\), without using the transfer matrices. It exhausts exactly \(19,173,952\) labelled graph-state pairs. Both reproduced outputs are included. Example populations for \(m=2,3,4,5,6,7,8\) are \((E_m,P_m,N_m)=(6,12,3),(20,82,31),(46,276,115),(122,1124,501),(324,4818,2247),(842,19380,9269),(2206,79300,38547)\). Finite experiments corroborate but do not substitute for the determinant identity and combinatorial proof for arbitrary \(m\).

## Relationship to prior work

The symmetric finite-threshold period-two theorem of Goles and Olivos proves eventual period at most two, not this half-decorated graph's exact periodic populations. Benjamini et al. (2014, arXiv:1405.2486v1) examine convergence, unanimity and disagreement, rather than this recurrence census. Kaaser, Mallmann-Trenn and Natale (2015, arXiv:1508.03519v1) prove general voting-time bounds and hardness; their introduction, theorems and appendices contain no corresponding mixed-decoration spectral formula.

Previously reported results for (i) a cycle with *one* private leaf, and (ii) a cycle with a leaf at *every* site, give a Fibonacci correction and a parity-factorized full-sunlet census respectively. Their proofs use different constraints: in (i) there is only one exceptional degree-three site; in (ii) every site has a pendant memory vertex. Neither implies the alternating half-leaf matrix \(DU\) or its quartic spectral law. The result for all fully whiskered degree-two base graphs provides a two-step entry bound, not an enumeration for partial whiskering. For example, at \(m=4\) the half-decorated graph has exactly \(276\) two-step states, whereas the fully whiskered eight-cycle has \(46^2=2116\), so substituting the known complete-corona formula is mathematically invalid. A generic bounded-width transfer method makes counting in principle possible, but is not itself an explicit matrix spectrum or a formula for the natural intermediate entropy. The comparison is based on statements and assumptions, not an assertion of global historical uniqueness.

## Limitations

These formulas concern *immediately* returning configurations and their primitive temporal cycles, not their attraction basins, transient-depth distributions, or probability of eventual oscillation from a random initial condition. The growth rate comparison is between three distinct graph families, not a monotonicity theorem for every possible attachment pattern. Historical priority remains qualified: an unindexed older calculation or alternative Boolean-network encoding could contain an equivalent formula. No independent external mathematical audit has been performed. The 2014 arXiv article was available at the bibliographic/abstract level rather than as a full text during the source comparison; the 2015 primary preprint was read in accessible HTML including its main theorems and supporting sections.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI: 10.1016/0012-365X(80)90121-1 (general background; exact first public day not asserted).
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11; https://arxiv.org/abs/1405.2486.
3. D. Kaaser, F. Mallmann-Trenn, and E. Natale, *On the Voting Time of the Deterministic Majority Process*, arXiv:1508.03519v1, first posted 2015-08-14; https://arxiv.org/html/1508.03519v1.
4. *One pendant edge preserves majority equilibria but creates Fibonacci-many oscillations*, publicly accessible record https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-one-pendant-edge-preserves-majority-equilibria-but-creates-fibon--404ec1da0b60.
5. *A parity-factorized periodic-orbit census for majority dynamics on sunlet graphs*, publicly accessible record https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-parity-factorized-periodic-orbit-census-for-majority-dynamics--8a5efe3ce640.
6. *Uniform two-step periodicity for majority dynamics on degree-two leaf coronas*, publicly accessible record https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-uniform-two-step-periodicity-for-majority-dynamics-on-degree-two--830f30f39271.
