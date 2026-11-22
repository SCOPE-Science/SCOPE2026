# Exact symmetry-defect witnesses and their radical layers in the binary quaternion group algebra

## Finding

Let \(Q_8=\langle i,j,z\mid z^2=1,\ z\text{ central},\ i^2=j^2=z,\ ji=zij\rangle\) and \(R=\mathbb F_2[Q_8]\), a ring of order \(256\). Define the *ordered symmetry-defect set*
\[
\mathcal W=\{(a,b,c)\in R^3:abc=0,\ acb\ne0\}.
\]
Then
\[
\boxed{|\mathcal W|=147456,\qquad \frac{|\mathcal W|}{|R|^3}=\frac9{1024}.}
\]
Let \(J\) be the augmentation radical and let \(v_J(x)=r\) for \(x\in J^r\setminus J^{r+1}\), with units assigned valuation zero and zero assigned valuation infinity. **Every** member of \(\mathcal W\) has one of the valuation vectors
\[
(1,1,2),\quad(1,2,1),\quad(2,1,1),
\]
and each vector occurs for exactly \(49152\) ordered triples. Thus the first failure of symmetry is quantitatively concentrated in exactly three, equally populated radical-layer configurations.

A finer, equivalent certificate is a complete joint multiplication-rank census. Put \(\rho_d:R\to R\), \(x\mapsto xd\), and for each ordered \((b,c)\) define
\[
r(b,c)=\operatorname{rank}_{\mathbb F_2}(\rho_{bc}),\qquad
s(b,c)=\operatorname{rank}_{\mathbb F_2}(\rho_{bc},\rho_{cb}).
\]
The complete list of \((r,s)\) and numbers of ordered pairs \((b,c)\) is:

| \((r,s)\) | Number of \((b,c)\) |
|---|---:|
| \((0,0)\) | 1664 |
| \((1,1)\) | 1408 |
| \((2,2)\) | 3072 |
| \((2,3)\) | 3072 |
| \((4,4)\) | 9216 |
| \((4,5)\) | 6144 |
| \((6,6)\) | 24576 |
| \((8,8)\) | 16384 |

No other rank pair occurs. These counts sum to \(65536=|R|^2\).

## Assumptions and scope

All products are associative ring products over \(\mathbb F_2\), not quaternion multiplication over the real numbers. The assertion concerns precisely the binary group ring \(\mathbb F_2[Q_8]\), with **ordered** pairs and triples and the specific implication \(abc=0\Rightarrow acb=0\). The known facts that this ring is reversible and nonsymmetric and has the least possible order among unital reversible nonsymmetric rings are not claimed as new.

## Proof

1. **Explicit multiplication.** Every element of \(Q_8\) has a unique normal form \(z^e i^u j^v\), with \(e,u,v\in\{0,1\}\). Label it by the integer \(e+2u+4v\). The defining relations give the exact multiplication law
   \[
   (e,u,v)(f,r,s)=(e+f+ur+vs+vr,\ u+r,\ v+s),
   \]
   with all coordinates reduced modulo two. Represent \(\sum_{g\in Q_8}\epsilon_g g\) by the eight-bit integer whose \(g\)-bit is \(\epsilon_g\). The product of any two elements is then obtained by bitwise exclusive-or of the products of their occupied group-basis positions. This constructs **every** entry of the \(256\)-by-\(256\) ring multiplication table from the group presentation, without relying on a published classification table.

2. **Radical filtration.** The augmentation kernel \(J\) consists of even-weight coefficient vectors. The code constructs linear bases of \(J,J^2,J^3,J^4,J^5\) by closure under multiplication; their dimensions are, respectively, \(7,5,3,1,0\). In particular \(J\) is nilpotent and \(R/J\cong\mathbb F_2\). Every vector outside \(J\) is a unit (it is \(1+j\), with \(j\in J\) nilpotent), so \(J\) is exactly the Jacobson radical. The computed filtration therefore gives intrinsic valuations, not merely auxiliary bit labels.

