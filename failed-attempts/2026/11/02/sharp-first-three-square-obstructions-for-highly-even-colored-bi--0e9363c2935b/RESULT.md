# Sharp first three-square obstructions for highly even-colored binary partitions

## Finding

Let \(m\) be a positive integer and define
\[
B_m(X)=\prod_{j\ge0}(1-X^{2^j})^{-m}
       =\sum_{n\ge0}b_m(n)X^n.
\]
Thus \(b_m(n)\) counts partitions of \(n\) into powers of two, each part having one of \(m\) colors. Define
\[
\rho(m)=\min\{n\ge0:b_m(n)\ne a^2+b^2+c^2\text{ for all }a,b,c\in\mathbb Z\}.
\]
The minimum exists for every color count covered below.

**Theorem.** Write \(m=2^k u\), where \(k\ge6\) and \(u\ge1\) is odd. The exact first obstruction depends only on the parity of \(k\) and on \(u\bmod8\):

| \(u\bmod8\) | even \(k\): \(\rho(m)\) | odd \(k\): \(\rho(m)\) |
|:---:|---:|---:|
| \(1\) | \(4\) | \(8\) |
| \(3\) | \(5\) | \(14\) |
| \(5\) | \(3\) | \(2\) |
| \(7\) | \(1\) | \(6\) |

The bound \(\rho(m)\le14\) for all \(m\) with \(64\mid m\) is sharp: equality holds whenever \(k\ge7\) is odd and \(u\equiv3\pmod8\). The valuation threshold \(k\ge6\) is also sharp for this uniform eight-class rule: \(m=96=2^5\cdot3\) has \(\rho(96)=18\), rather than the index 14 predicted by extending the odd-\(k\), \(u\equiv3\) case one level downward.

For powers of two below 64, the complete exceptions are
\[
\rho(2)=34,\quad\rho(4)=10,\quad\rho(8)=13,\quad
\rho(16)=4,\quad\rho(32)=8.
\]
Consequently, for every \(k\ge4\), \(\rho(2^k)=4\) for even \(k\), and \(\rho(2^k)=8\) for odd \(k\). Together with the three smaller exceptional exponents, this determines \(\rho(2^k)\) for every \(k\ge1\).

## Assumptions and scope

All indices are nonnegative integers, all color counts are positive integers, and squares are squares of arbitrary integers. The valuation \(\nu_2(z)\) is the exponent of 2 dividing a nonzero integer \(z\). Congruences with fractions whose denominators are odd are interpreted in \(\mathbb Z/8\mathbb Z\) by multiplication by the inverse of the denominator. No assumption is made that \(u\) is prime or bounded.

## Proof

**1. A coefficient-polynomial identity.** Formally,
\[
\log B_1(X)=\sum_{j\ge1}a_jX^j,\qquad
 a_j=\frac{2^{\nu_2(j)+1}-1}{j}.
\]
Indeed, the summand \(X^j\) in \(-\sum_{h\ge0}\log(1-X^{2^h})\) receives a contribution \(2^h/j\) for each \(h\) with \(2^h\mid j\). Put \(P_n(M)=[X^n]\exp(M\log B_1(X))\), so \(P_n(m)=b_m(n)\). Formal differentiation gives the rational-polynomial recursion
\[
P_0(M)=1,\qquad
P_n(M)=\frac{M}{n}\sum_{j=1}^{n}(2^{\nu_2(j)+1}-1)P_{n-j}(M)
\quad(n\ge1).
\]
Write \(P_n(M)=\sum_{t=1}^nc_{n,t}M^t\) for \(n>0\). The first coefficient is \(c_{n,1}=a_n\). The recursion constructs all \(c_{n,t}\) by exact rational arithmetic.

**2. A uniform fourteen-term 2-adic estimate.** For every \(1\le n\le14\), direct rational-polynomial recursion yields
\[
\min_{2\le t\le n,\ c_{n,t}\ne0}
\bigl(\nu_2(c_{n,t})+6(t-1)+\nu_2(n)\bigr)
\ge3.
\]
The minimum, with \(\infty\) for \(n=1\), is given for \(n=1,2,\ldots,14\) by
\[
\infty,6,5,5,4,4,4,4,3,3,3,3,3,3.
\]
These fourteen exact finite rational comparisons are reproduced by the standalone `verify.py` (function `coeff_polynomials`, with independent coefficient evaluation below). If \(m=2^ku\) with \(u\) odd and \(k\ge6\), each higher-degree term \(c_{n,t}m^t\) has valuation at least \(k-\nu_2(n)+3\), because increasing \(k\) from 6 adds \((t-1)(k-6)\) to the displayed margin. Thus
\[
b_m(n)\equiv m\,\frac{2^{\nu_2(n)+1}-1}{n}
\pmod{2^{k-\nu_2(n)+3}},\qquad 1\le n\le14.
\]
In particular,
\[
\nu_2(b_m(n))=k-\nu_2(n),\qquad
\frac{b_m(n)}{2^{k-\nu_2(n)}}
\equiv u\,\frac{2^{\nu_2(n)+1}-1}{n/2^{\nu_2(n)}}\pmod8.
\tag{1}
\]
The right-hand side of (1) is odd, so the stated exact valuation follows as well.

