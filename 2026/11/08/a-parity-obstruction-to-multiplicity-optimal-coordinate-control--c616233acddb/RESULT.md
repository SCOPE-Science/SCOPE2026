# A parity obstruction to multiplicity-optimal coordinate control on weighted hypercubes

## Finding

For every integer \(d\ge6\), give the Boolean hypercube \(\{0,1\}^d\) conductance \(w_i\) on every edge flipping coordinate \(i\), with
\[
(w_1,w_2,w_3,w_4,w_5,w_6)=(1,3,5,7,9,20),\qquad
w_j>\sum_{i<j}w_i\quad(7\le j\le d).
\]
Let \(\kappa_w\) be the minimum cardinality of a vertex set that, with one independent input per selected vertex, renders the continuous-time heat system controllable. Then
\[
\boxed{\max_\lambda\dim\ker(L_w-\lambda I)=2,\qquad \kappa_w=3.}
\]
The three coordinate vertices \(\{0,e_1,e_2\}\) attain the minimum. In particular the six-dimensional example is a connected, weighted-vertex-transitive graph on \(64\) vertices with Laplacian spectral multiplicity at most two but an exact three-coordinate-input requirement. The gap persists for arbitrarily large dimensions under the stated high-coordinate separation.

## Assumptions and scope

Vertices are binary vectors \(x=(x_1,\ldots,x_d)\); \(e_i\) flips coordinate \(i\), and \(\oplus\) denotes coordinatewise addition modulo two. Every \(w_i\) is fixed and strictly positive. The weighted combinatorial Laplacian is
\[
(L_wf)(x)=\sum_{i=1}^dw_i\bigl(f(x)-f(x\oplus e_i)\bigr).
\]
The controlled system is \(\dot z=-L_wz+B_Su\), with the columns of \(B_S\) exactly the standard basis vectors indexed by distinct vertices in \(S\). Thus each independent input acts at one vertex only. The assertion is not a claim about the minimum rank of an unrestricted, generally dense input matrix. The primary classification is \(93B05\).

## Proof

**Walsh eigenspaces.** For every frequency \(a\in\{0,1\}^d\), define the character \(\chi_a(x)=(-1)^{\sum_i a_ix_i}\). Then
\[
L_w\chi_a=2\Bigl(\sum_iw_ia_i\Bigr)\chi_a.
\]
The characters are an orthogonal basis, so the eigenspace indexed by weighted subset sum \(s\) consists exactly of the characters with \(\sum_iw_ia_i=s\). For the symmetric matrix \(L_w\), the PBH criterion says that a coordinate set \(S\) controls the system if and only if restriction of these characters to \(S\) is injective on **every** equal-sum fiber.

**Exact base collision census.** For the first six coordinates the subset-sum generating polynomial is
\[
F(t)=(1+t)(1+t^3)(1+t^5)(1+t^7)(1+t^9)(1+t^{20})
=\sum_{s=0}^{45}t^s-t^2-t^{43}+\sum_{s\in R}t^s,
\]
where
\[
R=\{8,9,10,12,13,15,16,17,20,21,24,25,28,29,30,32,33,35,36,37\}.
\]
This directly proves that exactly \(20\) fibers are double, the other \(24\) nonempty fibers are singletons, and no fiber has size three. For each double fiber consisting of frequencies \(a,b\), write its *difference mask* as \(\delta=a\oplus b\); number masks by \(\sum_i2^{i-1}\delta_i\). Direct expansion of the displayed product gives the complete collision table:

| Difference mask \(\delta\) | Weighted subset sums having this mask |
|---:|:---|
| 15 | 8, 17, 28, 37 |
| 23 | 9, 16, 29, 36 |
| 27 | 10, 15, 30, 35 |
| 30 | 12, 13, 32, 33 |
| 59 | 20, 25 |
| 61 | 21, 24 |

The two entries in every double fiber are distinct Walsh frequencies. As a transparent example, the subset sum \(8\) has the two representations \(3+5=1+7\) and difference mask \(15\); at sum \(20\), the representations \(1+3+7+9=20\) have mask \(59\).

