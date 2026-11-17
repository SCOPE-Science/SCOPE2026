# An exact spatial zeta function for phase-locked traveling waves of elementary cellular automaton Rule 6

## Finding

Consider elementary binary cellular automaton Rule 6, and its indexed cyclic ring of length \(n\ge3\). Among its configurations, single out the spatially translating, two-step phase-locked solutions satisfying \(F_n^2(x)=R_n^2(x)\), where \(R_n\) shifts every symbol one place to the left. Their exact number is
\[
B_n=1+2(-1)^n+u_n,\qquad u_0=3,\quad u_1=2,\quad u_2=0,\quad u_{n+3}=2u_{n+2}-2u_{n+1}+2u_n.
\]
The spatial shift restricted to this phase-locked family has the exact Artin–Mazur zeta function
\[
\zeta_R(z)=\exp\left(\sum_{n\ge1} \frac{B_n}{n}z^n\right)=\frac{1}{(1-z)(1+z)^2(1-2z+2z^2-2z^3)}.
\]
Here the formula for \(B_n\) is asserted for \(n\ge3\); its extension to lengths one and two is a transfer-matrix convention in which local positions may overlap. The periodic-point counts for these short lengths agree with the displayed rational zeta identity. The spatial topological entropy of the phase-locked subshift is \(\log\alpha\approx0.4341750147\), where \(\alpha\approx1.543689012692\) is the positive real root of \(t^3-2t^2+2t-2\). Thus \(B_n=\alpha^n+O(1.139^n)\). This is a positive-entropy family of *genuine periodic traveling waves* of Rule 6, while its fraction among all \(2^n\) cyclic configurations tends to zero.

## Assumptions and scope

For a binary word \(x=(x_i)_{i\in\mathbb Z/n\mathbb Z}\), indices are read modulo \(n\). Define the synchronous Rule 6 map by
\[
(F_nx)_i=f(x_{i-1},x_i,x_{i+1}),\qquad f(a,b,c)=(1-a)(b\mathbin{\mathrm{xor}}c).
\]
Thus the output is one only for neighborhoods 001 and 010 in the usual 111-to-000 elementary-rule order. The spatial left shift is \((R_nx)_i=x_{i+1}\). Equivalently, with the co-moving update \(G_n=R_n^{-1}F_n\), the phase-locked family is exactly \(\operatorname{Fix}(G_n^2)\); this is a natural co-moving temporal-two periodic-point set. No quotient by cyclic rotation is made in \(B_n\); all starting indices are distinguished. The assertion is about the naturally defined phase-locked family, not the entire recurrent set of Rule 6 or the claim that all Rule 6 orbits are traveling waves.

## Proof

An indexed cyclic word lies in this family if and only if, at each index, the following five-bit condition holds:
\[
f\bigl(f(a,b,c),f(b,c,d),f(c,d,e)\bigr)=e,
\qquad (a,b,c,d,e)=(x_{i-2},x_{i-1},x_i,x_{i+1},x_{i+2}).
\]
Indeed the left side is exactly \((F_n^2x)_i\) and the right side is \((R_n^2x)_i\). Form a directed multigraph with states the sixteen binary quadruples \(s=(a,b,c,d)\), and a directed edge from \((a,b,c,d)\) to \((b,c,d,e)\), for each \(e\in\{0,1\}\) obeying the condition above. Let \(T\) be its explicitly determined integer adjacency matrix. An indexed admissible cyclic word corresponds bijectively to a rooted length-\(n\) closed walk in this graph: read successive overlapping quadruples around the ring. The overlapping-window construction also handles \(n=3\), with repeated positions understood modulo \(n\). Therefore \(B_n=\operatorname{tr}(T^n)\).

