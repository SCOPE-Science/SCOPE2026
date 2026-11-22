# Sharp joint nilpotency and multinomial extremizers for finite-chain endomorphisms

## Finding

Let \(n\geq1\) and \(k\geq1\). For the chain \(C_n=\{0,1,\ldots,n\}\), take any \(k\) zero-preserving, nondecreasing self-maps \(f_1,\ldots,f_k\) that are nilpotent under composition, with exact nilpotency indices \(a_i=\nu(f_i)\). Set \(h=f_1\vee\cdots\vee f_k\), taking the maximum pointwise, and put

\[
N=1+\sum_{i=1}^{k}(a_i-1).
\]

Then

\[
\nu(h)\leq\min\{n,N\},
\]

and every composition word of length \(N\) in \(f_1,\ldots,f_k\) is the zero map. In fact, the least word length annihilating all products equals \(\nu(h)\). When \(n\geq N\), the bound \(N\) is attained by an explicit family for every tuple of positive indices \((a_1,\ldots,a_k)\).

On the smallest chain that permits attaining this bound, namely \(C_N\), the number of *ordered* tuples of maps with exact indices \((a_1,\ldots,a_k)\) and \(\nu(h)=N\) is exactly

\[
\boxed{\frac{(N-1)!}{\prod_{i=1}^{k}(a_i-1)!}}.
\]

These extremal tuples are in explicit bijection with words of length \(N-1\) in which label \(i\) appears exactly \(a_i-1\) times. This includes zero maps (index one) and the single-generator case.

## Assumptions and scope

The chain has \(n+1\) elements and addition of maps is pointwise maximum; multiplication is composition \((f\circ g)(x)=f(g(x))\). All maps preserve \(0\). The zero map sends every point to \(0\). For a nilpotent map \(f\), \(\nu(f)\) is the least positive integer \(a\) for which \(f^{\circ a}\) is the zero map. Every map here is monotone, so it is a join-semilattice endomorphism; the maps need not commute under composition. The exact extremal census is asserted for \(n=N\), not for arbitrary larger chain size; the construction exists on every \(n\ge N\), but no larger-chain count is asserted.

## Proof

**1. Strict decrease and height increments.** A monotone zero-preserving self-map is nilpotent if and only if \(f(x)<x\) for each \(x>0\). Indeed, a positive fixed point prevents nilpotence; if \(f(x)>x\) then monotonicity implies no power of \(x\) reaches zero. Conversely strict descent reaches zero in at most \(n\) iterations.

For such \(f\), define \(d_f(x)=\min\{r\geq0:f^{\circ r}(x)=0\}\). Its exact index is \(a=d_f(n)\), since \(n\) is the largest element and \(f\) is nondecreasing. For each positive \(x\),

\[
d_f(f(x))=d_f(x)-1,\qquad 0\leq d_f(x)-d_f(x-1)\leq1.
\]

The first identity follows from the minimal hitting time; the lower bound in the second follows from monotonicity; the upper bound follows from \(f(x)\leq x-1\) and monotonicity of the height function. In particular \(d_f(1)=1\).

**2. A potential bound.** Define \(D(x)=\sum_i d_{f_i}(x)\). Since all \(f_i\) strictly decrease positive inputs, so does their maximum \(h\). Given positive \(x\), select a label \(j\) with \(h(x)=f_j(x)\). Then the \(j\)-th height falls by one, and all other heights do not increase, so \(D(h(x))\leq D(x)-1\). If \(x>0\) and \(h(x)=0\), then *every* \(f_i(x)=0\); hence every \(d_{f_i}(x)=1\), and the last step drops the potential by exactly \(k\). Starting at \(D(n)=\sum_i a_i\), if \(h\) requires \(L\) steps to send \(n\) to zero, then

\[
\sum_i a_i\geq (L-1)+k,
\]

whence \(L\leq N\). Since \(h(x)<x\), also \(L\leq n\). This proves the displayed bound and identifies \(L=\nu(h)\).

**3. Arbitrary products.** Because the maps preserve pointwise maxima and composition distributes over this operation on both sides, the \(r\)-th compositional power \(h^{\circ r}\) is the pointwise maximum of the \(k^r\) composition words of length \(r\) in the generators. Every such word takes values \(\geq0\), so \(h^{\circ r}=0\) precisely when *all* length-\(r\) words vanish. Thus the least annihilating word length equals \(\nu(h)\), and \(N\) is an upper bound.

**4. All sharp constructions.** Suppose \(n=N\). Fix any coloring \(c_2,\ldots,c_N\) of the positions \(2,\ldots,N\) with exactly \(a_i-1\) occurrences of color \(i\). For each \(i\) prescribe a height profile

\[
d_i(0)=0,\qquad d_i(x)=1+\#\{t:2\leq t\leq x,\ c_t=i\}\quad (1\leq x\leq N).
\]

Set \(f_i(0)=0\) and, for positive \(x\),

\[
f_i(x)=\max\{0\leq y<x:d_i(y)=d_i(x)-1\}.
\]

