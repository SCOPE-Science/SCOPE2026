# Sharp separation threshold for lossless cyclic Rule 90 readout

## Finding

Let \(r\ge2\) and \(n\ge2r+3\) be integers. An indexed cyclic binary input is \(r\)-separated if there are at least \(r\) zeros between consecutive occupied sites in cyclic order. Let \(X_{n,r}\) be the set of such inputs, including the zero word. The one-step Rule 90 readout is
\[
(F_n(x))_i=x_{i-1}\oplus x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z.
\]
Write \(A_j(n,r)\) for the number of indexed outputs with exactly \(j\) predecessors in \(X_{n,r}\), for \(j\ge1\). The source cardinality is
\[
S_{n,r}=1+\sum_{k=1}^{\lfloor n/(r+1)\rfloor}\frac nk\binom{n-rk-1}{k-1}.
\]

**Theorem.** If \(n\) is odd, or \(r\ge4\), or \(r\in\{2,3\}\) with \(n\equiv2\pmod 4\), then \(F_n\) is injective on \(X_{n,r}\): \(A_1=S_{n,r}\) and all other \(A_j=0\). If \(r\in\{2,3\}\) and \(4\mid n\), exactly two outputs have two admissible predecessors: the alternating words \(0101\ldots\) and \(1010\ldots\). Then \(A_1=S_{n,r}-4\), \(A_2=2\), \(A_j=0\) for \(j\ge3\), and \(|F_n(X_{n,r})|=S_{n,r}-2\).

Thus four intervening zeros are necessary and sufficient for injectivity at every permitted ring length: the cases \(r=2,3\) fail at every permitted multiple of four, and the same collision witnesses are allowed under the weaker \(r=1\) constraint. The \(r=1\) fiber census is already given by the Lucas-constrained Rule 90 result [1]; it is not part of the new claim here.

## Assumptions and scope

Rotations are not identified: both the input and the output have a marked origin. The alphabet is \(\mathbb F_2\), indices are cyclic, and only the input is required to be separated. A word with zero or one occupied site is allowed. The observation is one synchronous step, not time-series sampling and not an endomorphism of the constrained shift. The theorem only concerns the stated lengths and separation parameters.

## Proof

**Source count.** For \(k\ge1\) occupied sites, mark one occupied site and measure the \(k\) successive forward spacings, each at least \(r+1\). The spacings minus \(r+1\) are an ordered weak composition of \(n-k(r+1)\) into \(k\) parts, giving \(\binom{n-rk-1}{k-1}\) possibilities. Choosing the position of the mark in \(n\) ways and dividing by the \(k\) possible marks per word, then adding the zero word, proves the count.

**Collisions.** If \(F_n(x)=F_n(x')\), the difference \(d=x\oplus x'\) satisfies \(d_i=d_{i+2}\). The only possible nonzero mask on an odd ring is the all-one mask \(J\). On an even ring the nonzero masks are \(J\), the even mask \(E\) and the odd mask \(O\). If both a word and its complement avoid adjacent ones, the word must alternate, because neither `11` nor `00` may occur. This excludes \(J\) on odd rings and also on even rings for \(r\ge2\).

Suppose \(n=2m\) and a collision differs by \(E\). Any occupied odd site would force its even neighbors to vanish in both inputs, impossible because those neighbors are flipped. The odd sublattice is thus zero. On the even sublattice the original pattern and its complement must both have no adjacent ones there, since occupied neighboring even sites would be distance two in the original ring. Hence that sublattice alternates, requiring \(m\) even, and its occupied sites are four apart. Both complementary patterns are allowed exactly for \(r=2,3\). They give one collision pair, and the same argument with \(O\) gives one other pair. An input with support equal to a single residue class modulo four produces ones at precisely the sites of opposite parity: each of those sites has one occupied neighbor. Thus the two pairs produce distinct alternating outputs. There are no further collision masks or pairs, proving the stated census.

## Verification

The kernel and exclusion arguments are exact for all stated lengths. The accompanying dependency-free `verify.py` is unchanged: its finite census exhausts all binary inputs for 57 parameter pairs, including the separately established \(r=1\) case [1] and the claimed \(r\ge2\) cases. It also checks both alternating-output witnesses in four selected cases with \(4\mid n\) and \(r\in\{2,3\}\). These finite checks corroborate the formulas but are not used to infer the general theorem.

## Relationship to prior work

The Lucas-constrained record [1] treats indexed cyclic words with no adjacent ones, equivalent to \(r=1\). Its one-step result already gives odd-cycle injectivity and, for \(n=2m\), one triple fiber at zero, \(2^m-2\) double fibers, and \(S_{n,1}-2^{m+1}+1\) singleton fibers. Its time-iterated results concern a different question. The new spacing analysis above begins with \(r=2\), where the complementary patterns must themselves alternate on a sublattice and the sharp threshold and two alternating-output exceptions follow. No ordering between the two same-date records is inferred.

Salo [2] studies von Neumann regularity and, in Proposition 20, Rule 28 on the golden-mean shift, not this indexed constrained-source census. The unconstrained cyclic predecessor counts are classical and the necklace result [3] counts rotation classes rather than indexed outputs. The hard-core preservation classification [4] concerns rules mapping the constrained set into itself, whereas Rule 90 here maps into the unrestricted binary space. The temporal sensor result [5] addresses multiple time observations rather than one spatial snapshot.

## Limitations

This is a noiseless one-step injectivity and multiplicity result, not a bound on error-correction distance or a claim for other rules, lengths or iterated readouts. The unconstrained linear kernel and the \(r=1\) census are not claimed as new. Historical priority outside the comparisons given is not asserted.

## References

1. *Parity-stable inversion of cyclic Rule 90 on Lucas-constrained inputs*, https://github.com/Resultary/2026/blob/main/2026/11/22/SCOPE-parity-stable-inversion-of-cyclic-rule-90-on-lucas-constrained-i--a49ca7533403/RESULT.md
2. V. Salo, *On von Neumann regularity of cellular automata*, https://doi.org/10.1007/s11047-022-09935-w
3. *The four-valued predecessor law for cyclic Rule 90 necklaces*, https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-the-four-valued-predecessor-law-for-cyclic-rule-90-necklaces--1b4786197dbc
4. *Radius-two rigidity across binary hard-core shifts, with sharp forbidden-block horizons*, https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-radius-two-rigidity-across-binary-hard-core-shifts-with-sharp-fo--824122558fbf
5. *Exact rank deficits and optimal static sensors for cyclic Rule 90*, https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-rank-deficits-and-optimal-static-sensors-for-cyclic-rule-9--162c468ed707
