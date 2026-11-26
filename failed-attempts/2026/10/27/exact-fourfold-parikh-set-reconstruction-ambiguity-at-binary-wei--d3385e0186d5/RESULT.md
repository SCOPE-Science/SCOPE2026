# Exact fourfold Parikh-set reconstruction ambiguity at binary weight three

## Finding
For a finite binary word \(w\), let \(\Pi(w)\) be the **set, not multiset**, of Parikh vectors of all its nonempty contiguous factors: each vector records the number of zeros and ones in a factor, and multiplicity is discarded. Fix \(n\geq3\) and a word containing exactly three ones, uniquely written
\[
w=0^a1\,0^b1\,0^c1\,0^d,\qquad a,b,c,d\in\mathbb Z_{\geq0},\quad n=a+b+c+d+3.
\]
The complete fiber of \(\Pi(w)\) among binary words of length \(n\) is the set of **distinct** words represented by
\[
(a,b,c,d),\qquad(d,c,b,a),
\]
and, **if and only if** \(\min(b,c)\geq\max(a,d)\), also
\[
(a,c,b,d),\qquad(d,b,c,a).
\]
Here \((e,f,g,h)\) denotes \(0^e1\,0^f1\,0^g1\,0^h\); repeat representations are counted only once. Consequently every fiber has size \(1\), \(2\), or \(4\), and a fiber has size four precisely when
\[
a\ne d,\qquad b\ne c,\qquad \min(b,c)\geq\max(a,d).
\]
A singleton fiber occurs exactly when \(a=d\) and \(b=c\). The first four-word fiber occurs at length seven: \(\{0100101,0101001,1001010,1010010\}\).

Let \(T_n\) denote the number of four-word fibers, \(S_n\) the number of singleton fibers, and \(U_n\) the number of two-word fibers, restricted to length \(n\) and weight three. Then
\[
\sum_{n\geq3}T_nz^n=\frac{z^7}{(1-z)(1-z^2)(1-z^3)(1-z^4)},\qquad
S_n=\begin{cases}(n-1)/2,&n\text{ odd},\\0,&n\text{ even},\end{cases}
\]
\[
U_n=\frac{\binom n3-S_n-4T_n}{2},\qquad
\#\{\Pi(w):|w|=n,\ |w|_1=3\}=\frac{\binom n3+S_n-2T_n}{2}.
\]
In particular, \(T_n\sim n^3/144\), and the proportion of length-\(n\), weight-three words belonging to four-word fibers tends to \(1/6\).

## Assumptions and scope
The alphabet is exactly \(\{0,1\}\); factors are contiguous and nonempty; the observation records **presence** of each factor composition, not how many factors have that composition. Reconstruction is among words of the same length and with exactly three ones. The statements apply to all nonnegative zero-gap lengths, including adjoining ones and words beginning or ending in one. A string's reversal necessarily has the same observation. No claim concerns arbitrary Hamming weights, factor-composition **multisets**, or scattered subsequences.

## Proof
**1. The complete composition set is determined by two window extremes.** For \(1\leq k\leq n\), let \(F(k)\) and \(G(k)\) denote the largest and smallest numbers of ones among length-\(k\) factors. Consecutive length-\(k\) windows change the one-count by at most one, so every integer between \(G(k)\) and \(F(k)\) is achieved. Hence equality of complete Parikh sets for two length-\(n\) words is equivalent to equality of \(F\) and \(G\) for every \(k\).

**2. Recover the unordered inner and outer zero gaps.** The least factor length containing at least two ones is \(\min(b,c)+2\), while the least length containing at least three is \(b+c+3\). These are read off from \(F\); hence \(\{b,c\}\) is determined. For \(r=0,1,2\), let \(L_r\) be the greatest length of a factor containing at most \(r\) ones. It is read off from \(G\), and a direct examination of factors spanning consecutive ones gives
\[
L_0=\max(a,b,c,d),\qquad
L_1=1+\max(a+b,b+c,c+d),\qquad
L_2=n-1-\min(a,d).
\]
Thus \(L_2\) and the known total number \(n-3-(b+c)\) of outer zeros determine the unordered pair \(\{a,d\}\). No more than the four independent choices of inner and outer order can share the observation.

