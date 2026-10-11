# The Gray image in Example 1 has dimension seven, not five
## Finding

In Example 1 of Hesari–Sari–Aydogdu, let
\[
C=\langle (k(x),0),(l(x),g(x))\rangle
\subseteq \mathbb F_2^7\times\mathbb F_4^4,
\]
where
\[
k(x)=1+x^2+x^3+x^4,\qquad
l(x)=1+x+x^3,
\]
and
\[
g(x)=\omega^2+\omega^2x+x^2,
\qquad \omega^2=\omega+1.
\]

The article reports that the binary Gray image is a \([15,5,4]_2\) code. For the displayed code, the correct parameters are
\[
[15,7,4]_2.
\]
Its exact Hamming weight enumerator is
\[
W_{\Psi(C)}(z)
=
1+12z^4+30z^6+63z^8+18z^{10}+4z^{12}.
\]

The standard binary code table has optimal minimum distance \(5\) for length \(15\) and dimension \(7\). Therefore this corrected Gray image, whose minimum distance is \(4\), is not distance-optimal.

## Assumptions and scope

The calculation uses exactly the mixed-alphabet module action, Gray map, polynomials, and generator matrix printed in the article.

Elements of \(\mathbb F_4\) are written as \(p+\omega q\), with \(p,q\in\mathbb F_2\), and the source Gray map is
\[
\Psi(a_0,\ldots,a_6,p_0+\omega q_0,\ldots,p_3+\omega q_3)
=
(a_0,\ldots,a_6,q_0,\ldots,q_3,p_0+q_0,\ldots,p_3+q_3).
\]
The source states that this map is binary linear and isometric.

No claim is made here about the other examples in the article.

## Proof

The article's Theorem 4 states that for
\[
C=\langle(k(x),0),(l(x),g(x))\rangle
\subseteq \mathbb F_2^r\times\mathbb F_4^s,
\]
the cardinality is
\[
|C|
=
2^{r-\deg k}\,4^{s-\deg g}.
\]
For Example 1,
\[
r=7,\qquad s=4,\qquad \deg k=4,\qquad \deg g=2,
\]
so
\[
|C|
=
2^{7-4}4^{4-2}
=
2^3\cdot 4^2
=
128
=
2^7.
\]

The Gray map is injective and binary linear. Hence
\[
|\Psi(C)|=|C|=128,
\]
and therefore
\[
\dim_{\mathbb F_2}\Psi(C)=7.
\]
Thus the reported dimension \(5\) cannot be correct.

For a direct reconstruction, start from the five mixed-alphabet rows printed in Example 1. The first three rows have zero \(\mathbb F_4\) part, so each contributes one binary generator. Each of the last two rows contributes two binary generators, obtained by multiplying it by \(1\) and by \(\omega\) before applying \(\Psi\). This gives a binary \(7\times15\) generator matrix of rank \(7\).

Enumerating its \(2^7=128\) codewords gives the weight distribution
\[
A_0=1,\quad
A_4=12,\quad
A_6=30,\quad
A_8=63,\quad
A_{10}=18,\quad
A_{12}=4,
\]
and no other nonzero coefficients. Hence the minimum distance is exactly
\[
d=4.
\]

## Verification

`artifacts/verify.py` uses only the Python standard library. It reconstructs \(\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1)\), the source module multiplication, all five displayed mixed-alphabet generator rows, and the source Gray map.

It independently checks the exact mixed-code cardinality \(128\), injectivity of the Gray image on the reconstructed code, rank \(7\) of the explicit binary Gray generator, all \(128\) binary codewords, minimum distance \(4\), and the complete weight distribution
\[
1+12z^4+30z^6+63z^8+18z^{10}+4z^{12}.
\]
Successful replay prints `VERIFY_OK`.

## Relationship to prior work

The primary article itself supplies both ingredients that force the corrected dimension. Its Theorem 4 gives
\[
|C|=2^{r-\deg k}4^{s-\deg g},
\]
while its preliminary section states that the Gray map is binary linear. Substituting the parameters of Example 1 gives \(128\) codewords, so the same article's later statement \([15,5,4]_2\) is internally inconsistent with its general cardinality theorem.

Focused searches using the article title, DOI, Example 1, the exact polynomials, the reported parameters, the corrected parameters, the number \(128\), and the full weight-enumerator coefficients did not locate a published correction or a prior statement of this exact correction.

Grassl's binary code table records lower and upper bound \(5\) for \([15,7]\) binary linear codes, with an explicit \([15,7,5]_2\) construction. Thus the corrected \([15,7,4]_2\) image is not optimal.

The earlier paper on \(\mathbb F_2\mathbb F_4\)-additive cyclic codes is relevant background for the mixed alphabet and Gray images, but the publicly inspected material did not identify this later skew-cyclic Example 1 or state the present correction.

## Limitations

The result corrects only Example 1 as printed. It does not establish whether the dimension error arose from a typographical mistake, an omitted restriction, or a computational convention not stated in the article.

The exact weight enumerator is for the Gray image reconstructed from the displayed generator and the article's stated module action and Gray map. No assertion is made about a different code that the authors may have intended.

Searches cannot prove absence from all unpublished or non-indexed sources. The originality assessment is limited to the inspected public literature and research-record searches.

## References

1. Roghayeh Mohammadi Hesari, Mustafa Sari, and Ismail Aydogdu, *\(\mathbb F_2\mathbb F_4\)-skew cyclic codes*, Computational and Applied Mathematics 44 (2025), article 264, DOI 10.1007/s40314-025-03226-7.
2. Markus Grassl, *Bounds on the minimum distance of linear codes*, binary \([15,7]\) table entry.
3. T. Abualrub, N. Aydin, and I. Aydogdu, *Optimal binary codes derived from \(\mathbb F_2\mathbb F_4\)-additive cyclic codes*, Journal of Applied Mathematics and Computing 64 (2020), 71–87.
