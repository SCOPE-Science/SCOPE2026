# First-force rigidity and zero-forcing polynomials of powers of cycles

## Finding
For every pair of integers \(k\ge1\) and \(n\ge2k+1\), let \(G=C_n^k\) have labelled vertices \(\mathbb Z/n\mathbb Z\), with two distinct vertices adjacent if their cyclic distance is at most \(k\). A set \(S\) is zero forcing if and only if some blue vertex \(v\in S\) initially has at most one white neighbor. This is a complete characterization of all zero-forcing sets, including the all-blue set.

All inclusion-minimal zero-forcing sets of \(G\) have size exactly \(2k\). In particular, \(G\) is well-forced and \(Z(G)=2k\); the scalar zero-forcing number is previously known and is not claimed as new. The number of **labelled minimum sets** is
\[
 m_{n,k}=\begin{cases}n,&n=2k+1,\\ kn,&n=2k+2,\\ (2k-1)n,&n\ge2k+3.\end{cases}
\]

There is an exact finite transfer-matrix formula for the entire zero-forcing polynomial \(\mathcal Z_{n,k}(z)=\sum_{S\subseteq V(G),\ S\text{ zero forcing}}z^{|S|}\). Let the rows and columns of \(M_k(z)\) be indexed by binary words \(a=(a_1,\dots,a_{2k})\in\{0,1\}^{2k}\). For each \(b\in\{0,1\}\), form \(w=(a_1,\ldots,a_{2k},b)\) and \(a'=(a_2,\ldots,a_{2k},b)\). If \(w_{k+1}=1\) and \(w\) has at most one zero, **do not** insert that transition. Otherwise contribute \(z^b\) to matrix entry \((a,a')\) (summing contributions if a pair can arise more than once). Then
\[
\boxed{\mathcal Z_{n,k}(z)=(1+z)^n-\operatorname{tr}(M_k(z)^n).}
\]
For example, \(\mathcal Z_{8,2}(z)=24z^4+48z^5+28z^6+8z^7+z^8\).

## Assumptions and scope
Graphs are finite, simple, undirected, and labelled. Standard ordinary (not skew) zero forcing is used: a blue vertex with exactly one white neighbor may color that neighbor blue. The case \(n=2k+1\) is the complete graph, and \(n=2k+2\) is the complete graph minus a perfect matching; both are included. Counts distinguish vertex-labelled subsets, not cyclic or dihedral orbits.

## Proof
**1. Local first-force criterion.** Every blue vertex has exactly \(2k\) neighbors. If a non-all-blue initial set has a forcing chronology, its first force comes from a blue vertex \(v\) having exactly one white neighbor. Conversely, suppose an initially blue \(v\) has at most one white neighbor. If there is one, force it. After this move, or immediately if there is none, all of the consecutive cyclic arc \(N[v]=\{v-k,\ldots,v+k\}\) of length \(2k+1\) is blue. As long as a blue consecutive arc \([a,b]\) of length at least \(2k+1\) is not all vertices, the blue vertex \(b-k+1\) has precisely one white neighbor, \(b+1\), because every other neighbor lies in the arc. Force \(b+1\), enlarging the arc by one, and repeat. This works on the cycle, including all boundary lengths. Hence the trigger criterion is sufficient. The all-blue set plainly satisfies it, because each of its vertices has zero white neighbors.

**2. Minimum and inclusion-minimal sets.** Let \(S\) be any zero-forcing set and choose a witnessing \(v\in S\). For any neighbor \(w\in N(v)\) that is white initially choose this \(w\); when no neighbor is white, choose an arbitrary neighbor \(w\). The \(2k\)-element set \(T_{v,w}=\{v\}\cup(N(v)\setminus\{w\})\) lies inside \(S\), and the criterion makes \(T_{v,w}\) zero forcing. Conversely no set of size below \(2k\) can make the first force, because the forcing vertex together with its other \(2k-1\) blue neighbors requires \(2k\) blue vertices. Thus every zero-forcing set contains a minimum set of size \(2k\), and every inclusion-minimal zero-forcing set is minimum. This also proves the scalar bound, independently of numerical computations.

**3. Count minimum sets.** If \(n=2k+1\), the graph is complete and its minimum sets omit exactly one vertex, giving \(n\). If \(n=2k+2\), the only non-neighbor of any vertex is its antipodal mate. A set of size \(2k\) leaves exactly two white vertices; it forces if and only if they are not an antipodal pair. Hence its number is \(\binom n2-n/2=kn\).

