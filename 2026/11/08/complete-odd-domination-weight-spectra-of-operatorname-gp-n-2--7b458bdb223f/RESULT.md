# Complete odd-domination weight spectra of \(\operatorname{GP}(n,2)\)

## Finding
For every integer \(n\ge5\), let \(W_n(z)=\sum_{S}z^{|S|}\), where the sum ranges over all subsets \(S\) of vertices of the generalized Petersen graph \(\operatorname{GP}(n,2)\) such that every closed neighborhood meets \(S\) in an odd number of vertices. Then
\[
W_n(z)=\begin{cases}
2z^n,&5\nmid n,\ n\text{ odd},\\
4z^n,&5\nmid n,\ n\text{ even},\\
10z^{3n/5}+12z^n+10z^{7n/5},&5\mid n,\ n\text{ odd},\\
10z^{3n/5}+44z^n+10z^{7n/5},&10\mid n.
\end{cases}
\]
Consequently, the odd domination number is \(3n/5\) if \(5\mid n\), and \(n\) otherwise. When \(5\mid n\), exactly ten minimum odd dominating sets exist. For other \(n\), the number of minimum sets is two for odd \(n\) and four for even \(n\). For context, the dimensions of the associated affine solution spaces over \(\mathbb F_2\) are \(1,2,5,6\), matching the already-studied homogeneous-kernel nullity regimes; these dimensions and the number of solutions are not asserted as new.

## Assumptions and scope
The graph is simple and has vertex set \(\{u_i,v_i:i\in\mathbb Z/n\mathbb Z\}\). Its edges are \(u_i u_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\), with indices modulo \(n\); \(n\ge5\) prevents degeneracies in this definition. Every selected vertex contributes one to the incidence count in its own closed neighborhood and to those of its neighbors. An odd dominating set is precisely a binary solution to \((I+A)\mathbf s=\mathbf1\) over \(\mathbb F_2\). The enumerator counts *labelled subsets*, not rotational equivalence classes.

## Proof
Write \(x_i\in\mathbb F_2\) and \(y_i\in\mathbb F_2\) for membership of \(u_i\) and \(v_i\), respectively. All indices are interpreted cyclically. The parity conditions are
\[
x_{i-1}+x_i+x_{i+1}+y_i=1,\qquad y_{i-2}+y_i+y_{i+2}+x_i=1.
\]
Eliminating \(y_i=1+x_{i-1}+x_i+x_{i+1}\) in the inner equation gives
\[
x_{i-3}+x_{i-2}+x_{i+2}+x_{i+3}=0,
\]
which, on replacing the index by \(j=i-3\), is equivalent to
\[
x_j+x_{j+1}+x_{j+5}+x_{j+6}=0.
\]
Set \(a_j=x_j+x_{j+1}\). Thus \(a_{j+5}=a_j\). Define \(t=a_0+a_1+a_2+a_3+a_4\) in \(\mathbb F_2\). For every index, summing five consecutive differences yields \(x_{j+5}=x_j+t\); hence \(x_{j+10}=x_j\). Conversely any such cyclic binary sequence \(x\), with \(y\) defined as above, satisfies both neighborhood conditions. This is a bijection between solutions and admissible \(x\)-sequences.

If \(5\nmid n\), the sequence \(a\) has periods both five and \(n\), so is constant. For odd \(n\), a nonzero constant difference is incompatible with cyclicity, leaving two constant \(x\)'s. For even \(n\), both constant and alternating \(x\)'s are allowed, giving four. In every one of these cases, either \(y\) is the complement of \(x\) or one of \(x,y\) is constantly zero while the other is constantly one, so the set has size \(n\).

If \(5\mid n\) and \(n\) is odd, the identity \(x_{j+5}=x_j+t\), iterated \(n/5\) times, forces \(t=0\). Hence \(x\) is any five-periodic binary pattern, yielding \(32\) solutions. If \(10\mid n\), any initial five-bit block and either value of \(t\) determine a valid periodic \(x\), yielding \(64\) solutions. The \(32\) cases with \(t=0\) repeat a five-bit pattern; the \(32\) with \(t=1\) satisfy \(x_{j+5}=1+x_j\) and \(y_{j+5}=1+y_j\), so their total selected size is exactly \(n\).

It remains to count sizes among the \(32\) five-periodic patterns. In one period there are five outer and five inner positions. The empty and full outer patterns (two patterns), five adjacent pairs and five complementary consecutive triples (ten patterns) all have selected size five. The five singleton patterns and five pairs with nonadjacent positions (ten patterns) all have selected size three. Their ten complements have selected size seven; complementation flips both \(x\) and \(y\) and changes total size \(w\) to \(10-w\). These are all \(32\) patterns, with weight multiset \(3^{10},5^{12},7^{10}\). Repeating each period \(n/5\) times multiplies the size by \(n/5\). For \(10\mid n\), the additional thirty-two twisted patterns have size \(n\). Collecting terms proves the four formulas and their minimum-set corollaries for every \(n\ge5\).

