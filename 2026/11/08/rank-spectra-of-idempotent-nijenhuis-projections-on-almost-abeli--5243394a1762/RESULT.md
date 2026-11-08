# Rank spectra of idempotent Nijenhuis projections on almost-Abelian Lie algebras

## Finding
Let \(q\) be a prime power, let \(m\geq2\), and let \(A\neq0\) be an endomorphism of \(V=\mathbb F_q^m\). Give \(L=\mathbb F_q t\oplus V\) the Lie bracket \([t,v]=Av\), \([V,V]=0\). For \(0\leq r\leq m+1\), write \(N_r(A)\) for the number of rank-\(r\), idempotent Lie Nijenhuis operators on \(L\), with the torsion convention specified below. Let
\[
 I_j(A)=\#\{W\leq V:\dim W=j,\ AW\subseteq W\},
\]
where \(I_j(A)=0\) outside \(0\leq j\leq m\). For \(a,b\geq0\), let
\[
 D_{a,b}(A)=\#\{(W,K):AW\subseteq W,\ AK\subseteq K,\ \dim W=a,\ \dim K=b,\ W\cap K=0\}.
\]
The pairs are ordered. Then the exact rank spectrum, for every \(A\), is
\[
 \boxed{N_r(A)=q^{r(m-r+1)}\bigl(I_{m-r}(A)+I_{r-1}(A)\bigr)
 +\mathbf 1_{1\leq r\leq m}(q-1)q^mD_{r-1,m-r}(A).}
\]
In particular \(N_0(A)=N_{m+1}(A)=1\) and \(N_r(A)=N_{m+1-r}(A)\). The formula includes all ranks, not merely the total number of operators, and needs no hypothesis on the characteristic or Jordan form of \(A\).

Three explicit extremes illustrate the role of the invariant-subspace structure. If \(A=\lambda I\), \(\lambda\neq0\), then
\[
 I_j(A)={m\brack j}_q,\qquad D_{r-1,m-r}(A)={m\brack1}_q{m-1\brack r-1}_q q^{(r-1)(m-r)}.
\]
If \(A\) is a single Jordan block, every \(I_j(A)=1\), and
\[
 N_1(A)=N_m(A)=(q+1)q^m,\qquad
 N_r(A)=2q^{r(m-r+1)}\quad(2\leq r\leq m-1).
\]
If the characteristic polynomial of \(A\) is irreducible of degree \(m\), then
\[
 N_1(A)=N_m(A)=q^m,\qquad N_r(A)=0\quad(2\leq r\leq m-1).
\]
In both latter cases the zero and identity operators are the only endpoint ranks. The complete disappearance of intermediate ranks under an irreducible action, in contrast to a single Jordan block of the same size, is an exact structural distinction.

When the characteristic polynomial is a product of pairwise distinct irreducible polynomials of degrees \(d_1,\ldots,d_s\), the invariants have the explicit finite generating expressions
\[
 I_j(A)=[u^j]\prod_{i=1}^s(1+u^{d_i}),\qquad
 D_{a,b}(A)=[u^av^b]\prod_{i=1}^s(1+u^{d_i}+v^{d_i}).
\]
Thus the rank spectrum is an explicit polynomial expression for this entire squarefree family, including the split-distinct and irreducible cases.

## Assumptions and scope
A linear endomorphism \(P:L\to L\) is *idempotent Nijenhuis* here if \(P^2=P\) and, for all \(x,y\in L\),
\[
 [Px,Py]=P\bigl([Px,y]+[x,Py]-P[x,y]\bigr).
\]
All subspaces, linear maps, ranks and counts are over the stated finite field; the underlying Lie algebra has dimension \(m+1\). The condition \(A\neq0\) makes it nonabelian in the usual terminology, although the counting argument also applies to \(A=0\). The formula for \(D_{a,b}\) is only invoked with \(a+b=m-1\). The Gaussian coefficient \({m\brack j}_q\) counts \(j\)-planes in \(\mathbb F_q^m\). No equivalence under automorphisms is taken: these are counts of actual linear operators.

