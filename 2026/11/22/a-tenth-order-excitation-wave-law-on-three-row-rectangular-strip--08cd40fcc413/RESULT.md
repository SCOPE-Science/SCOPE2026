# A tenth-order excitation-wave law on three-row rectangular strips

## Finding

For the synchronous, three-state Greenberg–Hastings excitation rule on every open rectangular grid \(P_3\square P_n\), \(n\ge2\), the exact number \(N_n\) of configurations already having **primitive temporal period three** has generating function

\[
\boxed{\sum_{n\ge2}N_nz^{n-2}=\frac{6+18z-42z^2+84z^3-690z^4+990z^5+402z^6+192z^7+36z^8}{1-11z+18z^2+22z^3+6z^4-162z^5+29z^6+105z^7+62z^8+22z^9+4z^{10}}.}
\]

Its first ten coefficients, for \(n=2,\ldots,11\), are

\[
6,\ 84,\ 774,\ 6954,\ 59988,\ 519126,\ 4486806,\ 38771652,\ 335039910,\ 2895154566.
\]

Every counted configuration is one of three temporal phases of its orbit, so there are exactly \(N_n/3\) primitive three-cycle orbits.

Writing
\[
Q(x)=x^{10}-11x^9+18x^8+22x^7+6x^6-162x^5+29x^4+105x^3+62x^2+22x+4,
\]
its unique root of modulus exceeding eight is a positive real number \(\lambda=8.64121650202738\ldots\). The population satisfies \(N_n\sim c\lambda^n\), where \(c=0.144327187163\ldots>0\), and the fraction of all \(27^n\) labelled initial states that belongs to an immediate primitive three-cycle tends to zero exponentially at rate \(\lambda/27\).

A width-dependent entropy amplification also follows: the spatial entropy per vertex is \((\log\lambda)/3=0.7188477905\ldots\), strictly greater than the corresponding two-row open-ladder value \(\frac12\log((3+\sqrt{17})/2)=0.6350983165\ldots\). This is a comparison of the same primitive-three sector at different widths, not a statement about overall topological entropy of every trajectory.

## Assumptions and scope

The graph has vertices \((i,j)\) for columns \(1\le i\le n\) and rows \(j=0,1,2\), with undirected nearest-neighbor edges between consecutive columns and consecutive rows. There is **no wrap-around boundary** in either direction. Every vertex carries one of the colors \(0,1,2\), meaning resting, excited, and refractory. In one simultaneous update \(1\mapsto2\), \(2\mapsto0\), and a resting vertex becomes excited exactly when at least one adjacent vertex is currently excited. Otherwise it remains resting. The contact threshold is one. All vertices are indexed; temporal phases are distinct configurations. The theorem only counts configurations periodic from time zero with least period exactly three; it does not count their full attraction basins or other primitive periods.

## Proof

**1. Characterization of immediate three-cycles.** On any finite connected graph, if a state satisfies \(F^3(x)=x\), a vertex must either be at rest through all three updates or traverse the forced excited–refractory–resting progression and advance by one color modulo three on every update. Indeed, an excited state must become refractory and then resting, while a resting state can only become excited. A permanently resting vertex cannot neighbor a vertex that cycles through all colors: the latter becomes excited at one of the three phases and would force the former to leave rest. Connectivity therefore implies that the only fixed-by-three state not advancing at *every* vertex is the all-rest state. Hence a nontrivial primitive three-periodic state is exactly a ternary coloring in which **each vertex has a neighbor bearing its successor color** \(x_v+1\pmod3\). Conversely, if this condition holds, all colors advance simultaneously; their successor contacts persist under common color increments, giving a primitive three-cycle.

**2. Exact transfer.** A column is a triple \(c=(c_0,c_1,c_2)\in\mathbb Z_3^3\). Let \(V(c;l,r)\in\{0,1\}\) assert that for every row \(j\), at least one of its actual vertical neighbors in \(c\), its left neighbor in \(l\) if present, or its right neighbor in \(r\) if present has color \(c_j+1\pmod3\). Missing boundary columns are denoted \(\varnothing\). The index set has \(3^3\cdot3^2=243\) elements \((l,u,v)\), with normalized current column \(c=(0,u,v)\) and preceding column \(l\in\mathbb Z_3^3\). Define boundary vectors and a matrix by

\[
\begin{aligned}
a_{(l,u,v)}&=V(l;\varnothing,(0,u,v)),\\
b_{(l,u,v)}&=V((0,u,v);l,\varnothing),\\
M_{(l,u,v),(l',u',v')}&=\sum_{r\in\mathbb Z_3^3}V((0,u,v);l,r)\,\mathbf1\{(l',u',v')=((0,u,v)-r_0\mathbf1,r_1-r_0,r_2-r_0)\}.
\end{aligned}
\]

All color differences are modulo three, and \(\mathbf1=(1,1,1)\). Normalization uses the top color of the next column; the missing global color is restored by exactly three choices. Each fully admissible coloring has exactly one path through the transfer, so
\[
\boxed{N_n=3aM^{n-2}b,\qquad n\ge2.}
\]
The explicit construction has 243 states and 2465 transition arcs (counting multiplicity). The embedded `verification/verify_transfer.py` independently reconstructs every integer entry from this definition.

