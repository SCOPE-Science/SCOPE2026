# A twelve-step characteristic-three wave resonance on Boolean hypercubes

## Finding
Let \(d\ge0\), \(q=3^f\) for an integer \(f\ge1\), and let \(Q_d\) be the simple Boolean \(d\)-cube, with the convention that \(Q_0\) has one isolated vertex. Write \(A_d\) for its adjacency matrix over \(\mathbb F_q\), and evolve arbitrary pairs of configurations by the reversible wave rule
\[
T_d(u,v)=(A_du-v,u),\qquad (u,v)\in\mathbb F_q^{2^d}\times\mathbb F_q^{2^d}.
\]
Define the nonnegative integers
\[
a_d=\frac{2^d-(-1)^d}{3},\qquad b_d=\frac{2^d+2(-1)^d}{3}.
\]
For \(t\in\{1,2,3,4,6,12\}\), the exact numbers of labelled two-time-level states fixed by \(t\) updates are
\[
\begin{array}{c|rrrrrr}
t&1&2&3&4&6&12\\\hline
\#\operatorname{Fix}(T_d^t)&q^{a_d}&q^{2a_d}&q^{2a_d}&q^{2a_d+2b_d}&q^{4a_d}&q^{4a_d+2b_d}.
\end{array}
\]
Every state is periodic from time zero. The sharp order of the entire permutation is \(4\) when \(d=0\), \(6\) when \(d=1\), and **\(12\) for every \(d\ge2\)**. In particular, the exact number of configurations of primitive period twelve is
\[
\boxed{P_{12}=q^{2a_d}(q^{2a_d}-1)(q^{2b_d}-1).}
\]
For \(d\ge2\), all six primitive periods \(1,2,3,4,6,12\) occur, with populations
\[
\begin{aligned}
P_1&=q^{a_d},&P_2&=q^{2a_d}-q^{a_d},&P_3&=q^{2a_d}-q^{a_d},\\
P_4&=q^{2a_d+2b_d}-q^{2a_d},&
P_6&=q^{4a_d}-2q^{2a_d}+q^{a_d},&
P_{12}&=q^{4a_d+2b_d}-q^{4a_d}-q^{2a_d+2b_d}+q^{2a_d}.
\end{aligned}
\]
The count of temporal orbits of least period \(j\) is exactly \(P_j/j\). For uniformly random initial states on \(Q_d\) with \(d\ge2\),
\[
\boxed{\Pr(\text{primitive period }12)=(1-q^{-2a_d})(1-q^{-2b_d}).}
\]
Hence for fixed \(q\), the failure probability tends to zero doubly exponentially in \(d\). For arbitrary positive \(t\), the fixed-state count equals that at \(\gcd(t,12)\).

## Assumptions and scope
The graph is the *simple* Boolean hypercube \(Q_d\): its vertices are binary strings of length \(d\), with an edge for each single-coordinate flip. The zero-dimensional convention is stated explicitly to cover the two exceptional orders. Each vertex carries an arbitrary element of the finite field \(\mathbb F_{3^f}\); this is not a Boolean voting or nonlinear excitation rule. Both initial time levels are independent. The minus sign in \(A_du-v\) is essential. All counts are for individually labelled spatial vertices and complete ordered pairs of consecutive configurations; no quotient by spatial automorphisms or exchange of time levels is imposed.

## Proof
**1. Diagonalization in odd characteristic.** For a subset \(S\subseteq\{1,\ldots,d\}\), the Walsh character of a vertex \(x\in\{0,1\}^d\) is
\[\chi_S(x)=(-1)^{\sum_{i\in S}x_i}.\]
Since the field has characteristic three, the \(2^d\) Walsh characters form an invertible Fourier basis: the Walsh matrix multiplied by its transpose equals \(2^dI\), an invertible scalar matrix. Directly summing over the neighbors gives
\[A_d\chi_S=(d-2|S|)\chi_S.\]
Modulo three these eigenvalues are \(0\), \(+1\), and \(-1\), with multiplicities \(b_d,a_d,a_d\), respectively. To verify the multiplicities without division by binomial polynomials, let \(a_d\) be the count for either nonzero eigenvalue and \(b_d\) the zero-eigenvalue count. At dimension zero the counts are \((a_0,b_0)=(0,1)\). Adding a binary coordinate changes each old eigenvalue by \(+1\) and \(-1\), hence
\[a_{d+1}=a_d+b_d,\qquad b_{d+1}=2a_d.\]
The invariant \(2a_d+b_d=2^d\) and this recurrence give
\[a_d=(2^d-(-1)^d)/3,\quad b_d=(2^d+2(-1)^d)/3.\]
For all \(d\ge2\), both multiplicities are strictly positive.

