# Exact ternary image and density phases of nonunit cubic Dickson parameters

## Finding
Let \(F_a(X)=X^3-3aX\) and \(V_a=F_a(\mathbb Z_3)\), where \(a\in3\mathbb Z_3\), including \(a=0\). There are exactly three types of image decomposition:

\[
V_a=(1+9\mathbb Z_3)\sqcup(-1+9\mathbb Z_3)\sqcup W_a,
\qquad
W_a=\begin{cases}
81\mathbb Z_3,&a=3b,\ b\equiv1\pmod3,\\
27\mathbb Z_3,&a=3b,\ b\equiv-1\pmod3,\\
27V_{a/9},&a\in9\mathbb Z_3.
\end{cases}
\]

All displayed unions are disjoint. For \(a\ne0\), each recurrence step removes two from the valuation: the iteration stops at a unit parameter for even valuation and at a valuation-one parameter for odd valuation. For \(a=0\), the recurrence gives a complete infinite decomposition:
\[
V_0=\{0\}\sqcup\bigsqcup_{j\ge0}27^j\bigl((1+9\mathbb Z_3)\sqcup(-1+9\mathbb Z_3)\bigr).
\]

Here is an exact finite-level formula. Put \(B(k)=2\cdot3^{\max(k-2,0)}\), and denote by \(N_a(k)\) the number of distinct values of \(F_a\) modulo \(3^k\). For nonunit \(a\),
\[
N_a(k)=\begin{cases}
B(k)+1,&1\le k\le3,\\
B(k)+3^{k-4},&k\ge4,\ a=3b,\ b\equiv1\pmod3,\\
B(k)+3^{k-3},&k\ge4,\ a=3b,\ b\equiv-1\pmod3,\\
B(k)+N_{a/9}(k-3),&k\ge4,\ a\in9\mathbb Z_3.
\end{cases}
\]
The recurrence has explicit terminal values for any unit \(u\in\mathbb Z_3^\times\):
\[
N_u(k)=\begin{cases}
3,&k=1,2,\ u\equiv1\pmod3,\\
5,&k=3,\ u\equiv1\pmod3,\\
13\cdot3^{k-4},&k\ge4,\ u\equiv1\pmod3,\\
3,&k=1,\ u\equiv-1\pmod3,\\
3^{k-1},&k\ge2,\ u\equiv-1\pmod3.
\end{cases}
\]
Thus the displayed formulas determine \(N_a(k)\) for *every* nonunit parameter and every precision, without enumeration or unstated recurrence bases.

The Haar measure \(\delta(a)=\mu(V_a)=\lim_{k\to\infty}3^{-k}N_a(k)\) is also exact. Define
\[
d_0(u)=\begin{cases}13/81,&u\equiv1\pmod3,\\1/3,&u\equiv-1\pmod3,\end{cases}
\quad
d_1(u)=\begin{cases}19/81,&u\equiv1\pmod3,\\7/27,&u\equiv-1\pmod3.\end{cases}
\]
For \(a\ne0\), write \(a=3^{2m+\epsilon}u\), where \(u\) is a unit, \(\epsilon\in\{0,1\}\), and \(2m+\epsilon\ge1\). Then
\[
\boxed{\delta(a)=\frac3{13}+27^{-m}\left(d_\epsilon(u)-\frac3{13}\right),\qquad\delta(0)=\frac3{13}.}
\]
This exposes two exceptional first-level density phases, \(19/81\) and \(7/27\), for parameters of valuation one and geometric convergence toward \(3/13\) along higher valuation strata.

## Assumptions and scope
\(\mathbb Z_3\) denotes the ring of ternary integers; \(3\mathbb Z_3\) includes zero. All residue images are taken in \(\mathbb Z/3^k\mathbb Z\), and each output residue is counted once, regardless of its number of preimages. The notation \(v_3\) denotes the ternary valuation, with \(v_3(0)=\infty\). The normalized additive Haar measure on \(\mathbb Z_3\) assigns \(3^{-j}\) to a single coset of \(3^j\mathbb Z_3\). No claim is made for parameters with negative valuation or for arbitrary primes.

## Proof
**1. Both unit-input branches are full cylinders.** Take \(a\in3\mathbb Z_3\) and \(r\in\{1,-1\}\). For \(x=r+3t\), direct expansion yields
\[
\frac{F_a(r+3t)-r}{9}=r^2t+3rt^2+3t^3-\frac a3r-at.
\]
Modulo three the normalized polynomial is the affine bijection \(t\mapsto t-(a/3)r\), and its derivative is congruent to \(1\pmod3\). For every normalized target there is exactly one root modulo three and it lifts uniquely by Hensel's lemma. Hence
\(F_a(r+3\mathbb Z_3)=r+9\mathbb Z_3\). The two cylinders are disjoint modulo three and contain no values from inputs divisible by three.

