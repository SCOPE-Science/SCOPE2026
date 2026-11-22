# One symmetry class of optimal identifying codes on the three-stage cyclic butterfly

## Finding

Let \(B_3\) be the undirected **cyclic** binary butterfly network with three stages and 24 vertices, as defined below. A radius-one identifying code is a set of monitoring vertices whose intersections with all closed neighborhoods are nonempty and pairwise distinct.

**Theorem.** The identifying-code number of \(B_3\) is exactly \(9\). There are exactly \(48\) distinct labeled minimum codes, all in one orbit under the natural group of \(48\) stage/address automorphisms. In particular, every minimum code has the distribution \((2,3,4)\) of sensor counts across its three stages, in some order; each of the six possible orders occurs eight times. The natural group acts freely and transitively on the 48 optimum codes.

An explicit optimum \(C_0\), where a pair is (stage, binary address), is

\[
\begin{aligned}
 C_0=\{ &(0,000),(0,011),(0,101),(0,110),\\
       &(1,001),(1,010),(1,100),\\
       &(2,100),(2,111)\}.
\end{aligned}
\]

Here each three-character address in the displayed set is a binary string, not a decimal integer. Its exact 24-bit membership mask in the encoding below is `901669` (hexadecimal).

## Assumptions and scope

The graph is the **cyclic** butterfly, not the conventional layered acyclic-butterfly network. Its vertex set is

\[
V=\{(i,a):i\in\{0,1,2\},\ a\in\{0,1\}^3\}.
\]

For each stage \(i\) (indices modulo three) and address \(a\), add undirected edges between \((i,a)\) and both \((i+1,a)\) and \((i+1,a\oplus e_i)\), where \(e_i\) flips bit \(i\) of the address (with bit positions indexed zero, one, two). This yields a simple four-regular graph on 24 vertices.

For any vertex \(v\), let \(N[v]\) contain \(v\) and its four neighbors. A sensor set \(C\subseteq V\) is identifying if \(N[v]\cap C\ne\varnothing\) for every \(v\), and if \(N[u]\cap C\ne N[v]\cap C\) whenever \(u\ne v\). Every sensor has closed-neighborhood, radius-one reach. Vertices and sensors are labeled by their precise stage and address.

## Proof

First, for any finite graph, the identification condition is equivalent to the conjunction of the following finite hitting conditions:

\[
\begin{split}
 C\cap N[v]&\ne\varnothing \quad(v\in V),\\
 C\cap (N[u]\mathbin{\triangle}N[v])&\ne\varnothing
 \quad(\{u,v\}\subset V,\ u\ne v).
\end{split}
\]

Indeed, the first condition is exactly domination. The second holds precisely when the two neighborhood intersections have different membership in at least one sensor. For \(B_3\) there are 24 domination conditions and \(\binom{24}{2}=276\) separation conditions, all nonempty. Thus there are exactly 300 explicitly generated conditions. The property is monotone in \(C\): adding a sensor cannot destroy domination or a difference of signatures.

Enumerate the 24 vertices by index \(j=8i+a\), where \(a\) is the binary address interpreted as an integer from zero through seven. A code is represented by a 24-bit integer with bit \(j\) set for vertex \((i,a)\). Construct the 24 closed-neighborhood masks from the edge definition; a candidate is identifying exactly when its bitwise intersection with every one of the 300 condition masks is nonzero. Exhaustive enumeration of the \(\binom{24}{8}=735{,}471\) masks of cardinality eight gives **zero** identifying codes. Exhaustive enumeration of the \(\binom{24}{9}=1{,}307{,}504\) masks of cardinality nine gives **exactly 48**. Monotonicity excludes every code of size less than eight, so the minimum is nine, and the 48 identified nine-element sets are all optima. The exact executable implementations are `verify.py` and `verify.cpp`.

For the orbit claim, let \(t\in\{0,1\}^3\) be an address translation, let \(k\in\{0,1,2\}\) be a simultaneous stage/bit-position rotation, and let \(r\in\{0,1\}\) indicate reflection. When \(r=0\), send

\[
(i,a)\longmapsto ((i+k)\bmod 3,\ \rho_k(a)\oplus t),
\]

