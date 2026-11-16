# Exact phaseless Walsh ambiguity for nine-point binary five-space

## Finding

For a nine-element set \(E\subseteq\mathbb F_2^5\), write
\[
W_E(u)=\sum_{x\in E}(-1)^{u\cdot x},\qquad
h(E)=(h_1,h_3,h_5,h_7,h_9),\quad
h_a=\#\{u\in\mathbb F_2^5:|W_E(u)|=a\}.
\]
Under affine equivalence, the \(\binom{32}{9}=28{,}048{,}800\) sets form **exactly nine classes**, with **exactly eight different Walsh-magnitude histograms**. Precisely one histogram is shared by two inequivalent classes:
\[
\boxed{h=(15,13,3,0,1).}
\]
Those two classes contain respectively \(6{,}666{,}240\) and \(2{,}222{,}080\) sets; together, exactly \(8{,}888{,}320\) sets (a proportion \(1792/5655\)) have this ambiguous histogram. Each other histogram determines its affine class uniquely.

An explicit inequivalent pair with that histogram is
\[
\begin{aligned}
E&=\{0,25,15,16,12,10,6,30,14\},\\
F&=\{0,6,26,5,25,31,19,11,27\},
\end{aligned}
\]
where integers encode five-bit vectors in the standard binary basis. Both sets affinely span \(\mathbb F_2^5\).

The complete census follows. A histogram lists the numbers of Fourier coefficients with absolute values \(1,3,5,7,9\), in that order. The six rank-five representatives use multiplicities of the eight columns \(000,001,010,011,100,101,110,111\) of a binary dimension-three affine-relation code; for affine rank four, the representatives are sixteen-bit subset masks in an affine hyperplane.

| Affine rank | Representative | Histogram \(h(E)\) | Number of sets |
| --- | --- | --- | ---: |
| \(4\) | `0x1ff` | \((28,0,0,2,2)\) | 14,880 |
| \(4\) | `0x37f` | \((22,6,2,0,2)\) | 416,640 |
| \(4\) | `0x777` | \((18,12,0,0,2)\) | 277,760 |
| \(5\) | `(0,0,0,1,1,2,2,3)` | \((19,7,5,0,1)\) | 6,666,240 |
| \(5\) | `(0,0,1,2,1,2,1,2)` | \((15,13,3,0,1)\) | 6,666,240 |
| \(5\) | `(0,1,1,1,1,1,1,3)` | \((15,13,3,0,1)\) | 2,222,080 |
| \(5\) | `(1,0,0,0,2,2,2,2)` | \((22,4,4,1,1)\) | 833,280 |
| \(5\) | `(1,0,1,1,1,1,2,2)` | \((18,10,2,1,1)\) | 9,999,360 |
| \(5\) | `(2,1,1,1,1,1,1,1)` | \((21,7,1,2,1)\) | 952,320 |

## Assumptions and scope

The group is the additive Boolean five-cube with the standard nondegenerate dot-product pairing. Its Fourier transform is **unnormalized**. Affine equivalence is under \(\operatorname{AGL}(5,2)\), acting on unordered supports; magnitude histograms ignore the positions and signs of transform coefficients. Because the support size is odd, all Walsh coefficients are odd and hence never zero. This theorem concerns histogram rigidity, not Fourier-support nonvanishing or orthogonal spectral bases.

## Proof

**1. Affine rank reduction.** Nine distinct points cannot fit into an affine three-plane (which has eight points). Thus every support has affine rank four or five.

**2. Full-rank supports and relation codes.** For an *ordered* full-rank configuration \(E=(x_1,\ldots,x_9)\), form the \(6\)-by-\(9\) matrix whose columns are \((1,x_j)\). Its row rank is six. The nullspace \(R\subseteq\mathbb F_2^9\) is a dimension-three code, all of whose words have even weight (the all-ones row annihilates \(R\)); distinct columns exclude weights one and two. Thus every nonzero codeword has even weight at least four. Conversely, for every such dimension-three code, \(R^\perp\) has dimension six and contains the all-ones vector. Extend that vector to a basis of \(R^\perp\) and use the other five vectors as coordinate rows. The resulting nine affine columns are distinct and affinely span five-space. Two unordered configurations are affinely equivalent if and only if their relation codes are equivalent by a coordinate permutation. Indeed, preservation of all affine dependencies gives an affine map, uniquely determined on an affine spanning subset.

**3. Complete code census.** For a generator of \(R\), let \(n_c\) be the multiplicity of column \(c\in\mathbb F_2^3\), including zero. The necessary and sufficient conditions are
\[
\sum_c n_c=9,\qquad \sum_c(n_c\bmod2)c=0,\qquad
\sum_{c:u\cdot c=1}n_c\ge4\quad(u\ne0).
\]
Each last sum is also even. There are \(\binom{16}{7}=11{,}440\) nonnegative eight-tuples of sum nine. Direct integer enumeration of these stated conditions leaves **148** tuples. The group \(\operatorname{GL}(3,2)\), of order \(168\), acts by permuting their eight column labels. Exact minimization over these 168 substitutions gives precisely the six rank-five multiplicity representatives in the table. This is an exhaustive finite classification because every generator-column multiset is considered and changing the relation-code basis is exactly the stated group action.

