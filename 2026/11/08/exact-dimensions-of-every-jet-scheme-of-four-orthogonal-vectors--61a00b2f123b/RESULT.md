# Exact dimensions of every jet scheme of four orthogonal vectors in three dimensions

## Finding
Let \(k=\mathbb C\). Let \(X\subset\mathbb A_k^{12}\) be defined by the six off-diagonal Gram equations \(\langle v_i,v_j\rangle=0\) for \(1\le i<j\le4\), where the four columns \(v_i\) lie in a nondegenerate three-dimensional quadratic space. For every integer \(L\ge1\), let \(J_L(X)\) be the scheme of \(k[t]/(t^L)\)-points, represented by the coefficient equations of these six Gram products. Then

\[
\boxed{\dim J_L(X)=\left\lfloor\frac{13L}{2}\right\rfloor\qquad(L\ge1).}
\]

In particular, the dimensions at lengths \(L=1,2,3,4,5,6\) are \(6,13,19,26,32,39\). The result supplies the previously untreated odd lengths for this natural non-log-canonical off-diagonal Gram zero fiber. All dimensions are Krull dimensions of schemes over \(\mathbb C\), not counts of finite-field points.

## Assumptions and scope
The characteristic is zero and the quadratic form is nondegenerate. Over \(\mathbb C\), all nondegenerate three-dimensional symmetric bilinear forms are linearly isometric, so use the split form
\[
B((x,y,z),(x',y',z'))=xy'+yx'+zz'.
\]
Write \(R_L=\mathbb C[t]/(t^L)\). The scheme \(J_L(X)\) is the affine scheme with \(12L\) coefficient coordinates obtained from \(B(v_i(t),v_j(t))=0\) in \(R_L\) for all six pairs. No reducedness or irreducibility assertion is needed.

## Proof
**1. Uniform upper bound.** The published log-canonical-threshold formula for off-diagonal Gram ideals gives
\[
\operatorname{lct}(I_{3,4})=\min\left\{6,\min_{0\le k\le2}\left(\binom{k+1}{2}+\frac{3(4-k)}2\right)\right\}=\frac{11}{2}.
\]
The same work establishes the bound \(\dim J_L(X_{M,h})\le L(Mh-\operatorname{lct}(I_{M,h}))\) for every \(L\ge1\), whether even or odd. Consequently
\[
\dim J_L(X)\le\left\lfloor\frac{13L}{2}\right\rfloor.
\]
This is an input from Xie (2026), not a newly proved general bound.

**2. An explicit isotropic chart.** In \(R_L\), choose arbitrary \(p,r\), with the constant term of \(p\) nonzero, and define
\[
A=\left(p,-\frac{r^2}{2p},r\right),\quad
z=\left(0,-\frac rp,1\right),\quad
b=\left(0,\frac1p,0\right).
\]
All divisions are valid because \(p\) is a unit in \(R_L\). Direct multiplication gives
\[
B(A,A)=B(A,z)=B(z,b)=0,\qquad
B(A,b)=B(z,z)=1.
\]
There are exactly \(2L\) independent coefficient parameters for \(A\): the \(L\) coefficients of each of \(p\) and \(r\), with one open nonvanishing condition.

**3. The maximal-dimensional jet family.** For a specified length \(L\), put \(a=\lfloor L/2\rfloor\). Choose arbitrary triples \((Y_2,Y_3,Y_4)\in R_L^3\) and \((W_2,W_3,W_4)\in(R_L/t^{L-a})^3\). Let
\[
v_1=A,\qquad v_j=A Y_j+t^a z W_j\quad(j=2,3,4).
\]
When \(L=2a\) is even, impose no further conditions. Each off-diagonal pairing with \(v_1\) vanishes; for \(i,j>1\) one has \(B(v_i,v_j)=t^{2a}W_iW_j=0\pmod{t^L}\). The parameter space has dimension \(2L+3L+3a=13a=13L/2\).

When \(L=2a+1\) is odd, impose the two coefficient equations \(W_3(0)=W_4(0)=0\), and, to select a nonempty open chart, require \(W_2(0)\ne0\). Then for distinct \(i,j\in\{2,3,4\}\), the product \(W_iW_j\) has zero constant coefficient, hence \(t^{2a}W_iW_j\) vanishes modulo \(t^{2a+1}\). The parameter-space dimension is
\[
2L+3L+3(a+1)-2=5L+3a+1=13a+6
=\left\lfloor\frac{13L}{2}\right\rfloor.
\]
For \(a=0\), this is a six-dimensional family of ordinary orthogonal frames; the construction includes that boundary case.

**4. No dimension loss under parametrization.** The first output column recovers \(A\), hence its first and third entries recover \(p,r\), and therefore \(z,b\). For each \(j=2,3,4\), the pairing \(B(b,v_j)\) recovers \(Y_j\); the pairing \(B(z,v_j)=t^aW_j\) recovers precisely all \(L-a\) coefficients of \(W_j\). Taking the coefficients of degrees \(a,\ldots,L-1\) is a regular inverse to multiplication by \(t^a\) on the image. Thus each displayed family is isomorphic to its locally closed image and has the dimension counted above. The upper bound in Step 1 is attained for both parity classes, proving the formula for every \(L\ge1\).

## Verification
The standalone script `check_jets.py` uses only the Python standard library. Run `python3 check_jets.py`. It constructs exact rational coefficient examples for each \(1\le L\le15\), verifies the isotropic Witt identities, tests all six Gram products modulo \(t^L\), checks recovery of parameters, and compares the parameter dimensions with \(\lfloor13L/2\rfloor\). Its final line is `ALL_EXACT_POLYNOMIAL_CHECKS_PASS`. Those are bounded checks. The proof for unrestricted \(L\) is the coefficient-level algebra and published uniform upper bound above.

## Relationship to prior work
Ying Xie (2026), Theorem 1.2 and equation (5.1), supply the exact log-canonical threshold and upper bound. Corollary 7.1 determines jet dimensions when the ambient dimension or the length is even, but does not assert equality at odd length in odd ambient dimension. Section 7 gives an explicit counterexample to such equality in a different low-dimensional case; Section 8 explicitly asks about odd-length dimensions in odd ambient dimension. The present result adds a sharp odd-length lower construction for the specific three-dimensional, four-column zero fiber, showing its upper bound is attained after integral rounding at all lengths.

The broader zero-fiber variety is the orthogonal-frame variety, also known through the Lovász–Saks–Schrijver ideal of a complete graph. Conca and Welker (2019) study algebraic and prime/complete-intersection properties; Casabella and Sammartano (2025/2026) study orthogonal-frame components and singularity properties. The accessible comparisons do not establish this all-length jet-dimension formula. The full text of the latter work was unavailable for direct comparison, which leaves a priority risk.

## Limitations
The statement determines dimensions, not irreducible-component counts, primary decompositions, reduced structures, motivic measures, or arbitrary coefficient fibers. It is specific to four vectors in complex dimension three and does not resolve the general odd-length/odd-ambient question for other parameters. The upper bound depends on a published theorem; the lower construction is supplied directly. An independent audit and exhaustive historical-priority verification have not been performed.

## References
1. Y. Xie, *Sharp FRS and singularity thresholds for off-diagonal Gram maps*, arXiv:2610.02585v1 (publicly submitted 2026-10-01), especially Theorem 1.2, (5.1), Corollary 7.1, Sections 7–8. https://arxiv.org/html/2610.02585v1
2. L. Casabella and A. Sammartano, *The variety of orthogonal frames*, arXiv:2512.25058 (first submitted 2025-12-31). https://arxiv.org/abs/2512.25058
3. A. Conca and V. Welker, *Lovász–Saks–Schrijver ideals and coordinate sections of determinantal varieties*, Algebra & Number Theory 13 (2019), 455–484, arXiv:1801.07916. https://arxiv.org/abs/1801.07916
