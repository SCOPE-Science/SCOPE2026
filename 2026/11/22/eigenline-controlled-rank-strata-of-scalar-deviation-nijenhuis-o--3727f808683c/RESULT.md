# Eigenline-controlled rank strata of scalar-deviation Nijenhuis operators on hemi-semidirect Leibniz algebras

## Finding
Fix a finite field \(k=\mathbb F_q\), an integer \(d\ge2\), a \(d\)-dimensional vector space \(V\), and an invertible \(k\)-linear operator \(T\colon V\to V\). Form the *left* Leibniz algebra \(L=kt\oplus V\), with
\[
[st+u,rt+v]=sTv\quad(s,r\in k,\ u,v\in V).
\]
For a linear endomorphism \(N\), impose the Leibniz Nijenhuis equation
\[
[Nx,Ny]=N\bigl([Nx,y]+[x,Ny]-N[x,y]\bigr)\qquad(x,y\in L).
\]
Every such \(N\) preserves the characteristic derived ideal \(V=[L,L]\). Thus write uniquely
\[
N(t)=at+c,\qquad N(v)=Dv\quad(a\in k,c\in V,D\in\operatorname{End}_k(V)).
\]
**The theorem classifies the intrinsic determinantal stratum** \(\operatorname{rank}(D-aI_V)\le1\). Set \(E=D-aI_V\). The Nijenhuis condition on this stratum is equivalent to \(E[T,E]=0\) and \(ETc=0\). In the zero-deviation branch \(E=0\), all \(a,c\) are allowed. When \(\operatorname{rank}E=1\), write \(E=u\otimes\varphi\) with \(u\ne0\), \(\varphi\ne0\), unique up to simultaneous reciprocal scaling. There are precisely two disjoint families:

1. *Square-zero branch:* \(\varphi(u)=\varphi(Tu)=\varphi(Tc)=0\).
2. *Eigenline branch:* \(\varphi(u)\ne0\), \(\varphi\circ T=\lambda\varphi\) for some \(\lambda\in k^\times\), and \(\varphi(c)=0\).

Let \(h_\lambda=\dim_k\ker(T-\lambda I)\), and set
\[
H_T=\sum_{\lambda\in k^\times}(q^{h_\lambda}-1),\qquad
K_T=\frac{q^d-1}{q-1}(q^{d-2}-1)+q^{d-2}H_T.
\]
These count, respectively, nonzero rational left eigenvectors of \(T\) and distinct nonzero square-zero-branch rank-one maps \(E\). For \(N\) in the stated stratum, define its exact rank polynomial \(P_{T,q}(z)=\sum_N z^{\operatorname{rank}N}\). Then
\[
\begin{aligned}
P_{T,q}(z)={}&1+(q^d-1+qK_T+q^{d-1}H_T)z\\
&+\big((q^{d-1}-q)K_T+q^{d-1}(q^{d-1}-1)H_T\big)z^2\\
&+q^{2d-2}H_Tz^d\\
&+\big((q-1)(q^d+q^{d-1}K_T)+(q-2)q^{2d-2}H_T\big)z^{d+1}.
\end{aligned}
\]
For \(d=2\), coefficients of equal powers of \(z\) must be added. For every \(d\ge3\), the number of stratum operators of corank one is exactly \(q^{2d-2}H_T\), and hence this stratum contains a corank-one Nijenhuis operator if and only if \(T\) has a rational eigenvalue. The total number is \(q(q^d+q^{d-1}K_T+q^{2d-2}H_T)\).

The square-zero branch also has an exact shifted-Jordan index-three subcount. Define
\[
K_{T,\mathrm{eig}}=\frac{H_T}{q-1}(q^{d-1}-1).
\]
Exactly \(q(K_T-K_{T,\mathrm{eig}})(q^{d-1}-q^{d-2})\) operators in the stratum satisfy \((N-aI_L)^3=0\ne(N-aI_L)^2\). For irreducible \(T\), this gives a positive count whenever \(d\ge3\), despite the absence of the corank-one stratum.

