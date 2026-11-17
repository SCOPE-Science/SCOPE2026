# A fivefold ternary clock and exact orbit census on prime-power sunlets

## Finding

Let \(r\ge1\), \(n=3^r\), and let \(H_n=C_n\odot K_1\) be the simple sunlet graph consisting of an \(n\)-cycle with one private pendant vertex at each cycle vertex. For any finite field \(\mathbb F_q\) of characteristic three, so \(q=3^f\) with \(f\ge1\), write \(A_n\) for the open-neighbor adjacency operator on \(\mathbb F_q^{2n}\). On ordered pairs of vertex configurations define the reversible wave
\[
 T_n(u,v)=(A_nu-v,u).
\]
Every state is periodic from its initial instant. The permutation \(T_n\) has **exact order**
\[
 \boxed{5n=5\cdot3^r}.
\]
For every positive integer \(k\), its full fixed-space census is
\[
 \boxed{\#\operatorname{Fix}(T_n^k)=
 \begin{cases}
  1,&5\nmid k,\\
  q^{4\min\{n,\,2\cdot3^{\nu_3(k/5)}\}},&5\mid k,
 \end{cases}}
\]
where \(\nu_3(m)\) is the exponent of three in the positive integer \(m\). Thus the only least positive periods are \(1\) and \(5\cdot3^j\) for \(0\le j\le r\). Writing \(P_d\) for the number of labelled configurations of least period \(d\), their **exact populations** are
\[
 P_1=1,\quad P_5=q^8-1,
\]
\[
 P_{5\cdot3^j}=q^{4\min\{n,\,2\cdot3^j\}}-
 q^{4\min\{n,\,2\cdot3^{j-1}\}}\quad(1\le j\le r),
\]
with \(P_d=0\) for every other positive integer \(d\). Every listed nonzero population is strictly positive; the number of distinct temporal orbits of least period \(d\) equals \(P_d/d\).

For the triangular sunlet \(n=3\) over \(\mathbb F_3\), there is one fixed state, \(6{,}560\) states of least period five, and \(524{,}880\) states of least period fifteen, summing to all \(531{,}441\) states. For comparison, the undecorated cycle under the same reversible wave has global period \(3n\) at odd characteristic, whereas its full one-leaf corona has global period \(5n\). The temporal clock changes by the exact factor \(5/3\), for every \(n=3^r\).

## Assumptions and scope

Graphs are finite, labelled, undirected and loopless. The cycle length is a positive integral power of three with \(n\ge3\), so the two rim neighbors are distinct. Each rim vertex has precisely one additional private leaf. The field can be any finite extension of \(\mathbb F_3\); \(u\) and \(v\) are arbitrary and independent elements of \(\mathbb F_q^{2n}\). The update uses field subtraction and the loopless adjacency sum, not Boolean majority or a graph Laplacian. A temporal orbit is counted by labelled states, without quotienting by spatial rotations or reflections. The inverse is \(T_n^{-1}(s,t)=(t,A_nt-s)\), so recurrence starts at time zero.

## Proof

**1. Identify the spatial module.** Over the given characteristic-three field, set
\[
 R=\mathbb F_q[z,z^{-1}]/(z^n-1),\qquad \epsilon=z-1.
\]
Since \(n=3^r\), the Frobenius identity gives \(z^n-1=(z-1)^n\). Consequently \(R\cong\mathbb F_q[\epsilon]/(\epsilon^n)\) is an Artinian local ring, with \(z=1+\epsilon\) a unit. Using the cyclic shift on the rim, the spatial adjacency on rim and pendant layers is the \(R\)-linear matrix
\[
 A=\begin{pmatrix}c&1\\1&0\end{pmatrix},
 \qquad c=z+z^{-1}=2+\delta,
 \qquad \delta=\frac{\epsilon^2}{1+\epsilon}.
\]
The two-time-layer configuration space is \(R^4\). Multiplication by \(\delta^a\) has kernel dimension \(\min(n,2a)\) over \(\mathbb F_q\) on each copy of \(R\); the denominator is a unit.

