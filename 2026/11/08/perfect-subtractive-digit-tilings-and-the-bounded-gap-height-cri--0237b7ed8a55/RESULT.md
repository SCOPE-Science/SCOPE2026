# Perfect subtractive digit tilings and the bounded-gap height criterion

## Finding

**Theorem (perfect coverage and sharp witness-height dichotomy).** Fix an integer base \(q\ge2\). Partition the nonnegative digit positions as \(\mathbb N_0=S\sqcup T\), with no assumption of periodicity. Let
\[
A_S^0=\left\{\sum_{i\in S}\varepsilon_i q^i:\varepsilon_i\in\{0,\ldots,q-1\},\ \varepsilon_i=0\text{ for all but finitely many }i\right\},
\]
\[
B_T^0=\left\{\sum_{i\in T}\eta_i q^i:\eta_i\in\{0,\ldots,q-1\},\ \eta_i=0\text{ for all but finitely many }i\right\}.
\]
Use \(A=1+A_S^0\) and \(B=1+B_T^0\), both subsets of the positive integers. Every integer has **at most one** representation \(n=b-a\) with \((a,b)\in A\times B\). Every integer has **exactly one** such representation if and only if both \(S\) and \(T\) are infinite.

Assume now that both supports are infinite, and let \((a(n),b(n))\) be the unique pair. Define the witness height \(H(n)=\max\{a(n),b(n)\}\) for \(n\ne0\). Then
\[
\sup_{n\in\mathbb Z\setminus\{0\}}\frac{H(n)}{|n|}<\infty
\quad\Longleftrightarrow\quad
S\text{ and }T\text{ both have bounded gaps}.
\]
More quantitatively, if every block of \(R\ge1\) consecutive nonnegative positions meets both supports, then, for every nonzero integer,
\[
H(n)\le 1+q^{R+1}|n|.
\]
Conversely, if \([j,j+r-1]\subseteq S\) and \(j+r\in T\), then the pair for \(n=q^j\) is exactly
\[
(a(n),b(n))=(1+q^{j+r}-q^j,\ 1+q^{j+r}),
\]
so \(H(n)/|n|=q^r+q^{-j}\). If instead \([j,j+r-1]\subseteq T\) and \(j+r\in S\), the analogous pair for \(n=-q^j\) has the same height ratio. These witnesses show the bounded-gap criterion is necessary, not merely sufficient.

**Polynomial-growth consequence.** For each real \(0<\alpha<1\), take
\[
S_\alpha=\{i\ge0:\lfloor(i+1)\alpha\rfloor-\lfloor i\alpha\rfloor=1\},\qquad T_\alpha=\mathbb N_0\setminus S_\alpha.
\]
Both sets have bounded gaps. The resulting positive-integer sets satisfy \(A(x)\asymp x^\alpha\), \(B(x)\asymp x^{1-\alpha}\), and
\[
d_{B,A}(n):=\#\{(a,b)\in A\times B:b-a=n\}=1
\qquad\text{for every }n\in\mathbb Z,
\]
with \(H(n)=O_{q,\alpha}(|n|)\) for nonzero \(n\). In particular, the positive-side summatory representation count equals \(\lfloor x\rfloor\) for every real \(x\ge1\).

## Assumptions and scope

The sets include a simultaneous translation by \(1\) only to make all elements positive; translating both sets by the same amount does not change any difference or representation multiplicity. An interval of \(R\) consecutive positions means \(\{j,j+1,\ldots,j+R-1\}\) for arbitrary \(j\ge0\). “Bounded gaps” means that some finite \(R\) works for the indicated support. The base \(q\) is fixed, although the support partition may be arbitrary and noncomputable. The representation of \(n=0\) is the single pair \((1,1)\); witness height is defined only for nonzero \(n\). The counting functions \(A(x)\) and \(B(x)\) count positive elements not exceeding real \(x\).

## Proof

