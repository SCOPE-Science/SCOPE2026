# Exact phase and factor counts of higher Abelian powers in two-run periodic binary words

## Finding

Let \(a,b\ge1\), \(p=a+b\), and \(X=(0^a1^b)^\omega\). An *Abelian \(q\)-power of block length \(k\)* is a length-\(qk\) factor admitting a specified decomposition into \(q\) adjacent blocks, each of length \(k\), whose numbers of zeros and ones coincide. The integers \(q\ge3\) and \(k\ge1\) are arbitrary.

Let \(N_{a,b,q}(k)\) denote the number of admissible start positions among the \(p\) residues modulo \(p\); let \(D_{a,b,q}(k)\) count *distinct* length-\(qk\) factors that are Abelian \(q\)-powers with block length \(k\).

Set \(r=k\bmod p\). The complete phase count is

\[
N_{a,b,q}(k)=\begin{cases}
p,&r=0,\\
2,&r\ne0,\ 2\min(r,p-r)=p,\ a,b\text{ both even},\\
0,&r\ne0,\ 2\min(r,p-r)=p,\ \text{otherwise},\\
\max\{0,a-qs+1\}+\max\{0,b-qs+1\},&2s<p,\ s=\min(r,p-r).
\end{cases}
\]

The distinct-factor count is

\[
D_{a,b,q}(k)=\begin{cases}
\mathbf1_{a\ge qk}+\mathbf1_{b\ge qk},&qk<p,\\
N_{a,b,q}(k),&qk\ge p.
\end{cases}
\]

The exceptional half-period case yields exactly two admissible phases when both run lengths are even, despite the impossibility of \(q\) consecutive monochromatic half-period blocks. For example \(a=4,b=8,q=3,k=6\) gives \(p=12\) and \(N=D=2\). At \(k=13\) for the same parameters, \(N=D=8\).

## Assumptions and scope

All words use the binary alphabet \(\{0,1\}\). The infinite word is indexed from zero; the choice of a starting phase is considered modulo the full period \(p\). An Abelian power means equality of *Parikh vectors*, not literal equality of constituent blocks, and the same length \(k\) is imposed on every constituent. The theorem covers every \(a,b\ge1\), every \(q\ge3\), and every \(k\ge1\), with no balancedness or coprimality assumptions. The separate number of positions and number of distinct factors are part of the same classification.

## Proof

**Reduction modulo the period.** Write \(k=mp+r\) with \(0\le r<p\). Each length-\(k\) block contains \(m\) full periods plus a cyclic window of length \(r\). If \(f_r(i)\) counts ones in that window, its total ones count is \(mb+f_r(i)\). Thus Abelian equivalence of the \(q\) consecutive blocks starting at \(i\) is precisely

\[
f_r(i)=f_r(i+r)=\cdots=f_r(i+(q-1)r).
\]

If \(r=0\), every starting phase works, and \(N=p\).

**Reduction to the shorter arc.** For \(0<r<p\), complementary cyclic arcs give \(f_{p-r}(i)=b-f_r(i-r)\). Reversing the \(q\) terms in the equality above shows that the number of successful starting phases for step \(r\) equals that for step \(p-r\). It is therefore enough to use \(s=\min(r,p-r)\le p/2\).

**Strictly short arcs.** Suppose \(0<s<p/2\). The values of \(f_s\), as the window moves once around the cyclic word, form a plateau–slope–plateau–slope profile. Its minimum and maximum are

\[
\min_i f_s(i)=\max(0,s-a),\qquad \max_i f_s(i)=\min(s,b).
\]

Every value strictly between these extremes occurs at exactly two phases: once when the window enters the unique run of ones and once when it leaves. The three arguments \(i,i+s,i+2s\) are distinct modulo \(p\) because \(0<s<p/2\). Consequently, equality of at least three such window counts is impossible at an interior value.

If \(f_s\) attains the lower extreme \(s-a>0\), then its window contains the entire nonempty zero run. Two consecutive length-\(s\) windows are disjoint in the cyclic order and cannot each contain that run. The upper extreme \(b<s\) is similarly impossible at two consecutive windows, since each would have to contain the entire one run. Hence the only possible common values for \(q\ge3\) are \(0\), realized when all \(qs\) letters of the consecutive windows are zero, and \(s\), realized when all are one. A run of \(a\) consecutive zeros contains exactly \(\max(0,a-qs+1)\) starting positions of a zero-only block of length \(qs\); the one run contributes \(\max(0,b-qs+1)\). Their sum proves the asserted formula for \(2s<p\).