## Verification
The independent programs `verify_odd_matrix.py` and `verify_odd_periodic.py` are complete standalone Python 3 scripts. The former builds the actual closed-neighborhood system on all \(2n\) vertices, performs exact binary Gauss–Jordan elimination, enumerates every free-variable assignment and checks every recovered vector against the original equations; it verifies every \(5\le n\le60\). The latter enumerates ten-step binary patterns satisfying the *derived* recurrence, enforces the cyclic boundary, reconstructs the inner ring, and checks the parity conditions; it verifies every \(5\le n\le100\), including the exhaustive count of 64 valid ten-periodic patterns. Both compare the entire cardinality histogram to the formula. Their success markers are `DIRECT_GF2_MATRIX_PASS_n5_to60` and `PERIODIC_RECURRENCE_PASS_n5_to100`. These finite checks support but do not replace the universal proof above.

## Relationship to prior work
The closed-neighborhood homogeneous kernel of the same generalized Petersen family has previously been studied, including exact nullities and weight enumerators. That is the solution set of \((I+A)\mathbf s=\mathbf0\), while the present polynomial enumerates the *distinct inhomogeneous affine coset* \((I+A)\mathbf s=\mathbf1\). An ordinary kernel weight enumerator does not determine the weight enumerator of a specified nonzero-syndrome coset. Torrence and Torrence (2016) studied the same generalized Petersen graphs as Lights Out systems and tabulated homogeneous nullities, without giving the full all-on-game minimal-press or weight spectrum. Caro, Klostermeyer and Goldwasser (2001) established the odd-domination framework and results for powers of cycles, their complements, grids and other classes. Caro and Klostermeyer (2003) developed further bounds and extremal constructions; neither paper supplies the specific full labelled weight enumerator of \(\operatorname{GP}(n,2)\). Hatzl and Wagner (2007) studied general parity constraints and a general bounded-treewidth procedure, not this particular closed form. The classification of perfect and total perfect codes in generalized Petersen graphs by Wang and Zhang (2026) concerns *exactly one* selected vertex in each relevant neighborhood rather than odd cardinality; in fact their perfect-code criterion excludes \(\operatorname{GP}(n,2)\), whereas odd dominating sets always exist. A more recent report obtains the numerical value \(3n/5\) for a *dominating induced matching* invariant in a related family; that counts edges in an induced matching, not odd dominating vertex sets. The mathematical invariant and the all-size solution enumerator here are different. No claim is made to novelty of the homogeneous kernel dimension, homogeneous weight enumerator, or general existence of odd dominating sets.

## Limitations
The theorem applies only to \(\operatorname{GP}(n,2)\) for integer \(n\ge5\), not arbitrary \(\operatorname{GP}(n,k)\) or other cubic graphs. Its originality has not undergone independent scholarly verification. A 2001 foundation paper has a verified publication year but no independently established exact first-publication *day* in the inspected records; February 28, 2003 is the earliest complete calendar date independently verified for a primary public odd-domination source. A related induced-matching publication was only accessible via a search-exposed statement, not full text; it concerns a different invariant. Undiscovered equivalent prior derivations cannot be ruled out.

## References
1. Y. Caro, W. F. Klostermeyer and J. L. Goldwasser, “Odd and residue domination numbers of a graph,” *Discussiones Mathematicae Graph Theory* **21** (2001), 119–136, DOI: 10.7151/dmgt.1137.
2. Y. Caro and W. F. Klostermeyer, “The Odd Domination Number of a Graph,” *Journal of Combinatorial Mathematics and Combinatorial Computing* **44** (2003), 65–83; published February 28, 2003. https://combinatorialpress.com/jcmcc-articles/volume-044/the-odd-domination-number-of-a-graph/
3. J. Hatzl and S. Wagner, “Combinatorial properties of a general domination problem with parity constraints,” preprint dated March 23, 2007. https://math.sun.ac.za/swagner/genparity.pdf
4. X. Wang and J. Zhang, “Classification of perfect and total perfect codes in generalized Petersen graphs,” arXiv:2603.20722 (March 21, 2026). https://arxiv.org/html/2603.20722v1
5. B. Torrence and R. Torrence, “An iterative strategy for Lights Out on Petersen graphs,” *Involve* **9** (2016), 721–732, DOI: 10.2140/involve.2016.9.721.
6. “Dominating induced matchings and other graph parameters,” DOI: 10.1080/09728600.2024.2342310 (2024; only a search-visible statement was inspected).
