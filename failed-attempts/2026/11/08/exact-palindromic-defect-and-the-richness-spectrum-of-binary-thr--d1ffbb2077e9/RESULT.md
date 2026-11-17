# Exact palindromic defect and the richness spectrum of binary three-marker words

## Finding

For a finite binary word \(w\), let \(\operatorname{Pal}(w)\) be its set of **distinct nonempty contiguous palindromic factors**, and define its palindromic defect by
\[
D(w)=|w|-|\operatorname{Pal}(w)|.
\]
A word is *rich* precisely when \(D(w)=0\). For all \(a,b,c,d\in\mathbb Z_{\ge0}\), put
\[
w=0^a1\,0^b1\,0^c1\,0^d.\]
The exact defect is
\[
\boxed{D(w)=\begin{cases}0,&b=c,\\[2pt]\max\{0,\min(a,d)-\max(b,c)\},&b\ne c.\end{cases}}
\]
Consequently, a binary word with exactly three ones is non-rich if and only if \(b\ne c\) and \(\min(a,d)>\max(b,c)\). Every word containing at most two ones is rich. The inclusion-minimal non-rich binary factors containing three ones are exactly
\[
0^{m+1}1\,0^b1\,0^c1\,0^{m+1},\qquad m\ge1,\quad \max(b,c)=m,\quad b\ne c.
\]

Let \(N_r(n)\) be the number of *indexed* length-\(n\) binary words with exactly three ones and defect \(r\), for \(r\ge1\). For each fixed \(r\ge1\),
\[
\boxed{\sum_{n\ge3}N_r(n)z^n=
\frac{2z^{6+2r}(1+z)}{(1-z)(1-z^3)(1-z^4)}.}
\]
Thus all defect multiplicities, including the zero-defect count \(\binom n3-\sum_{r\ge1}N_r(n)\), are explicit. The joint generating function is
\[
\boxed{\sum_{n\ge3}\sum_{|w|=n,\,|w|_1=3} z^nu^{D(w)}=
\frac{z^3}{(1-z)^4}+\frac{2z^8(1+z)(u-1)}{(1-z)(1-z^2)(1-z^3)(1-z^4)(1-uz^2)}.}
\]
For \(n\ge8\), the maximal defect is \(\lfloor(n-6)/2\rfloor\); for \(3\le n\le7\) it is zero.

For \(W_n\) uniform among the \(\binom n3\) words of length \(n\) with exactly three ones, \(D(W_n)/n\) converges in distribution to \(X\) with an atom \(\Pr(X=0)=5/6\) and continuous density
\[
f_X(t)=(1-2t)^2,\qquad 0<t<1/2.
\]
In particular, \(\mathbb E X=1/48\) and \(\operatorname{Var}(X)=43/11520\). The limiting probability of non-richness is \(1/6\).

## Assumptions and scope

Words are finite, linear, indexed binary strings, not necklaces, and neither rotations nor reversal are identified. Exponents \(a,b,c,d\) count maximal consecutive zeros, which may be zero. Palindromic factors are *contiguous* and counted once per distinct literal string; repeated occurrences and the empty word are not counted. The result covers precisely Hamming weight three for the full defect spectrum and gives richness for lower weights. Lengths and gap parameters are unrestricted nonnegative integers within those domains. The generating functions are identities of formal power series.

## Proof

**1. Palindromes by marker count.** Write \(M=\max(a,b,c,d)\) and \(T=\max\{\min(a,b),\min(b,c),\min(c,d)\}\). The palindromes containing no ones are exactly \(0,0^2,\ldots,0^M\), hence \(M\) distinct words. Those containing one one are exactly \(0^j1\,0^j\) for \(0\le j\le T\), hence \(T+1\). Two-one palindromes must surround the first two or last two ones. If \(b\ne c\), their central zero-run lengths distinguish the two classes, and their number is \(2+\min(a,c)+\min(b,d)\). If \(b=c\), the two classes overlap and their union has size \(1+\max\{\min(a,c),\min(b,d)\}\). A three-one palindrome exists precisely when \(b=c\), and then there are \(1+\min(a,d)\) of them. These four categories are exhaustive and disjoint.

**2. Defect simplification for equal inner gaps.** Suppose \(b=c=t\). Then \(T=t\), \(\max\{\min(a,t),\min(t,d)\}=\min(t,\max(a,d))\), and
\[
|\operatorname{Pal}(w)|=\max(t,a,d)+t+\min(t,\max(a,d))+\min(a,d)+3
=a+2t+d+3=|w|.
\]
Thus \(D(w)=0\).

**3. Defect simplification for unequal inner gaps.** Reversal interchanges \((a,b,c,d)\) with \((d,c,b,a)\), preserves defect, and leaves the proposed formula invariant. Assume \(b<c\). Directly from the four categories,
\[
D(w)=\max(a,c)+\max(b,d)-\max(a,c,d)-\max(b,\min(c,d)).
\]
If \(d<b\), then \(d<b<c\) makes both differences cancel, giving zero. If \(d\ge b\), then \(\min(c,d)\ge b\), and the expression becomes
\[
\min(\max(a,c),d)-\min(c,d)
=\max\{0,\min(a,d)-c\}.
\]
This establishes the claimed formula for \(b<c\), and reversal covers \(b>c\). The zero-defect criterion follows immediately.

