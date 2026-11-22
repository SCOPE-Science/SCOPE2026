# Complete seven-adic image and fibers of consecutive fourth-power sums

## Finding

For each integer \(n\ge0\), let
\[
F(n)=\sum_{j=1}^{n}j^4=\frac{n(n+1)(2n+1)(3n^2+3n-1)}{30}.
\]
Interpret the displayed polynomial as a continuous map \(F:\mathbb Z_7\to\mathbb Z_7\). There is a unique \(c\in1+7\mathbb Z_7\) satisfying \(F'(c)=0\). Put \(A=F(c)\) and \(u=c(c+1)(2c+1)\), so that \(u\equiv6\pmod7\) and \(A\equiv1\pmod{49}\). Its image, and hence the seven-adic closure of the integer power sums, is the disjoint union
\[
\boxed{F(\mathbb Z_7)=7\mathbb Z_7\ \sqcup\ (3+7\mathbb Z_7)\ \sqcup\ (4+7\mathbb Z_7)\ \sqcup\ (A+49u\mathbb Z_7^2)\ \sqcup\ (-A-49u\mathbb Z_7^2).}
\]
Here \(\mathbb Z_7^2=\{t^2:t\in\mathbb Z_7\}\), and the last two sets lie in residue classes \(1\) and \(6\) modulo seven respectively. The exact Haar measure is
\[
\boxed{\mu_7(F(\mathbb Z_7))=\frac{25}{56}.}
\]
For \(k\ge1\), write \(V(k)=|\{F(n)\bmod7^k:n\ge0\}|\). Set \(Q(0)=1\), and for \(m\ge1\) set
\[
Q(m)=1+3\sum_{j=0}^{\lfloor(m-1)/2\rfloor}7^{m-2j-1}.
\]
Then \(Q(m)\) counts distinct squares modulo \(7^m\), and
\[
\boxed{V(1)=5,\qquad V(k)=3\cdot7^{k-1}+2Q(k-2)\quad(k\ge2).}
\]
The first six values are \(5,23,155,1073,7505,52523\). The least index period of \(F(n)\bmod7^k\), starting at \(n=0\), is exactly \(7^k\).

All fibers are explicit. For \(k=1\) the residues \(0,1,3,4,6\) occur with respective multiplicities \(3,1,1,1,1\). For \(k\ge2\), let \(R_k(y)=\#\{n\bmod7^k:F(n)\equiv y\pmod{7^k}\}\). If \(y\equiv3,4\pmod7\), then \(R_k(y)=1\). If \(y\equiv0\pmod7\), then
\[
\boxed{R_k(y)=2+7\mathbf1_{\{y\equiv0\pmod{49}\}}.}
\]
Let \(r_m(z)=\#\{t\bmod7^m:t^2\equiv z\pmod{7^m}\}\), with \(r_0(0)=1\). In the two other attainable residue classes, set \((A_+,u_+)=(A,u)\) and \((A_-,u_-)=(-A,-u)\). For \(\sigma\in\{+,-\}\), a target \(y\equiv1\pmod7\) (for \(\sigma=+\)) or \(y\equiv6\pmod7\) (for \(\sigma=-\)) has \(R_k(y)=0\) unless \(y\equiv A_\sigma\pmod{49}\); in the latter case
\[
\boxed{R_k(y)=7\,r_{k-2}\left(u_\sigma^{-1}\frac{y-A_\sigma}{49}\right),}
\]
where the argument is interpreted modulo \(7^{k-2}\). Every unlisted target has no preimages. In particular, the branch above \(0\pmod7\) has a distinguished ninefold fiber on exactly \(49\mathbb Z/7^k\mathbb Z\), despite contributing no extra image values there.

## Assumptions and scope

All congruences are in the ordinary residue ring \(\mathbb Z/7^k\mathbb Z\), with \(k\) a positive integer. The half-sum polynomial is integral on every integer and has coefficients in \(\mathbb Z_7\), because \(30\) is a seven-adic unit. All finite target multiplicities count indices modulo the asserted exact period, not unrestricted nonnegative indices. The measure is normalized Haar measure on \(\mathbb Z_7\). The infinite square set includes zero and nonunit squares.

## Proof

**1. Polynomial, symmetry, and residue branches.** Direct summation of consecutive fourth powers gives the stated polynomial. Differentiating yields
\[
F'(x)=x^2(x+1)^2-\frac1{30},\qquad \frac{F''(x)}2=x(x+1)(2x+1).
\]
Writing \(z=x+1/2\) gives the exact identity
\[
F(x)=\frac{z^5}{5}-\frac{z^3}{6}+\frac{7z}{240},
\]
which proves \(F(-1-x)=-F(x)\). A complete calculation modulo seven is

| \(a\pmod7\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---:|---:|---:|---:|---:|---:|---:|
| \(F(a)\pmod7\) | 0 | 1 | 3 | 0 | 4 | 6 | 0 |
| \(F'(a)\pmod7\) | 3 | 0 | 4 | 0 | 4 | 0 | 3 |

For \(a=0,2,4,6\), expansion of \(F(a+7t)-F(a+7s)\) shows that the quotient by \(7(t-s)\) is congruent to the unit \(F'(a)\pmod7\). Hence each such branch maps bijectively and isometrically from \(a+7\mathbb Z_7\) onto \(F(a)+7\mathbb Z_7\). These four branches cover exactly the full target balls \(0+7\mathbb Z_7\), \(3+7\mathbb Z_7\), \(4+7\mathbb Z_7\); the first ball receives two regular branches.

**2. The additional but image-redundant central branch.** Since \(-1/2\equiv3\pmod7\), all inputs in the remaining class \(3+7\mathbb Z_7\) have the form \(x=-1/2+7t\). The centered polynomial becomes
\[
F(-1/2+7t)=49\left(\frac{t}{240}-\frac{7t^3}{6}+\frac{343t^5}{5}\right).
\]
The parenthesized map is congruent to \(t/240\pmod7\), and its difference quotient is a unit modulo seven for all distinct arguments. It is therefore an isometric bijection of \(\mathbb Z_7\) onto itself. This entire branch maps onto \(49\mathbb Z_7\), already contained in the regular \(7\mathbb Z_7\) ball. Modulo \(7^k\) with \(k\ge2\), each target in this smaller ball acquires exactly seven additional preimages: one normalized preimage modulo \(7^{k-2}\) and seven choices for its further index digit.

**3. Two exact quadratic branches.** The reduced derivative is proportional to \((x-3)^2(x-1)(x-5)\pmod7\). In particular, \(F'(1)\equiv0\pmod7\) and \(F''(1)\equiv5\not\equiv0\pmod7\). Hensel's lemma gives a unique \(c\in1+7\mathbb Z_7\) with \(F'(c)=0\). The symmetry gives its partner \(-1-c\in5+7\mathbb Z_7\), with critical value \(-A\). Taylor expansion about \(c\) gives, for every \(t\in\mathbb Z_7\),
\[
F(c+7t)=A+49u t^2\left(1+7tH(t)\right),
\]
where \(H(t)\in\mathbb Z_7[t]\), because the coefficient of \(t^2\) is the unit \(u=F''(c)/2\). The unique seven-adic square root \(h(t)=\sqrt{1+7tH(t)}\in1+7\mathbb Z_7\) exists by Hensel lifting. Its defining convergent power series has integral coefficients after extracting powers of seven; in particular \(h(t)=1+7K(t)\) with \(K\) one-Lipschitz. Hence \(\Phi(t)=t h(t)\) obeys
\[
\nu_7(\Phi(t)-\Phi(s))=\nu_7(t-s)
\]
for all \(t,s\); the reduction is \(\Phi(t)\equiv t\pmod7\). Thus \(\Phi\) induces a bijection at every finite precision and on \(\mathbb Z_7\), proving \(F(1+7\mathbb Z_7)=A+49u\mathbb Z_7^2\). The symmetry proves the negative branch as stated. Neither branch overlaps another, since their reductions modulo seven are respectively \(1\) and \(6\).

**4. Fiber formula, cardinalities, and measure.** Each of the two quadratic branches has normalized index parameter \(t\) modulo \(7^{k-1}\) and output precision \(7^{k-2}\). It therefore gives \(7r_{k-2}(z)\) indices for any compatible target, proving the fiber formula in the finding. Squares modulo \(7^m\) consist of zero and the unit-square classes of even valuations \(2j<m\). For each such valuation the count is \(3\cdot7^{m-2j-1}\); hence the formula for \(Q(m)\). The disjoint image decomposition gives the formula for \(V(k)\). The Haar measure of square values in \(\mathbb Z_7\) is
\[
\sum_{j\ge0}\frac3{7^{2j+1}}=\frac7{16}.
\]
Each quadratic branch has target measure \(7^{-2}(7/16)=1/112\), while the three complete balls have total measure \(3/7\). Summing gives \(25/56\).

**5. Exact period.** Since \(F\in\mathbb Z_7[x]\), the shift \(7^k\) is a period modulo \(7^k\). In the reduction modulo seven, the value \(1\) occurs only at index \(1\), so any period must be divisible by seven. If a purported period \(h\) satisfies \(\nu_7(h)=j\) with \(1\le j<k\), then the nonzero constant coefficient of \(F(x)/x\) is \(-1/30\), a seven-adic unit; therefore \(\nu_7(F(h)-F(0))=j\), impossible for a period modulo \(7^k\). Thus every positive period is divisible by \(7^k\), as required.

## Verification

The standalone `checker.py` performs exact integer computations without external dependencies. For every \(1\le k\le6\), it independently builds the complete prefix-sum histogram from the recurrence \(F(n+1)-F(n)=(n+1)^4\), derives the critical root by Hensel lifting, computes the predicted image count and every target fiber from square-root counts, and compares all \(7^k\) targets. It passed 274,512 exact comparisons. The resulting image counts at moduli \(7,49,343,2401,16807,117649\) are respectively \(5,23,155,1073,7505,52523\). The all-precision proof is Steps 1–5, not extrapolation from those comparisons.

Run `python3 checker.py` from a directory containing this document and the script. No external data files are needed.

## Relationship to prior work

W. J. Ralph's 1995 study of polynomial value sets over residue rings derives a general cardinality inequality, but the accessible abstract does not provide this particular Faulhaber image-and-fiber classification; the full paper was not accessible for line-by-line inspection. Mullen, Wan and Wang (2012) give upper bounds for polynomial-map value sets over finite fields, whereas here the claim concerns all powers of a fixed prime and singular branches. Mahmood and Ahmad (2014) develop algorithms for prime-power lifting of monomial congruences, without classifying this degree-five polynomial's image or its overlapping regular and singular fibers. The distinction is one of exact implications, not merely title vocabulary. A separately published pentatope polynomial classification concerns \(\binom{x}{4}\) at good primes; its value-set formula depends on that polynomial's nested-square identity and does not imply the different degree-five Faulhaber formula or its extra ninefold central fiber. A separately published dyadic even-power-sum study concerns sums of freely chosen powers, not consecutive-index partial sums. General Hensel and seven-adic Morse techniques are used as known mathematical tools and are not claimed as new.

## Limitations

This is a local classification for the specific consecutive fourth-power-sum polynomial at the prime seven; it is not a theorem for arbitrary Faulhaber polynomials, other primes, or global integer representability. The exact historical-priority status remains qualified because the complete 1995 polynomial-value-set paper could not be inspected. Checker tests are finite demonstrations; independent mathematical verification has not been performed.

## References

1. W. J. Ralph, *The value set of polynomials over \(\mathbb Z_m\) and the combinatorics of sequences*, Mathematika 42 (1995), 190–198, first published 1 June 1995. https://doi.org/10.1112/S0025579300011487
2. G. L. Mullen, D. Wan and Q. Wang, *Value sets of polynomial maps over finite fields*, arXiv:1210.8119v1, 30 October 2012. https://arxiv.org/abs/1210.8119
3. M. K. Mahmood and F. Ahmad, *Recursive Elucidation of Polynomial Congruences Using Root-Finding Numerical Techniques*, Abstract and Applied Analysis (2014), article 575064, published 5 May 2014. https://doi.org/10.1155/2014/575064
