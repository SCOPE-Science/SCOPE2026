# Exact closed-factor complexity of five-run binary words

## Finding

A nonempty word is **closed** when it is a single letter or has a nonempty proper factor occurring exactly twice, once as its prefix and once as its suffix; the two occurrences may overlap. Let \(C(w)\) count the **distinct nonempty** closed contiguous factors of \(w\), without counting the empty word. For all integers \(a,b,c,d,e\geq 1\), set
\[
w=0^a1^b0^c1^d0^e,\qquad n=a+b+c+d+e,
\quad u=\min\{a,c\},\quad v=\min\{c,e\},\quad m=\min\{b,d\}.
\]
Then
\[
\boxed{C(w)=n+m(u+v)+\begin{cases}uv-\min\{u,v\},&b=d,\\0,&b\ne d.\end{cases}}
\]
Thus an equality of the two one-run lengths produces a genuine additional term, beyond the ordinary run-pair contribution. Among all binary words of length \(n\) with **exactly five runs**, the maximal number of distinct nonempty closed factors has the sharp asymptotic leading constant
\[
\boxed{\lim_{n\to\infty}\frac{1}{n^2}\max_{\substack{|z|=n\\z\text{ has five runs}}}C(z)=\frac18.}
\]
More precisely, every such \(w\) satisfies \(C(w)\leq n+n^2/8\), and for every integer \(t\geq1\),
\[
w_t=0^{2t}1^t0^{2t}1^t0^{2t},\quad |w_t|=8t,\quad C(w_t)=8t^2+6t.
\]

## Assumptions and scope

The alphabet is the fixed labeled binary alphabet \(\{0,1\}\); a run means a maximal constant block. The five run lengths are positive, with no ordering or equality restrictions. Complementing both letters also preserves the result. Factors are **linear**, not circular; multiplicity of occurrences is irrelevant except to test closedness. The empty word, which is closed by another common convention, is *excluded* throughout. To convert to the convention counting it, add exactly one to each count.

## Proof

**Complete classification by the number of runs of the closed factor.** Put \(M_0=\max\{a,c,e\}\), \(M_1=\max\{b,d\}\), \(h=\min\{a,e\}\), and let \(I\) be one when \(b=d\) and zero otherwise. Every factor has between one and five runs.

A one-run factor is a unary power. Its closed count is \(M_0+M_1\). A two-run factor starts and ends with different letters, and a proper border would have to contain its only letter transition twice; thus no two-run factor is closed.

For a three-run factor, the only possible nonempty border is a unary power. The factor is closed precisely when its first and last run lengths agree. The two zero-ended families have forms \(0^i1^b0^i\) for \(1\leq i\leq u\) and \(0^i1^d0^i\) for \(1\leq i\leq v\). These families overlap in \(\min\{u,v\}\) members exactly when \(b=d\). The one-ended family is \(1^j0^c1^j\) for \(1\leq j\leq m\). Therefore the number of distinct closed three-run factors is \(u+v-I\min\{u,v\}+m\).

Four-run factors have exactly one of the forms \(0^i1^b0^c1^j\) or \(1^i0^c1^d0^j\). Any proper border must cross the corresponding letter transition once at each of the two available transitions of the same direction. The first form is closed exactly when \(1\leq i\leq u\) and \(1\leq j\leq m\), by the border \(0^i1^j\). The second is closed exactly when \(1\leq i\leq m\) and \(1\leq j\leq v\), by the border \(1^i0^j\). Each border occurs at those two transitions only. Consequently there are \(m(u+v)\) distinct closed four-run factors.