**2. A fifth-cyclotomic identity.** Let \(T\) be the \(R\)-linear companion \(T=\begin{psmallmatrix}A&-I_2\\ I_2&0\end{psmallmatrix}\). Direct determinant expansion yields
\[
 \det((X^2+1)I_2-XA)
 =X^4-cX^3+X^2-cX+1
 =\Phi_5(X)-\delta(X^3+X),
\]
where \(\Phi_5(X)=X^4+X^3+X^2+X+1\). The Cayley–Hamilton theorem over the commutative ring \(R\) therefore gives
\[
 \Phi_5(T)=\delta(T^3+T),\qquad
 T^5-I=\delta U,
 \qquad U=(T-I)(T^3+T).
\]
All of these factors commute. Reduction modulo \(\epsilon\) makes \(\delta=0\) and hence \(\bar T^5=I\). Moreover \(\bar T-I\) is invertible: its characteristic polynomial divides \(\Phi_5\), and \(\Phi_5(1)=5=2\ne0\) in characteristic three. Also \(\bar T^2+I\) is invertible. Otherwise an eigenvalue \(\lambda\) over an algebraic closure would obey both \(\lambda^2=-1\) and \(\lambda^5=1\); then \(\lambda^4=1\) forces \(\lambda=1\), contradicting \(1\ne-1\) in characteristic three. Hence \(U=T(T-I)(T^2+I)\) is invertible modulo the maximal ideal and therefore invertible over \(R\).

**3. Fixed spaces of all iterates.** The reduction \(\bar T\) has order five: its fifth power is identity and it is not identity, while five is prime. Thus for \(5\nmid k\) the reduction of \(T^k-I\) is invertible, and so \(T^k-I\) is itself invertible over \(R\); its only fixed vector is zero.

For \(5\mid k\), write \(k=5\cdot3^j h\), with \(j\ge0\) and \(3\nmid h\). From \(T^5=I+\delta U\) and characteristic three,
\[
 T^{5\cdot3^j}-I=(\delta U)^{3^j}
 =\delta^{3^j}U^{3^j}.
\]
Raising this unipotent element to the power \(h\) multiplies \(\delta^{3^j}U^{3^j}\) by an additional polynomial factor congruent to \(h\) modulo \(\epsilon\), hence a unit. As the factors commute and \(U\) is invertible,
\[
 \ker(T^k-I)=\ker(\delta^{3^j}:R^4\longrightarrow R^4).
\]
This kernel has dimension \(4\min(n,2\cdot3^j)\) over \(\mathbb F_q\). Counting its vectors proves the stated fixed-space formula, including field extensions.

**4. Exact order and primitive populations.** At \(j=r\), the fixed space is all of \(R^4\), because \(2\cdot3^r\ge n\). At \(j=r-1\), it is proper because \(2\cdot3^{r-1}<3^r=n\). Hence \(T^{5\cdot3^r}=I\) but \(T^{5\cdot3^{r-1}}\ne I\). The previous step forbids nonzero orbits with periods prime to five, and therefore the exact permutation order is \(5\cdot3^r\). The nested fixed spaces at times \(5,15,\ldots,5\cdot3^r\) have cardinalities shown above. Subtracting consecutive cardinalities gives every primitive-period population. Strict growth of the kernel dimensions gives positivity. Every orbit has no transient because \(T\) is invertible. This completes the proof.

## Verification

