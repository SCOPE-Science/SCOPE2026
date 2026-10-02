# Tate-duplication at \(q=5\): finite forward images of every nondegenerate Berkovich disk

## Context and definitions

Let \(K=\mathbb C_5\), \(E=K^\times/5^{\mathbb Z}\), and \(x:E\to\mathbb P^1\) be the quotient by \([-1]\). Define the degree-four Lattès map by \(L\circ x=x\circ[2]\). The Tate equation and quotient descend to \(\mathbb Q_5\), so \(L\in\mathbb Q_5(X)\). The non-Archimedean absolute value satisfies \(|5|=1/5\).

A disk means a nondegenerate positive-radius open or closed Berkovich disk, or its projective-coordinate image, as in Benedetto's lecture Definitions6.1 and6.4. It is a subset of \(\mathbb P^{1,\mathrm{an}}\), not the associated Gauss point. Radius-zero singletons and generalized typeIV singletons are excluded. The assertions below retain arbitrary disks in this sense, not only whole Fatou components.

The folded Tate skeleton is \(\Sigma=x(S_E)\), of length \(-\log|5|/2\). In normalized coordinates \(0\le s\le1/2\), its action is
\[
 T(s)=\begin{cases}2s&0\le s\le1/4,\\1-2s&1/4\le s\le1/2.\end{cases}
\]
The exact Tate coefficients, rational duplication formula and identification \(\Sigma=\{\zeta(0,5^{-s}):0\le s\le1/2\}\) are given in the irrational-boundary check below.

## Result

The Julia set is \(\Sigma\). Its complement is the disjoint union of open Fatou disks; every component is preperiodic, and every periodic component is indifferent. There is no classical attracting periodic point. The component containing infinity is fixed with multiplier4.

For every disk \(D\) in the stated conventional sense, the sets \(L^n(D)\) take only finitely many distinct values. A disk contained in the Fatou set eventually has a finite cycle of subdisk images. A disk meeting a positive interval of \(\Sigma\) eventually maps onto the whole projective line. A closed disk meeting \(\Sigma\) only at an endpoint maps into the fixed endpoint disk. This is the original arbitrary-disk scope with its missing argument supplied, not a narrowing to components.

## Proof: Julia geometry and Fatou components

The standard Tate-Lattès Julia-segment result is already described in Benedetto's 2010 Project2(d–f). Uniformization takes the circle skeleton under doubling, and the quotient by reflection folds it to \(\Sigma\). The Lattès equilibrium measure is the pushforward of uniform circle measure and has full support \(\Sigma\). Thus \(J(L)=\Sigma\), and \(L^{-1}(\Sigma)=\Sigma=L(\Sigma)\). Every complementary component is an open disk. This geometry is established prior theory, not a claimed new subresult.

For no wandering, apply the exact locally-compact theorem stated in Benedetto's lecture Theorem7.20 (printed81, PDF80), also stated by Benedetto and coauthors in Theorem17.4 of *Current Trends and Open Problems in Arithmetic Dynamics*. The coefficient field \(\mathbb Q_5\) is complete and locally compact, its algebraic closure is dense in \(K\), its characteristic is zero and residue characteristic is5. Every local degree of \(L\) lies in \(\{1,2,3,4\}\), hence no local degree is divisible by5. There is no wild point, in particular no wild recurrent classical Julia critical point. All hypotheses of that theorem are satisfied, so every Fatou component is preperiodic.

If \(x(P)\) is periodic of period \(n\), then \([2^n]P=\pm P\). At an unbranched quotient point the multiplier of \(L^n\) is \(\pm2^n\). Among images of \(E[2]\), only \(x(0)=\infty\) is periodic: all other branch images map to infinity. In the quadratic quotient coordinate at0, its return multiplier is \(4^n\). All these are 5-adic units; hence no classical attracting cycle exists. The periodic-component classification (survey Theorem17.2) makes a periodic component of return degree at least2 an attracting component with a classical attracting periodic point. Consequently all periodic components here have return degree1 and are indifferent.

