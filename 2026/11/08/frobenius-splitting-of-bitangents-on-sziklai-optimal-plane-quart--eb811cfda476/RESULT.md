# Frobenius splitting of bitangents on Sziklai-optimal plane quartics over \(\mathbb F_5\)

## Finding
Let \(C/\mathbb F_5\) be a smooth plane quartic with \(16\) rational points (equality in the Sziklai bound). A bitangent means a geometric line \(L\) for which \(C\cdot L=2D\) for some effective divisor \(D\) of degree \(2\); hyperflex lines, for which \(D=2P\), are included. The \(28\) geometric bitangents have Frobenius cycle lengths
\[
2,2,4,4,4,4,4,4.
\]
Consequently the exact number of bitangent lines defined over \(\mathbb F_{5^n}\), for every integer \(n\ge1\), is
\[
\#\operatorname{Bit}(C)(\mathbb F_{5^n})=
\begin{cases}
0,&n\text{ odd},\\
4,&n\equiv2\pmod4,\\
28,&4\mid n.
\end{cases}
\]
The smallest field defining *all* bitangents is \(\mathbb F_{625}\), whereas exactly four appear already over \(\mathbb F_{25}\). Equivalently, among the \(28\) odd geometric theta characteristics, none is \(\mathbb F_5\)-rational, four are \(\mathbb F_{25}\)-rational, and all are \(\mathbb F_{625}\)-rational.

## Assumptions and scope
The base field is exactly \(\mathbb F_5\). The smoothness and geometric integrality of \(C\) are required. An optimal quartic has \(16\) rational points. All bitangents are geometric lines of the *canonical plane embedding*; the theorem counts their fields of definition, not the rationality of their contact points or distinct isomorphism classes of degree-two del Pezzo surfaces. The Frobenius is the coordinatewise fifth-power map on the dual projective plane.

## Proof
**Reduction to one rational normal form.** Ferreira and Speziali, Theorem 4.4, prove that any plane quartic attaining the degree-four Sziklai bound over \(\mathbb F_5\) is projectively equivalent over \(\mathbb F_5\) to
\[
\alpha X^4+\beta Y^4+\gamma Z^4=0,
\qquad \alpha,\beta,\gamma\in\mathbb F_5^*,\quad
\alpha+\beta+\gamma=0.
\]
There are exactly twelve ordered nonzero triples satisfying this equation. Each is obtained from \((1,1,3)\) by a coordinate permutation and common nonzero scalar, because the only unordered scalar types are \((1,1,3)\) and \((1,2,2)\), and the latter equals a permutation of \(2(1,1,3)\). Thus all such curves are projectively equivalent **over the base field** to
\[
C_0:\quad X^4+Y^4+3Z^4=0.
\]
This model is smooth: its three derivatives are nonzero multiples of the coordinate cubes and have no common projective zero. It has exactly \(16\) rational points, namely those with all three coordinates nonzero (nonzero fourth powers in \(\mathbb F_5\) equal \(1\)). The projective equivalence preserves Frobenius on the bitangent set.

**Explicit complete bitangent set.** Work over \(\overline{\mathbb F}_5\). Define
\[
R_4=\{s:s^4=4\},\qquad R_2=\{s:s^4=2\}.
\]
Both sets have four distinct elements. There are twelve hyperflex lines
\[
X=sY\ (s\in R_4),\quad
X=sZ\ (s\in R_2),\quad
Y=sZ\ (s\in R_2).
\]
For example, restricting the equation to \(X=sY\), where \(s^4=4=-1\), gives \(3Z^4\); the other two families restrict to fourth powers \(Y^4\) and \(X^4\), respectively. Hence all twelve are hyperflexes.

There are another sixteen lines
\[
Z=uX+vY,\qquad u,v\in R_2.
\]
On each, the restricted quartic is the exact square
\[
X^4+Y^4+3(uX+vY)^4
=(u^2X^2+uvXY+v^2Y^2)^2.
\]
The quadratic has discriminant \(-3u^2v^2=2u^2v^2\ne0\), so these are ordinary bitangents, not hyperflexes. The twenty-eight displayed lines are pairwise distinct: their coefficient-zero patterns separate the first twelve, and the last sixteen all have normalized \(Z\)-coefficient \(1\). In characteristic different from two a smooth plane quartic has exactly \(28\) geometric odd theta characteristics and hence \(28\) bitangent lines, counting hyperflexes. Thus this list is exhaustive.

