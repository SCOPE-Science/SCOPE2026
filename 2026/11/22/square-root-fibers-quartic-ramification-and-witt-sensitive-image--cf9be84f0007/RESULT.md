# Square-root fibers, quartic ramification, and Witt-sensitive images in finite spin-factor Jordan algebras

## Finding

For every odd prime power \(q\), every integer \(d\geq2\), and every nondegenerate symmetric bilinear form \(B\) on \(V=\mathbb F_q^d\), let \(Q(v)=B(v,v)\) and form the spin-factor Jordan algebra \(J=\mathbb F_q1\oplus V\). The squaring map \(\Phi:J\to J\), \(x\mapsto x\circ x\), has a pointwise exact fiber law and a closed image cardinality. It distinguishes the two quadratic-form discriminant classes as soon as \(q\geq5\), but not when \(q=3\).

Put \(H=(\mathbb F_q^\times)^2\), \(h=|H|=(q-1)/2\), and define \(T_0,T_+,T_-\) to be the number of vectors \(v\) with \(Q(v)=0\), with \(Q(v)=s\) for any fixed nonzero square \(s\), or with \(Q(v)=s\) for any fixed nonsquare \(s\), respectively. For a target \((b,w)\in\mathbb F_q\oplus V\), the exact number of square roots is

\[
N(b,w)=\#\Phi^{-1}(b,w)=
\begin{cases}
T_0,&w=0,\ b=0,\\
T_++2,&w=0,\ b\in H,\\
T_-,&w=0,\ b\in\mathbb F_q^\times\setminus H,\\
2\#\{t\in H:t^2-bt+Q(w)/4=0\},&w\ne0.
\end{cases}
\]