The independent elementary component check is consistent: an off-skeleton disk is attached at a typeII point, so its normalized skeletal coordinate is rational because \(|K^\times|=5^{\mathbb Q}\). Rational tent orbits are finite, and a return tangent map defined over a finite residue field has finite orbits on every direction in \(\mathbb P^1(\overline{\mathbb F}_5)\). This alternative tracks whole components only; it does not itself prove the arbitrary-subdisk sentence.

## Proof: arbitrary disks

### Fatou subdisks. Disks contained in the Fatou set

Let \(D\) be such a disk disjoint from \(\Sigma=J(L)\). Connectedness places it in one Fatou component. By Benedetto's no-wandering theorem and the unit periodic multipliers, that component eventually reaches an indifferent periodic disk \(U\). Images of disks under a rational map are disks or the whole projective line; the latter is impossible for a subset of the totally invariant Fatou set. Thus a forward image \(D'\) lies in \(U\). The precise primary reference for the disk-image assertion is lecture Proposition3.28, printed25/PDF24, complete statement and proof lines2086-2105, together with Proposition6.13, printed62-63/PDF61-62, complete statement and proof lines5003-5049. Proposition6.13 conventionally uses the open version of an irrational disk. For its closed counterpart, include the one typeIII boundary point: the open irrational disk is dense in its compact closed counterpart, so continuity and compactness identify the closed image with the closure of the open image. In coordinates avoiding a pole on the target component, the nonconstant convergent power series has image radius \(|c_j|\rho^j\) for some positive integer \(j\); an irrational logarithmic radius stays irrational because \(|c_j|\in5^{\mathbb Q}\). Thus the corresponding image is the closed irrational disk, not a new missing case.

Pass to the return \(f=L^m\) of \(U\). Its degree on \(U\) is one. Choose a projective coordinate over a finite extension of \(\mathbb Q_5\) taking \(U\) to the open unit disk. This is possible because its boundary is typeII: choose an algebraic center sufficiently close to any center and an algebraic scale of the prescribed radius. The return remains defined over that finite extension.

