# The exact infinity semigroup and conductor of projected hyperelliptic space curves

## Finding

For each admissible projected hyperelliptic space curve described below and every integer \(g\ge4\), the unique branch of its singular point at infinity has value semigroup
\[
S(Q_\infty)=\langle 2g-5,\,2g-3,\,2g+1\rangle.
\]
Put \(m=2g-5\), write \(m=3h+r\) with \(r\in\{0,1,2\}\), and let \(c\) denote the semigroup conductor. Then
\[
c=\begin{cases}(h+2)m-3,&r=1,\\(h+2)m-1,&r=0\text{ or }2,\end{cases}
\qquad
\delta_{Q_\infty}=\frac{3h(h+1)}2+rh+\frac{r(r-1)}2+\frac{m-1}2.
\]
The first cases \(g=4,5,6,7,8,9\) have respective pairs \((\delta,c)=(4,8),(8,14),(14,25),(22,44),(30,54),(40,75)\).

## Assumptions and scope

Let \(k=\mathbb F_q\) have odd characteristic and \(g\ge4\). Let \(\widetilde C\) be the smooth projective model of \(y^2=f(x)\), where \(f\in k[x]\) is squarefree of odd degree \(2g+1\). Choose an admissible degree-two point \(P\) as in Hilario–Salomão–Vidal Martins, Theorem 3.3: its coordinate \(\alpha\in\mathbb F_{q^2}\setminus k\) satisfies \(\beta^2=f(\alpha)\ne0\), and \(P\) consists of the conjugate pairs \((\alpha,\beta)\) and \((\alpha^q,\beta^q)\). Set \(\varphi(x)=(x-\alpha)(x-\alpha^q)\), and let \(\lambda(x)\in k[x]\) be the unique polynomial of degree at most one with \(\lambda(\alpha)=\beta\) and \(\lambda(\alpha^q)=\beta^q\). Define \(t=y-\lambda(x)\), \(u=\varphi(x)\), and \(w=x\varphi(x)\). Consider the closure \(C\subset\mathbb P^3\) of the image under \((u:w:t:1)\).

The source proves this map is the normalization and that the point \(Q_\infty\) over the unique point at infinity of \(\widetilde C\) is rational and unibranch. The present result refines its bounds for this *particular* point and this *particular* projective model. It makes no assertion that the complete curve has only this singularity; one or two non-split nodes also occur as described in the source.

The value semigroup is the set of nonnegative valuations of nonzero elements of \(\mathcal O_{C,Q_\infty}\) in the discrete valuation ring of the normalization. Its numerical conductor is the least integer \(c\) for which all integers at least \(c\) lie in the semigroup.

## Proof

**1. Valuations and homogeneous pieces.** The valuations at the unique point at infinity of \(\widetilde C\) are \(v(x)=-2\), \(v(y)=-(2g+1)\). Because \(\deg\lambda\le1\), we also have \(v(t)=-(2g+1)\). In the chart \(T\ne0\) of \(C\), the local coordinate functions are
\[
a=w/t,\qquad b=u/t,\qquad e=1/t,
\]
with respective valuations \(m\), \(m+2\), and \(m+6\), where \(m=2g-5\). Thus the semigroup \(H=\langle m,m+2,m+6\rangle\) is contained in \(S(Q_\infty)\).

For each integer \(n\ge1\), the \(k\)-span of all monomials of total degree \(n\) in \(a,b,e\) consists of fractions \(F(x)/t^n\) with numerators in
\[
V_n=\operatorname{span}_k\{x^i\varphi(x)^j:0\le i\le j\le n\}
   =k\cdot1+\varphi(x)\,k[x]_{\le3n-2}.
\]
Indeed, every nonconstant generator is divisible by \(\varphi\), and for each integer degree \(d\) from \(2\) through \(3n\) some generator \(x^i\varphi^j\) has degree \(d=2j+i\): for \(j=1,2,\ldots,n\), the intervals \([2j,3j]\) together cover \([2,3n]\). Picking one monic generator for each degree gives an upper-triangular basis of the right side. Therefore a nonzero element of the homogeneous span has valuation precisely
\[
n(m+6)-2d,\qquad d\in\{0\}\cup\{2,3,\ldots,3n\}.
\]
Call this finite set \(E_n\). It is exactly the set of valuations of some degree-\(n\) monomials (as well as their nonzero linear combinations), so \(\bigcup_{n\ge0}E_n=H\), where \(E_0=\{0\}\).

