# Prime-power collision zeta and first-lift reversal for unit-perturbed biquadratics

## Finding
For each odd prime \(p\), unit \(c\in\mathbb Z_p^\times\), and integer \(k\ge1\), put \(q=p^k\) and
\[
f_c(x)=x^4+cx^2,\qquad
N_{p,k,c}(z)=\#\{x\bmod q:f_c(x)\equiv z\pmod q\}.
\]
The **equal-value collision count**, or second fiber moment, is
\[
E_{p,k}(c)=\sum_{z\bmod q}N_{p,k,c}(z)^2
=\#\{(x,y)\bmod q:f_c(x)\equiv f_c(y)\pmod q\}.
\]
Let \(\chi_p\) be the quadratic character modulo \(p\), with \(\chi_p(0)=0\), and define \(\epsilon=\chi_p(-1)\) and \(\eta=\chi_p(-c/2)\in\{-1,1\}\). Here division by two means inversion modulo \(p\). Then for **every** \(k\ge1\),
\[
\boxed{E_{p,k}(c)=p^{k-1}\left[3p-3-\epsilon-2\eta+(k-1)(p-1)(3+2\eta)\right].}
\tag{1}
\]
In particular, the count depends on \(c\) only through its quadratic class modulo \(p\), not through any higher \(p\)-adic digit. For \(c_+,c_-\in\mathbb Z_p^\times\) with \(\chi_p(-c_+/2)=1\), \(\chi_p(-c_-/2)=-1\),
\[
\boxed{E_{p,k}(c_+)-E_{p,k}(c_-)=4p^{k-1}\big((k-1)(p-1)-1\big).}
\tag{2}
\]
Thus the positive-character class has **four fewer** collision pairs modulo \(p\) but **strictly more** modulo \(p^k\) for every \(k\ge2\), a uniform first-lift reversal. The collision generating function is the rational series
\[
\sum_{k\ge1}E_{p,k}(c)T^k=
\frac{(3p-3-\epsilon-2\eta)T}{1-pT}
+\frac{(3+2\eta)(p-1)pT^2}{(1-pT)^2}.
\tag{3}
\]
Its double-pole coefficient changes by a factor of five between the two coefficient classes. Equivalently, for a uniformly chosen target residue, the fiber multiplicity has mean one and variance
\[
\operatorname{Var}_z N_{p,k,c}(z)=\frac{2p-3-\epsilon-2\eta+(k-1)(p-1)(3+2\eta)}{p},
\]
which grows linearly with the precision; the two possible slopes are \((p-1)/p\) and \(5(p-1)/p\).

## Assumptions and scope
The input and target spaces are the residue ring \(\mathbb Z/p^k\mathbb Z\), not the finite field \(\mathbb F_{p^k}\). The coefficient may be any integer not divisible by \(p\), or any unit of \(\mathbb Z_p\); its residue modulo \(p^k\) determines the map. The collision count uses **ordered** pairs, including the diagonal. Every odd prime, including \(p=3\), and every positive exponent are covered. No assertion is made at \(p=2\) or when \(p\mid c\).

## Proof
**1. Factor the collision equation.** In \(\mathbb Z[x,y]\) one has
\[
f_c(x)-f_c(y)=(x-y)(x+y)(x^2+y^2+c).
\tag{4}
\]
Write these factors as \(L_-=x-y\), \(L_+=x+y\), and \(Q=x^2+y^2+c\). Modulo the odd prime \(p\), all three curves are smooth on their zero loci: the two lines have nonzero gradients, and \(\nabla Q=(2x,2y)\) vanishes only at \((0,0)\), which is not on \(Q=0\) because \(c\) is a unit.

**2. Count and classify the mod-\(p\) zero points.** Each line has \(p\) points. The conic \(Q=0\) has \(p-\epsilon\) points. Indeed, for \(a=-c\ne0\),
\[
\#\{(x,y)\in\mathbb F_p^2:x^2+y^2=a\}=p+\sum_{x\in\mathbb F_p}\chi_p(a-x^2)=p-\chi_p(-1).
\]
The character sum follows by counting the solutions to \(v^2-u^2=a\): the change of variables \((v-u,v+u)\) gives \(p-1\) solutions, while \(\sum_u(1+\chi_p(u^2+a))=p+\sum_u\chi_p(u^2+a)\), hence \(\sum_u\chi_p(u^2+a)=-1\) for \(a\ne0\). Rescaling \(u\) gives the displayed identity.

The two lines meet at \((0,0)\), and each line meets \(Q\) in exactly \(1+\eta\) points, since there \(2x^2=-c\). There is no triple intersection. Consequently the number of mod-\(p\) points lying on at least two components is
\[
I=1+2(1+\eta)=3+2\eta\in\{1,5\}.
\tag{5}
\]
By inclusion–exclusion the number on their union is
\[
U=3p-3-\epsilon-2\eta.
\tag{6}
\]
These are precisely the \(U\) solutions to (4) modulo \(p\). The remaining \(U-I\) zeros lie on exactly one component.

**3. Lift the smooth points.** At a residue point where exactly one factor vanishes, the gradient of the product (4) is nonzero modulo \(p\). Fixing either coordinate freely and using the one-variable Hensel lemma on the other at each digit shows that this residue point has exactly \(p^{k-1}\) lifts satisfying (4) modulo \(p^k\). The same holds if the unique zero component is the conic, since at least one partial derivative of \(Q\) is a unit.

