# A parity-filtered balanced Boolean layer has a sharp one-unit static–adaptive gap

## Finding

For disjoint sets \(X,Y\) of odd sizes \(|X|=a=2u+1\), \(|Y|=b=2v+1\), where \(u,v\) are arbitrary nonnegative integers, set \(m=u+v+1\) and consider the membership concept class
\[
\mathcal H_{a,b}=\{S\subseteq X\sqcup Y:|S|=m,\ |S\cap X|\equiv0\pmod2\}.
\]
Its exact static and adaptive shattering dimensions are
\[
\operatorname{VCdim}(\mathcal H_{a,b})=m-1,\qquad
\operatorname{Ldim}(\mathcal H_{a,b})=
\begin{cases}m,& a,b\ge3,\\m-1,&\min(a,b)=1.\end{cases}
\]
Thus a single parity restriction on a balanced uniform layer causes a strict one-unit static–adaptive gap precisely when both parity blocks have at least three coordinates. Moreover, \(|\mathcal H_{a,b}|=\tfrac12\binom{2m}{m}\). The unrestricted balanced layer has both dimensions \(m\).

## Assumptions and scope

All sets are finite, disjoint, and labelled. Queries are the individual Boolean coordinates \(q_x(S)=[x\in S]\). A support \(T\) is VC-shattered when every subset of \(T\) occurs as \(S\cap T\). Littlestone dimension is the greatest depth of a complete binary adaptive membership-query tree with every root-to-leaf labeling consistent with a concept; each branch may choose different later coordinates. The empty support has depth zero. The theorem includes the boundary \(a=1\), \(b=1\), and \(a=b=1\).

## Proof

**Cardinality.** The involution \(S\mapsto(X\sqcup Y)\setminus S\) preserves \(|S|=m\), since the ground set has \(2m\) elements, and reverses the parity of \(|S\cap X|\), because \(|X|=a\) is odd. Exactly half the balanced subsets obey the parity restriction.

**Universal VC upper bound.** If an \(m\)-element support \(T\) were shattered, its all-one trace would require \(S=T\), so \(|T\cap X|\) would be even. Its all-zero trace would require \(S=(X\sqcup Y)\setminus T\), whose intersection with \(X\) has parity opposite to \(|T\cap X|\). Contradiction. No larger support is shattered because shattering is downward closed. Hence \(\operatorname{VCdim}\le m-1\).

**Adaptive lower bound in the interior.** Suppose \(u,v\ge1\) and choose \(x_0\in X\) as the first query. Put \(X'=X\setminus\{x_0\}\), so \(|X'|=2u\). Under answer zero, the residual concepts have \(m\) selected coordinates and an even number from \(X'\); under answer one, they have \(m-1\) selected coordinates and an odd number from \(X'\).

