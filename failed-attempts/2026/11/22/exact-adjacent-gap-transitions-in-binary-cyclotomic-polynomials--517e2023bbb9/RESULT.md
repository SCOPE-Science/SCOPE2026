# Exact adjacent-gap transitions in binary cyclotomic polynomials of order five times a prime

## Finding

For each integer \(q>5\) with \(\gcd(q,5)=1\), consider the two-generator semigroup polynomial
\[
F_q(X)=\frac{(1-X)(1-X^{5q})}{(1-X^5)(1-X^q)}.
\]
When \(q\) is prime, this is exactly the binary cyclotomic polynomial \(\Phi_{5q}\). Arrange its nonzero coefficient exponents in increasing order, \(e_0<e_1<\cdots<e_s\), and define the gaps \(g_i=e_{i+1}-e_i\). The *ordered adjacent-gap count* is
\[
C_{a,b}(q)=\#\{i:0\le i<s-1,\ (g_i,g_{i+1})=(a,b)\}.
\]
Write \(q=5h+r\), with \(h\ge1\) and \(1\le r\le4\). The following is a complete, exact classification: every pair not listed has count zero.

| \(r\) | Ordered pairs \((a,b)\) | Multiplicity of each pair |
|---|---|---|
| 1 | \((1,4),(4,1),(2,3),(3,2)\) | \(2h-1\) |
| 1 | \((2,4),(4,2),(3,3)\) | \(1\) |
| 2 | \((1,1)\) | \(4h+3\) |
| 2 | \((1,2),(2,1),(1,4),(4,1)\) | \(2h\) |
| 3 | \((1,1)\) | \(4h+1\) |
| 3 | \((1,2),(2,1)\) | \(2h+2\) |
| 3 | \((1,4),(4,1)\) | \(2h\) |
| 4 | \((1,3),(3,1),(2,2)\) | \(1\) |
| 4 | \((1,4),(4,1)\) | \(2h\) |
| 4 | \((2,3),(3,2)\) | \(2h+1\) |

The result gives more than the frequency of each individual gap. For example, when \(r\in\{2,3\}\), every gap of length \(2\) or \(4\) has only gaps of length \(1\) as neighbors, a transition rigidity that marginal gap counts alone cannot establish. The two-gap transition matrices are symmetric, consistently with coefficient reciprocity.

## Assumptions and scope

The integer \(q\) need not be prime for the semigroup-polynomial version. For the cyclotomic interpretation, \(q>5\) must be prime. We count *linear* adjacent pairs \((g_i,g_{i+1})\); there is no cyclic wraparound from the final gap to the first. The coefficient support is on the inclusive interval from \(0\) through degree \(D=4(q-1)\). Every formula holds for all \(h\ge1\), including \(q=6,7,8,9\) as the four semigroup base cases.

## Proof

**1. Transition representation.** Let \(S=\langle 5,q\rangle\), and set \(B(n)=\mathbf1_{n\in S}\) for nonnegative \(n\), with \(B(-1)=0\). Every \(n<5q\) has at most one representation \(n=5a+qb\) in nonnegative integers: two such representations would force a difference in \(b\) divisible by five, but \(0\le b\le4\). Since \(D=4(q-1)<5q\), the rational identity defining \(F_q\) yields exactly
\[
[X^n]F_q=B(n)-B(n-1),\qquad 0\le n\le D.
\]
Thus a nonzero coefficient is precisely a boundary between represented and unrepresented integers.

**2. Four periodic stages.** Fix \(r=q\bmod5\). If \(jq\le n<(j+1)q\) for \(j=0,1,2,3\), then
\[
B(n)=\mathbf1_{n\bmod5\in R_j},\qquad R_j=\{0,r,2r,\ldots,jr\}\bmod5.
\]
Indeed a representation needs some \(b\le j\), and then exists exactly if \(n\equiv bq\pmod5\). Away from the three stage junctions, the support of the transition word \(B(n)-B(n-1)\) is therefore five-periodic; its active residues are those at which the indicator of \(R_j\) changes relative to its predecessor modulo five. The periodic *cyclic gap sequences*, in the order \(j=0,1,2,3\), are

| \(r\) | \(j=0\) | \(j=1\) | \(j=2\) | \(j=3\) |
|---|---|---|---|---|
| 1 | \((1,4)\) | \((2,3)\) | \((3,2)\) | \((4,1)\) |
| 2 | \((1,4)\) | \((1,1,1,2)\) | \((1,1,1,2)\) | \((1,4)\) |
| 3 | \((1,4)\) | \((1,2,1,1)\) | \((2,1,1,1)\) | \((1,4)\) |
| 4 | \((1,4)\) | \((3,2)\) | \((2,3)\) | \((1,4)\) |

