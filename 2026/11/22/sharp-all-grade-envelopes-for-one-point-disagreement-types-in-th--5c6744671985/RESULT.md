# Sharp all-grade envelopes for one-point disagreement types in the generic permutation

## Finding

Let \(n\ge1\). In the countable homogeneous structure with two independent dense linear orders, fix \(n\) distinct named parameters. Write the parameters in the first order as \(1,\ldots,n\), and in the second order as a permutation \(\pi=(\pi(1),\ldots,\pi(n))\). Every complete nonalgebraic singleton type over these parameters is uniquely specified by a pair of insertion gaps \((i,j)\), where \(0\le i,j\le n\).

Let \(A_i=\{1,\ldots,i\}\), \(B_j=\{\pi(1),\ldots,\pi(j)\}\), and define the disagreement grade of this type to be \(d(i,j)=|A_i\mathbin{\triangle}B_j|\). Thus \(d(i,j)\) is the number of parameters for which the two linear orders put the new point on opposite sides. Define the graded type polynomial
\[
D_\pi(z)=\sum_{i=0}^{n}\sum_{j=0}^{n}z^{d(i,j)}=\sum_{k=0}^n c_k(\pi)z^k.
\]

**Theorem (sharp coefficient envelopes at every grade).** For every \(n\ge1\), every \(0\le k\le n\), and every \(\pi\in S_n\),
\[
\boxed{2\min\{k+1,n-k+1\}\ \le\ c_k(\pi)\ \le\ (k+1)(n-k+1).}
\]
Both bounds are attained for every \((n,k)\). For \(k\le n/2\), the decreasing permutation attains the lower bound; for \(k\ge n/2\), the increasing permutation does. An explicit folded permutation given below attains the upper bound at every prescribed grade. In particular, for grades near \(n/2\), the possible coefficient range is between linear and quadratic in \(n\), although \(D_\pi(1)=(n+1)^2\) for every \(\pi\).

## Assumptions and scope

The language has exactly two strict linear-order symbols. The structure is the Fraïssé limit of finite sets equipped with two arbitrary linear orders; both order relations are dense and without endpoints in the limit. The named parameters are pairwise distinct and induce the two-order pattern \(\pi\). A complete *nonalgebraic* singleton type means the order comparison of a fresh point with every named parameter in both orders, excluding equality. There are no additional constraints between the two order relations, so every pair of insertion gaps is realized, giving \((n+1)^2\) types.

For fixed \(n,k\), define \(\pi_{n,k}\) by its second-order list, for \(1\le t\le n\):
\[
\pi_{n,k}(t)=\begin{cases}
k+1-t,&t\text{ odd and }t\le k,\\
t-k,&t\text{ odd and }t>k,\\
t+k,&t\text{ even and }t\le n-k,\\
2n-k+1-t,&t\text{ even and }t>n-k.
\end{cases}
\]
The four clauses yield distinct values covering \(\{1,\ldots,n\}\), as also proved in the constructive argument below. There is no claim that these are all upper-bound equality cases.

## Proof

**1. The coordinate rectangle gives the upper bound.** Fix a type \((i,j)\) of grade \(k\). Put \(h=|A_i\cap B_j|\), so \(k=i+j-2h\). Since \(h\le\min(i,j)\) and \(h\ge\max(0,i+j-n)\), the necessary conditions are
\[
|i-j|\le k,\qquad k\le i+j\le2n-k,\qquad i+j\equiv k\pmod 2.
\]
Set \(u=(i+j-k)/2\) and \(v=(i-j+k)/2\). The three conditions are equivalent to \(0\le u\le n-k\) and \(0\le v\le k\), with inverse \(i=u+v\), \(j=u+k-v\). Thus there are only \((n-k+1)(k+1)\) candidate insertion-gap pairs. This proves the upper inequality for every permutation.

**2. A folded permutation realizes every candidate pair.** We show that the displayed \(\pi_{n,k}\) is a permutation and that all candidate cells have grade \(k\). The first and third branches (odd \(t\le k\) and even \(t\le n-k\)) enumerate, respectively, the positive integers at most \(k\) and the integers greater than \(k\), all of the same parity as \(k\). The second and fourth branches (odd \(t>k\) and even \(t>n-k\)) enumerate, respectively, the positive integers at most \(n-k\) and the integers greater than \(n-k\), all of the parity opposite to \(k\). These four sets are disjoint and partition \(\{1,\ldots,n\}\), proving that \(\pi_{n,k}\) is a permutation.

