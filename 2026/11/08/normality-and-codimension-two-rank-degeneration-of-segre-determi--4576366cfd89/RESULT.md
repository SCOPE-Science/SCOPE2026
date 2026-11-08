# Normality and codimension-two rank degeneration of Segre-determinantal loci

## Finding
Let \(r\ge2\), \(m_i\ge1\), \(d=\sum_{i=1}^r m_i\), and \(M+1=\prod_{i=1}^r(m_i+1)\). Let \(B=\prod_{i=1}^r\mathbb P^{m_i}_{\mathbb C}\) with its Segre embedding \(\sigma:B\hookrightarrow\mathbb P^M\). For every \(n\ge M+1\), let \(X\subseteq B^n\) be the locus of ordered configurations \((p_1,\ldots,p_n)\) for which the Segre vectors \(\sigma(p_i)\) span a linear subspace of vector dimension at most \(M\). Use the natural maximal-minor scheme structure.

**Theorem.** The projective variety \(X\) is integral, Cohen--Macaulay, and **normal**. Its rank-at-most-\(M-1\) sublocus \(X_{<M}\) has codimension at least two in \(X\). Moreover, writing \(X_M=X\setminus X_{<M}\), the singular locus of \(X_M\) is contained in the configurations for which the *unique* common Segre hyperplane is tangent to \(\sigma(B)\) at one or more of the points. This containing tangency locus in \(X_M\) has codimension at least \(d\) (and hence at least two).

These are statements about the **multiprojective** degeneracy scheme, not about the affine multicone defined by its multihomogeneous equations. The normality assertion strengthens the previously established primality and Cohen--Macaulayness of the natural maximal-minor ideal.

## Assumptions and scope
All varieties are over \(\mathbb C\). Every \(m_i\) is positive, so \(d\ge2\), and the Segre variety is smooth, irreducible, and nondegenerate. The inequality \(M\ge d+1\) follows because \(\prod_i(m_i+1)\ge d+2\) for at least two positive factors. Let \(N=M+1\) be the number of Segre coordinates. The \(n\times N\) evaluation matrix has rank at most \(M\) precisely on \(X\); rank \(M\) corresponds to a unique point of the dual projective space \((\mathbb P^M)^*\). The results on primality and Cohen--Macaulayness of its maximal-minor ideal are used from Alstad--Duff--Katzman [1], Sections 2--3; all new geometric steps are proved below.

## Proof
**1. Hyperplane incidence and its dimension.** Set
\[
W=\{((p_1,\ldots,p_n),H)\in B^n\times(\mathbb P^M)^*:H(\sigma(p_i))=0\ (1\le i\le n)\}.
\]
The map \(q:W\to(\mathbb P^M)^*\) has fiber \((B\cap H)^n\). Since \(B\) is nondegenerate and positive-dimensional, every hyperplane section \(B\cap H\) is a nonempty effective Cartier divisor of pure dimension \(d-1\), including when it is singular or reducible. Consequently all fibers of \(q\) have dimension \(n(d-1)\), and \(W\) has dimension
\[
D=M+n(d-1).
\]
In fact \(W\) is irreducible: for generic \(H\), Bertini's theorem makes \(B\cap H\) smooth and irreducible (since \(d\ge2\)), so the generic fiber is irreducible; there cannot be a component lying entirely over a proper closed subset of the dual base, as the constant-fiber-dimension bound would give that subset's preimage dimension at most \(D-1\), whereas \(W\) is a pure codimension-\(n\) complete intersection in the smooth ambient product. (Purity follows from the \(n\) incidence equations and the just-established dimension.) Thus \(W\) is irreducible of dimension \(D\).

The projection \(\pi:W\to B^n\) has image \(X\), and the fiber over a configuration of Segre matrix rank \(s\le M\) is precisely \(\mathbb P^{M-s}\). The rank-\(M\) locus is nonempty: choose the \(M\) coordinate Segre points corresponding to all tensor basis vectors except one; they span the coordinate hyperplane in \(\mathbb P^M\). Repetitions fill any additional positions. Hence \(X\) has dimension \(D\), and \(\pi\) is birational. Over the rank-\(M\) locus \(X_M\), the one-dimensional kernel of the evaluation matrix determines the hyperplane by its signed \(M\times M\) minors. Those minor expressions give regular local inverse maps, so \(\pi^{-1}(X_M)\cong X_M\) **scheme-theoretically**.