**4. Fourier histograms.** Let \(\mathbf1\in\mathbb F_2^9\) be the all-ones word. Since \(\mathbf1\in R^\perp\), the \(64\) elements of \(R^\perp\) pair as \(s,s+\mathbf1\), with equal absolute signed sums. Their 32 pairs correspond bijectively to the 32 characters of the affine span, and hence
\[
\boxed{h_a(E)=\tfrac12\#\{s\in R^\perp:|9-2\operatorname{wt}(s)|=a\}.}
\]
Evaluating this exact formula for each six representative codes yields the six displayed rank-five histograms. The standalone checker independently constructs actual nine-point supports and directly evaluates their 32 character sums, giving the same histograms. The two representatives sharing \((15,13,3,0,1)\) are inequivalent: their multisets of positive generator-column multiplicities are respectively \(\{2,2,2,1,1,1\}\) and \(\{3,1,1,1,1,1,1\}\). An invertible row change only permutes the eight column types, so it cannot equate these multiplicity patterns.

**5. Exact orbit sizes.** A full-rank set's affine stabilizer is isomorphic to the coordinate-permutation automorphism group of its relation code. For a column multiplicity tuple \(n\), this group has size
\[
\left|\operatorname{Stab}_{\operatorname{GL}(3,2)}(n)\right|\prod_c n_c!.
\]
Dividing \(|\operatorname{AGL}(5,2)|=319{,}979{,}520\) by that quantity gives all six exact rank-five orbit sizes in the table. Their total is \(27{,}339{,}520\).

**6. Affine rank four.** An affine rank-four nine-point set lies in a *unique* affine hyperplane: intersections of distinct affine hyperplanes have at most eight points. There are \(62\) affine hyperplanes in five-space. Within one such hyperplane, exhaustive enumeration of its \(\binom{16}{9}=11{,}440\) supports under affine translations, coordinate swaps and shears (generators of \(\operatorname{AGL}(4,2)\)) yields three orbits of sizes \(240,6{,}720,4{,}480\). The corresponding sixteen-frequency magnitude histograms are \((14,0,0,1,1)\), \((11,3,1,0,1)\), and \((9,6,0,0,1)\). Every hyperplane character occurs twice upon restriction from the five-space, so both the histograms and orbit sizes lift by the factors two and 62, respectively, yielding the first three rows. Their total is \(709{,}280\).

Finally, \(27{,}339{,}520+709{,}280=\binom{32}{9}\), so all nine classes are accounted for. The nine histograms displayed in the table take exactly eight values, with exactly one duplicate, as claimed.

## Verification

Run `python3 verify.py` with Python 3 (standard library only). It checks the 168 three-dimensional linear substitutions, all 11,440 generator-column compositions, the 148 admissible cases and six orbits; constructs full-rank point sets from each code; compares the 32 direct Walsh sums with an independent 64-word dual-code calculation; computes orbit sizes using stabilizers; and exhaustively classifies all 11,440 nine-element subsets of four-space to handle hyperplane configurations. The final assertion checks that the nine orbit sizes sum to 28,048,800 and that precisely one of eight histograms is shared by two classes. All calculations are exact integer operations. The finite classification is exhaustive by Steps 2, 3 and 6; it is not statistical sampling.

## Relationship to prior work

Danielsen and Parker (2007), *Edge Local Complementation and Equivalence of Binary Linear Codes*, provide a general code-equivalence framework and cite existing classifications of short binary codes. These classifications may contain the underlying length-nine codes; the present statement instead supplies the complete nine-point binary five-space **Walsh-magnitude histogram**, its precise affine fibers, and every labeled support-orbit multiplicity. General short-code classification alone does not state the Fourier-histogram equivalences or exact nine-point orbit census. MacWilliams-type dual weight identities are classical, and the dual-code counting in Step 4 is not claimed as a new identity.

Related public results determine the Walsh support counts for eight-point binary sets and exhibit isospectral but inequivalent dimension-three binary codes in another parameter family. Neither inspected result establishes the five-dimensional nine-point classification given here; the latter code examples concern different lengths and do not specify these nine-point affine supports. An older tabulation of precisely these nine-point Walsh histograms remains a priority risk.

## Limitations

The theorem concerns nine-element unweighted supports in the *five-dimensional* binary group, and the histogram is unlabeled: it does not claim ambiguity of the fully labeled Fourier magnitude function. It neither classifies larger ambient dimensions nor gives noise stability. A full independent mathematical audit and an exhaustive historical database search have not been performed.

## References

1. L. E. Danielsen and M. G. Parker, *Edge Local Complementation and Equivalence of Binary Linear Codes*, arXiv:0710.2243v1, publicly posted 2007-10-11; journal version, *Designs, Codes and Cryptography* 49 (2008), 161–170. https://arxiv.org/abs/0710.2243
2. *The complete Walsh Fourier-support spectrum of eight-point binary sets*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-the-complete-walsh-fourier-support-spectrum-of-eight-point-binar--bc4834afd25d
3. *Exact distortion of an isospectral binary code family in dimension three*, public research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/12/SCOPE-exact-distortion-of-an-isospectral-binary-code-family-in-dimensi--17a2f2b6a09c