**Arithmetic Frobenius cycles.** If \(s^4=4\), then \(s^5=4s=-s\). As \(s\ne0\), its fifth-power orbit has length exactly \(2\). The four lines of the first hyperflex type therefore form two \(2\)-cycles.

If \(s^4=2\), then \(s^5=2s\). Since \(2\in\mathbb F_5^*\) has multiplicative order \(4\), its fifth-power orbit has length exactly \(4\). The eight hyperflex lines of the remaining two types consequently form two \(4\)-cycles. On the ordinary bitangent set, the Frobenius map sends the normalized coefficient pair \((u,v)\) to \((2u,2v)\), again with orbit length exactly \(4\), giving four more \(4\)-cycles. This proves the asserted cycle decomposition and all extension-field counts.

## Verification
Running `python verify_symbolic.py` performs exact arithmetic in \(\mathbb F_5[t]/(t^4-2)\), constructs the \(28\) line equations, verifies their square restrictions, checks pairwise distinctness and the fifth-power orbit decomposition, and checks the twelve nonzero coefficient triples form one permutation-and-scalar orbit. Running `python verify_f25.py` independently enumerates all \(31\) lines over \(\mathbb F_5\) and all \(651\) lines over \(\mathbb F_{25}\), testing exactly whether the binary quartic restriction is a scalar multiple of a square; it finds respectively \(0\) and \(4\). Both tests use pure Python and assert expected exact identities. The characteristic-independent \(28\)-bitangent bound is a classical theorem, used as a separate mathematical input to prove completeness.

## Relationship to prior work
Ferreira–Speziali (2022, Theorem 4.4) supplies the Sziklai-extremal plane-curve normal form; that classification is **not new** here. Classical equations for the geometric twenty-eight bitangents of the complex Fermat/Dyck quartic go back to Cayley and were recorded by Edge (1938). Bethea–Brazelton (2024, §4.2) determines the geometric automorphism-group bitangent orbits of sizes \(12\) and \(16\) over characteristic zero. Those orbit sizes are **not new** here. The extra arithmetic determination is the fifth-power Galois action on the unique rational \(16\)-point quartic over \(\mathbb F_5\), whose orbits instead have lengths \(2,2,4,4,4,4,4,4\). Betten–Kaplan–Karaoglu (2021) tabulates quartics and geometric bitangents over some small finite fields, including \(\mathbb F_{25}\), but does not supply this F5 Frobenius cycle calculation in its accessible dataset. The assertion concerns rational descent and is not an assertion about geometric automorphism orbits.

## Limitations
This arithmetic classification applies only to smooth plane quartics meeting the Sziklai bound over \(\mathbb F_5\). It does not classify arbitrary genus-three curves or general quartic twists. The projective uniqueness is taken from published work; the theorem does not reprove that classification. Classical bitangent formulas imply important components of the computation, so an equivalent older arithmetic specialization remains a historical-priority risk. This is a self-review, not independent mathematical or historical certification.

## References
1. W. de P. Ferreira and P. Speziali, *Optimal plane curves of degree q−1 over a finite field*, arXiv:2211.14288v1 (25 Nov 2022), Theorem 4.4. https://arxiv.org/abs/2211.14288
2. C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242v1 (11 Oct 2024), §4.2 and Remark 4.4. https://arxiv.org/abs/2410.09242
3. A. Betten, N. Kaplan and F. Karaoglu, *Classification of Quartic Curves Over Small Finite Fields*, online dataset (29 Oct 2021). https://www.math.colostate.edu/~betten/mathdata/quartic_curves.html
4. W. L. Edge, *Determinantal representations of x4+y4+z4*, Math. Proc. Camb. Phil. Soc. 34 (1938), 6–21. https://doi.org/10.1017/S0305004100019848