Consider a candidate \((u,v)\), and put \(i=u+v\), \(j=u+k-v\). Then \(|i-j|\le k\) and \(k\le i+j\le2n-k\). Count \(\pi_{n,k}(t)\le i\) for \(1\le t\le j\). At odd positions \(t\le k\), the condition becomes \(t\ge k+1-i\); at odd positions \(t>k\), the condition is automatic because \(t-k\le j-k\le i\). Hence the number of contributing odd sites is
\[
\left\lceil\frac j2\right\rceil-\max\left\{0,\left\lceil\frac{k-i}{2}\right\rceil\right\}.
\]
At even positions \(t\le n-k\), the condition becomes \(t\le i-k\); because \(i-k\le n-k\) and \(i-k\le j\), these sites contribute \(\max\{0,\lfloor(i-k)/2\rfloor\}\). At even positions \(t>n-k\), no position contributes: \(t\le j\) gives \(\pi_{n,k}(t)\ge 2n-k+1-j>i\). Therefore
\[
|A_i\cap B_j|=\left\lceil\frac j2\right\rceil+\left\lfloor\frac{i-k}{2}\right\rfloor=\frac{i+j-k}{2}=u,
\]
where the last equality uses \(i+j\equiv k\pmod2\). So \(d(i,j)=i+j-2u=k\) at every candidate cell. There are exactly \((k+1)(n-k+1)\) such cells; the upper bound is attained.


**3. Universal lower bound.** First let \(0\le k\le n/2\). For each fixed first-order gap \(i\), the sequence \(d(i,0),d(i,1),\ldots,d(i,n)\) begins at \(i\), ends at \(n-i\), and changes by exactly \(1\) in absolute value at every step, since one named parameter enters \(B_j\) per step. Thus for every row \(0\le i\le k\) and every row \(n-k\le i\le n\), at least one \(j\) has \(d(i,j)=k\). If \(2k<n\) these are \(2(k+1)\) distinct rows. If \(2k=n\), the common central row \(i=k\) has both endpoints \(j=0\) and \(j=n\) at grade \(k\), contributing two cells instead of one; the other \(2k\) rows contribute one each. In either case, \(c_k(\pi)\ge2(k+1)\).

For \(k\ge n/2\), replace the second order by its reverse, which replaces each prefix \(B_j\) with the complement of \(B_{n-j}\) and takes every disagreement grade \(d\) to \(n-d\). Applying the established inequality at grade \(n-k\) gives \(c_k(\pi)\ge2(n-k+1)\).

**4. Sharpness of the lower bound.** In the increasing permutation, \(d(i,j)=|i-j|\), hence \(c_0=n+1\) and \(c_k=2(n-k+1)\) for \(1\le k\le n\). In the decreasing permutation, \(d(i,j)=\min\{i+j,2n-i-j\}\), hence \(c_k=2(k+1)\) for \(0\le k<n\) and \(c_n=n+1\). The required lower equalities follow, including endpoints. This completes the proof.

## Verification

The accompanying standard-library Python script `check.py` computes grades both from bitmask symmetric differences of prefixes and, for small sizes, independently from the comparison signs of individual parameters. It exhausts all permutations at \(1\le n\le9\), checks each coefficient against both bounds, checks each constructed upper extremizer and its entire rectangle at \(1\le n\le80\), and records the output in `check_output.txt` ending `VERIFY_OK`. These finite tests do not prove the inequalities or construction for arbitrary \(n\); the proof above does.

## Relationship to prior work

Cameron's homogeneous-permutation classification supplies the two-order Fraïssé framework and explains the homogeneous structure. Linman and Pinsker study the reduct lattice and symmetries of the same random permutation, but not the graded prefix-disagreement coefficient envelope here. An earlier exact expectation theorem evaluates every grade of the spectrum under a uniformly random parameter permutation; that average does not determine the pointwise extrema proved here. Previously recorded specialized results establish the sharp grade-one bound \(c_1\le2n\) and the sharp grade-two bound \(c_2\le3(n-1)\), including detailed equality classifications; **those bounds are implied by, and not novel consequences of, this theorem**. This finding concerns the simultaneous sharp bounds at *every* grade, an explicit extremizer for each prescribed grade, and the quadratic-versus-linear central-grade gap. The proof does not characterize every maximizing permutation; prior low-grade equality classifications are finer in that respect.

## Limitations

The claim concerns finite distinct parameters in the generic two-linear-order structure, with one new nonalgebraic point. It does not classify all extremizers, simultaneous attainment of several distinct grade maxima, higher-arity types, or theories with additional relations. The original-claim comparison is based on accessible research literature and records and does not establish definitive historical priority. No independent mathematical audit has been performed.

## References

1. P. J. Cameron, *Homogeneous Permutations*, Electronic Journal of Combinatorics 9(2), R2 (2002), first published 2002-10-31. DOI: https://doi.org/10.37236/1674 ; full text: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v9i2r2/pdf/ .
2. J. Linman and M. Pinsker, *Permutations on the random permutation*, arXiv:1405.4297 (2014), https://arxiv.org/abs/1405.4297 ; author manuscript: https://www.dmg.tuwien.ac.at/pinsker/papers/randompermutation/pinsker_permutation.pdf .
