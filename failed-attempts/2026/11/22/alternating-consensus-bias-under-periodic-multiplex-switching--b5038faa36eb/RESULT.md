# Alternating consensus bias under periodic multiplex switching

## Finding

For every integer \(n\ge3\), let the first social layer be the undirected, equally weighted complete graph without self-loops, with row-stochastic opinion update matrix \(A\). Let the second layer be any connected, nonbipartite, positively weighted undirected graph on the same vertices, with row-stochastic update matrix \(B\) and **nonconstant weighted vertex degrees**. The synchronous protocol applies \(A\) for \(k\ge1\) consecutive updates and then \(B\) for one update, repeating the block indefinitely. Write \(u=(1/n,\ldots,1/n)\) and \(r_k=(-1/(n-1))^k\).

For every \(k\ge1\), the block update \(P_k=BA^k\) is primitive and has the unique stationary row vector
\[
\boxed{\pi_k=(1-r_k)u(I-r_kB)^{-1}.}
\]
Let \(c=uB-u\). It is nonzero precisely because the second layer has nonconstant weighted degrees. For every coordinate \(j\) with \(c_j\ne0\), the eventual consensus starting with only vertex \(j\) holding opinion one, and all other opinions zero, satisfies
\[
\pi_{k,j}-\frac1n=r_kc_j+O(r_k^2).
\]
Its sign therefore **alternates with the parity of the block length \(k\)** for all sufficiently large \(k\); the eventual consensus converges to the complete-layer consensus while crossing it infinitely often. Explicitly, the remainder is at most \(|r_k|^2\|c\|_1/(1-|r_k|)\), so the parity sign is guaranteed whenever
\[
0<|r_k|<\frac{|c_j|}{\|c\|_1+|c_j|}.
\]

For a three-person example, the complete first layer has all off-diagonal weights one, and the second layer has undirected edge weights \(w_{12}=2\), \(w_{13}=w_{23}=1\). Then for **every** integer \(k\ge1\),
\[
\boxed{\pi_k=\left(\frac{2+r_k}{2(3+r_k)},\frac{2+r_k}{2(3+r_k)},\frac1{3+r_k}\right),\qquad r_k=(-\tfrac12)^k.}
\]
Starting from \((0,0,1)\), the isolated layers have consensus \(1/3\) and \(1/4\), respectively. The switching consensus \(1/(3+(-1/2)^k)\) exceeds **both** isolated consensuses for every odd \(k\), but lies strictly between them for every even \(k\ge2\). The exact \(k=1\) example was already reported in the originating study; the all-period parity classification and general-layer theorem are the contribution assessed here.

## Assumptions and scope

Opinions are real numbers in \([0,1]\), updated simultaneously by neighbor-weighted arithmetic averaging, with no self-weights. The first network is \(K_n\) with uniform undirected positive edge weights. The second is a fixed, connected, nonbipartite, positively weighted undirected graph on the identical \(n\) vertices with no loops and unequal weighted degrees. The integer \(k\ge1\) is a fixed deterministic time-block parameter, not a random switching duration. An initial unit-vector opinion profile is an admissible observation; more generally any initial profile \(x\in[0,1]^n\) with \(cx\ne0\) has eventual alternating bias. The claim concerns the infinite-time consensus value for each fixed \(k\), followed by varying \(k\), and not temporal oscillation of opinions within one fixed protocol.

## Proof

Define the all-ones column \(\mathbf1\) and the rank-one averaging projection \(U=\mathbf1u\). Then \(U^2=U\), \(B\mathbf1=\mathbf1\), and
\[
A=U-\frac1{n-1}(I-U),\qquad A^k=U+r_k(I-U).
\]
Consequently \(BA^k=U+r_k(B-U)\), since \(BU=U\). For \(n\ge3\), \(A^k\) is strictly positive for \(k\ge2\), so \(BA^k\) is positive. The case \(k=1\) is also primitive, as follows. Its entries are \((BA)_{ij}=(1-B_{ij})/(n-1)\), since \(B\) is stochastic. Every row corresponding to a vertex with at least two neighbors is strictly positive; every row corresponding to a leaf is positive at all columns except its unique neighbor. Nonbipartiteness guarantees at least three vertices on an odd cycle, each of which has at least two neighbors. All rows therefore have a positive transition into this three-vertex set, and every vertex in the set has positive transitions to every vertex. Thus \(BA\) is irreducible, and its positive diagonal makes it aperiodic. Consequently all \(P_k\) are primitive and repeated blocks converge to consensus. Thus \(P_k\) has a unique positive stationary law, and repeated blocks reach consensus.

