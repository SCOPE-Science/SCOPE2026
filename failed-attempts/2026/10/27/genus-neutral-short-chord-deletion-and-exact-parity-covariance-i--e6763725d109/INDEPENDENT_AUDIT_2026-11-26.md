# Independent mathematical audit

## correctness

PASS

In the face permutation gamma*pi, an adjacent pair a,b with gamma(a)=b gives the singleton cycle b. With a nonempty residual diagram, deletion removes that singleton and splices a out of its other cycle; thus Euler's formula leaves genus unchanged. At the final one-to-zero step, use the disk with one boundary component and genus zero, not the cycle count of the empty permutation. Marking one edge in a size-k matching of the 2n-cycle gives k A_{n,k}=2n*binom(2n-k-1,k-1) for k>=1, including k=n; each chosen collection has a uniform residual matching. Ordered marking and factorial simplification give the claimed coefficient, and binomial expansion gives the PGF. Differentiating the exact Harer–Zagier normalization in Chmutov–Pittel gives the odd-harmonic face mean and the two asserted genus-mean increments; multiplication by -2n/(2n-1) gives the covariance, tending to -1/2. For fixed k the normalization at n-k and at n differs by an asymptotically negligible change of center and scale. The uniform bound 2^k justifies exchanging the factorial series and the limit, and tightness follows from the bounded first short-chord moment and the genus marginal CLT. Every subsequential limit is identified by the mixed PGF and bounded continuous genus-scale tests. The frozen check.py was inspected, not executed; its reported exact enumeration is finite evidence only.

## originality

FAIL

Alexeev–Andersen–Penner–Zograf already enumerate a strictly finer statistic on the same marked polygon gluings: the entire vertex-degree spectrum at fixed genus and order. Their Remark 1, equations (7)–(8), directly gives every entry of the frozen joint law after degree specialization. The specific Harer–Zagier reduction is not printed there, but it uses the already explicit cyclic factorial-transfer count and the genus-neutral leaf case of known chord erasure. The parity and limiting formulas are not identified as verbatim earlier statements; they follow by the same transfer template with the known genus mean and genus CLT. The decision is established coverage of the finite law and a direct derivation of the displayed refinement and consequences, not evidence of copying or precise first publication of the simplified formulas.

## value

FAIL

Genus and monogons are natural observables, and the compact expression is convenient. But the exact law is already available as a projection of the full degree spectrum, and its simpler computation uses the established factorial transfer with the standard monogon erasure case. The parity formula and mixed limit are direct extractions from that reduction and the established univariate laws, not a distinct structural extension beyond these inputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