**Why no two vertices work.** If the two actuator vertices are \(x,y\), put \(v=x\oplus y\). At a double fiber with difference mask \(\delta\), the restricted \(2\)-by-\(2\) Walsh matrix has full rank exactly when
\[
\sum_{i=1}^d v_i\delta_i\equiv1\pmod2.
\]
Among the six occurring masks, five satisfy
\[
15\oplus23\oplus30\oplus59\oplus61=0.
\]
Were one pair of actuator vertices to control all these double fibers, summing their five necessary odd-parity equations modulo two would give \(0=1\), a contradiction. This excludes **every** choice of two vertices. Zero or one actuator also fails because double eigenspaces exist.

**Why three specified vertices work.** Select \(S=\{0,e_1,e_2\}\). For a double fiber with frequencies \(a,b\), the ratios of their character values on these three vertices are \(\{1,(-1)^{\delta_1},(-1)^{\delta_2}\}\). Each of \(15,23,27,30,59,61\) has at least one of its first two bits set; hence those ratios are not all equal, and the two character columns are independent. Every singleton restriction is nonzero, since Walsh characters never vanish. PBH therefore gives full controllability with these three coordinate inputs.

**Infinite extension.** For \(j\ge7\), the condition \(w_j>\sum_{i<j}w_i\) ensures that the highest coordinate at which two subsets differ cannot be compensated by any lower coordinates. Consequently two equal weighted sums have identical frequency bits \(7,\ldots,d\), and their first-six bits form precisely one of the preceding equal-sum pairs. Every old collision appears in each high-bit sector, so maximum multiplicity stays exactly two, the five-mask odd circuit still obstructs every two-site choice, and the same \(\{0,e_1,e_2\}\) controls all eigenspaces. This proves the claim for every finite \(d\ge6\).

## Verification

Run `python3 checker.py` using the Python standard library only. The script independently constructs all first-six subset-sum fibers, checks the polynomial-derived complete collision table, verifies the five-mask parity contradiction, and tests all \(2016\) unordered pairs of six-cube vertices against the exact PBH criterion. It also verifies \(4096\) integer Laplacian/Walsh identities, certifies the proposed three-site placement on every fiber, and checks the separated-weight instances in dimensions \(7\), \(8\), and \(9\). Computations are exact integers; the universal dimension-extension step is the proof above, not an inference from those finite checks.

## Relationship to prior work

Yuan et al. (2013) give the eigenvalue-multiplicity principle for the *number of unconstrained input channels*, which supplies a lower bound for dedicated coordinate inputs but is not a substitute for checking one common coordinate set on all eigenspaces. Notarstefano and Parlangeli (2012/2013) analyze coordinate controllability of unweighted Cartesian-product grid Laplacians through eigenvectors; their unit-conductance model does not contain these direction-dependent resonances. Monshizadeh, Zhang, and Camlibel (2014) study qualitative-family controllability and zero forcing, a stronger, different quantifier over matrices. Hsu (2019) already distinguishes terminal-coordinate control from unrestricted and binary input matrices for threshold graphs; the general phenomenon of different input budgets is therefore **not** asserted as new. The contribution here is the explicit positive-weight, vertex-transitive hypercube family, the exact \(2\)-versus-\(3\) separation, and the short odd-Walsh-parity certificate with an explicit attaining placement.

## Limitations

This theorem is about fixed direction-homogeneous conductances, not arbitrary edge-by-edge perturbations, not all direction-weight vectors, and not robustness under perturbing the six prescribed weights. Generic perturbations can remove the repeated eigenvalues. It makes no minimal-dimension assertion for the first possible separation and no claim about control energy or numerical conditioning. The exact result should not be read as contradicting the unrestricted-input channel theorem; the admissible input matrices differ. The literature comparison is based on the cited accessible primary texts and searches, and unindexed specialized coverage remains a priority risk.

## References

1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang, Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications 4, 2447 (first public journal appearance 2013-09-12), https://doi.org/10.1038/ncomms3447; preprint https://arxiv.org/abs/1310.5806.
2. G. Notarstefano and G. Parlangeli, *Controllability and observability of grid graphs via reduction and symmetries*, IEEE Transactions on Automatic Control 58 (2013), 1719–1731; preprint https://arxiv.org/abs/1203.0129.
3. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, IEEE Transactions on Automatic Control 59 (2014), 2562–2567; preprint https://arxiv.org/abs/1403.4868.
4. S.-P. Hsu, *Minimal Laplacian controllability problems of threshold graphs*, IET Control Theory & Applications 13 (2019), 1639–1645, https://doi.org/10.1049/iet-cta.2018.5875.
