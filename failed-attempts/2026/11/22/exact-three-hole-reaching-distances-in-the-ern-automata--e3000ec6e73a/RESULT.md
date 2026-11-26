# Exact three-hole reaching distances in the Černý automata

## Finding

Let \(n\ge4\) and \(Q=\{0,\ldots,n-1\}\). In the standard labeled Černý automaton, the input letters act as
\[
a(i)=i+1\pmod n,\qquad
b(i)=\begin{cases}0,&i=n-1,\\i,&0\le i<n-1.\end{cases}
\]
For a three-element omitted-state set \(H\subset Q\), let \(d_n(H)\) be the shortest length of a word \(w\) such that \(Qw=Q\setminus H\). The following gives the exact distance for **every** target, rather than only the minimum or maximum distance.

Write \(H=\{u,v,w\}\), where \(0\le u<v<w<n\), and let \(e(H)\) be the number of cyclic neighboring pairs in \(H\):
\[
e(H)=|\{h\in H:(h+1)\bmod n\in H\}|.
\]
For \(e(H)=0\),
\[
d_n(H)=\begin{cases}v+4,&w=n-1,\\w+4,&w<n-1.\end{cases}
\]
For \(e(H)=1\),
\[
d_n(H)=\begin{cases}
n+2,&(v,w)=(n-2,n-1),\\
n+3,&u=0,\ w=n-1,\\
n+x+4,&\text{otherwise},
\end{cases}
\]
where \(x\) in the last case is the unique index for which \(\{x,x+1\}\subset H\).
For \(e(H)=2\),
\[
d_n(H)=\begin{cases}
2n+1,&H=\{n-3,n-2,n-1\},\\
2n+2,&H=\{0,n-2,n-1\},\\
2n+3,&H=\{0,1,n-1\},\\
2n+u+4,&H=\{u,u+1,u+2\},\ 0\le u\le n-4.
\end{cases}
\]
These cases partition the three-element subsets, including at \(n=4\).

For \(n\ge5\), the complete distance histogram \(h_n(t)=|\{H\subset Q:|H|=3,\ d_n(H)=t\}|\) is
\[
\boxed{h_n(t)=\begin{cases}
\binom{t-5}{2},&7\le t\le n+2,\\
n-4,&n+3\le t\le2n,\\
n-3,&t=2n+1,\\
1,&2n+2\le t\le3n,\\
0,&\text{otherwise}.
\end{cases}}
\]
At \(n=4\), the four target distances are \(9,10,11,12\), one each. In every size \(n\ge5\), the unique most difficult target omits \(\{n-4,n-3,n-2\}\) and needs exactly \(3n\) letters. The worst-case value \(3n\) was already known through the avoidance threshold; the **target-dependent formula and complete spectrum** are the assertions here.

## Assumptions and scope

Words act from left to right on the *specified* transformations, and both letters cost one unit; no initial/final cyclic relabeling is free. Reaching means exact equality of the image with \(Q\setminus H\), not merely avoiding the states in \(H\) while possibly omitting more. Every intermediate image has cardinality no larger than the preceding image. The three missing states are distinct; no claim is made for other defect-one automata or higher codimension.

For the proof, represent an image \(S\) by its missing set \(H=Q\setminus S\). Then \(a\) rotates holes by one. The action of \(b\) is
\[
Hb=\begin{cases}
H,&n-1\in H,\\
(H\setminus\{0\})\cup\{n-1\},&0\in H,\ n-1\notin H,\\
H\cup\{n-1\},&0,n-1\notin H.
\end{cases}
\tag{1}
\]
Thus the number of missing states never decreases.

## Proof

**1. Explicit reaching words.** Let \([x]_n\) denote the least nonnegative residue of \(x\) modulo \(n\). Choose an ordering \((\alpha,\beta,\gamma)\) of the three desired holes, and put
\[
r=[\alpha+1]_n,\qquad d=[\beta-\alpha]_n,\qquad e=[\gamma-\beta]_n.
\]
If \(d,e\ge2\) and \([d+e]_n\notin\{0,1\}\), the word
\[
W(\alpha,\beta,\gamma)=b a^e b a^d b a^r
\tag{2}
\]
has exactly the holes \(\{\alpha,\beta,\gamma\}\). Indeed, the first \(b\) creates hole \(n-1\); after \(a^e\) the first hole is \(e-1\), which avoids \(0,n-1\). The next \(b\) adds hole \(n-1\). After \(a^d\), the two holes are \(d+e-1,d-1\) modulo \(n\), both outside \(\{0,n-1\}\) by the stated conditions. The last \(b\) adds \(n-1\), and \(a^r\) places them at \(\gamma,\beta,\alpha\). The word has length \(3+e+d+r\).

