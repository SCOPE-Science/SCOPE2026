# Exact Abelian-square content counts and Parikh minima for four-run binary words

## Finding

Let \(p,q,r,s\) be arbitrary positive integers and \(w=a^p b^q a^r b^s\). Write \(\theta(w)\) for the number of **distinct nonempty factor words** that are Abelian squares: words \(uv\) with \(|u|=|v|\) and \(u,v\) having identical numbers of both letters. Different occurrences of the same factor are counted once; factors of equal Parikh vector but different contents are counted separately.

For \(m\ge1\) and an integer \(t\), define
\[
E(m,t)=\#\{j\in\{1,\ldots,m\}:j\equiv t\pmod2\}
=\begin{cases}\lfloor m/2\rfloor,&t\equiv0\pmod2,\\\lceil m/2\rceil,&t\equiv1\pmod2.\end{cases}
\]
Write \(\mathbf1_{P}\) for the indicator of proposition \(P\). The following formula holds for **all** positive \(p,q,r,s\):
\[
\boxed{\begin{aligned}
\theta(a^p b^q a^r b^s)={}&
\left\lfloor\frac{\max(p,r)}2\right\rfloor
+\left\lfloor\frac{\max(q,s)}2\right\rfloor\\
&+\mathbf1_{2\mid q}\min(p,r)
 +\mathbf1_{2\mid r}\min(q,s)\\
&+\mathbf1_{r\le p}E(\min(q,s),q)
 +\mathbf1_{q\le s}E(\min(p,r),r)\\
&-\mathbf1_{r\le p}\mathbf1_{q\le s}.
\end{aligned}}
\]

Put \(H(t)=\lfloor(t+2)/4\rfloor\). For **each pair of integer letter counts \(A,B\ge4\)**, the sharp minimum among all four-run words with exactly \(A\) occurrences of \(a\) and \(B\) occurrences of \(b\) is
\[
\boxed{\min_{\substack{p+r=A,\ q+s=B\\p,q,r,s\ge1}}
 \theta(a^p b^q a^r b^s)=H(A)+H(B).}
\]
An attaining word is obtained by setting
\[
r=2H(A)+1,\quad p=A-r,\quad q=2H(B)+1,\quad s=B-q.
\]
Thus the effective four-run construction already known to attain this count is **optimal within the entire four-run family**, without asserting optimality among arbitrary binary words.

## Assumptions and scope

The alphabet consists of two distinct letters \(a,b\). Runs are nonempty, and factors are contiguous and linear (not circular). The first formula has no minimum-length restriction beyond positive runs. The sharp-minimum theorem assumes the counts of *each* letter are at least four. The distinction between distinct factor **contents**, factor occurrences, and Parikh-equivalence classes is essential. Abelian squares may have one-letter halves.

## Proof

**1. Exhaustive structural classification.** A nonempty Abelian square is either entirely inside one run or spans at least two run boundaries. It cannot cross *exactly one* run boundary: if the midpoint is in either constant block, one half consists solely of the letter of that block whereas the other half contains the other letter. If the midpoint lies at the boundary the halves are of different single letters. Consequently any mixed Abelian square spans three or four runs.

Inside a single run the distinct possibilities are \(a^{2t}\), for \(1\le t\le\lfloor\max(p,r)/2\rfloor\), and \(b^{2t}\), for \(1\le t\le\lfloor\max(q,s)/2\rfloor\).

A factor spanning precisely three runs has the form \(a^i b^q a^j\) or \(b^i a^r b^j\) with positive outer exponents. Equal letter counts in the halves force \(i=j\), and the complete interior run must have even length. Thus the only possibilities are
\[
\{a^t b^q a^t:1\le t\le\min(p,r),\ 2\mid q\},\qquad
\{b^t a^r b^t:1\le t\le\min(q,s),\ 2\mid r\}.
\]

Every factor spanning all four runs has the form \(a^i b^q a^r b^j\) with \(1\le i\le p\), \(1\le j\le s\). Its midpoint must lie in one of its two *internal* runs; if the midpoint lies in the first \(b\)-run, matching numbers of \(a\)'s requires \(i=r\), and matching numbers of \(b\)'s requires \(j\le q\) and \(j\equiv q\pmod2\). This yields the family
\[
\mathcal F_b=\{a^r b^q a^r b^j:r\le p,\ 1\le j\le\min(q,s),\ j\equiv q\pmod2\}.
\]
If the midpoint is in the internal \(a\)-run, the equal Parikh counts instead require \(j=q\), \(i\le r\), and \(i\equiv r\pmod2\). This yields
\[
\mathcal F_a=\{a^i b^q a^r b^q:q\le s,\ 1\le i\le\min(p,r),\ i\equiv r\pmod2\}.
\]
These conditions are sufficient: in either case a midpoint inside the indicated run is constructed by bisecting the matching letter counts.

The four basic run-number patterns (one, three starting with \(a\), three starting with \(b\), four) are disjoint as factor contents. The two four-run families overlap in exactly one string, \(a^r b^q a^r b^q\), and only when \(r\le p\) and \(q\le s\). Counting the families, subtracting their single possible intersection, gives the displayed exact formula.

