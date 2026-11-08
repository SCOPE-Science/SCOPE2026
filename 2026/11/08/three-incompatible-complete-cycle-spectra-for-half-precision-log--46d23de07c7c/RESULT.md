# Three incompatible complete cycle spectra for half-precision logistic dynamics

## Finding
Let \(S\) be the set of all nonnegative IEEE-754 binary16 numbers in \([0,1]\), with zero represented only by its positive encoding, and let \(R\) denote correctly rounded binary16 arithmetic (nearest, ties to even). The set has exactly \(|S|=15,361\) elements. Three evaluations of the real logistic polynomial \(L(x)=4x(1-x)\) define distinct deterministic maps \(S\to S\):

\[
 F(x)=R\!\left(R(4x)\,R(1-x)\right),\qquad
 G(x)=R\!\left(R(4x)-R(4R(x^2))\right),\qquad
 H(x)=R\!\left(4x(1-x)\right).
\]

Here \(F\) and \(G\) round after each displayed basic operation, and \(H\) evaluates the polynomial exactly before a single final rounding; the last is a correctly rounded reference, not a sequence of half-precision arithmetic instructions. These three finite systems have the **complete primitive orbit and basin census** below. A row represents one entire primitive cycle, specified by its least period, number of starting encodings eventually entering it, and least numerical bit encoding of a cycle point. A basin includes its own cycle.

| Evaluation | Least period | Basin cardinality | Minimal cycle encoding |
| --- | ---: | ---: | --- |
| \(F\) | 1 | 5092 | `0x0000` |
| \(F\) | 1 | 2 | `0x3a00` |
| \(F\) | 40 | 10267 | `0x1dfe` |
| \(G\) | 1 | 6671 | `0x0000` |
| \(G\) | 1 | 33 | `0x3a00` |
| \(G\) | 4 | 91 | `0x3470` |
| \(G\) | 17 | 881 | `0x2480` |
| \(G\) | 25 | 3648 | `0x2000` |
| \(G\) | 30 | 4037 | `0x2400` |
| \(H\) | 1 | 15236 | `0x0000` |
| \(H\) | 1 | 8 | `0x3a00` |
| \(H\) | 5 | 117 | `0x2dbd` |

There are no other cycles. The maximum number of iterations before the first periodic state is respectively \(83\), \(59\), and \(109\) for \(F\), \(G\), and \(H\). The sums of these first-entry times over all \(15,361\) initial states are respectively \(389,795\), \(242,447\), and \(712,352\).

Thus the fraction of uniformly counted representable starting values captured by a nonfixed cycle changes from \(10,267/15,361\) to \(8,657/15,361\) to \(117/15,361\), even though the corresponding exact real polynomials agree.

## Assumptions and scope
All values are interpreted as nonnegative binary16 numbers, including the \(1,023\) positive subnormals and zero, in the closed unit interval. All operations use round-to-nearest, ties-to-even, with no fused operations, extended internal precision, reassociation, fast-math optimization, or stochastic rounding. The two algebraic evaluation graphs are part of the definitions, rather than claimed to be every possible implementation of a compiler expression. Both fixed-point basins include the corresponding fixed states \(0\) and \(3/4\). The reference evaluation \(H\) computes the exact rational expression \(4x(1-x)\) before rounding once.

The probabilities quoted from the census use **uniform counting measure on the representable binary16 states**, and should not be mistaken for Lebesgue measure or for a uniform real initial condition rounded to binary16. Completeness refers to these three explicitly defined maps at parameter \(4\), not other binary formats, rounding modes, or parameters.

## Proof
Every positive binary16 encoding in \([0,1]\) has a unique unsigned integer code \(j\) between `0x0000` and `0x3c00`. Write \(e=\lfloor j/2^{10}\rfloor\) and \(f=j\bmod2^{10}\), and set \(U(j)=2^{24}x_j\). The integer conversion is exactly
\[
U(j)=\begin{cases}f,&e=0,\\(2^{10}+f)2^{e-1},&e\geq1.\end{cases}
\]
Thus all state coordinates are integers on the uniform rational scale \(2^{-24}\). For intermediate operations through the value \(4\), enumerate all codes from `0x0000` through `0x4400`. Their scaled integer values form a strictly increasing list. To round a nonnegative rational \(q=n/(d2^{24})\), find its two neighboring values in this integer list by exact cross multiplication, choose the closer, and for an exact midpoint choose the even final significand bit, equivalently the code with even low bit. This reproduces the IEEE rounding rule including subnormals and exponent transitions.

