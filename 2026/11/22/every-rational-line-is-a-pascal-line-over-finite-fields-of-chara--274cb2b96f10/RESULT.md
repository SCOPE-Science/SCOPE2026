# Every rational line is a Pascal line over finite fields of characteristic at least five

## Finding

Let \(K\subset\mathbb P^2_{\mathbb F_q}\) be any nonsingular conic, where \(q\) is an odd prime power of characteristic at least five. Consider **all** cyclic orderings of six pairwise distinct \(\mathbb F_q\)-rational points of \(K\), identified under cyclic rotation and reversal. There are \(60\binom{q+1}{6}\) such *unoriented rational hexagons*. Associate to each the Pascal line through the three intersections of its opposite side pairs, counting hexagons with multiplicity even if distinct hexagons have coincident Pascal lines.

Put \(\epsilon=\chi_q(-3)\), where \(\chi_q\) is the quadratic character of \(\mathbb F_q\). The number of these hexagons having any specified rational line \(L\) as their Pascal line is:

\[
\begin{array}{c|c|c}
\#(L\cap K)(\mathbb F_q)&\text{number of such rational lines}&\text{hexagons per line}\\
\hline
2& q(q+1)/2&\displaystyle \frac{(q-1)((q-5)^2(q-3)-2(1+\epsilon))}{12}\\[6pt]
1& q+1 &\displaystyle\frac{q(q-1)(q-4)(q-5)}{12}\\[6pt]
0& q(q-1)/2 &\displaystyle\frac{(q+1)(q^3-7q^2+15q-13+2(1+\epsilon))}{12}.
\end{array}
\]

These three types are respectively secants, tangents, and exterior lines (a nonsplit intersection with the conic). In characteristic at least five, \(q=5\) gives multiplicities \((0,0,6)\). For **every \(q\ge7\)** in the stated domain, every multiplicity is positive: the Pascal-line map from rational hexagons is **surjective onto all \(q^2+q+1\) rational projective lines**. In particular, at \(q=7\) the multiplicities are \((6,21,64)\) for all \((28,8,21)\) lines of the three types. The formulas cover every extension-degree prime power, not just prime fields.

## Assumptions and scope

The conic is geometrically nonsingular and split, as every nonsingular conic over a finite field is. An unoriented hexagon means a six-vertex cyclic ordering modulo the dihedral group of order twelve, **not** a set of six points without a cyclic order. The three opposite side pairs for a hexagon \((A,B,C,D,E,F)\) are \((AB,DE)\), \((BC,EF)\), and \((CD,FA)\); their intersection points lie on one Pascal line. Every six-vertex configuration is counted exactly once per unoriented cyclic ordering. No general-position assumption about additional Pascal coincidences is made. The characteristic hypotheses ensure that the elementary quadratic-character calculations below have separable factors, notably that \(2\), \(3\), and \(4\) are invertible.

## Proof

**1. Normalization and the line equation.** Choose \(P(t)=[t^2:t:1]\) for finite \(t\in\mathbb F_q\) and \(P(\infty)=[1:0:0]\). The order-three transitivity of \(G=\operatorname{PGL}_2(\mathbb F_q)\) is sharp: every ordered triple of distinct conic points is carried uniquely to \((P(\infty),P(0),P(1))\). Thus every ordered sextuple has a unique representation
\[
 (gP(\infty),gP(0),gP(1),gP(x),gP(y),gP(z)),\qquad g\in G,
\]
where \(x,y,z\in U:=\mathbb F_q\setminus\{0,1\}\) are pairwise distinct. In particular \(|G|=q(q^2-1)\) and the number of normalized triples is \(N=(q-2)(q-3)(q-4)\). Computing opposite-chord intersections by cross products gives the Pascal line coefficients
\[
[-z:\; x(y+z-1)+z:\;-xyz].
\]
The conic intersection discriminant, after division by the nonzero square \(z^2\), is
\[
D(x,y,z)=(1+kx)^2-4xy,\qquad k=\frac{y+z-1}{z}.
\]
Its quadratic character is \(1,0,-1\) exactly for the secant, tangent, and exterior types. Write \(A_S,A_T,A_E\) for the counts of normalized triples in these types.