**3. Decide when the independent inner swap is invisible.** Reversal simultaneously exchanges the orders of the two pairs and always preserves the observation. If either pair consists of equal numbers, the four possibilities collapse to at most two distinct words, necessarily reversals, so there is no further condition. Otherwise write \(A>\alpha\) for the two outer gaps and \(B>\beta\) for the two inner gaps. One of the nonreversed placements puts the larger outer and larger inner gap next to each other, with
\[
L_1-1=\max(A+B,B+\beta)=B+\max(A,\beta).
\]
The other placement gives
\[
L_1-1=\max(A+\beta,\alpha+B,B+\beta).
\]
If \(\beta\geq A\), both expressions equal \(B+\beta\); if \(\beta<A\), the first is \(A+B\) while every entry of the second is strictly less than \(A+B\). The remaining invariant \(L_0\) is automatically unchanged when the two unordered gap pairs are fixed. Hence both independent swaps preserve the full composition set **exactly** when \(\min(b,c)\geq\max(a,d)\). This proves the complete fiber formula, including all boundary and equality cases.

**4. Count the fibers and take the asymptotic limit.** A singleton word equals its reverse, which here means \(a=d\) and \(b=c\); counting \(a+b=(n-3)/2\) yields \(S_n\). Every four-word fiber has a unique gap representative satisfying \(a<d\leq b<c\). Set
\[
a=x,\quad d=x+1+y,\quad b=x+1+y+z,\quad c=x+2+y+z+t
\]
with \(x,y,z,t\geq0\). Its length is \(n=7+4x+3y+2z+t\), proving the displayed generating function. Every weight-three word lies in exactly one fiber, so \(\binom n3=S_n+2U_n+4T_n\). Finally, near \(z=1\), the generating function has leading singularity \(1/[24(1-z)^4]\); equivalently, lattice-point counting in \(4x+3y+2z+t=n-7\) yields \(T_n\sim n^3/144\). Division by \(\binom n3\sim n^3/6\) gives the limiting proportion \(1/6\).

## Verification
The accompanying standalone standard-library checker `verify.py` independently constructs each Parikh set from **all substrings**, groups all \(\binom n3\) weight-three words by that set, and compares each resulting fiber with the explicit gap-swap formula. It also compares the counts of fibers of sizes one, two and four with the closed formulas and generating-function coefficients. Every check passed for each length \(3\leq n\leq24\), comprising 12,650 distinct words and 5,927 fibers. These finite checks corroborate, but do not replace, the unrestricted proof above. Run `python3 verify.py` from the directory containing the file.

## Relationship to prior work
Prefix normal forms and the maximum/minimum window-count criterion are classical tools for binary jumbled pattern matching; the reduction to the two extremes is also stated in Burcsi--Fici--Lipták--Ruskey--Sawada, *On Prefix Normal Words and Prefix Normal Forms* (arXiv:1611.09017, Theorem 4). Earlier work on prefix normal words (arXiv:1401.6346; arXiv:1805.12405) studies the indexing observation and **single** prefix-normal-form classes. These ingredients do not by themselves enumerate the intersection fibers determined by **both** extremes; the new statement is the exact fixed-weight-three reconstruction fiber, its sharp fourfold boundary, and the complete fiber-size enumeration. In contrast, Acharya et al., *String Reconstruction from Substring Compositions* (arXiv:1403.2439), retains composition **multiplicity** and proves that all words of length at most seven are reconstructible up to reversal from that stronger observation; our fourfold example at length seven shows why those results do not imply the present equivalence.

## Limitations
The classification is specifically for three ones and the set-valued full-length factor-composition observation. No formula is asserted for weight four or more, for composition multisets, or for alternative observations such as selected factor lengths. Historical originality cannot be absolutely guaranteed against unindexed literature; mathematical correctness of the finite checks does not confer independent audit or external certification.

## References
1. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346 (first version 2014-01-24). https://arxiv.org/abs/1401.6346
2. P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017 (2016); see Theorem 4 and the discussion of fixed-density prefix-normal counts. https://arxiv.org/abs/1611.09017
3. G. Fici and Z. Lipták, *On Prefix Normal Words*, arXiv:1805.12405; see the discussion of prefix-normal equivalence classes. https://arxiv.org/abs/1805.12405
4. J. Acharya et al., *String Reconstruction from Substring Compositions*, arXiv:1403.2439 (2014); see the definition of the composition **multiset** and the reconstruction threshold. https://arxiv.org/abs/1403.2439
