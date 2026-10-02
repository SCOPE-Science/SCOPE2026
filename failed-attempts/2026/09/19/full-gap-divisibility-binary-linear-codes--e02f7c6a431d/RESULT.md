# Full initial weight gaps force divisibility in binary linear codes

## Statement

Let \(C\) be a binary linear \([n,k,d]\) code, with weight distribution
\((A_0,\ldots,A_n)\), and put
\[
M=n-k+1.
\]
Assume that the complete initial interval above the minimum distance is empty:
\[
A_{d+1}=A_{d+2}=\cdots=A_M=0.
\tag{1}
\]
(When \(M=d\), the condition is vacuous.) Then every codeword of \(C\) is a
sum of pairwise support-disjoint minimum-weight codewords. In particular,
\[
\operatorname{wt}(c)\in d\mathbb Z
\qquad(c\in C),
\tag{2}
\]
so \(C\) is \(d\)-divisible.

More generally, the same conclusion holds for any binary linear code in which
all minimal codewords have one common weight \(d\).

The minimum supports consequently satisfy
\[
|\operatorname{supp}(x)\cap\operatorname{supp}(y)|\in\{0,d/2\}
\tag{3}
\]
for any two distinct minimum-weight codewords \(x,y\), with the second option
possible only when \(d\) is even.

For odd \(d>1\), (1) is rigid: either \(k=1\), or
\[
(n,k,d)=(2d,2,d)
\tag{4}
\]
and, after a coordinate permutation, \(C\) is the direct sum of two length-\(d\)
binary repetition codes. Therefore every binary \([n,k,d]\) code with odd
\(d>1\) and \(k\ge3\) has at least one codeword of a weight
\[
d<w\le n-k+1.
\tag{5}
\]

## Proof

Ashikhmin and Barg proved three facts about minimal vectors that are decisive
here: a minimal support in an \([n,k]\) code has size at most \(n-k+1\); the
minimal vectors span the code; and, in a binary code, every nonminimal codeword
\(c\) can be written
\[
c=c_1+c_2
\]
where \(c_1,c_2\ne0\) have disjoint supports properly contained in the support
of \(c\) [1, Lemma 2.1(2),(4),(5)].

Under (1), every minimal codeword has weight between \(d\) and \(M\), hence has
weight exactly \(d\). Now induct on the weight of a nonzero codeword \(c\). If
\(c\) is minimal, it is already a minimum-weight word. Otherwise use the binary
disjoint-support decomposition above. Both \(c_1\) and \(c_2\) have smaller
positive weight. Applying the induction hypothesis to each gives decompositions
into minimum-weight words. Because the supports of \(c_1\) and \(c_2\) are
disjoint, all terminal minimum-weight words are pairwise disjoint. This proves
the decomposition claim and (2).

The same induction proves the more general statement whenever all minimal
codewords have common weight \(d\), without reference to (1).

Let \(x\ne y\) be minimum-weight words and set
\(s=|\operatorname{supp}(x)\cap\operatorname{supp}(y)|\). The word \(x+y\) is
nonzero and, by (2), has weight divisible by \(d\). But
\[
\operatorname{wt}(x+y)=2d-2s,
\]
which lies in \([d,2d]\). Hence it is either \(d\) or \(2d\), giving (3).
If \(d\) is odd, \(2d-2s\) is even and cannot equal \(d\); thus all distinct
minimum supports are disjoint.

Assume now that \(d>1\) is odd. The minimum words span \(C\), and pairwise
disjoint nonzero binary vectors are linearly independent. Thus there are exactly
\(k\) minimum words, and, up to coordinate permutation,
\[
C\cong \operatorname{Rep}_2(d)^{\oplus k}\oplus 0^z,
\qquad n=kd+z,
\tag{6}
\]
where the last term denotes \(z\) identically-zero coordinates. If \(k\ge2\),
the code contains a word of weight \(2d\). Condition (1) therefore requires
\[
2d>n-k+1=kd+z-k+1.
\tag{7}
\]
For \(k=2\), (7) forces \(z=0\), giving (4). For \(k\ge3\), its right-hand side
minus \(2d\) equals
\[
(k-2)d+z-k+1\ge d-2>0,
\]
a contradiction. This proves the odd-distance classification and (5).

## Relation to recent work

He [2] proved a local mirror-vanishing theorem: if
\(A_{d+1}=\cdots=A_{d+t}=0\) and \(k\ge n-2d+1\), then the reflected band
\(A_{2d+1},\ldots,A_{2d+t}\) also vanishes. The result above concerns a stronger
but natural endpoint condition: the initial gap reaches the universal
Ashikhmin--Barg ceiling \(n-k+1\) for minimal supports. At that endpoint, the
binary disjoint-decomposition property closes recursively and yields a global
arithmetic conclusion on every weight, rather than one additional vanishing
band. For odd minimum distance it also makes such a full gap impossible in
dimension at least three.

No novelty is claimed for the Ashikhmin--Barg minimal-vector properties
or for the recent mirror-band theorem. The contribution here is the global
closure/divisibility consequence of the full initial gap and its odd-distance
rigidity corollary.

## Verification

`artifacts/verify_small_codes.py` exhaustively enumerates all binary linear
subspaces of length at most 6 and dimension at most 3. For every code satisfying
(1), it checks divisibility of every nonzero weight by \(d\); for odd \(d>1\) it
also checks the dimension-two classification. The recorded output is in
`artifacts/verification.txt`.

The finite check is only a sanity check; the general statements are proved
above.

## Limitations

The full-gap hypothesis (1) is substantially stronger than the short initial
band in [2], so this result does not replace or sharpen the hypotheses of He's
mirror theorem. The recursive disjoint-support step is specific to binary codes.
For even \(d\), (3) allows half-size intersections, and no complete
classification is claimed here. Originality is only to the best of our
knowledge; because [2] is extremely recent and the new argument is short once
combined with the classical minimal-vector lemma, near-simultaneous or folklore
coverage remains a material risk.

## References

1. A. Ashikhmin and A. Barg, “Minimal Vectors in Linear Codes,” *IEEE
   Transactions on Information Theory* 44(5), 2010–2017 (1998),
   DOI: 10.1109/18.705584. Public author copy:
   https://user.eng.umd.edu/~abarg/reprints/MinimalVectors98.pdf
2. X. He, “A Mirror Vanishing Band for Weight Distributions of Binary Linear
   Codes,” arXiv:2609.20344v1 (2026), https://arxiv.org/abs/2609.20344
3. V. Chubenko and S. Kurz, “Divisible Minimal Codes,” *Serdica Journal of
   Computing* 18(2), 97–124 (2025), arXiv:2312.00885. This is background on
   divisible minimal codes; it is not used in the proof.