**2. Character-sum evaluation.** For fixed distinct \(y,z\in U\), the polynomial \(z^2D\) in \(x\) has discriminant \(16yz^3(y-1)(z-1)\ne0\). The complete quadratic-character sum over \(x\in\mathbb F_q\) is \(-1\) if \(k\ne0\), and \(0\) if \(k=0\), when the polynomial is linear. There are \(q-3\) pairs \((y,z)\) with \(y+z=1\). Hence the complete three-variable sum before removing forbidden values of \(x\) is \(-(q-3)^2\).

The values \(x=0\) and \(x=z\) each contribute character \(1\), for a total subtraction \(2(q-2)(q-3)\). For \(x=1\) we have
\[
z^2D(1,y,z)=(y-1)(y-(2z-1)^2).
\]
For each fixed \(z\in U\), the complete sum in \(y\) is \(-1\); deleting \(y=0,1,z\) and using \(\sum_{z\in U}\chi_q(1-4z)=-1-\epsilon\) yields
\[
\sum_{\substack{y,z\in U\\y\ne z}}\chi_q(D(1,y,z))=-2q+6+\epsilon.
\]
For \(x=y\) one obtains
\[
z^2D(y,y,z)=(y-1)(y-z)(y^2+3yz-y+z).
\]
As a polynomial in \(z\), this is a product of two distinct linear factors for \(y\in U\), except that its leading coefficient may vanish at \(y=-1/3\); the linear case has character sum zero. Summing over all \(z\) gives \(-\chi_q(-(y-1)(3y+1))\), including the exceptional case. On removing \(z=0,1,y\), and using the quadratic-character identity
\[
\sum_{y\in U}\chi_q(-(y-1)(3y+1))=-\epsilon-1,
\]
we get the same contribution \(-2q+6+\epsilon\). Therefore
\[
S:=A_S-A_E=-(q-3)^2-2(q-2)(q-3)-2(-2q+6+\epsilon)
=-3q^2+20q-33-2\epsilon.
\]
Every character-sum identity follows from the standard complete-sum rule \(\sum_{t\in\mathbb F_q}\chi_q(at^2+bt+c)=-\chi_q(a)\) for a quadratic of nonzero discriminant and nonzero leading coefficient, together with the zero sum for a nonconstant linear polynomial. The exclusions above explicitly treat the exceptional linear case.

**3. Tangent triples.** The same discriminant calculation gives the total number of zeros of \(D\) over **all** \(x\in\mathbb F_q\), summed over distinct \(y,z\in U\), as
\[
(q-2)(q-3)+(3-q)-(q-3)=(q-3)(q-4).
\]
Indeed the sum of \(\chi_q(y(y-1))\chi_q(z(z-1))\) over distinct \(y,z\in U\) equals \(3-q\), and the \(q-3\) pairs with \(k=0\) need one correction each. The deleted \(x=0,z\) never yield zeros. The deleted \(x=1\) yields a zero exactly when \(y=(2z-1)^2\), giving \(q-4\) admissible pairs after excluding \(z=1/2,1/4\). The deleted \(x=y\) yields a zero exactly when \(z=-y(y-1)/(3y+1)\), giving another \(q-4\) admissible pairs after excluding \(y=-1/3,-1\). These excluded triples are disjoint because \(x,y,z\) are required pairwise distinct. Consequently
\[
A_T=(q-3)(q-4)-2(q-4)=(q-4)(q-5).
\]
Now \(A_S+A_T+A_E=N\), so from the preceding character sum
\[
A_S=\frac{(q-5)^2(q-3)-2(1+\epsilon)}2,
\quad
A_E=\frac{q^3-7q^2+15q-13+2(1+\epsilon)}2.
\]

