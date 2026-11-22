# Sharp separation threshold for lossless cyclic Rule 90 readout

## Finding

Fix integers \(r\ge1\) and \(n\ge2r+3\). An indexed cyclic binary input is **\(r\)-separated** if each pair of consecutive occupied sites, in cyclic order, is separated by at least \(r\) zeros. Let \(X_{n,r}\) be the set of these inputs and let the one-step observation be the elementary Rule 90 map
\[
  (F_n(x))_i=x_{i-1}\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
For each indexed output \(y\), let \(p_{n,r}(y)=|\{x\in X_{n,r}:F_n(x)=y\}|\). Let \(A_j(n,r)\) count outputs with exactly \(j\) admissible predecessors, for \(j\ge1\), and write
\[
 S_{n,r}=|X_{n,r}|=1+\sum_{k=1}^{\lfloor n/(r+1)\rfloor}\frac nk\binom{n-rk-1}{k-1}.
\]

**Theorem (complete inverse-fiber spectrum).** All nonempty inverse fibers have at most three elements. Their distribution, at every admissible \((n,r)\), is as follows:

1. If \(n\) is odd, or \(r\ge4\), or \(r\in\{2,3\}\) with \(n\equiv2\pmod4\), the observation is injective on \(X_{n,r}\): \(A_1=S_{n,r}\) and \(A_2=A_3=0\).
2. If \(r\in\{2,3\}\) and \(4\mid n\), exactly **two outputs** have two predecessors, namely the two alternating outputs \(0101\ldots\) and \(1010\ldots\). Thus \(A_2=2\), \(A_1=S_{n,r}-4\), \(A_3=0\), and \(|F_n(X_{n,r})|=S_{n,r}-2\).
3. If \(r=1\) and \(n=2m\), then
\[
 \boxed{A_1=S_{n,1}-2^{m+1}+1,\qquad A_2=2^m-2,\qquad A_3=1.}
\]
The unique three-predecessor output is the all-zero word, and the exact number of distinct outputs is \(S_{n,1}-2^m\). In all cases, \(A_j=0\) for every \(j\ge4\).

In particular, **four forbidden distances** (four intervening zeros between cyclic ones) restore one-step injectivity at every permitted ring length. The threshold is sharp: for exclusion distances two and three, loss of injectivity persists at every ring length divisible by four, while at exclusion distance one, exponentially many outputs have multiple admissible predecessors.

## Assumptions and scope

Inputs and outputs have a marked site origin: cyclic rotations are **not** identified. The binary alphabet is \(\{0,1\}\), addition is in \(\mathbb F_2\), and all subscripts are reduced modulo \(n\). The ring length lower bound \(n\ge2r+3\) ensures the cyclic spacing constraint is nondegenerate and includes all claimed sharp witness families. The output need not obey the input separation constraint: the theorem studies one spatial observation from a constrained source, **not** an endomorphism of the hard-core shift. The formula for \(A_j\) counts **distinct indexed output words** rather than distinct pairs of inputs or necklaces.

## Proof

**1. Counting the constrained source.** The zero input contributes one word. If a nonzero input has exactly \(k\) occupied sites, write the \(k\) cyclic forward gaps between successive ones as positive integers \(d_1,\ldots,d_k\), each at least \(r+1\), summing to \(n\). Put \(e_i=d_i-(r+1)\), so the \(e_i\) are nonnegative and sum to \(n-k(r+1)\). There are
\[
 \binom{n-rk-1}{k-1}
\]
ordered gap compositions. Designating one occupied site among \(n\) indexed positions and then forgetting which of the \(k\) occupied sites was designated gives exactly \(\frac nk\binom{n-rk-1}{k-1}\) distinct indexed words. Summing over \(k\) proves the displayed \(S_{n,r}\) formula.

**2. The complete kernel of the observation.** If two inputs \(x,x'\) have the same output, their difference \(d=x\oplus x'\) satisfies \(d_{i-1}=d_{i+1}\) for every \(i\), hence \(d_i=d_{i+2}\). For odd \(n\), the only nonzero solution is the all-one mask \(J\). For even \(n\), the only nonzero solutions are \(E\), \(O\), and \(J=E\oplus O\), where \(E\) and \(O\) are the masks of the even and odd sites. This classification is exhaustive because the step-two rotation has one orbit on odd rings and two orbits on even rings.

**3. The all-site mask.** For both \(x\) and \(x\oplus J\) to contain no adjacent ones, \(x\) may contain neither adjacent `11` (for itself) nor adjacent `00` (for its complement). Thus \(x\) must alternate at every site. Cyclic alternation is possible only for even \(n\); the resulting two alternating inputs are \(1\)-separated, but not \(r\)-separated for any \(r\ge2\). Consequently odd rings are injective, and the \(J\) mask can connect inputs only when \(r=1\) and \(n\) is even.

**4. The one-parity masks.** Suppose \(n=2m\) and both \(x\) and \(x\oplus E\) belong to \(X_{n,r}\). Every odd coordinate of \(x\) must be zero: if an odd site were one, its even neighbors would be forbidden from being one in *both* inputs, whereas those neighbors are flipped by \(E\). Conversely, when \(r=1\), all \(2^m\) choices of the even-coordinate pattern are allowed, and \(E\) pairs these choices into \(2^{m-1}\) unordered collision edges.

For \(r\ge2\), the even-site pattern \(a=(a_0,\ldots,a_{m-1})\) and its complement must each avoid adjacent ones **in the cyclic parity sublattice**, because successive even coordinates are distance two on the original ring. The first condition rules out `11` and the second rules out `00`; therefore \(a\) is alternating. This is possible exactly when \(m\) is even. The two such inputs, supported on one of the two positions in every consecutive four-site block, are \(r\)-separated precisely for \(r\le3\), since their occupied sites are four apart. At \(r=2,3\) and \(4\mid n\), they form one \(E\)-collision pair; at \(r\ge4\) no \(E\)-collision exists. Reversing the roles of the parities gives the identical classification for \(O\): one different pair when \(r\in\{2,3\}\) and \(4\mid n\), or \(2^{m-1}\) edges when \(r=1\).

**5. Assembling fibers without double-counting.** For \(r\ge2\), the \(J\)-mask is unavailable, so a fiber cannot simultaneously have an \(E\)-edge and an \(O\)-edge; their endpoints would differ by \(J\). In the intermediate regime \(r=2,3\) and \(4\mid n\), the two pairs generate respectively the two alternating output patterns, which are different. Thus there are exactly two double fibers and all remaining source words have singleton outputs. The other \(r\ge2\) cases have no collision at all.

For \(r=1\), a fiber involving both an \(E\)-edge and an \(O\)-edge requires an input with all even and all odd bits zero by Step 4, hence includes the all-zero input. Its other two inputs are the two alternating words, and all three map to zero. The fourth linear preimage \(J\) is not allowed. This is the **unique** triple fiber. Of the \(2^{m-1}\) edges of each parity, exactly one is incident to this triple fiber, leaving \(2(2^{m-1}-1)=2^m-2\) disjoint double fibers. All remaining \(S_{n,1}-3-2(2^m-2)=S_{n,1}-2^{m+1}+1\) source words give singleton fibers. Adding fiber counts proves the image size formula, the global multiplicity bound, and the complete theorem. \(\square\)

## Verification

Run `python3 verify.py` in the directory holding this document. The dependency-free checker enumerates **every** one of the \(2^n\) indexed binary inputs for each of 57 allowed parameter pairs \(1\le r\le6\), \(2r+3\le n\le\min(20,2r+13)\), constructs each actual Rule 90 output, and compares the entire fiber-size histogram with the closed formula. It also checks that the exact two double-output witnesses in four selected intermediate cases are the two alternating words. The observed output from the packaged checker begins `VERIFY_OK parameter_pairs=57`.

The all-parameter theorem is proved by the complete kernel and exclusion analysis above. Finite tests corroborate but do not replace the infinite proof; the checker makes no unverified statement about larger sizes.

## Relationship to prior work

Salo (2022, arXiv:2209.13373, published 2023) studies cellular-automaton regularity, periodic preimages and finite-type images, including a restriction involving the golden-mean shift for Rule 28. This motivates distinguishing full-shift preimages from constrained-source preimages, but it does not give the present Rule 90 separation-dependent fiber spectrum. General finite-ring Rule 90 theory already gives a one-dimensional kernel for odd rings and a two-dimensional kernel for even rings; **that kernel calculation is not claimed as new**.

The published result *The four-valued predecessor law for cyclic Rule 90 necklaces* studies **unconstrained** inputs and counts predecessor classes after quotienting by spatial rotation, unlike these exact constrained, indexed fibers. *Radius-two rigidity across binary hard-core shifts, with sharp forbidden-block horizons* classifies maps preserving each constrained shift, whereas Rule 90 here maps into the full binary output space and generally does **not** preserve the input restriction. *Exact rank deficits and optimal static sensors for cyclic Rule 90* uses time-series samples from fixed sites and an unrestricted input space, not the single-spatial-snapshot problem posed here. None of these statements directly implies the sharp spacing threshold or the three-regime fiber census without further exclusion analysis.

## Limitations

The input separation and lower length bound are essential as stated; no claim is made for smaller rings, noisy readouts, other local rules, other alphabets or repeated updates. The injectivity theorem concerns exact noiseless one-step identification and is not an error-correction-distance guarantee. The underlying unconstrained linear kernel is classical and general finite-state predecessor tests are known; originality is confined to the sharp constrained-source phase classification and its exact multiplicities. Historical priority, including possibly equivalent formulations in constrained coding or cellular-automaton literature, has not been independently certified. No independent mathematical audit has been performed.

## References

1. V. Salo, *On von Neumann regularity of cellular automata*, first public version 2022-09-27, arXiv:2209.13373. Open-access article: https://doi.org/10.1007/s11047-022-09935-w
2. *The four-valued predecessor law for cyclic Rule 90 necklaces*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-four-valued-predecessor-law-for-cyclic-rule-90-necklaces--1b4786197dbc
3. *Radius-two rigidity across binary hard-core shifts, with sharp forbidden-block horizons*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-radius-two-rigidity-across-binary-hard-core-shifts-with-sharp-fo--824122558fbf
4. *Exact rank deficits and optimal static sensors for cyclic Rule 90*, public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-exact-rank-deficits-and-optimal-static-sensors-for-cyclic-rule-9--162c468ed707
