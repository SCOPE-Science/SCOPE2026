# A uniform non-maximal-embedding-dimension family beyond the known three-coin p-Apéry range

## Finding
For every integer \(a\ge7\), let \(k=\lfloor a/2\rfloor\), \(p=k+5\), and define the denumerant
\[
d_a(n)=\#\{(x,y,z)\in\mathbb Z_{\ge0}^3:ax+(a+1)y+(a+2)z=n\}.
\]
Let \(S_{a,p}=\{0\}\cup\{n\ge1:d_a(n)\ge p+1\}\). Then this numerical semigroup has multiplicity
\[
m=(a+2)^2-2
\]
but its embedding dimension is strictly smaller than its multiplicity. More precisely, writing \(c=(a+2)^2\):

* If \(a\) is even, \(d_a(c)=p+1\) while \(d_a(c+2)=p\). Consequently \(c,c\in S_{a,p}\) and \(c+c-m=c+2\notin S_{a,p}\).
* If \(a\) is odd, \(d_a(c-1)=d_a(c)=p+1\) while \(d_a(c+1)=p\). Consequently \(c-1,c\in S_{a,p}\) and \((c-1)+c-m=c+1\notin S_{a,p}\).

In particular, these give an infinite explicit family of generalized-representation numerical semigroups which **do not** have maximal embedding dimension.

## Assumptions and scope
All variables \(a,k,p,n,x,y,z\) are integers and all representation coordinates are nonnegative. The claimed statement requires \(a\ge7\) and \(p=\lfloor a/2\rfloor+5\); it is not a classification for arbitrary \(p\), nor does it determine the actual embedding dimension. The numerical semigroup contains zero by definition. Its multiplicity is its least positive element and its embedding dimension is the cardinality of its unique minimal set of positive additive generators.

## Proof
**1. Exact length enumeration.** A representation with total coin count \(t=x+y+z\) has \(u=n-at=y+2z\). For given \(t\), there is one representation for every integer \(z\) satisfying
\[
\max(0,u-t)\le z\le\lfloor u/2\rfloor.
\]
Thus the exact finite formula, with negative contributions replaced by zero, is
\[
d_a(n)=\sum_{t=0}^{\lfloor n/a\rfloor}
\max\left\{0,\lfloor(n-at)/2\rfloor-\max(0,n-(a+1)t)+1\right\}.
\tag{1}
\]
Adding one coin of value \(a\) injects the representations of \(n\) into those of \(n+a\), so \(d_a(n+a)\ge d_a(n)\).

**2. The first positive element.** Put \(n_0=(a+1)(a+2)\), so \(m=n_0+a\). For each \(0\le r<a\), direct application of (1) shows that the only admissible total counts for \(n_0+r\) are \(t=a+2,a+3\), together with \(t=a+1\) when \(r=0\), and \(t=a+4\) when \(r\in\{a-2,a-1\}\). Their respective contributions are
\[
\left\lfloor\frac{a+2-r}{2}\right\rfloor+1,\qquad
\left\lfloor\frac r2\right\rfloor+2,\qquad1,\qquad1.
\]
It follows that
\[
d_a(n_0+r)=\left\lfloor\frac{a+2-r}{2}\right\rfloor+
\left\lfloor\frac r2\right\rfloor+3+\mathbf1_{r=0}+\mathbf1_{r\ge a-2}.
\tag{2}
\]
If \(a=2k\), the sum of the first two floors equals \(k+1\) for even \(r\) and \(k\) for odd \(r\). If \(a=2k+1\), that sum equals \(k+1\) for every \(r\). Hence (2) gives \(d_a(n_0+r)\le k+5=p\) throughout the interval.

For any integer \(0\le n<m\), choose a nonnegative \(j\) so that \(n+ja\in[n_0,m-1]\), unless \(n\) is already in that interval. Monotonicity along step \(a\) gives \(d_a(n)\le d_a(n+ja)\le p\). At \(n=m=n_0+a\), only \(t=a+2,a+3,a+4\) contribute, with respective counts \(2,k+2,2\), so \(d_a(m)=k+6=p+1\). Thus the multiplicity is exactly \(m\).

