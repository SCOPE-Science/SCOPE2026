# Complete gap spectra of binary cyclotomic polynomials for residues \(\pm2\)

## Finding

For coprime integers \(5\le a<b\) with \(a=2h+1\) odd and \(h\ge2\), define the two-generator semigroup polynomial
\[
P_{a,b}(X)=\frac{(1-X)(1-X^{ab})}{(1-X^a)(1-X^b)}.
\]
Its degree is \((a-1)(b-1)\). If its nonzero exponents are \(0=e_0<e_1<\cdots<e_m=(a-1)(b-1)\), let \(H_g(a,b)=\#\{i:e_{i+1}-e_i=g\}\), counting gaps of length one as well.

**Theorem (complete \(\pm2\) gap law).** Suppose \(s\ge1\) is an integer.

* For \(b=as+2\),
  \[
  H_1=2h^2s+2h,\qquad H_{2j}=2s\quad(1\le j\le h).
  \]
* For \(b=a(s+1)-2\),
  \[
  H_1=2h^2s+2h(h-1),\quad H_{2j}=2s+2\quad(1\le j<h),\quad H_{2h}=2s.
  \]

All unlisted gap counts are zero. Thus every gap longer than one has even length, and the full multiplicity pattern depends only on \(a\), \(s\) and the sign. The number of nonzero coefficients is respectively
\[
2h(h+1)s+2h+1\quad\text{or}\quad2h(h+1)(s+1)-(2h+1).
\]
When \(a=p<b=q\) are distinct odd primes, \(P_{p,q}=\Phi_{pq}\), so the theorem supplies the complete spectra for \(q\equiv\pm2\pmod p\). It also applies when either generator is composite.

## Assumptions and scope

Integers \(a=2h+1\ge5\), \(s\ge1\) and \(b>a\) are as stated; \(b=as+2\) and \(b=a(s+1)-2\) are automatically coprime to odd \(a\). A gap is a difference of **consecutive nonzero coefficient exponents**, including length one; it is not a gap in the numerical semigroup itself. Intervals in the proof are closed integer intervals. The proof does not assume primality, nor does it assume that the index ratio is bounded.

## Proof

**1. Two-rectangle coefficient identity.** For any coprime \(a,b\), there is a unique pair \(1\le\alpha<b\), \(1\le\beta<a\) satisfying \(a\alpha+b\beta=ab+1\) (take the inverses of \(a\) modulo \(b\), and \(b\) modulo \(a\)). Put
\[
U(X)=\left(\sum_{i=0}^{\alpha-1}X^{ia}\right)\left(\sum_{j=0}^{\beta-1}X^{jb}\right),\qquad
V(X)=X\left(\sum_{i=0}^{b-\alpha-1}X^{ia}\right)\left(\sum_{j=0}^{a-\beta-1}X^{jb}\right).
\]
Multiplication by \((1-X^a)(1-X^b)\) and the equality \(a\alpha+b\beta=ab+1\) give exactly
\[
(1-X^a)(1-X^b)(U-V)=(1-X)(1-X^{ab}).
\]
Within each rectangle, degrees are distinct: if \(ia+jb=i'a+j'b\) with \(|j-j'|<a\), coprimality forces \(j=j'\) and \(i=i'\). In the two families below, the positive and negative degrees also occupy **disjoint residue classes modulo \(a\)**, so the support of \(P_{a,b}=U-V\) is precisely their union, without cancellation.

**2. The \(+2\) family.** Write \(b=as+2\). Then \(\alpha=hs+1\) and \(\beta=h+1\). Express every exponent uniquely as \(n=at+r\), \(0\le r<a\). The two rectangles yield
\[
\begin{array}{ll}
r=2j\ (0\le j\le h): & js\le t\le(j+h)s,\\
r=2j+1\ (0\le j<h):&js\le t\le(j+h+1)s.
\end{array}
\]
No other \((t,r)\) belongs to the support. Consequently, for each row \(t=0,\ldots,2hs\) the occupied residues are one entire integer interval \([L_t,R_t]\), with
\[
L_t=\begin{cases}0,&t\le hs,\\ 2\left\lceil\frac{t-hs}{s}\right\rceil-1,&t>hs,\end{cases}
\qquad
R_t=\begin{cases}2\left\lfloor\frac ts\right\rfloor+1,&t<hs,\\2h,&t\ge hs.\end{cases}
\]
Consecutive occupied positions within a row give only gaps of length one. The gap between the last support position in row \(t\) and the first in row \(t+1\) is \(a+L_{t+1}-R_t\). For \(0\le t<hs\), this equals \(2(h-\lfloor t/s\rfloor)\); for \(hs\le t<2hs\), it equals \(2\lceil(t+1-hs)/s\rceil\). Each of the \(h\) even lengths \(2,4,\ldots,2h\) therefore appears precisely \(2s\) times. Counting degrees in the two disjoint rectangles gives \(2h(h+1)s+2h+1\) nonzero coefficients; subtracting one and the \(2hs\) nonunit gaps gives \(H_1=2h^2s+2h\).

**3. The \(-2\) family.** Write \(b=au-2\), \(u=s+1\ge2\). Now \(\alpha=(h+1)u-1\) and \(\beta=h\). Its complete residue-row membership is
\[
\begin{array}{ll}
r=0:&0\le t\le(h+1)u-2,\\
r=1:&0\le t\le hu-2,\\
r=a-2j\ (1\le j<h):&ju-1\le t\le(j+h+1)u-3,\\
r=a+1-2j\ (1\le j\le h):&ju-1\le t\le(j+h)u-3.
\end{array}
\]
These disjoint residue classes give the following complete row description; all intervals below are intervals of occupied residues:

* For \(0\le t\le u-2\): \([0,1]\).
* For each \(1\le j<h\), when \(ju-1\le t\le(j+1)u-2\): \([0,1]\cup[a-2j,a-1]\).
* For \(hu-1\le t\le(h+1)u-3\): \(\{0\}\cup[2,a-1]\).
* At \(t=(h+1)u-2\): \(\{0\}\cup[2,a-2]\).
* For \((h+1)u-1\le t\le(h+2)u-3\): \([2,a-2]\).
* For each \(2\le j<h\), when \((h+j)u-2\le t\le(h+j+1)u-3\): \([2,a-2j]\).

The first \(u-1\) boundaries between rows have gap \(2h\), and the final \(u-1\) row boundaries also have gap \(2h\). The late right-edge stages give \(u\) inter-row gaps of each length \(4,6,\ldots,2h-2\). All remaining row boundaries have gap one. In the early two-component rows, each \(j=1,\ldots,h-1\) contributes \(u\) within-row gaps of length \(2(h-j)\). The central two-component rows contribute a further \(u\) within-row gaps of length two. No other within-row gap exceeds one. Hence \(H_{2h}=2(u-1)=2s\), and \(H_{2j}=2u=2s+2\) for \(1\le j<h\). The two rectangles have \(h((h+1)u-1)+(h+1)(hu-1)=2h(h+1)u-(2h+1)\) nonzero coefficients. Subtracting one and the \(2hu-2\) nonunit gaps yields \(H_1=2h^2u-2h=2h^2s+2h(h-1)\). This proves both cases. \(\square\)

## Verification

The standalone \(CHECK.py\) computes \(P_{a,b}\) independently from the coefficient recursion for \((1-X^a)^{-1}(1-X^b)^{-1}\), up to degree \((a-1)(b-1)<ab\). It then compares all nonzero exponents, every residue-row membership and the entire gap histogram with the theorem. It passes 810 parameter cases: every odd \(5\le a\le57\), \(1\le s\le15\), and both residue signs; in total 8,050,320 coefficient positions and 4,140,180 nonzero support positions. Run \(`python3 CHECK.py`\). These finite checks are supplementary; the proof above covers all eligible integers.

## Relationship to prior work

The numerical-semigroup identity for \(P_{a,b}\) and classical coefficient representations are established in the earlier binary-cyclotomic literature. Camburu, Ciolan, Luca, Moree and Shparlinski (2015 preprint) proved the maximum gap and its multiplicity, and characterized the residue classes exhibiting every gap length. Cafure and Cesaratto (2021 preprint, updated 2024) gave a complete coefficient-word representation and algorithm. In their July 2025 paper, they determined the second-largest gap for arbitrary residues and all gap multiplicities when \(b\equiv\pm1\pmod a\). Their full-text theorems do not state the complete \(\pm2\) histograms obtained here. A separately published exact run-length result for the narrow family \(b=a+2\) covers the \(+2\) formula at \(s=1\), but its parameter relation does not cover \(s\ge2\) or the \(-2\) branch generally. The present claim is the two-variable \(\pm2\) spectrum, not the known maximum-gap fact or the special \(s=1\) case.

## Limitations

The theorem does not address residues other than \(\pm2\), or arbitrary products of more than two distinct primes. It is a complete statement about coefficient **support spacing**, not the signs of coefficients. A formula can be implied by an uncatalogued or not fully indexed result even where searches do not find identical wording; independent bibliographic validation is still warranted.

## References

1. O.-M. Camburu, E.-A. Ciolan, F. Luca, P. Moree and I. E. Shparlinski, *Cyclotomic coefficients: gaps and jumps*, first posted 2015-07-25, https://arxiv.org/abs/1507.07098 , Theorem 3.2 and Section 3.3.
2. A. Cafure and E. Cesaratto, *Binary Cyclotomic Polynomials: Representation via Words and Algorithms*, first posted 2021-09-15, https://arxiv.org/abs/2109.07544 , Theorem 2.1.
3. I. E. Shparlinski and L. P. Wijaya, *On Nonzero Coefficients of Binary Cyclotomic Polynomials*, first posted 2023-07-14, https://arxiv.org/abs/2307.07229 , Introduction.
4. A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, first posted 2025-07-25, https://arxiv.org/abs/2507.19381 , Theorems 1.1 and 1.2 and Sections 3–4.