Assume \(n\ge2k+3\). By the criterion, a minimum set has exactly \(2k\) blue vertices contained in an arc of length \(2k+1\) obtained from a closed neighborhood by omitting one neighbor (not its center). If the omitted position is at an end, the blue set is a single block of \(2k\) consecutive vertices: exactly \(n\) possibilities. Otherwise the blue vertices form two nonempty consecutive blocks of sizes \(a\) and \(2k-a\), separated by exactly one white vertex. The remaining outside white block has length \(n-2k-1\ge2\); hence the two-block representation and its ordered lengths are unique, with \(n\) rotations for each \(a=1,\ldots,2k-1\). The closed arc's center has to remain blue, which is equivalent to \(a\ne k\). There are \((2k-2)n\) two-block sets. Therefore the minimum multiplicity is \(n+(2k-2)n=(2k-1)n\).

**4. Full polynomial.** Code a blue vertex by \(1\) and a white vertex by \(0\). The local characterization says an \(n\)-bit cyclic word is zero forcing exactly when at least one length-\(2k+1\) cyclic window has a blue center and at most one zero. The binary de Bruijn matrix \(M_k(z)\) precisely forbids these windows, with weight \(z\) for each blue symbol appended. Its length-\(n\) closed walks correspond bijectively, with a fixed labelled starting coordinate, to cyclic binary words avoiding every forbidden window; each bit is appended once, including when \(n=2k+1\). Consequently \(\operatorname{tr}(M_k(z)^n)\) is the weight enumerator of non-zero-forcing subsets. Subtracting it from \((1+z)^n\), the enumerator of all subsets, proves the formula.

## Verification
Run the included Python 3 standalone file `verify.py` with `python verify.py`. It independently builds the graph adjacency and applies the literal iterative color-change rule. It checks 327,512 subsets over 35 graph profiles, compares all polynomial coefficients with a separately implemented cyclic-window transfer, and checks 30 additional boundary profiles of minimum multiplicities. The exact execution returned `VERIFY_OK` with `literal_dynamics=PASS`, `cyclic_transfer_polynomial=PASS`, and `minimum_multiplicity=PASS`. This finite test supports but is not a proof of the infinitely many cases; the preceding argument is unrestricted.

## Relationship to prior work
Boyer et al. introduced zero-forcing polynomials and studied ordinary cycles and other graph families [1]; the ordinary-cycle case \(k=1\) is prior coverage. Brimkov and Carlson studied minimal zero-forcing sets and general conditions for well-forcedness [2]. Grood et al. studied well-forced graph classes [3]. Abiad et al. explicitly gave the scalar \(Z(C_n^k)=2k\) and a forcing construction for consecutive vertices [4]. No originality is claimed for these previously known results. The present claim is the all-set **first-force equivalence**, the complete transfer-matrix enumerator for cycle powers, their well-forcedness, and the exact labelled minimum-set multiplicity with its sharp two boundary cases. Relevant alias terminology is `consecutive circulant` \(C_n(1,\ldots,k)\); the square \(C_{2m}^2\) is also the total graph of an ordinary \(m\)-cycle, when the parameters match. Equivalent unindexed prior enumerations remain possible.

## Limitations
The formula is a finite matrix expression of dimension \(2^{2k}\), not an asserted simple scalar closed form for each coefficient. It proves no enumeration of symmetry orbits and no corresponding theorem for nonconsecutive circulants or powers of arbitrary graphs. Originality is literature-search-based and provisional, and independent mathematical review has not been performed.

## References
[1] K. Boyer et al., *The zero forcing polynomial of a graph*, arXiv:1801.08910, first submitted 2018-01-26. https://arxiv.org/abs/1801.08910

[2] B. Brimkov and J. Carlson, *Minimal Zero Forcing Sets*, arXiv:2204.01810, first submitted 2022-04-04. https://arxiv.org/abs/2204.01810

[3] C. Grood et al., *Well-forced graphs*, arXiv:2312.14298, first submitted 2023-12-21. https://arxiv.org/abs/2312.14298

[4] A. Abiad et al., *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892, submitted 2026-10-02. https://arxiv.org/abs/2610.03892