Every five-run factor is \(F_{i,j}=0^i1^b0^c1^d0^j\) for \(1\leq i\leq a\) and \(1\leq j\leq e\). If a proper border contains a \(1\), it must span exactly one complete \(1\)-run in each of its two occurrences. This is possible precisely when \(b=d\), \(i\leq c\), and \(j\leq c\): the proper border is \(0^i1^b0^j\), occurring around the two \(1\)-runs only. If there is no such border, a border made entirely of zeros occurs only at the ends precisely when \(i=j>c\). These two cases are disjoint, and the number of closed five-run factors is
\[
Iuv+\max\{0,\min\{a,e\}-c\}.
\]
These cases exhaust all possible factor-run counts and all possible borders. Since the word shapes distinguish the families (apart from the explicitly subtracted three-run overlap), adding them gives
\[
\begin{aligned}
C(w)={}&M_0+M_1+(u+v-I\min\{u,v\}+m)\\
&+m(u+v)+Iuv+\max\{0,\min\{a,e\}-c\}.
\end{aligned}
\]
For any three positive integers \(a,c,e\), direct comparison of their order yields
\[
M_0+\min\{a,c\}+\min\{c,e\}+\max\{0,\min\{a,e\}-c\}=a+c+e.
\]
Also \(M_1+m=b+d\). Substitution proves the exact formula.

**Sharp five-run envelope.** Let \(E=C(w)-n\), put \(x=\max\{u,v\}\), \(y=\min\{u,v\}\), \(s=x+y\), and \(\delta=x-y\). The three zero runs have total length at least \(u+v+\max\{u,v\}=2x+y\).

If \(b=d=m\), then \(n\geq2m+2x+y\), so
\[
E=m(x+y)+xy-y
\leq\frac{s(n-s)}{2}-\frac{\delta(s+\delta)}{4}-y
\leq\frac{n^2}{8}.
\]
If \(b\ne d\), then \(b+d\geq2m+1\), and \(2x+y\geq3s/2\). Thus
\[
E=ms\leq\frac{(n-1)s}{2}-\frac{3s^2}{4}
\leq\frac{(n-1)^2}{12}\leq\frac{n^2}{8}.
\]
This proves the uniform upper bound.

For \(w_t\) the exact formula gives \(C(w_t)=8t^2+6t\). For an arbitrary sufficiently large length \(n\), choose \(t=\lfloor n/8\rfloor\) and append \(n-8t\) zeros to \(w_t\). The result still has exactly five runs and contains all closed factors of \(w_t\). Since \(t=n/8+O(1)\), this yields a lower bound \(n^2/8-O(n)\). Together with the upper bound it proves the asserted limit.

## Verification

The standalone source file `verify_closed_five_runs.py` enumerates all distinct nonempty linear factors, tests the complete-return definition directly by enumerating candidate borders and their occurrence positions, and independently compares that number with the displayed formula. It passed all \(9,592\) cases consisting of every five-tuple of run lengths in \(\{1,2,3,4\}^5\) and every composition of each length from \(5\) through \(18\) into five positive parts. The largest input in the Cartesian block had length \(20\); ten additional sharp-family identities were also checked. This finite computation is a consistency check only. The proofs above establish the unrestricted infinite statements.

## Relationship to prior work

Badkobeh, Fici, and Lipták established the general lower bound of \(n\) distinct nonempty closed factors, characterized the minimum case, and constructed a related five-run word to prove a quadratic lower bound, without providing a count for arbitrary five run lengths. Parshina and Puzynina subsequently established the asymptotic unrestricted maximum \(n^2/6\), using much more flexible finite words. Those theorems give neither the five-run exact formula nor the sharp five-run constant \(1/8\); the present result addresses this natural restricted-complexity problem. No claim is made about an unrestricted optimum or a complete classification of five-run maximizers at each fixed length.

## Limitations

The theorem is restricted to exactly five positive binary runs, counts distinct nonempty linear closed factors, and proves only an asymptotic rather than a fixed-length exact maximum. It does not describe general words with more runs or closed-factor multiplicities. Independent external mathematical review has not been performed.

## References

1. G. Badkobeh, G. Fici, Z. Lipták, *On the Number of Closed Factors in a Word*, first public arXiv version 2013-05-28, arXiv:1305.6395, https://arxiv.org/abs/1305.6395. See the closed-factor definitions, binary CR-poor characterization, and five-run quadratic construction in Section 5.
2. O. Parshina, S. Puzynina, *Finite and infinite closed-rich words*, first public arXiv version 2021-11-01, arXiv:2111.00863, https://arxiv.org/abs/2111.00863. See the unrestricted asymptotic estimate, finite-word upper bound, and Proposition 8.