The package includes two **independently structured** programs and their actual outputs. Run `python3 checks/check_wave.py` to build the complete matrix of the update from graph adjacency over \(\mathbb F_3\), check the claimed exact orders and calculate fixed-space nullities by modular Gaussian elimination at \(n=3,9,27\). It has no external Python dependencies. Run `g++ -std=c++17 -O3 -o check_orbits checks/check_orbits.cpp && ./check_orbits` for exhaustive direct vertex-level enumeration of all \(3^{12}=531{,}441\) states on the triangular sunlet; this enumerator tracks individual trajectories without using the modular matrix nullities. Compare outputs with `checks/check_wave.out` and `checks/check_orbits.out`. Both programs were actually run from their recorded source paths and passed.

Finite computations do not prove the formulas for arbitrary \(r\) or every extension field; the ring-theoretic argument above provides the infinite-family proof. The reference implementation computes exact residues with integer arithmetic, not floating-point approximations.

## Relationship to prior work

Reversible second-order cellular automata occur in Macfarlane's binary matrix framework (2004) and Vlasov's general construction (initial arXiv version in 2013). Their established reversible mechanism is used, not claimed as new. Barik, Pati and Sarma (2007, particularly their Theorem 3.1) study spectra of graph coronas, but their complex-spectrum formula does not supply the characteristic-three nilpotent ring analysis or a temporal orbit census.

The closest publicly available graph-wave classifications are the characteristic-two dyadic-sunlet result and the general characteristic-two nilpotent-base corona theorem, neither of which assumes characteristic three or entails the fifth-cyclotomic temporal clock. A separate theorem for the reversible finite-field wave on *bare* cycles applies over odd characteristic and yields global period \(3n\), but does not count temporal orbits after the graph is decorated with pendant leaves. Another characteristic-three result concerns Hamming graphs rather than cyclic coronas. These comparisons distinguish statements and hypotheses, not merely titles.

## Limitations

The theorem applies to one private leaf per cycle site, circumference a pure power of three, and a field of characteristic three. It does not claim a classification at arbitrary circumferences, for other graph coronas, or for nonlinear reversible rules. The published Macfarlane manuscript could not be obtained for complete inspection; its publisher abstract concerns three binary rules and pattern weights, but inaccessible details remain a historical-priority risk. Previously unindexed equivalent formulas cannot be ruled out by searching. The mathematical verification here is an internal review and reproducibility check; no independent scientific audit is claimed.

## References

1. A. J. Macfarlane, "Linear reversible second-order cellular automata and their first-order matrix equivalents," *Journal of Physics A: Mathematical and General* **37** (2004), 10791–10814, DOI: 10.1088/0305-4470/37/45/006. Online publication 28 October 2004.
2. S. Barik, S. Pati and B. K. Sarma, "The Spectrum of the Corona of Two Graphs," *SIAM Journal on Discrete Mathematics* **21** (2007), 47–56, DOI: 10.1137/050624029; especially Theorem 3.1.
3. A. Yu. Vlasov, "On generalization of reversible second-order cellular automata," arXiv:1311.4297, first posted 18 November 2013; especially equations (2) and (12).
4. W.-H. Steeb and Y. Hardy, "One-Dimensional Cellular Automata, Conservation Laws and Partial Differential Equations," *Zeitschrift für Naturforschung A* **62** (2007), 569–572, DOI: 10.1515/zna-2007-10-1103.
5. "Pendant memory creates a threefold wave clock on dyadic sunlet graphs," published research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-pendant-memory-creates-a-threefold-wave-clock-on-dyadic-sunlet-g--0c20c45a4756 .
6. "Nilpotent-base coronas have exactly threefold dyadic reversible-wave clocks," published research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-nilpotent-base-coronas-have-exactly-threefold-dyadic-reversible--2c0994ba5f2e .
7. "An exact periodic-orbit census for reversible finite-field waves on cycles," published research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-an-exact-periodic-orbit-census-for-reversible-finite-field-waves--6f3d55fba7da .
8. "A three-class wave clock and exact orbit census for ternary-modular Hamming graphs," published research statement, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-three-class-wave-clock-and-exact-orbit-census-for-ternary-modu--13302e527b48 .
