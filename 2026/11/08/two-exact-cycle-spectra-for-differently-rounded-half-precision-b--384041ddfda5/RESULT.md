# Two exact cycle spectra for differently rounded half-precision beta shifts

## Finding

For the generalized Bernoulli map at \(\beta=3/2\), two natural deterministic IEEE-754 binary16 implementations have different *complete* periodic-orbit and attraction-basin censuses. Let \(\mathcal H\) consist of the 15,360 nonnegative binary16 numbers in \([0,1)\), counting positive zero once. Write \(R\) for round-to-nearest, ties-to-even in binary16, and \(\langle t\rangle=t-\lfloor t\rfloor\) for the exact fractional part. Define maps from \(\mathcal H\) to itself by

\[
 A(x)=\langle R(\langle 3x/2\rangle)\rangle,
 \qquad B(x)=\langle R(R(3x/2))\rangle.
\]

The final fractional-part operation identifies an output rounded to one with zero. In \(A\), multiplication and reduction modulo one are exact until one final rounding. In \(B\), the product is rounded first; subtraction of one where necessary is exact at the represented binary16 values in question, so the displayed second \(R\) is redundant but emphasizes the operation order. Both use the exactly representable coefficient \(3/2\).

The complete census is:

| Map | Primitive period \(p\) | Number of primitive cycles of period \(p\) | Basin size (number of starting encodings) |
| --- | ---: | ---: | ---: |
| \(A\) | 1 | 1 | 468 |
| \(A\) | 3 | 1 | 28 |
| \(A\) | 8 | 1 | 2,480 |
| \(A\) | 18 | 1 | 187 |
| \(A\) | 164 | 1 | 12,197 |
| \(B\) | 1 | 1 | 5,705 |
| \(B\) | 3 | 1 | 26 |
| \(B\) | 4 | 1 | 3,138 |
| \(B\) | 24 | 1 | 2,013 |
| \(B\) | 41 | 1 | 4,478 |

There are exactly five primitive cycles for each map and no others. The maximum number of iterations before first entering a cycle is respectively \(144\) for \(A\) and \(155\) for \(B\). Exactly \(512\) of the 15,360 state encodings have different immediate successors under the two maps. In particular, the basin size of the fixed point zero changes from \(468\) to \(5,705\), while the longest cycle changes from period \(164\) to period \(41\). The basin sizes are **uniform counts over representable states**, not Lebesgue-measure basin sizes in the real interval.

## Assumptions and scope

The domain contains finite nonnegative IEEE-754 binary16 numbers strictly less than one, subnormals included. The binary16 positive encodings from hexadecimal `0x0000` through `0x3bff` enumerate the domain in increasing order. The encoding `0x3c00` is the value one, excluded from the domain but included as a rounding candidate; its final fractional part is zero. Each primitive cycle means a simple directed cycle of least period \(p\). The basin of such a cycle is the set of all starting states eventually entering it. Transient length counts steps to first arrival on the cycle, with zero for states already on it. No floating-point exception values, negative zero, alternative rounding modes or stochastic rounding are involved.

## Proof

**1. Exact representation.** For each nonnegative finite binary16 bit pattern \(b\) up to `0x4000` (the value two), let \(n(b)\) be the represented real value multiplied by \(2^{24}\). If the exponent field is zero, \(n(b)\) is the ten-bit fraction field. Otherwise, if the exponent field is \(e\in\{1,\dots,16\}\) and the fraction field is \(f\in\{0,\dots,1023\}\), then

\[
 n(b)=(1024+f)2^{e-1}.
\]

This integer identity follows directly from the binary16 exponent bias and significand. In units of \(2^{-25}\), the exact product of a state represented by \(b\) and \(3/2\) has numerator \(3n(b)\), and one has numerator \(2^{25}\).

**2. Exact successor construction.** Form the strictly increasing integers \(u_j=2n(j)\) for binary16 patterns \(j\) running from zero through `0x3c00`, and \(v_j=2n(j)\) for patterns zero through `0x4000`. Let \(\operatorname{near}_u\) and \(\operatorname{near}_v\) return the nearest indexed entry to an integer argument, resolving exact midway ties toward the entry whose binary16 significand has even least-significant bit. Because successive positive binary16 encodings are numerically ordered, this amounts to choosing the even indexed pattern on a tie. Then the two successor bit patterns are exactly

\[
 \begin{aligned}
 a_b&=\operatorname{near}_u\bigl((3n(b))\bmod 2^{25}\bigr)\bmod15360,\\
 j_b&=\operatorname{near}_v(3n(b)),\\
 b_b&=\operatorname{near}_u\bigl(v_{j_b}\bmod 2^{25}\bigr)\bmod15360.
 \end{aligned}
\]

