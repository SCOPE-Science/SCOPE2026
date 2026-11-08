# The complete dyadic value image of derangement numbers

## Finding

Let \(D_n\) count fixed-point-free permutations of an \(n\)-element set, so \(D_0=1\) and \(D_n=nD_{n-1}+(-1)^n\) for every \(n\ge1\). For every integer \(k\ge3\), the set of residues \(D_n\bmod 2^k\) as \(n\) ranges over all nonnegative integers is exactly

\[
\{a\bmod 2^k:2\mid a\}\;\sqcup\;\{a\bmod 2^k:a\equiv1\pmod8\}.
\]

Its size is \(5\cdot2^{k-3}\), and every allowed class occurs for infinitely many indices. For \(k=1\) and \(k=2\), the images are respectively \(\{0,1\}\) and \(\{0,1,2\}\). Equivalently, in the ring of \(2\)-adic integers,

\[
\overline{\{D_n:n\ge0\}}=2\mathbb Z_2\;\sqcup\;(1+8\mathbb Z_2),
\]

and the normalized additive Haar measure of this closure is \(5/8\).

The structural reason is an exact distance law for two index branches. Define the \(2\)-adic interpolation

\[
 d(x)=\sum_{r=0}^{\infty}(-1)^r(x)_{\underline r},\qquad (x)_{\underline r}=\prod_{j=0}^{r-1}(x-j),\quad (x)_{\underline0}=1.
\]

For distinct odd \(x,y\in\mathbb Z_2\),

\[
\nu_2(d(x)-d(y))=\nu_2(x-y),
\]

while for distinct \(x,y\in4\mathbb Z_2\),

\[
\nu_2(d(x)-d(y))=\nu_2(x-y)+1.
\]

Consequently \(-d\) maps the ball \(1+2\mathbb Z_2\) bijectively and isometrically onto \(2\mathbb Z_2\), while \(d\) maps \(4\mathbb Z_2\) bijectively onto \(1+8\mathbb Z_2\), scaling \(2\)-adic distances by precisely \(1/2\).

## Assumptions and scope

All indices \(n\) are integers \(n\ge0\). All target moduli are positive powers of \(2\). The valuation \(\nu_2\) takes \(\nu_2(0)=+\infty\); the distance assertions concern distinct arguments. The ring \(\mathbb Z_2\) is the inverse limit of \(\mathbb Z/2^k\mathbb Z\), and its closed balls are compact. No assertion is made about odd-prime residue images or exact frequencies for individual values.

## Proof

**1. Convergence and agreement at integer indices.** Among any \(r\) consecutive integers one obtains a multiple of \(r!\). By density and continuity the same holds for \((x)_{\underline r}\) for every \(x\in\mathbb Z_2\). Therefore \(\nu_2((x)_{\underline r})\ge\nu_2(r!)\), uniformly in \(x\), and \(d\) converges uniformly to a continuous \(\mathbb Z_2\)-valued function. For every nonnegative integer \(n\), terms beyond \(r=n\) vanish and the inclusion-exclusion formula gives

\[
 d(n)=\sum_{r=0}^n(-1)^r\frac{n!}{(n-r)!}=(-1)^nD_n.
\]

In particular \(d(0)=1\) and \(d(1)=0\).

**2. Uniform divided-difference convergence.** For \(r\ge1\), write \(P_r(X)=(X)_{\underline r}\). The polynomial divided difference

\[
 Q_r(x,y)=\frac{P_r(x)-P_r(y)}{x-y}
 =\sum_{j=0}^{r-1}\left(\prod_{i=0}^{j-1}(x-i)\right)
 \left(\prod_{i=j+1}^{r-1}(y-i)\right)
\]

extends to \(x=y\) by its polynomial formula. Each summand is the product of \(j\) consecutive shifts of \(x\) and \(r-j-1\) consecutive shifts of \(y\), hence is divisible by \(j!(r-j-1)!\) in \(\mathbb Z_2\). Its valuation is at least

\[
\left\lfloor\frac j2\right\rfloor+
\left\lfloor\frac{r-j-1}{2}\right\rfloor
\ge \left\lfloor\frac{r-2}{2}\right\rfloor.
\]

