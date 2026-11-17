# Exact shortest periods and extremal orbit counts in the first ten Kolakoski finite-depth shifts

## Finding

For each integer \(k\geq1\), let \(X_k\) be the bi-infinite binary sequences over \(\{1,2\}\) on which run-length differentiation can be performed \(k\) consecutive times (each differentiated sequence having only runs of length one or two). Give \(X_k\) the left shift, and let \(p_k\) be the shortest least period of its periodic points. The first ten shortest periods are, exactly,

\[
(p_1,\ldots,p_{10})=(2,3,8,12,18,27,80,120,180,269).
\]

The numbers of distinct shift-orbits having exactly the corresponding shortest periods are

\[
(1,2,1,2,4,8,4,8,16,16).
\]

In particular, \(X_{10}\) has no periodic point of least period below \(269\), and exactly \(16\) distinct shift-orbits of least period \(269\). These are counts of *oriented* binary necklaces: complement and reversal are not used to identify orbits. The verified finite computation also supplies the general lower bound \(p_k\geq 2(4/3)^{k-1}\) for every \(k\geq1\).

## Assumptions and scope

For a nonconstant bi-infinite periodic sequence \(x\), its run-length derivative \(D(x)\) lists the successive maximal constant-run lengths, viewed modulo shift. The derivative is defined in the alphabet \(\{1,2\}\) only when no run exceeds two. Write \(X_1\) for the sequences admitting a first binary derivative and define \(X_{k+1}=\{x\in X_1:D(x)\in X_k\}\). A periodic point has *least period* \(n\) if \(n\) is the minimum positive shift fixing the sequence. Each primitive cyclic word of length \(n\) represents one such shift-orbit. Constant binary sequences are outside \(X_1\), since their infinite constant runs do not have finite run lengths. The \(k\)-fold derivative is a sequence of runs, and its origin may shift when the original origin is shifted; membership and periodic orbit questions are unaffected.

These are finite-depth two-sided periodic approximants, **not** periodic trajectories in the full infinitely smooth Kolakoski subshift. No assertion is made about period counts beyond the shortest-period sector at each depth.

## Proof

**1. Primitive circular inverse differentiation.** Let \(v\) be a primitive circular word of length \(m\) over \(\{1,2\}\). To construct a periodic binary sequence whose run-length derivative is the periodic sequence \(v^\infty\), interpret the symbols of \(v\) as consecutive run lengths and alternate the run symbol \(1,2,1,2,\ldots\). If \(m\) is even, the lengths \(v\) close the alternation. If \(m\) is odd, repeat \(v\) twice to close it. These yield a primitive circular expansion \(E(v)\) and its bitwise complement, up to rotation. Every primitive periodic preimage arises in this way. Indeed, periodic alternation requires an even number of runs, and the primitive period of the run-length sequence contains exactly \(m\) runs; the least even multiple of \(m\) is \(m\) or \(2m\) as prescribed. Any larger even multiple repeats the shorter expansion and is not primitive. Thus the least period of the inverse is

\[
|E(v)|=\begin{cases}\sum_{i=1}^{m}v_i,&m\text{ even},\\2\sum_{i=1}^{m}v_i,&m\text{ odd}.\end{cases}
\]

This construction respects rotations but **not complementation of the run-length word**: complementing \(v\) changes run lengths. Consequently, every stage of the enumeration retains both bitwise orientations of the inverse expansion as separate oriented rotation classes when they differ.

**2. A uniform period expansion bound.** Every primitive word \(v\) representing a periodic point of \(X_1\) avoids the cyclic triples \(111\) and \(222\). In particular, each cyclic three-position window contains a \(2\); counting windows proves that the number of \(2\)'s in \(v\) is at least \(m/3\). Thus \(\sum v_i=m+|v|_2\geq4m/3\). Inverting the derivative therefore multiplies the least period by at least \(4/3\), including the parity-doubling case. All derivatives of an \(X_k\) periodic sequence are in \(X_1\), so iterative inversion proves \(p_k\ge2(4/3)^{k-1}\).