Apply this exact rule to the arithmetic graphs. The resulting codes are computed without floating-point operations by the `nextbit` function of `verify.py`. Specifically, for \(u=U(j)\), \(a=R_*(4u)\), \(b=R_*(2^{24}-u)\), and \(v=R_*(u^2/2^{24})\), where \(R_*\) outputs an encoding from a rational expressed in scaled units, the new encodings are
\[
 F(j)=R_*\!\left(U(a)U(b)/2^{24}\right),\quad
 G(j)=R_*\!\left(U(a)-U(R_*(4U(v)))\right),\quad
 H(j)=R_*\!\left(4u(2^{24}-u)/2^{24}\right).
\]
Every returned encoding lies between `0x0000` and `0x3c00`, as checked on all \(15,361\) possible inputs. The source file explicitly implements \(R_*\) by integer comparisons; there is no dependence on host floating-point rounding.

For each of the three maps, construct its complete directed functional graph. Starting at every as-yet unclassified code, traverse successor codes until a previously classified code or a code already on the current path is reached. In the latter case, the repeated suffix is a new entire primitive cycle. Assign its cycle ID and distance zero, then propagate cycle ID and first-entry distance backward along the traversed path. If the path reaches a previously classified code, propagate the known ID and distance similarly. Every code is assigned exactly once, and every traversal ends in at most \(15,362\) steps, because the finite state space has \(15,361\) elements. Therefore the procedure exhaustively finds all cycles and all basin counts, with no sampling or extrapolation. It also computes each maximum and total first-entry time. The algorithm is fully specified by the included standalone `verify.py`, whose outputs are checked against every row of the table and whose edge-array hashes are specified in the Verification section. Direct independent evaluation using NumPy half-precision operations agreed with each of the \(46,083\) computed successor encodings (\(15,361\) for each map); this separate cross-check does not enter the proof.

## Verification
Run `python3 verify.py` using the Python standard library. It builds each entire edge array from integer arithmetic, extracts every cycle and basin, checks the complete tables, first-entry statistics, and the full byte-level SHA-256 hashes of the edge arrays (encoded in little-endian unsigned 16-bit code order). A successful run ends with `EXACT_GRAPH_CHECK_OK`.

The three complete edge-array SHA-256 values, in the order \(F,G,H\), are:

- `300ed95c25d2fe4a9b836b60802d0c6b8af3c9c1c01e0654f895781ea889027c`
- `7dac595f8435d93aa3bea32a701ef4c9d19d30f0079195a63f5db7ca0353729c`
- `262e0316d1e5e82c3b1c694ecde3dde9b8c6a8a24956d407f6b6b008c2d116af`

The finite-state calculation is an exhaustive proof **for these finite maps only**. It is not a proof about the infinite-precision logistic system or about every floating-point compiler and architecture.

## Relationship to prior work
Klöwer, Coveney, Paxton and Palmer (2023) examine low-precision cycles of the logistic map and explicitly describe Monte Carlo orbit searches; they do not provide the complete three-graph, all-state census here. Corless (2024), slide 60, explicitly reports the forty-cycle and its \(10,267\)-point basin for a half-precision logistic implementation; **that observation is prior work**, not claimed as new here. The contribution is the complete and comparable census for the explicitly staged expanded graph and the single-round reference, alongside precise definitions and exhaustive integer verification of the differences. Krulikovskyi et al. (2024) investigate sensitivity to arithmetic ordering, using double precision and sampled trajectories rather than this binary16 three-evaluation complete classification.

## Limitations
The integer program is a finite certificate whose completeness depends on the readable rounding routine and graph traversal; independent formal verification is not supplied. The published factored forty-cycle is credited. The binary16 starting-state counting law is not the invariant distribution under randomly sampled real initial points. Different rounding modes, fused arithmetic, hidden extended precision and reordered operations may produce different graphs. Unindexed equivalent calculations may exist, and independent scientific validation has not been performed.

## References
1. M. Klöwer, P. V. Coveney, E. A. Paxton, T. N. Palmer, *Periodic orbits in chaotic systems simulated at low precision*, Scientific Reports 13 (2023), 11410, published 2023-07-14. DOI: 10.1038/s41598-023-37004-4.
2. R. M. Corless, *Floats for Philosophers: A talk in three parts*, August 2024, especially slide 60. https://rcorless.github.io/FloatsForPhilosophers.pdf
3. O. Krulikovskyi, S. Haliuk, V. Ivashko, R. Politanskyi, *Periodicity of Timeseries Generated by Logistic Map: Part II*, SISIOT 2(2) (2024), 02003. DOI: 10.31861/sisiot2024.2.02003.
