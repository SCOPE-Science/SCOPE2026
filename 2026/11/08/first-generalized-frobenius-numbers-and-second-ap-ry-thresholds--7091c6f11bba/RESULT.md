# First generalized Frobenius numbers and second Apéry thresholds for a near-arithmetic triple

## Finding
For all integers \(m\ge3\) and \(2\le h\le m-1\), consider the numerical semigroup
\[
S_{m,h}=\langle m,m+1,hm-1\rangle.
\]
Write \(R(n)\) for the number of triples \((z,x,y)\in\mathbb Z_{\ge0}^3\) with \(mz+(m+1)x+(hm-1)y=n\), and put \(q=h+1\), \(c=hm-1\), and \(u=\lfloor c/q\rfloor\). For every residue \(0\le r<m\), let \(w_r\) be the smallest nonnegative integer congruent to \(r\) modulo \(m\) with at least two representations. Then the complete second Apéry thresholds are
\[
w_r=\begin{cases}
r(m+1)+qm,&0\le r\le u-1,\\
(m-u)c,&r=u,\\
(u+1)(m+1),&r=u+1,\\
(m-r)c+qm,&u+2\le r\le m-1.
\end{cases}
\]
An interval with its lower endpoint greater than its upper endpoint contributes no cases. The first generalized Frobenius number is
\[
\boxed{g_1(S_{m,h})=(m+1)\left\lfloor\frac{hm-1}{h+1}\right\rfloor+(h-1)m-1+\mathbf1_{\,h+1\mid m}.}
\]
The generalized genus (number of nonnegative integers having zero or one representation) is
\[
\boxed{n_1(S_{m,h})=
\frac{(m+1)(u(u+1)/2+1)+c((m-u)(m-u-1)/2+1)+qm(m-2)}{m}-\frac{m-1}{2}.}
\]

## Assumptions and scope
The parameters are integers in the stated ranges, with \(m\) the least and \(c\) the largest generator; \(\gcd(m,m+1)=1\) makes the complement finite. The generators are distinct and minimal: the least nonnegative element of \(\langle m,m+1\rangle\) congruent to \(-1\) modulo \(m\) is \(m^2-1>hm-1\). The statement concerns exactly the threshold of *two* representations, not the higher generalized Frobenius numbers. The residue class \(r=0\) is included, and \(R(0)=1\).

## Proof
**1. Reducing to two nonnegative coefficients.** For fixed \(r\in\{0,\ldots,m-1\}\), put \(A_r=r(m+1)\) and \(B_r=(m-r)c\). A pair \((x,y)\in\mathbb Z_{\ge0}^2\) contributes the base weight \(T(x,y)=(m+1)x+cy\) with \(T(x,y)\equiv r\pmod m\) exactly when \(x-y\equiv r\pmod m\). If \(x-y=r\), the two least such weights are \(A_r\) and \(A_r+qm\), reached by \((r,0)\) and \((r+1,1)\). If \(x-y=r-m\), the two least weights are \(B_r\) and \(B_r+qm\), reached by \((0,m-r)\) and \((1,m-r+1)\). Here increasing both coefficients by one increases weight by \((m+1)+c=qm\).

No other branch can enter the two lowest weights: if \(x-y\ge r+m\), the least weight is at least \(A_r+m(m+1)>A_r+qm\), since \(q\le m\). If \(x-y\le r-2m\), the least weight is at least \(B_r+mc>B_r+qm\), since \(c>q\). Thus the two cheapest base weights in the residue class come from the four displayed candidates, and the second cheapest is
\[
w_r=\min\{\max(A_r,B_r),\min(A_r,B_r)+qm\}.
\]
For \(n\equiv r\pmod m\), every base pair \((x,y)\) with \(T(x,y)\le n\) corresponds to exactly one full representation, with \(z=(n-T(x,y))/m\). Consequently \(n\) has at least two representations exactly when \(n\ge w_r\) in its residue class. This also establishes the use of the second-base-weight threshold without assuming any unproved monotonicity of \(R(n)\) across different residues.