**Half-period arcs.** If \(s=p/2\), the step has order two modulo \(p\), so \(q\ge3\) consecutive window counts are all equal if and only if the two complementary half-period windows have equal numbers of ones. This is equivalent to \(f_s(i)=b/2\). If \(b\) is odd, no such phase exists. If \(b\) is even, \(a=p-b\) is even, and \(b/2\) lies strictly between \(\max(0,s-a)\) and \(\min(s,b)\) because \(a,b>0\); the profile takes this interior value at exactly two phases. This gives precisely \(2\) valid phases.

**Distinctness.** If \(qk<p\), then \(k=s\) and \(qs=qk<p\); no half-period case can occur for \(q\ge3\). The strictly short-arc proof shows that every valid length-\(qk\) factor is monochromatic. The zero factor occurs exactly when \(a\ge qk\) and the one factor exactly when \(b\ge qk\), which proves the short-length expression for \(D\). If \(qk\ge p\), distinct phases give distinct factors: the circular word \(0^a1^b\) is primitive, because it has exactly one cyclic run of each symbol, and any proper period would repeat both runs. Thus length at least \(p\) identifies its starting phase. Consequently \(D=N\). All cases are exhausted.

## Verification

The accompanying standalone `verify.py` separately enumerates all starting phases by constructing each factor and comparing the numbers of ones in its \(q\) consecutive blocks, then checks both the admissible-position count and the distinct-factor count against the formulas. The enumeration includes every \(1\le a,b\le12\), \(3\le q\le8\), and \(1\le k\le2(a+b)\), plus 2,000 deterministically seeded random larger cases. All 24,464 cases (404,329 checked phase positions) pass. Execute `python3 verify.py` alongside this file; no nonstandard dependencies are required. These finite experiments are cross-checks and do not establish the infinitely quantified result, which follows from the proof above.

## Relationship to prior work

Sugimoto, Noda, Inenaga, Bannai and Takeda [1] give run-length encoded algorithms for Abelian regularities, with Abelian-square detection as a primary task, rather than an all-exponent exact two-run periodic occurrence spectrum. Fici, Mignosi and Shallit [2] investigate rich families of Abelian squares. Work on Abelian powers of Sturmian words [3] uses irrational rotations and aperiodic balanced words and does not directly enumerate the periodic two-run factors here. The survey [4] provides broader word-combinatorial context. The recent study of circular Abelian squares [5] has a related two-run boundary analysis, but concerns exponent two rather than the \(q\ge3\) arbitrary-block classification. This proof uses a three-window profile obstruction that does not arise in the same form for Abelian squares. The cited source dates are earliest public versions where applicable.

## Limitations

This result is limited to the cyclic two-run binary family and to \(q\ge3\); it does not assert a classification for general periodic words, other alphabets, or Abelian squares. The phase count and factor count are exact only under the given definitions. The available literature inspection does not exclude every unindexed equivalent statement; independent mathematical and bibliographic review has not been performed.

## References

[1] S. Sugimoto, N. Noda, S. Inenaga, H. Bannai, and M. Takeda, *Computing Abelian regularities on RLE strings*, arXiv:1701.02836, first public version January 11, 2017. https://arxiv.org/abs/1701.02836

[2] G. Fici, F. Mignosi, and J. Shallit, *Abelian-Square-Rich Words*, arXiv:1701.00948 (2017). https://arxiv.org/abs/1701.00948

[3] *Abelian Powers and Repetitions in Sturmian Words*, arXiv:1506.02797 (2015). https://arxiv.org/abs/1506.02797

[4] G. Fici and S. Puzynina, *Abelian Combinatorics on Words: A Survey*, arXiv:2207.09937 (2022). https://arxiv.org/abs/2207.09937

[5] *The minimum number of distinct abelian squares in a binary circular word*, hexagon:2610.00473v2 (2026). https://hexagonmath.org/2610.00473v2
