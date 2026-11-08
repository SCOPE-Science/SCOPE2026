# Orthomorphism fibers and cycle spectra of finite bands

## Finding
Let \(B\) be any nonempty finite band (an associative semigroup in which every element is idempotent). A **complete mapping** is a permutation \(\alpha:B\to B\) for which its **orthomorphism** \(\theta_\alpha(x)=x\alpha(x)\) is also a permutation. Write \(\mathcal D(B)\) for the Green \(\mathcal D\)-classes. Each class \(D\) is a rectangular band with \(a_D\) Green \(\mathcal R\)-classes of \(b_D\) elements each; thus \(|D|=a_Db_D\).

**Theorem.** The orthomorphisms arising from complete mappings are **exactly** the permutations of \(B\) preserving each Green \(\mathcal R\)-class individually. Every such orthomorphism has precisely
\[
F(B)=\prod_{D\in\mathcal D(B)}(a_D!)^{b_D}
\]
complete-mapping preimages. Consequently the exact number of complete mappings is
\[
C(B)=\prod_{D\in\mathcal D(B)}(a_D!)^{b_D}(b_D!)^{a_D}.
\]
More strongly, writing \(c_k(\pi)\) for the number of cycles of length \(k\) in a permutation \(\pi\), their **complete orthomorphism cycle spectrum** is
\[
\sum_{\alpha\text{ complete}}\ \prod_{k\ge1}t_k^{c_k(\theta_\alpha)}
=\prod_{D\in\mathcal D(B)}(a_D!)^{b_D}
 \left(\sum_{\pi\in\mathfrak S_{b_D}}\prod_{k\ge1}t_k^{c_k(\pi)}\right)^{a_D}.
\]
In particular, a uniformly chosen complete mapping induces a uniformly chosen permutation of the elements within each \(\mathcal R\)-class, with these permutations independent. All results depend only on the rectangular-class sizes, not on the products between distinct \(\mathcal D\)-classes.

## Assumptions and scope
The band is finite, nonempty, associative and idempotent; it need not be commutative, normal, or unital. The permutation \(\mathfrak S_{b_D}\) acts on the \(b_D\) elements in one \(\mathcal R\)-class. The product over classes is finite. Factorials at one equal one. The cycle-spectrum identity is a formal polynomial identity in commuting indeterminates \(t_k\), with \(1\le k\le|B|\). No assertion about non-band semigroups or the joint cycles of \(\alpha\) and \(\theta_\alpha\) is made.

## Proof
**1. Class preservation follows from ideals and finiteness.** If \(I\) is a two-sided ideal of \(B\), then \(\theta_\alpha(I)\subseteq I\): for \(x\in I\), the product \(x\alpha(x)\in I\). Since \(\theta_\alpha\) is a permutation and \(I\) is finite, \(\theta_\alpha(I)=I\). Thus \(x\) and \(\theta_\alpha(x)\) belong to exactly the same ideals. The intersection of all ideals containing \(x\) is its principal two-sided ideal \(B^1xB^1\). Hence they generate the same principal ideal, i.e. \(x\mathrel{\mathcal J}\theta_\alpha(x)\).

As \(\theta_\alpha(x)=x\alpha(x)\), its principal ideal is contained in the principal ideal of \(\alpha(x)\). Therefore \(J(x)\le J(\alpha(x))\) in the partial order of \(\mathcal J\)-classes. Iterate along the finite \(\alpha\)-orbit of \(x\):
\[
J(x)\le J(\alpha(x))\le\cdots\le J(\alpha^r(x))=J(x).
\]
Antisymmetry forces equality at each step. Thus \(\alpha\) preserves every \(\mathcal J\)-class. For finite bands, \(\mathcal J=\mathcal D\), and each \(\mathcal D\)-class is a rectangular subband (the classical band decomposition into rectangular bands). Both \(\alpha\) and \(\theta_\alpha\) therefore restrict to permutations on each rectangular class.

