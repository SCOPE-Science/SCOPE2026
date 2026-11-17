# Spatial rigidity of primitive temporal six-cycles in elementary Rule 54

## Finding

For every indexed binary ring of circumference \(n\ge3\), let \(F_n\) be synchronous elementary cellular automaton Rule 54. Its number of configurations of **least temporal period six** is exactly
\[
P_6(n)=24\,\mathbf{1}_{8\mid n}.
\]
Equivalently, the number of primitive temporal six-cycle **orbits**, without quotienting spatial rotations, is \(4\,\mathbf{1}_{8\mid n}\). Every such state has least spatial period exactly eight: increasing ring size by repeating its eight-site word never creates additional labelled six-periodic configurations. Moreover, on every such state \(F_n^3\) agrees with a translation by four sites. Four representatives of the temporal orbits at eight sites are `00000011`, `00000110`, `00001100`, `00011000`; these form one class under spatial translation.

The complete six-step return count is
\[
\#\operatorname{Fix}(F_n^6)=1+4\mathbf{1}_{4\mid n}+24\mathbf{1}_{8\mid n},
\]
while \(\#\operatorname{Fix}(F_n^2)=1+4\mathbf{1}_{4\mid n}\) and \(\#\operatorname{Fix}(F_n^3)=1\). In particular six-period recurrence is **spatially rigid**, rather than an exponentially growing family of independent glider combinations.

## Assumptions and scope

Index sites by \(i\in\mathbb Z/n\mathbb Z\); all site labels and spatial rotations remain distinct configurations, and only temporal shifts are identified when counting temporal orbits. The local rule at time \(s\) is
\[
 x_i^{s+1}=f(x_{i-1}^s,x_i^s,x_{i+1}^s),\qquad
 f(a,b,c)=(a\wedge\neg b)\vee(\neg a\wedge(b\oplus c)).
\]
Thus precisely the input triples `001`, `010`, `100`, `101` produce output one. Ring lengths \(n\ge3\) ensure three distinct sites in each neighborhood. The claim is only for least temporal period six, not for eventual periods or longer temporal periods.

## Proof

For temporal height \(t\), encode the entire time history of one site as a \(t\)-bit word \(u\in\{0,1\}^t\). Let \(\tau(u)\) shift its bit at time \(s+1\) into position \(s\), indices taken modulo \(t\). Construct the finite directed graph \(G_t\) with vertices \((a,b)\in(\{0,1\}^t)^2\) and an edge \((a,b)\to(b,c)\) exactly if the bitwise application of \(f\) obeys \(f(a,b,c)=\tau(b)\). Here all Boolean operators act independently at each of the \(t\) time coordinates.

A cyclic closed walk of length \(n\) in \(G_t\) is **bijective** with a labelled width-\(n\), height-\(t\) space-time history obeying the update equation. Its initial time slice determines its entire history, so this is also bijective with \(\operatorname{Fix}(F_n^t)\). Consequently \(\#\operatorname{Fix}(F_n^t)=\operatorname{tr}(A_t^n)\) for the adjacency matrix of \(G_t\). This is an exact all-\(n\) identity, not a numerical extrapolation from a bounded list of ring lengths.

The complete finite graph check in `transfer_certificate.cpp` visits all ordered triples of temporal words, tests every possible edge, computes all strongly connected components using two passes of directed depth-first search, and verifies the induced in/outdegree of each cyclic component is one. Its independently replayed output is recorded in `transfer_output.txt`. The full recurrent components are:

| \(t\) | Graph vertices | Directed edges | Lengths of cyclic components |
|---:|---:|---:|---|
| 1 | 4 | 2 | 1 |
| 2 | 16 | 20 | 1, 4 |
| 3 | 64 | 56 | 1 |
| 6 | 4096 | 4160 | 1, 4, 8, 8, 8 |

The directed graph can contain transient vertices, but every closed walk lies in a strongly connected component. Since all recurrent components are simple directed cycles, a component of length \(\ell\) contributes exactly \(\ell\) to \(\operatorname{tr}(A_t^n)\) when \(\ell\mid n\), and zero otherwise. This proves the displayed formulas for the three return counts. A period dividing six, but not equal to six, divides either two or three; the one-period configuration is already included in both. Hence
\[
 P_6(n)=\#\operatorname{Fix}(F_n^6)-\#\operatorname{Fix}(F_n^2)
 -\#\operatorname{Fix}(F_n^3)+\#\operatorname{Fix}(F_n)
 =24\mathbf{1}_{8\mid n}.
\]
Dividing by six gives the orbit count.

The length-eight recurrent components give all twenty-four six-periodic configurations on the eight-site ring, and no shorter spatial words occur in those components. Their spatial words include `00111111`, `10000100` and `11000000`, each of least spatial period eight. The update traces of the four displayed temporal orbit representatives show that the sixth return occurs after three iterations followed by a four-site spatial shift, so \(F_n^3(x)=\sigma^4(x)\) on this entire class. All states at larger rings are periodic repetitions of these eight-site words, preserving this identity.

## Verification

Compile and run `transfer_certificate.cpp` with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic transfer_certificate.cpp -o transfer_certificate && ./transfer_certificate`. This checks every edge of \(G_t\), not a sample, for \(t\in\{1,2,3,6\}\). Run `python3 direct_enumeration.py` independently to evolve all original binary configurations on each ring \(3\le n\le16\), checking both fixed-power counts and the shift property. The recorded exact outputs are `transfer_output.txt` and `direct_output.txt`. Only source, not an executable binary, is needed for reproduction.

## Relationship to prior work

Martínez, Adamatzky and McIntosh's 2008 primary study of Rule 54 develops de Bruijn/cycle diagrams and lists a period-six phenomenon in a ring-size-specific attractor table. Their 2014 comprehensive treatment also contains a finite table of cycle diagrams and glider regular expressions. Thus **the existence and the eight-site example are pre-existing knowledge**. The new statement is that *every* primitive temporal six-cycle on *every* finite ring is obtained from the same eight-site spatial rotation class: the exact universal divisibility restriction and constant four-orbit census, proved by a complete return-transfer analysis. The OEIS maximum-period table for small rings is only a maximum statistic and does not imply the present all-size period-six rigidity. Related mathematical-record results about Rule 54 one-step image languages and about short cycles of other elementary rules do not imply this claim.

## Limitations

This does not classify temporal periods other than six or the basins of the four orbits. The proof of the finite SCC lemma is a complete executable integer enumeration with two-pass SCC verification, not a hand classification of all 4,096 vertices. Historical literature may contain an unindexed equivalent all-circumference classification; external independent mathematical validation has not been carried out. The results are for synchronous rule 54, not the unrelated reversible RCA54.

## References

1. G. J. Martínez, A. Adamatzky, H. V. McIntosh, *On the Representation of Gliders in Rule 54 by De Bruijn and Cycle Diagrams*, LNCS 5191 (2008), pp. 83–91, https://doi.org/10.1007/978-3-540-79992-4_11 ; public author's PDF: https://www.comunidad.escom.ipn.mx/genaro/Papers/Papers_on_CA_files/acri08R54.pdf . Springer records ebook publication 2008-08-24.
2. G. J. Martínez, A. Adamatzky, H. V. McIntosh, *Complete Characterization of Structure of Rule 54*, arXiv:1410.3096, first posted 2014-10-12, https://arxiv.org/abs/1410.3096 . Section 4 and Table 5 give selected ring-length attractors, not the all-size period-six classification.
3. OEIS A204714, *Maximum period of cellular automaton rule 54 in a cyclic universe of width n*, https://oeis.org/A204714 , initiated 2012-01-18. This source concerns maximum temporal periods, not complete counts.