The integer modulo implements the exact fractional part, and pattern `0x3c00` is mapped to zero. There is no approximation in these successor formulas. The script `verify_beta_graph.py` implements them with exact integers and binary search, independently of any floating-point library.

**3. Exhaustive graph decomposition.** For each of the 15,360 bit patterns, follow successive edges until reaching a previously processed vertex or revisiting a vertex in the current path. The latter produces one new directed simple cycle. Assign its vertices transient length zero, then assign each preceding path vertex its successor's cycle and successor's transient length plus one. If the path reaches an already processed vertex, propagate that existing classification backward along the path. Mark all processed vertices, and continue until every vertex is marked. Every unprocessed graph component is handled exactly once. This deterministic finite algorithm proves both completeness of the cycle list and uniqueness of the basin assignment; it does not extrapolate from sampled trajectories.

The resulting cycle-length-to-basin dictionaries are precisely

\[
 \begin{aligned}
 A:&\quad\{1:468,\ 3:28,\ 8:2480,\ 18:187,\ 164:12197\},\\
 B:&\quad\{1:5705,\ 3:26,\ 4:3138,\ 24:2013,\ 41:4478\}.
 \end{aligned}
\]

The respective sums both equal 15,360. Every detected cycle is rechecked edge by edge, every state's assigned label and distance are checked against its successor, and the maximum transient lengths and number of differing edges are checked against the stated values. A cycle is checked to have no repeated vertex before closure, hence the listed length is primitive. Since the algorithm processes all states, no omitted periodic points or basins are possible.

## Verification

Run `python3 verify_beta_graph.py` using only the Python standard library. It reconstructs all 30,720 successor edges by integer arithmetic and verifies the cycle and basin manifest. Its terminal marker is `BETA_HALF_EXACT_CENSUS_OK; states=15360; differing_successors=512`. The little-endian 16-bit successor arrays have SHA-256 digests:

- \(A\): `a21bb105ef931ff72c49eed6b71a097a8c6ed3089faa7ef35978f468804d66f0`.
- \(B\): `5b2f33943cdf5fa52dafdaaa48c8b354e29542389d30954404fe1842cfe245e6`.

An independent evaluation of every successor using NumPy binary16 arithmetic (with a wider exact product for \(A\) and a binary16-rounded intermediate product for \(B\)) found zero mismatches for either map. That second implementation is supplementary; the proof of the finite-state statements is the exhaustive exact-integer certificate.

## Relationship to prior work

Boghosian, Coveney and Wang (2019) established pronounced finite-precision distortion for the generalized Bernoulli map, including a calculation at \(\beta=3/2\), but their exhaustive orbit analysis uses **binary32**, not these two binary16 evaluation orders. Klöwer, Coveney, Paxton and Palmer (2023) explicitly distinguished low-precision intermediate multiplication from a wider-precision product followed by conversion, and studied corresponding orbit spectra and invariant measures. Their main article includes exact-orbit methodology for individual formats and float16 graphical results, but does not state this joint exhaustive binary16 two-order census with the listed ten period/basin pairs and the 512 differing successors. The latter juxtaposition is the contribution here, not the general observation that finite-precision maps eventually cycle.

## Limitations

The result is a finite-state statement at the single natural parameter \(\beta=3/2\), for precisely stated evaluation and endpoint conventions. No conclusion is asserted for real-number chaotic orbits, alternative compiler contractions, different precision or other beta parameters. A basin's representable-state count is not a fraction of Lebesgue measure. Published supplementary figures and source notebooks associated with the 2023 article may encode some information about one evaluation convention; they do not establish from the inspected material that the two-way exact census is covered. Publication priority beyond inspected sources remains subject to external review.

## References

1. B. M. Boghosian, P. V. Coveney, H. Wang, *A New Pathology in the Simulation of Chaotic Dynamical Systems on Digital Computers*, Advanced Theory and Simulations **2** (2019), 1900125. DOI: `10.1002/adts.201900125`. Open full text: `https://discovery.ucl.ac.uk/id/eprint/10090503/1/Boghosian_et_al-2019-Advanced_Theory_and_Simulations.pdf`.
2. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports **13** (2023), 11410, first published 14 July 2023. DOI: `10.1038/s41598-023-37004-4`. Open full text: `https://pure.uva.nl/ws/files/187636674/Periodic_orbits_in_chaotic_systems_simulated_at_low_precision.pdf`.