**4. Lower weights and minimal obstructions.** With two ones \(0^a1\,0^b1\,0^c\), put \(v=\max(a,c)\). The palindromes by marker count total
\[
\max(b,v)+1+\min(b,v)+1+\min(a,c)=a+b+c+2,
\]
so all such words are rich. Words of weight zero or one are also rich by direct zero-run and one-marker counting. For a non-rich three-one word, a proper factor retaining all three ones only trims one or both outer zero runs. It is minimal non-rich precisely when trimming either side makes the defect vanish, which by the formula is \(a=d=\max(b,c)+1\). Every factor losing a one is rich by the lower-weight result. This proves the stated minimal-factor family.

**5. Exact defect enumerator.** Fix \(r\ge1\). Write \(m=\max(b,c)\ge1\), \(\ell=\min(b,c)\) with \(0\le\ell<m\). The inner gaps have two distinct orientations. Defect exactly \(r\) means \(a=m+r+x\) and \(d=m+r+y\), for \(x,y\ge0\) with \(\min(x,y)=0\). Their generating series is
\[
\sum_{\min(x,y)=0}z^{x+y}=\frac{1+z}{1-z},\qquad
\sum_{m\ge1}\sum_{0\le\ell<m}z^{3m+\ell}
=\frac{z^3}{(1-z^3)(1-z^4)}.
\]
There are three marked ones, adding \(z^3\), and the outer baseline runs contribute \(z^{2r}\). Multiplication proves the formula for \(N_r(n)\). All weight-three words have series \(z^3/(1-z)^4\); replacing the weight of each positive-defect word by \(u^r\) instead of one and summing the geometric series \(\sum_{r\ge1}(u^r-1)z^{2r}\) proves the bivariate formula. The smallest length with defect \(r\) is \(6+2r\) (take \(m=1\), \(\ell=x=y=0\)), giving the maximum-defect claim.

**6. Limiting law.** Put \(h_k=[z^k](1+z)/((1-z)(1-z^3)(1-z^4))\), taking \(h_k=0\) for \(k<0\). The unique triple pole at one yields \(h_k=k^2/12+O(k+1)\), with remaining unit-circle poles contributing at most bounded periodic terms (the numerator cancels the pole at minus one). Hence, uniformly for \(1\le r\le\lfloor(n-6)/2\rfloor\),
\[
N_r(n)=\frac{(n-6-2r)^2}{6}+O(n).
\]
As \(\binom n3=n^3/6+O(n^2)\), the positive part of \(D(W_n)/n\) converges by Riemann sums to density \((1-2t)^2\) on \((0,1/2)\). Its mass is \(1/6\); the remaining mass \(5/6\) is at zero. Direct integration gives \(\mathbb E X=1/48\), \(\mathbb E X^2=1/240\), and variance \(43/11520\). This completes the proof.

## Verification

Run `python3 verify.py` with Python 3 and no additional packages. The checker enumerates independently all distinct palindromic contiguous factors of every indexed weight-three word of lengths 3 through 34, compares defects and all exact defect-layer counts, verifies the algebraic formula on \(18^4\) gap quadruples, and independently integrates the stated limit-density moments over rational numbers. The observed result was `VERIFY_OK 52360 direct words; 18^4 algebra tuples; rational moments`. The infinite result relies on the preceding symbolic proof, not this finite check.

## Relationship to prior work

Glen, Justin, Widmer and Zamboni introduced the systematic study of palindromically rich words and the complete-return characterization; their arXiv posting is dated 2008-01-10 [1]. Bucci, De Luca, Glen and Zamboni gave an alternative richness characterization in terms of longest palindromic prefixes and suffixes [2]. Vesti explicitly listed the shortest non-rich binary examples and gave unrestricted rich-word bounds and tables [3]; those length-eight examples are exactly the first two three-one obstructions in this theorem, with their complements contributing the other two unrestricted binary examples. These foundational results are credited and **not** claimed as new. The new statement is the all-length, fixed-content exact defect formula, every positive-defect layer, and its conditional limiting distribution. General definitions and universal richness criteria alone do not state these finite-content enumerators. A separate existing classification of privileged weight-three words concerns a different recursive palindrome property and does not imply the number of distinct palindromic factors or the defect spectrum.

## Limitations

The result does not classify weight-four or higher binary words, arbitrary alphabets, cyclic factors, multiplicity-weighted palindrome counts, or infinite-word richness. Its probabilistic law is conditional on precisely three ones and does not describe random words with independent fair bits. The priority comparison has a remaining risk from unindexed specializations of general richness results; independent audit and external mathematical validation have not been performed.

## References

[1] A. Glen, J. Justin, S. Widmer, and L. Q. Zamboni, *Palindromic Richness*, arXiv:0801.1656 (initial posting 2008-01-10), https://arxiv.org/abs/0801.1656 .

[2] M. Bucci, A. De Luca, A. Glen, and L. Q. Zamboni, *A New Characteristic Property of Rich Words*, arXiv:0807.2303 (2008), https://arxiv.org/abs/0807.2303 .

[3] J. Vesti, *Extensions of Rich Words*, arXiv:1312.4350 (initial posting 2013-12-16), Sections 3–4, https://arxiv.org/abs/1312.4350 .
