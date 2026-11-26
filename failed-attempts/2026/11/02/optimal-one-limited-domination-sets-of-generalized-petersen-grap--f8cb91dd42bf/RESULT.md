# Optimal one-limited domination sets of generalized Petersen graphs with inner step three

## Finding
For every integer \(n\ge 7\), let \(G_n=\operatorname{GP}(n,3)\) be the generalized Petersen graph on the fixed, individually labelled vertices \(a_i,b_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). Let \(\mathcal D_n\) be the family of minimum-cardinality one-limited dominating subsets of \(V(G_n)\). Then
\[
\gamma^{\mathrm L}_1(G_n)=n,\qquad
|\mathcal D_n|=2+4\mathbf1_{\{4\mid n\}}+10\mathbf1_{\{5\mid n\}}.
\]
In particular the count is \(2\), \(6\), \(12\), or \(16\), according as neither, only \(4\), only \(5\), or both \(4\) and \(5\) divide \(n\).

More precisely, encode each member \(D\in\mathcal D_n\) by signs \(u_i\in\{-1,+1\}\), with \(u_i=+1\) precisely when \(a_i\in D\). The allowed cyclic outer words are exactly: the two constant words; four different indexed rotations of the four-letter pattern \((+,+,-,-)\) when \(4\mid n\); and, when \(5\mid n\), the five indexed rotations of each five-letter pattern \((+,+,-,-,-)\) and \((-,-,+,+,+)\). For each such outer word the inner selection is uniquely determined by the equation
\[
v_i=u_i-u_{i-1}-u_{i+1}\in\{-1,+1\},
\qquad b_i\in D\ \Longleftrightarrow\ v_i=+1.
\]
No other minimum sets occur, including when \(20\mid n\).

## Assumptions and scope
The vertex set consists of \(a_i\) and \(b_i\), for \(i\in\mathbb Z/n\mathbb Z\), and the edges are exactly \(a_i a_{i+1}\), \(a_ib_i\), and \(b_i b_{i+3}\). For \(n\ge7\) this is a simple cubic graph. A set \(D\) is *one-limited dominating* when each vertex outside \(D\) has at least one neighbor in \(D\), while every vertex inside \(D\) has at most one neighbor outside \(D\). Vertex labels are fixed: rotations and color-complements of assignments are counted as distinct subsets whenever they differ. The theorem concerns every integer \(n\ge7\), not just the tested finite range.

## Proof
**1. Equality and the perfect-crossing condition.** Write \(S=V(G_n)\setminus D\), and let \(e(D,S)\) count edges joining the two sets. Domination gives \(|S|\le e(D,S)\), while the one-limited condition gives \(e(D,S)\le |D|\). Since \(|D|+|S|=2n\), necessarily \(|D|\ge n\). Choosing all \(a_i\), or choosing all \(b_i\), gives a one-limited dominating set of cardinality \(n\). Thus the minimum is \(n\). At equality every vertex in either set has exactly one neighbor in the other set. Equivalently every vertex has two neighbors of its own sign and exactly one neighbor of the opposite sign; the crossed edges form a perfect matching.

**2. Linear recurrence.** Assign signs \(u_i,v_i\) to \(a_i,b_i\) according to membership of \(D\). Since a vertex's three neighbor signs sum to its own sign precisely when it has two neighbors of the same sign, the equality condition reads
\[
u_{i-1}+u_{i+1}+v_i=u_i,\qquad
v_{i-3}+v_{i+3}+u_i=v_i.
\]
Let \(E\) denote cyclic translation, \((Ew)_i=w_{i+1}\). The first equation says \(v=(1-E-E^{-1})u\). Substituting into the second gives
\[
\big[(1-E^3-E^{-3})(1-E-E^{-1})-1\big]u=0.
\]
Multiplication by \(E^4\) gives the polynomial identity
\[
E^4\big[(1-E^3-E^{-3})(1-E-E^{-1})-1\big]
=E^8-E^7+E^6-E^5-E^3+E^2-E+1
=(E-1)^2(E^2+1)(E^4+E^3+E^2+E+1).
\]
The operator \(E\) on complex sequences of period \(n\) is diagonalizable, because it satisfies \(E^n=1\) and \(z^n-1\) has distinct roots over \(\mathbb C\). Consequently every Fourier mode of \(u\) belongs to the eigenvalue \(1\), to a primitive fourth root, or to a primitive fifth root. Hence \(u\) is twenty-periodic (as well as \(n\)-periodic), and can be written as the sum of a four-periodic sequence and a five-periodic sequence.