One ordering attaining the displayed answer in each case is as follows; in the 'ordinary pair' row, \(x,x+1\) is the unique ordinary neighboring pair and \(y\) is the remaining hole.

| Configuration | \((\alpha,\beta,\gamma)\) |
|---|---|
| No cyclic adjacent pair, \(w<n-1\) | \((u,v,w)\) |
| No cyclic adjacent pair, \(w=n-1\) | \((n-1,u,v)\) |
| Ordinary adjacent pair \(x,x+1\) and remaining \(y>x+1\) | \((x+1,y,x)\) |
| Ordinary adjacent pair \(x,x+1\) and remaining \(y<x\) | \((x+1,y,x)\) |
| Terminal pair \(\{n-2,n-1\}\) plus \(u\) | \((n-1,u,n-2)\) |
| Wrap pair \(\{0,n-1\}\) plus \(v\) | \((0,v,n-1)\) |
| Straight triple \(\{u,u+1,u+2\}\), \(u\le n-4\) | \((u+2,u+1,u)\) |
| Terminal triple \(\{n-3,n-2,n-1\}\) | \((n-1,n-2,n-3)\) |
| Triple \(\{0,n-2,n-1\}\) | \((0,n-1,n-2)\) |
| Triple \(\{0,1,n-1\}\) | \((1,0,n-1)\) |

The straightforward substitutions into (2) show that every displayed candidate is admissible, reaches its target, and has exactly the claimed length. This proves the upper bound for all \(n\ge4\).

**2. A lower-bound potential on high-rank images.** Define \(F(H)\) on missing sets of size at most three. Put \(F(\varnothing)=0\), and
\[
F(\{h\})=\begin{cases}1,&h=n-1,\\h+2,&h<n-1.\end{cases}
\]
For two holes \(\{p,q\}\), \(p<q\), define
\[
F(\{p,q\})=\begin{cases}
n+2,&(p,q)=(0,n-1),\\
p+3,&q=n-1,\ p\ge1,\\
n+p+3,&q=p+1\le n-2,\\
q+3,&q\le n-2,\ q-p\ge2.
\end{cases}
\tag{3}
\]
For three holes, take \(F(H)\) to be the proposed formula in the Finding. We show for each \(H\) with at most three holes and each letter \(c\) whose result still has at most three holes,
\[
F(Hc)\le F(H)+1.
\tag{4}
\]
This is a local inequality on explicitly defined functions, not an appeal to shortest-path computation.

For \(a\), holes rotate. For a three-hole set with largest index \(w\le n-3\), the same adjacency category shifts one place and the value increases by exactly one. For \(w=n-2\), the rotated set has a terminal hole \(n-1\); substitution in the formulas gives an increase of at most one, separately for no edge, an ordinary neighboring pair, and the straight triple. For \(w=n-1\), a rotation turns the terminal pair into the wrap pair, the wrap pair into an ordinary pair, and the three special consecutive triples successively into one another and then \(\{0,1,2\}\); in each case the potential increases by exactly one. For an ordinary pair with the third hole at \(n-1\), the pair remains ordinary after rotation and its starting index increases by one. For a separated set \(\{u,v,n-1\}\), it becomes \(\{0,u+1,v+1\}\), with potential increasing from \(v+4\) to \(v+5\). These cases exhaust the rotations. The same direct check using (3) verifies (4) for zero, one or two holes.

For \(b\), (1) gives three cases: the holes are unchanged; \(0\) is moved to \(n-1\); or an extra terminal hole is added. The only transitions from two to three holes insert \(n-1\) into \(\{p,q\}\) with \(1\le p<q\le n-2\). If \(q=p+1\), the resulting ordinary-pair triple (or terminal triple at \(q=n-2\)) has potential \(n+p+4=F(\{p,q\})+1\). If \(q-p\ge2\), the resulting separated triple (or terminal-pair triple at \(q=n-2\)) has potential \(q+4=F(\{p,q\})+1\). When \(b\) preserves the number of three holes, it replaces \(\{0,p,q\}\) by \(\{p,q,n-1\}\), with \(1\le p<q\le n-2\). The four possibilities—no neighboring pair, the pair \(\{0,1\}\), the pair \(\{p,p+1\}\), or the triple \(\{0,1,2\}\)—all have nonincreasing potentials under this replacement; the terminal subcases \(q=n-2\) also satisfy the inequality. The analogous one- and two-hole replacements follow directly from (3). Finally, adding the first hole increases \(F\) from zero to one. Therefore (4) holds in every case.

