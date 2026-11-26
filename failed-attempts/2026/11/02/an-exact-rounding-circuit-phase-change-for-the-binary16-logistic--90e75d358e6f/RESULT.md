# An exact rounding-circuit phase change for the binary16 logistic map

## Finding

Let \(S\) be the set of 15,361 nonnegative IEEE 754 binary16 numbers in \([0,1]\), where signed zero is represented once. Let \(R\) denote correctly rounded conversion to binary16 using round-to-nearest, ties-to-even. At the chaotic logistic parameter \(4\), compare the following **different finite-state maps on exactly the same set**:
\[
F_{\mathrm{staged}}(x)=R\bigl((4x)R(1-x)\bigr),\qquad
F_{\mathrm{single}}(x)=R\bigl(4x(1-x)\bigr).
\]
The factor \(4x\) is exactly representable throughout \(S\). The second map is an idealized exact-polynomial-then-round evaluator, not an assertion about a particular compiler or fused instruction. Both maps send \(S\) to itself.

**Exact finite-state theorem.** The complete periodic orbit counts, attraction-basin cardinalities, and maximal transient distances are:

| Evaluator | Period-one basins (at \(0\) and \(3/4\)) | Nontrivial primitive cycle | Its basin | Maximum steps before entering a cycle |
| --- | --- | --- | --- | --- |
| staged rounding | 5,092 and 2 | exactly one, period 40 | 10,267 | 83 |
| one final rounding | 15,236 and 8 | exactly one, period 5 | 117 | 109 |

There are no other periodic orbits. In both systems, the fixed points are \(0\) and \(3/4\). The two nontrivial cycles have no elements in common.

Let \(\nu\) be the uniform probability distribution on the *finite set of binary16 encodings* \(S\), and define the asymptotic Cesàro distributions
\[
\mu_i=\lim_{T\to\infty}\frac1T\sum_{t=0}^{T-1}(F_i^t)_*\nu,
\quad i\in\{\mathrm{staged},\mathrm{single}\}.
\]
Both limits exist, and their exact total-variation distance is
\[
\boxed{\ \|\mu_{\mathrm{staged}}-\mu_{\mathrm{single}}\|_{\mathrm{TV}}
=\frac{10267}{15361}=0.6683809647809388\ldots\ }.
\]
In particular, changing only the arithmetic evaluation and rounding placement can change the eventual discrete stationary statistics by more than two thirds in total variation, despite identical input encodings and the same continuum polynomial.

## Assumptions and scope

Binary16 is interpreted with a five-bit biased exponent, ten fraction bits, subnormals, and IEEE ties-to-even rounding. Nonnegative codes \(c=0,\ldots,15360\) index the states in increasing numerical order. Set \(D=2^{24}\). For exponent \(e=c\mathbin{\mathrm{div}}1024\) and fraction \(m=c\bmod1024\), the exact state is \(u(c)/D\), where
\[
u(c)=\begin{cases}m,&e=0,\\(1024+m)2^{e-1},&1\le e\le15.\end{cases}\]
Here the maximum allowed code is the encoding of \(1\), namely \(c=15360\). The initial distribution is **uniform over codes**, not uniform with respect to real Lebesgue length in \([0,1]\); these are very different measures. In particular, no assertion is made for randomly initialized real-number states or any other floating-point implementation.

The staged evaluator performs the subtraction and final multiplication with binary16 roundings. The single evaluator performs the entire quadratic polynomial over exact rationals before one binary16 rounding. All arithmetic definitions, including ties, are mathematical specifications independent of the hardware arithmetic used to execute the provided checker.

## Proof

**1. Complete state list.** There are 1,024 codes with exponent zero, fourteen blocks of 1,024 codes with exponents 1 through 14, and one endpoint code for \(1\). Thus \(|S|=1024+14\cdot1024+1=15361\). The function \(u(c)\) above gives strictly increasing integer coordinates; it includes every subnormal, normal, zero, and the upper endpoint of \([0,1]\) exactly once.

**2. Exact adjacency construction.** For an integer numerator \(A\ge0\) and positive integer denominator \(B\), define \(\rho(A,B)\) to be the code minimizing \(|u(c)-A/B|\), with ties resolved toward the even least-significant encoding bit. Binary search in the entire sorted integer array \(u(0),\dots,u(15360)\), followed by integer comparison of the adjacent gaps, computes \(\rho\) without any floating-point operation. With \(c\) denoting the current code and \(w=\rho(D-u(c),1)\), the exact transition arrays are
\[
T_{\mathrm{staged}}(c)=\rho(4u(c)u(w),D),\qquad
T_{\mathrm{single}}(c)=\rho(4u(c)(D-u(c)),D).
\]
For the staged evaluator, the largest pre-final-rounded polynomial value is exactly \(1+8144/D\), which is strictly below the binary16 midpoint \(1+8192/D\) above the endpoint \(1\); consequently \(\rho\) restricted to \([0,1]\) performs the correct binary16 rounding even for this small overshoot. This calculation and the independent binary16 comparison are checked by the program.