**3. Exhaustive finite cutoff.** If a primitive periodic point in \(X_{10}\) has least period at most \(269\), the ninefold derivative has a primitive period

\[
m\leq269(3/4)^9<21.
\]

Hence all such periodic points arise from primitive circular words of lengths \(2\) through \(20\) in \(X_1\). Those base words are exactly the binary primitive necklaces with no cyclic triple of equal symbols; every such necklace can be found by enumerating the words whose first symbol is \(1\), testing every proper divisor for a shorter period, and canonicalizing under rotation. This produces \(2170\) oriented base necklaces.

At each of the next nine levels, apply the exact primitive inverse-run rule to every retained necklace, include its complementary output as a distinct candidate when appropriate, canonicalize only under cyclic rotations, and discard any length exceeding \(269\). Lengths increase strictly under each inversion, so no discarded branch can return below the cutoff. The numbers of retained oriented necklaces at levels \(1,\ldots,10\) are

\[
2170,3474,5632,9073,11218,5590,2666,300,32,16.
\]

The computed least lengths at these levels and their multiplicities are precisely the two arrays in the Finding. The last level consists of \(16\) primitive necklaces, all of length \(269\), proving both absence below the cutoff and the exact orbit count at the cutoff. For the lower levels, if an unenumerated shorter orbit existed, its starting level-one derivative would have length at most \(p_k(3/4)^{k-1}\leq20.20<21\), contradicting the exhaustive base enumeration and its retained inverse branches. Thus the complete first-ten minimum and multiplicity arrays are also exact.

The computer-assisted enumeration is a finite exhaustive proof, not an extrapolation from a numerical sample. Its small exact-integer standalone implementation is provided in `verify_periodic_systole.py`.

## Verification

Run `python3 verify_periodic_systole.py` without additional dependencies. It checks the base-seed bound, enumerates the complete \(2170\)-necklace base sector, retains both inverse orientations, confirms all stage counts and least periods, verifies primitivity, and directly differentiates all \(16\) extremal length-\(269\) necklaces through ten admissible levels. Separately, direct brute-force enumeration over binary periodic words validates the first five least periods without using the inverse-run enumeration. The expected output begins `CERTIFICATE_OK` and ends with an explicit length-\(269\) witness.

## Relationship to prior work

Mitchell, Walton, and Whittaker [1] prove topological transitivity of the full infinitely smooth Kolakoski shift and define the same run-length differentiation hierarchy; they do not compute these periodic minimum periods or their extremal multiplicities. Cassaigne and Henry [2] study smooth-word factor complexity and prove that smooth sequences are not eventually periodic, which motivates following periodic points as the differentiability depth increases. Fédou and Fici [3] construct finite-level automata for *finite differentiable words*, rather than giving the stated two-sided primitive-period census. The present finite-depth result is compatible with all three works. No assertion of general bibliographic uniqueness is made.

## Limitations

The table stops at differentiability depth ten; nothing is inferred about the exact shortest periods at greater depths from the finite census alone. The growth bound \(2(4/3)^{k-1}\) is general but need not be sharp. The \(16\) extremal orbits are distinct modulo shift, not modulo complement or reversal. The cutoff certificate is exhaustive because of the independently proved inverse-growth bound; finite brute-force checks by themselves would not prove the infinite statement for every depth. Publication-priority comparisons in the wider finite-word and dynamical literature may be incomplete.

## References

[1] A. C. Mitchell, J. J. Walton, M. F. Whittaker, *The full Kolakoski shift is topologically transitive*, arXiv:2611.06878v1, first posted 2026-11-04, https://arxiv.org/html/2611.06878v1.

[2] J. Cassaigne, R. Henry, *The complexity of finite smooth words over binary alphabets*, arXiv:2603.10733v1, first posted 2026-03-11, https://arxiv.org/html/2603.10733v1.

[3] J.-M. Fédou, G. Fici, *Automata and Differentiable Words*, arXiv:1102.0913v3 (2012), https://arxiv.org/pdf/1102.0913.