**2. The valuation-one bifurcation.** If \(a=3b\), with \(b\) a unit, direct substitution gives \(F_a(3t)=27(t^3-bt)\). For \(b\equiv1\pmod3\), the normalized polynomial \(g(t)=t^3-bt\) reduces to zero on every input modulo three, while \(g'(t)=3t^2-b\) is a unit. Hensel lifting on each input coset shows that \(g(\mathbb Z_3)=3\mathbb Z_3\). For \(b\equiv-1\pmod3\), \(g(t)\equiv2t\pmod3\), again with unit derivative; the three cosets map onto all three residue cylinders, so \(g(\mathbb Z_3)=\mathbb Z_3\). Multiplication by 27 gives respectively \(81\mathbb Z_3\) and \(27\mathbb Z_3\).

**3. The rescaling identity.** If \(a=9c\), then
\[
F_a(3t)=27F_c(t).
\]
This proves the remaining image recurrence. Repeated division of a nonzero parameter by nine ends at valuation zero or one. At \(a=0\), repeated substitution never ends, but the compact intersection of the nested zero branches is exactly \(\{0\}\); all other branches are the displayed disjoint cylinders.

**4. Terminal unit calculations.** If \(u\equiv-1\pmod3\), the normalized map on each input class \(x=r+3t\) has derivative \(r^2-u\equiv-\!u+r^2\) modulo three, a unit for \(r=\pm1\). Thus those images are precisely \(r(1-3u)+9\mathbb Z_3\), while the zero-input branch has image \(9\mathbb Z_3\) because
\(F_u(3t)=9(-ut+3t^3)\) and its normalized derivative is a unit. All three cylinders are distinct modulo nine. Therefore \(N_u(1)=3\) and \(N_u(k)=3^{k-1}\) for \(k\ge2\).

If \(u\equiv1\pmod3\), choose a square root \(s\in\mathbb Z_3^\times\) with \(s^2=u\), which exists by Hensel's lemma. Then \(F_u(st)=s^3F_1(t)\), and multiplication by \(s^3\) is a unit bijection. The zero-input branch of \(F_1\) has image \(9\mathbb Z_3\), as above. On \(x=1+3t\),
\(F_1(1+3t)=-2+27t^2(t+1)\). The factor \(h(t)=t^2(t+1)\) has values modulo three \(0,2,0\) on input classes \(0,1,-1\); its derivative \(h'(t)=3t^2+2t\) is a unit on classes \(1,-1\). These latter two input classes map onto the entire two output classes \(2+3\mathbb Z_3\) and \(3\mathbb Z_3\), and the remaining class contributes no new values. Hence the image of the positive unit-input branch is precisely \((-2+81\mathbb Z_3)\sqcup(52+81\mathbb Z_3)\). By oddness, the negative branch has the two opposite cosets. They are disjoint from the \(9\mathbb Z_3\) zero branch. Counting these 13 residue classes modulo 81 gives \(N_1(1)=N_1(2)=3\), \(N_1(3)=5\), and \(N_1(k)=13\cdot3^{k-4}\) for \(k\ge4\), proving the remaining terminal formula.

**5. Finite levels and measure.** The two outer image cylinders contribute \(B(k)\) residues modulo \(3^k\). The zero branch contributes one residue when \(k\le3\); for \(k\ge4\), it contributes \(3^{k-4}\), \(3^{k-3}\), or \(N_{a/9}(k-3)\) in the cases of Steps 2–3. This proves the exact \(N_a(k)\) formulas. The measures of disjoint cylinders add, so
\(\delta(3b)=2/9+1/81\) or \(2/9+1/27\), and \(\delta(9c)=2/9+\delta(c)/27\). The unit cases from Step 4 have densities \(13/81\) and \(1/3\). Iterating the affine recurrence gives the displayed closed phase formula. For \(a=0\), its fixed-point equation is \(\delta(0)=2/9+\delta(0)/27\), giving \(3/13\). The finite congruence images are exactly the reductions of \(V_a\). Their inverse images in \(\mathbb Z_3\) are decreasing unions of cylinders of measures \(3^{-k}N_a(k)\), and their intersection is \(V_a\) because that image is compact. Continuity of measure from above proves the stated limit.

## Verification
The standalone `verify.py` uses no third-party dependencies. It directly enumerates all distinct outputs of \(F_a\) for 181 integer parameters from \(-90\) to \(90\) at precisions \(1\) through \(8\), checks the image cardinalities against a separate implementation of the formula, and verifies the full image decomposition in every nonunit case. Additional enumeration at precisions \(9\) and \(10\) covers eight representative nonunit parameters. These finite checks supplement rather than prove the all-parameter theorem; the infinite scope follows from Steps 1–5.

## Relationship to prior work
Shang (first public preprint 31 October 2023) establishes a sharp general upper bound for the image sizes of nonpermutation polynomials over integer residue rings; it does not specialize that bound to this cubic family or distinguish its valuation-one branches. Bremser and Gomez-Calderon (1991) studied general Dickson value sets over Galois rings and is the principal historical priority risk: only its abstract, not its full article, was accessible, so this comparison is unresolved at full-text level. An independently published fixed-parameter analysis of \(X^3-3X\) determines one unit-parameter specialization, not the nonunit parameter phase diagram. Classical finite-field value-set results also do not by themselves supply the stated all-depth ternary image decomposition. The use of Hensel lifting, scaling identities, and elementary valuation arguments is classical and is not claimed as original.

## Limitations
The result is solely an exact value-set and normalized density classification for the third Dickson polynomial with \(a\in3\mathbb Z_3\); it does not classify fibers, arbitrary Galois extensions, or higher-degree Dickson polynomials. The full 1991 Galois-ring article could not be inspected and may contain an equivalent or stronger specialization; originality remains subject to this specific priority risk and independent human verification. No independent mathematical audit is claimed.

## References
1. Shikui Shang, *Value sets of non-permutation polynomials over the residue class rings of integers*, arXiv:2310.20226v1, first publicly posted 2023-10-31, https://arxiv.org/abs/2310.20226.
2. P. S. Bremser and J. Gomez-Calderon, *Value sets of Dickson polynomials over Galois rings*, Journal of Number Theory 38 (1991), 240–250, https://doi.org/10.1016/0022-314X(91)90087-R (abstract consulted; full text inaccessible).
3. T. Brazelton, J. Harrington, M. Litman, and T. W. H. Wong, *Residue sums of Dickson polynomials over finite fields*, https://tbrazel.github.io/assets/papers/dickson.pdf (finite-field background, not a ring-image theorem).
