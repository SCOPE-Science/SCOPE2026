# Exact period-three zeta and entropy of Brian's Brain on three-row tori

## Finding

Let \(F_n\) denote synchronous Brian's Brain (the three-state B2/S/C3 automaton) on the labelled Moore-neighborhood torus \(\mathbb Z_3\times\mathbb Z_n\), for every integer \(n\ge3\). Let \(S_n=\#\operatorname{Fix}(F_n^3)\), and let \(C_3(n)\) be the number of primitive **temporal** three-cycle orbits, without identifying spatial shifts or reflections. Define

\[
\begin{aligned}
q(z)&=1+18z^3+9z^4+81z^6+81z^7+81z^8,\\
r(z)&=1-z-36z^3-18z^4+18z^5+324z^6+1053z^7\\
&\qquad+405z^8-81z^9-11664z^{10}-11664z^{11}-2916z^{12}.
\end{aligned}
\]

The **exact all-circumference period-three census** is

\[
\boxed{\quad S_n=[z^n]\left(-z\frac{d}{dz}\log(q(z)^2r(z))\right),\qquad C_3(n)=\frac{S_n-1}{3},\quad n\ge3.\quad}
\]

Equivalently, the formal spatial zeta function of the time-three-fixed subshift is

\[
\exp\!\left(\sum_{n\ge1}\frac{\operatorname{tr}(A^n)}{n}z^n\right)=\frac{1}{q(z)^2r(z)},
\]

where the explicitly defined \(184\times184\) matrix \(A\) below has \(559\) nonzero unit entries. For the two formal coefficients with \(n=1,2\), this zeta represents symbolic closed walks, not Moore tori with eight distinct neighbors.

The first admissible circumference \(n=3\) has no nontrivial temporal three-cycle; at \(n=4\) there are exactly \(48\) such orbits (\(145\) time-three-fixed states, including the all-rest state). The temporal-three population has exponential rate

\[
C_3(n)\sim\frac{\rho^n}{3},\qquad 3.26505918<\rho<3.26505920,
\]

with \(\rho\) the Perron eigenvalue of \(A\), equivalently the largest-modulus eigenvalue in the characteristic polynomial specified in the proof. Thus the exact growth rate and the sharp first eligible circumference are determined.

## Assumptions and scope

The three states are \(0\) (resting), \(1\) (firing), and \(2\) (refractory). A resting cell fires at the next time if and only if **exactly two** of its eight Moore neighbors are currently firing. Firing cells become refractory, and refractory cells become resting, unconditionally. Neighbor offsets \((\Delta r,\Delta c)\in\{-1,0,1\}^2\setminus\{(0,0)\}\) are reduced modulo \((3,n)\); for \(n\ge3\), the eight positions are distinct. Columns and rows are indexed, not identified under automorphisms. The claim is strictly about fixed points of the third iterate, not longer recurrent cycles or attraction basins.

## Proof

**1. Four local time histories.** A site in a configuration fixed by \(F_n^3\) has either the constantly resting history \((0,0,0)\), or one of the three cyclic phases \((0,1,2)\), \((1,2,0)\), and \((2,0,1)\). Indeed \(1\mapsto2\mapsto0\), and a return from \(0\) to itself in three steps without firing in between forces it to remain resting. Encode the three cycling phases by \(0,1,2\), and the constantly resting history by symbol \(3\). A vertical column has \(4^3=64\) possible symbolic histories.

**2. Exact local compatibility.** For a column symbol \(a\in\{0,\ldots,63\}\), let its row \(j\in\{0,1,2\}\) carry the two-bit digit \(a_j\in\{0,1,2,3\}\). Define the firing-bit mask at time \(t\in\{0,1,2\}\) by

\[
E_t(a)=\sum_{j=0}^2\mathbf1_{\{a_j\ne3,\ (a_j+t)\bmod3=1\}}2^j.
\]

For three successive columns \((a,b,c)\), the number of firing neighbors of middle row \(j\) at time \(t\) is exactly

\[
N_{t,j}(a,b,c)=|E_t(a)|+|E_t(c)|+|E_t(b)|-\mathbf1_{\{j\in E_t(b)\}},
\]

where \(|\cdot|\) denotes the number of set bits. Require \(N_{t,j}=2\) whenever the middle site is in its resting phase of a cycling history, and \(N_{t,j}\ne2\) at all three times whenever it is constantly resting. The firing and refractory steps of cycling histories are automatic. These are necessary and sufficient for the three time slices to evolve correctly.

**3. Closed-walk bijection.** Form the directed graph \(G\) on all ordered pairs \((a,b)\in\{0,\ldots,63\}^2\). Put \((a,b)\to(b,c)\) exactly if the local compatibility conditions of step 2 hold. A cyclic sequence of \(n\) columns yields an indexed closed walk of length \(n\) in \(G\), and conversely each such closed walk uniquely reconstructs a configuration fixed by \(F_n^3\). Thus \(S_n=\operatorname{tr}(G^n)\) for all \(n\ge3\), where \(G\) also denotes its adjacency matrix.

