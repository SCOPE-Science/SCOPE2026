# Complete gap-run spectrum for three-generator semigroups with shifts three and five

## Finding

For every integer \(a\ge8\), consider the numerical semigroup \(S_a=\langle a,a+3,a+5\rangle\). Let \(B_g(a)\) be the number of **maximal** intervals of exactly \(g\) consecutive positive integers outside \(S_a\). Write \(a=5k+r\) with \(0\le r\le4\). Then

\[
 B_1(a)=\begin{cases}4k+2,&r=0,\\4k,&r=1,\\4k+3,&r=2,3,4,\end{cases}\qquad
 B_2(a)=k+1+\mathbf1_{r=3}.
\]

For every integer \(g\ge3\),

\[
 B_g(a)=\begin{cases}1,&3\le g\le a-1\text{ and }g\equiv a-1\pmod5,\\0,&\text{otherwise}.\end{cases}
\]

Thus each long gap length belongs to a single arithmetic progression and occurs **exactly once**. The length-one and length-two frequencies exhibit a genuine five-class transition.

## Assumptions and scope

Here \(\langle a,a+3,a+5\rangle\) consists of all nonnegative integer combinations of its three generators. Since \(\gcd(a,a+3,a+5)=\gcd(a,3,5)=1\), the complement is finite. The lower bound \(a\ge8\) ensures that all three generators are minimal. A maximal missing interval has semigroup elements immediately before and after it, except that its initial endpoint may follow zero. All counts include every gap, not merely those below a computational cutoff.

## Proof

**1. Fixed-summand offsets.** For any integer \(m\ge0\), let \(D_m=\{3u+5v:u,v\ge0,\ u+v\le m\}\). Every element of \(S_a\) with exactly \(m\) generator summands has the form \(ma+d\), \(d\in D_m\). Directly, \(D_0=\{0\}\) and \(D_1=\{0,3,5\}\). For every \(m\ge2\),

\[
D_m=\{0,3,5,6\}\cup\{8,9,\ldots,5m-4\}\cup\{5m-2,5m\},
\]

where the integer interval is empty if its upper endpoint is below eight. The case \(m=2\) is direct. Inductively, \(D_{m+1}=D_m\cup(3+D_m)\cup(5+D_m)\), and the displayed union merges into the same form with \(m\) replaced by \(m+1\). This proves the offset identity for all \(m\).

**2. Row membership.** Split the nonnegative integers into rows \(R_m=[ma,(m+1)a-1]\). Every row begins with a representable integer, so no missing interval crosses a row boundary. Put \(a=5k+r\). For \(0\le m\le k+3\), an element in row \(m\) cannot arise from \(m-2\) or fewer summands: \(5(m-2)<2a\), whenever \(m\ge2\), and the maximum value at \(m-2\) summands is \((m-2)(a+5)\). Therefore, for \(0\le t<a\), the exact membership test in these rows is

\[
ma+t\in S_a\quad\Longleftrightarrow\quad t\in D_m\ \text{ or }\ (m\ge1\text{ and }a+t\in D_{m-1}).
\]

For \(m\ge k+4\), \(D_m\) contains every offset \(t\in\{0,3,5,6\}\cup[8,a-1]\). The remaining offsets \(t\in\{1,2,4,7\}\cap[0,a-1]\) are covered by \(a+t\in[8,5(m-1)-4]\subseteq D_{m-1}\), because \(a+7\le5k+11\le5(m-1)-4\). Hence all later rows are full.

**3. Exact finite row patterns, uniform in the parameter.** In each row identify a missing block by the pair \((t,\ell)\), meaning offsets \(t,t+1,\ldots,t+\ell-1\). The offset identity in step 1 and membership test in step 2 give the following complete patterns for \(k\ge2\):

