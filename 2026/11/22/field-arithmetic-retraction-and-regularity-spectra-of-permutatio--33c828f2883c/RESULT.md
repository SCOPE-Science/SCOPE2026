# Field-arithmetic retraction and regularity spectra of permutation evolution algebras

## Finding
Let \(q\) be any prime power and let \(\mathbf c=(c_n)_{n\ge1}\) be a finitely supported collection of nonnegative integers with \(\sum_n c_n>0\). In the permutation evolution algebra defined below, put
\[
g_n=\gcd(q-1,2^n-1),\quad d(\mathbf r)=\sum_n nr_n,\quad 0\le r_n\le c_n,
\]
\[
B_n(\mathbf r)=1+g_n\sum_{m\mid n}mr_m,\qquad H_n(\mathbf r)=1+g_n\sum_{\substack{m\mid n\\m<n}}mr_m.
\]
The rank enumerator of **composition-idempotent** algebra endomorphisms is
\[
\boxed{I_E(t)=\sum_{\mathbf r}t^{d(\mathbf r)}\prod_n\binom{c_n}{r_n} B_n(\mathbf r)^{c_n-r_n}.}\tag{1}
\]
The rank enumerator of **von Neumann regular** algebra endomorphisms is
\[
\boxed{R_E(t)=\sum_{\mathbf r}t^{d(\mathbf r)}\prod_n\left[\binom{c_n}{r_n}\sum_{j=0}^{r_n}(-1)^j\binom{r_n}{j}\bigl(H_n(\mathbf r)+ng_n(r_n-j)\bigr)^{c_n}\right].}\tag{2}
\]
A map \(\varphi\) is regular when some algebra endomorphism \(\psi\) satisfies \(\varphi\psi\varphi=\varphi\). Equations (1) and (2) enumerate all such maps by their **linear image dimension**, including the zero map. Empty powers are defined by \(0^0=1\). The signed inclusion-exclusion summation is evaluated separately for each distinct length \(n\), **inside** the product over lengths.

For example, with exactly one cycle of length one and one of length two, put \(g=\gcd(q-1,3)\). Then
\[
I_E(t)=1+(1+g)t+t^2+t^3,\qquad R_E(t)=1+(1+g)t+2gt^2+2gt^3.
\]
Thus the total regular endomorphism count is \(2+5g\): it is \(7\) for \(q=2\) and \(17\) for \(q=4\), with different distributions at ranks one, two and three.

## Assumptions and scope
The base field is \(\mathbb F_q\). For every supported positive integer \(n\), take \(c_n\) distinct labeled directed cycles of length \(n\). Their natural basis vectors \(e_{i,a}\), with \(a\) modulo the length of cycle \(i\), multiply by
\[
e_{i,a}^2=e_{i,a+1},\qquad e_{i,a}e_{j,b}=0\quad\text{for }(i,a)\ne(j,b).
\]
The resulting algebra is nonassociative in general and has no assumed unit. An endomorphism means any \(\mathbb F_q\)-linear multiplication-preserving self-map, including zero and maps that collapse or diagonally embed cycle summands. Rank means dimension of the vector-space image, not the number of nonzero target components. The classification is restricted to unweighted permutation structure matrices, not arbitrary weighted evolution algebras.

## Proof
**1. Cycle-component classification.** Project an algebra endomorphism to one designated target cycle of length \(n\). The complete Hom classification in [3] says that this component is either zero or chooses exactly one source cycle \(i\) of some length \(m\mid n\). For each such source cycle the component has \(m g_n\) possibilities. To see the arithmetic, start from a target coordinate at one chosen residue class modulo \(m\), with scalar \(\lambda\). Successive source squares propagate the scalar as \(\lambda,\lambda^2,\lambda^{2^2},\ldots\); closure around the target cycle forces \(\lambda^{2^n-1}=1\). There are exactly \(g_n\) such scalars in \(\mathbb F_q^\times\), and \(m\) residue choices. Nonzero components into the same target cycle cannot involve two different source cycles because their supports would overlap. Different target components make independent choices. Every selected source cycle contributes its full length to image rank; if it is selected multiple times, its rank is counted only once. This is a previously established Hom classification, not a newly asserted theorem.

Encode an endomorphism by its **partial cycle map** \(f\): for each target cycle \(j\), either the image of that target's coordinate component is zero or \(f(j)=i\) is the chosen source cycle with length dividing the target length. Although this notation is reversed relative to the ordinary action on algebra basis vectors, composition of endomorphisms induces composition of these partial maps in the matching order; the scalar phases multiply through the same squaring compatibility. The rank equals the sum of lengths of cycles occurring in \(\operatorname{im}f\).

**2. Idempotents.** If \(\varphi^2=\varphi\), the partial cycle map satisfies \(f^2=f\). Conversely, suppose \(f^2=f\), meaning that every selected image cycle is fixed. A nonzero component from a cycle to itself is an isomorphism; the identity \(\varphi^2=\varphi\) forces its scalar phase to be the identity isomorphism, rather than an arbitrary one of the \(n g_n\) isomorphisms. Then all other components landing in fixed cycles may be chosen freely: on the fixed image, applying \(\varphi\) again acts as the identity. Therefore choose \(r_n\) fixed cycles among the \(c_n\) cycles of length \(n\), in \(\binom{c_n}{r_n}\) ways. Each of the remaining \(c_n-r_n\) target cycles chooses zero (one option) or any fixed source cycle of divisor length \(m\mid n\), with \(m g_n\) scalar-phase options. That yields the factor \(B_n(\mathbf r)^{c_n-r_n}\). Every fixed source cycle is in the image and no other source cycles are; hence the rank is exactly \(d(\mathbf r)\). Multiplying the independent choices and summing proves (1).

