# Square-class-resolved reflection convolution and the exact two-step law in ternary orthogonal groups

## Finding
Let \(q\) be an odd prime power, and let \((V,Q)\) be a nondegenerate quadratic space of dimension \(n\ge2\) over \(\mathbb F_q\). Write \(\epsilon(a)\in\{+1,-1\}\) for the quadratic character of \(a\in\mathbb F_q^\times\). An anisotropic projective line \(\langle v\rangle\) determines the reflection \(r_v\) and its type \(\epsilon(Q(v))\). Let \(\mathcal R_+\) and \(\mathcal R_-\) be the two reflection types. For each \(g\in O(V,Q)\) define
\[
 F_{a,b}(g)=\#\{(r,s)\in\mathcal R_a\times\mathcal R_b:rs=g\},\qquad a,b\in\{+1,-1\}.
\]
For \(W_g=\operatorname{im}(I-g)\), let \(\theta(g)\) be the quadratic character of the Wall spinor norm. The exact prescribed-target convolution is:

1. If \(g=I\), then \(F_{a,b}(I)=\mathbf1_{a=b}N_a\), where \(N_a\) is the number of anisotropic lines of norm class \(a\). For \(n=2m+1\), put \(\kappa=\epsilon((-1)^m\det Q)\) and \(N_a=(q^{n-1}+a\kappa q^m)/2\); for \(n=2m\), put \(\kappa=\epsilon((-1)^m\det Q)\) and \(N_a=(q^{n-1}-\kappa q^{m-1})/2\).
2. If \(g\ne I\) and \(\dim W_g\ne2\), then \(F_{a,b}(g)=0\).
3. If \(\dim W_g=2\), then
\[
 F_{a,b}(g)=\mathbf1_{ab=\theta(g)}\,A_b(W_g),
\]
where \(A_b(W)\) is the number of projective lines \(\langle v\rangle\subseteq W\) with \(\epsilon(Q(v))=b\). Its complete evaluation is:
   * If \(Q|_W\) has rank two and \(\eta=\epsilon(-\det(Q|_W))\), then \(A_+(W)=A_-(W)=(q-\eta)/2\).
   * If \(Q|_W\) has rank one and its nonzero square class is \(c\), then \(A_c(W)=q\) and \(A_{-c}(W)=0\).
   * If \(Q|_W=0\), then \(A_+(W)=A_-(W)=0\).

For \(n=3\), write \(\kappa=\epsilon(-\det Q)\). Every \(g\in SO(V,Q)\) is a product of two reflections. Among the \(q(q^2-1)\) elements of this group, the complete *unrefined* number-of-factorizations spectrum is

| Fiber size \(\sum_{a,b}F_{a,b}(g)\) | Number of targets |
|---|---:|
| \(q^2\) | \(1\) (identity) |
| \(q-1\) | \(q(q+1)(q-2)/2\) |
| \(q\) | \(q^2-1\) |
| \(q+1\) | \(q^2(q-1)/2\) |

The class-resolved refinement is exact: the \(q^2-1\) targets with fiber size \(q\) occur **only** in \(\mathcal R_\kappa\mathcal R_\kappa\), with \(F_{\kappa,\kappa}(g)=q\) and all other four-class pairs having zero fibers at such \(g\). For a nondegenerate split moved plane the individual nonzero class-pair fiber is \((q-1)/2\), and for a nonsplit plane it is \((q+1)/2\), in both cases with \(ab=\theta(g)\). A split plane supports \((q-3)/2\) spinor-positive and \((q-1)/2\) spinor-negative targets; a nonsplit plane supports \((q-1)/2\) spinor-positive and \((q+1)/2\) spinor-negative targets. The numbers of split, nonsplit, and degenerate planes are \(q(q+1)/2\), \(q(q-1)/2\), and \(q+1\), respectively.

If two reflections are sampled independently and uniformly from their union (of cardinality \(q^2\)), then their product is supported on \(SO_3(q)\), and its total-variation distance from the uniform distribution on that group is **exactly**
\[
 \left\|\mu_{\mathcal R}^{*2}-U_{SO_3(q)}\right\|_{\mathrm{TV}}=
 \frac{q^2-q-1}{2q^2(q-1)}=\frac1{2q}+O(q^{-2}).
\]

