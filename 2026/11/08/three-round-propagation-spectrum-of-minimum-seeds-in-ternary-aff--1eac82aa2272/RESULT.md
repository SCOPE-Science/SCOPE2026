# Three-round propagation spectrum of minimum seeds in ternary affine Steiner systems

## Finding
Let \(d\ge1\), let \(\operatorname{AG}(d,3)\) denote the Steiner triple system on \(\mathbb F_3^d\) with blocks the three distinct points \(x,y,-x-y\), and let \(S\) be any affine basis (a set of \(d+1\) affinely independent points). Define \(F_0=S\) and, for \(r\ge0\),
\[
F_{r+1}=F_r\cup\{-x-y:x,y\in F_r,\ x\ne y\}.
\]
Thus \(F_r\) is precisely the set burned after \(r\) parallel propagation rounds with all seed points burned at time zero and no additional ignitions. Put \(n=d+1\), with the convention \(\binom nk=0\) for \(k>n\).

**Theorem.** The first three propagation profiles are independent of the choice of affine basis and satisfy
\[
\begin{aligned}
|F_0|&=n,\\
|F_1|&=n+\binom n2,\\
|F_2|&=n+\binom n2+3\binom n3+\binom n4,\\
|F_3|&=n+\binom n2+3\binom n3+5\binom n4
   +11\binom n5+15\binom n6+7\binom n7+\binom n8.
\end{aligned}
\]
There is a complete *pointwise* description, not merely a scalar formula. Express a point in its unique affine coordinates \(a=(a_1,\ldots,a_n)\in\mathbb F_3^n\) with \(\sum_i a_i=1\), and set \(u(a)=|\{i:a_i=1\}|\) and \(v(a)=|\{i:a_i=2\}|\). Then
\[
\begin{aligned}
F_1:&\quad (u,v)\in\{(1,0),(0,2)\},\\
F_2:&\quad (u,v)\in\{(1,0),(0,2),(2,1),(4,0)\},\\
F_3:&\quad (u,v)\in\{(1,0),(0,2),(2,1),(4,0),\\
&\hspace{27mm}(1,3),(0,5),(3,2),(2,4),(1,6),(0,8)\}.
\end{aligned}
\]
In these descriptions the types are automatically restricted by \(u+v\le n\). In particular, **the entire system is burned within three propagation rounds if and only if \(d\le4\)**. In dimension \(5\), precisely \(237\) of the \(243\) points are burned after three rounds; the remaining six are exactly those with five affine coefficients \(1\) and one coefficient \(2\).

## Assumptions and scope
All arithmetic for point coordinates is in \(\mathbb F_3\), and all points are labelled by their actual vector coordinates. A seed is a minimum-cardinality lazy burning set, as characterized by affine independence: its size is \(d+1\), and its affine span is the full geometry. Propagation is simultaneous: points created in round \(r+1\) may only participate in propagation in the following round. The round index starts at \(r=0\) immediately after the seeds are burned; this is not the sequential source-ignition burning number. No probabilistic ignition or additional sources are used.

## Proof
**Affine coordinate reduction.** Given an affine basis \(S=\{p_1,\ldots,p_n\}\), the map
\[
(a_1,\ldots,a_n)\longmapsto\sum_{i=1}^n a_ip_i,
\qquad \sum_{i=1}^n a_i=1,
\]
is bijective from an affine hyperplane in \(\mathbb F_3^n\) onto \(\mathbb F_3^d\). Under this map the third point of the block through distinct coefficient vectors \(a,b\) has coefficients \(-a-b\). The seed vectors become the \(n\) standard unit vectors. Permuting these \(n\) coordinates corresponds to an affine automorphism, so the reachable set is determined by the pair \((u,v)\) of counts of entries \(1\) and \(2\).

**Rounds one and two.** Joining two distinct standard units produces precisely a vector with two entries \(2\), giving the round-one types. For round two, the possibilities are: two distinct units (an old type); a unit with a two-\(2\) vector (an old unit or a vector with two \(1\)'s and one \(2\)); or two distinct two-\(2\) vectors (an old type or a vector with four \(1\)'s). The new types are \((2,1)\) and \((4,0)\). Every arrangement of the stated coefficients occurs whenever its support fits within \(n\).

**Round three: exhaustive type calculation.** Write \(A=(1,0)\), \(B=(0,2)\), \(C=(2,1)\), and \(D=(4,0)\) for the four round-two types. For any two distinct vectors of these types, the type of \(-a-b\) depends only on the overlap of their \(1\)- and \(2\)-positions. The following upper-triangular table lists *all* possible output types. The operation is symmetric, so the other half is redundant.

| Input types | Output types |
|:--|:--|
| \(A,A\) | \(B\) |
| \(A,B\) | \(A,C\) |
| \(A,C\) | \(B,C,(1,3)\) |
| \(A,D\) | \((1,3),(0,5)\) |
| \(B,B\) | \(C,D\) |
| \(B,C\) | \(A,B,C,(1,3),(3,2)\) |
| \(B,D\) | \(B,(1,3),(2,4)\) |
| \(C,C\) | \(A,B,C,D,(1,3),(0,5),(3,2),(2,4)\) |
| \(C,D\) | \(C,(1,3),(0,5),(3,2),(2,4),(1,6)\) |
| \(D,D\) | \((3,2),(2,4),(1,6),(0,8)\) |