**2. The four residue intervals.** Since
\[
A_r-B_r=m(qr-c),
\]
write \(c=qu+\rho\) where \(0\le\rho<q\). For \(r\le u-1\), one has \(B_r-A_r\ge qm\), so \(w_r=A_r+qm\). For \(r=u\), the difference is \(m\rho<qm\), so \(w_u=B_u\). At \(r=u+1\), the difference is \(m(q-\rho)\le qm\), so \(w_{u+1}=A_{u+1}\). For \(r\ge u+2\), the difference is greater than \(qm\), so \(w_r=B_r+qm\). This proves the stated complete threshold table.

**3. Maximization.** The first branch is strictly increasing, while the fourth is strictly decreasing. The sole candidates for the maximum are at \(u-1\), \(u\), \(u+1\), or \(u+2\), with nonexistent endpoints omitted. We have
\[
w_{u-1}-w_{u+1}=m(h-1)-2>0,
\qquad
w_u-w_{u-1}=1+m(\rho-q+1).
\]
When \(u+2\le m-1\), also
\[
w_{u+2}-w_{u+1}=1+m(\rho-q+1)\le1.
\]
As \(w_{u-1}-w_{u+1}\ge1\), the fourth branch cannot exceed \(w_{u-1}\). The maximum is therefore \(w_{u-1}\), unless \(\rho=q-1\), in which case \(w_u=w_{u-1}+1\). Finally \(\rho=q-1\) holds precisely when \(q\mid(c+1)=hm\), equivalently when \(q\mid m\) because \(\gcd(h,h+1)=1\). Subtracting \(m\) from the maximal \(w_r\) yields exactly the formula for \(g_1\).

**4. Counting the gaps.** In residue \(r\), the nonnegative integers with at most one representation are exactly \(r,r+m,\ldots,w_r-m\), a set of size \((w_r-r)/m\). Hence
\[
n_1=\frac1m\sum_{r=0}^{m-1}w_r-\frac{m-1}{2}.
\]
Summing the four pieces gives
\[
\sum_{r=0}^{m-1}w_r=(m+1)\bigl(u(u+1)/2+1\bigr)
+c\bigl((m-u)(m-u-1)/2+1\bigr)+qm(m-2).
\]
Substitution proves the genus formula and completes the proof. All steps hold at the extreme permitted values, including \(m=3\) and \(h=m-1\).

## Verification
The standalone `verify.py` implements an independent unbounded-in-count but finite-in-domain dynamic-programming representation counter. It computes the full three-coin generating-function coefficients by successive coin additions, identifies the first residuewise occurrence of at least two representations, and compares these to the four-branch formula. It independently measures the last integer with at most one representation and counts the whole generalized-gap set. The saved `checks.txt` documents **3,916** parameter pairs, **238,876** residue thresholds and **24,283,898** integer states, all passing. Computation is corroborative; the preceding argument proves the infinite assertions.

## Relationship to prior work
Komatsu and Ying, *The p-Numerical Semigroup of the Triple of Arithmetic Progressions* (arXiv:2206.13052, first public 2022-06-27; Symmetry 15 (2023), 1328), developed the general \(p\)-Apéry approach and explicit \(p\)-Frobenius and genus formulas for the genuine arithmetic triple \(\langle a,a+d,a+2d\rangle\). Here the two-parameter triple \(\langle m,m+1,hm-1\rangle\) is generally not an arithmetic progression, and its first generalized Frobenius number exhibits a divisibility-dependent single-unit jump. The general Apéry identity is previously known and is not claimed as new; the contribution is the complete new family's explicit second thresholds and closed \(g_1,n_1\) formulas. General algorithms for three-generator denumerants do not directly constitute this parameterwise closed classification.

## Limitations
The formulas apply to exactly \(m\ge3\), \(2\le h\le m-1\), and \(p=1\); no statement is made for larger \(p\), nonminimal or shifted triples, or arbitrary three-generator semigroups. Extensive finite checks are not an independent audit, and the novelty comparison cannot exclude an unindexed equivalent specialization in older literature. Independent scientific validation remains unperformed.

## References
1. T. Komatsu and H. Ying, *The p-numerical semigroup of the triple of arithmetic progressions*, arXiv:2206.13052 (first publicly posted 2022-06-27); *Symmetry* **15** (2023), 1328. https://arxiv.org/abs/2206.13052 ; https://doi.org/10.3390/sym15071328.
2. J. L. Ramírez Alfonsín, *The Diophantine Frobenius Problem*, Oxford University Press (2005), for the standard classical Frobenius and Apéry framework.
