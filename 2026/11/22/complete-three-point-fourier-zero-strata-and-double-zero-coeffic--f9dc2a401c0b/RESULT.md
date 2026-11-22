# Complete three-point Fourier zero strata and double-zero coefficient census on finite abelian groups
## Finding
Let \(G\) be any finite abelian group of order \(N\ge3\). Fix three distinct points \(S=\{x_0,x_1,x_2\}\), set \(a=x_1-x_0\), \(b=x_2-x_0\), \(H=\langle a,b\rangle\), \(h=|H|\), and write \(m_a=\operatorname{ord}(a)\), \(m_b=\operatorname{ord}(b)\), and \(m_c=\operatorname{ord}(a-b)\). All coefficients on \(S\) are nonzero complex numbers.

Define the nonnegative even integer
\[
L=h-\frac{h}{m_a}-\frac{h}{m_b}-\frac{h}{m_c}+2.
\]
The possible numbers of Fourier zeros are exactly \(0,N/h,2N/h\) unless \(H\cong (\mathbb Z/2\mathbb Z)^2\); in that exceptional case, they are exactly \(0,N/h\). For every fixed support \(S\), every listed level is attained. The missing two-zero level is characterized solely by the subgroup type: \(L=0\) if and only if \(H\cong(\mathbb Z/2\mathbb Z)^2\).

Moreover, the number of distinct projective coefficient rays \([c_0:c_1:c_2]\), with \(c_0c_1c_2\ne0\), producing exactly two zero cosets of \(H^\perp\) is **exactly**
\[
\boxed{\frac{hL}{2}}.
\]
In particular these maximally vanishing coefficient rays form a finite, completely counted collection. The statement is about complex coefficients and the unnormalized Fourier transform. The count does not identify coefficient rays under translations, modulations, permutations or conjugation.

As a global corollary, let \(q\) be the least element order at least three in \(G\), with \(2/q=0\) if no such element exists, and put \(e_G=1/4\) if \(G\) contains a subgroup isomorphic to \((\mathbb Z/2\mathbb Z)^2\), otherwise \(e_G=0\). The minimum Fourier-support cardinality over exactly three-point supported functions is
\[
\boxed{N\left(1-\max\{2/q,e_G\}\right)}.
\]

## Assumptions and scope
Use the unnormalized Fourier transform \(\widehat f(\chi)=\sum_{x\in G}f(x)\overline{\chi(x)}\), \(\chi\in\widehat G\). Support means exactly three nonzero values; all coefficient triples are considered modulo common nonzero complex scaling when counting projective rays. The annihilator \(H^\perp\) has size \(N/h\). No primeness, cyclicity, exponent restriction or positivity assumption is imposed. When \(G\) has exponent two and order at least four, every three-point difference subgroup is Klein four and the maximum number of Fourier zeros is \(N/4\).

## Proof
**Reduction to the two-generated subgroup.** Translate the support to \(\{0,a,b\}\); this changes Fourier values only by unimodular characters. Every character of \(H\) extends to one of \(G\), and restriction \(\widehat G\to\widehat H\) has fibers of cardinality \(N/h\). Each local Fourier zero therefore lifts to exactly one coset of \(H^\perp\). Working on \(H\), let \(u(\chi)=\overline{\chi(a)}\), \(v(\chi)=\overline{\chi(b)}\). Since \(a,b\) generate \(H\), \(\chi\mapsto(u(\chi),v(\chi))\) is injective, and
\[
F(\chi)=c_0+c_1u(\chi)+c_2v(\chi),\qquad c_0c_1c_2\ne0.
\]

**At most two local zeros.** If \(F(\chi)=0\), then \(|c_0+c_1u(\chi)|=|c_2|\), which upon squaring is
\[
\operatorname{Re}(c_0\overline{c_1}\,\overline{u(\chi)})
=\frac{|c_2|^2-|c_0|^2-|c_1|^2}{2}.
\]
The left side is a nonconstant real linear functional on the unit circle because \(c_0\overline{c_1}\ne0\); a real line intersects the unit circle in at most two points. Given \(u\), the equation \(F=0\) determines \(v\) uniquely. Injectivity of \(\chi\mapsto(u,v)\) proves that at most two characters of \(\widehat H\) vanish.