The set is nonempty: at a height jump, \(y=x-1\) qualifies; on a plateau, the position before the most recent jump (or \(0\) for height one) qualifies. The resulting \(f_i\) is nondecreasing: it stays constant on height plateaus and takes the new value \(x-1\) at each jump. It always satisfies \(f_i(x)<x\). By induction on \(x\), its actual iteration-height profile is the prescribed \(d_i\), so its exact index is \(a_i\). Whenever \(c_x=i\), the formula gives \(f_i(x)=x-1\). Consequently \(h(x)=x-1\) for every \(x>0\), and \(\nu(h)=N\).

If \(n>N\), retain these maps on \(0,\ldots,N\) and set \(f_i(x)=f_i(N)\) for \(x>N\). Monotonicity, strict descent and the exact indices persist, and their join still has index \(N\).

**5. Rigidity and the multinomial census.** Conversely assume \(n=N\) and \(\nu(h)=N\). A strictly decreasing trajectory of \(N\) steps from \(N\) to zero must follow \(N,N-1,\ldots,0\); hence \(h(x)=x-1\) for all positive \(x\). At each \(x=2,\ldots,N\), some \(i\) must satisfy \(f_i(x)=x-1\), implying \(d_{f_i}(x)=d_{f_i}(x-1)+1\). Across all labels and positions, the number of height jumps is exactly

\[
\sum_{i=1}^{k}\big(d_{f_i}(N)-d_{f_i}(1)\big)=\sum_i(a_i-1)=N-1.
\]

There are \(N-1\) positions, each forcing at least one jump. Therefore exactly *one* height jumps at each position. Its label is a unique coloring with the prescribed color frequencies.

The coloring determines each map uniquely: at a color-\(i\) jump at \(x\), one has \(f_i(x)=x-1\); while on a height plateau following the last color-\(i\) jump at \(y\), monotonicity gives \(f_i(x)\geq f_i(y)=y-1\), and the iteration-height identity forces \(f_i(x)\leq y-1\). Before any color-\(i\) jump its height is one and its image is zero. Thus the maps are exactly the constructions of Step 4 and are uniquely indexed by the color words. Counting these words proves the multinomial formula.

**6. Noncommutative sharp example.** On \(C_3\), the maps

\[
f=(0,0,1,1),\qquad g=(0,0,0,2)
\]

both have index two, and their maximum is \((0,0,1,2)\), with index three. Yet \(f\circ g=(0,0,0,1)\) while \(g\circ f=0\). Thus the sharp theorem genuinely applies to noncommuting generators, not merely to the standard commuting-nilpotent sum bound.

## Verification

The standalone Python file `VERIFY.py` enumerates every nilpotent nondecreasing zero-preserving map on \(C_n\), computes exact composition indices, tests all ordered \(k\)-tuples for \(k=2\) through \(n=8\), \(k=3\) through \(n=5\), and \(k=4\) at \(n=4\), then independently checks the minimal-chain extremal count and coloring construction in every tested index stratum. The largest pair test enumerates \(2{,}044{,}900\) ordered pairs. Run with `python VERIFY.py` using standard Python 3; its final line is `JOIN_NILPOTENCY_AND_MULTINOMIAL_CHECKS_PASSED`. These finite enumerations are corroboration, not a proof of the universal result, which is supplied above.

## Relationship to prior work

Trendafilov and Vladeva (2013), Proposition 2.1 and Theorem 3.3, establish the nilpotent-subsemiring structure and Catalan counts for individual nilpotents; these facts are prior work. Gusev and Volkov (arXiv first public 2023-12-04) study finite identity bases for the same endomorphism-semiring framework, not the sharp joint composition bound or extremal generator census. Trendafilov's 2013 public arXiv preprint of the 2014 simplex study was inspected in full: it treats structural ideals and nilpotent types, rather than the all-arity specified-indices extremal enumeration. The 2024 partial-transformation product-factorization paper uses a different monoid and question. The sharp noncommuting bound and exact multinomial equality classification are the claimed refinements, not the pre-existing closure or individual Catalan count.

## Limitations

The multinomial census applies on the minimal chain \(C_N\); it is *not* a count of extremal tuples on a larger chain. The theorem concerns zero-preserving monotone maps, not arbitrary transformations or sums in an arbitrary semiring. A standard nilpotent-sum bound for *commuting* elements in general semirings is distinct from this noncommuting statement; the displayed sharp example is noncommutative. Historical priority beyond the inspected literature is not independently certified. The finite checks do not establish the theorem for unbounded \(n\) or \(k\).

## References

1. I. Trendafilov and D. Vladeva, *Nilpotent Elements of the Endomorphism Semiring of a Finite Chain and Catalan Numbers*, Mathematics and Education in Mathematics, 2013, pp. 265–271. https://www.math.bas.bg/~smb/2013_PK/tom_2013/pdf/265-271.pdf
2. S. V. Gusev and M. V. Volkov, *The Finite Basis Problem for Endomorphism Semirings of Finite Chains*, arXiv:2312.01770, first posted 2023-12-04. https://arxiv.org/abs/2312.01770
3. I. Trendafilov, *Simplices in the Endomorphism Semiring of a Finite Chain*, arXiv:1311.5548, first public preprint 2013-11-21; journal version 2014, DOI:10.1155/2014/263605. https://arxiv.org/abs/1311.5548
4. A. Kachalla and B. A. Madu, *Expressing Partial Order-Preserving Transformations as Products of Nilpotents*, International Journal of Development Mathematics, 1(3), 2024, pp. 112–125. https://doi.org/10.62054/ijdm/0103.08