**2. Exact two-level Jordan blocks.** Every Walsh eigenspace supports the \(2\times2\) time-update matrix
\[M_c=\begin{pmatrix}c&-1\\1&0\end{pmatrix},\qquad c\in\{0,+1,-1\}.\]
When \(c=0\), \(M_0^2=-I\), so \(M_0\) has exact order four and no nonzero fixed vector except at times divisible by four. When \(c=+1\), the characteristic polynomial is \((X+1)^2\), and \(M_{+1}\ne-I\); hence there is one genuine size-two Jordan block at \(-1\). For positive \(t\), its fixed-space dimension is zero for odd \(t\), one for even \(t\) not divisible by three, and two for multiples of six. When \(c=-1\), similarly there is one size-two Jordan block at \(+1\), contributing fixed-space dimension one if \(3\nmid t\), and two if \(3\mid t\). The size-two Jordan powers are immediate from \((\pm I+N)^t=(\pm1)^t I+t(\pm1)^{t-1}N\) with \(N^2=0\) in characteristic three.

**3. Fixed populations and sharp temporal orders.** Summing the independent two-level fixed-space dimensions with multiplicities \(b_d,a_d,a_d\) gives
\[\dim\ker(T_d^t-I)=2b_d\mathbf{1}_{4\mid t}
+a_d\mathbf{1}_{2\mid t}(1+\mathbf{1}_{3\mid t})
+a_d(1+\mathbf{1}_{3\mid t}).\]
In a finite field, a linear subspace of dimension \(r\) has \(q^r\) points; substitution at \(t=1,2,3,4,6,12\) yields the six fixed populations. Each block has order dividing \(12\). If \(d=0\) only the zero-eigenvalue block occurs, giving sharp order four; if \(d=1\) only the two nonzero-eigenvalue blocks occur, giving sharp order six; for \(d\ge2\) all three occur, whose least common multiple is twelve. Invertibility holds explicitly:
\[T_d^{-1}(u,v)=(v,A_dv-u).\]
Thus no initial state has a nonperiodic transient.

