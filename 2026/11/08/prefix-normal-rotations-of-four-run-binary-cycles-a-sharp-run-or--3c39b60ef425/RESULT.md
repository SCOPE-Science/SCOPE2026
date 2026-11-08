# Prefix-normal rotations of four-run binary cycles: a sharp run-order obstruction and an exact necklace census

## Finding

Let \(a,b,c,d\) be arbitrary positive integers, and let \(W\) be the cyclic binary word represented by
\[
U=1^a0^b1^c0^d,\qquad L=a+b+c+d.
\]
A rotation \(V\) of \(U\) is called **periodically prefix normal** when every prefix of \(V^\omega\) contains at least as many ones as every factor of \(V^\omega\) of the same length. Then \(W\) has such a rotation if and only if
\[
\boxed{(a-c)(b-d)\le 0.}
\]
If one exists, it is unique as an infinite word (or, equivalently, as a distinct rotation of the length-\(L\) representative). This includes nonprimitive cycles.

A sharper quantitative assertion holds. Suppose \(a\ge c\) and take the rotation beginning with \(1^a\), namely \(V=U\). Let
\[
P_V(n)=|\operatorname{pref}_n(V^\omega)|_1,\qquad F_W(n)=\max_{0\le s<L}|(V^\omega)[s,s+n)|_1.
\]
Its **prefix-normal defect** is exactly
\[
\boxed{\Delta(V)=\max_{n\ge1}\bigl(F_W(n)-P_V(n)\bigr)
      =\min\{c,\max(0,b-d)\}.}
\]
If \(b>d\), the displayed maximum is attained at \(n=a+b\). Thus the criterion has a concrete run-order witness, with a sharply quantified deficit.

Write \(S_n\) and \(B_n\) for the numbers of length-\(n\) binary cyclic words having **exactly four cyclic runs**, respectively admitting and not admitting a periodically prefix-normal rotation. Count cyclic rotations as identical, but not reversal or complementation. Their ordinary generating functions are
\[
\boxed{\sum_{n\ge0}S_nz^n=\frac{z^4}{(1-z)^2(1-z^2)^2},\qquad
\sum_{n\ge0}B_nz^n=\frac{z^6}{(1-z)^2(1-z^2)^2}.}
\]
In particular \(B_n=S_{n-2}\) (with counts zero for inadmissible lengths), and \(S_n/(S_n+B_n)\to\tfrac12\) as \(n\to\infty\). The first successful counts, for lengths \(4,5,\ldots,12\), are \(1,2,5,8,14,20,30,40,55\). The numerical sequence is the shifted existing OEIS sequence A006918; the four-run prefix-normal interpretation is the finding here.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). All four run lengths are strictly positive; consequently, the cyclic word has two positive one-runs separated by two positive zero-runs, even when \(U\) is a power of a shorter word. A cyclic run crosses the end of a written representative if necessary. Rotations only, not reversal or bit exchange, define the equivalence relation for the census.

Prefix normality is evaluated in the **infinite periodic extension**, not merely among the non-wrapping substrings of the single finite representative. For a factor of length \(n=qL+r\) with \(0\le r<L\), every cyclic length-\(n\) window and every length-\(n\) prefix contain exactly \(q(a+c)\) additional ones beyond their length-\(r\) counterparts. Therefore it suffices to test lengths \(0\le n\le L\).

## Proof

**1. Reduction of the extremal factor to two beginnings.** For any cyclic binary word, fix a window length \(n\). Moving a window's start one step forward when its first symbol is zero cannot reduce its number of ones. Moving its start one step backward when the preceding symbol is one likewise cannot reduce its number of ones. Starting in a zero-run, advance to the following one-run; starting inside a one-run, retreat to its beginning. Hence a maximum-weight window starts at the beginning of a one-run. For \(W\), there are exactly two such starts.

The second start gives the rotation \(C=1^c0^d1^a0^b\). For \(0\le n\le L\), put \([x]_+=\max(x,0)\). Direct run-counting gives
\[
P_U(n)=\min(a,n)+\min\{c,[n-a-b]_+\},\qquad
P_C(n)=\min(c,n)+\min\{a,[n-c-d]_+\}.
\]
The preceding extremal-window lemma says precisely
\[
F_W(n)=\max\{P_U(n),P_C(n)\}.
\]

**2. Defect of the longer-one-run start.** Assume \(a\ge c\). Define \(H(n)=P_C(n)-P_U(n)\). For \(0\le n\le a\), \(P_U(n)=n\), so \(H(n)\le0\).

If \(b\le d\), then on \(a\le n\le a+b\) the first prefix has \(a\) ones and the second has at most \(a\). On \(a+b\le n\le a+b+c\) the first has \(n-b\) ones. If \(n<c+d\), the second has \(c\le a\le n-b\) ones; otherwise it has at most \(n-d\le n-b\) ones. Beyond \(a+b+c\), the first prefix already contains all \(a+c\) ones. Thus \(H(n)\le0\) for every \(n\), proving \(\Delta(U)=0\) in this case.

If \(b>d\), then \(a+b>c+d\). On the interval \(a\le n\le a+b\), the first prefix has exactly \(a\) ones while the second prefix's one-count is nondecreasing, so \(H\) is nondecreasing. For \(a+b\le n\le a+b+c\),
\[
P_C(n)=\min(a+c,n-d),\qquad P_U(n)=n-b,
\]
and therefore \(H(n)=\min(a+c-n+b,b-d)\) is nonincreasing. For \(n\ge a+b+c\), the first prefix contains all the ones, and again \(H(n)\le0\). Consequently the largest positive value of \(H\) is at \(n=a+b\), where
\[
H(a+b)=\min(a+c,a+b-d)-a=\min(c,b-d).
\]
Together with the length reduction and Step 1, this proves the defect formula for all \(a\ge c\) and \(b,d\ge1\).

