# Exact three-cycle zeta and a persistent-clock contrast on two-row Moore tori

## Finding
For every integer \(n\ge3\), let \(F_n\) be synchronous three-state Greenberg–Hastings (threshold-one) dynamics on the labelled periodic Moore grid \(\mathbb Z_2\times\mathbb Z_n\). Its eight Moore offsets are counted with their lattice multiplicities, though the threshold-one predicate only depends on the existence of a neighbor. Write \(S_n\) for the number of configurations with **least temporal period three**, distinguished by labelled vertex and temporal phase. Let
\[
a_0=3,\quad a_1=6,\quad a_2=54,\qquad a_n=6a_{n-1}+9a_{n-2}+18a_{n-3}\quad(n\ge3).
\]
Then, for every \(n\ge3\),
\[
\boxed{S_n=a_n+4\cdot3^n\cos(2\pi n/3),\qquad\#\{\text{primitive temporal three-orbits}\}=S_n/3.}
\]
Equivalently, with \(D(z)=(1-6z-9z^2-18z^3)(1+3z+9z^2)^2\),
\[
\sum_{n\ge1}S_nz^n=-z\,\frac{D'(z)}{D(z)},
\]
where the coefficients at \(n=1,2\) are formal transfer traces and not asserted as physical two-row tori. The dominant exponential rate is \(\lambda=7.51606789856803\ldots\), the unique positive root of \(\lambda^3-6\lambda^2-9\lambda-18=0\); in particular \(S_n=\lambda^n+O(3^n)\), with spatial entropy per physical cell \((\log\lambda)/2\).

Despite \(S_n/9^n\to0\), for a uniformly random initial state the probability of a *permanently active three-vertex clock* is at least \(1-(7/9)^{\lfloor n/2\rfloor}\to1\). This latter assertion is not an eventual-period-three census of the entire lattice.

## Assumptions and scope
The sites are pairs \((r,i)\) with \(r\in\{0,1\}\), \(i\in\mathbb Z_n\). Neighbor offsets are \((\delta r,\delta i)\in\{-1,0,1\}^2\setminus\{(0,0)\}\), evaluated modulo the respective periods. For height two, the two vertical offsets reach the same opposite-row site. The unique-neighbor graph is the simple five-regular graph consisting of a rung edge at each column and all four edges between successive columns; it is the strong product \(K_2\boxtimes C_n\). States belong to \(\{0,1,2\}\): \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) exactly when some (possibly multiply incident) neighbor is in state \(1\); otherwise \(0\mapsto0\). All updates are simultaneous. Configurations, not translation classes, are counted.

## Proof
**Reduction to three-phase clocks.** A configuration returning after three updates either is identically zero or all sites increment globally by one modulo three at each update. To prove this, for any vertex the forced transitions from state one and state two imply that its three-step orbit either stays at zero at every step or visits each color cyclically. A vertex permanently zero cannot touch a cyclic vertex: its neighbor is excited during one of the three steps, so it would update. Connectivity forces the zero/cyclic choice to be global. The nonzero configurations returning after three steps thus have least period exactly three and are precisely the colorings \(x\) such that *each vertex has a neighbor colored \(x(v)+1\) modulo three*. For sufficiency this successor-neighbor condition is invariant under global color increment, and each vertex at rest is forced to advance.

**Column transfer.** Let \(\mathcal A=\{0,1,2\}^2\) be the nine ordered column colors. For \(A,B,C\in\mathcal A\), let \(q(A,B,C)=1\) if, for each row \(r\in\{0,1\}\), the successor color \(B_r+1\pmod3\) appears in \(\{B_{1-r},A_0,A_1,C_0,C_1\}\), otherwise zero. Define the explicit \(81\times81\) matrix indexed by ordered column pairs,
\[
T_{(A,B),(B',C)}=\mathbf1\{B=B'\}\,q(A,B,C).
\]
A closed spatial walk of length \(n\ge3\) in this graph corresponds bijectively to a valid labelled period-three coloring; consequently \(S_n=\operatorname{tr}(T^n)\). This is a constructive all-length equality, not an extrapolation from small rings.

**Exact finite determinant identity.** Multiplying the explicit integer matrix and using exact characteristic-polynomial arithmetic yields
\[
\boxed{\chi_T(X)=X^{74}(X^2+3X+9)^2(X^3-6X^2-9X-18).}
\]
The standalone script `verification/transfer.py` constructs the defining entries and computes the characteristic polynomial exactly with symbolic integer arithmetic; the structurally independent `verification/independent_certificate.py` constructs the graph with different loops, computes the traces of all first 81 matrix powers using integer arrays, and reconstructs *every* characteristic-polynomial coefficient by Newton identities. Its detailed coefficient list independently establishes the claimed polynomial. These finite integer identities are complete, checkable certificates of the 81-dimensional determinant identity, and suffice for all circumferences once the column-transfer bijection is proved.

Let \(a_n\) be the sum of the \(n\)-th powers of the three roots of \(X^3-6X^2-9X-18\), including multiplicity. Newton identities yield the initial values \(3,6,54\), and Cayley–Hamilton yields the displayed recurrence. The two roots of \(X^2+3X+9\) are \(3\exp(\pm2\pi i/3)\), each with multiplicity two, giving their aggregate \(4\cdot3^n\cos(2\pi n/3)\). Nilpotent eigenvalues contribute zero to every positive power trace. This proves the formula and its logarithmic generating function.

The cubic is strictly increasing on \([0,\infty)\) after its unique positive zero, and has one positive root \(\lambda\in(7.51606,7.51608)\); its other two roots are a conjugate pair of modulus \(\sqrt{18/\lambda}<2\), so the unique dominant spectral term is \(\lambda^n\), the quadratic factor's roots having modulus three. In particular \(S_n/9^n\to0\).

**A distinct high-probability persistent-clock event.** For every disjoint consecutive column pair \((2j,2j+1)\), use the triangle with vertices \((0,2j),(1,2j),(0,2j+1)\). These triangles are vertex-disjoint for \(0\le j<\lfloor n/2\rfloor\). Under independent uniform initial colors, each triangle is rainbow (all three colors once) with probability \(3!/3^3=2/9\), independently. A rainbow triangle remains a globally phase-incrementing three-cycle on its own three vertices forever, even if external neighbors evolve arbitrarily, because each site always has its successor-colored neighbor within the triangle. Thus the probability of at least one persistent triangle is at least \(1-(7/9)^{\lfloor n/2\rfloor}\). This illustrates the statistical distinction between immediate global periodicity and nonextinction, without identifying the full-system eventual period.

## Verification
The exact symbolic transfer checker and an independent dependency-free integer Newton-identity checker both produce the same characteristic polynomial, with 81 matrix states and 585 directed edges. The independent direct C++17 checker implements the local synchronous rule at the site level and enumerates all \(3^{2n}\) configurations for each \(n=3,4,5,6\), finding exactly one fixed configuration and respectively \(541,3025,23491,183223\) third-iterate fixed configurations. The resulting primitive period-three populations are \(540,3024,23490,183222\), agreeing with the transfer formula. The transfer also computes the counts \(1350594\), \(10171008\), \(76623732\), and \(575198496\) for \(n=7,8,9,10\), respectively. Actual scripts and their outputs are supplied. Small-size tests are supplementary; the all-length proof rests on the exact determinant identity and transfer bijection.

## Relationship to prior work
The 1991 Durrett–Steif paper treats nearest-neighbor Greenberg–Hastings dynamics in one dimension and finite boxes, not this two-row fully periodic Moore-contact graph or its temporal orbit counts. Durrett–Griffeath's preprint (first posted 1993-03-22) examines phase transitions and spiral-core stability in excitable cellular automata; its abstract, but not complete full text, was accessible in this inspection. Gravner–Lyu–Sivakoff's full-text study of arbitrary-graph three-color excitation establishes general activity and comparison methods but not the displayed exact Moore-strip transfer characteristic polynomial. The independently published open-ladder three-clock census concerns the *rail-and-rung* graph \(P_n\square K_2\), with free ends. The separately published circular/Möbius ladder seam comparison concerns *cubic* graphs \(C_n\square K_2\) without diagonal contact; their dominant growth base \((3+\sqrt{17})/2\) is not \(\lambda\). Neither statement implies the present eight-offset torus census. The general successor-neighbor reduction is standard and is not claimed as new. The contribution is the exact natural Moore-torus census and its accompanying transient-versus-persistent probability contrast.

## Limitations
The period-three enumeration counts configurations already periodic at time zero, not arbitrary attraction basins or other eventual periods. The two-row quotient has duplicate neighbor incidences and the threshold-one update makes multiplicity immaterial; alternative contact thresholds require different treatment. The characteristic-polynomial certificate is exact computer-assisted finite algebra; the full matrix is reproducibly defined by an explicit local predicate, not printed as 6561 numerals. The 1980 Greenberg–Greene–Hastings combinatorial paper was not accessible in full text and might contain alternate formulations; historical priority is not independently certified. No external independent audit is asserted.

## References
1. R. Durrett and J. E. Steif, *Some Rigorous Results for the Greenberg–Hastings Model*, Journal of Theoretical Probability 4 (1991), 669–690. https://sites.math.duke.edu/~rtd/reprints/paper66.pdf.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, arXiv:patt-sol/9303002, submitted 1993-03-22. https://arxiv.org/abs/patt-sol/9303002.
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, arXiv:1610.07320, submitted 2016-10-24. https://arxiv.org/abs/1610.07320.
4. J. M. Greenberg, C. Greene, and S. P. Hastings, *A combinatorial problem arising in the study of reaction-diffusion equations*, SIAM Journal on Algebraic and Discrete Methods 1 (1980), 34–42, DOI:10.1137/0601006.
5. *Exact primitive-three wave census on open ladders*, publicly available mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-primitive-three-wave-census-on-open-ladders--c343292238f3.
6. *Exponential seam screening for three-color excitable waves on cubic ladders*, publicly available mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exponential-seam-screening-for-three-color-excitable-waves-on-cu--b0ea4c831bc4.
