# Exact one-step tortoise complexity of nontrivial two-run binary periods

## Finding
Let \(a,b\ge 2\) and let \(\mathbf x_{a,b}=(0^a1^b)^\omega\), of least period \(p=a+b\). For a finite binary word \(w\), define \(T(w)\) by deleting its leftmost occurrence of \(1\), if one exists, and appending \(1\); let \(T(0^n)=0^n\). Let \(c_{a,b}(n)\) count **distinct image words** \(T(w)\) as \(w\) ranges over the distinct contiguous length-\(n\) factors of \(\mathbf x_{a,b}\). Then, for every \(n\ge1\),
\[
 c_{a,b}(n)=\begin{cases}
 2,&n=1,\\
 \min(n,a)+\min(n,b)-1,&2\le n\le a+b,\\
 a+b,&n\ge a+b+1.
 \end{cases}
\]

For each \(2\le n\le a+b\), **exactly one** unordered pair of distinct length-\(n\) factors has the same image under \(T\), and there is no fiber of size three or larger. The sole collision pair is
\[
 \begin{cases}
 \{0^{n-1}1,\ 10^{n-1}\},&2\le n\le a+1,\\
 \{0^a1^{n-a},\ 10^a1^{n-a-1}\},&a+2\le n\le a+b.
 \end{cases}
\]
The one-step map is injective on this factor set for every \(n\ge a+b+1\); this cutoff is sharp.

## Scope and conventions
The infinite word is one-sided but all cyclic phases occur, so the factor language is independent of the starting phase. Factors are contiguous, images are counted as distinct labelled words rather than occurrences, and the map moves exactly **one** leftmost \(1\) per step. The theorem assumes both run lengths at least two. It does not claim an all-iterate formula, any result for an arbitrary multi-run period, or originality for the one-run boundary cases \(a=1\) or \(b=1\). The latter are already covered by published rational-Christoffel tortoise theorems.

## Proof
Every binary word with \(m\) ones has a unique zero-gap representation
\[
 w=0^{z_0}1\,0^{z_1}1\cdots1\,0^{z_m},\qquad z_i\ge0.
\]
If \(m\ge1\), moving the first one to the end gives
\[
 T(w)=0^{z_0+z_1}1\,0^{z_2}1\cdots0^{z_m}1.
\]
Thus the number \(m\) of ones is preserved. Equality of two images with \(m\ge2\) fixes \(z_0+z_1\), all \(z_2,\ldots,z_m\), and \(m\). For a factor of \((0^a1^b)^\omega\), the first two ones are either consecutive (\(z_1=0\)) or separated by a complete zero-run (\(z_1=a\)). If their gaps \(z_1\) agree, all gaps agree, so the factors coincide. Otherwise \(0\le z_0\le a\), and equality of the first image gap forces the two initial gap pairs to be \((a,0)\) and \((0,a)\). These correspond respectively to a factor beginning at the start of a zero-run and to a factor beginning at the last one of a one-run.

For the remaining image gaps to agree, both factors must finish within the same relevant one-run: their common trailing zero gaps must all vanish. Consequently the only possible distinct multi-one collision is
\[
 u=0^a1^m,\qquad v=10^a1^{m-1},\qquad 2\le m\le b,
\]
with common length \(n=a+m\). Both factors occur: \(u\) begins at the start of the zero-run and \(v\) begins at the last one before that zero-run. If an additional one is included, the following complete zero-run appears in different image-gap positions; if only zeros extend the factor, the terminal zero gaps differ. Hence these are exactly the multi-one collisions, at lengths \(a+2,\ldots,a+b\).

If \(m=1\), the image is always \(0^{n-1}1\). Because \(b\ge2\), a factor containing only one \(1\) cannot contain zeros both before and after it: any one is adjacent to another one within its run on at least one side. Thus the only possible distinct single-one factors are \(0^{n-1}1\) and \(10^{n-1}\), and both occur exactly for \(2\le n\le a+1\). A zero-only factor has its own image and cannot collide with a positive-one factor.

For comparison, the ordinary length-\(n\) factor complexity of the two-run primitive period is
\[
 p_{\mathbf x}(n)=\min(n,a)+\min(n,b).
\]
Indeed, among the \(a+b\) starting phases, all duplicates are due to homogeneous windows: \(0^n\) contributes \(\max(a-n,0)\) redundant starts, and \(1^n\) contributes \(\max(b-n,0)\); the remaining factors are distinguished by the first letter and position of their first change. This also shows all \(a+b\) factors are distinct at and beyond length \(a+b\). We have classified exactly one double fiber at every \(2\le n\le a+b\), none at \(n=1\), and none at \(n\ge a+b+1\). Subtracting its single excess member from the ordinary factor count proves the formula and sharpness. \(\square\)

## Verification
The accompanying standalone `verify.py` checks the operator both by direct first-one deletion and by the zero-gap recurrence, enumerating all \(a+b\) cyclic starting phases for many pairs \(a,b\ge2\) and every tested length through several periods. It checks the complete image count, exact collision-pair identities, and absence of other collisions. These finite experiments corroborate the all-parameter collision argument above, not replace it.

## Relationship to previous results and limitations
Campbell and Rampersad, *Subword enumeration up to stack-sorting equivalence* (arXiv:2604.25811v2, October 5, 2026), develop the tortoise-factor-complexity invariant and provide general bounded-gap comparisons and spectra for other words. Defant and Kravitz, *Stack-sorting for words* (arXiv:1809.09158), introduce the underlying map. Exact rational-Christoffel one-step complexity was published on October 25, 2026, and the complete iterated Christoffel spectrum on November 2, 2026. They already imply the \(a=1\) or \(b=1\) boundary cases; these are **excluded** rather than asserted anew here. For \(a,b\ge2\), the period has both \(00\) and \(11\), so it cannot be Christoffel/balanced (its length-two factor weights differ by two). The surviving classification therefore does not follow as a rational-Christoffel special case. An unindexed separate enumeration of two-block periodic factors could still affect historical priority.

The result supplies an exact all-length classification of the one-step fibers, not the higher-iterate distributions when both run lengths exceed one. It is not a claim about arbitrary stack-sorting transformations, and no finite experiment proves the infinite-parameter statement.

## References
- J. M. Campbell and N. Rampersad, *Subword enumeration up to stack-sorting equivalence*, arXiv:2604.25811v2 (2026), https://arxiv.org/abs/2604.25811.
- C. Defant and N. Kravitz, *Stack-sorting for words*, arXiv:1809.09158 (2018), https://arxiv.org/abs/1809.09158.
- *Exact tortoise-image complexity of periodic Christoffel words* (October 25, 2026), https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-tortoise-image-complexity-of-periodic-christoffel-words--0a43126d45d9/RESULT.md.
- *Exact iterated tortoise complexity of periodic Christoffel words* (November 2, 2026), https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-iterated-tortoise-complexity-of-periodic-christoffel-words--068034d6a525/RESULT.md.