## Assumptions and scope
Here \(k\) is any finite field of any characteristic; \(T\) is invertible but **need not be semisimple or irreducible**, and \(d\ge2\). The bracket is left Leibniz and normally not skew-symmetric. Its derived ideal \(V\) is invariant under all Nijenhuis operators. The theorem concerns only those operators satisfying the stated *rank-one deviation* restriction: no classification of all unrestricted \(N\) is claimed. Rank refers to the full \((d+1)\)-dimensional endomorphism. The sum defining \(H_T\) is over nonzero elements of \(k\); since \(T\) is invertible, there are no zero eigenvalues. Every count is for labeled linear endomorphisms, not conjugacy orbits.

## Proof
**Step 1 (derived ideal and universal equations).** The defining bracket obeys the left Leibniz identity, and because \(T\) is invertible, \([L,L]=V\). Initially allow \(N(v)=\beta(v)t+Dv\) and \(N(t)=at+c\). Evaluating Nijenhuis torsion on \((v,w)\in V\times V\) gives a \(t\)-coordinate \(\beta(v)\beta(Tw)\). If \(\beta\ne0\), some \(v\) has \(\beta(v)\ne0\), implying \(\beta\circ T=0\), and invertibility of \(T\) forces \(\beta=0\). Thus \(N(V)\subset V\). Evaluating torsion on \((t,t)\) and \((t,v)\) gives, respectively,
\[
(D-aI)Tc=0,\qquad(D-aI)[T,D]=0.
\]
All other ordered basis-pair equations are then automatic, so these two equations are necessary and sufficient. With \(E=D-aI\), they become \(ETc=0\) and \(E[T,E]=0\).

**Step 2 (rank-one normal form).** For \(E=u\otimes\varphi\), direct composition shows
\[
E[T,E]=u\otimes\bigl(\varphi(Tu)\varphi-\varphi(u)(\varphi\circ T)\bigr).
\]
If \(\varphi(u)=0\), the equation is equivalent to \(\varphi(Tu)=0\). If \(\varphi(u)\ne0\), it forces \(\varphi\circ T=\lambda\varphi\), with \(\lambda=\varphi(Tu)/\varphi(u)\). Invertibility of \(T\) forces \(\lambda\ne0\). Finally, \(ETc=0\) is \(\varphi(Tc)=0\), which in the second branch is equivalent to \(\varphi(c)=0\). This gives the complete mutually exclusive classification.

**Step 3 (count the two branches).** Distinct rank-one maps are classified by a projective functional line \([\varphi]\) and a nonzero vector \(u\) after a representative for that line is fixed. There are \((q^d-1)/(q-1)\) such lines. Exactly \(H_T/(q-1)\) are eigenlines for \(T^*\), since the left and right eigenspaces for each \(\lambda\) have equal dimension. For a noneigenline, \(\varphi\) and \(\varphi\circ T\) are independent, so the number of nonzero \(u\) killed by both is \(q^{d-2}-1\). For an eigenline it is \(q^{d-1}-1\). Summing yields \(K_T\). In the second branch, an eigenline permits \((q-1)q^{d-1}\) vectors with \(\varphi(u)\ne0\), for \(H_Tq^{d-1}\) maps \(E\). Each nonzero \(E\) allows exactly \(q^{d-1}\) choices for \(c\), because \(\varphi\circ T\) is a nonzero covector. For \(E=0\), all \(q^d\) choices of \(c\) are allowed. The scalar \(a\) is always arbitrary.

**Step 4 (rank enumeration).** If \(a=0\), then \(\operatorname{im}N=\operatorname{span}(c,\operatorname{im}E)\). For the zero branch \(E=0\), the rank is zero only for \(c=0\), and one otherwise. For each square-zero-branch \(E\), \(c\in\ker(\varphi\circ T)\) lies in \(ku\) in precisely \(q\) cases, giving rank one; the remaining \(q^{d-1}-q\) give rank two. For each eigenline-branch \(E\), \(\varphi(u)\ne0\) and \(c\in\ker\varphi\), so rank one occurs only at \(c=0\); the other \(q^{d-1}-1\) choices give rank two. If \(a\ne0\), the upper-triangular block \(N\) has invertible top-left entry, so its full rank is one plus the rank of \(aI+E\). In the square-zero branch \(E^2=0\), making \(aI+E\) invertible. In the eigenline branch \(E^2=\sigma E\) with \(\sigma=\varphi(u)\ne0\); its eigenvalues are \(a\) on \(\ker\varphi\) and \(a+\sigma\) on \(ku\). Hence the operator has rank \(d\) exactly when \(a+\sigma=0\), and is otherwise invertible. Each prescribed nonzero \(\sigma\) occurs equally often. Collecting these cases yields the asserted polynomial and the rank-gap equivalence.