**3. Explicit local gaps.** Write \(c=m+2=(a+2)^2\). For even \(a=2k\), formula (1) gives the following contributions, indexed by \(t=a+2,a+3,a+4\):
\[
\begin{array}{c|c|c}
\text{target}&\text{contributions}&\text{total}\\
 c &(1,k+2,3)&k+6=p+1\\
 c+2&(0,k+1,4)&k+5=p.
\end{array}
\]
For odd \(a=2k+1\), the corresponding counts are
\[
\begin{array}{c|c|c}
\text{target}&\text{contributions}&\text{total}\\
 c-1&(1,k+3,2)&k+6=p+1\\
 c&(1,k+2,3)&k+6=p+1\\
 c+1&(0,k+2,3)&k+5=p.
\end{array}
\]
All possible larger or smaller \(t\) contribute zero by the bounds in (1), because \(a\ge7\). This proves the membership and gap claims.

**4. Failure of maximal embedding dimension.** A cofinite additive submonoid is a numerical semigroup. Here \(d_a(n)\ge p+1\) for all sufficiently large \(n\): since \(d_a(m)\ge p+1\) and the three coin denominations have gcd one, every sufficiently large \(n-m\) is representable, and adding any fixed representation of \(n-m\) injects the \(p+1\) representations of \(m\) into those of \(n\). Moreover if \(s,t>0\) lie in \(S_{a,p}\), adjoining any one fixed representation of \(t\) to all representations of \(s\) gives \(d_a(s+t)\ge d_a(s)\ge p+1\). Thus \(S_{a,p}\) is a numerical semigroup.

For a numerical semigroup \(S\) of multiplicity \(m\), its Apéry set contains exactly one element in each residue class modulo \(m\). If the embedding dimension equals \(m\), each of the \(m-1\) nonzero Apéry elements is an indecomposable minimal generator. Consequently, for any positive \(u,v\in S\), the decomposable sum \(u+v\) cannot lie in the Apéry set; hence \(u+v-m\in S\). The explicit choices of \(u,v\) above violate this consequence. Therefore the embedding dimension is strictly below \(m\). QED.

## Verification
The companion standard-library Python program `verify_denumerant.py` implements two independently organized finite evaluation procedures: a three-coin dynamic-programming denumerant and direct enumeration over total coin count in (1). It checks all integer parameters \(7\le a\le100\), all targets below the proposed multiplicity, and the neighboring witnesses and gaps. It prints `PASS 5969 formula-and-DP comparisons and invariant checks, a=7..100`. These are finite diagnostic tests, not proofs for all parameters; the proof above establishes the universal assertions.

## Relationship to prior work
Komatsu and Ying's June 2022 preprint `arXiv:2206.13052` studies the \(p\)-Apéry sets, \(p\)-Frobenius numbers and genus for triples in arithmetic progression, giving general closed forms for \(0\le p\le\lfloor a/2\rfloor\). The present \(p=\lfloor a/2\rfloor+5\) is outside that proven uniform range, and the invariant here is maximal embedding dimension rather than Frobenius number or genus. Komatsu and Ying's July 2022 `arXiv:2207.08962` establishes structural properties of \(p\)-numerical semigroups, including the adjoined-zero convention, but does not supply this counterfamily. The general Apéry criterion for maximal embedding dimension is standard; it is not claimed as new. No exhaustive novelty or independence claim is made.

## Limitations
This is a single parameter ray beyond the published simple \(p\)-Apéry range, not an assertion that \(\lfloor a/2\rfloor+5\) is the first failing parameter. The actual embedding dimension and all higher-parameter behavior remain undetermined here. The originality comparison is limited to the cited, inspected primary work and targeted discoverable literature; unindexed equivalent deductions may exist. No independent mathematical audit has been performed.

## References
1. T. Komatsu and H. Ying, *The \(p\)-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052, first posted 2022-06-27.
2. T. Komatsu and H. Ying, *\(p\)-numerical semigroups with \(p\)-symmetric properties*, arXiv:2207.08962, first posted 2022-07-18.