**3. Existence and uniqueness of a suitable rotation.** Let \(A=\max(a,c)\). Every periodically prefix-normal rotation must have a prefix consisting of \(A\) ones, because a run of that length occurs as a factor. It must therefore begin at the start of a longest one-run. If \(a>c\), only the \(1^a\)-start is eligible and Step 2 says it works precisely when \(b\le d\). If \(c>a\), exchange \((a,b)\) and \((c,d)\), obtaining the condition \(d\le b\). If \(a=c\), at least one of the two starts works: choose the start followed by the shorter zero-run. These three cases are equivalent to \((a-c)(b-d)\le0\). Uniqueness also follows from the fact that two prefix-normal rotations would have the same prefix-one count \(F_W(n)\) at every length, hence would be the same binary infinite word.

**4. Exact enumeration.** The four-run necklace is represented by \((a,b,c,d)\) with the sole identification \((a,b,c,d)\sim(c,d,a,b)\). For the successful necklaces the inequalities \(a\ge c\) and \(b\le d\) select one representative uniquely, including equality cases. Write \(a=c+x\), \(d=b+y\), where \(b,c\ge1\) and \(x,y\ge0\). Then \(L=2(b+c)+x+y\), giving
\[
\sum_{n\ge0}S_nz^n
 =\sum_{b,c\ge1}\sum_{x,y\ge0}z^{2(b+c)+x+y}
 =\frac{z^4}{(1-z^2)^2(1-z)^2}.
\]
For the unsuccessful necklaces the unique representative has \(a>c\) and \(b>d\). Write \(a=c+x\), \(b=d+y\) with \(c,d,x,y\ge1\), which gives
\[
\sum_{n\ge0}B_nz^n
 =\sum_{c,d,x,y\ge1}z^{2(c+d)+x+y}
 =\frac{z^6}{(1-z^2)^2(1-z)^2}.
\]
The stated shift identity follows immediately. Each generating function has its leading singular term proportional to \(\tfrac14(1-z)^{-4}\) as \(z\to1\), while the pole at \(z=-1\) has lower order; hence \(S_n\sim B_n\sim n^3/24\) and the successful proportion tends to one-half. This covers the periodic equality case \(a=c,b=d\) without double counting.

## Verification

The standalone `verify.py` uses explicit circular-window prefix sums, not the proof's two-run-start reduction, to compute the worst factor count at each length. It independently enumerates all starting phases and compares defects and prefix-normality classifications. Running `python verify.py` gives:

```
VERIFY_OK: exhaustive quadruples 2401 ; larger seeded quadruples 650 ; all 32 length-specific necklace counts
```

The exhaustive quadruples have each of \(a,b,c,d\) in \(\{1,\dots,7\}\); the additional seeded tests use positive lengths up to 50. Counts are independently checked for every length from 4 through 35 against coefficients of the two rational generating functions. These finite tests are corroborative; the four proof steps establish the infinite claims.

## Relationship to prior work

Prefix normal forms and their connection to binary jumbled pattern matching were studied by Burcsi, Fici, Lipták, Ruskey and Sawada [1]. Cicalese, Lipták and Rossi [2] studied infinite prefix normal words and related their prefix normal forms to Abelian complexity. Cunha and collaborators [3] proved a general run-start reduction for maximum-weight windows in run-length encoded finite strings, closely related to Step 1 here. The present result uses these foundations but classifies when the canonical prefix-normal *infinite periodic form is itself a rotation* for the first nontrivial four-run cyclic family, quantifies the obstruction and counts both kinds of necklaces. General indexing algorithms are not claimed to be new.

The successful-count sequence coincides, after an index shift, with OEIS A006918 [4]. Its integer values and generating function are therefore not newly discovered; what is asserted here is the run-order interpretation, the sharp periodic prefix-normal criterion and the complementary two-step census. The broader indexed literature was checked for matching formulations, but an unindexed equivalent characterization remains possible.

## Limitations

Only cyclic words with exactly four positive runs are classified; no theorem about arbitrary run counts or arbitrary alphabets is asserted. The defect formula concerns a specifically oriented rotation beginning at a longest one-run and must not be mistaken for the minimum defect over all rotations. Finite prefix normality of one unwrapped representative is distinct from infinite periodic prefix normality. The enumeration treats reversal and complementation as different necklaces. The result has not undergone independent expert validation.

## References

[1] P. Burcsi, G. Fici, Z. Lipták, F. Ruskey, J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017, first posted 2016-11-28, https://arxiv.org/html/1611.09017v1.

[2] F. Cicalese, Z. Lipták, M. Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273, first posted 2018-11-15, https://pmc.ncbi.nlm.nih.gov/articles/PMC8219218/.

[3] L. Cunha, S. Dantas, T. Gagie, R. Wittler, L. Kowada, J. Stoye, *Fast and Simple Jumbled Indexing for Binary Run-Length Encoded Strings*, arXiv:1702.01280, first posted 2017-02-04, https://arxiv.org/abs/1702.01280.

[4] OEIS Foundation, *The On-Line Encyclopedia of Integer Sequences*, A006918, https://oeis.org/A006918 (numeric sequence only).
