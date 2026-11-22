# Three-extension recovery of cubic-surface Frobenius from lines and tritangent planes

## Finding

Let \(X/\mathbb F_q\) be a smooth cubic surface, in any characteristic. Let \(L_n\) be the number of geometric lines on \(X\) defined over \(\mathbb F_{q^n}\), and let \(T_n\) be the number of geometric tritangent planes defined over \(\mathbb F_{q^n}\). Here a tritangent plane is defined over the field when its *unordered triple of lines* is Frobenius stable: the three individual lines need not descend.

**Theorem.** The six counts
\[
(L_1,T_1,L_2,T_2,L_3,T_3)
\]
uniquely determine the conjugacy class of Frobenius in \(W(E_6)\). They therefore determine the complete zeta functions of the reduced finite étale schemes of lines and tritangent planes, and the conjugacy class of Frobenius on the geometric Picard lattice. For the \(25\) conjugacy classes there are exactly \(20\) line-only cycle spectra, \(24\) tritangent-only cycle spectra, and \(25\) combined spectra. The number of distinct joint profiles through extension degrees one, two, three is respectively \(19\), \(23\), \(25\).

This is a **sharp three-extension bound for the Weyl-group reconstruction problem**. In fact, one collision through extension degree two consists of classes with pairs of counts \(((0,1),(0,3))\), whose third-degree counts are \((3,7)\) and \((3,13)\). Another consists of classes with counts \(((0,3),(0,3))\), whose third-degree counts are \((15,15)\) and \((27,45)\). The equidistribution/realization theorem of Banwait–Fité–Loughran implies that these collisions are realized by actual smooth cubic surfaces over all sufficiently large finite fields; no universal claim is made for each small finite field.

## Assumptions and scope

The surface is geometrically smooth, projective, and of degree three in \(\mathbb P^3\). No restriction on \(\operatorname{char}(\mathbb F_q)\) is imposed. A geometric cubic surface is the blow-up of \(\mathbb P^2\) at six points in general position. Write its geometric Picard group in the basis \(H,E_1,\ldots,E_6\), with intersection form \(H^2=1\), \(E_i^2=-1\), and other pairwise products zero. The anticanonical class is \(-K_X=3H-\sum_i E_i\).

The \(27\) line classes are the six \(E_i\), the fifteen \(H-E_i-E_j\) for \(i<j\), and the six \(2H-\sum_{j\ne i}E_j\). A tritangent plane corresponds to an unordered triple of these classes whose sum is \(-K_X\), equivalently a triangle in the intersection graph. The two natural reduced zero-dimensional schemes associated to the lines and tritangent planes are finite étale over the perfect field \(\mathbb F_q\).

The claim is *recovery of the Weyl conjugacy class*, not recovery of the defining equation, the isomorphism class of the surface, or a canonical labeling of its lines. In particular, the theorem concerns the full set of abstract Weyl possibilities, although not every Weyl class occurs for each small field.

## Proof

**Geometric transfer.** The Galois action on the geometric Picard group preserves the canonical class and the intersection form; it therefore lies in the Weyl group \(W(E_6)\). The classical blow-up description identifies its actions on the \(27\) lines and on the \(45\) tritangent planes with the actions on the above explicitly given divisor classes and anticanonical triples. This holds in every characteristic.

**A finite exact certificate.** The accompanying standalone script `verify_e6.py` performs the following exhaustive integer operations, requiring no external packages:

1. Constructs all \(27\) divisor classes, enumerates all \(45\) anticanonical triples, and *independently* verifies the same \(45\) triples as all triangles in the intersection graph.
2. Generates the full \(51\,840\)-element Weyl group using transpositions of exceptional indices, a six-cycle, and reflection in the root \(H-E_1-E_2-E_3\). It checks that the generators preserve the intersection form and the tritangent set.
3. Partitions all \(51\,840\) group elements into conjugacy classes by exhaustive conjugation with the generators. It obtains exactly \(25\) classes, whose sizes sum to \(51\,840\).
4. Computes the complete cycle decompositions of each class representative on the \(27\) lines and the \(45\) tritangent triples; it verifies that the pairs of cycle types are all different (\(25\) total), while the individual spectra have cardinalities \(20\) and \(24\).
5. For any permutation with \(c_d\) cycles of length \(d\), computes its fixed points under the \(n\)-th power as \(\sum_{d\mid n} d c_d\). It obtains exactly \(19\), \(23\), and \(25\) distinct combined profiles for extension cutoffs one, two, and three and checks the two explicit collisions displayed above.