**2. Numerical conductor and its upper bound.** Since \(m\) is odd and at least three, residues of \(m+2\) and \(m+6\) modulo \(m\) are respectively \(2\) and \(6\). For each \(j\in\{0,\ldots,m-1\}\), the minimal element of \(H\) congruent to \(2j\pmod m\) is
\[
A_j=m\bigl(\lfloor j/3\rfloor+(j\bmod3)\bigr)+2j.
\]
To prove minimality, write an arbitrary combination of the two non-\(m\) generators as \(s(m+2)+t(m+6)\) and set \(h=s+3t\). For fixed \(h\), the minimum number \(s+t\) is \(\lfloor h/3\rfloor+(h\bmod3)\). Among nonnegative \(h\equiv j\pmod m\), this weight is strictly minimized at \(h=j\), because replacing \(h\) by \(h+m\) raises the term \(2h\) by \(2m\) and never decreases the minimal coin count (use \(m-2\lceil m/3\rceil\ge0\) for odd \(m\ge3\)). Thus the \(A_j\) are the full Apéry set relative to \(m\).

Consequently \(c=\max_j A_j-m+1\). Inspecting the final one to three residue positions in the three cases \(m\equiv0,1,2\pmod3\) gives the displayed conductor formula. In particular
\[
c\le m\bigl(\lceil m/3\rceil+2\bigr)-1.
\]
The number of gaps of \(H\) is obtained by summing the number of missing nonnegative integers in each residue class:
\[
\#(\mathbb N_0\setminus H)=\frac1m\sum_{j=0}^{m-1}A_j-\frac{m-1}2
=\sum_{j=0}^{m-1}\bigl(\lfloor j/3\rfloor+(j\bmod3)\bigr)+\frac{m-1}2.
\]
Writing \(m=3h+r\) evaluates this to the displayed \(\delta\) formula.

**3. No hidden low valuations.** Every number in \(E_n\) has parity \(n\bmod2\), since \(m+6=2g+1\) is odd. Thus sets of opposite degree parity never overlap. If \(n'>n\) have the same parity and \(E_n\cap E_{n'}\ne\varnothing\), then \(n'\ge n+2\) and
\[
(n+2)m\le n'm\le n(m+6).
\]
The first inequality follows from \(n'\ge n+2\). Hence \(n\ge m/3\); any shared valuation is at least \((\lceil m/3\rceil+2)m\), strictly beyond the conductor \(c\) found in Step 2.

Every regular function at \(Q_\infty\) is a quotient of a polynomial in \(a,b,e\) by a unit. Split such a polynomial into its finitely many total-degree parts. Each nonzero part has leading valuation in its corresponding \(E_n\). If the polynomial's valuation is below \(c\), its lowest-valuation degree part cannot cancel with any different degree, because such an overlap is impossible below \(c\). Thus that valuation lies in \(H\). Any valuation at least \(c\) already lies in \(H\) by definition of the conductor. Therefore \(S(Q_\infty)=H\), completing the uniform proof.

Finally, the unique normalization branch is rational. The usual length/gap identity for a residually rational unibranch curve singularity yields \(\delta_{Q_\infty}=\#(\mathbb N_0\setminus S(Q_\infty))\). The source's rational-point formula then gives the exact Aubry–Perret deficit \(\delta_{Q_\infty}\) when the normalization is maximal.

## Verification

The accompanying standalone script `verify_semigroup.py` checks over \(\mathbb F_{101}\) the leading-degree spanning statement for all \(1\le n\le17\), and checks the Apéry conductor, gap count and absence of low cross-degree collisions for all integers \(4\le g\le100\). It prints `FINITE_CHECKS_PASSED`. These finite checks are diagnostic only; the proof above supplies the all-genus conclusion independently of enumeration. The checker does not test whether a given finite field has a particular admissible degree-two point; the theorem is conditional on admissibility.

## Relationship to prior work

Hilario–Salomão–Vidal Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557v1/v2, Theorem 3.3(e) and proof Step 8, establish only inclusion of the three given generators, the lower bound \(2g-6\le\delta_{Q_\infty}\), and the upper bound equal to the number of gaps of the three-generator semigroup. The current proof establishes that this upper bound is attained for every admissible projection and gives the exact conductor and closed delta formula. Their distinct canonical cone model of Theorem 3.5 has a non-split node instead of this infinity branch and does not imply the result.

The algebraic Apéry computation is elementary; the mathematical contribution is the uniform equality between the numerical semigroup and the *geometric local value semigroup*, which could a priori acquire extra values through cancellation of polynomial expressions.

## Limitations

The result treats only the infinity branch of the specific noncanonical projective three-space model, not arbitrary embeddings of the same normalization or a classification of its analytic isomorphism type. It presupposes the source's proven normalization and admissibility hypotheses, and does not establish existence of admissible data over every prescribed small finite field. Earlier unindexed work on these local models could affect priority. Independent validation has not been performed.

## References

1. C. Hilario, R. Salomão and R. Vidal Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557v1 (first public 2026-09-18), https://arxiv.org/abs/2609.22557; specifically Theorem 3.3, Steps 1, 2, 7, 8, Lemma 2.8 and Theorem 3.5.
2. R. Rosa and K.-O. Stöhr, *Trigonal Gorenstein curves*, J. Pure Appl. Algebra 174 (2002), 187–205, https://doi.org/10.1016/S0022-4049(02)00122-6 (context for the different canonical cone model).