The entries are obtained by testing only the five residues \(0,1,2,3,4\) for the sets \(R_j\). The stage-junction symbols use the preceding stage on their left; these boundary conditions depend only on \(r\), not on \(h\).

**3. The five-step insertion lemma.** Replace \(q\) by \(q+5\), keeping \(r\) fixed. The beginning of stage \(j\) shifts by \(5j\) positions and its ending by \(5(j+1)\). Consequently each of the four stages gains precisely one full period of its five-periodic transition word. Its start/end residues and its splice to neighboring stages are unchanged. Inserting a complete periodic block adds precisely the ordered adjacent-gap pairs in one cyclic pass through that block's gap sequence; pairs touching the unchanged splices cancel on comparison. The same conclusion follows directly by checking the five residue positions on each side of a junction. The four added cycles from the displayed table therefore contribute
\[
\begin{array}{ll}
r=1\text{ or }4:&\Delta C_{1,4}=\Delta C_{4,1}=\Delta C_{2,3}=\Delta C_{3,2}=2,\\
r=2\text{ or }3:&\Delta C_{1,1}=4,\quad\Delta C_{1,2}=\Delta C_{2,1}=\Delta C_{1,4}=\Delta C_{4,1}=2,
\end{array}
\]
with all other increments zero. Here \(\Delta C_{a,b}=C_{a,b}(q+5)-C_{a,b}(q)\). The linear endpoints contribute no extra term because their fixed four-term neighborhoods are unchanged under the insertion.

**4. Four base cases and induction.** Directly list the support of the transition word for \(q=6,7,8,9\) using Step 1. The ordered adjacent-gap counts are:

| Base \(q\) | Pair counts, omitting zeros |
|---|---|
| 6 | \((1,4),(4,1),(2,3),(3,2),(2,4),(4,2),(3,3)\): one each |
| 7 | \((1,1)\): seven; \((1,2),(2,1),(1,4),(4,1)\): two each |
| 8 | \((1,1)\): five; \((1,2),(2,1)\): four each; \((1,4),(4,1)\): two each |
| 9 | \((1,3),(3,1),(2,2)\): one each; \((1,4),(4,1)\): two each; \((2,3),(3,2)\): three each |

Adding the corresponding increment from Step 3 exactly \(h-1\) times proves the ten formula rows, including the assertion that no other pair can occur.

## Verification

The included `verification/verify.py` uses integer semigroup representation to recompute all adjacent-gap counts independently for every \(6\le q\le500\) coprime to five (396 cases). It also checks the four cyclic insertion increments directly, then independently constructs \(22\) prime cyclotomic polynomials \(\Phi_{5q}\) symbolically and compares all coefficient vectors. All checks passed. Finite checks are corroboration; the induction above proves the unbounded statement.

Run with `python verification/verify.py` using Python 3 and SymPy.

## Relationship to prior work

Cafure and Cesaratto, *Gaps in binary cyclotomic polynomials* (arXiv:2507.19381, first public July 25, 2025), determine the second-largest gap and individual-gap multiplicities for \(q\equiv\pm1\pmod p\). Their theorem does not state consecutive-*pair* gap transitions, including the \(q\equiv\pm2\pmod5\) cases. Their earlier 2021 article (arXiv:2109.07544) supplies a general coefficient-word construction for every binary cyclotomic polynomial. The present result derives a uniform closed ordered two-gap law rather than an algorithm for reconstructing coefficients. Camburu, Ciolan, Luca, Moree and Shparlinski (2016) determine the largest gap and existence of specified gap lengths, but not their ordered adjacency matrix. The published universal first-order gap-frequency formula for odd squarefree conductors includes the individual-gap marginals at conductor five, but does not determine how those gaps are ordered. The formula above refines these marginal statements without claiming their known consequences as new.

## Limitations

This theorem is confined to conductor five (and coprime two-generator semigroup polynomials); it does not classify adjacent gaps for arbitrary first prime or triples of consecutive gaps. An abstract coefficient-word representation can reconstruct the pair counts at each fixed input, but does not itself state the parameter-uniform transition formulas; implicit or unindexed coverage by earlier work remains possible. The proof is mathematical and the included computation is a check, not independent certification.

## References

1. A. Cafure and E. Cesaratto, *Gaps in binary cyclotomic polynomials*, arXiv:2507.19381 (first public July 25, 2025), https://arxiv.org/abs/2507.19381.
2. A. Cafure and E. Cesaratto, *Binary Cyclotomic Polynomials: Representation via Words and Algorithms*, arXiv:2109.07544 (2021), https://arxiv.org/abs/2109.07544.
3. O.-M. Camburu, E.-A. Ciolan, F. Luca, P. Moree and I. E. Shparlinski, *Cyclotomic coefficients: gaps and jumps*, Journal of Number Theory 163 (2016), 211–237, https://doi.org/10.1016/j.jnt.2015.11.020.