**4. Lift each crossing.** At the line–line crossing \((0,0)\), the coordinate map \((x,y)\mapsto(L_-,L_+)\) has unit determinant \(2\), and \(Q\) is a unit. At a line–conic crossing \((t,\pm t)\), one has \(t\ne0\); the Jacobian determinant of \((L_\pm,Q)\) is a unit (equal up to sign to \(4t\)), and the third factor is a unit. Therefore, by the inverse form of Hensel's lemma, each crossing residue disk is bijective at every level to pairs \((u,v)\equiv(0,0)\pmod p\), with the collision equation equivalent to \(uv\equiv0\pmod{p^k}\).

For such pairs, there are \(p^{k-1}\) with \(u=0\). For each valuation \(i\in\{1,\ldots,k-1\}\), exactly \((p-1)p^{k-i-1}\) values of \(u\) have valuation \(i\), and the congruence demands that \(v\) be divisible by \(p^{k-i}\), giving \(p^i\) values. Thus each crossing lifts to
\[
W_k=p^{k-1}+\sum_{i=1}^{k-1}(p-1)p^{k-1}
=p^{k-1}\bigl(1+(k-1)(p-1)\bigr).
\tag{7}
\]
For \(k=1\), the empty sum correctly gives \(W_1=1\). As every solution modulo \(p^k\) lies over exactly one of the classified mod-\(p\) zeros, combining the disjoint disks gives
\[
E_{p,k}(c)=(U-I)p^{k-1}+IW_k
=p^{k-1}\bigl(U+(k-1)(p-1)I\bigr),
\]
which proves (1) after substituting (5) and (6).

**5. Reversal and generating series.** Taking the difference between \(\eta=1\) and \(\eta=-1\) in (1) gives (2), negative at \(k=1\) and positive for every \(k\ge2\), since \((k-1)(p-1)\ge2\). Summing geometric and differentiated geometric series in (1) gives (3). This finishes the proof.

## Verification
The standalone script `artifacts/verify.py` computes \(N_{p,k,c}(z)\) directly by tabulating \(f_c(x)\bmod p^k\), squares every fiber count, and compares its sum with (1). It additionally checks selected pairs directly from the original collision congruence, independently counts smooth and crossing points on the three curves over finite fields, and checks (2) in both coefficient classes. Its completed execution gave `PASS histogram_cases=105 input_residues=57885 direct_pair_checks=114015 finite_field_geometry_cases=35 phase_comparisons=24`. The finite checks are not a proof of the all-prime, all-exponent statement; that proof is Steps 1–5.

Run `python3 artifacts/verify.py` using Python 3 and no additional packages.

## Relationship to prior work
Seraj's 18 September 2023 preprint [1] studies the **sum of distinct outputs** of the same family \(x^4+cx^2+e\) modulo primes and its coefficient-class dependence. Its sections 1–3 and collision Lemmas 9–14, read in full as a source for this comparison, work in \(\mathbb F_p\); they do not state the ordered equal-value count at all prime-power exponents or the first-lift reversal. Li and Xiong [2] determine the more general **line-intersection distribution** of degree-four polynomial graphs over finite fields, in particular the classes \(x^4+cx^2\). This stronger finite-field result can give information about mod-\(p\) fibers but is not an all-\(k\) congruence count over the nonfield ring \(\mathbb Z/p^k\mathbb Z\). A published note [3] computes **additive graph energy** for \((x,x^4+cx^2)\) modulo \(p^2\), involving four variables and pair sums. That quantity is not \(E_{p,k}(c)\), which counts equal polynomial values in two variables. In particular, its prime-square result does not imply the full exponent tower (1)–(3). Another note [4] concerns the unperturbed quartic graph \((x,x^4)\) and a different four-variable additive invariant; neither the object nor the unit-coefficient scope matches.

## Limitations
The result is a complete formula for a **second moment**, not a target-by-target classification of all fiber multiplicities or the full value set. It excludes \(p=2\) and nonunit parameters \(c\). The mod-\(p\) case is elementary and overlaps methods known from finite-field quartic studies; the distinct contribution assessed here is the uniform higher-power count and resulting coefficient-class reversal. General normal-crossing lifting arguments are standard; other sources may contain an implicit equivalent specialized calculation, so bibliographic originality remains subject to independent checking. No independent mathematical audit has been performed.

## References
1. Samer Seraj, *Sum of Distinct Biquadratic Residues Modulo Primes*, arXiv:2309.13070v1, first posted 18 September 2023, https://arxiv.org/abs/2309.13070 .
2. Shuxing Li and Maosheng Xiong, *Intersection distribution of degree four polynomials over finite fields*, published online 4 October 2024, https://doi.org/10.1007/s10623-024-01488-6 .
3. *Exact fourth moments of unit-perturbed quartic graphs over prime-square rings*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-exact-fourth-moments-of-unit-perturbed-quartic-graphs-over-prime--327b026713c6 .
4. *Exact additive energy of the quartic graph over prime-power rings*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-additive-energy-of-the-quartic-graph-over-prime-power-ring--35db6c8e1cdf .