For either branch select a support \(T\subset X'\sqcup Y\) of size \(m-1=u+v\), with \(i\) coordinates in \(X'\) and \(j=m-1-i\) in \(Y\). Choose \(i\in\{u-1,u\}\) to be **even** in the zero branch, and **odd** in the one branch. Since these are consecutive integers, both choices exist. Then \(j\in\{v,v+1\}\), and the numbers of unqueried coordinates outside \(T\) in \(X'\) and \(Y\) are respectively
\[
\alpha=2u-i\ge1,\qquad\beta=2v+1-j\ge1,\qquad\alpha+\beta=m.
\]

We prove that this \(T\) is shattered within its respective branch. Fix any desired positive trace \(P\subseteq T\). In the zero branch, one must add \(t=m-|P|\) points from the \(m\)-element exterior, thus \(1\le t\le m\). For \(1\le t\le m-1\), possible numbers of chosen exterior points from \(X'\) form the full integer interval
\[
\max(0,t-\beta)\le h\le\min(\alpha,t).
\]
Since \(\alpha,\beta\ge1\), this interval contains two consecutive integers, so one can choose the parity of \(h\) required to make the total \(X'\)-count even. At \(t=m\), all exterior points are chosen: their \(X'\)-count is \(\alpha=2u-i\equiv i\pmod2\), so the total count \(i+\alpha=2u\) is even. At \(t=1\), the interior interval argument already applies when \(m\ge2\), as in this interior case.

In the one branch, the number of added exterior points is \(t=m-1-|P|\), hence \(0\le t\le m-1\). For \(1\le t\le m-1\), the same consecutive-integers interval permits an odd total \(X'\)-count. When \(t=0\), one has \(P=T\) and the \(X'\)-count is \(i\), odd by construction. Thus every requested trace in either branch is realized. Each child of the root shatters an \((m-1)\)-coordinate support (not necessarily the same support), and thereby supports a complete membership tree of depth \(m-1\). The root produces a depth-\(m\) tree. Consequently \(\operatorname{Ldim}\ge m\) and \(\operatorname{VCdim}\ge m-1\).

**Universal adaptive upper bound.** Any complete decision tree of depth \(m+1\) has an all-positive root-to-leaf branch. Repeating a query along that branch would make its opposite child unrealizable, so the \(m+1\) positive answers require \(m+1\) distinct elements of a concept. Every concept has cardinality \(m\), a contradiction. Thus \(\operatorname{Ldim}\le m\).

**One-point-block boundary.** If \(a=1\), the only \(X\)-coordinate is always absent and the class is exactly the set of all \(m\)-subsets of \(Y\), of size \(|Y|=2m-1\). If \(b=1\), then \(|S\cap Y|\) is fixed to the parity of \(m\), and \(S\cap X\) ranges over all \(k\)-subsets of \(X\), where \(k=m\) for even \(m\) and \(k=m-1\) for odd \(m\), with \(|X|=2m-1\). For the membership class of all \(k\)-subsets of an \(N\)-set, both dimensions equal \(\min(k,N-k)\): any support of that size is shattered, while an all-positive or all-negative adaptive path of length one greater exhausts the available positives or negatives. In both boundary cases this value is \(m-1\), including \(m=1\). The VC upper bound and the interior lower bound complete the proof.

## Verification

The standalone `check.py` enumerates all \(m\)-element parity-filtered subsets on odd block partitions of total sizes \(4,6,8,10\), every coordinate support and its complete trace set, and the exact adaptive recurrence over all subfamilies reachable by membership queries. Its final assertion compares both dimensions to the theorem in every case; the recorded `check_output.txt` contains the observed dimensions and state counts. The finite exhaustive test is supplementary to the unrestricted proof above, not a substitute for it. Run `python3 check.py` with standard Python 3.

## Relationship to prior work

Hu, Weinberger and Shayevitz study VC dimension of binary codes, including constant-weight ensembles, in the context of asymptotic coding rate and minimum distance [1]. Their exact statements do not give the finite parity-intersection family above or an adaptive dimension. General Littlestone closure bounds [2] also do not supply this sharp all-parameter threshold. The ordinary balanced uniform slice has both dimensions \(m\) by the standard uniform-layer argument; its parity-restricted subfamily exhibits the separation described here. Related published results about parity functions, graph-neighborhood systems on Johnson graphs and constrained binary words concern different query domains or concept families. These comparisons do not establish universal historical priority.

## Limitations

The theorem assumes both blocks have odd cardinality, the selected-set cardinality is exactly half the ground size, and the parity constraint is even on one distinguished block. It does not classify arbitrary cardinality slices, even block sizes, all shattering faces, or topological invariants. The exact result is mathematically proved but has no independent mathematical audit. An unindexed equivalent prior result could affect novelty.

## References

[1] Sihuang Hu, Nir Weinberger and Ofer Shayevitz, *On the VC-Dimension of Binary Codes*, arXiv:1703.01586, first made public 2017-03-05. https://arxiv.org/abs/1703.01586

[2] *Near-tight closure bounds for Littlestone and threshold dimensions*, ALT 2021. https://research.google/pubs/near-tight-closure-bounds-for-littlestone-and-threshold-dimensions/
