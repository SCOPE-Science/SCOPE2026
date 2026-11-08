# Sharp negative-type threshold and Euclidean rank drop for three-dimensional Hermitian forms graphs

## Finding

Let \(q\ge2\) be any prime power. On the additive group \(\mathcal H_q=\operatorname{Herm}_3(\mathbb F_{q^2})\), of size \(q^9\), consider the rank metric \(d(X,Y)=\operatorname{rank}_{\mathbb F_{q^2}}(X-Y)\). Define
\[
\Phi_q(t)=q^3 3^t-q(q^2-q+1)2^t-q^2+q-1.
\]
It has one positive zero \(\beta_q\), and the precise interval of negative type is
\[
\boxed{\quad 0<t\le\beta_q.\quad}
\]
Strict negative type holds for \(0<t<\beta_q\), while at the endpoint only the **full-rank Hermitian Fourier sector** becomes null. The critical exponent obeys
\[
\boxed{\lim_{q\to\infty}q^3\beta_q=\frac1{\log(3/2)}.}
\]
The minimum real Euclidean dimension realizing squared distances \(d(X,Y)^t\) is \(q^9-1\) for \(0<t<\beta_q\) and, at \(t=\beta_q\), drops sharply to
\[
\boxed{q^9-1-q^3(q-1)^2(q^2+1)(q^2+q+1).}
\]
For example, when \(q=2\), the threshold is \(0.187962707562\ldots\), and the minimum embedding dimension falls from \(511\) to \(231\).

## Assumptions and scope

Let \(F=\mathbb F_q\) and \(K=\mathbb F_{q^2}\), with field involution \(\overline x=x^q\). A Hermitian matrix satisfies \(H=\overline H^{\mathsf T}\). Its diagonal entries lie in \(F\); there are \(q^9\) such matrices. Every Hermitian form has a diagonal normal form by invertible congruence, classified by its rank \(s\in\{0,1,2,3\}\). The rank function is subadditive, so \(d\) is a translation-invariant metric. We use the conventional definition: \(d\) has \(t\)-negative type if \(\sum_{X,Y}c_Xc_Yd(X,Y)^t\le0\) for all real \(c_X\) with \(\sum_Xc_X=0\); it is strict if equality forces every \(c_X=0\).

An isometric embedding of the **snowflake metric** \(d^{t/2}\) into real Euclidean space is equivalent to realizing \(d^t\) as squared Euclidean distances. The endpoint rank is the rank of the centered Gram matrix, with the constant vector excluded.

## Proof

**1. Fourier orbit multipliers.** Fix a nontrivial additive character \(\psi:F\to\mathbb C^\times\). The pairing \(\langle B,M\rangle=\operatorname{tr}(BM)\in F\) between Hermitian matrices is nondegenerate as an \(F\)-bilinear form: rank-one Hermitian tensors span the space and separate all nonzero frequencies. Its characters are \(\chi_B(M)=\psi(\operatorname{tr}(BM))\). The Fourier multiplier of the rank-\(r\) indicator is
\[
P_r(s)=\sum_{\operatorname{rank}M=r}\chi_B(M),\qquad \operatorname{rank}B=s.
\]
Congruence invariance shows it depends only on \(s\). Put \(L=q^4+q^2+1\). To derive all multipliers without assuming a published eigenmatrix, for each \(t\)-dimensional \(K\)-subspace \(U\le K^3\) sum characters over all Hermitian matrices whose image is contained in \(U\). There are exactly \(q^{t^2}\) such matrices, and their character sum is \(q^{t^2}\) precisely when the restricted Hermitian form \(B|_U\) is zero, otherwise it is zero. If \(I_t(s)\) counts totally isotropic \(t\)-spaces for \(B\), double counting by matrix rank gives
\[
q^{t^2}I_t(s)=\sum_{r=0}^t {3-r\brack t-r}_{q^2}\,P_r(s).
\]
In particular,
\[
P_0(s)=1,\quad P_1(s)=qI_1(s)-L,\quad
P_2(s)=q^4I_2(s)-L-(q^2+1)P_1(s),
\]
and \(P_3(s)=q^9\mathbf1_{s=0}-P_0(s)-P_1(s)-P_2(s)\). Here \({a\brack b}_{q^2}\) denotes the number of \(b\)-spaces in an \(a\)-space over \(K\).

**2. Exact isotropic space counts.** If a Hermitian form has rank \(s\) on a \(3\)-space, its radical has dimension \(3-s\). The number of isotropic vectors in a nondegenerate Hermitian \(s\)-space is
\[
Z_s=q^{2s-1}+(-1)^s(q-1)q^{s-1}\quad(s\ge1),\qquad Z_0=1.
\]
To verify this, express a nondegenerate form as a sum of \(s\) field norms. Norm has one preimage of \(0\) and \(q+1\) of every nonzero value; additive-character orthogonality gives \((q^{2s}+(q-1)(-q)^s)/q\). Hence \(I_1(s)=(q^{2(3-s)}Z_s-1)/(q^2-1)\). A totally isotropic \(2\)-space lies in the radical when \(s=1\); when \(s=2\) it contains the radical and corresponds to an isotropic line in a nondegenerate Hermitian plane; when \(s=3\) none exists. We obtain
\[
\begin{array}{c|rrrr}
s&0&1&2&3\\\hline
I_1(s)&L&q^2+1&q^3+q^2+1&q^3+1\\
I_2(s)&L&1&q+1&0
\end{array}
\]
(the \(s=0\) entry counts all planes). Substitution gives the complete nonconstant multiplier table:
\[
\begin{array}{c|rrr}
s&P_1(s)&P_2(s)&P_3(s)\\\hline
1&-q^4+q^3-q^2+q-1&q(q-1)(q^2+1)^2&-q^3(q-1)(q^2+1)\\
2&(q-1)(q^2+1)&q(q^3-2q^2+q-1)&-q^3(q-1)\\
3&-q^2+q-1&-q(q^2-q+1)&q^3
\end{array}
\]
The rank-\(3\) frequency multiplicity equals the number of invertible Hermitian matrices, which is \(q^3(q-1)^2(q^2+1)(q^2+q+1)\). It follows either by the orbit-stabilizer formula for \(\mathrm{GL}_3(K)\) acting by congruence or by \(P_3(0)=q^9-1-P_1(0)-P_2(0)\).

