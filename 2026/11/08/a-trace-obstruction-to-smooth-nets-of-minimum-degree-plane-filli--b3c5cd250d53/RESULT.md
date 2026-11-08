# A trace obstruction to smooth nets of minimum-degree plane-filling curves in characteristic three

## Finding
Let \(q=3^r\), with \(r\geq 1\), and put \(k=\mathbb F_q\). Let \(W_q\) be the vector space of degree-\(q+2\) homogeneous equations over \(k\) that vanish at every point of \(\mathbb P^2(k)\). Call a nonzero equation **smooth** if its projective zero curve is smooth over \(\overline{k}\); a subspace is **rationally all-smooth** if each of its nonzero \(k\)-rational equations is smooth.

**Theorem.** For every such \(q\), the largest possible \(k\)-dimension of a rationally all-smooth linear subspace \(V\subset W_q\) is exactly \(2\). Thus there exist pencils of \(q+1\) distinct smooth minimum-degree plane-filling curves, but **no projective net** all of whose \(q^2+q+1\) rational members are smooth.

More precisely, \(W_q\) has a canonical (up to a common nonzero factor under projective change of coordinates) nonzero linear trace functional \(\mathcal T\). Every rationally all-smooth pencil \(\mathbb P(V)\) contains **exactly one** rational member in \(\mathbb P(\ker\mathcal T)\). Every individual smooth member of \(W_q\) extends to a rationally all-smooth pencil. These statements hold simultaneously for every exponent \(r\geq1\), without an assumption that all geometric pencil members are smooth.

## Assumptions and scope
Fix coordinates \([X:Y:Z]\) and let
\[
 U=Y^qZ-YZ^q,\quad V_0=Z^qX-ZX^q,\quad W_0=X^qY-XY^q.
\]
For \(A\in M_3(k)\), put
\[
 F_A=(X,Y,Z)A(U,V_0,W_0)^{\mathsf T}.
\]
The established Homma--Kim matrix criterion (reference 1, Lemma 3.1 and Theorem 3.2) states that \(A\mapsto F_A\) induces an isomorphism \(M_3(k)/kI_3\simeq W_q\), and \(F_A\) is geometrically smooth exactly when \(\det(tI_3-A)\in k[t]\) is an irreducible cubic. Smoothness concerns all points over \(\overline{k}\). All-smoothness of a pencil or net concerns only its \(k\)-rational members, not every member after extending the parameter field.

Since \(\operatorname{char}k=3\), the function
\[
 \mathcal T(F_A)=\operatorname{tr}(A)
\]
is well-defined: adding a scalar matrix changes the trace by \(3\mu=0\). It is nonzero, for example on the class of \(\operatorname{diag}(1,0,0)\). The zero condition is unchanged by scaling \(F_A\), and under projective coordinate changes it is unchanged because the matrix action is conjugation followed by nonzero scalar multiplication and scalar-matrix addition (references 1 and 2).

## Proof
**1. The necessary quadratic condition.** Put \(H=\ker\mathcal T\). For an element \(F_A\in H\), choose any representing matrix \(A\) with \(\operatorname{tr}(A)=0\). Its characteristic polynomial has form
\[
 \det(tI_3-A)=t^3+c(A)t+d(A),\qquad
 c(A)=-\tfrac12\operatorname{tr}(A^2).
\]
Set \(Q(F_A)=-c(A)=\tfrac12\operatorname{tr}(A^2)\). This is a homogeneous quadratic form on \(H\): upon replacing \(A\) by \(A+\mu I_3\), its trace-square expression is unchanged because
\[
 \operatorname{tr}((A+\mu I_3)^2)
 =\operatorname{tr}(A^2)+2\mu\operatorname{tr}(A)+3\mu^2
 =\operatorname{tr}(A^2).
\]
Here \(\tfrac12\) means the inverse of \(2\) in \(k\). If \(F_A\ne0\) is smooth, \(t^3+c(A)t+d(A)\) has no root in \(k\). Consider the additive map
\[
 L_A:k\longrightarrow k,\qquad t\longmapsto t^3+c(A)t.
\]
If \(L_A\) were injective, it would be surjective (\(k\) is finite), and we could find \(t\in k\) with \(L_A(t)=-d(A)\), contradicting irreducibility. Hence \(L_A\) has a nonzero kernel element \(t\), and \(t^2=-c(A)=Q(F_A)\). Thus
\[
 \boxed{\text{smooth }F\in H\setminus\{0\}\ \Longrightarrow\ Q(F)\in(k^\times)^2.}
\]
The square is necessarily nonzero; this is only a *necessary* condition for smoothness, not a sufficient one.

**2. Binary quadratic obstruction.** We use the following lemma: for every finite field \(k\) of odd order and every quadratic form \(R:k^2\to k\), either \(R\) has a nonzero isotropic vector, or \(R\) represents every element of \(k^\times\). To prove it, if \(R\) has no nonzero zero then it is nondegenerate, so diagonalization gives \(R(s,t)=a(s^2-\delta t^2)\) with \(a\ne0\) and a nonsquare \(\delta\in k^\times\). This is the scalar multiple of the norm of \(s+t\sqrt\delta\in k(\sqrt\delta)=\mathbb F_{q^2}\). The finite-field norm is surjective onto \(k^\times\): if \(g\) generates \(\mathbb F_{q^2}^\times\), then \(g^{q+1}\) generates \(k^\times\). This proves the lemma, including degenerate forms (which have a nonzero radical vector).

In particular **no quadratic form on a two-dimensional \(k\)-space has its entire punctured domain mapped into the nonzero squares**, because a nonzero zero or a nonsquare value must occur.