**2. Smallness of the rank-drop image.** Let \(E=\pi^{-1}(X_{<M})\). It is a proper closed subset of the irreducible \(D\)-dimensional variety \(W\), so \(\dim E\le D-1\). Every fiber of \(E\to X_{<M}\) has dimension \(M-s\ge1\). The fiber dimension inequality yields
\[
\dim X_{<M}\le\dim E-1\le D-2,
\]
which proves \(\operatorname{codim}_X X_{<M}\ge2\). This does not assert that \(\pi\) is finite; it is not finite on the rank-drop locus.

**3. Codimension-one regularity on the incidence space.** Write the equations of \(W\) as \(F_i(p_i,H)=H(\sigma(p_i))=0\). If \(H\) is **not** tangent to \(\sigma(B)\) at any of the \(p_i\), then each differential \(dF_i\) is nonzero along the tangent directions belonging to its own \(p_i\). Those tangent blocks are disjoint across \(i\), so the \(n\) differentials are linearly independent. Thus \(W\) is smooth there.

Let \(T_i\) be the locus in \(W\) where \(H\) contains the embedded tangent space to \(\sigma(B)\) at \(p_i\). The incidence of tangent hyperplanes and marked points has dimension
\[
\dim\{(p,H):H\supset T_{\sigma(p)}\sigma(B)\}
=d+(M-d-1)=M-1.
\]
For each such pair the remaining \(n-1\) points lie in \(B\cap H\), which has dimension \(d-1\) independently of the tangency. Hence
\[
\dim T_i\le M-1+(n-1)(d-1)=D-d.
\]
It follows that \(\operatorname{Sing}(W)\subseteq\bigcup_i T_i\), and the singular locus of \(W\) has codimension at least \(d\ge2\). At rank \(M\), the isomorphism above carries this inclusion to the asserted singular/tangency bound on \(X_M\). **No converse is claimed**: an individual tangency need not make the full incidence singular because variations of \(H\) may still give independent differentials.

**4. Serre's criterion.** By [1], the natural maximal-minor ideal defines an integral Cohen--Macaulay multiprojective scheme \(X\). Consequently its local rings satisfy Serre's condition \((S_2)\). By Step 2, every codimension-one point of \(X\) lies in \(X_M\). Steps 1 and 3 show that \(X_M\) is regular in codimension one, hence \(X\) satisfies \((R_1)\). The integral Noetherian scheme \(X\) therefore satisfies \((R_1)+(S_2)\), and is normal.

## Verification
The proof is infinite and geometric; there is no exhaustive finite enumeration. The accompanying `verify.py` is a finite exact-arithmetic check of the key explicit rank-\(M\) construction (coordinate Segre vectors spanning a hyperplane) and the dimension/codimension inequalities for several product parameters. Execute `python3 verify.py` with the Python standard library. It is not used to replace either the geometric dimension arguments or the published Cohen--Macaulay theorem. The essential check is that every rank-drop fiber has positive dimension and that the tangent-hyperplane incidence bound is \(D-d\), strictly below \(D-1\).

## Relationship to prior work
Alstad, Duff and Katzman [1] prove the maximal-minor scheme is irreducible/prime and Cohen--Macaulay and establish a universal Gröbner basis, with an application to the image variety for three flatland cameras. Those properties by themselves do **not** imply normality: Cohen--Macaulay integral schemes may fail to satisfy \((R_1)\). The present proof adds explicit smallness of the rank-drop locus and a codimension estimate for the tangency obstruction, giving \((R_1)\) uniformly. Pratt's Segre-determinant work [2] studies the square determinant, Chow--Lam interpretation and applications, not a general normality criterion for these multiprojective rank loci. The line-multiview determinantal results of Breiding, Rydell, Shehu and Torres [3] involve a different camera incidence model.

## Limitations
This theorem requires at least two positive-dimensional Segre factors and concerns the maximal-minor **multiprojective** incidence \(n\ge M+1\) over \(\mathbb C\). It does not establish that the associated affine multicone is integrally closed, does not calculate the exact singular locus or its scheme structure, and does not resolve exceptional camera configurations not equivalent to the specified Segre rank model. Historical priority, including implicit normality implications of broader determinantal-incidence results, is not independently certified.

## References
[1] C. Alstad, T. Duff, M. Katzman, *Segre-Determinantal Loci and the Image Variety for Three Flatland Cameras*, arXiv:2606.31965v1 (first publicly posted 2026-06-30); specifically the prime/Cohen--Macaulay maximal-minor results in Section 2.

[2] E. Pratt, *The Segre Determinant*, arXiv:2505.09204v1 (first publicly posted 2025-05-14).

[3] P. Breiding, F. Rydell, E. Shehu, A. Torres, *Line Multiview Varieties*, arXiv:2203.01694 (first publicly posted 2022-03-03), SIAM J. Applied Algebra and Geometry, for comparison with another multiview model.