Lecture Proposition3.14 (printed19-20/PDF18-19, lines1515-1580) proves that a degree-one map between disks is an exact similarity; here the domain and range are the same unit disk, so it is an isometry. The proof and Proposition3.15 supply its analytic inverse over the same field. Therefore it sends a subdisk of radius \(\rho>0\) to the same kind of subdisk of the same radius. If \(D'=U\), it is already fixed. Otherwise its radius is smaller than one.

Choose an algebraic point \(b\) in \(D'\), by density, close enough to a center that \(D'\) is the disk of the same radius/type centered at \(b\). Enlarge the coefficient field once to a finite extension \(F/\mathbb Q_5\) containing \(b\). The entire center orbit \(f^n(b)\) remains in \(F\cap U\). This set is compact: in a finite discretely valued extension the open unit ball is the closed maximal-ideal ball. A compact ultrametric set has finitely many equivalence classes for either \(|x-y|<\rho\) or \(|x-y|\le\rho\). Thus only finitely many disks of the given radius/type can occur as \(f^n(D')\). There are only \(m\) other iterate residues, so the full \(L\)-orbit of \(D\) is finite. This includes arbitrary small/irrational-radius subdisks, not only whole components.

### Disks meeting a Julia interval. Disks meeting a positive interval of the Julia segment

For an open disk meeting \(\Sigma\), its intersection contains a nondegenerate relative open segment; the same is true of a closed disk unless it touches \(\Sigma\) at just its boundary point. Choose a smaller open skeletal interval \(I\) in the disk, avoiding the single possible attachment of the disk's omitted direction. Every off-skeleton component attached at any point of \(I\) is then entirely in \(D\).

The folded doubling map is topologically exact on its segment. Explicitly, its \(n\)-fold monotonicity intervals have mesh tending to zero and map across the whole segment. For large \(n\), a full such interval lies in \(I\); hence \(T^n(I)=\Sigma\), with preimages chosen inside \(I\).

For each target Fatou component \(V\) attached to a typeII point \(\eta\in\Sigma\), choose a preimage \(\xi\in I\) with \(L^n(\xi)=\eta\). Its normalized coordinate is rational because the target coordinate is rational and inverse tent branches are affine over dyadic rationals, so \(\xi\) is typeII. The induced residue map at \(\xi\) is a nonconstant rational map over the algebraically closed residue field and is therefore surjective on directions. Lecture Theorem6.12 (printed61-62/PDF60-61, lines4915-4990, complete statement and proof read) gives this map and the actual image of each direction.

A skeletal source direction contains a positive skeletal segment and cannot map to an off-skeleton target direction. Hence a direction mapping to \(V\) is off-skeleton; its entire component is contained in \(D\). It cannot be a surplus/bad direction whose image is all of the projective line, since the Fatou set is totally invariant. By Theorem6.12, or lecture Proposition7.1, this component maps onto \(V\). Consequently \(L^n(D)\) contains every Fatou component as well as the whole Julia segment: it equals \(\mathbb P^{1,\mathrm{an}}\). All subsequent images are the same set.

### Endpoint-touching closed disks. Closed disks merely touching the segment

The remaining case is a closed disk whose intersection with \(\Sigma\) is only its boundary point. This point must be an endpoint of \(\Sigma\): at an interior point the two skeletal directions are distinct, whereas a closed disk omits only one direction. Both endpoints are typeII. At an endpoint \(\xi\), the disk in question consists of \(\xi\) and **all** off-skeleton components attached there; it omits the sole skeletal direction. It is NOT the closure of a single open component. For example, the closure of the open unit disk contains the Gauss point but not the residue-class-one open disk, whereas the closed unit disk contains both. The erroneous closure identification is not used here.

Let \(B_\xi\) denote that endpoint disk. Its image cannot contain a skeletal point other than \(L(\xi)\), because \(L^{-1}(\Sigma)=\Sigma\). Every off-skeleton direction maps to an off-skeleton direction and maps its entire component onto the image component: it cannot be a surplus direction, since a Fatou component cannot map onto the projective line. Conversely, for each target off-skeleton direction at \(L(\xi)\), the nonconstant typeII tangent map supplies a preimage direction. The sole source skeletal direction maps to the target skeletal direction (by the tent-map germ), so the preimage direction is off-skeleton. All such directions belong to \(B_\xi\). Consequently \(L(B_\xi)=B_{L(\xi)}\). The endpoint \(s=1/2\) maps to \(s=0\), which is fixed, so these closed disks have at most two forward images. This argument uses the same published Theorem6.12 as the Julia-interval argument.

These cases prove the conventional positive-radius ANY-disk statement. They do not cover degenerate radius-zero singleton sets or arbitrary typeIV singletons. If those were included in the original undefined word disk, the sentence would require clarification; no blanket falsehood or universal coverage is asserted for that different meaning.

### Irrational-boundary check. Explicit check of the suggested irrational-boundary counterexample

The standard Tate equation is \(y^2+xy=x^3+a_4x+a_6\), with
\[
a_4=-5\sum_{k\ge1}\frac{k^3 5^k}{1-5^k},\qquad
a_6=-\frac1{12}\sum_{k\ge1}\frac{(7k^5+5k^3)5^k}{1-5^k}.
\]
In its standard quotient coordinate the exact duplication rational map is
\[
 L(X)=\frac{X^4-2a_4X^2-8a_6X+a_4^2-a_6}
 {4X^3+X^2+4a_4X+4a_6}.
\]
This is the usual Weierstrass duplication formula with \(b_2=1,b_4=2a_4,b_6=4a_6,b_8=a_6-a_4^2\). The Tate coordinate series and coefficient definitions were checked directly in Silverman, *The Arithmetic of Elliptic Curves*, second edition, Appendix C.14, printed444-445/PDF454-455 (522-page PDF), https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . The rational formula here is an algebraic deduction from those coefficients, not a claim that this source prints this particular specialized rational map.

On the Tate annulus with \(|u|=5^{-s}\), \(0<s<1/2\), the series
\[
x(u)=\sum_{k\in\mathbb Z}\frac{5^ku}{(1-5^ku)^2}
-2\sum_{k\ge1}\frac{5^k}{(1-5^k)^2}
\]
has leading Laurent term \(u\), since the next possible norm is \(|5|/|u|<|u|\) and the constant term is no larger than \(|5|\). Thus the annular Gauss point maps to \(\zeta(0,5^{-s})\); continuity supplies the two endpoints. This identifies
\(\Sigma=\{\zeta(0,5^{-s}):0\le s\le1/2\}\).
The coefficient norms are \(|a_4|=5^{-2}\) and \(|a_6|=5^{-1}\). On this Gauss segment the numerator norm is \(\max(5^{-4s},5^{-1})\), and denominator norm is \(5^{-2s}\). Together with the Tate doubling identity this reproduces precisely \(T(s)=2s\) for \(s\le1/4\), \(T(s)=1-2s\) for \(s\ge1/4\).

Now choose any irrational \(\alpha\in(0,1/2)\), and the ordinary positive-radius closed Berkovich disk \(D_\alpha=\overline D_{\rm Ber}(0,5^{-\alpha})\). Its boundary \(\zeta_\alpha\) is typeIII and does have an infinite tent orbit: equality of two iterates would force \((\pm2^n\mp2^m)\alpha\) to be an integer, hence \(\alpha\) rational. But
\[
 D_\alpha\cap\Sigma=[\alpha,1/2],
\]
not a singleton. If \(\alpha<1/4\), this interval already contains a full tent branch. If \(\alpha\ge1/4\), its first image is \([0,1-2\alpha]\), a positive-length interval that grows under doubling until it covers a full branch. This supplies a concrete instance of the Julia-interval argument: after enlarging the iterate to use a full branch strictly inside an interior skeletal interval of \(D_\alpha\), all target off-skeleton directions have preimages inside the disk, and \(L^N(D_\alpha)=\mathbb P^{1,\rm an}\). The boundary's infinite point orbit does not remain the boundary of these set images.

The analogous open disk has \(D_\alpha\cap\Sigma=(\alpha,1/2]\), and likewise contains an interior interval; the same conclusion holds. The disk on the other side of the typeIII boundary has an interval toward0 and is treated identically. Therefore the suggested irrational-boundary construction is not a counterexample to the ANY **disk-as-subset** sentence. It does give a counterexample to a different sentence saying every typeIII **point** is preperiodic, which the original did not state. If the intended word disk instead means an associated Gauss point rather than its Berkovich disk subset, this semantic change must be recorded explicitly.


## Original proof defect and its repair

The former unrestricted attracting-cycle-critical-point rule is false. Benedetto's lecture Proposition7.16 (printed78–79/PDF77–78) requires an attracting periodic disk whose return Weierstrass degree is not divisible by the residue characteristic. Remark7.18 (printed79/PDF78) exhibits \(z^p\) in mixed characteristic as the counterexample.

Concretely over \(\mathbb C_5\), \(z^5\) has a fixed attracting Fatou component \(D_{\mathrm{Ber}}(1,1)\) with multiplier5 at1 and return degree5. Its only critical points0 and infinity are fixed and are not attracted to1. For \(z=1+w\), \(|w|<1\), the binomial expansion gives
\[
 |(1+w)^5-1|\le\max(|5w|,|w|^5)<|w|.
\]
Thus the omitted hypothesis matters. This is a counterexample to the general lemma, NOT to the target \(L\) or its arbitrary-disk conclusion. For \(L\), one-step component degrees1 through4 make every periodic-return degree a product not divisible by5; alternatively the direct unit multipliers above already replace the invalid step. The defective lemma is withdrawn, not reused as a reason to call the target false.

## Priority and scientific interpretation

The completed correctness assessment is PASS for the conventional arbitrary-disk conclusion proved here. Originality is FAIL, and value is FAIL, for substantive prior implication rather than a missing source or certificate.

Each part is a routine consequence of established inputs: the Tate coefficients and Weierstrass duplication formula; Tate-Lattès folded Julia geometry; the locally-compact no-wandering theorem and periodic-component classification; the published degree-one disk similarity and typeII tangent-map theorem; elementary compactness of finite local-field extensions; and the full-branch exactness of the elementary tent map. The arbitrary-disk extension is expressly proved above rather than falsely attributed to the no-wandering theorem alone. The same reasoning works throughout this already tame local-field setting; choosing the numerical Tate parameter5 does not isolate a new mathematical gap.

The torsion ledger
\[
 \#x(E[2^n])=(4^n+4)/2=2^{2n-1}+2\quad(n\ge1)
\]
is the standard orbit count: four involution-fixed torsion points and pairs for the remainder. It is not a newly unknown exact invariant. Finite orbit/discrepancy checks support the arithmetic but cannot establish an infinite analytic assertion. The proof repair clarifies a known implication and invalid citation; it does not create an independently useful unknown datum.

## Limitations and reproducibility

Only positive-radius disk subsets are claimed. A typeIII Gauss point can have an infinite orbit; it is not such a disk. No statement is made for arbitrary singletons, wild residue characteristic, higher-rank coefficient fields, or all Tate parameters. No formal proof or external expert attestation is claimed.

The original unchanged artifact is \(\texttt{artifacts/tent\_ledger.py}\); it checks rational tent orbits for denominators up to200, torsion counts through6 and folded-grid discrepancy through10. Those finite checks are auxiliary, not the proof above.

## Sources and inspected scope

- R. L. Benedetto, [Non-Archimedean Dynamics in Dimension One: Lecture Notes](https://swc-math.github.io/aws/2010/2010BenedettoNotes-09Mar.pdf) (2010), 87-page PDF. Complete relevant statements/proofs of Proposition3.14,3.15 (printed19–21/PDF18–20), Proposition3.28 (printed25/PDF24), Definitions6.1/6.4 and the closure distinction (printed52,56–57/PDF51,55–56), Theorem6.12 and Proposition6.13 (printed61–63/PDF60–62), Proposition7.1, Proposition7.16/Corollary7.17/Remark7.18 (printed78–79/PDF77–78), and Theorem7.20 (printed81/PDF80) were inspected. This is not a claim of reading all87 pages.
- R. L. Benedetto et al., [Current Trends and Open Problems in Arithmetic Dynamics](https://arxiv.org/html/1806.04980), full relevant Section17 component definitions, Theorems17.2/17.4 and qualifications. The original Compositio2000 no-wandering paper was not directly retrieved; the theorem used here was read in the author's own lecture and primary coauthor exposition.
- R. L. Benedetto, [Non-Archimedean Dynamics in Dimension One: Project Descriptions](https://swc-math.github.io/aws/2010/2010BenedettoProjects-0210.pdf), relevant complete Project2(d–f) and Project3(h), pp.2–3. The Julia-segment/folding description is prior theory.
- J. H. Silverman, [The Arithmetic of Elliptic Curves](https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf), second edition, Appendix C.14, complete relevant Tate coefficient/coordinate formulas and Theorem14.1 statement, printed444–445/PDF454–455 of the522-page PDF. No whole-book read is claimed. The specialized duplication rational formula above is an algebraic deduction from the general Weierstrass formula.
- J. Rivera-Letelier, [Irrational Fatou components in non-Archimedean dynamics](https://arxiv.org/html/2505.09383), relevant full introduction, theorem statements and Lattès comparison. The rank-at-least-two wandering result does not cover \(\mathbb C_5\), but its inapplicability does not remove the stronger locally-compact prior coverage.