**4. Recovering each line fiber.** The group \(G\) is transitive on rational secant lines, tangent lines, and nonsplit exterior lines, with orbit cardinalities respectively \(q(q+1)/2\), \(q+1\), and \(q(q-1)/2\). Each normalized triple of a given type gives \(|G|\) ordered sextuples of that type, equidistributed over the lines in that orbit. Dividing the resulting per-line number of ordered sextuples by twelve (the free action of rotations and reversal on six distinct ordered vertices) gives the three boxed multiplicities. This argument remains valid when several different hexagons accidentally produce the same line. Positivity is immediate at \(q=7\) from \((6,21,64)\), and the three displayed formulas are positive for every larger permitted odd prime power: the secant numerator grows from a positive \(q=7\) value (the possible correction is at most four), the tangent factors are positive, and the exterior cubic is increasing and already positive at \(q=7\). This proves the surjectivity assertion.

## Verification

Run `python3 verify_pascal.py` using Python 3.9 or later with no external packages. The companion `verification_output.txt` is from executing that standalone script. For the prime fields of sizes \(5,7,11,13\), it constructs every hexagon from all rational conic points, computes the three opposite-side intersections as exact projective cross products, checks collinearity, enumerates the **entire rational line distribution**, and matches the three formulas. Independently, it exhaustively enumerates normalized distinct triples in prime fields of sizes \(5,7,11,13,17,19,23,29\); the last calculation uses the extension field \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-2)\). All checks completed. These finite experiments are regression checks, not the proof of the theorem for all prime powers; Steps 1–4 above supply that proof.

## Relationship to prior work

Chipalkatti's *On the Enumerative Geometry of Pascal's Hexagram* (2023), notably Proposition 2.1, studies the four-dimensional variety of six-point configurations with **one fixed Pascal line**, and then enumerates the solutions to **three specified** Pascal-line constraints over the complex field. Its one-line parametrization is a substantial antecedent to the present problem, but that article does not determine the three different finite-field rational fiber multiplicities, their quadratic-character dependence, or the all-line surjectivity boundary. Chipalkatti and Da Silva (2022) examine degenerations when conic vertices collide; here all vertices remain distinct. The previously determined six-point case over \(\mathbb F_5\) gives the special values \((0,0,6)\), which are contained in, but do not imply, this universal theorem. The published Pascal–Kirkman Frobenius spectrum concerns sixty lines from one *fixed generic* sextuple, whereas this theorem sums over **every rational sextuple on the entire conic**. These are different quantifications. The character sums could potentially have an equivalent expression in older finite-projective-geometry literature; that remains a priority risk rather than a claim of absolute uniqueness.

## Limitations

Only smooth conics over finite fields of characteristic at least five are asserted; characteristic two or three, repeated vertices, and nonreduced configuration schemes are excluded. Hexagon preimages are counted as geometric cyclic arrangements of six distinct rational vertices, not as distinct line images. The theorem classifies the fibers of the single Pascal-line map by conic-line type; it does not classify every simultaneous coincidence or higher-order incidence among the sixty Pascal lines of a fixed sextuple. The computation has been checked by a single mathematical review; independent scientific audit remains to be performed.

## References

- Jaydeep Chipalkatti, *On the Enumerative Geometry of Pascal's Hexagram*, arXiv:2303.10319, publicly posted 2023-03-18, https://arxiv.org/abs/2303.10319. In particular, §2, Proposition 2.1, is the closest geometric fiber antecedent.
- Jaydeep Chipalkatti and Sergio Da Silva, *Degenerations of Pascal Lines*, arXiv:2202.12975, publicly posted 2022-02-25, https://arxiv.org/abs/2202.12975.
- Jaydeep Chipalkatti and Andrew Ryba, *Absolute Projectivities in Pascal's Multimysticum*, arXiv:2007.04315, https://arxiv.org/abs/2007.04315.
- Jaydeep Chipalkatti, *Enumerative Geometry of Pascal's Theorem*, lecture slides dated 2023-09-28, https://www.math.fsu.edu/~agashe/chipalkatti.pdf.