**2. Full parametrization on one rectangular class.** Fix \(D\cong I\times\Lambda\), where \(|I|=a\), \(|\Lambda|=b\), and
\[
(i,\lambda)(j,\mu)=(i,\mu).
\]
Write \(\alpha(i,\lambda)=(h(i,\lambda),v(i,\lambda))\). Necessarily
\[
\theta_\alpha(i,\lambda)=(i,v(i,\lambda)).
\]
Therefore \(\theta_\alpha|_D\) is a permutation exactly when, for each \(i\in I\), the map \(\tau_i:\Lambda\to\Lambda\), \(\lambda\mapsto v(i,\lambda)\), is a permutation. Fix these \(a\) arbitrary row permutations. The map \(\alpha|_D\) is bijective exactly when for each \(\mu\in\Lambda\) the map
\[
p_\mu:I\to I,\qquad i\mapsto h(i,\tau_i^{-1}(\mu))
\]
is a permutation. Conversely, any independent choices \((\tau_i)_{i\in I}\) and \((p_\mu)_{\mu\in\Lambda}\) define a bijective complete mapping via
\[
\alpha(i,\lambda)=\bigl(p_{\tau_i(\lambda)}(i),\tau_i(\lambda)\bigr),
\qquad\theta_\alpha(i,\lambda)=(i,\tau_i(\lambda)).
\]
There are \((b!)^a\) choices of the \(\tau_i\), and \((a!)^b\) choices of the \(p_\mu\). Each prescribed row-preserving orthomorphism therefore has the constant fiber size \((a!)^b\).

**3. Independence between classes.** The maps obtained in Step 2 preserve each \(\mathcal D\)-class. Since products of two elements in one rectangular class stay in that class, \(\theta_\alpha(x)=x\alpha(x)\) is also computed entirely inside the same class. Hence arbitrary independent complete mappings on distinct classes glue to one on all of \(B\), regardless of products between the classes. Step 1 proves there are no others. Multiplying the local counts establishes the first two formulas and the orthomorphism-image classification.

**4. Cycle spectrum.** Every orthomorphism is a product of independent permutations \(\tau_i\) on the separate \(\mathcal R\)-classes. Cycles cannot cross those classes. Thus their cycle monomials multiply and their generating polynomial factors. Every orthomorphism has the same fiber size, producing the displayed polynomial and uniform law. This proves all assertions.

## Verification
The separate direct-enumeration standard-library checker `verify.py` directly enumerates *all permutations* of each of seven explicit finite bands, forms \(\theta_\alpha(x)=x\alpha(x)\) from their multiplication tables, and compares the exact image, all fiber sizes, total complete mappings, and cycle-type multiplicities with the theorem. The seven bands include rectangular bands of shapes \(2\times2\) and \(3\times2\); a two-level semilattice product of \(2\times2\) rectangular bands; a nonuniform two-level band with a two-element left-zero top and a \(2\times2\) rectangular bottom glued by a nonconstant connecting homomorphism; four-element left-zero and right-zero bands; and the five-element free left regular band on two generators. There are 41,952 input permutations across these cases. Full checker source and actual output are included. These finite experiments corroborate the argument but are not the proof for arbitrary bands.

## Relationship to prior work
Araújo, Bentz, Cameron, Hendrey and Kinyon (2026) developed complete mappings of finite semigroups, including principal-factor reduction, Green-class restrictions and the existence of complete mappings on bands (Section 12). Their Problem 15.6 asks for cycle structures of complete mappings and orthomorphisms reflecting Green–Rees structure. The present theorem answers the **orthomorphism-only** spectrum and uniform preimage enumeration for **every finite band**, by explicit independent row/column permutation coordinates. It does not claim the earlier existence theorem or the classical rectangular-band decomposition as new. Higgins's semigroup text records the standard decomposition of bands into rectangular classes; prior cycle-type work of Bors and Wang concerns complete mappings of finite fields and groups, not this non-group band enumeration.

## Limitations
This theorem does not solve the full Problem 15.6 for arbitrary semigroups, nor does it determine the joint cycle spectrum of \(\alpha\) and \(\theta_\alpha\), the cycle spectrum of \(\alpha^{-1}\theta_\alpha\), or non-band complete-mapping counts. The finite verification covers specified small examples only. The historical-priority search did not establish that an equivalent band-specific enumeration has never appeared under different Latin-transversal terminology; this remains a residual risk.

## References
1. J. Araújo, W. Bentz, P. J. Cameron, K. Hendrey, M. Kinyon, *Complete Mappings of Semigroups*, arXiv:2608.25092v1 (first public: 2026-08-25), especially Sections 1, 3, 4, 12 and Problem 15.6. https://arxiv.org/html/2608.25092
2. P. M. Higgins, *Techniques of Semigroup Theory* (1992), Theorem 13.9 (bands as semilattices of rectangular bands). https://djvu.online/file/dSCVGzi7Ud1ri
3. A. Bors and Q. Wang, *Cycle types of complete mappings of finite fields*, arXiv:2105.00140 (2021). https://arxiv.org/abs/2105.00140
4. A. Bors and Q. Wang, *Compositions and parities of complete mappings and of orthomorphisms*, arXiv:2207.09642 (2022). https://arxiv.org/abs/2207.09642