**3. Finite exhaustive orbit certificate.** The supplied standalone `binary16_census.py` constructs both length-15,361 integer transition arrays. Its first census follows every as-yet-unclassified vertex until it reaches a previously classified vertex or repeats a vertex of its current path. In the latter case the repeated suffix is exactly one directed cycle. Reverse traversal labels all preceding vertices by their eventual cycle and their distance from it. This terminates because no vertex can be visited more than once as unclassified. A *second, structurally independent* census repeatedly removes indegree-zero vertices and enumerates the cycles remaining in the directed functional graph; reversing the peel order independently reconstructs each attraction basin and each transient distance. Both traversals cover all 15,361 vertices and agree exactly on all period/basin pairs, maxima, and total transient distances.

The staged orbit with least code \(7678\) has period \(40\); the one-round orbit with least code \(11709\) has period \(5\), with ordered cycle codes
\[
11709,\ 13625,\ 15113,\ 14026,\ 15313.
\]
The 40-cycle is fully printed by the checker. The exact ordered two-byte little-endian SHA-256 digests of the two complete transition arrays are respectively
`300ed95c25d2fe4a9b836b60802d0c6b8af3c9c1c01e0654f895781ea889027c`
and
`262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af`.
The full census outputs the counts stated in the theorem and confirms that the only recurrent codes shared between the two graphs are \(0\) and \(14848\), representing \(0\) and \(3/4\).

**4. Cesàro limit and sharp separation.** Each finite-state orbit is eventually periodic; its time-averaged point masses converge to the uniform distribution on its eventual cycle. Summing over all \(15,361\) equally weighted starting encodings gives an invariant mixture, with mass \(b/15361\) evenly distributed over each cycle having basin size \(b\). For any finite probability measures \(\alpha,\beta\),
\[
\|\alpha-\beta\|_{\mathrm{TV}}=1-\sum_{z\in S}\min(\alpha\{z\},\beta\{z\}).
\]
Only the two shared fixed-point atoms contribute to this overlap. Their lesser respective weights are \(5092/15361\) and \(2/15361\). Therefore the overlap is \(5094/15361\), giving the claimed exact distance \(1-5094/15361=10267/15361\). This last deduction is analytical; the prior finite orbit census is exhaustive, not a simulation of selected seeds.

## Verification

Run `python3 binary16_census.py` to execute the wholly integer-arithmetic state graph construction, both exact enumerations, the exact cycle and basin assertions, and the total-variation calculation. Run `python3 binary16_census.py --crosscheck` with NumPy available for an additional separately implemented binary16 staged calculation on **all 15,361** encodings and independent `fractions.Fraction` nearest-neighbor verification of all single-rounding transitions. The default proof-certificate program needs only the Python standard library; NumPy is optional for the cross-check.

Additional exact census figures: staged total entrance distance \(389795\), single-rounded total entrance distance \(712352\). Both complete transition-array hashes above were computed by the checker. A finite exhaustive certificate is valid for the *specified finite set*; it does not prove infinite-dimensional, all-precision, or real-chaos statements.

## Relationship to prior work

Klöwer, Coveney, Paxton and Palmer studied the loss of chaotic behavior under finite precision, including the logistic map and different low-precision representations. A public preprint of their broader investigation is dated **2022-11-08**; the 2023 journal version adds explicit logistic-map analysis. This supplies the mathematical motivation and is not claimed as new. Galias developed complete finite-precision cycle and basin enumeration for *single and double precision*, establishing the important general methodology. Corless's August 2024 presentation already reports the **40-cycle and its 10,267-point attraction basin** in the ordinary binary16 logistic map. Those facts are explicitly pre-existing: the distinctive claim here is the exhaustive *one-final-rounding comparison* and the exact, nontrivial \(10267/15361\) Cesàro total-variation separation between arithmetic circuits. Searches of relevant literature and mathematical research records did not identify the same quantitative comparison; this absence is not proof of global publication priority.

## Limitations

The claim is a finite, fixed-format result under precisely specified rounding and evaluation order. The one-final-rounding evaluator is idealized and cannot be assumed to coincide with ordinary compiler evaluation, a single fused operation, or stochastic rounding. Exact cycle/basin counts depend on that arithmetic contract and the initial distribution over encodings. Hardware behavior, other formats, parameters other than \(4\), and any comparison to the continuum invariant density are outside scope. General prior literature on equivalent arithmetic-circuit effects or an unindexed exact table may overlap; independent publication-priority review and independent mathematical audit have not been performed.

## References

1. M. Klöwer, P. V. Coveney, E. A. Paxton, and T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, public preprint posted 2022-11-08, DOI: https://doi.org/10.21203/rs.3.rs-2223046/v1; subsequently *Scientific Reports* **13**, 11410 (2023), https://doi.org/10.1038/s41598-023-37004-4.
2. Z. Galias, *Periodic orbits of the logistic map in single and double precision implementations*, *IEEE Transactions on Circuits and Systems II* **68** (2021), 3471–3475, https://doi.org/10.1109/TCSII.2021.3081604.
3. R. M. Corless, *Floats for Philosophers: A Talk in Three Parts*, August 2024, slides 59–61, https://rcorless.github.io/FloatsForPhilosophers.pdf.