## Proof
**1. Nijenhuis torsion and complementary Lie subalgebras.** Since \(P^2=P\), its image \(U\) and kernel \(K'\) give a unique vector-space splitting \(L=U\oplus K'\). Evaluating the displayed torsion identity on \(U\times U\) gives \([u,u']-P[u,u']=0\), which is exactly that \(U\) is a Lie subalgebra. Evaluating on \(K'\times K'\) gives \(P[k,k']=0\), which is exactly that \(K'\) is a Lie subalgebra. On mixed arguments the identity holds automatically because \(P^2=P\). Hence the sought operators correspond *bijectively* to ordered complementary pairs of Lie subalgebras \((U,K')\), with \(\dim U=r\).

**2. Subalgebra normal form.** A subspace \(S\leq L\) either lies inside \(V\), where it is automatically an abelian subalgebra, or projects nontrivially onto the one-dimensional quotient \(L/V\). In the second case it is uniquely of the form
\[
 S=W\oplus\mathbb F_q(t+u),\qquad W=S\cap V,\quad u\in V/W.
\]
It is a Lie subalgebra if and only if \(AW\subseteq W\), as \([t+u,w]=Aw\). The underlying subalgebra forms occur already in Avetisyan's Proposition 3; we use them here to count *complementary ordered pairs*, not as a new subalgebra classification.

**3. Exactly three disjoint positions relative to \(V\).** Fix rank \(r\), so \(\dim U=r\) and \(\dim K'=m+1-r\). As \(L=U\oplus K'\), at least one of these two subalgebras must project nontrivially to \(L/V\).

(a) If \(U\subseteq V\), then \(K'=K\oplus\mathbb F_q(t+v)\) with \(K\leq V\) an invariant \((m-r)\)-plane. For each such \(K\), the complements \(U\) in \(V\) number \(q^{r(m-r)}\); the cosets \(v\in V/K\) number \(q^r\). The case contributes \(q^{r(m-r+1)}I_{m-r}(A)\).

(b) If \(K'\subseteq V\), then \(U=W\oplus\mathbb F_q(t+u)\) with \(W\) an invariant \((r-1)\)-plane. There are \(q^{(r-1)(m-r+1)}\) choices of a complementary \(K'\) in \(V\), and \(q^{m-r+1}\) cosets \(u\in V/W\). This contributes \(q^{r(m-r+1)}I_{r-1}(A)\).

(c) If both subalgebras project nontrivially to \(L/V\), write
\[
 U=W\oplus\mathbb F_q(t+u),\qquad K'=K\oplus\mathbb F_q(t+v),
\]
where \(W\) and \(K\) are invariant of dimensions \(r-1\) and \(m-r\), respectively. The direct-sum condition is equivalent to \(W\cap K=0\) and \(u-v\notin W+K\). The invariant sum \(W+K\) is a hyperplane in \(V\). Choices for \(u\in V/W\) and \(v\in V/K\) number \(q^{m-r+1}q^r=q^{m+1}\); exactly \((q-1)/q\) of these satisfy the nonzero quotient-difference condition in \(V/(W+K)\). Each ordered pair \((W,K)\) therefore contributes \((q-1)q^m\). Summing gives the displayed mixed term. The cases are disjoint and exhaustive, proving the rank formula even at \(r=0,m+1\).

**4. Consequences.** Replacing \(P\) by \(I-P\) exchanges the two complementary Lie subalgebras, proving the rank symmetry. For \(A=\lambda I\), all subspaces are invariant; choose \(H=W\oplus K\) as an \((m-1)\)-plane, then an \((r-1)\)-plane \(W\) in \(H\), and finally a complement \(K\) in \(H\). This yields the Gaussian expression for \(D\). For a single Jordan block, all invariant subspaces form one chain, hence two nonzero invariant subspaces cannot intersect trivially. Only the two boundary mixed pairs survive. For irreducible \(A\), the only invariant subspaces are \(0\) and \(V\), eliminating all intermediate ranks. For squarefree characteristic polynomial, the module is a sum of pairwise nonisomorphic simple modules and every invariant subspace is the sum of a unique subset of them; disjoint ordered pairs correspond to assigning each factor to neither side or exactly one side. This proves the generating formulas.

## Verification
The accompanying `check.py` and `check_f4.py` are standalone, standard-library finite-field checkers. The prime-field checker (i) enumerates invariant subspaces and disjoint invariant pairs for the formula and (ii) enumerates every linear endomorphism, testing \(P^2=P\) and the displayed *original torsion identity* on all basis pairs, before classifying its rank. All tests are exhaustive over the specified small finite fields, including a genuine extension field; no pre-classification assumption is used for the direct side.

The seven passing prime-field configurations are: scalar, one-block and irreducible defining maps in dimensions \(m=2,3\) over \(\mathbb F_2\), plus a split squarefree defining map in dimension \(m=2\) over \(\mathbb F_3\). In dimension \(m=3\) over \(\mathbb F_2\), the rank spectra in ranks \(0,1,2,3,4\) are respectively \((1,120,560,120,1)\), \((1,24,32,24,1)\), and \((1,8,0,8,1)\). Run `python check.py`; its recorded output is in `check_output.txt` and ends with `ALMOST_ABELIAN_NIJENHUIS_DIRECT_TORSION_OK`. A separate genuine extension-field checker uses \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\): run `python check_f4.py`. It exhausts the scalar, one-block Jordan, irreducible and split-distinct cases in dimension \(m=2\), giving rank spectra \((1,336,336,1)\), \((1,80,80,1)\), \((1,16,16,1)\) and \((1,144,144,1)\), respectively. Its output is in `check_f4_output.txt` and ends with `ALMOST_ABELIAN_NIJENHUIS_GF4_EXTENSION_OK`. These finite verifications are not substitutes for the general proof.

## Relationship to prior work
Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365 (publicly posted October 17, 2016), Proposition 3, already describes all subalgebras of the almost-Abelian Lie algebra. Its original subalgebra description is used and fully credited. Its inspected text does not supply this rank-by-rank enumeration of *complementary pairs* or the corresponding idempotent Nijenhuis operator counts. M. J. Azimi, C. Laurent-Gengoux, and J. M. Nunes da Costa, *Nijenhuis forms on \(L_\infty\)-algebras and Poisson geometry*, arXiv:1308.6119 (publicly posted August 28, 2013), studies Nijenhuis deformations more generally rather than these finite-field enumerators. The Nijenhuis condition and the general projection/subalgebra relationship are background, not independent novelty claims. The assessed contribution is the exact, arbitrarily dimensioned rank spectrum with its two-sided invariant-subspace incidence correction and the explicit spectrum gaps across Jordan and irreducible actions.

## Limitations
The result counts idempotent, not arbitrary Nijenhuis maps. It does not classify conjugacy orbits, the scheme of Nijenhuis operators, or finite-dimensional solvable Lie algebras without a codimension-one abelian ideal. For a general defining matrix the expression uses computable invariant-subspace and disjoint-invariant-pair counts rather than a single universal polynomial in \(q\); explicit Gaussian and factorization formulas are given for the stated cases. Independent validation and exhaustive historical-priority verification are not performed. An unidentified more general prior counting theorem could subsume the formula.

## References
1. Z. Avetisyan, *The structure of almost Abelian Lie algebras*, arXiv:1610.05365, v1 October 17, 2016; consulted v2 PDF, Proposition 3, https://arxiv.org/abs/1610.05365 .
2. M. J. Azimi, C. Laurent-Gengoux, and J. M. Nunes da Costa, *Nijenhuis forms on \(L_\infty\)-algebras and Poisson geometry*, arXiv:1308.6119, v1 August 28, 2013; consulted v2 HTML, https://arxiv.org/abs/1308.6119 .