**4. Primitive periods and asymptotics.** Because \(T_d^{12}=I\), a state of exact period \(j\) has \(j\mid12\). Fixed sets partition according to exact periods. Möbius inversion, or direct subtraction over the divisors of twelve, gives the six displayed \(P_j\). In particular,
\[P_{12}=\#\operatorname{Fix}(T_d^{12})-\#\operatorname{Fix}(T_d^6)-\#\operatorname{Fix}(T_d^4)+\#\operatorname{Fix}(T_d^2),\]
which factors as claimed. The primitive populations are positive for every listed period when \(a_d,b_d>0\); the exceptional dimensions follow from \(a_0=0\) and \(b_1=0\). Dividing \(P_{12}\) by the total \(q^{2^{d+1}}=q^{4a_d+2b_d}\) states gives the probability formula. Both \(a_d\) and \(b_d\) grow as \(2^d/3\), so the deficit decays as \(q^{-\Theta(2^d)}\). This completes the proof for every dimension and every allowed field size.

## Verification
Two standalone Python 3 programs with no nonstandard dependencies independently checked the theorem. Run `python3 proof/verify_matrix.py` and `python3 proof/verify_enumeration.py` from the package root. The first constructs full two-layer update matrices directly from the hypercube neighbors over \(\mathbb F_3\), computes exact modular ranks at all six divisors of twelve and verifies the sharp order for \(d=0,1,2,3,4,5\); its output is `proof/verify_matrix.out`. The second avoids matrix rank methods, directly simulates every one of the \(9\), \(81\), and \(6561\) two-layer configurations on \(Q_0,Q_1,Q_2\), and compares the complete primitive-period and fixed-point censuses; its output is `proof/verify_enumeration.out`. All checks passed on the embedded final scripts. The unlimited-dimensional and extension-field conclusions are proved algebraically, not inferred from finite testing.

For \(d=2\), \(q=3\), the population by primitive periods \(1,2,3,4,6,12\) is \((3,6,6,720,66,5760)\), totalling \(6561\) two-row states. For \(d=1\), only \(1,2,3,6\) occur, and for \(d=0\), only \(1,4\).

## Relationship to prior work
The reversible second-order construction is classical. Macfarlane (2004) analyzes linear reversible cellular automata mainly in one-dimensional binary settings, and Vlasov (2013) studies general reversible second-order local rules; neither inspected source derives the modular three-characteristic Boolean-hypercube orbit census. Brunnet and Chaté (2004) study nonlinear binary cellular automata on high-dimensional Boolean cubes, a different local state space and update mechanism. The standard hypercube adjacency spectrum is classical and is not asserted here as new; the new assertion is its exact characteristic-three two-level period census, the sharp \(4,6,12\) dimension transition, and the maximal-period concentration formula.

The closest separately published mathematical comparisons are *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs* (2026, full theorem and proof inspected) and *Twelve-step resonance and exact orbit census for mixed Hamming waves* (2026, full theorem and proof inspected). The former assumes that every coordinate clique size is divisible by three; this excludes the binary alphabet \(K_2\) at every coordinate and has square-zero modular clique adjacency, rather than the present Walsh diagonalization. The latter assumes characteristic two and includes both even- and odd-sized clique coordinates, which excludes the present homogeneous binary product over characteristic three. A previously published universal-hub Boolean-cube wave census (2026, full theorem and proof inspected) is likewise characteristic two and has a different graph and time map. None of these statements implies the explicit present primitive-period populations; similarity of a maximal period of twelve in some different regimes is not statement equivalence.

## Limitations
The theorem applies only to the exact reversible open-neighbor sum rule and fields of characteristic three on Boolean cubes. It does not claim the same census in other characteristics, for alphabet sizes other than two, or for nonlinear threshold automata. No mathematical priority guarantee is possible against unindexed antecedents or inaccessible full texts. Computation directly checks only fields of size three and dimensions at most five, but the proof covers all allowed cases. The period counts do not identify states up to cube automorphisms. The proof and programs have not undergone independent mathematical validation.

## References
1. L. G. Brunnet and H. Chaté, *Cellular automata on high-dimensional hypercubes*, Physical Review E **69** (2004), 057201, first public journal date 2004-05-18. DOI: `10.1103/PhysRevE.69.057201`.
2. A. J. Macfarlane, *Linear reversible second-order cellular automata and their first-order matrix equivalents*, Journal of Physics A **37** (2004), 10791–10814, first public journal date 2004-10-28. DOI: `10.1088/0305-4470/37/45/006`.
3. A. Yu. Vlasov, *On generalization of reversible second-order cellular automata*, arXiv:1311.4297, first posted 2013-11-18. https://arxiv.org/abs/1311.4297.
4. J. Florkowski, *Spectral Graph Theory of the Hypercube*, Naval Postgraduate School thesis (2008), specifically the hypercube adjacency eigenvalue table. https://hdl.handle.net/10945/3852.
5. *A three-class wave clock and exact orbit census for ternary-modular Hamming graphs* (2026), public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-class-wave-clock-and-exact-orbit-census-for-ternary-modu--13302e527b48.
6. *Twelve-step resonance and exact orbit census for mixed Hamming waves* (2026), public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-twelve-step-resonance-and-exact-orbit-census-for-mixed-hamming-w--ae5e876acfba.
7. *A hub-induced period-eight parity transition for reversible waves on Boolean cubes* (2026), public mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-hub-induced-period-eight-parity-transition-for-reversible-wave--f559fa00b785.
