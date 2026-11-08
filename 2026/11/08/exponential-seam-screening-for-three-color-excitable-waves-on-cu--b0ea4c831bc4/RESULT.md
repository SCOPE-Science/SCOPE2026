# Exponential seam screening for three-color excitable waves on cubic ladders

## Finding
For every integer \(n\ge3\), consider synchronous three-state, threshold-one Greenberg–Hastings dynamics on the circular ladder \(C_n\square K_2\) and on the Möbius ladder obtained by twisting one end-to-end pair of rail edges. Let \(P_n\) and \(M_n\) count labelled initial states of **least temporal period three** on these respective graphs. Define \(s_0=3\), \(s_1=0\), \(s_2=-10\), and \(s_n=-5s_{n-2}+3s_{n-3}\) for \(n\ge3\). Then
\[
P_n-M_n=2\bigl(1+(-1)^n\bigr)+4s_n.\tag{1}
\]
Both complete counts are exactly determined by the two characteristic-polynomial identities in the proof below. In particular, writing \(\alpha=(3+\sqrt{17})/2\), letting \(r\) be the unique real root of \(X^3+5X-3\), and setting \(\rho=\sqrt{3/r}<\alpha\), one has
\[
P_n\sim\alpha^n,\qquad M_n\sim\alpha^n,\qquad |P_n-M_n|=O(\rho^n).
\]
Thus a change from an untwisted to a Möbius seam changes the finite-length periodic population, sometimes in either direction, but not its exponential growth constant; the relative discrepancy decays exponentially. The corresponding numbers of primitive temporal orbits are \(P_n/3\) and \(M_n/3\).

## Assumptions and scope
The labelled prism has vertices \((i,j)\) with \(0\le i<n\), \(j\in\{0,1\}\), all rung edges \((i,0)(i,1)\), and horizontal rail edges \((i,j)(i+1,j)\) with indices modulo \(n\). For the twisted ladder retain horizontal edges between columns \(i\) and \(i+1\) for \(0\le i<n-1\), but replace the closing pair with \((n-1,0)(0,1)\) and \((n-1,1)(0,0)\). Both are cubic simple connected graphs when \(n\ge3\).

The dynamics updates each vertex state in \(\{0,1,2\}\) simultaneously by \(1\mapsto2\), \(2\mapsto0\), and \(0\mapsto1\) if and only if an adjacent vertex currently has state \(1\); otherwise \(0\mapsto0\). A primitive-three state is an initial state \(x\) satisfying \(U^3x=x\) and \(Ux\ne x\), not merely a state whose trajectory eventually reaches a three-cycle. Every vertex and temporal phase is distinguished in \(P_n,M_n\).

## Proof
**Step 1: reduction to successor-dominated three-colorings.** On any finite connected graph, a state with least period three cannot have a vertex that is forever \(0\) while an adjacent vertex cycles through nonzero colors. Each vertex in a periodic-three state either stays forever \(0\) or runs through \(0,1,2\) once per three updates, because the transitions from \(1\) and \(2\) are forced. Connectivity therefore implies that every vertex cycles. Consequently a state has least period three precisely when every vertex \(v\) initially has a neighbor of color \(x(v)+1\pmod3\). Necessity follows by observing the time at which \(v\) is resting. Sufficiency follows because, under a simultaneous increment of all colors, the same successor-neighbor relation persists at every time.

**Step 2: an explicit transfer operator.** Set \(\mathcal C=\{0,1,2\}^2\), the nine possible colorings of a rung. Let \(T\) be the \(81\)-by-\(81\) zero-one matrix indexed by ordered pairs \((a,b)\in\mathcal C^2\). For \(a,b,c\in\mathcal C\), put
\[
T_{(a,b),(b,c)}=\prod_{j=0}^1\mathbf1\left\{
  b_{1-j}\equiv b_j+1\ \text{or}\ a_j\equiv b_j+1\ \text{or}\ c_j\equiv b_j+1\pmod3
\right\},
\]
with all other entries zero. A closed length-\(n\) transfer walk is exactly a successor-dominated coloring of the prism; hence \(P_n=\operatorname{tr}(T^n)\). Let \(J\) permute \((a,b)\mapsto(\bar a,\bar b)\), where \(\bar a\) interchanges the two entries of a rung. A length-\(n\) walk whose end rung pair equals the swapped initial pair gives exactly a coloring with the twisted closing seam. Thus \(M_n=\operatorname{tr}(JT^n)\).