Every scalar target \((b,0)\) is attained. All fibers over nonzero \(w\) have cardinality \(0,2\), or \(4\). More precisely, for any fixed \(w\ne0\), write \(s=Q(w)\). If \(s=0\) or \(s\notin H\), there are exactly \(h\) attained scalar coordinates \(b\), with exactly two roots each. If \(s\in H\), let \(f_s=\#\{t\in H:t^2=s/4\}\). There are exactly \(f_s\) values of \(b\) with two roots, and \((h-f_s)/2\) values with four roots; all other scalar coordinates are unattained. The integer \(f_s\) is nonzero exactly when \(s/4\) is a fourth power; it equals \(\gcd(2,h)\) then. Thus the individual fibers can detect a quartic-residue condition even where the total image depends only on the quadratic discriminant.

The numbers of attainable targets with \(w\ne0\) and precisely two or four roots are, respectively,

\[
M_2=(T_0-1)h+T_-h^2+T_+h,\qquad
M_4=T_+\frac{h(h-1)}2.
\]

In particular the entire square image has size

\[
\boxed{|\Phi(J)|=q+(T_0-1)h+T_-h^2+T_+\frac{h(h+1)}2.}
\]

Let \(\delta=\det B\) in any basis and \(\chi\) be the quadratic character of \(\mathbb F_q^\times\). Write \(\epsilon=\chi((-1)^{\lfloor d/2\rfloor}\delta)\). Then

\[
(T_0,T_+,T_-)=
\begin{cases}
(q^{d-1}+(q-1)\epsilon q^{d/2-1},\,q^{d-1}-\epsilon q^{d/2-1},\,q^{d-1}-\epsilon q^{d/2-1}),&d\text{ even},\\
(q^{d-1},\,q^{d-1}+\epsilon q^{(d-1)/2},\,q^{d-1}-\epsilon q^{(d-1)/2}),&d\text{ odd}.
\end{cases}
\]

Equivalently,

\[
\boxed{|\Phi(J)|=q-h+\frac32q^{d-1}h(h+1)+
\begin{cases}
\epsilon\frac{h(h-1)}2q^{d/2-1},&d\text{ even},\\
-\epsilon\frac{h(h-1)}2q^{(d-1)/2},&d\text{ odd}.
\end{cases}}
\]

For fixed \(q\), the image density tends to \(3(q^2-1)/(8q^2)\) as \(d\to\infty\); for fixed \(d\ge2\), it tends to \(3/8\) as \(q\to\infty\) through odd prime powers. For \(q\ge5\), opposite discriminant classes have different image sizes, whereas for \(q=3\) both classes give the same image size.

## Assumptions and scope

The field has odd characteristic and the bilinear form is nondegenerate. The dimension \(d\) is at least two; no isotropy assumption is imposed. All square-root counts are counts of elements, not automorphism orbits or scheme-theoretic multiplicities. The scalar/vector coordinates are relative to the canonical decomposition \(J=\mathbb F_q1\oplus V\). The determinant class does not depend on the chosen basis because change of basis multiplies \(\det B\) by a square. The special treatment of characteristic two is outside the claim.

## Proof

**1. Eliminate the vector variable.** By the defining Jordan product,

\[
(a,v)\circ(b,w)=(ab+B(v,w),aw+bv),\qquad
\Phi(a,v)=(a^2+Q(v),2av).
\]

If the target has \(w=0\), then \(2av=0\), so either \(a=0\) or \(v=0\). When \(b=0\), only \(a=0\) contributes (the other possibility is the same zero element), producing \(T_0\) roots. When \(b\ne0\), the branch \(a=0\) contributes \(T_+\) or \(T_-\) roots according to the square class of \(b\). The branch \(v=0\) contributes two additional roots exactly when \(b\) is a nonzero square. This proves the scalar cases. The standard finite-field nondegenerate quadratic-form count listed below gives \(T_0,T_+,T_->0\) for \(d\ge2\), so all scalar targets occur.

For \(w\ne0\), necessarily \(a\ne0\), and the vector equation has exactly one solution \(v=w/(2a)\) for each \(a\). Substitution into the scalar equation gives \(b=a^2+Q(w)/(4a^2)\). Put \(t=a^2\in H\). Each \(t\) has exactly two square roots \(a\), and the scalar equation becomes \(t^2-bt+Q(w)/4=0\). This proves the pointwise fiber formula, including zero fibers.

**2. Count distinct scalar coordinates for a fixed nonzero vector target.** For \(c=Q(w)/4\), consider \(\varphi_c:H\to\mathbb F_q\), \(t\mapsto t+c/t\). If \(\varphi_c(t)=\varphi_c(u)\), then \((t-u)(1-c/(tu))=0\): either \(t=u\) or \(tu=c\). If \(c=0\), or \(c\) is a nonsquare, the second alternative is impossible unless \(t=u\); hence \(\varphi_c\) is injective and has exactly \(h\) outputs, each with one parameter \(t\) and two square roots. If \(c\in H\), then \(t\mapsto c/t\) is an involution of \(H\). Its fixed-point count is \(f_s=\#\{t\in H:t^2=c\}\). Singleton orbits have two algebra roots; two-element orbits have four. Consequently there are \(f_s\) two-root outputs and \((h-f_s)/2\) four-root outputs. Since \(H\) is cyclic of order \(h\), the equation \(t^2=c\) in \(H\) has either zero or \(\gcd(2,h)\) solutions, exactly as claimed.

**3. Sum over vector targets.** There are \(T_0-1\) nonzero vectors of norm zero, \(T_-h\) vectors whose norm is a nonsquare, and \(T_+h\) whose norm is a nonzero square. The first two classes each supply \(h\) two-root scalar outputs per vector. In the third class the sum of \(f_s\) over all \(h\) square norms is precisely \(h\): multiplication by \(1/4\) permutes \(H\), and counting pairs \((s,t)\) with \(t^2=s/4\) directly counts the \(h\) choices of \(t\). Each norm value occurs for exactly \(T_+\) vectors. Therefore the two-root total is \((T_0-1)h+T_-h^2+T_+h\), and subtracting this from the \(T_+h\) times the total \(h\) parameter values shows that four-root outputs total \(T_+h(h-1)/2\). Summing all attained outputs (including the \(q\) scalar targets) yields the first image formula.

**4. Norm counts, discriminants and limits.** Diagonalizing the nondegenerate quadratic form and applying the quadratic Gauss-sum evaluation yields the displayed norm-value distributions. For completeness: for an additive nontrivial character \(\psi\), the orthogonality identity gives \(T_s=q^{-1}\sum_{\lambda\in\mathbb F_q}\psi(-\lambda s)\sum_{v\in V}\psi(\lambda Q(v))\). For \(\lambda\ne0\), diagonalization factors the inner sum into \(\chi(\lambda)^d\chi(\delta)G^d\), where \(G=\sum_{x\in\mathbb F_q}\psi(x^2)\) and \(G^2=\chi(-1)q\). If \(d\) is even, summing \(\psi(-\lambda s)\) produces \(q-1\) at \(s=0\) and \(-1\) at \(s\ne0\); if odd, quadratic character summation produces the plus/minus dichotomy. This gives exactly the stated \(T\)-formulas with \(\epsilon=\chi((-1)^{\lfloor d/2\rfloor}\delta)\).

Substitute these into the image count, and use \(q-1=2h\). The common term simplifies to \(q-h+\frac32q^{d-1}h(h+1)\), and the sign term becomes \(\epsilon h(h-1)q^{d/2-1}/2\) for even dimension and its negative times \(q^{(d-1)/2}\) in odd dimension. When \(q=3\), \(h=1\), so the discriminant term vanishes; for \(q\ge5\) the coefficient is nonzero. Finally dividing by \(\#J=q^{d+1}\) gives the fixed-field and large-field limits. No classification of Jordan-algebra isomorphisms is needed for these counts.

## Verification

The independently executable `CHECKER.py` directly enumerates the square map, *all* input elements, and *all* possible target elements, including unattained targets, for \(q\in\{3,5,7,9,11\}\), dimensions \(d=2,3,4\), and both determinant square classes. It implements \(\mathbb F_9\) as \(\mathbb F_3[\theta]/(\theta^2+1)\) rather than incorrectly assuming prime-field arithmetic. All thirty complete cases verify every pointwise root formula, all zero and nonzero norm counts, exact two-/four-root target counts, and both equivalent image formulas. Recorded outputs are embedded as `CHECK_OUTPUT.json`; run with `python CHECKER.py` (Python 3, standard library only).

Exhaustive finite examples are corroboration, not proof for arbitrary field sizes or dimensions. The general proof is the four-step argument above.

## Relationship to prior work

Kaygorodov–Lopatin–Popov (arXiv:1511.00742, first posted 2015-11-02), especially Sections 2 and 4.3, supplies the established spin-factor product and quadratic trace/norm identity, while investigating derivations with invertible values. These foundational identities are not new and directly underlie the elimination step; the article does not present the prescribed finite-field squaring fibers, the quartic-residue branching, or the all-dimensional image cardinality derived here. Lemmens–Roelands–van Imhoff (arXiv:1609.08304, first posted 2016-09-27) studies order-theoretic characterization of real spin factors and their positive square cones rather than arithmetic point counts. Diniz–Souza (2016) treats graded identities of Jordan algebras of bilinear forms in characteristic zero; its abstract does not resolve the finite-field square-root problem. The arithmetic reduction also uses classical finite-field quadratic Gauss sums. Published related results on rank-one operators and associative closure in spin factors study different invariants and cannot by themselves imply the pointwise fiber formula.

## Limitations

The claim excludes characteristic two, degeneracy of \(B\), and dimension one. The counts are set-theoretic; singular fibers over extension rings and scheme structures are not addressed. The proof derives arithmetic counting from known quadratic-form theory and the elementary spin-factor squaring identity; an equivalent result in broader literature on quadratic Jordan maps remains a historical-priority risk. No independent expert audit has been performed. The exact pointwise fiber formula, not merely an image-density heuristic, is the asserted result.

## References

1. I. Kaygorodov, A. Lopatin, Y. Popov, *Jordan algebras admitting derivations with invertible values*, arXiv:1511.00742 (initial public posting 2015-11-02), https://arxiv.org/abs/1511.00742 .
2. B. Lemmens, M. Roelands, H. van Imhoff, *An order theoretic characterization of spin factors*, arXiv:1609.08304 (initial public posting 2016-09-27), https://arxiv.org/abs/1609.08304 .
3. D. Diniz, M. da Silva Souza, *Specht property for the 2-graded identities of the Jordan algebra of a bilinear form*, Communications in Algebra, DOI:10.1080/00927872.2016.1222402 (first online 2016-10-07), https://doi.org/10.1080/00927872.2016.1222402 .
