# Exact temporal-four orbit census and spectral growth for elementary cellular automaton Rule 54

## Finding

Let \(F_n\) be synchronous elementary cellular automaton Rule 54 on indexed binary cyclic words of length \(n\ge3\). Its Wolfram rule table, in neighborhood order \(111,110,101,100,011,010,001,000\), is \(00110110\). Write \(R_k(n)=\#\operatorname{Fix}(F_n^k)\), and let \(C_4(n)\) be the number of primitive temporal orbits of least period four, counted without distinguishing the four time phases.

Define an integer sequence \(b_n\) for \(n\ge1\) by the first ten values

\[
(b_1,\ldots,b_{10})=(0,0,0,4,0,12,14,12,18,30),
\]

and the recurrence, for every integer \(n\ge1\),

\[
b_{n+10}=b_{n+6}+2b_{n+4}+2b_{n+3}+b_{n+2}+2b_{n+1}+b_n.
\]

Then, for **every** \(n\ge3\),

\[
\boxed{R_1(n)=R_3(n)=1,\qquad R_2(n)=1+4\mathbf1_{4\mid n},\qquad R_4(n)=1+4\mathbf1_{4\mid n}+2b_n,\qquad C_4(n)=b_n/2.}
\]

Primitive temporal four-cycles exist **exactly** at ring sizes \(n=4\) and every \(n\ge6\), never at \(n=3\) or \(n=5\). The sequence is even, so the orbit formula is integral. Moreover,

\[
C_4(n)\sim \tfrac12\alpha^n\quad(n\to\infty),
\]

where \(\alpha=1.380277569\ldots\) is the unique real root greater than one of \(z^4-z^3-1=0\). This is the spatial growth rate of the primitive temporal-four orbit population, not a claim about the full dynamics or longer least temporal periods.

## Assumptions and scope

Cells \(i\in\mathbb Z/n\mathbb Z\) take values in \(\{0,1\}\). For every \(n\ge3\) and \(x\in\{0,1\}^n\),

\[
(F_n(x))_i=\left(54\mathbin{\mathrm{div}} 2^{4x_{i-1}+2x_i+x_{i+1}}\right)\bmod 2.
\]

Indices are reduced modulo \(n\), and sites are labelled. Temporal fixed-point counts distinguish spatial translates; temporal orbits identify only the four phases of an orbit, not spatial translations or reflections. The conclusions concern periods dividing one, two, three, or four; no bound on other possible periods or transients is asserted. Source literature is used to motivate Rule 54 and its characteristic period-four structures, but the census is derived afresh below.

## Proof

**Space-time transfer.** For \(p\in\{1,2,3,4\}\), encode the length-\(p\) time history at one site by a binary integer \(a\in\{0,\ldots,2^p-1\}\), whose bit \(t\) is its state at time \(t\). Form the directed graph \(G_p\) on ordered pairs \((a,b)\), with a directed edge

\[
(a,b)\longrightarrow(b,c)
\]

if and only if, for every \(t\in\mathbb Z/p\mathbb Z\), bit \(t+1\) of \(b\) is the Rule 54 output from bits \(t\) of \(a,b,c\). A length-\(n\) closed directed walk corresponds bijectively to a complete periodic space-time cylinder with \(n\) indexed sites and \(p\) time rows. Determinism makes its first row a unique word fixed by \(F_n^p\). Thus, if \(T_p\) is the adjacency matrix,

\[
R_p(n)=\operatorname{tr}(T_p^n).
\]

**Complete cyclic-component calculation.** The rule gives exactly the following strongly connected components containing directed cycles: for \(p=1\) and \(p=3\), the sole loop \((0,0)\); for \(p=2\), the loop \((0,0)\) and one simple directed four-cycle; for \(p=4\), the loop \((0,0)\), a simple directed four-cycle, and two disjoint directed components each with ten vertices and fourteen edges. Their cyclic parts exhaust every closed walk, because a closed walk cannot use an edge outside a cyclic strongly connected component. These lists can be reconstructed by checking all \((2^p)^3\) possible consecutive site-time columns; `transfer_certificate.py` contains this exhaustive integer procedure.

Here is an explicit finite certificate for one ten-vertex component. Enumerate its vertices in the order

```
0:(1,1)  1:(1,9)  2:(4,4)  3:(4,6)  4:(5,6)
5:(5,9)  6:(6,4)  7:(6,5)  8:(9,1)  9:(9,5)
```

Its fourteen directed edges, specified by zero-based source and target indexes, are

```
(0,1) (1,9) (2,3) (3,7) (4,6) (4,7) (5,8)
(5,9) (6,2) (6,3) (7,5) (8,0) (8,1) (9,4)
```

Write \(B\) for this ten-by-ten zero-one adjacency matrix. Cyclically rotating the four time bits of each coordinate maps this component onto the other ten-vertex component and conjugates their adjacency matrices. Exact determinant expansion or the integer Faddeev–LeVerrier computation yields

\[
\det(zI-B)=z^{10}-z^6-2z^4-2z^3-z^2-2z-1
=(z+1)(z^4-z^3-1)(z^5+z^3+z+1).
\]

The single loop contributes \(1\) to every \(R_p(n)\); the four-cycle contributes \(4\) if \(4\mid n\), and zero otherwise. Consequently,

\[
R_4(n)=1+4\mathbf1_{4\mid n}+2\operatorname{tr}(B^n),
\qquad R_2(n)=1+4\mathbf1_{4\mid n},
\]

with \(R_1(n)=R_3(n)=1\) by the other component calculations. The characteristic polynomial of \(B\), Cayley–Hamilton, and the first ten exact traces give the displayed recurrence with \(b_n=\operatorname{tr}(B^n)\). In particular every initial trace is even, hence every subsequent trace is even. Exactly \(R_4(n)-R_2(n)=2b_n\) words have least temporal period four; dividing by four yields \(C_4(n)=b_n/2\).

**Sharp ring-size support.** The first five traces vanish except at \(n=4\), where \(b_4=4\). The component represented by \(B\) has a vertex \((5,6)\) supporting closed walks of each length \(4,6,7,8,9\). Explicit examples of their vertex sequences are:

```
4: (5,6) (6,5) (5,9) (9,5) (5,6)
6: (5,6) (6,4) (4,6) (6,5) (5,9) (9,5) (5,6)
7: (5,6) (6,4) (4,4) (4,6) (6,5) (5,9) (9,5) (5,6)
8: (5,6) (6,4) (4,6) (6,5) (5,9) (9,1) (1,9) (9,5) (5,6)
9: (5,6) (6,4) (4,4) (4,6) (6,5) (5,9) (9,1) (1,9) (9,5) (5,6)
```

Concatenating the length-four loop with a closed walk of length \(6,7,8\), or \(9\) produces a closed walk of every length \(n\ge6\), by its residue modulo four. Therefore \(b_n>0\) precisely for \(n=4\) and \(n\ge6\) in the stated range.

**Asymptotic.** The ten-vertex component is strongly connected and has cycles of coprime lengths four and seven, so its nonnegative adjacency matrix \(B\) is primitive. Perron–Frobenius gives a unique simple positive eigenvalue of maximum modulus. The displayed factorization shows the only positive root exceeding one is \(\alpha\), the positive root of \(z^4-z^3-1\). Hence \(\operatorname{tr}(B^n)=\alpha^n+o(\alpha^n)\), proving the asymptotic.

## Verification

The standalone `transfer_certificate.py` reconstructs all four time-window transfer graphs, identifies cyclic components by Tarjan's algorithm, produces both ten-state matrices, verifies the integer characteristic polynomial and recurrence, and checks exact trace values and representative closed walks. It needs only Python 3 standard library modules. Its supplied output is `transfer_output.txt`.

Independently, `direct_enumeration.cpp` applies Rule 54 directly to every binary word on each ring \(3\le n\le20\), without consulting the transfer graphs. It counts returns at times one, two, three and four and verifies the orbit formula. Compile it with `c++ -O3 -std=c++17 direct_enumeration.cpp -o direct_enumeration` and run `./direct_enumeration 20`. Its output is `direct_output.txt`.

Representative counts are:

| \(n\) | \(R_2(n)\) | \(R_4(n)\) | \(C_4(n)\) |
|---:|---:|---:|---:|
| 3 | 1 | 1 | 0 |
| 4 | 5 | 13 | 2 |
| 5 | 1 | 1 | 0 |
| 6 | 1 | 25 | 6 |
| 7 | 1 | 29 | 7 |
| 8 | 5 | 29 | 6 |
| 9 | 1 | 37 | 9 |
| 10 | 1 | 61 | 15 |
| 12 | 5 | 85 | 20 |
| 20 | 5 | 1313 | 327 |

The finite direct checks are not used to extrapolate an infinite theorem: the transfer identity, finite graph certificate, Cayley–Hamilton recurrence and Perron argument provide its all-\(n\) proof.

## Relationship to prior work

Rule 54 and its period-four ether and stationary gliders are classical. Martínez, Adamatzky and McIntosh (2014) use de Bruijn diagrams, glider tiles, and finite cycle diagrams, including examples on finite periodic rings and a table of selected attractors. Their inspected sections on de Bruijn graphs and cycle diagrams do not give this all-circumference primitive temporal-four count, the ten-state characteristic polynomial, or its spatial growth law. The general use of de Bruijn transfer graphs is not new; the specific complete decomposition and all-size formula are the asserted contribution.

Redeker's 2014 thesis addresses ether formation and flexible-time dynamics for Rule 54. Its abstract was consulted, but not its complete text. Public records on Rule 54's one-step image counts, periodic-predecessor lifting, and singleton-predecessor counts study image fibers rather than temporal four-step returns, and those distinct invariants do not determine the formula above. A similarly named *reversible* Rule 54 appearing in later integrable-circuit literature is a different block-partitioned map and is not the Wolfram elementary rule studied here.

## Limitations

The theorem is restricted to the synchronous Wolfram Rule 54 map on finite cyclic binary words with \(n\ge3\), and to fixed points of the first four temporal iterates. It makes no assertions about longer least periods, attraction-basin sizes, or typical transient times. The local transfer certificate and direct enumeration are reproducible but are not independent external mathematical validation. Historical-priority searching cannot exclude every unpublished or inaccessible earlier derivation, and the complete Redeker thesis was not inspected.

## References

1. G. J. Martínez, A. Adamatzky, and H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, arXiv:1410.3096v1, first posted 2014-10-12. https://arxiv.org/html/1410.3096v1
2. M. Redeker, *Flexible Time and Ether in One-dimensional Cellular Automata*, arXiv:1403.0193v1, first posted 2014-03-02. https://arxiv.org/abs/1403.0193
3. Public mathematical-record comparisons: *Exact cyclic image counts and entropy for elementary Rule 54*; *Periodic lifting and exact one-step image enumeration for Rule 54*; *Exact singleton-predecessor generating function for cyclic elementary Rule 54*. These concern one-step images or fibers, not the temporal-four orbit census.