where \(\rho_k\) rotates the three bit positions by \(k\). When \(r=1\), first reflect \((i,a)\) to \(((-i)\bmod 3,\sigma(a))\), with \(\sigma\) sending bit position \(j\) to \(2-j\), and then apply the preceding rotation and translation. Directly applying the edge rule proves these are automorphisms: rotation carries the toggled bit \(i\) to bit \(i+k\); reflection reverses the directed stage progression and carries its toggled bit \(i\) to bit \(2-i\). There are \(8\cdot3\cdot2=48\) such transformations, all distinct.

Apply them to \(C_0\). The supplied exact verifiers show that their images are 48 *distinct* nine-vertex identifying codes, and that their set agrees with the complete nine-element census. Consequently every minimum code is in this single orbit and its stabilizer in the natural group is trivial. The representative has stage counts \((4,3,2)\). Stage rotations/reflections give all six permutations; translations yield eight variants of each. This proves the remaining assertions.

## Verification

Two standalone source programs and a machine-readable list of all 48 masks accompany this result. Run either of the following in the extracted package directory:

```sh
python3 verify.py
g++ -O2 -std=c++17 verify.cpp -o verify_cpp && ./verify_cpp
```

The Python program generates all vertices and edges using set-based adjacency, checks all code sizes zero through nine directly against all 300 hitting conditions, constructs the 48 symmetry images, and compares with `OPTIMA.txt`. The C++ program independently constructs neighborhoods by bit operations, checks all eight- and nine-element subsets, validates the 48 graph automorphisms on every ordered vertex pair, checks the representative, reconstructs its orbit, and compares with `OPTIMA.txt`. Both programs have been executed against the packaged data and returned `VERIFY_OK`. The C++ search over eight-element subsets suffices to exclude all smaller sets by monotonicity.

## Relationship to prior work

Foucaud's 2009 research thesis, Section 4.2, defines precisely this *cyclic* butterfly graph and gives general lower and constructive upper bounds for identifying codes; its upper construction is stated for dimensions at least four. Its displayed graph for dimension three does not provide an exact dimension-three minimum or a classification of all dimension-three optima. The present finite theorem sharpens the generic eight-sensor lower bound to nine at this first four-regular instance, and classifies every optimum.

Chen, Lu, and Miao (2009) give identifying-code results for paths and cycles, not the cyclic butterfly. Ferrero and coauthors (2016) address minimum rank and zero forcing on a *different*, conventional layered butterfly graph having \((r+1)2^r\) vertices. Their parameters and objective therefore neither define nor imply this theorem. A comparison of similarly indexed sensor-identification results for de Bruijn, Kautz, Fibonacci and Lucas networks likewise concerns different graph families; none implies the complete 48-placement census in \(B_3\).

## Limitations

This is an **exact finite theorem only for the 24-vertex, three-stage cyclic butterfly**. It does not prove any all-dimensional formula for butterfly identifying codes, nor determine the minimum for four stages. No independent mathematical audit has been performed. The exhaustive code and symmetry classification are reproducible from the complete source files; they are not a formal proof in a theorem prover. A previously unindexed equivalent finite computation cannot be excluded by literature search alone. Foucaud's thesis is dated June 2009 but its first exact public release day was not verified; the 2009-08-19 date in metadata is an independently verified date for the cited open identifying-code antecedent, not a claimed publication day for the thesis.

## References

1. F. Foucaud, *Les codes identifiants dans certaines classes de graphes*, research master's thesis, Université Bordeaux 1, June 2009, Section 4.2, pages 46–49. https://perso.limos.fr/ffoucaud/Publications/MastersThesis/memoire_master2_florent_foucaud_codes_identifiants_2009.pdf
2. C. Chen, C. Lu, and Z. Miao, *Identifying codes and locating-dominating sets on paths and cycles*, arXiv:0908.2750v1, submitted 19 August 2009. https://arxiv.org/abs/0908.2750
3. D. Ferrero, C. Grigorious, T. Kalinowski, J. Ryan, and S. Stephen, *Minimum rank and zero forcing number for butterfly networks*, arXiv:1607.07522v1, 26 July 2016. https://arxiv.org/abs/1607.07522