**Step 3: symmetry-sector determinants.** The defining predicate is unchanged under simultaneously swapping the two rails, so \(JT=TJ\). The \(+1\) and \(-1\) eigenspaces of \(J\), over \(\mathbb Q\), have dimensions \(45\) and \(36\), respectively: among the 81 pair states there are 9 fixed states and 36 swapped pairs. An explicit rational basis consists of fixed state vectors and sums of swapped pairs in the first sector, and differences of swapped pairs in the second. Substituting the displayed entry rule into those bases yields the exact characteristic polynomials
\[
\begin{aligned}
\chi_+(X)&=X^{30}(X-1)^3(X^2-3X-2)(X^2+X+1)^2(X^3+2X^2+X-1)^2,\\
\chi_-(X)&=X^{28}(X-1)(X+1)(X^3+5X-3)^2.
\end{aligned}\tag{2}
\]
These are finite integer determinant identities, not heuristic spectral fits. The standalone `verification/verify_transfer.py` constructs all 81 entries directly from the displayed predicate, constructs both rational symmetry bases, and computes both characteristic polynomials exactly over \(\mathbb Z\). It also independently compares the power traces with equation (1).

**Step 4: the exact seam difference.** Because traces of matrix powers equal the sums of powers of eigenvalues with algebraic multiplicity even for nondiagonalizable matrices,
\[
P_n-M_n=2\operatorname{tr}(T_-^n)=2(1+(-1)^n)+4s_n,
\]
where \(s_n\) is the power sum of the three roots of \(X^3+5X-3\). Newton identities give \(s_0=3\), \(s_1=0\), \(s_2=-10\) and the recurrence in (1).

**Step 5: the common entropy and strict spectral gap.** The polynomial \(X^2-3X-2\) contributes one simple root \(\alpha>3\) to the positive sector. Its other root has modulus less than one. The two roots of \(X^2+X+1\) lie on the unit circle. The cubic \(X^3+2X^2+X-1\) has one root \(u\in(2/5,1/2)\) and two other roots of modulus \(u^{-1/2}<\sqrt{5/2}<\alpha\). The cubic \(X^3+5X-3\) has exactly one real root \(r\in(1/2,3/5)\) and a conjugate pair of modulus \(\rho=\sqrt{3/r}<\sqrt6<\alpha\). Every other root in (2) has modulus strictly below \(\alpha\). Hence both traces have the sole dominant term \(\alpha^n\) with coefficient one and their difference has order at most \(\rho^n\). This proves the claim for all \(n\ge3\).

## Verification
The standalone SymPy exact-integer checker `verification/verify_transfer.py` verifies all 81 transfer entries, commutation with the seam involution, the \(45/36\) sector decomposition, both characteristic polynomials, and the trace recurrence for \(1\le n\le15\). The independent pure-Python checker `verification/verify_direct.py` enumerates the \(3^{2n}\) labelled states of both graphs for \(3\le n\le6\) and evaluates the original nonlinear update explicitly for \(3\le n\le5\), checking equivalence to the local successor condition.

For \(n=3,4,5,6\), respectively, \((P_n,M_n)=(72,36),(252,48),(450,750),(1566,2454)\). The code, versioned dependency and captured outputs are included as standalone files in this package; no sample enumeration is used as a substitute for the all-length proof.

## Relationship to prior work
The 1993 preprint by Durrett and Griffeath develops excitable cellular-automaton dynamics and spiral activity rather than this finite-ladder orbit census. Gravner, Lyu and Sivakoff (arXiv:1610.07320; full 2018 text inspected) characterize synchronization/activity on arbitrary graphs using graph cycle integrals, but do not derive the period-three multiplicities or twisted-seam transfer spectrum of these two ladder families. Doba (2018; full text inspected) similarly characterizes long-run excitation using maximum cycle density without enumerating immediate period-three states for the two seam types. A related open-ladder primitive-three recurrence concerns \(P_n\square K_2\) with free ends, and does not imply either cyclic or twisted counts: neither boundary trace is determined by open-boundary populations alone. The use of transfer matrices and involution-sector determinants is standard; the exact factors (2), seam-correction recurrence (1), and exponential screening conclusion are the new specific statements under comparison.

## Limitations
Only initially primitive-three states of the specified three-color, one-contact deterministic model are counted. Eventual basins, other temporal periods, more than two rails, and general stochastic excitation are outside scope. The count includes all labelled configurations without quotienting by spatial automorphisms. The literature check cannot exclude an unindexed equivalent formulation, and the original 1993 preprint was available here only at abstract level. There has been no independent audit.

## References
- R. Durrett and D. Griffeath, “Asymptotic Behavior of Excitable Cellular Automata,” arXiv:patt-sol/9303002, first posted 1993-03-22.
- J. Gravner, H. Lyu and D. Sivakoff, “Limiting behavior of 3-color excitable media on arbitrary graphs,” arXiv:1610.07320 (2016-10-24), *Annals of Applied Probability* 28 (2018), 3324–3357; DOI 10.1214/17-AAP1350.
- N. Doba, “The Time Evolution of a Greenberg–Hastings Cellular Automaton on a Finite Graph,” *Complex Systems* 27 (2018), 101–126; DOI 10.25088/ComplexSystems.27.2.101.