**1. Forced signed digits and injectivity.** For any integer \(n\), set \(u_0=n\). At position \(i\in S\), choose the unique \(\varepsilon_i\in\{0,\ldots,q-1\}\) with \(u_i+\varepsilon_i\equiv0\pmod q\), and put \(u_{i+1}=(u_i+\varepsilon_i)/q=\lceil u_i/q\rceil\). At \(i\in T\), choose the unique \(\eta_i\in\{0,\ldots,q-1\}\) with \(u_i-\eta_i\equiv0\pmod q\), and put \(u_{i+1}=(u_i-\eta_i)/q=\lfloor u_i/q\rfloor\). Taking all unused digits as zero gives
\[
n=\sum_{i\ge0}(\eta_i-\varepsilon_i)q^i
\]
whenever this recurrence reaches zero. Conversely, any finite signed expansion with the permitted digit at each position is forced one digit at a time by reduction modulo \(q\). Therefore two distinct finite digit pairs cannot represent the same integer, even if one support is finite.

**2. Exact coverage.** When \(n>0\), all quotients \(u_i\) remain nonnegative. Every step is either floor or ceiling division by \(q\), hence repeated divisions eventually put \(u_i\) in \(\{0,1\}\). At state \(1\), a position in \(T\) sends the quotient to \(0\), while a position in \(S\) leaves it equal to \(1\). Thus an infinite \(T\) ensures finite termination for every positive \(n\). For \(n<0\), the quotient eventually belongs to \(\{-1,0\}\); an \(S\) position sends \(-1\) to zero, so infinite \(S\) ensures termination. The zero integer terminates immediately. Necessity is equally exact: if \(T\) is finite, \(B_T^0\) is bounded and sufficiently large positive integers cannot belong to \(B_T^0-A_S^0\); if \(S\) is finite, sufficiently large negative integers are excluded. This proves the first equivalence.

**3. Sufficiency of bounded gaps for linear witness height.** Suppose every length-\(R\) block meets both supports, and let \(n>0\) with \(q^h\le n<q^{h+1}\). At each step \(u_{i+1}\le\lceil u_i/q\rceil\), so \(0\le u_{h+1}\le\lceil n/q^{h+1}\rceil=1\). If the quotient is \(1\), its first subsequent \(T\) position occurs no later than \(h+R\), where it becomes zero. Therefore every nonzero signed digit lies at a position at most \(h+R\), and both nonnegative components are strictly smaller than \(q^{h+R+1}\). Since \(n\ge q^h\), the translated components are at most \(1+q^{R+1}n\). For negative \(n\), replace \(T\) by \(S\) in the termination argument and use \(|n|\) for the bound.

**4. Necessity of bounded gaps.** If \(T\) has unbounded gaps, then, since it is infinite, there exist arbitrarily long blocks of \(S\)-positions beginning at \(j\) and terminating at the next \(T\)-position \(j+r\). Apply the forced-digit algorithm to \(n=q^j\). Every position from \(j\) through \(j+r-1\) contributes the negative digit \(-(q-1)\), and the position \(j+r\) contributes \(+1\). It gives exactly \(q^j=q^{j+r}-(q^{j+r}-q^j)\) and the stated witness. Its height ratio is at least \(q^r\), which is unbounded. If instead \(S\) has unbounded gaps, apply the symmetric construction to \(n=-q^j\). This proves the converse and the quantitative sharpness.

**5. Growth-constrained exact-covering pairs.** For the displayed mechanical partition, among positions \(0,\ldots,N-1\) exactly \(s_N=\lfloor\alpha N\rfloor\) belong to \(S_\alpha\). Consequently the number of \(A_S^0\)-elements below \(q^N\) equals \(q^{s_N}\), while the corresponding number of \(B_T^0\)-elements equals \(q^{N-s_N}\). Comparing consecutive powers of \(q\) gives \(A(x)\asymp x^\alpha\) and \(B(x)\asymp x^{1-\alpha}\), even after translating by \(1\). For every interval of \(R\) positions, the number of \(S_\alpha\) positions is at least \(\lfloor R\alpha\rfloor\), and the number of \(T_\alpha\) positions is at least \(\lfloor R(1-\alpha)\rfloor\). Choosing \(R\) so that both floor values are positive proves bounded gaps and the height assertion. By steps 1–2, \(d_{B,A}(n)=1\) for all integers, so summation on positive integers gives \(\lfloor x\rfloor\).