**3. All-length recurrence, not sequence guessing.** Let \(Q\) be the monic integer polynomial above. The matrix is exactly 243-dimensional. Direct integer evaluation from the matrix definitions yields the **243 separate exact identities**
\[
3aM^kQ(M)b=0\qquad(0\le k<243).
\]
These are verified without floating point by the standalone program, which constructs the 254 required successive integer values rather than relying on a stored sequence table. The Cayley–Hamilton theorem applies to \(M\), so its scalar sequence \(3aM^kQ(M)b\) obeys a recurrence of order at most 243. Thus these 243 consecutive zeros force all later terms to vanish, proving the \(Q\)-recurrence for **every** \(n\ge2\). From the first ten exact transfer evaluations, the displayed rational generating function follows by coefficient multiplication. Its numerator and denominator are coprime over \(\mathbb Q\), certified by their reduction modulo seven (the denominator has nonzero top coefficient mod seven, and the Euclidean gcd is one).

**4. Entropy and sharp root.** On \(|x|=8\), decompose \(Q(x)=x^9(x-11)+R(x)\), where \(\deg R\le8\). The triangle bound is \(|R(x)|\le355185204<402653184\le |x^9(x-11)|\). Rouché's theorem yields nine roots of \(Q\) inside \(|x|<8\) and exactly one outside. Since \(Q(8)=-58084812<0\) and \(Q(9)=99120064>0\), that exterior root \(\lambda\in(8,9)\) is real, positive, and simple. The rational generating numerator does not cancel its pole, so \(N_n\sim c\lambda^n\) with nonzero \(c\); nonnegative integer populations imply \(c>0\). Standard evaluation of the exact residue gives the stated numerical constants. Previously established two-row primitive-three growth is \(\lambda_2=(3+\sqrt{17})/2<4\), while \(\lambda>8\), so \(\lambda^2>64>\lambda_2^3\), which proves \(\frac13\log\lambda>\frac12\log\lambda_2\).

## Verification

Run `python3 verification/verify_transfer.py` using Python 3.9 or later. It builds the 243 normalized states, 2465 arcs and both boundary vectors; checks the first ten counts, all 243 Cayley–Hamilton base identities, the exact rational numerator, a strict Rouché bound, and Euclidean coprimality mod seven. The bundled `verification/transfer_results.txt` is the reproduced output.

Independently, compile and run `verification/verify_direct.cpp` using `g++ -O3 -std=c++17 verification/verify_direct.cpp -o verify_direct && ./verify_direct`. This independently implements local time evolution on every one of the \(3^6\), \(3^9\), and \(3^{12}\) initial colorings for widths two through four. Its exact counts \(6,84,774\) match the transfer; fixed states are exactly one at each size. See `verification/direct_results.txt`. Exhaustive tests at finite widths alone would not prove the unrestricted result; the exact 243-dimensional matrix identity and Cayley–Hamilton argument do so.

## Relationship to prior work

Durrett and Steif (1991), Sections 4–5, study clocks and temporal three-cycles of Greenberg–Hastings dynamics in lattice boxes but do not enumerate immediate primitive-three states on open three-row grids. Gravner, Lyu and Sivakoff (2016), Theorem 3 and Sections 1–3, provide general finite-graph dynamical and circulation characterizations rather than this strip's tenth-order exact enumeration. A published two-row open-ladder census supplies the benchmark growth \((3+\sqrt{17})/2\); its three-dimensional reduced transfer and cubic recurrence do **not** cover a three-row grid with interior degree four. General transfer-matrix existence results permit a finite computational method but do not imply this denominator, all ten coefficients, or the strict width-dependent per-vertex entropy comparison. Published exact three-period claims for three-row *rook* graphs have all-to-all column connectivity rather than rectangular nearest-neighbor edges. Primary claims were compared at the level of graph edges, contact rule, boundary conditions, and actual generated populations, not merely article titles.

## Limitations

The enumeration covers only immediate primitive period-three configurations, not eventual period-three basins or other temporal periods. It requires **open longitudinal boundaries** and fixed width three; cylindrical or toroidal closure changes the transfer. The proof is a finite, exact integer certificate plus Cayley–Hamilton, with standalone standard-library code; the independently checked exhaustive widths are only two through four. The early Greenberg–Greene–Hastings (1980) combinatorial paper's abstract concerns two-dimensional periodic structures, but its full text was unavailable for complete priority comparison, leaving a historical originality risk. Broader unpublished or unindexed equivalents cannot be excluded. No independent external validation is claimed.

## References

1. R. Durrett and J. E. Steif, *Some rigorous results for the Greenberg–Hastings Model*, Journal of Theoretical Probability **4** (1991), 669–690, DOI: 10.1007/BF01259549. Author PDF: https://sites.math.duke.edu/~rtd/reprints/paper66.pdf.
2. R. Durrett and D. Griffeath, *Asymptotic Behavior of Excitable Cellular Automata*, initial public preprint March 22, 1993, https://arxiv.org/abs/patt-sol/9303002.
3. J. Gravner, H. Lyu, and D. Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, initial preprint October 24, 2016, https://arxiv.org/abs/1610.07320, published Annals of Applied Probability 28 (2018), 3324–3357.
4. *Exact primitive-three wave census on open ladders*, previously public mathematical record (open two-row nearest-neighbor strips); the established two-row entropy is quoted for direct comparison.
5. J. M. Greenberg, C. Greene, and S. P. Hastings, *A combinatorial problem arising in the study of reaction-diffusion equations*, SIAM Journal on Algebraic and Discrete Methods **1** (1980), 34–42, DOI: 10.1137/0601006 (abstract available; complete text not inspected).
