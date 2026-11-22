# Sharp minimum genus for a two-gap pseudo-Frobenius covariety

## Finding
For every integer \(k\ge 2\), put \(F=2k+1\) and let \(\mathcal C_k\) be the numerical semigroups \(S\) satisfying \(F(S)=F\) and \(F-2\in\operatorname{PF}(S)\). Then
\[
\min_{S\in\mathcal C_k}g(S)=k+2,
\qquad
\#\{S\in\mathcal C_k:g(S)=k+2\}=\left\lfloor\frac{2k}{3}\right\rfloor.
\]
Every minimizer is uniquely \(S_{k,t}\), where
\[
\left\lceil\frac{k-3}{3}\right\rceil\le t\le k-2,
\quad
S_{k,t}=\{0,2k\}\cup E_{k,t}\cup O_{k,t}\cup[2k+2,\infty),
\]
\[
E_{k,t}=\{2k-2-2j:0\le j<t\},\qquad
O_{k,t}=\{3+2j:t\le j\le k-3\}.
\]
The sets with empty index ranges are empty. All these semigroups have the prescribed pseudo-Frobenius number; the statement does not assert that they have *exactly* two pseudo-Frobenius numbers.

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). Its genus is \(g(S)=\#(\mathbb N_0\setminus S)\), its Frobenius number \(F(S)\) is its largest gap, and \(x\in\operatorname{PF}(S)\) means \(x\notin S\) but \(x+s\in S\) for every positive \(s\in S\). All variables are integers, and \(k\ge2\); only odd Frobenius numbers \(F\ge5\) are considered. There is no hypothesis on multiplicity, embedding dimension or type.

## Proof
Fix \(k\ge2\), \(F=2k+1\). Since \(F\) is a gap, \(1\notin S\). Moreover \(F-2\) is pseudo-Frobenius exactly when both \(F-2\notin S\) and \(2\notin S\): if \(2\in S\), then \((F-2)+2=F\notin S\), whereas if \(1,2\notin S\), every positive member is at least \(3\), and adding it to \(F-2\) exceeds \(F\). Thus the three excluded numbers \(2,F-2,F\) (and automatically \(1\)) completely characterize membership in \(\mathcal C_k\) among numerical semigroups of Frobenius \(F\).

Write \(B=S\cap[3,2k-2]\). Because \(F\) and \(F-2\) are gaps, no two members of \(B\), including equal ones, may sum to either integer. These forbidden-pair edges form the path of \(2k-4\) vertices
\[
2k-2,\ 3,\ 2k-4,\ 5,\ \ldots,\ 4,\ 2k-3.
\]
Indeed successive sums alternate between \(F\) and \(F-2\), and each vertex has no further neighbor with sum in that two-element set. The vertex \(2k\) is the only remaining possible positive member at most \(F\). A path on \(2r\) vertices, where \(r=k-2\), has independence number \(r\). Hence \(\#(S\cap[1,F])\le r+1=k-1\), so \(g(S)\ge F-(k-1)=k+2\).

Equality forces \(2k\in S\) and \(B\) to be a maximum independent set of that even path. Its \(r+1\) possible maximum independent sets have a unique switch index \(t\in\{0,\ldots,r\}\): choose the even-positioned path vertices before index \(t\), and the odd-positioned vertices from index \(t\) onward. In numerical order these are exactly \(E_{k,t}\cup O_{k,t}\). (For \(r=0\), there is one empty path independent set.) Thus every possible minimizer has the displayed form.

It remains to impose additive closure. Within \([1,F]\), the even members are all even integers in \([2k-2t,2k]\) when \(t\ge1\), and just \(2k\) when \(t=0\). The odd members, if any, are the odd integers in \([2t+3,2k-3]\). Two even members have either sum exceeding \(F\) or an even sum already present. A mixed sum is at least \((2k-2t)+(2t+3)=2k+3>F\) if both types are nonempty; sums involving \(2k\) also exceed \(F\). Two odd members have smallest possible sum \(4t+6\); all of their sums not exceeding \(F\) are even. These lie in the displayed even interval if and only if
\[
4t+6\ge2k-2t\quad\Longleftrightarrow\quad 3t\ge k-3.
\]
When the odd set is empty the condition holds automatically in the stated index range; when \(t=0\), the only cases satisfying the inequality are the small cases for which the direct same calculation gives closure. Thus precisely the indices \(\lceil(k-3)/3\rceil\le t\le k-2\) produce numerical semigroups. Their conductor is \(F+1\), the designated gaps are absent, and their genus is \(k+2\).

There are
\[
(k-2)-\left\lceil\frac{k-3}{3}\right\rceil+1
=k-\left\lceil\frac{k}{3}\right\rceil
=\left\lfloor\frac{2k}{3}\right\rfloor
\]
such indices. This proves the sharp bound, the classification and the count.

## Verification
Run `python3 verify.py` from this package. The program independently enumerates every numerical semigroup with Frobenius \(F\) and with \(2,F-2\) absent by adding admissible new multiplicities, explicitly tests additive closure after every addition, and compares the complete set of genus minimizers with the formula for every odd \(F\) from \(5\) through \(31\). It prints `EXACT_MINIMUM_GENUS_OK` when all cases agree. This finite check corroborates but does not replace the preceding argument for unbounded \(k\).

## Relationship to prior work
Hernández-Yanes and Rosales (2026) define and algorithmically enumerate \(\mathcal C(\mathcal P)\) for arbitrary prescribed pseudo-Frobenius subsets, and give genus bounds in terms of \(F\) and the cardinality of \(\mathcal P\). Here \(\mathcal P=\{F-2,F\}\), and the distinct contribution is a sharp bound with explicit classification and a closed count of *all* genus minimizers for every odd \(F\ge5\), rather than a general enumeration algorithm. The existing minimum-genus classification of perfect numerical semigroups applies to the different constraint of having no isolated gap: in particular it reports a unique odd-Frobenius minimizer, whereas the present covariety has \(\lfloor2k/3\rfloor\) minimizers. The classical type-two literature treats exact pseudo-Frobenius pairs, while the present theorem allows additional pseudo-Frobenius gaps. Multiparameter numerical-semigroup counting results enumerate by Frobenius number, genus and multiplicity, not by this prescribed pseudo-Frobenius condition.

## Limitations
Only odd Frobenius numbers are classified; no assertion is made for even \(F\), for all genus levels, or for semigroups with exactly the two prescribed pseudo-Frobenius numbers. Although targeted literature and mathematical-record comparisons did not reveal the exact extremizer formula, unindexed equivalent results or implicit deductions in broad classification literature remain possible. The 2016 type-two article and the latest multiparameter counting article could not both be inspected in full here, so historical priority is provisional. Verification through \(F=31\) is finite and is not a proof of the infinite theorem.

## References
1. W. G. Hernández-Yanes and J. C. Rosales, *The covariety of numerical semigroups with some prescribed pseudo-Frobenius numbers*, arXiv:2611.09425v1, first public 2026-11-06, https://arxiv.org/abs/2611.09425.
2. A. M. Robles-Pérez and J. C. Rosales, *The genus, Frobenius number and pseudo-Frobenius numbers of numerical semigroups of type 2*, Proc. R. Soc. Edinburgh A 146 (2016), 1081–1090, https://doi.org/10.1017/S0308210515000840.
3. M. Bras-Amorós and V. Torra, *Multiparameter counting of numerical semigroups by Frobenius number, genus, and multiplicity*, arXiv:2611.11559v1, first public 2026-11-08, https://arxiv.org/abs/2611.11559.
4. *Complete minimum-genus classification of perfect numerical semigroups*, published-finding corpus record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-complete-minimum-genus-classification-of-perfect-numerical-semig--eae339a60699.