**3. Regularity.** We prove a witness criterion and then count its fibers. Necessity: if \(\varphi=\varphi\psi\varphi\), then the underlying cycle map \(f\) satisfies \(f=fgf\) for the map \(g\) of \(\psi\). For an image cycle \(i\), a cycle \(j\) with \(f(j)=i\) must be reachable through such a witness. Since maps can only decrease cycle lengths along divisibility, the chain \(i\xrightarrow{g}j\xrightarrow{f}i\) forces \(j\) to have the same length as \(i\). Thus every image cycle must be hit by a same-length source cycle. Sufficiency: for each image cycle \(i\), select a same-length \(j\) with \(f(j)=i\). The corresponding component is a cycle-isomorphism, hence has an inverse algebra homomorphism from cycle \(i\) back to cycle \(j\) (invert its phase and its nonzero coefficient). Combining these inverse components on disjoint selected target cycles defines an endomorphism \(\psi\) with \(\varphi\psi\varphi=\varphi\). This qualitative partial-cycle criterion is analogous to and in its semigroup formulation is explicitly established by Konieczny [2, Lemma 4.1]; it is not claimed as original here.

**4. Counting regular maps.** Fix the set of image cycles, having \(r_n\) cycles of each length \(n\); their total linear dimension is \(d(\mathbf r)\). Any target cycle of length \(n\) can choose zero, one of the image cycles with a proper divisor length (\(H_n(\mathbf r)\) choices in all), or one of the \(r_n\) length-\(n\) image cycles (\(n g_n r_n\) choices). The witness criterion requires that *every one* of the \(r_n\) selected length-\(n\) image cycles be hit from a length-\(n\) target cycle. By inclusion-exclusion on the set of missed equal-length image cycles, the number of such assignments for the \(c_n\) target cycles is
\[
\sum_{j=0}^{r_n}(-1)^j\binom{r_n}{j}(H_n(\mathbf r)+ng_n(r_n-j))^{c_n}.
\]
Each image cycle is guaranteed selected by the equal-length witness, so there is no overcount between distinct image sets. Select those sets in \(\binom{c_n}{r_n}\) ways independently over \(n\). This proves (2), including \(\mathbf r=0\), when the only endomorphism is zero.

**5. Boundary and the previously known all-regular criterion.** Every element is regular iff no two **distinct supported lengths** have a proper divisibility relation. Indeed, in an antichain of supported lengths every nonzero component has equal source/target cycle lengths and hence any image cycle has a same-length witness. If there are supported lengths \(m<n\) with \(m\mid n\), map one length-\(n\) target component nontrivially into one length-\(m\) source cycle and set all others to zero. This image cycle has no equal-length witness, producing a nonregular map. This criterion coincides with the known regularity theorem for partial-transformation centralizers [2, Theorem 4.2] and is a consistency statement, **not** the claimed novelty.

## Verification
The standalone `verify.py` uses literal finite-field scalar multiplication for \(q=2,3,4\), explicitly constructs all cycle-component choices, computes the composition of each pair of endomorphisms, tests \(\varphi^2=\varphi\), and checks whether a witness \(\psi\) exists for \(\varphi\psi\varphi=\varphi\). It then compares the rank histograms against two independently implemented finite sums for (1) and (2). All 13 exhaustive configurations passed, including mixed divisibility, multiple equal cycles, rank-zero and full-rank maps, and a nonprime field. The test script runs with `python3 verify.py` and writes the captured output reproduced in `verification_output.txt`. The formulas for arbitrary dimensions and all finite fields are justified by the proof, not by finite experiments.

## Relationship to prior work
Elduque and Labra [1] introduce the graph viewpoint on evolution algebras, providing archival motivation for investigating graph-structured endomorphisms. Konieczny [2] already proves the cycle-map regularity witness criterion (Lemma 4.1) and the divisibility-antichain characterization of completely regular partial-transformation centralizers (Theorem 4.2). Neither statement is claimed as new.

The published complete Hom classification [3] explicitly gives the permissible source-to-target cycle maps and root-of-unity counts. That classification, including nonmonomial homomorphisms, is *used as a lemma*, not reclaimed. The related published centralizer result [4] gives an unweighted, total-transformation idempotent rank polynomial and a minimal retraction rank formula. Our counted objects instead are finite-field algebra endomorphisms, permit zero components, and have target-length-dependent root-of-unity weights. In particular the regular rank polynomial (2) has no counterpart in [3] or [4]. The contribution claimed is this simultaneous exact finite-field enumeration of composition-idempotents and regular elements, not the underlying cycle-map classification, their qualitative regularity conditions, or generic inclusion-exclusion.

## Limitations
The rank spectra are for unweighted permutation evolution algebras, not arbitrary weighted cycles or general evolution algebras. Equations (1) and (2) use established cycle decomposition and classical inclusion-exclusion; they do not establish new general structure theorems for Green's relations. An earlier universal weighted partial-map rank enumerator might imply the present formulas by specialization; publication priority has not been certified independently.

## References
1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1 (first public submission 17 December 2013), https://arxiv.org/abs/1312.4685.
2. J. Konieczny, *Green's relations and regularity in centralizers of permutations*, Glasgow Mathematical Journal 41 (1999), 45–57 (Cambridge first online posting verified 19 July 2001), DOI: 10.1017/S0017089599970301, https://doi.org/10.1017/S0017089599970301.
3. *Complete homomorphism counts and rank distributions for permutation evolution algebras*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-complete-homomorphism-counts-and-rank-distributions-for-permutat--f14321710094.
4. *Rank enumeration and minimum retraction size in permutation-centralizer monoids*, published published-finding corpus finding, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-rank-enumeration-and-minimum-retraction-size-in-permutation-cent--46b24971b86b.
