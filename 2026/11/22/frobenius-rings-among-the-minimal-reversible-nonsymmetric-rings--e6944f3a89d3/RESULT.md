# Frobenius rings among the minimal reversible nonsymmetric rings of order 256

## Finding

Let \(\mathcal R\) be the set of isomorphism classes of unital reversible nonsymmetric rings \(R\) with \(|R|=256\). In the numbering of the complete 186-ring classification of Grau Ribas and Oller-Marcén, precisely the two rings numbered 7 and 20 are not Frobenius:

\[
\#\{R\in\mathcal R:R\text{ is Frobenius}\}=184,\qquad
\#\{R\in\mathcal R:R\text{ is not Frobenius}\}=2.
\]

Moreover, throughout this finite classification, the following two properties coincide: \(R\) is a Frobenius ring; \(R\) is a duo ring (every one-sided ideal is two-sided). Every one of the other 184 rings has coincident left and right socles equal to its last nonzero Jacobson-radical power, an ideal of order two. The two exceptions have two-dimensional terminal radical layers and socles of order at least four.

Here a finite ring is Frobenius when it admits a generating additive character, equivalently when its additive character module is isomorphic to its regular module; no commutativity or field-algebra hypothesis is imposed.

## Assumptions and scope

All rings are associative and unital. The words *reversible* and *symmetric* mean respectively \(ab=0\Rightarrow ba=0\) and \(abc=0\Rightarrow acb=0\). Set \(J=J(R)\) and \(J^{D}\ne0\), \(J^{D+1}=0\). The 2026 classification proves that all \(R\in\mathcal R\) are local, have residue field \(\mathbb F_2\), and belong to precisely three radical-Hilbert types:

| Radical-Hilbert vector including degree zero | Isomorphism classes | Frobenius | Not Frobenius |
|---|---:|---:|---:|
| \((1,2,3,2)\) | 2 | 0 | 2 |
| \((1,2,2,2,1)\) | 64 | 64 | 0 |
| \((1,3,3,1)\) | 120 | 120 | 0 |

The first row comprises ring 7 in characteristic two and ring 20 in characteristic four; they are also precisely the two nonduo classes of the cited classification. This result is a *classification within these 186 rings*, not a general equivalence between being duo and Frobenius.

## Proof

**1. A socle criterion independent of coefficient characteristic.** Let \(R\) be any finite local ring with \(R/J\cong\mathbb F_2\). Write \(\operatorname{Soc}_{\ell}(R)=\{r\in R:Jr=0\}\) and \(\operatorname{Soc}_{r}(R)=\{r\in R:rJ=0\}\). Such a ring is Frobenius exactly when its left socle has two elements. To see sufficiency, choose an additive character \(\chi:R\to\mathbb C^\times\) nontrivial on the order-two socle; an extension exists because characters extend from any subgroup of a finite abelian group. Every nonzero left ideal meets the socle, and a socle of order two is the unique nonzero simple left submodule. Hence the kernel of \(\chi\) contains no nonzero left ideal. The map \(r\mapsto(x\mapsto\chi(xr))\) injects the regular right module into the additive-character module, and is an isomorphism by equality of cardinalities. Conversely, when the left socle has at least four elements, its additive group is an \(\mathbb F_2\)-vector space of dimension at least two. Every additive character kills some nonzero socle element, and its one-dimensional span is a nonzero left ideal in the character kernel. Thus no generating character exists. For reversible rings, \(Jr=0\) is equivalent to \(rJ=0\), so both socles coincide.

**2. Filtered top-pairing criterion.** Put \(G=\operatorname{gr}_J(R)=\bigoplus_{i=0}^{D}J^i/J^{i+1}\), an \(\mathbb F_2\)-algebra even when \(R\) has characteristic four. Suppose \(\dim_{\mathbb F_2}G_D=1\) and each multiplication pairing

\[
G_i\times G_{D-i}\longrightarrow G_D,\qquad
(\bar a,\bar b)\longmapsto\overline{ab}
\]

is nondegenerate on both sides for \(1\le i<D\). If \(a\in J^i\setminus J^{i+1}\) with \(i<D\), a complementary positive-degree element \(b\in J^{D-i}\subseteq J\) has \(ab\ne0\), and a possibly different element has \(ba\ne0\). The case \(i=0\) follows because \(a\) is a unit and \(J^D\ne0\). Therefore neither left nor right socle has elements outside \(J^D\). Conversely \(J J^D=J^D J=0\), hence both socles are precisely \(J^D\), of order two. By part 1, \(R\) is Frobenius. Notice that this step applies unchanged to mixed-characteristic deformations.