3. **Kernel identity.** For fixed \((b,c)\), write \(d=bc\) and \(e=cb\). The conditions \(abc=0\), \(acb\ne0\) say that \(a\) lies in \(\ker\rho_d\) but not in \(\ker\rho_d\cap\ker\rho_e\). Rank-nullity on the eight-dimensional vector space gives the exact number of such \(a\):
   \[
   2^{8-r(b,c)}-2^{8-s(b,c)}.
   \]
   This identity is valid independently of any enumeration.

4. **Exhaustive, bounded certificate.** `CHECKER.py` implements the eight-element group multiplication law, constructs the full ring table, and iterates over **all** \(256^2\) ordered pairs \((b,c)\). The eight images of the ring-basis vectors under each multiplication map yield the ranks by exact bit-vector Gaussian elimination. The resulting eight rank-pair frequencies are exactly the table displayed above. Only two pairs contribute nonzero terms to the kernel identity: \((r,s)=(2,3)\) contributes \(3072(2^6-2^5)=98304\), and \((r,s)=(4,5)\) contributes \(6144(2^4-2^3)=49152\). Summing gives \(147456\).

5. **Independent direct census of valuations.** A separate loop in the same file examines **all** \(256^3=16777216\) ordered triples and tests the two triple products directly from the ring table, without using rank-nullity. It obtains exactly the three valuation strata and their frequencies stated above. Agreement of the direct loop and the linear-kernel computation is a consistency check; both loops are complete finite enumerations, not extrapolations.

For a concrete witness, using the group-basis convention above, take \(a=1+i\), \(b=1+j\), and \(c=z+i+j+ij\). The computed values are \(abc=0\) and \(acb=\sum_{g\in Q_8}g\ne0\). The witness has radical valuations \((1,1,2)\).

## Verification

Run `python3 CHECKER.py` with Python 3.10 or later. No third-party libraries, downloaded data, hidden parameters, random trials, or external certificates are required. The program terminates after finite loops over \(8^3\) group triples, \(256^2\) ring pairs and \(256^3\) ring triples, using exact integer and bit operations. It asserts the radical dimensions, the complete rank-pair distribution, the two nonzero rank contributions, the full valuation census and the probability identity. The verified output begins `QUATERNION_SYMMETRY_DEFECT_OK`.

## Relationship to prior work

Grau Ribas and Oller-Marcén, arXiv:2611.19962v1, first publicly submitted on 2026-11-15, classify all \(186\) unital reversible nonsymmetric rings of order \(256\), including \(\mathbb F_2[Q_8]\), and verify the qualitative properties of their presentations. Sections 1, 7 and 8 and the presentation tables contain neither the present exact ordered-witness count nor the joint two-product rank spectrum or three-stratum valuation statement. Earlier work of Marks and Szabo establishes nonsymmetry and minimality, and Szabo’s Example 4.2 already describes the radical-power generators, but not this quantitative census. Separately reported single-element multiplication-rank distributions of quaternion group algebras do not determine the joint rank correlations of \(bc\) and \(cb\) from which this count follows. Consequently the claim is specifically the quantified and layer-refined defect in a canonical smallest example, not minimality or ring classification.

## Limitations

This is an exact finite computation with a complete executable certificate, not a closed-form theorem over every finite coefficient field or a census of all \(186\) minimal rings. The novelty assessment relies on inspected primary classification and historical full-text preprint, older available excerpts, and searches for equivalent statements; a numerical census buried in unindexed historical material cannot be ruled out. The count is appropriate as a benchmark for future comparisons of qualitative and quantitative nonsymmetry among minimal rings, but no classification by this statistic is claimed.

## References

1. J. M. Grau Ribas and A. M. Oller-Marcén, *All unital reversible nonsymmetric rings of order 256*, arXiv:2611.19962v1 (publicly submitted 2026-11-15), https://arxiv.org/html/2611.19962v1 .
2. S. Szabo, *Minimal reversible nonsymmetric rings*, Journal of Pure and Applied Algebra **223** (2019), 4583–4591, https://doi.org/10.1016/j.jpaa.2019.02.005 ; public preprint https://arxiv.org/abs/1710.07338 .
3. G. Marks, *Reversible and symmetric rings*, Journal of Pure and Applied Algebra **174** (2002), 311–318.
