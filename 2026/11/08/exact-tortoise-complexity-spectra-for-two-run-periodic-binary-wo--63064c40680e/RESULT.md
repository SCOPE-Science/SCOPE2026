# Exact tortoise-complexity spectra for two-run periodic binary words

## Finding

Let \(a,b\geq1\) be integers and let \(\mathbf{x}_{a,b}=(0^a1^b)^\omega\). For a finite binary word \(w\), define \(T(w)\) by deleting its leftmost \(1\), if any, and appending \(1\) at the right; set \(T(0^n)=0^n\). For integers \(n,k\geq1\), let
\[
 c_{a,b}^{(k)}(n)=\bigl|\{T^k(w):w\text{ is a contiguous factor of }\mathbf{x}_{a,b}\text{ of length }n\}\bigr|.
\]
Put \(p=a+b\). The following two formulas give a complete one-step spectrum for **every** two-run period, and the complete iteration hierarchy when the \(1\)-run is a singleton.

**One-step spectrum for \(b\geq2\).** For every \(n\geq1\),
\[
 c_{a,b}^{(1)}(n)=
 \begin{cases}
 2,&n=1,\\
 \min(n,a)+\min(n,b)-1,&2\leq n\leq p,\\
 p,&n\geq p+1.
 \end{cases}
\]
For each \(2\leq n\leq p\), exactly one pair of **distinct** length-\(n\) factors is identified by \(T\); there are no other nonsingleton equivalence classes.

**All iterations for \(b=1\).** Fix any \(k\geq1\), now put \(p=a+1\), and write \(n=qp+r\), where \(q\geq0\) and \(0\leq r<p\). Then
\[
 c_{a,1}^{(k)}(n)=
 \begin{cases}
 1,&q<k\ \text{and }r=0,\\
 2,&q<k\ \text{and }1\leq r<p,\\
 r+1,&q=k,\\
 p,&q>k.
 \end{cases}
\]
In particular, every one of the lengths \(p,2p,\ldots,kp\) has a single \(k\)-tortoise equivalence class, and the exact least length from which the complexity is permanently equal to the ordinary factor complexity \(p\) is \((k+1)p-1\). The value immediately before this least length is \(p-1\).

## Assumptions and scope

All factors are **contiguous**, not scattered. The word \(\mathbf{x}_{a,b}\) is one-sided, infinite, purely periodic and over the ordered alphabet \(0<1\). Its least period is \(p=a+b\). Positions begin at zero, but all statements are independent of the initial phase because the set of finite factors contains every cyclic phase. The operation \(T\) is the binary specialization of the Defant--Kravitz tortoise map as used for the \(k\)-tortoise complexity of Campbell and Rampersad; exponent \(k\) denotes **iteration**, not deletion of an arbitrary set of \(k\) symbols. No assertion is made about the complete \(k\)-step spectrum when both \(b\geq2\) and \(k\geq2\).

## Proof

**The operation.** A finite binary word with \(m\geq1\) ones has a unique presentation
\[
 w=0^{z_0}1\,0^{z_1}1\cdots1\,0^{z_m},\qquad z_i\geq0.
\]
Directly from the definition,
\[
 T(w)=0^{z_0+z_1}1\,0^{z_2}1\cdots0^{z_m}1.
\]
Repeated application removes the first \(\min(k,m)\) ones and places the removed ones at the end in the same number. If \(k\geq m\), the image is the sorted word \(0^{|w|-m}1^m\).

**Ordinary factor complexity and phases.** The \(p\) starting phases of \(\mathbf{x}_{a,b}\) give exactly \(\min(n,a)+\min(n,b)\) distinct length-\(n\) factors. To see this, different phases giving a factor with both letters are distinguished by the initial symbol and the position of its first change, while an all-zero or all-one factor can be repeated in respectively \(\max(a-n+1,0)\) or \(\max(b-n+1,0)\) starting phases. Thus the number of duplicate phases is \(\max(a-n,0)+\max(b-n,0)\), and subtraction from \(p\) gives the claimed expression. For \(n\geq p\), all \(p\) factors are distinct.

**One step when \(b\geq2\).** The number of ones is invariant under \(T\), so only factors with the same number \(m\) of ones can collide. If \(m=0\), there is just one all-zero factor. If \(m=1\), every factor has image \(0^{n-1}1\). For \(2\leq n\leq a+1\), precisely the two distinct one-one factors \(0^{n-1}1\) and \(10^{n-1}\) occur; outside that range at most one distinct one-one factor occurs.