* In row \(m=0\), there is \((1,a-1)\).
* In row \(m=1\), there are \((1,2),(4,1),(6,a-6)\).
* For every \(2\le m\le k\), there are \((1,2),(4,1),(7,1),(5m-3,1),(5m-1,1)\), plus \((5m+1,a-5m-1)\) if its length is positive. Repeated descriptions of the **same** block at \(m=2\) are counted only once: \((7,1)=(5m-3,1)\).
* In row \(m=k+1\), there are \((1,2),(4,1),(7,1)\), plus \((5k+2,1)\) when \(r=3\) or \(r=4\).
* In row \(m=k+2\), the blocks are \((1,1),(7,1)\) for \(r=1\); \((1,1),(4,1),(7,1)\) for \(r=3\); and \((2,1),(4,1),(7,1)\) otherwise.
* In row \(m=k+3\), there is no gap for \(r=1\), only \((4,1)\) for \(r=3\), and only \((7,1)\) otherwise.

Each pattern follows by taking the complement in \([0,a-1]\) of the two explicit offset sets in step 2. No unbounded enumeration is needed. For \(k=1\), allowed values are just \(a=8,9\); substituting \(D_0,\ldots,D_4\) gives the same claimed aggregate counts (the row \(m=k\) pattern is shortened because its initial and terminal portions overlap).

**4. Aggregation.** The long block from row \(m\), for \(0\le m\le k-1\), has length \(a-1-5m\); when \(r=4\), row \(m=k\) adds a single block of length three. When \(r=2\) or \(r=3\), that row instead adds respectively one singleton or one doubleton. All other blocks have length one or two. Counting the blocks in the row patterns yields exactly the displayed expressions for \(B_1\) and \(B_2\). Since rows do not join across representable row-start elements, this completes the proof for every \(a\ge8\).

## Verification

The accompanying `CHECK.py` independently constructs semigroup membership via forward dynamic programming, checks full gap histograms for every \(8\le a\le300\), checks the exact offset identity for \(0\le m\le69\), and compares the claimed row patterns with the summand-offset criterion for every \(10\le a\le300\). All checks completed successfully. This finite computation is a reproducibility check, not a substitute for the all-parameter argument above.

## Relationship to prior work

Shor's 2021 work determines *residue equidistribution of individual gaps* for specified semigroups, not the distribution of lengths of maximal consecutive missing intervals. Liu–Xin–Ye–Yin (arXiv:2306.03459; earliest public version 6 June 2023) study Frobenius numbers and genus of broad generator families, different invariants from the complete run spectrum here. Related previously reported results address two-generated semigroups or isolated gaps of the different progression \(\langle a,a+2,a+4\rangle\), so do not imply the displayed three-generator spectrum. The gap-run claim remains subject to the usual possibility of an unindexed equivalent identity in older semigroup literature.

## Limitations

The theorem is restricted to the natural family \(\langle a,a+3,a+5\rangle\) with \(a\ge8\); it does not classify arbitrary generator shifts. The checker's upper bound is finite, whereas the mathematical proof is all-parameter. No assertion of independent verification or publication priority is made.

## References

1. Caleb M. Shor, *On evenly distributed sets of gaps of numerical semigroups*, arXiv:2101.01760, first submitted 5 January 2021, https://arxiv.org/abs/2101.01760 (sections 3 and 5).
2. Feihu Liu, Guoce Xin, Suting Ye, and Jingjing Yin, *On the Frobenius Number and Genus of a Collection of Semigroups Generalizing Repunit Numerical Semigroups*, arXiv:2306.03459, first submitted 6 June 2023, https://arxiv.org/html/2306.03459v4 (the 2025 version was used to inspect content; first-source date is the 2023 v1 date).
3. Related published mathematical finding, *Exact run-length frequencies for binary semigroups with \(a=dt+1\) and \(b=a+d\)*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-exact-run-length-frequencies-for-binary-semigroups-with-a-dt-1-a--584c998005ae (two-generator case, comparison from available record summary).
4. Related published mathematical finding, *Isolated gaps of the three-term progression \(\langle a,a+2,a+4\rangle\)*, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-isolated-gaps-of-the-three-term-progression-langle-a-a-2-a-4-ran--1a98ce07f8f0 (different generators and only isolated gaps; comparison from available record summary).