**Step 5 (shifted-Jordan index).** Put \(M=N-aI_L\). For the square-zero branch \(E^2=0\), its block action is \(M(t)=c\), \(M|_V=E\), so \(M^2(t)=Ec\), \(M^3=0\). A square-zero-branch map formed from an eigenline has \(Ec=0\) because \(c\in\ker(\varphi\circ T)=\ker\varphi\). The number of such maps is \(K_{T,\mathrm{eig}}\). For every noneigenline map, \(\varphi\) is nonzero on the \((d-1)\)-dimensional space \(\ker(\varphi\circ T)\), giving exactly \(q^{d-1}-q^{d-2}\) admissible \(c\) with \(Ec\ne0\). Multiply by \(q\) possible \(a\) to obtain the formula.

## Verification
`VERIFY.py` is a standalone Python 3 checker requiring only the Python standard library. Execute `python VERIFY.py` in the same directory after extracting this package. It enumerates all zero/rank-one deviations, all scalar and vector parameters, and tests the **original Nijenhuis identity on every ordered basis pair**. Independently it calculates the predicted equations, full rank distribution, and shifted-Jordan-index-three counts, for matrices over \(\mathbb F_2\) and \(\mathbb F_3\) in dimensions two through four. The polynomial formula is proved in Steps 1–5 and is not extrapolated from these finite tests.

As a diagnostic illustration, take \(q=2\), \(d=3\). For an irreducible \(T\), the rank polynomial is \(1+21z+14z^2+36z^4\); if \(T\) is the direct sum of a one-dimensional fixed line and an irreducible two-dimensional action, it is \(1+29z+30z^2+16z^3+44z^4\). The presence or absence of rational eigenlines is exactly detected by the rank-three coefficient.

## Relationship to prior work
Mondal and Saha, *Nijenhuis operators on Leibniz algebras* (arXiv:2306.06428v1, first public June 10, 2023), provide the Nijenhuis Leibniz formalism and general deformation theory; their treatment does not supply the present hemisemidirect rank-one scalar-deviation census. Li, Ma and Wang, *When Leibniz algebras are Nijenhuis?* (arXiv:2310.14267, first public October 22, 2023), develop the bialgebraic Nijenhuis relationship and low-dimensional triangular classifications, not this finite-field spectral classification. Standard hemi-semidirect constructions motivate the object. Existing indexed Nijenhuis enumerations for almost-abelian *Lie* algebras concern skew-symmetric brackets and either square-zero rank-one operators or idempotent projections. They do not directly imply the present left-Leibniz classification, which contains both the \(\varphi(u)=0\) and \(\varphi(u)\ne0\) branches and an exact rank polynomial for an arbitrary invertible action \(T\).

## Limitations
Originality is assessed against the specifically inspected primary sources and indexed results, not against every possible general Nijenhuis classification. Full texts of some relevant indexed works could not be inspected; a broader operator-theoretic classification could potentially subsume these formulas. This theorem is limited to the intrinsic rank-one scalar-deviation stratum and does not address arbitrary-rank deviations, automorphism-orbit classification, or the full scheme geometry. The exact rank-three versus invertibility comparison is only a corank-one detector for \(d\ge3\). Independent mathematical verification has not been performed.

## References
- B. Mondal and R. Saha, *Nijenhuis operators on Leibniz algebras*, arXiv:2306.06428v1 (June 10, 2023), https://arxiv.org/abs/2306.06428.
- H. Li, T. Ma and S. Wang, *When Leibniz algebras are Nijenhuis?*, arXiv:2310.14267v1 (October 22, 2023), https://arxiv.org/abs/2310.14267.
- Y. Sheng, R. Tang and C. Zhu, *The Controlling L-infinity Algebra, Cohomology and Homotopy of Embedding Tensors and Lie–Leibniz Triples*, Communications in Mathematical Physics (2021), https://link.springer.com/article/10.1007/s00220-021-04032-y.