**2. The sharp lower bound.** For \(t\ge4\), every decomposition \(u+v=t\) into positive integers satisfies
\[
\left\lfloor\frac{\max(u,v)}2\right\rfloor\ge H(t)-\delta_t(u,v),
\]
where \(\delta_t(u,v)=1\) exactly when \(t\equiv2\pmod4\) and \(u=v=t/2\), and is zero otherwise. This follows by taking \(\max(u,v)\ge\lceil t/2\rceil\) and considering the four residues of \(t\) modulo four. In a deficient case, the equal run length \(t/2\) is odd and at least three.

The trivial Abelian squares of \(w\) therefore already contribute at least \(H(A)+H(B)-\delta_A(p,r)-\delta_B(q,s)\). We exhibit at least as many *distinct mixed* squares as the number of deficiencies:

If \(\delta_A(p,r)=1\), then \(p=r\ge3\) is odd. For even \(q\), the mixed square \(ab^q a\) appears across the first three runs. For odd \(q\), the four-run mixed square \(a^r b^q a^r b\) appears, since \(r=p\) and \(s\ge1\).

If \(\delta_B(q,s)=1\), then \(q=s\ge3\) is odd. For even \(r\), the mixed square \(ba^r b\) appears across the last three runs. For odd \(r\), the four-run mixed square \(ab^q a^r b^q\) appears, since \(q=s\) and \(p\ge1\).

When both deficiencies occur, \(r\ge3\) and \(q\ge3\) are odd, so the two exhibited four-run squares are distinct: the first has initial \(a\)-run of length \(r\) and final \(b\)-run of length one, while the second has initial \(a\)-run of length one and final \(b\)-run of length \(q\). Hence the mixed factors compensate for both possible missing trivial counts. This proves the lower bound \(H(A)+H(B)\).

**3. Attainment.** For \(A,B\ge4\), the stated exponents are positive and satisfy \(r>p\), \(q>s\), with both \(q\) and \(r\) odd. The exact classification eliminates all four mixed-factor families: the three-run types require an even internal run, and the four-run types require \(r\le p\) or \(q\le s\). Only the trivial squares remain. Their number is \(\lfloor r/2\rfloor+\lfloor q/2\rfloor=H(A)+H(B)\). This proves sharpness.

## Verification

The standalone standard-library program `verify_four_run.py` independently enumerates all even-length factors using prefix Parikh sums, generates the six structural families as explicit word contents, and evaluates the closed formula. The three results agree for each of the \(9^4=6561\) positive four-run parameter tuples with individual runs at most nine. It also exhaustively minimizes the formula for every \(4\le A,B\le22\) (361 parameter pairs) and tests the failure of naively extending the minimum law to \(A=B=2\). A separate symmetry check confirmed 10,000 reversal/complement parameter cases. These are finite reproducibility checks, **not** substitutes for the symbolic all-integer proof.

To replay: `python3 verify_four_run.py` from the directory containing the delivered files. No external packages, data, or network are required.

## Relationship to prior work

Fazekas, Mammoliti, Mercaş, and Simpson, *Binary Words Containing Few Abelian Squares*, first made public April 25, 2026, define effective partitions and prove in their Theorem 12 that a particular four-run word contains exactly \(H(A)+H(B)\) distinct Abelian squares and that all are trivial. Their Conjecture 13 proposes a corresponding lower bound for *all* binary words with the given interior Parikh counts. The present claim uses their construction for the upper bound but adds an exact formula for every positive four-run tuple and proves the matching lower bound within the four-run family. It does not settle that conjecture for arbitrary words.

Fici and Saarela's earlier minimum problem and Simpson's survey distinguish the open general minimum from established bounds for words having only trivial squares. Such conditional or unrestricted lower-bound conjectures do not yield the exact distribution of mixed square contents for arbitrary four-run inputs.

## Limitations

The unrestricted fixed-Parikh minimum over binary words with five or more runs is **not** established. The count is of distinct word contents, not occurrences or Abelian-equivalence classes. The sharp-minimum theorem requires \(A,B\ge4\): for example, \(abab\) has just one distinct Abelian square although \(H(2)+H(2)=2\). The exact first formula remains valid for every positive four-run tuple. Historical priority beyond the accessible primary texts and indexed records remains subject to unindexed equivalent work; no independent mathematical validation has been carried out.

## References

1. S. Z. Fazekas, A. Mammoliti, R. Mercaş, and J. Simpson, *Binary Words Containing Few Abelian Squares*, arXiv:2604.23188, first submitted April 25, 2026. https://arxiv.org/abs/2604.23188 (Theorems 10 and 12, Conjecture 13, pp. 5–7).
2. G. Fici and A. Saarela, *On the Minimum Number of Abelian Squares in a Word*, Dagstuhl Reports 4(3), 34–35 (2014). https://doi.org/10.4230/DagRep.4.3.28 (section 3.4).
3. J. Simpson, *Solved and Unsolved Problems about Abelian Squares*, arXiv:1802.04481 (2018). https://arxiv.org/abs/1802.04481.