To reproduce the complete table without assumptions about the dimension, choose representatives in eight coordinates: fix the first operand to \(1^u2^v0^{8-u-v}\), and enumerate every second operand with its prescribed multiplicities. Exclude identical operands; take \(-a-b\) coordinatewise. This finite classification is exhaustive in *all* dimensions because both input vectors have support at most four, so the union of their supports has size at most eight. Every overlap type in a larger coordinate space can be relocated into eight coordinates without changing the output type. Conversely, an output whose support is at most \(n<8\) appears already in the \(n\)-coordinate system: the following witnesses show the newly appearing types with exactly their support size, with each displayed pair consisting of round-two vectors; remaining zero coordinates can be appended:
\[
\begin{array}{c|c|c}
\text{output type}&\text{first input}&\text{second input}\\\hline
(1,3)&1000&1111\\
(0,5)&10000&01111\\
(3,2)&22000&00112\\
(2,4)&220000&001111\\
(1,6)&1120000&0001111\\
(0,8)&11110000&00001111
\end{array}
\]
Here words are strings of coefficients in \(\mathbb F_3\), and their outputs are calculated by \(-a-b\); all entries satisfy the affine sum condition. This proves precisely the ten claimed round-three types. The appended `verify.py` independently reproduces every entry in the table and checks the counts by direct propagation.

**Enumeration.** For fixed \((u,v)\), the number of vectors is \(\binom nu\binom{n-u}v\). Summing over the listed types for each round yields the three stated binomial polynomials. For instance, the round-three contributions at supports \(1,2,3,4,5,6,7,8\) are respectively
\[
 n,\ \binom n2,\ 3\binom n3,\ 5\binom n4,\ 11\binom n5,\ 15\binom n6,\ 7\binom n7,\ \binom n8.
\]
This also establishes basis independence for the full pointwise and counting statements.

**Three-round completion threshold.** For \(n\le5\), the list of round-three types contains every admissible coefficient type with \(u+2v\equiv1\pmod 3\) and \(u+v\le n\); direct enumeration of these finitely many pairs, or the size formula \(|F_3|=3^{n-1}\), proves completion. For \(n\ge6\), vectors having five entries equal to \(1\) and one entry equal to \(2\) (and all other entries zero) have affine coefficient sum \(7\equiv1\pmod3\) but type \((5,1)\), absent from the round-three list. They therefore remain unburned. At \(n=6\) there are exactly \(6\) such vectors, and the polynomial gives \(|F_3|=237\) of \(243\) points.

## Verification
Run `python3 verify.py` using Python's standard library. It independently constructs the full affine geometry with seed \(\{0,e_1,\ldots,e_d\}\), simulates the simultaneous update rule without importing the affine-profile enumeration, and compares the predicted counts for every \(1\le d\le9\). It also exhaustively enumerates all type-pair overlaps in eight affine coordinates and verifies the ten-row table, then checks the multinomial identities for \(2\le n\le24\). The formal unrestricted proof is the coordinate-and-overlap argument above, not interpolation from the finite tests.

## Relationship to prior work
Burgess, Danziger, Jones, Marbach, and Pike, *Burning Steiner Triple Systems* (first submitted 26 August 2026), prove the minimum lazy burning size \(d+1\) for \(\operatorname{AG}(d,3)\) and determine its separate sequential-source burning number \(d+3\). Their Section 4 treats eventual closure and optimal source rounds; it does not give the simultaneous early-time distribution from a minimum seed or the exact three-round completion dimension. The known correspondence between Steiner-system spreading sets and lazy burning means this claim is also a statement about finite-time closure under line completion; it is not treated as a distinct independent novelty claim. Nagy and Szemerédi (2022) study minimal spreading-set cardinalities and geometrical subsystems, not the parallel round-three profile. Searches of related finite-field bootstrap percolation and affine-line propagation literature found no theorem implying the stated ten orbit types or the polynomial. These negative searches do not establish exhaustive historical priority.

## Limitations
The theorem gives a complete profile only through three *parallel* propagation rounds; it does not determine the completion time for every dimension larger than four. It concerns minimum seed sets (affine bases), not the dynamics of arbitrary initial subsets. The formula is a result about ternary affine Steiner triple systems and does not assert an analogous result for non-affine triple systems or projective systems. Independent mathematical audit and exhaustive historical priority verification have not been performed.

## References
1. Andrea C. Burgess, Peter H. Danziger, Caleb W. Jones, Trent G. Marbach, David A. Pike, *Burning Steiner Triple Systems*, arXiv:2608.25627v1, submitted 2026-08-26. https://arxiv.org/abs/2608.25627 . Full text: https://arxiv.org/html/2608.25627 .
2. Zoltán Lóránt Nagy and Levente Szemerédi, *Steiner triple systems and spreading sets in projective spaces*, Journal of Combinatorial Designs **30** (2022), 549–560, DOI:10.1002/jcd.21841. https://onlinelibrary.wiley.com/doi/full/10.1002/jcd.21841 .