**3. Exhaustive graded checks for the two one-dimensional-top types.** The appendix of the cited classification specifies all the needed graded presentations. In radical-Hilbert type \((1,2,2,2,1)\), its six characteristic-two rings and 58 characteristic-four rings have the same graded model \(G\) with generators \(x,y\) and homogeneous relations \(x^2+y^2\), \(x^2+xy+yx\), \(x^2y^2\), and every word of length five. The top-pairing matrix ranks in complementary degrees \((1,3),(2,2),(3,1)\) are exactly \((2,2,2)\). These ranks equal the dimensions of both source factors, so the pairings are perfect.

For radical-Hilbert type \((1,3,3,1)\), there are twelve characteristic-two graded presentations (numbers 8–19) and four characteristic-four graded models, called A, B, C and D in the source appendix (numbers 79–186). Exact reduction of the homogeneous two-sided defining ideals gives Hilbert vector \((1,3,3,1)\) for each of all sixteen models and the two complementary top-pairing ranks \((3,3)\). For the four characteristic-four models, the degree-one left pairing matrices, in the monomial quotient bases returned by the supplied checker, are:

\[
M_A=M_B=\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix},\quad
M_C=\begin{pmatrix}1&0&1\\0&1&0\\1&1&0\end{pmatrix},\quad
M_D=\begin{pmatrix}1&1&0\\1&0&0\\0&1&1\end{pmatrix}.
\]

Their determinants are all one over \(\mathbb F_2\); the complementary reversed-degree matrices also all have determinant one. The script `frobenius_socle_checker.py` records **all** seventeen graded models, computes the quotient and both pairing ranks by exact Gaussian elimination, and independently computes the left and right socle dimensions of all nineteen characteristic-two presentations. These are exhaustive calculations over the *finite list of graded types*, not extrapolation from sample rings. By step 2, all 64+120=184 rings of the two types are Frobenius and have socle \(J^D\) of order two.

**4. The two exceptions.** The classification gives radical-Hilbert vector \((1,2,3,2)\) for rings 7 and 20. Thus \(J^4=0\), while \(J^3\) has \(\mathbb F_2\)-dimension two and is contained in both socles. Their left socles have at least four elements; part 1 proves neither ring Frobenius. The same primary classification identifies precisely these two rings as nonduo; combining with the established Frobenius census proves the claimed equivalence within \(\mathcal R\).

## Verification

Run `python3 frobenius_socle_checker.py` using Python 3 and the standard library, from a directory containing the standalone embedded script. It prints `REVERSIBLE_256_SOCLE_CERTIFICATE_OK` only after all assertions. Its inputs are all 19 characteristic-two presentations and the 17 graded models: the common two-generator model, the four characteristic-four three-generator models, and the twelve characteristic-two three-generator models. For each it constructs the truncation of the free associative algebra, spans all admissible left-and-right translates of the listed relations, and reduces exact binary matrices. The actual run obtained 18 characteristic-two rings with left/right socle dimension one and only ring 7 with dimension two; the rank profile was \((2,2,2)\) for the common two-generator model and \((3,3)\) for each three-generator model. The full published classification supplies the coverage from these graded models to all 186 rings; the checker does not independently redo that classification.

## Relationship to prior work

Grau Ribas and Oller-Marcén (arXiv:2611.19962v1, first publicly posted 15 November 2026) proved the complete 186-class list, its characteristic/Hilbert distribution, and the duo/nonduo dichotomy, but did not formulate or calculate the Frobenius or generating-character status of its rings. The present result uses that list as input and determines a distinct invariant, with a uniform associated-graded explanation rather than 186 unrelated character computations. Szabo (arXiv:1710.07338, 2017) established minimal size 256 and constructed a nonduo example; this does not classify the Frobenius status of the 186 classes. Standard finite-ring Frobenius/socle criteria are known; the additional content here is their exhaustive new application to the newly classified 186 rings, certified by the nondegenerate top-degree pairings.

## Limitations

The result depends on the correctness and completeness of the 186-ring list published in arXiv:2611.19962v1; it does not re-establish that classification. It is not a general theorem that all finite duo rings are Frobenius, nor does it classify all reversible rings of larger orders. For the two exceptional rings only the lower bound of four for the socle order is asserted (the characteristic-two computation gives exact socle dimension two for ring 7). The mathematical proof and exact finite calculations were reviewed within the producing analysis; no independent external audit is claimed. Earlier unindexed equivalent counts cannot be excluded absolutely.

## References

1. J. M. Grau Ribas and A. M. Oller-Marcén, *All unital reversible nonsymmetric rings of order 256*, arXiv:2611.19962v1 (15 November 2026), https://arxiv.org/html/2611.19962v1, especially Theorem A and Appendix A.
2. S. Szabo, *Minimal Reversible Nonsymmetric Rings*, arXiv:1710.07338 (2017), https://arxiv.org/abs/1710.07338.
3. Standard characterization of finite Frobenius rings by generating additive characters and socle modules (used with a direct argument in Proof 1); https://en.wikipedia.org/wiki/Quasi-Frobenius_ring.