**3. No all-smooth trace-zero plane.** Suppose \(L\subset H\) has \(k\)-dimension \(2\) and every nonzero member of \(L\) is smooth. By Step 1, the restriction \(Q|_L\) takes only nonzero square values on \(L\setminus\{0\}\), contrary to Step 2. Thus no such \(L\) exists.

**4. No all-smooth net and uniqueness of the distinguished pencil member.** If \(V\subset W_q\) has dimension at least \(3\), the kernel of \(\mathcal T|_V\) has dimension at least \(2\). The contradiction of Step 3 therefore shows \(V\) cannot be rationally all-smooth. If instead \(V\) is a rationally all-smooth \(2\)-space, \(V\cap H\) has dimension at least \(1\), and Step 3 shows its dimension is exactly \(1\). Hence the pencil contains exactly one trace-zero rational projective member. The invariance of the trace-zero condition under changes of projective coordinates was explained in the assumptions, so this member is intrinsically distinguished within the embedded linear system.

**5. Sharpness and extension of each individual smooth member.** Let \(F_A\in W_q\) be any smooth equation. Because the characteristic polynomial of \(A\) is irreducible cubic, \(K=k[A]\subset M_3(k)\) is a field of degree \(3\) over \(k\). Choose \(B\in K\setminus(kI_3+kA)\), possible since \(\dim_k K=3\). Then every nonzero element \(sA+tB\) of \(\operatorname{span}_k\{A,B\}\) lies outside \(kI_3\): otherwise \(I_3,A,B\) would be linearly dependent. Every element of \(K\setminus kI_3\) generates \(K\) over \(k\), since the extension has prime degree \(3\); thus its multiplication matrix has irreducible cubic characteristic polynomial. The image of \(\operatorname{span}_k\{A,B\}\) in \(M_3(k)/kI_3\) is a \(2\)-space consisting entirely of smooth nonzero equations and containing \(F_A\). This produces a pencil over every \(k\), proves the bound is sharp, and establishes the extension assertion. \(\square\)

## Verification
The standalone `verify_trace_obstruction.py` requires only Python 3's standard library. Run `python3 verify_trace_obstruction.py` from the directory containing the script. It exhaustively checks all \(729\) binary quadratic forms over \(\mathbb F_9\), independently confirming the required nonzero-isotropic-or-nonsquare alternative; it enumerates all \(576\) smooth plane-filling quintic equations and all \(2016\) smooth-member pencils over \(\mathbb F_3\), finding precisely one trace-zero member per pencil; and it verifies a four-member explicit matrix-pencil witness. Recorded output:

```
F9_QUADRATIC_ALTERNATIVE_PASS 729
F3_TALLINI_PENCILS_PASS 576 144 2016
F3_FIELD_MULTIPLICATION_WITNESS_PASS
```

The exact all-\(\mathbb F_{3^r}\) assertion follows from the algebraic proof in Steps 1--5, not extrapolation from these finite checks. The coefficient \(Q\) is the negative linear characteristic coefficient only on the trace-zero hyperplane; no assertion is made that it descends as a quadratic form to all of \(W_q\).

## Relationship to prior work
Homma--Kim (2009/2013) prove the matrix presentation and smoothness criterion for individual minimum-degree plane-filling curves. Homma (2019/2020) studies reducible members and projective equivalence via the same matrix representation. Their individual-curve criteria are used here as prior results, not claimed as new. Asgarli--Ghioca (2022/2023) ask for pencils with every rational member smooth and prove general existence under field-size hypotheses not tailored to degree \(q+2\). Their 2023 study addresses higher-degree plane-filling curves. The added assertion here is the **all-characteristic-three sharp net obstruction**, the projectively meaningful **unique trace-zero member of every smooth pencil**, and **pencil extension through every smooth member**.

An earlier finite census over \(\mathbb F_3\) already reports the absence of such nets in that single field. That finite case is not asserted as new. Its enumeration does not imply the proof for every extension field \(\mathbb F_{3^r}\), nor does it provide the invariant trace-zero uniqueness for every such field.

## Limitations
The result applies to degree \(q+2\) plane-filling equations over finite fields of characteristic \(3\), not to arbitrary degree or characteristic. It restricts rational members of linear systems; a pencil may have singular members for parameters over field extensions. The quadratic-square condition is necessary, not sufficient, for smoothness; thus it is not a classification of all pencils or their projective orbits. It does not assert that general finite-field smooth nets of degree \(q+2\) without the plane-filling condition are impossible. Historical priority relative to unindexed finite-geometric treatments of matrix subspaces remains a risk; independent validation has not been performed.

## References
1. M. Homma and S. J. Kim, *Nonsingular plane filling curves of minimum degree over a finite field and their automorphism groups: Supplements to a work of Tallini*, arXiv:0903.1918, first public March 11, 2009; Lemma 3.1 and Theorem 3.2. https://arxiv.org/abs/0903.1918
2. M. Homma, *Fragments of plane filling curves of degree q+2 over the finite field of q elements, and of affine-plane filling curves of degree q+1*, arXiv:1906.00164, first public June 1, 2019; Section 2 and Theorem 2.4. https://arxiv.org/abs/1906.00164
3. S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first public March 14, 2022; Question 1.2, Theorem 1.3, and Section 3. https://arxiv.org/abs/2203.07169
4. S. Asgarli and D. Ghioca, *Plane-filling curves of small degree over finite fields*, arXiv:2307.03072, first public July 6, 2023. https://arxiv.org/abs/2307.03072
