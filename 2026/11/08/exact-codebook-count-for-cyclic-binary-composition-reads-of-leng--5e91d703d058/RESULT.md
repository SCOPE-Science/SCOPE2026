# Exact codebook count for cyclic binary composition reads of lengths at most four

## Finding
Let \(w\in\{0,1\}^n\) be a cyclic word with indexed sites, \(n\ge1\). For each \(k\in\{1,2,3,4\}\), count the \(n\) cyclic substrings of length \(k\), grouped solely by their number of ones. The complete resulting array \(\mathcal C_4(w)\) has \(14\) entries. Substrings wrap around, including when \(n<4\).

The number \(R_4(n)\) of distinct possible arrays—and hence the largest size of a noiseless codebook whose words have pairwise distinct arrays—is given exactly for **every** \(n\ge1\) by
\[
R_4(n)=2+\sum_{r=1}^{\lfloor n/2\rfloor}\sum_{a=r}^{n-r}
\sum_{p=0}^{r}\sum_{q=0}^{r}
V_r(n-a,p)V_r(a,q)\bigl(H_r(p,q)-L_r(p,q)+1\bigr).
\]
Here, for integral \(r\ge1\), \(m\ge0\), \(0\le u\le r\), define
\[
V_r(m,u)=\begin{cases}
\mathbf1_{m=r},&u=r,\\
\mathbf1_{m=2r-u}+\max\{0,r-u-\max(0,3r-2u-m)\},&u<r,
\end{cases}
\]
and write \(s=p+q\). The explicit bounds are
\[
L_r(p,q)=\begin{cases}
0,&s<r\text{ or }pq=0,\\
1,&s=r\text{ and }pq>0,\\
2(s-r),&s>r,
\end{cases}
\quad
H_r(p,q)=\begin{cases}
2r,&p=q=r,\\
0,&s=0,\\
\min\{2p,2q,s-1\},&\text{otherwise}.
\end{cases}
\]
No enumeration of the \(2^n\) source words occurs in this expression. The values for \(n=1,\ldots,20\) are
\[
2,3,4,6,8,13,18,30,46,72,110,169,250,369,534,764,1074,1494,2046,2776.
\]
The fourth-length reads first distinguish profiles not separated by lengths at most three at \(n=8\), and do so at every \(n\ge8\).

## Assumptions and scope
Every cyclic starting site contributes one observation at each length, with multiplicity. A rotated word gives the same observation; words are **not** identified under bit-complementation. The codebook uses exact, error-free observations, and each selected message may be represented by any one word having its own array. The formula counts arrays, not source words or rotation orbits. We allow observations longer than a primitive period and, for \(n<4\), longer than the ring.

## Proof
**1. Complete run coordinates.** Separate the two constant words. In every nonconstant cyclic binary word there are \(r\ge1\) zero-runs and \(r\) one-runs. Let \(a\) be the number of ones, \(p\) and \(q\) the numbers of singleton zero- and one-runs, and \(v_0,v_1\) the numbers of runs of length two in the two colors. Let \(e\) count incidences between a singleton zero-run and an adjacent singleton one-run, counted on both sides; at \(r=1\), an adjacent pair counts twice. These seven integers \((a,r,p,q,v_0,v_1,e)\) completely determine \(\mathcal C_4\), and conversely are recovered from it.

Indeed, write \(Z=n-a\), and let \(T_{k,j}\) be the number of cyclic \(k\)-windows of Hamming weight \(j\). Then
\[
\begin{aligned}
T_{1,1}&=a,&T_{2,1}&=2r,\\
T_{3,0}&=Z-2r+p,&T_{3,3}&=a-2r+q,\\
T_{4,0}&=Z-3r+2p+v_0,&T_{4,4}&=a-3r+2q+v_1,\\
T_{4,1}&=2r-2p-2v_0+2q-e,&
T_{4,3}&=2r-2q-2v_1+2p-e.
\end{aligned}
\]
The remaining weights at lengths two and three follow from their sums and total Hamming weights; \(T_{4,2}=n-T_{4,0}-T_{4,1}-T_{4,3}-T_{4,4}\). The displayed equations recover the seven coordinates in the stated order. Each identity counts windows through runs and their boundaries. They also hold for the short mixed rings of lengths two and three by direct cyclic-window inspection.

**2. Feasible run lengths.** If a given color has \(r\) runs, exactly \(u\) of length one and exactly \(v\) of length two, the number of symbols of that color is \(m=u+2v\) when all runs have length at most two, or may be **any** \(m\ge 3r-2u-v\) when at least one run has length at least three. Every such total is realizable by putting any excess into one long run. Consequently \(V_r(m,u)\), defined above, is exactly the number of feasible values of \(v\). This counts distinct run-coordinate data, not arrangements of runs.

