# Complete anticanonical linear-section spectrum of a quartic del Pezzo surface over \(\mathbb F_5\)

## Finding

Let \(X\subset\mathbb P^4_{\mathbb F_5}\) be the smooth complete intersection of the quadrics
\[
\begin{aligned}
Q_3&=x_1^2+2x_0x_2+2x_3^2+4x_2x_4+2x_3x_4+x_4^2,\\
Q_4&=2x_1x_2+x_2^2+2x_0x_3+2x_1x_3+2x_2x_3+x_3^2\\
&\qquad+2x_0x_4+2x_1x_4+2x_2x_4+x_3x_4+4x_4^2.
\end{aligned}
\]
The equations are the explicit type-\(4_3\) example in Blache--Couvreur--Hallouin--Madore--Nardi--Rambaud--Randriam [1]. There are precisely 31 rational points. For each integer \(1\le k\le4\) and nonnegative integer \(s\), define
\[
H_k(s)=\#\{L\subset\mathbb P^4(\mathbb F_5):L\text{ is rational linear of codimension }k,\ \#(L\cap X(\mathbb F_5))=s\}.
\]
The following table gives **every** nonzero entry, with all omitted entries zero.

| Codimension | Values of \(s\) | Corresponding \(H_k(s)\) |
| --- | --- | --- |
| \(k=1\) | \(0,2,3,4,5,6,7,8,9,10\) | \(1,46,62,63,122,126,124,108,82,47\) |
| \(k=2\) | \(0,1,2,3,4\) | \(5880,7081,4770,1935,640\) |
| \(k=3\) | \(0,1,2\) | \(15935,3906,465\) |
| \(k=4\) | \(0,1\) | \(750,31\) |

In particular, there are **640 rational projective planes** through four distinct rational points of this surface, and no rational projective plane contains five rational points. The anticanonical evaluation code \(C\), which was previously known to have parameters \([31,5,21]_5\), has generalized Hamming weights
\[
(d_1,d_2,d_3,d_4,d_5)=(21,27,29,30,31).
\]
Its ordinary Hamming weight enumerator is
\[
\begin{aligned}
W_C(z)={}&1+188z^{21}+328z^{22}+432z^{23}+496z^{24}+504z^{25}\\
&+488z^{26}+252z^{27}+248z^{28}+184z^{29}+4z^{31}.
\end{aligned}
\]

## Assumptions and scope

All statements concern the **single explicit** surface defined by the displayed equations over \(\mathbb F_5\), not every quartic del Pezzo surface or every representative of its Frobenius type. Every \(L\) is an \(\mathbb F_5\)-defined *projective linear subspace*, and the intersection count records distinct \(\mathbb F_5\)-rational points, not geometric multiplicity or a scheme length. The code evaluates all linear forms on these 31 points with arbitrary nonzero homogeneous representatives; its support data are unchanged by column scaling.

## Proof

**Smoothness and the point set.** Write \(A\) and \(B\) for the symmetric coefficient matrices of \(2Q_3\) and \(2Q_4\). Exact polynomial determinant arithmetic modulo five gives the coefficients \((3,3,3,3,2,3)\), in ascending powers of \(t\), for \(\det(tA+B)\). The derivative is coprime to this degree-five polynomial. The standard squarefree-pencil criterion for intersections of two quadrics in odd characteristic proves that \(X\) is smooth. Enumerating the 781 normalized homogeneous representatives of \(\mathbb P^4(\mathbb F_5)\) gives exactly 31 simultaneous zeros of \(Q_3,Q_4\). An independent reconstruction from the five rows of the published \(5\times31\) generator matrix yields precisely the same projective point set.

**Exhaustive sections.** A codimension-\(k\) rational linear space is uniquely the common zero locus of the rows of a rank-\(k\) reduced-row-echelon matrix in five variables over \(\mathbb F_5\). The program `verify_sections.py` enumerates every pivot set and every allowable free entry, exactly once, and tests each of the 31 points. For \(k=1,2,3,4\), the numbers of distinct matrices checked are respectively \(781,20306,20306,781\). The resulting four histograms are exactly those stated above. In particular, \(x_0+2x_4=x_1=0\) contains four points of \(X(\mathbb F_5)\); the unique point-free rational hyperplane has equation \(x_0+x_1+3x_2+4x_3+3x_4=0\).