Any stationary row vector \(\pi_k\) satisfies
\[
\pi_k=\pi_k[U+r_k(B-U)]=(1-r_k)u+r_k\pi_kB.
\]
Since \(|r_k|<1\) and \(B\) is stochastic, \(I-r_kB\) is invertible, yielding the boxed formula. This formula sums to one because \((I-r_kB)\mathbf1=(1-r_k)\mathbf1\).

For its bias subtract the identity \(u(I-r_kB)=(1-r_k)u-r_k(uB-u)\), to get the exact resolvent formula
\[
\pi_k-u=r_k(uB-u)(I-r_kB)^{-1}
       =r_k\sum_{m=0}^{\infty}r_k^m cB^m.
\]
A stochastic matrix contracts the row \(\ell^1\) norm, so \(\|cB^m\|_1\le\|c\|_1\). The sum of all terms with \(m\ge1\) has coordinate magnitude at most \(|r_k|^2\|c\|_1/(1-|r_k|)\). The stated strict bound on \(|r_k|\) makes that remainder smaller than \(|r_kc_j|\), proving the eventual alternating signs. The stationary distribution of irreducible undirected weighted \(B\) is proportional to weighted degrees; if \(c=0\), then \(u\) is also stationary and uniqueness makes all degrees equal. Conversely uniform weighted degrees imply \(uB=u\). This proves exactly when the effect occurs.

For the three-person witness, the matrix \(B\) has rows \((0,2/3,1/3)\), \((2/3,0,1/3)\), \((1/2,1/2,0)\). Symmetry forces \(\pi_{k,1}=\pi_{k,2}=(1-\pi_{k,3})/2\); the third coordinate of \(\pi_k=(1-r_k)u+r_k\pi_kB\) gives \(\pi_{k,3}=(1-r_k)/3+r_k(1-\pi_{k,3})/3\), hence \(\pi_{k,3}=1/(3+r_k)\). The first two coordinates follow by normalization. Odd \(k\) has \(r_k<0\) and even \(k\) has \(0<r_k\le1/4\); comparison with \(1/3\) and \(1/4\) gives all claimed strict inequalities.

## Verification

`check.py` uses exact rational arithmetic to construct both neighbor-averaging matrices, multiply their powers, compare \(BA^k\) with \(U+r_k(B-U)\), and verify the claimed stationary vector, sum to one, invariance and parity inequalities independently for integers \(1\le k\le31\). It also checks the two isolated-layer stationary vectors. These computations corroborate, but do not replace, the analytical proof for every integer \(k\) and every eligible graph.

## Relationship to prior work

Shiu and Naghizadeh's 2026 multiplex coordination study defines the alternating \(k\)-step first-layer/one-step second-layer process, proves primitive-block consensus, and supplies a single \(k=1\) three-person instance whose switching consensus lies outside the two isolated values. Its Proposition IV.4 gives a large-\(k\) **magnitude** bound without a sign classification. The witness here uses the same published three-person graph, expressly preserving that established \(k=1\) case, but supplies the complete all-period formula, a strict odd/even reversal, a uniform resolvent formula in every population size, and a quantitative parity-onset criterion for all nonregular connected undirected second layers.

Classical DeGroot averaging and perturbation identities for finite Markov chains supply the algebraic context. General stationary-vector perturbation methods are not asserted to be new; the claimed scope is the parity-controlled consensus response to the precise multiplex switching protocol.

## Limitations

The network classes are fixed and deterministic; in particular, the first layer is a uniformly weighted complete graph. Arbitrary first layers, random switching, time-dependent edge weights and nonlinear interpersonal responses are not covered. The general theorem guarantees alternation relative to the **complete-layer consensus** for sufficiently long blocks, not an overshoot of both isolated-layer consensuses for every graph; that stronger comparison is proved only for the explicit three-person network. The phenomenon is variation of the eventual consensus when the **protocol parameter** changes, not nonconvergence of opinions for any individual protocol. The historical-priority assessment is literature-bounded, not independent validation.

## References

1. Ruey-An Shiu and Parinaz Naghizadeh, *Coordination Games on Multiplex Networks: Consensus, Convergence, and Stability of Opinion Dynamics*, arXiv:2603.07633 (first public version, 2026-03-08), sections IV and Appendix, https://arxiv.org/abs/2603.07633.
2. M. H. DeGroot, *Reaching a Consensus*, Journal of the American Statistical Association 69 (1974), 118–121, https://doi.org/10.1080/01621459.1974.10480137.
3. P. J. Schweitzer, *Perturbation Theory and Finite Markov Chains*, Journal of Applied Probability 5 (1968), 401–413, https://doi.org/10.2307/3212262.
4. J. Gómez-Gardeñes and collaborators, *Discrete-time distributed consensus on multiplex networks*, New Journal of Physics 16 (2014), 113063, https://doi.org/10.1088/1367-2630/16/11/113063.