Every word reaching a target with exactly three holes remains within the domain \(|H|\le3\), by monotonicity of hole count. Applying (4) to its letters, starting at \(F(\varnothing)=0\), proves \(F(H)\le |w|\). Coupled with the explicit matching witnesses in step 1, this establishes the claimed *exact* distance for every three-hole target.

**3. Counting the distances.** For \(7\le t\le n+2\), separated triples whose largest hole is not terminal and whose distance is \(t\) contribute \(\binom{t-6}{2}\) when defined, while separated triples with terminal largest hole contribute \(t-6\), except at \(t=n+2\) where the latter contribution is replaced by the \(n-4\) terminal-pair triples. Together these give \(\binom{t-5}{2}\), using the convention \(\binom{x}{2}=0\) for \(x<2\). At \(t=n+3\), there are \(n-4\) wrap-pair triples. At every \(n+4\le t\le2n\), the unique ordinary adjacent pair starting at \(x=t-n-4\) can be augmented by exactly \(n-4\) third-hole positions without producing another cyclic edge. At \(t=2n+1\), there are \(n-4\) ordinary-pair triples starting at \(n-3\) and one terminal triple. The next two distances are the special wrap triples, and all remaining \(2n+4,\ldots,3n\) distances are attained once by straight triples. Hence the histogram. For \(n=4\), direct use of the four triple cases gives \(9,10,11,12\). Summing the histogram yields \(\binom n3\), as required.

## Verification

The standalone Python standard-library program `artifacts/verify_reaching.py` computes exact reaching distances independently by breadth-first search on the image-subset graph, then evaluates the displayed formulas, constructs and executes strict three-merge witnessing words, and verifies the entire predicted histogram for all \(4\le n\le18\). It separately verifies (4) for **every** admissible high-rank transition for all \(4\le n\le95\); this includes the smallest sizes and all boundary cases. The actual output is embedded as `artifacts/verification_output.txt`, ending in `VERIFY_OK`. The finite computation supports the proof but does not replace its all-\(n\) argument.

Reproduce with `python3 artifacts/verify_reaching.py` from the containing directory; no external dependencies or precomputed inputs are required.

## Relationship to prior work

The general reaching/avoiding literature establishes existence bounds and the completely reachable property, not this target-indexed codimension-three distance spectrum. Ferens and Szykuła (2022) give general reaching-length estimates; Casas and Volkov (2023/2024) and Zhu (2024) study properties and boundaries of Don-type estimates.

The published *Exact \(k\)-avoiding thresholds of the Černý automata* already proves the worst-case value \(3n\) for three omitted states and its unique hard target. The published *Exact early deficiency profile of the Černý automata* already proves the **minimum** distance \(7\) when \(n\ge5\). Two public codimension-two results give exact distances of prescribed **pairs** of missing states, including the two-hole potential (3), but expressly exclude codimension three. Those known extrema and the two-hole case are credited, not claimed as new. The present contribution is the all-target three-hole function, the explicit adjacent-hole classification, and the full graded histogram.

## Limitations

The statement concerns only the specified labeled Černý family, exactly three distinct missing states and the exact image-reaching metric. It says nothing about arbitrary binary completely reachable automata, or missing sets of cardinality four or more. Other sources might contain an equivalent three-hole classification under different terminology; no formal priority or independent expert validation is asserted.

## References

1. R. Ferens and M. Szykuła, *Completely reachable automata: a quadratic decision algorithm and a quadratic upper bound on the reaching threshold*, arXiv:2208.05956v1, first public 2022-08-11, https://arxiv.org/abs/2208.05956.
2. D. Casas and M. V. Volkov, *Don's conjecture for binary completely reachable automata: an approach and its limitations*, arXiv:2311.00077v1, first public 2023-10-31, https://arxiv.org/html/2311.00077v2.
3. Y. Zhu, *Around Don's conjecture for binary completely reachable automata*, arXiv:2402.19089v1, first public 2024-02-29, https://arxiv.org/html/2402.19089v1.
4. *Exact k-avoiding thresholds of the Černý automata*, published finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-cerny-k-avoiding-thresholds--5cdbaf373a0f.
5. *Exact early deficiency profile of the Černý automata*, published finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-early-deficiency-profile-of-the-ern-automata--766d362d36d3.
6. *A complete codimension-two reaching-distance spectrum for the Černý automata*, published finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-a-complete-codimension-two-reaching-distance-spectrum-for-the-er--139e56d5f521.
7. *Exact two-hole reaching distances in the Černý automata*, published finding, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-two-hole-reaching-distances-in-the-ern-automata--da5e8c8c82a9.