**Independent incidence certificate for the four-point maximum.** The second program `verify_incidence.py` uses only the printed generator matrix from [1], with an unrelated rank-elimination algorithm. It checks that every triple among the 31 columns is linearly independent, then inspects all \(\binom{31}{4}=31465\) unordered quadruples. Exactly 640 have rank three. Since three points are never collinear, such a quadruple determines a unique rational projective plane. Since the first exhaustive census shows that no plane has more than four surface points, 640 is also the exact number of four-point planes. Conversely, the elementary plane-incidence moments reproduce the entire codimension-two histogram: the total number of planes is 20306, the number through any point is 806, through any pair is 31, and every triple spans a unique plane. For codimension three, every pair spans a unique line and no three surface points are collinear, yielding the stated \((15935,3906,465)\) histogram. Codimension four is immediate from distinctness of the 31 points.

**Code interpretation.** A \(k\)-dimensional space of linear-form codewords has zero set exactly \(X(\mathbb F_5)\cap L\), where \(L\) is the common zero locus of its \(k\) independent forms. Thus its support size is \(31-\#(L\cap X(\mathbb F_5))\). Since the evaluation map has rank five, maximizing the relevant count gives the displayed generalized weights. Each rational hyperplane corresponds to four nonzero scalar multiples of one codeword, proving the ordinary weight enumerator formula.

## Verification

Run `python3 verify_sections.py` and `python3 verify_incidence.py` using Python 3 (standard library only). The first verifies the smooth-pencil discriminant, all rational points, every rational linear subspace of codimension one through four, and the weight enumerator. The second transcribes the independent published generator matrix, confirms all 4495 triples are independent and counts the 640 coplanar quadruples, then derives the plane and line histograms by finite incidence moments. Both programs fail with a nonzero exit status if an asserted result changes. These are finite exhaustive certificates for the stated single-field claim, not proofs of uniform results over other fields.

## Relationship to prior work

Blache et al. [1, Section 6 and final example] construct precisely this smooth Frobenius-type-\(4_3\) quartic del Pezzo model, print its generator matrix, and give the code parameters \([31,5,21]_5\). They do not state the displayed full linear-section profiles, the 640 four-point plane count or the remaining four generalized weights. Little and Schenck [2, Section 5.1] study another Picard-rank-small quartic surface over \(\mathbb F_7\) and its minimum-distance code parameters. Boguslavskii [3] computes generalized weights for **split** del Pezzo surfaces; this model is nonsplit of arithmetic Picard rank one. A later general theorem on codes from reduced zero-dimensional complete intersections [4] concerns a different hypothesis and does not furnish this surface's exact section histogram. The new statement is an exact arithmetic refinement of a *published example*, not a new construction or a general del Pezzo code theorem.

## Limitations

The answer is confined to the displayed model over \(\mathbb F_5\); it is not asserted for other surfaces of the same Frobenius type, for extensions, or for other characteristics. The counts do not classify the geometric singularity types of the hyperplane sections, nor do they assert new bounds for all quartic del Pezzo codes. The exact spectral data can be independently recomputed but are not independently audited, and an older unindexed code-table calculation remains a possible priority risk.

## References

[1] R. Blache, A. Couvreur, E. Hallouin, D. Madore, J. Nardi, M. Rambaud and H. Randriam, *Anticanonical codes from del Pezzo surfaces with Picard rank one*, arXiv:1903.09397v1 (first public version 22 March 2019), Section 6, https://arxiv.org/pdf/1903.09397.

[2] J. Little and H. Schenck, *Codes from Surfaces with Small Picard Number*, SIAM J. Applied Algebra and Geometry 2 (2018), 242--258, Section 5.1, https://mathcs.holycross.edu/~little/PicCodesFinalSIAGA.pdf.

[3] M. I. Boguslavskii, *Sections of the Del Pezzo Surfaces and Generalized Weights*, Problems of Information Transmission 34 (1998), 14--24, https://www.mathnet.ru/eng/ppi392.

[4] E. Camps Moreno, F. Salizzoni and R. San-José, *Generalized Hamming weights of codes arising from complete intersection*, arXiv:2608.19978 (2026), https://arxiv.org/abs/2608.19978.