**3. Every incidence value in a sharp interval.** Index the alternating zero-runs and one-runs by \(i\in\mathbb Z/r\mathbb Z\), and let \(A_i,B_i\in\{0,1\}\) mark which runs are singletons. Thus \(\sum_i A_i=p\), \(\sum_i B_i=q\), and
\[e=\sum_i A_i(B_{i-1}+B_i).\]
For \(r\ge2\), these incidences are edges in the cycle \(C_{2r}\) induced by \(p\) selected vertices on one bipartition and \(q\) on the other. The maximum is \(H_r(p,q)\): at most two edges touch each selected vertex, and unless all vertices are selected the induced graph is a disjoint union of paths with at most \(p+q-1\) edges. Equality is reached by a contiguous alternating path when \(p=q<r\), or by selecting all neighbors of the smaller side when \(p\ne q\). If all vertices are selected, there are \(2r\) edges.

The minimum is \(L_r(p,q)\). With fewer than \(r\) selected vertices of prescribed bipartition counts, an independent selection exists. At exactly \(r\) selected vertices, the only independent selections are the two entire bipartition classes; mixed choices attain exactly one edge. For more than \(r\) vertices, apply the identity \(e=2(p+q-r)+e'\), where \(e'\) is the number of edges induced by the *unselected* vertices; fewer than \(r\) vertices remain, so they may be independent. Adjacent swaps of a singleton marker with a nonsingleton marker on its own run-index cycle connect every fixed-\((p,q)\) arrangement; each swap changes \(e\) by at most one, because the shared neighbor's contribution cancels. Hence **every integer** between the minimum and maximum occurs. For \(r=1\) the same formulas follow directly from the two incidences between the two runs.

**4. Summation.** Fix \(r,a,p,q\). The number of choices of the distinct run-length-two counts is \(V_r(n-a,p)V_r(a,q)\), and every one of the \(H_r(p,q)-L_r(p,q)+1\) incidence counts can be realized independently of those choices by assigning lengths to the marked and unmarked runs. These are distinct composition arrays by Step 1. Summing and adding the two monochromatic arrays proves the formula. Selecting one source word for each array attains the stated codebook cardinality, and the pigeonhole principle proves optimality.

**5. Sharp distinction from shorter reads.** For lengths at most three, the analogous run coordinates are just \((a,r,p,q)\). Direct exhaustive inspection of the \(2^n\) words for \(1\le n\le7\) shows that their length-four arrays do not subdivide any such class. For every \(n\ge8\), the two cyclic words \(10^2 10^{n-4}\) and \(10^3 10^{n-5}\) have the same \((a,r,p,q)=(2,2,0,2)\), but their numbers of zero-runs of length two are respectively one and zero; their length-four arrays therefore differ. This proves the sharp threshold.

## Verification
`code/formula_check.py` computes the exact finite sum through length 30 and independently enumerates all incidence supports for \(1\le r\le8\), including the double-incidence convention at \(r=1\). `code/direct_enum.cpp` directly enumerates each indexed binary word, computing all fourteen observation counts from the cyclic word itself for \(1\le n\le20\). The outputs agree on all twenty common lengths. `code/threshold_check.py` independently enumerates length-three and length-four equivalence classes through length eight and confirms the sharp separation threshold. `data/counts_1_20.tsv` gives the full checked table. These finite checks corroborate but are not substitutes for the unrestricted proof of Steps 1–4.

## Relationship to prior work
Acharya et al. introduced substring-composition reconstruction using linear, complete substring multisets. Ye and Elishco studied limited-length composition reconstruction for linear strings and provided code constructions, not this circular fixed-four-read spectrum. Kiah, Puleo and Milenkovic study ordered substring frequency profiles and de Bruijn methods; ordered profiles are a different observation: they distinguish more source words than composition-only profiles, already at cyclic length six. Previous direct calculations of length-three cyclic profiles or linear length-three composition observations do not imply the additional length-two-run counts and the sharp singleton-adjacency incidence interval needed here.

## Limitations
The alphabet is binary, the read lengths are precisely one through four, and all cyclic windows are observed without error. The finite sum is explicit but is not asserted to be a minimal rational generating function or an asymptotic expansion. No independence or historical-priority certification is claimed. Other alphabets, partial coverage, noisy channels, and longer reads are not treated.

## References
1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, first posted 2014-03-10. https://arxiv.org/abs/1403.2439
2. H. M. Kiah, G. J. Puleo, O. Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1410.8837, first posted 2014-10-31. https://arxiv.org/html/1410.8837v2
3. Z. Ye, O. Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963, first posted 2022-08-31, Section VIII. https://arxiv.org/abs/2208.14963