**3. Binary additive rigidity.** We show that a sequence \(u_i\in\{-1,+1\}\) expressible as a sum of four- and five-periodic sequences actually has period dividing \(4\) or period dividing \(5\). The Chinese remainder correspondence identifies residues \(i\pmod{20}\) bijectively with pairs \((r,s)\in\mathbb Z/4\mathbb Z\times\mathbb Z/5\mathbb Z\); write \(u_i=A_r+B_s\). If \(A\) is nonconstant, select \(r,r'\) with \(\delta=A_r-A_{r'}\ne0\). As the row entries \(A_r+B_s\) and \(A_{r'}+B_s\) both lie in \(\{-1,+1\}\), their fixed nonzero difference is \(\delta=\pm2\). Each entry of the first row is then forced to the same sign, independent of \(s\), so \(B\) is constant. Otherwise \(A\) is already constant. Thus only one of the two periods can be essential; in particular no mixed twenty-periodic binary solution exists.

**4. Enumerating the surviving words.** The first vertex equation forces \(v_i=u_i-u_{i-1}-u_{i+1}\) to be a sign. If the two adjacent outer signs both oppose \(u_i\), the right-hand side has magnitude \(3\), which is impossible. In any other arrangement its magnitude is \(1\). Thus a cyclic sign word must have no singleton run. For period dividing \(4\), the only such words are the constants and the four rotations of \((+,+,-,-)\). For period dividing \(5\), they are the constants and the ten rotations of \((+,+,-,-,-)\) and its sign-complement. Direct substitution of these three representative types, together with their rotations and sign-complements, into the two equations in step 2 confirms that each is an actual solution.

A nonconstant word of fundamental period \(4\) can close around \(n\) precisely when \(4\mid n\). The nonconstant five-letter words have fundamental period \(5\) and close precisely when \(5\mid n\). The two constant outer words are always valid; their inner words are respectively the opposite constants. The patterns of fundamental periods \(4\) and \(5\) cannot coincide, even if \(20\mid n\). Thus there are exactly \(2+4\mathbf1_{\{4\mid n\}}+10\mathbf1_{\{5\mid n\}}\) distinct minimum dominating sets, as claimed.

## Verification
Run the included standalone standard-library script with `python3 verify.py`. It reconstructs the original graph independently and exhaustively checks all size-\(n\) candidate vertex subsets at \(n=7,8,9\), exhaustively classifies all \(2^{20}\) binary spin words of period \(20\), checks the polynomial identity by coefficient multiplication, and independently checks all constructed minimizers for \(7\le n\le100\). Those computations support, but do not replace, the all-\(n\) recurrence and rigidity proof above.

## Relationship to prior work
The cubic-graph lower bound and the interpretation of the equality case as a perfect matching edge-cut are known, including the characterization of Fakharan and coauthors and the exposition by Radić, Radić, and Tepeh. What is supplied here is the complete labelled enumeration and explicit classification for the fixed-inner-step-three generalized Petersen family.

The same configurations are perfect two-colorings with parameter matrix \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\). Alaeiyan and Karami (2016) prove existence of such a coloring on every generalized Petersen graph using the two monochromatic rings. Karami (2022) enumerates which *parameter matrices* are possible for \(\operatorname{GP}(n,3)\), including that matrix, rather than enumerating every realization of this matrix. The modular four- and five-period families and the exact count in the current statement are not implied by those existence results. These are close prior works, so completeness of historical priority is not claimed.

The older graph notion of \([1,2]\)-domination, which constrains the number of selected neighbors of each **unselected** vertex, is different from the present one-limited condition imposed on **selected** vertices, and does not give the current classification.

## Limitations
Only \(\operatorname{GP}(n,3)\), with \(n\ge7\), is classified. No extension to other inner steps, to arbitrary cubic graphs, or to non-minimum one-limited dominating sets is established. The graph-theoretic proof is complete; the attached finite checks are not a substitute for its infinite argument. Historical-priority verification is bounded by the inspected literature and may miss another equivalent formulation.

## References
- A. Tepeh, *On \(k\)-limited domination: complexity and Cartesian products*, arXiv:2606.22428, first submitted 21 June 2026. https://arxiv.org/abs/2606.22428
- G. Radić, G. Radić, and A. Tepeh, *Structural aspects of \(1\)-limited domination in cubic graphs*, arXiv:2610.26259, first submitted 19 October 2026. https://arxiv.org/abs/2610.26259
- M. Alaeiyan and H. Karami, *Perfect 2-colorings of the generalized Petersen graph*, Proceedings–Mathematical Sciences 126 (2016), 289–294. DOI:10.1007/s12044-016-0285-4.
- H. Karami, *Perfect 2-colorings of the generalized Petersen graph \(\operatorname{GP}(n,3)\)*, Electronic Journal of Graph Theory and Applications 10 (2022), 239–245. DOI:10.5614/ejgta.2022.10.1.16.
- Fakharan et al., *On \((1,2)\)-domination in cubic graphs*, Discrete Mathematics (2021), equality characterization cited in Radić, Radić and Tepeh (2026).