Direct elimination of the sixteen state variables in the determinant, reproduced by the accompanying exact-arithmetic script, gives the identity
\[
\det(tI-T)=t^{10}(t-1)(t+1)^2(t^3-2t^2+2t-2).
\]
Hence its nonzero eigenvalues consist of \(1\), a double \(-1\), and the three roots of the cubic. The trace of a positive power is the corresponding power sum, yielding the formula for \(B_n\) and the displayed integer recurrence by Newton identities. The formal series identity \(\exp(\sum_{n\ge1}\operatorname{tr}(T^n)z^n/n)=\det(I-zT)^{-1}\) proves the zeta formula.

The cubic has a simple real root \(\alpha\in(1.5436,1.5438)\) and a conjugate pair whose squared modulus is \(2/\alpha\), since the product of all roots is two. In particular their modulus is below \(1.139<\alpha\), giving the claimed asymptotic and entropy. Irreducibility of the positive-entropy component can also be read from the finite transfer graph; alternatively the explicit trace growth and the finite-type presentation show its entropy is the logarithm of its spectral radius \(\alpha\). Finally, \(F_n\) and \(R_n\) commute. If \(F_n^2x=R_n^2x\), induction gives \(F_n^{2n}x=R_n^{2n}x=x\), proving genuine temporal periodicity; for even \(n\), \(F_n^nx=x\) already.

A primitive spatial necklace count is consequently available for all \(n\ge3\):
\[
M_n=\frac1n\sum_{d\mid n}\mu(d)\,B_{n/d},
\]
where \(B_1\) and \(B_2\) use the same five-bit overlap convention. This count classifies spatially primitive configurations, not temporal least periods.

## Verification

The supplied standalone `verification/check_rule6.py` builds the full sixteen-state matrix from the local equation and computes its characteristic polynomial and \(\det(I-zT)\) with exact symbolic arithmetic. Independently, a direct per-vertex implementation iterates over all \(\sum_{n=3}^{15}2^n=65{,}528\) labeled binary ring configurations. Both methods agree on every count for \(3\le n\le15\); the direct calculation also verifies the temporal return identity for every qualifying configuration. The exact determinant calculation, rather than finite enumeration, establishes the formulas for every length. The captured output is `verification/check_rule6.out`. These computational checks are reproducible, not independent external certification.

## Relationship to prior work

Wolfram's elementary-cellular-automaton framework (1983) establishes the model and Rule numbering; the later *Cellular Automaton Properties* tables give finite-ring data for individual rules. Neither inspected accessible material supplies this all-length exact enumeration of solutions of the specific space–time locking equation or its cubic zeta function. General finite-type and symbolic-dynamical theory explains why such transfer-matrix zeta functions are rational, but does not supply these particular Rule 6 coefficients. Published results concerning temporal two-cycles of Rule 18, temporal three-cycles of Rule 62, one-step images of Rule 110, and one-step image entropies across elementary rules have distinct dynamical predicates; none implies the displayed phase-lock equation and its exact count without additional analysis. The comparison is limited by incomplete access to all historical individual-rule tables.

## Limitations

The theorem does not enumerate every Rule 6 attractor, temporal least period, basin, or transient time. The wave family is not defined by all possible spatial velocities: the chosen equation fixes a specific displacement in two updates. The zeta function is for spatial shifts within this family, not for the global temporal map on all binary rings. A matching formula in an unexamined earlier source remains a priority risk; no claim of an independent mathematical audit is made.

## References

1. S. Wolfram, *Statistical Mechanics of Cellular Automata*, Reviews of Modern Physics 55 (1983), 601–644, DOI: 10.1103/RevModPhys.55.601 (published July 1, 1983).
2. S. Wolfram, *Cellular Automaton Properties*, published collection of finite-ring rule tables: https://content.wolfram.com/sw-publications/2020/07/cellular-automaton-properties.pdf.
3. S. Wolfram, *A New Kind of Science*, notes on elementary automaton rule numbering: https://www.wolframscience.com/nks/chap-3--the-world-of-simple-programs--notes/.
