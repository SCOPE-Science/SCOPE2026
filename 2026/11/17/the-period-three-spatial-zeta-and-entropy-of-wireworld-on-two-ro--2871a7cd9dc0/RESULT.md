# The period-three spatial zeta and entropy of Wireworld on two-row tori

## Finding

For the usual four-state Wireworld rule on the labelled periodic Moore lattice \(\mathbb Z_2\times\mathbb Z_n\), \(n\ge3\), counting all eight offsets with multiplicity, let \(R_n=\#\operatorname{Fix}(F_n^3)\) and let \(C_n\) be the number of primitive temporal three-cycle **orbits** without identifying translations. Write

\[
\begin{aligned}
a(z)&=1-z^2+3z^4-3z^6+3z^8,\\
b(z)&=1+2z^2+3z^4+6z^6+3z^8,\\
c(z)&=1+2z+5z^2+12z^3+29z^4-8z^5-41z^6\\
 &\qquad+122z^7+153z^8-30z^9-36z^{10},\\
d(z)&=1-8z+18z^2-62z^3+47z^4+116z^5\\
 &\qquad+126z^6+280z^7-77z^8-648z^9+12z^{10}+144z^{11},\\
Q(z)&=a(z)^2b(z)c(z)^2d(z).
\end{aligned}
\]

The complete period-three spatial counting law is

\[
R_n=[z^n]\left(-z\frac{Q'(z)}{Q(z)}\right),\qquad
C_n=\frac{R_n-4^n}{3}\quad(n\ge3).
\]

The exponential growth base \(\lambda\) is the largest real root of

\[
X^{11}-8X^{10}+18X^9-62X^8+47X^7+116X^6+126X^5+280X^4-77X^3-648X^2+12X+144.
\]

It satisfies \(6.44175<\lambda<6.44176\) with a finite exact integer certificate, and \(C_n\sim\lambda^n/3\). In particular, primitive period-three configurations have entropy \(\log\lambda/2\approx0.9314006051\) per physical site, and there are exponentially many three-cycle orbits at large circumference.

## Assumptions and scope

Each cell is empty, head, tail or conductor. Empty persists, head becomes tail, tail becomes conductor; conductor becomes head precisely when one or two of its eight Moore-neighbor *offset incidences* are heads, and otherwise stays conductor. The two vertical shifts land at the same opposite-row site, as do the two diagonals of each horizontal direction: **multiplicity is retained**. Thus the six opposite-row incidences and two same-row horizontal incidences are distinct update contributions even when sites repeat. Every time step is synchronous. Horizontal coordinates are labelled, and a temporal orbit is identified only under time translation. The small-width formulas are asserted for \(n\ge3\), where the left and right column positions are distinct.

## Proof

A cell returning after three steps has exactly five possible three-time histories: always empty; always conductor; or a rotating head–tail–conductor history with head phase \(\phi\in\{0,1,2\}\). Write these histories as symbols \(0,1,2,3,4\), with head at time \(t\) when \(s=2+t\). Each column is an ordered pair of symbols, so there are 25 column symbols \(a\).

For columns \(L,M,R\) and row \(r\in\{0,1\}\), at time \(t\in\{0,1,2\}\), let \(I_t(s)=\mathbf1_{\{s=2+t\}}\). The exactly eight-offset head count at the middle cell is

\[
h_{r,t}=I_t(L_r)+I_t(R_r)+2I_t(L_{1-r})+2I_t(M_{1-r})+2I_t(R_{1-r}).
\]

A middle history \(M_r=1\) is legal precisely when \(h_{r,t}\notin\{1,2\}\) for all three times. If \(M_r=2+\phi\), it is legal precisely when \(h_{r,(\phi+2)\bmod3}\in\{1,2\}\); no condition is needed in its head or tail phases. Empty histories impose no condition. These local tests are necessary and sufficient for three-step return.

Define the 625-state adjacency matrix \(T\), indexed by pairs \((a,b)\) of 25 column symbols, with one edge \((a,b)\to(b,c)\) precisely when the middle column passes the above test. Labelled cyclic column words of length \(n\) correspond bijectively to closed length-\(n\) walks, hence \(R_n=\operatorname{tr}(T^n)\).

There are exactly 4,090 edges. The subgraph on directed cycles consists of one strongly connected component of 283 vertices and 1,816 edges; all other vertices lie on no directed cycle. Its exact characteristic polynomial is

\[
X^{228}p_8(X)^2q_8(X)r_{10}(X)^2s_{11}(X),
\]

where each factor is the reversed polynomial of \(a,b,c,d\), respectively: \(p_8(X)=X^8a(1/X)\), \(q_8(X)=X^8b(1/X)\), \(r_{10}(X)=X^{10}c(1/X)\), and \(s_{11}(X)=X^{11}d(1/X)\). This identity is established by exact symbolic characteristic-polynomial calculation from the fully specified integer adjacency matrix and replayed by `verify_transfer.py`. Therefore \(\det(I-zT)=Q(z)\). The formal identity \(\sum_{n\ge1}\operatorname{tr}(T^n)z^n=-z(\log\det(I-zT))'\) proves the generating function.

The only fixed configurations consist entirely of empty and conductor cells, numbering \(2^{2n}=4^n\). By divisibility of temporal periods into three, all other third-return states belong to primitive three-cycles, so \(C_n=(R_n-4^n)/3\).

The recurrent component is irreducible and has a self-loop, hence is primitive. Its Perron eigenvalue is the unique strictly dominating eigenvalue in modulus of the cyclic core. `spectral_certificate.json` gives a positive integer vector \(v\) indexed by this component and proves, entrywise using exact integer comparisons,

\[
644175v<100000Tv<644176v.
\]

Collatz–Wielandt gives \(6.44175<\lambda<6.44176\). The factored characteristic polynomial identifies it as the largest real root of \(s_{11}\), and primitivity gives \(R_n=\lambda^n+O(\mu^n)\) for some \(\mu<\lambda\). Since \(4<\lambda\), the claimed asymptotic for \(C_n\) follows.

## Verification

Two distinct programs are supplied. `verify_transfer.py` enumerates all \(25^3=15{,}625\) local triples, rebuilds the graph, verifies strongly connected components and the exact symbolic polynomial, checks the integer Perron witness, and produces counts by Newton power sums. `direct_enumeration.cpp` independently applies the original four-state Moore update to every initial state for widths three through six; there are \(4^{2n}\) such states at each width. Its result agrees with the transfer counts exactly.

| Width | Fixed | Three-step return | Primitive three-cycle orbits |
|---:|---:|---:|---:|
| 3 | 64 | 238 | 58 |
| 4 | 256 | 1,840 | 528 |
| 5 | 1,024 | 12,064 | 3,680 |
| 6 | 4,096 | 70,540 | 22,148 |
| 7 | 16,384 | 453,478 | 145,698 |
| 8 | 65,536 | 2,975,344 | 969,936 |

The first four rows are independently simulated; subsequent rows and all larger lengths follow from the proved transfer identity.

## Relationship to prior work

Dewdney's 1990 account is the earliest precisely dated archival Wireworld source established here. Gladkikh and Nigay's 2018 detailed primary treatment describes period-three signal clocks and introduces the seven-state Wireworld++ generalization. Period-three clocks themselves, and the five-history encoding as an elementary method, are not claimed as new. The contribution is the complete two-row periodic eight-incidence three-cycle census, its factored spatial zeta and exact exponential entropy. No equivalent formula was identified in the inspected material or targeted bibliographic comparisons; this is a qualified priority assessment, not proof of global uniqueness.

## Limitations

The result applies to the periodic two-row quotient with offset multiplicities. Replacing it by a simple graph that counts each distinct site once changes the rule and invalidates these formulas. It does not count other temporal periods, spatial-symmetry quotients, basin populations or wider/open strips. The entire original 1990 magazine article was not accessible for full-text inspection; unidentified historical calculations remain a priority risk. Direct simulation at bounded sizes alone does not establish the infinite-family result: the exact transfer identity does.

## References

- A. K. Dewdney, “Computer Recreations: The cellular automata programs that create wireworld, rugworld and other diversions,” *Scientific American* **262** (1990), 146–149. First listed public date 1990-01-01. https://doi.org/10.1038/scientificamerican0190-146
- V. Gladkikh and A. Nigay, “Wireworld++: A Cellular Automaton for Simulation of Nonplanar Digital Electronic Circuits,” *Complex Systems* **27** (2018), 19–41. https://doi.org/10.25088/ComplexSystems.27.1.19