For \(m\geq2\), suppose distinct factors \(u,v\) have the same image. In the gap representation above, equality of the images fixes \(m\), the sum \(z_0+z_1\), and each of \(z_2,\ldots,z_m\). In this periodic word, the first two ones of a factor are either adjacent (so \(z_1=0\)) or are separated by exactly \(a\) zeros (so \(z_1=a\)). If the two factors have the same \(z_1\), their equality follows, contradicting distinctness. Hence they have different \(z_1\), and equality of their sums, together with \(0\leq z_0\leq a\), forces their initial gap pairs to be \((z_0,z_1)=(a,0)\) and \((0,a)\). These are the phases at the very beginning of a zero-run and at the last one of a one-run. Comparing the remaining gaps shows equality exactly for
\[
 u=0^a1^m,\qquad v=10^a1^{m-1},\qquad 2\leq m\leq b,\qquad n=a+m.
\]
Indeed, for those lengths the tails have all remaining zero gaps equal to zero. If a further one occurs, the gap between the \(b\)-th and \((b+1)\)-st ones is \(a\) in one factor and zero in the other; if the window is merely extended without an extra one, their terminal gaps differ. Thus no longer collision is possible. The one-one collision ranges over \(2\leq n\leq a+1\), and the displayed multi-one collision ranges over \(a+2\leq n\leq a+b=p\). Exactly one pair collides at every length \(2\leq n\leq p\), and no pair collides at \(n\geq p+1\). Subtracting one from the ordinary factor count proves the first formula.

**All steps when \(b=1\).** Write \(p=a+1\). Identify each cyclic starting phase with the integer \(d\in\{0,\ldots,a\}\) counting the zeros until the first one. For \(n=qp+r\), the \(p\) phase windows have \(q\) or \(q+1\) ones. If \(r=0\), all have \(q\) ones; otherwise precisely \(r\) windows have \(q+1\) ones and \(p-r\) have \(q\).

If \(q<k\), all these windows contain at most \(k\) ones, so every image is sorted. Its ones count is the only invariant: there is one class for \(r=0\), and two for \(r>0\). If \(q=k\), the \(p-r\) phases with exactly \(k\) ones give one sorted image (when \(r=0\) this is every phase). For each of the remaining \(r\) phases, \(d=0,\ldots,r-1\), there are \(k+1\) ones and their images are exactly
\[
 T^k(w_d)=0^{d+ka}1\,0^{r-d-1}1^k.
\]
These \(r\) images have distinct initial zero-run lengths, and their number of ones distinguishes them from the sorted \(k\)-one image. Hence the number is \(r+1\).

Finally, if \(q>k\), every phase factor has at least \(k+1\) ones. After deleting the first \(k\), its initial zero run has length exactly \(d+ka\), so all \(p\) phases have distinct images. This proves the second formula. At length \((k+1)p-1\), the formula yields \(p\), and all subsequent lengths also yield \(p\); at the preceding length it yields only \(p-1\), proving sharpness.

## Verification

The embedded standalone program `verify.py` implements \(T\) in two independently written ways: direct first-one deletion and the zero-gap recurrence. It enumerates the entire cyclic factor set, compares both image sets, and checks the formulas. It passed 15,810 parameter-length comparisons, including all \(1\leq a,b\leq12\) for the one-step statement and all \(1\leq a\leq12\), \(1\leq k\leq10\) for the singleton-one-run hierarchy, over the length ranges specified in the code. The program uses only the Python standard library. These finite checks corroborate but do not replace the proof for all parameter values.

## Relationship to prior work

Campbell and Rampersad introduced factor complexity under iterative tortoise equivalence, established a coarse comparison with ordinary factor complexity for bounded-gap words of linear complexity, and calculated the tortoise complexity of the paperfolding and Thue--Morse words [1]. That comparison implies a bounded eventual deficit for the periodic words here, but it does not determine the exact finite spectrum, the unique collision at every intermediate one-step length, or the sharp dependence of the recovery threshold on \(k\). The prior source's general operator definition is used, not claimed as novel. Defant and Kravitz previously defined the underlying sorting map and studied its preimages for finite words [2]. Their finite-word preimage framework is different from an exact all-length factor spectrum for a fixed periodic infinite word.

## Limitations

The complete all-iteration formula is restricted to singleton \(1\)-runs. For \(b\geq2\), only the first iterate is classified. There is no assertion for arbitrary periodic binary words with three or more runs per period, for aperiodic words, or for other sorting operators. Exhaustive computations establish only finite test cases. The bibliographic comparison does not exclude unpublished or unindexed equivalent results; independent external mathematical validation has not been performed.

## References

1. J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811. First public version 2026-04-28 UTC; version 2, 2026-10-05. https://arxiv.org/html/2604.25811v2
2. C. Defant and N. Kravitz, *Stack-sorting for words*, arXiv:1809.09158, first public version 2018-09-24 UTC; Australasian Journal of Combinatorics 77 (2020), 51–68. https://arxiv.org/abs/1809.09158