## Assumptions and scope
All quadratic spaces are nondegenerate, all ground fields finite of odd cardinality, and factors are genuine nonidentity reflections, not arbitrary involutions or symplectic transvections. Matrices may be taken over any odd-prime-power finite field, including nonsplit quadratic spaces. \(\det Q\) denotes the determinant of a symmetric Gram matrix representing \(Q\), defined modulo squares; the signs \(\kappa,\eta\) are therefore basis-independent. The Wall spinor sign \(\theta(g)\) is the quadratic character of the determinant of the Wall bilinear form on \(W_g\), also basis-independent. The zero-dimensional determinant is one. For \(g\in O(V,Q)\), let \(B(u,v)=Q(u+v)-Q(u)-Q(v)\); the Wall form \(\chi_g\) is characterized by \(\chi_g((I-g)x,w)=B(x,w)\) for \(w\in W_g\), where the quotient definition is well-defined because \(W_g=(\ker(I-g))^\perp\).

## Proof
**Step 1 (a bijection, with exact factor order).** Define \(r_v(x)=x-B(x,v)v/Q(v)\) whenever \(Q(v)\ne0\). If \(g=r_u r_v\) with independent normal lines, then \(\operatorname{im}(I-g)\subseteq\langle u,v\rangle\). Since the product of two distinct reflections cannot be the identity or a reflection, its moved space has dimension two and equals that span. Conversely, for every anisotropic \(\langle v\rangle\subseteq W_g\) with \(\dim W_g=2\), Wall's reflection-shortening lemma gives \(\dim\operatorname{im}(I-r_vg)=1\). The latter orthogonal isometry is uniquely a reflection, say \(r_u\), so \(g=r_vr_u\). Each choice of the *first* reflection is therefore a unique ordered factorization. Applying the same argument to \(g^{-1}\), whose moved space and spinor sign agree with those of \(g\), and reversing the resulting ordered factors, shows that each choice of the *second* reflection is also a unique factorization. Thus \(F_{a,b}(g)=A_b(W_g)\) times the spinor condition. The spinor-norm homomorphism yields \(ab=\theta(g)\); in rank two the two factors' projective directions are distinct. If \(W_g\) is totally singular, no such factor exists. For \(g=I\), the second factor equals the first, and no other ranks can occur. The geometric correspondence and the spinor-norm law are the established Wall-factorization facts [1], not claimed as original here.

**Step 2 (count the lines and norm classes).** A nondegenerate binary quadratic form has two isotropic projective points when its discriminant sign \(\eta=+1\), and none when \(\eta=-1\). On the remaining \(q-\eta\) lines the nonzero norm square classes occur equally often: the usual norm-fiber computation gives \((q-\eta)/2\) for each. A binary form of rank one has a unique radical line, leaving \(q\) anisotropic lines of its single nonzero square class. A zero form has none. For a nondegenerate ambient form of dimension \(n\), count nonzero vectors with fixed nonzero norm and divide by \(q-1\), separating the \((q-1)/2\) norm values of each square class. Standard one-variable Gauss sums give \(N_a=(q^{n-1}+a\kappa q^{(n-1)/2})/2\) in odd \(n\) and \(N_a=(q^{n-1}-\kappa q^{(n-2)/2})/2\) in even \(n\), proving the general formula.

**Step 3 (the complete ternary target census).** In dimension three, every oriented isometry other than the identity has moved rank two: its determinant is one, an odd-dimensional reciprocal characteristic polynomial has eigenvalue one, and moved rank one would be a determinant-minus-one reflection. Also every two-plane contains an anisotropic line because the Witt index of a nonsingular ternary quadratic space is at most one. The number of isotropic normal lines is \(q+1\); taking the orthogonal complement gives \(q+1\) degenerate planes. The two anisotropic normal-line types have cardinalities \(q(q+1)/2\) and \(q(q-1)/2\), giving the asserted split/nonsplit plane counts (the types may interchange according to \(\kappa\)). A degenerate plane has nonzero norm class \(\kappa\).