**4. Finite exact reduction and characteristic identity.** The complete graph has \(4096\) pair vertices, \(12286\) directed edges, and \(2125\) vertices incident to edges. Exact strongly connected component decomposition gives exactly one component containing a directed cycle; it has \(184\) vertices and \(559\) internal edges. Every other component is acyclic, so none contributes to the trace of any positive power. Let \(A\) be the adjacency matrix on that sole cyclic component, with its vertices sorted by integer code \(64a+b\). Exact integer polynomial arithmetic gives

\[
\det(xI-A)=x^{156}Q(x)^2R(x),
\]

where

\[
\begin{aligned}
Q(x)&=x^8+18x^5+9x^4+81x^2+81x+81,\\
R(x)&=x^{12}-x^{11}-36x^9-18x^8+18x^7+324x^6+1053x^5\\
&\qquad+405x^4-81x^3-11664x^2-11664x-2916.
\end{aligned}
\]

These are verified by `verify_transfer.py`; the source code defines every edge independently of the displayed factorization. Reversal \(x^dP(1/x)\) of each monic factor gives \(\det(I-zA)=q(z)^2r(z)\). The formal identity \(-z\,d\log\det(I-zA)/dz=\sum_{n\ge1}\operatorname{tr}(A^n)z^n\) proves the exact census. The only time-one-fixed state is the all-rest state: a firing site cannot stay firing, and a refractory site cannot stay refractory. Every remaining fixed point of the third iterate therefore has least temporal period three and belongs to an orbit of three labelled configurations.

**5. Sharp onset and entropy.** Direct closed-walk evaluation gives \(S_3=1\) and \(S_4=145\), yielding zero and \(48\) primitive three-orbits, respectively. The \(184\)-vertex component is strongly connected and contains a self-loop, hence its adjacency matrix is primitive. A strictly positive integer vector in `perron_vector.txt` satisfies the componentwise inequalities

\[
3.26505918\,v<Av<3.26505920\,v.
\]

The checker verifies both inequalities exactly, by integer multiplication, so the Collatz–Wielandt bound rigorously encloses its unique dominant Perron eigenvalue \(\rho\). Perron–Frobenius theory gives \(\operatorname{tr}(A^n)\sim\rho^n\), and the stated asymptotic follows.

## Verification

`verify_transfer.py` builds the entire \(4096\)-vertex graph from the local rule, computes the cyclic strongly connected components, verifies the exact characteristic polynomial via symbolic integer algebra, counts direct closed walks through circumference \(12\), and checks integer-only Perron inequalities against `perron_vector.txt`. `verify_direct.cpp` separately evolves all \(3^{3n}\) labelled original-state configurations for \(n=3,4,5\), and counts fixed points of the third iterate. Its binary is not required to verify or reproduce the result. The saved outputs `transfer_output.txt` and `direct_output.txt` are provided for comparison; the executable proofs are the programs and their justified exhaustive domains, not those outputs alone.

Selected values are \(S_3=1\), \(S_4=145\), \(S_5=181\), \(S_6=3133\), \(S_7=5356\), \(S_8=7417\), \(S_9=40420\) and \(S_{12}=1322353\).

## Relationship to prior work

The Brian's Brain rule and its compulsory refractory step are established in M. Steven Evans's complete 2002 account and in the 1987 cellular-automata book by Toffoli and Margolus (whose relevant excerpt was located but whose full PDF was too large to inspect here). Period-three oscillators on the unrestricted plane were known by 1999; their existence is not claimed as new. Erica Jen's 1988 transfer-matrix framework supplies the general methodological precedent for periodic-point enumerations of cellular automata. The contribution here is the specific all-circumference three-row enumerator, degree-\(28\) nonzero spectral factor, sharp circumference-four onset, and certified entropy rate. No claim is made that the transfer-matrix method itself is novel.

## Limitations

This result uses periodic **three-row** geometry, and does not count all temporal periods, all attractors, or states attracted to a temporal three-cycle. The cyclic-orbit counts retain spatial labelling. Exhaustive direct-state enumeration covers only circumferences three through five; the all-size result depends on the exact finite transfer construction and verified characteristic identity. Historical-priority searches do not exhaust offline oscillator catalogues or inaccessible archival materials, including the uninspected complete 1987 book and the unavailable original 1996 MIT page; independent external validation has not been performed.

## References

1. M. Steven Evans, *Brian's Brain*, January 28, 2002, https://www.msevans.com/automata/briansbrain.html (full primary description and date).
2. *OCA:Brian's Brain*, LifeWiki, https://conwaylife.com/wiki/OCA%3ABrian%27s_Brain (historical oscillator examples, including period three; accessible search extract, full page restricted).
3. E. Jen, *Cylindrical cellular automata*, Communications in Mathematical Physics 118 (1988), 569–590, https://doi.org/10.1007/BF01221109 (general transfer and characteristic-polynomial method; abstract inspected).
4. T. Toffoli and N. Margolus, *Cellular Automata Machines: A New Environment for Modeling* (MIT Press, April 1987), https://people.csail.mit.edu/nhm/cam-book.pdf (relevant indexed excerpt in Chapter 6, not complete PDF inspected).
5. M. Resnick and B. Silverman, *Exploring Emergence: The Brain Rules* (1996; original page presently unavailable), http://www.playfulinvention.com/emergence/mutants.html (historical reference, not relied on for a claim of absence).