**3. First forbidden term.** Legendre's three-square theorem says that a nonnegative integer fails to be a sum of three integer squares exactly when it has the form \(4^a(8b+7)\), with nonnegative integers \(a,b\). By (1), a forbidden term among \(1\le n\le14\) occurs precisely when \(k-\nu_2(n)\) is even and the right-hand side of (1) is 7 modulo 8. Checking the fourteen possible indices yields the first such index for each \((k\bmod2,u\bmod8)\). In increasing order of indices, the decisive normalized units are
\[
\begin{array}{c|rrrrrrrr}
 n&1&2&3&4&5&6&8&14\\\hline
 (2^{\nu_2(n)+1}-1)/(n/2^{\nu_2(n)})\pmod8
 &1&3&3&7&5&1&7&5
\end{array}.
\]
For even \(k\), only \(n\) with even \(\nu_2(n)\) can obstruct; the first ones are 1,3,4,5, in the order needed for the four odd residues of \(u\). For odd \(k\), only \(n\) with odd \(\nu_2(n)\) can obstruct; the first possible indices are 2,6,8,10,14, with unit values 3,1,7,7,5. The four odd residue classes of \(u\) give first indices 2,6,8,14 as tabulated. All preceding indices have either odd 2-adic valuation or a unit other than 7; the index 0 has coefficient 1. This proves the full table for all \(k\ge6\) and every odd \(u\).

**4. Small powers of two.** For \(m=2,4,8,16,32\), apply the independent exact integer recurrence obtained by differentiating \(B_m\):
\[
b_m(0)=1,\qquad
n b_m(n)=m\sum_{j=1}^{n}(2^{\nu_2(j)+1}-1)b_m(n-j).
\]
Its exhaustive coefficients from index 0 through, respectively, 34, 10, 13, 4 and 8 have no earlier three-square obstruction. Their first forbidden values are respectively 32192, 4464, 2292736, 6204 and 169008476; in all five cases removing the largest power of 4 leaves an integer congruent to 7 modulo 8. These exhaustive short checks are reproduced from integer arithmetic in `verify.py`. There is no untested intermediate index. The same recurrence checks all indices through 18 for \(m=96\), proving \(\rho(96)=18\) and the sharpness of the hypothesis \(k\ge6\) for the uniform eight-class rule. This completes the proof. \(\square\)

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. The script independently derives rational coefficients through index 14, recomputes the fourteen valuation margins, tests forty large-even-color representatives and the small exceptional indices, and checks the exact first forbidden coefficients. The proof's universal parameter quantifiers follow from the polynomial valuation inequality and residue analysis, not from sampling the forty representatives.

## Relationship to prior work

Sobolewski and Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares* (arXiv:2211.16622; published 2023), solve the three-square representation problem for color counts \(m=2^k-1\), and state in their Section 7, Problem 7.2, the general problem of characterizing the nonrepresentable index sets \(S_m\) for arbitrary \(m\). The theorem here concerns the complementary, highly-even color regime and its sharp initial obstruction, not a full description of \(S_m\). Their Proposition 7.3 supplies automaticity of each fixed-modulus coefficient sequence but does not imply the first-index table across all color counts.

Gawron, Miska and Ulas (arXiv:1703.01955) develop the general colored binary-partition coefficients and related 2-adic congruences; their published results include the \(m=2^k-1\) valuation structure. The present result adds a uniform eight-class initial three-square classification for \(\nu_2(m)\ge6\). The explicit first three-square obstruction for the uncolored case belongs to the already known theory and is not claimed here.

## Limitations

The theorem determines only the first forbidden index and does not classify every index at which \(b_m(n)\) is not a sum of three squares. For color counts with \(\nu_2(m)<6\), only the five stated pure powers of two are covered. The threshold 6 is optimal for the stated uniform residue-class table, as witnessed by \(m=96\); optimality of other possible reformulations is not asserted. Bibliographic comparison cannot exclude unindexed equivalent results.

## References

1. B. Sobolewski and M. Ulas, *Values of Binary Partition Function Represented by a Sum of Three Squares*, arXiv:2211.16622 (first posted 2022-11-29); *Results in Mathematics* 78 (2023), article 188, doi:10.1007/s00025-023-01966-8.
2. M. Gawron, P. Miska and M. Ulas, *Arithmetic properties of coefficients of power series expansion of \(\prod_{j\ge0}(1-X^{2^j})^t\)*, arXiv:1703.01955 (first posted 2017-03-06).
3. A.-M. Legendre, the classical three-square theorem (the forbidden integers are \(4^a(8b+7)\)).