Choose a basis of a fixed moved plane \(W\) and write \(S\) for the Gram matrix of \(Q|_W\). Every bilinear form on \(W\) whose diagonal equals \(Q|_W\) has the matrix \(S+\left(\begin{smallmatrix}0&t\\-t&0\end{smallmatrix}\right)\). Wall's parametrization [1] gives exactly one isometry with moved space \(W\) per nondegenerate such form. Its determinant is \(\det S+t^2\), and its spinor sign is \(\epsilon(\det S+t^2)\). If \(Q|_W\) is split, nonsplit or rank one, there are respectively \(q-2\), \(q\), or \(q-1\) admissible parameters \(t\). In the first two cases, \(\sum_{t\in\mathbb F_q}\epsilon(t^2+d)=-1\) for \(d\ne0\) gives the claimed per-plane spinor-positive and -negative counts. In the rank-one case admissibility means \(t\ne0\), so the spinor sign is positive and the unique nonzero norm class is \(\kappa\). Multiplying these per-plane numbers yields the four rows of the target table; they add to \(q(q^2-1)\). All determinant-minus-one elements have empty fibers.

**Step 4 (sharp two-step mixing).** The source has \(q^2\) reflections, hence \(q^4\) equiprobable ordered pairs. The uniform fiber benchmark on \(SO_3(q)\) is \(q^4/[q(q^2-1)]\), which lies strictly between \(q\) and \(q+1\) for odd \(q\ge3\). Only the identity and the \(q^2(q-1)/2\) nonsplit-plane targets exceed this benchmark. Summing the two positive deviations and dividing by \(q^4\) gives exactly \((q^2-q-1)/(2q^2(q-1))\); the remaining deviations have the opposite sign. This establishes the stated total variation distance.

## Verification
The accompanying standalone script `orthogonal_fibers_check.py` constructs reflections directly, multiplies ordered pairs, and computes the Wall spinor sign by solving its defining linear equations; it does not infer the expected class counts from the observed products. Over prime fields of orders 3, 5 and 7 it exhaustively tests the predicted square-class-resolved fiber law for all attainable products in dimensions two, three and four, including both binary quadratic types. Where feasible it also generates every orthogonal element to verify zero fibers away from the predicted support. All ten configurations pass, including all ternary global spectra, exact total-variation values \(5/36\), \(19/200\), and \(41/588\) for \(q=3,5,7\), and characteristic-three degeneracies. The script and captured output are embedded with this record. These finite checks are supplementary to the algebraic proof; field extensions and unbounded dimensions follow from the proof, not from extrapolation.

## Relationship to prior work
[1] provides Wall's moved-space parametrization, direct factorization theorem, reflection-shortening lemma, reflection length and spinor homomorphism. The line-to-factorization correspondence is a direct application of this established structural theory and is explicitly not asserted to be new. The numerical finite-field evaluation by **both** reflection square classes, the entire ternary target spectrum, the degenerate-plane class exclusion and the exact two-step total-variation distance are the assertions being submitted. [2] identifies the two involution classes and their sizes in the related projective linear group, but does not compute their ordered-product fibers. [3] analyzes a coherent configuration on pairs of conic lines under \(PGL_2(q)\), not conjugacy-class convolution on the group itself; its cross-ratio and line incidence tools are a plausible alternative route to related counts. Related earlier finite-field two-factor results for two-by-two matrices and symplectic transvections have different factor sets and target groups; neither is used as a proof of uniqueness here.

## Limitations
This is an arithmetic evaluation of established Wall-factorization machinery, not a new classification of reflection factorizations in arbitrary fields. The geometric line correspondence, spinor norm, and reflection-length criterion are classical. The all-dimensional formula has no global count of target matrices by every possible Wall-form type beyond the dimension-three specialization. The checker directly covers prime fields only. A potentially unindexed finite-group character-table calculation or a recoding of an earlier association-scheme intersection table could duplicate the explicit ternary numerical counts; priority therefore remains provisional pending independent specialist review. No claim of independent verification or of mathematical incomparability with all published literature is made.

## References
[1] Jon McCammond and Giovanni Paolini, *Factoring isometries of quadratic spaces into reflections*, arXiv:2103.02507 (first posted 2021-03-03), Sections 1–3. https://arxiv.org/abs/2103.02507

[2] Robert M. Guralnick and Michael E. Zieve, *Polynomials with PSL(2) monodromy*, arXiv:0707.1835 (first posted 2007-07-12), Appendix Lemma A.3. https://arxiv.org/abs/0707.1835

[3] Henk D. L. Hollmann and Qing Xiang, *Association schemes from the action of PGL(2,q) fixing a nonsingular conic in PG(2,q)*, arXiv:math/0503573 (first posted 2005-03-24), Sections 4–7. https://arxiv.org/abs/math/0503573