**Counting the two-zero rays.** Choose distinct local characters \(\chi,\psi\). Their two zero equations have rows \((1,u(\chi),v(\chi))\) and \((1,u(\psi),v(\psi))\); the rows are independent because \((u,v)\) distinguishes characters. Thus their common coefficient kernel is one-dimensional. Its three coordinates are nonzero if and only if each of the three \(2\times2\) minors is nonzero, equivalently
\[
(\chi^{-1}\psi)(a)\ne1,\quad
(\chi^{-1}\psi)(b)\ne1,\quad
(\chi^{-1}\psi)(a-b)\ne1.
\]
For any such pair the preceding upper bound says there are *exactly* two local Fourier zeros. Conversely, each two-zero coefficient ray supplies a unique unordered pair. Thus the count equals the number of unordered pairs of characters satisfying all three conditions.

For \(\rho\in\widehat H\), each condition forbids an annihilator subgroup of sizes \(h/m_a\), \(h/m_b\), and \(h/m_c\). Any two of \(a,b,a-b\) generate \(H\), so pairwise intersections of these three annihilators are exactly \(\{1\}\), as is the triple intersection. Inclusion-exclusion gives exactly \(L=h-h/m_a-h/m_b-h/m_c+2\) allowable ratios \(\rho\). Each ratio has \(h\) choices of \(\chi\), and each unordered pair appears twice; hence the number of rays is \(hL/2\). In fact \(L\) is even: an allowed character cannot have order one or two, since if its values on \(a\) and \(b\) are both \(-1\), its value on \(a-b\) is \(1\). The allowed characters therefore pair with their distinct inverses.

**The only exception.** Denote the three annihilators by \(A,B,C\) inside \(\widehat H\). All are proper subgroups (the three differences are nonzero), and any two meet only at the identity. If any is trivial, the remaining two proper subgroups cannot cover \(\widehat H\), so \(L>0\). If \(L=0\), all three are nontrivial and their union equals \(\widehat H\). For arbitrary \(s\in A\setminus\{1\}\) and \(t\in B\setminus\{1\}\), the product \(st\) belongs to \(C\setminus\{1\}\). The multiplication map \((A\setminus\{1\})\times(B\setminus\{1\})\to C\setminus\{1\}\) is injective because \(A\cap B=\{1\}\). Therefore
\[
|C|-1\ge (|A|-1)(|B|-1).
\]
The two cyclic analogues imply, on multiplying the three inequalities, that \((|A|-1)(|B|-1)(|C|-1)\le1\). Since these are positive integers, every annihilator has order two. Their union is a four-element group, necessarily Klein four, and therefore \(H\) is Klein four. Conversely, for \(H\cong(\mathbb Z/2\mathbb Z)^2\), all three differences are its nonidentity elements, the three annihilators cover \(\widehat H\), and \(L=0\). Thus for every other \(H\), \(L>0\), so the two-zero level is actually attained.

**The zero and one levels.** Coefficients giving no zeros form the complement of finitely many proper complex hyperplanes and of the three coordinate hyperplanes; this complement is nonempty. For any chosen local character, the corresponding zero hyperplane is distinct from every other zero hyperplane because the rows \((1,u,v)\) are distinct; it also is not a coordinate hyperplane. A finite union of proper subspaces cannot cover this two-dimensional hyperplane, so coefficients with exactly that single zero exist and can be chosen with all three entries nonzero. This completes the fixed-support classification.

**Global corollary.** For non-Klein difference subgroup \(H\), the maximum Fourier-zero fraction is \(2/h\); as \(H\) contains an element of order at least three, \(h\ge q\). A cyclic subgroup of order \(q\) realizes \(2/q\) using three of its points. For Klein-four \(H\), the maximum fraction is \(1/4\), realized by its three-point support. Taking the largest available fraction proves the global formula.