Since every Frobenius element belongs to one of these \(25\) Weyl classes, equality of six counts forces equality of class. Its two permutations and all extension-field counts are then determined. The finite check is exhaustive on a *known finite group*, not extrapolation from a sample of fields. All \(25\) classes and their data are independently tabulated in `e6_profiles.csv`, and the checker re-derives and byte-compares that CSV.

**Sharpness for actual cubic surfaces.** The two degree-two-profile collisions show that no uniform cutoff of two can distinguish all Weyl classes. Banwait–Fité–Loughran prove that every \(W(E_6)\) class occurs for sufficiently large \(q\), by asymptotic equidistribution with positive class density. Thus both classes in each collision occur over every sufficiently large finite field, making the cutoff genuinely sharp in that range. This argument does not claim explicit equations over each small finite field.

## Verification

Extract the script and CSV from this package into one directory and run:

```bash
python3 verify_e6.py e6_profiles.csv
```

Successful output is exactly `E6_27_LINES_45_TRITANGENTS_25_CLASSES_SHARP_THREE_EXTENSIONS_VERIFIED`. This has been executed on the embedded source and table. The script uses only Python's standard library, and the CSV contains exactly \(25\) data rows plus one header.

## Relationship to prior work

The blow-up geometry, the \(27\) lines, and the \(45\) tritangents are classical, not claimed new. Banwait–Fité–Loughran (arXiv:1606.00300, especially Table 7.1 and Section 7) give a \(25\)-class Weyl table with line orbit types and Picard eigenvalues and establish large-field realizability, but do not tabulate the tritangent cycle types or state the sharp joint three-extension inverse theorem. McKean (arXiv:2101.08217) studies rational-line counts and their field dependence; his results do not state this two-scheme recovery principle. Brundu–Logar–Polli (arXiv:2207.04493) describe the \(45\) tritangents and automorphism actions in characteristic zero; their studied automorphism stabilizers are not a full arithmetic Frobenius classification. Loughran–Trepalin (arXiv:1811.06785) solve the realization problem over finite fields, not the inverse reconstruction from these six counts.

The additional statement here is the *joint arithmetic recovery result with a proven optimal finite-extension cutoff*, not a discovery of \(W(E_6)\), of the tritangent configuration, of the \(25\) conjugacy classes, or of geometric realizability. Previously published equivalent character/cycle-index computations remain a possible priority risk.

## Limitations

This provides no algorithm to extract lines or tritangent equations directly from a cubic polynomial, and no explicit example realizing each Weyl class over every small \(q\). The classification is for geometrically smooth cubic surfaces and reduced finite étale configuration schemes. Its correctness depends on the stated classical geometric correspondence and an exhaustive finite computation, with a fully inspectable verifier; no independently commissioned mathematical audit is claimed.

## References

- Stephen McKean, *Rational lines on smooth cubic surfaces*, first posted 2021-01-20, https://arxiv.org/abs/2101.08217.
- Michela Brundu, Alessandro Logar, Federico Polli, *Construction of symmetric cubic surfaces*, first posted 2022-07-10, https://arxiv.org/abs/2207.04493.
- Barinder Banwait, Francesc Fité, Daniel Loughran, *Del Pezzo surfaces over finite fields and their Frobenius traces*, first posted 2016-06-01, https://arxiv.org/abs/1606.00300, especially Table 7.1 and the large-field distribution result.
- Daniel Loughran, Andrey Trepalin, *Inverse Galois problem for del Pezzo surfaces over finite fields*, first posted 2018-11-16, https://arxiv.org/abs/1811.06785.
- Frank Sottile, Thomas Yahl, *Splitting types of the 27 lines on cubic surfaces*, https://franksottile.github.io/research/stories/27_Frobenius/index.html (web exposition of a 2021 computational study; exact public page creation date unverified).