Thus \(\sum_{r\ge1}(-1)^rQ_r(x,y)\) converges uniformly on \(\mathbb Z_2^2\) to a function \(U(x,y)\), with \(d(x)-d(y)=(x-y)U(x,y)\) for all \(x,y\). For \(x\equiv y\pmod{2^s}\), integral polynomial arithmetic yields \(Q_r(x,y)\equiv P_r'(x)\pmod{2^s}\).

**3. Odd-index isometry.** If \(x\) is odd, for every \(r\ge4\), the product of any \(r\) consecutive factors contains at least two even factors; differentiation deletes at most one, so \(P_r'(x)\equiv0\pmod2\). The first three nonzero terms have derivative sum

\[
\frac{d}{dX}\bigl[1-X+X(X-1)-X(X-1)(X-2)\bigr]\equiv1\pmod2
\]

at odd \(x\). Hence \(U(x,y)\equiv1\pmod2\) for all odd \(x,y\), proving \(\nu_2(d(x)-d(y))=\nu_2(x-y)\) when they differ. Since \(d(1)=0\), \(-d(1+2\mathbb Z_2)\subseteq2\mathbb Z_2\). At every modulus \(2^k\), the induced map between the \(2^{k-1}\) odd input classes and the \(2^{k-1}\) even output classes is injective by the distance law, hence bijective. Taking inverse limits gives the asserted isometry onto \(2\mathbb Z_2\).

**4. The even-index obstruction and the second isometry.** For even \(x\), the product of any four consecutive factors contains two even factors, one divisible by four, so \(P_r(x)\equiv0\pmod8\) whenever \(r\ge4\). The first four terms yield

\[
 d(x)\equiv 1-X+X(X-1)-X(X-1)(X-2)\big|_{X=x}
 \equiv1-x^3+4x^2-4x\equiv1\pmod8.
\]

For \(x\in4\mathbb Z_2\), the derivative of \(P_r\), \(r\ge5\), is divisible by four: among the five factors \(x,x-1,x-2,x-3,x-4\) there are three even factors, and deleting any one leaves at least two. Differentiating the first five terms instead gives

\[
 \frac{d}{dX}\left[1-X+X(X-1)-X(X-1)(X-2)+X(X-1)(X-2)(X-3)\right]
 =4X^3-21X^2+30X-10\equiv2\pmod4
\]

when \(X\in4\mathbb Z_2\). As \(x\equiv y\pmod4\), it follows that \(U(x,y)\equiv2\pmod4\) on \((4\mathbb Z_2)^2\). This proves the claimed \(\nu_2\)-distance law. Since \(d(0)=1\), the map \(d:4\mathbb Z_2\longrightarrow1+8\mathbb Z_2\) is injective, and at modulus \(2^k\), \(k\ge3\), the source classes modulo \(2^{k-1}\) and target classes modulo \(2^k\) each number \(2^{k-3}\). The distance law shows injectivity on these finite classes and hence surjectivity. Passing to the inverse limit proves exact equality of the balls.

**5. Image and infinitude.** For odd nonnegative \(n\), \(D_n=-d(n)\). For even \(n\), \(D_n=d(n)\equiv1\pmod8\). The positive odd integers are dense in \(1+2\mathbb Z_2\), and the nonnegative multiples of four are dense in \(4\mathbb Z_2\). The preceding maps therefore realize exactly the two claimed residue balls in the closure, while the congruence obstruction excludes every other residue. Each residue class has arbitrarily large nonnegative indices, because the interpolation is integral and continuous and the corresponding input arithmetic progression has infinitely many positive representatives. Counting the two disjoint sets modulo \(2^k\) gives \(2^{k-1}+2^{k-3}=5\cdot2^{k-3}\) for \(k\ge3\). The Haar measure is \(1/2+1/8=5/8\). Direct reduction covers \(k=1,2\). \(\square\)

## Verification

Run `python3 verify_derangement_image.py` using Python 3 standard library. The program computes the full image modulo \(2^k\) for each \(1\le k\le12\) from the exact recurrence, compares it with the predicted set, and checks the two distance laws for thousands of index pairs modulo \(2^{16}\). Its finite checks are corroboration only; the proof above establishes every exponent.

## Relationship to prior work

Miska's 2015 preprint (later published 2016) proves periodicity and \(2\)-adic valuation identities for derangements and develops a general pseudo-polynomial Hensel approach. The falling-factorial interpolation itself is explicitly present there. Those facts are assumed to be prior work, not new. The present claim asks a different question: which **values**, rather than which valuation orders, occur modulo every dyadic power? Sections 3 and 4.1.3 of the accessible full text discuss Hensel lifting for zeros, periodicity, and valuation of \(D_n\), but do not state the two-branch exact image, scaled isometry, or the \(5/8\) density. A specialized extension of the earlier Hensel machinery could recover the current result with additional calculations; this implication risk remains for independent priority review.

OEIS A000166 tabulates derangements and standard recurrences but does not establish the all-level image. A search of related mathematical research records identified no equivalent derangement claim, which is not evidence of historical uniqueness.

## Limitations

The result does not give exact multiplicities among a fixed set of indices or images modulo odd prime powers. Even after inspecting pertinent earlier primary text, an unlocated earlier equivalence remains possible.

## References

1. P. Miska, *Arithmetic Properties of the Sequence of Derangements and its Generalizations*, preprint first public 2015-08-09, arXiv:1508.01987v1, especially Sections 3 and 4.1.3; corresponding article *Arithmetic properties of the sequence of derangements*, Journal of Number Theory 163 (2016), 114–145, DOI 10.1016/j.jnt.2015.11.014.
2. OEIS Foundation, A000166, *Subfactorial or rencontres numbers, or derangements*, https://oeis.org/A000166.