## Verification
The standalone `artifacts/verify_triple.py` performs independent-of-floating-point finite checks with character phases represented as rational classes modulo one. On 4,605 anchored three-point supports from cyclic and mixed direct-product groups it directly builds the difference subgroup, enumerates distinct character restrictions, verifies the inclusion-exclusion formula for \(L\), checks that the Klein-four criterion is exact, and matches the unordered-pair count \(hL/2\). Its actual output is `VERIFY_OK fixed_supports= 4605 double_zero_coefficient_lines= 499659 klein_four_supports= 69`. Finite checks supplement, but do not prove, the universal statements, whose proof is given above.

## Relationship to prior work
The finite-abelian uncertainty stability theorem of Massoulié addresses proximity to subgroup indicators when the support product approaches its minimum; it does not count Fourier-zero strata for a prescribed three-point set. Meshulam gives lower bounds by group orders and divisor interpolation. Bonami–Ghobber analyze equality cases and particular families but not this all-group coefficient-ray census. Krahmer–Pfander–Rashkov give general support-rank techniques and small-group diagrams, not the group-uniform formula here.

Specialized earlier results include the sharp *minimum* for three-point support on every cyclic group (published-finding corpus, 2026/10/4, `cf7d7124f263`), fixed-support exact spectra over odd-prime vector spaces (`ca0d22e76a34`), and the exact three-sparse spectrum on powers of the cyclic group of order four (`0b9b4b6c4f5d`). Their particular cases of the support-level claim are **already covered** and are not asserted to be new. The present classification covers **all** finite abelian groups and adds the integer-valued projective coefficient-ray census \(hL/2\), absent from the inspected full statements. A differently worded older classification in Fourier-minor or sparse-polynomial literature remains possible.

## Limitations
No classification is asserted for four or more supported points, nor for real, nonnegative or unimodular restricted coefficients; their attainable zeros may be fewer. The two-zero coefficient-ray count is before factoring by group automorphisms or frequency modulation. The universal theorem has a complete analytic proof, but originality is assessed only against inspected literature and indexed records, not an exhaustive global bibliography. The motivating result is about uncertainty stability, whereas the present exact classification is a related finite sparse-Fourier question rather than a consequence of that stability theorem.

## References
1. Laurent Massoulié, *Uncertainty principles as forcing mechanisms*, arXiv:2610.38909, first public 2026-10-28, https://arxiv.org/abs/2610.38909.
2. Roy Meshulam, *An uncertainty inequality for finite abelian groups*, arXiv:math/0312407, first public 2003-12-22, https://arxiv.org/abs/math/0312407.
3. Aline Bonami and Saifallah Ghobber, *Equality cases for the uncertainty principle in finite Abelian groups*, arXiv:1003.5060, first public 2010-03-26, https://arxiv.org/abs/1003.5060.
4. Felix Krahmer, Götz E. Pfander and Peter Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups*, arXiv:math/0611493, first public 2006-11-16, https://arxiv.org/abs/math/0611493.
5. *Exact three-point Fourier uncertainty on every cyclic group*, published published-finding corpus record `2026/10/4/SCOPE-exact-three-point-fourier-uncertainty-on-every-cyclic-group--cf7d7124f263`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-point-fourier-uncertainty-on-every-cyclic-group--cf7d7124f263.
6. *Exact three-sparse Fourier support spectra on elementary Abelian odd-prime groups*, published published-finding corpus record `2026/10/4/SCOPE-exact-three-sparse-fourier-support-spectra-on-elementary-abelian--ca0d22e76a34`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-three-sparse-fourier-support-spectra-on-elementary-abelian--ca0d22e76a34.
7. *Three-sparse Fourier support is controlled by affine span on the fourth-power cyclic groups*, published published-finding corpus record `2026/10/4/SCOPE-three-sparse-fourier-support-is-controlled-by-affine-span-on-mat--0b9b4b6c4f5d`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-three-sparse-fourier-support-is-controlled-by-affine-span-on-mat--0b9b4b6c4f5d.