**3. The unique negative-type obstruction.** On each nonzero Fourier character, the powered-distance matrix has eigenvalue
\[
F_s(t)=P_1(s)+2^tP_2(s)+3^tP_3(s),\qquad s=1,2,3.
\]
For every nontrivial \(s\), \(F_s(0)=-1\). In sector \(s=1\), \(P_2(1)>0\), \(P_3(1)<0\), and \(P_2(1)/|P_3(1)|=(q^2+1)/q^2\le5/4<\log3/\log2\). Consequently \(F'_1(t)<0\) for every \(t\ge0\). In sector \(s=2\), \(P_2(2)>0\) and \(|P_3(2)|-P_2(2)=q(q^2-q+1)>0\), so \(F'_2(t)<0\) for all \(t\ge0\). In sector \(s=3\), the derivative
\[
F'_3(t)=q^3(\log3)3^t-q(q^2-q+1)(\log2)2^t
\]
is strictly positive, since \(q^2>q^2-q+1\) and \(3^t\ge2^t\). Thus \(F_3(0)=-1\) and \(F_3(t)\to\infty\), giving exactly one positive root, namely \(\beta_q\). The powered-distance kernel is conditionally negative semidefinite iff all the nontrivial multipliers are nonpositive, hence exactly for \(0<t\le\beta_q\). They are strictly negative for \(0<t<\beta_q\). At the endpoint precisely sector \(s=3\) vanishes.

**4. Embedding rank and asymptotic.** Finite Fourier diagonalization gives the positive-semidefinite centered Gram matrix \(-\frac12JD_tJ\), where \(J\) is projection onto mean-zero vectors and \(D_t(X,Y)=d(X,Y)^t\). The rank of this matrix equals the minimum dimension of a real Euclidean realization. Below the threshold it is \(q^9-1\); at the threshold it loses exactly the rank-\(3\) frequency multiplicity. For the asymptotic, expand \(F_3(t)\) at \(0\):
\[
F_3(t)=-1+\bigl(q^3\log(3/2)+(q^2-q)\log2\bigr)t+O(q^3t^2).
\]
Since \(F_3\) is increasing, the unique root has order \(q^{-3}\); insertion into the expansion proves \(q^3\beta_q\to 1/\log(3/2)\).

## Verification

The standalone exact-field checker `check.py` constructs all Hermitian \(3\times3\) matrices over \(\mathbb F_4\) and \(\mathbb F_9\), independently computes their ranks and the trace character sums for all four frequency ranks, and compares every entry with the table above. It also checks rank-class multiplicities, the monotonic sector signs and the numerical roots for field sizes \(2,3,4,5,7,11\). It prints `HERMITIAN_THREE_NEGATIVE_TYPE_PASS` on success. These tests support, but are not substitutes for, the all-prime-power proof.

## Relationship to prior work

Gow, Lavrauw, Sheekey and Vanhove [1] developed constant-rank-distance sets for Hermitian matrices and used their association-scheme Fourier characters. Their paper contains exact rank-class counts and character formulas, which are **prior results**, not novelty claims here. Sánchez [2] supplied a general finite-metric formula for supremal negative type; it does not state this Hermitian family's threshold. Cioabă and Gupta [3] give general Hermitian-forms graph eigenvalue formulas and inequalities, but their results concern individual distance-graph eigenvalues, rather than the powered combination and endpoint Euclidean rank. The claimed contribution is the exact cross-sector dominance, exponent threshold and endpoint embedding dimension for this rank-three family, not the underlying known eigenmatrix. The same-method alternating-form and rectangular-matrix cases concern different additive groups and have non-implying Fourier spectra.

## Limitations

The result covers all finite fields but only Hermitian matrices of size \(3\). It does not assert a general-rank classification, new association-scheme eigenmatrices, or any sharp weighted Fourier-extension inequality. The direct consequence of combining known Hermitian eigenmatrices with general metric negative-type theory makes historical priority particularly delicate; older work on Euclidean representations of Hermitian forms graphs could contain equivalent statements. The review is not an independent specialist audit.

## References

1. R. Gow, M. Lavrauw, J. Sheekey and F. Vanhove, *Constant rank-distance sets of hermitian matrices and partial spreads in hermitian polar spaces*, arXiv:1208.1903v1, first public 9 August 2012, https://arxiv.org/abs/1208.1903.
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451v1, first public 2 August 2011, https://arxiv.org/abs/1108.0451.
3. S. M. Cioabă and H. Gupta, *On the eigenvalues of Grassmann graphs, Bilinear forms graphs and Hermitian forms graphs*, arXiv:2102.10155v1, first public 19 February 2021, https://arxiv.org/abs/2102.10155.