## Verification

The accompanying standalone `verify_digit_tiling.py` uses exact integer arithmetic. It checks signed integers from \(-350\) through \(350\) over all nonconstant period-at-most-five partitions in bases \(2,3,4,5\), independently enumerates all six-digit pair differences to test injection, checks five rational mechanical slopes for signed integers from \(-1000\) to \(1000\), and verifies four explicit long-gap witnesses. Run with `python3 verify_digit_tiling.py` from the package directory. The actual verification output is recorded in `VERIFICATION.md`. No finite enumeration can prove the universal assertions; those follow from the five proof steps above.

## Relationship to prior work

Ding, Kiss, Niu, Pach, and Sándor (2026), Example 2.1, already use complementary **binary** digit supports of the same type to prove a pointwise upper bound \(d_{B,A}(n)\le1\) under polynomial counting-function constraints. **That injection and its use for the original first-moment upper bound are not claimed as new here.** Their construction does not state coverage of every signed integer, a necessary-and-sufficient infinite-support criterion, or the sharp bounded-gap characterization of linear representation height. The distinction is substantive: an injective difference representation may omit arbitrarily many integers, and finite or unbounded-gap supports give different coverage or height behavior.

Heuberger, Kropf, and Prodinger (2015/2017) analyze signed digit expansions with the same digit alphabet at every position, including constant mixed-sign alphabets; the present theorem instead concerns a position-dependent alternation of the two extreme sign alphabets, interpreted as a pair of positive integer sets, and characterizes witness height through support gaps. Hegarty (2007) and Xiong–Tang (2013/2014) treat unique representations for general linear forms or single-set bi-bases over signed integers, rather than this polynomial-growth two-set positional classification. Classical de Bruijn additive systems give **sum** decompositions of nonnegative integers; they do not themselves state the signed-difference height criterion. These comparisons do not exclude obscure earlier equivalent formulations.

## Limitations

The classification applies to complementary positional digit supports of a **fixed** integer base; it does not classify all pairs of positive integer sets with \(d_{B,A}(n)=1\). For a general noncomputable support partition the theorem is existential, not an algorithmic complexity guarantee. The uniform linear height bound is qualitative with an explicit sufficient constant, not an exact optimal constant for every partition. The polynomial counting functions are comparable to powers, not generally asymptotic to fixed constants times those powers. The result does not address the stronger regularity regime of Ding and coauthors, where their multiplicity lower bounds apply. A detailed historical search found no covering statement of the height criterion, but positional signed-digit folklore remains a priority risk.

## References

1. Y. Ding, S. Z. Kiss, W. Niu, P. P. Pach, C. Sándor, *Multiple representations in difference sets under polynomial density constraints*, arXiv:2610.40489v1, first posted 2026-10-29, especially Example 2.1, Proposition 1.1, and Section 5. https://arxiv.org/html/2610.40489v1
2. C. Heuberger, S. Kropf, H. Prodinger, *Analysis of Carries in Signed Digit Expansions*, arXiv:1503.08816 (2015), *Monatshefte für Mathematik* 182 (2017), Sections 1–2. https://arxiv.org/abs/1503.08816
3. P. Hegarty, *The inverse problem for representation functions for general linear forms*, arXiv:0712.4399 (2007), Sections 1–2. https://arxiv.org/abs/0712.4399
4. R. Xiong, M. Tang, *Unique representation bi-basis for the integers*, *Bulletin of the Australian Mathematical Society* 89 (2014), 460–465, DOI:10.1017/S0004972713000762, Theorems 1.1–1.2.
