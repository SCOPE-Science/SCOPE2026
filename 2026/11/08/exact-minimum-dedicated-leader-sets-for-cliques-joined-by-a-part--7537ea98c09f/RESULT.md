# Exact minimum dedicated-leader sets for cliques joined by a partial matching

## Finding

Let \(B_{m,k}\) be the union of two vertex-disjoint copies of \(K_m\), on ordered sets
\(\{u_1,\ldots,u_m\}\) and \(\{v_1,\ldots,v_m\}\), with added edges \(u_iv_i\) for
\(1\le i\le k\). For every pair of integers \(m\ge3\) and \(2\le k\le m\),
consider the continuous-time fixed, unweighted Laplacian system
\[
\dot x=-L(B_{m,k})x+B_S f(t),
\]
where the columns of \(B_S\) are distinct standard-coordinate vectors at a chosen
leader set \(S\). Write \(\kappa(m,k)\) for the least number of columns that makes
the pair \((-L,B_S)\) Kalman controllable.

**Theorem.** The exact minimum and the number of distinct optimal vertex sets are
\[
\kappa(m,k)=
\begin{cases}
2m-k-2,&2\le k<m,\\
m-1,&k=m,
\end{cases}
\qquad
N(m,k)=
\begin{cases}
2^k m(m-k),&2\le k<m,\\
m\,2^{m-1},&k=m.
\end{cases}
\]

All minimum sets are as follows.

* When \(k<m\), form the \(k\) matched classes \(M_i=\{u_i,v_i\}\), the
  \(m-k\) unmatched-left singleton classes \(U_j=\{u_j\}\), and the
  \(m-k\) unmatched-right singleton classes \(V_j=\{v_j\}\). Select exactly
  one vertex in every class except two; the two omitted classes must have
  **different types** from \(\{M,U,V\}\). Within a selected matched class,
  either endpoint is allowed.
* When \(k=m\), omit one matched pair entirely and choose exactly one of its
  endpoints in each of the other \(m-1\) pairs.

In particular, adding the final matching edge changes the shape of the optimal
leader sets but not their minimum size or their total number:
\(\kappa(m,m-1)=\kappa(m,m)=m-1\) and
\(N(m,m-1)=N(m,m)=m2^{m-1}\).

## Assumptions and scope

All clique edges and matching edges have conductance one. The graph is finite,
simple, connected and undirected. Every chosen vertex receives its **own independent
input**, not one shared input coupled to several vertices. Full state controllability
is meant in the usual Kalman/PBH sense for the specified graph Laplacian; the theorem
does **not** assert strong structural controllability for arbitrary edge weights.
The claimed classification covers \(m\ge3\) and \(2\le k\le m\); the one-bridge
case and the exceptional four-cycle \(B_{2,2}\) are not part of the theorem.

## Proof

### 1. Exact eigenspaces for a partial matching

For \(k<m\), write \(\ell=m-k>0\). The Laplacian has the following orthogonal
eigenspace decomposition (up to choosing bases within each eigenspace):
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
0&1\\
m&2m-k-2\\
m+2&k-1\\
\lambda_-&1\\
\lambda_+&1
\end{array}
\quad
\lambda_\pm=\frac{m+2\pm\sqrt{(m+2)^2-8k}}{2}.
\]
Indeed, \(Lx=mx\) first forces the coordinate sum in each clique to vanish
because an unmatched vertex has the equation
\(m x_{u_j}-\sum_i x_{u_i}=m x_{u_j}\), and similarly on the right.
The matched equations then give \(x_{u_i}=x_{v_i}=a_i\).
Thus the entire \(m\)-eigenspace is parametrized by the \(2m-k\) class
values \(a_i,b_j,c_j\), subject to precisely two independent constraints
\[
\sum_{i=1}^k a_i+\sum_{j=k+1}^m b_j=0,\qquad
\sum_{i=1}^k a_i+\sum_{j=k+1}^m c_j=0.
\]
The two constraints have full rank because unmatched-left and
unmatched-right classes are both present. Therefore the dimension is
\(2m-k-2\).

The \(m+2\)-eigenspace is given by
\[
x_{u_i}=a_i,\quad x_{v_i}=-a_i \quad(1\le i\le k),
\qquad
\sum_{i=1}^k a_i=0,
\]
with zero unmatched coordinates, hence dimension \(k-1\).
The all-ones vector spans the zero eigenspace. The remaining
two-dimensional invariant antisymmetric subspace has coordinates
\(x_{u_i}=a,\ x_{v_i}=-a\) for matched indices and
\(x_{u_j}=b,\ x_{v_j}=-b\) for unmatched indices.
In the variables \((a,b)\), its matrix is
\[
\begin{pmatrix}
m+2-k&-(m-k)\\
-k&k
\end{pmatrix},
\]
with characteristic polynomial
\(\lambda^2-(m+2)\lambda+2k\).
Its two roots are real, distinct and disjoint from
\(0,m,m+2\): its discriminant is positive for \(k\le m-1\);
the characteristic polynomial takes the values \(2k,-2(m-k),2k\)
at \(0,m,m+2\), respectively. Each root's eigenvector has both
\(a\ne0\) and \(b\ne0\), so it is nonzero on **every** vertex.

### 2. Every possible minimum set when \(k<m\)

Because \(L\) is real symmetric, the PBH criterion states that \(S\)
controls the system if and only if coordinate restriction to \(S\)
is injective on *each* eigenspace. The \(m\)-eigenspace yields the lower
bound \(|S|\ge2m-k-2\).

Suppose equality holds. On this eigenspace, observing either one or two
vertices of a matched class measures only its single common class
variable. There are \(2m-k\) class variables. With \(2m-k-2\)
observations, coordinate restriction can be injective only if exactly
\(2m-k-2\) **different** classes are observed, once each, leaving exactly
two unobserved classes. To see the last equivalence, restrict the two
displayed constraints to variables in the unobserved classes: their
coefficient columns are
\[
M:(1,1)^{\mathsf T},\qquad
U:(1,0)^{\mathsf T},\qquad
V:(0,1)^{\mathsf T}.
\]
A pair of these columns is independent if and only if its types differ.
This proves the claimed *necessary and sufficient* condition for
injectivity on the high-multiplicity \(m\)-eigenspace.

Every such set omits at most one matched class. Hence the
\(m+2\)-eigenspace is also detected: its matched coefficients sum to
zero, and all but at most one are observed. The two remaining simple
eigenspaces have nonvanishing coordinates everywhere, and the constant
zero eigenvector is detected by any nonempty set. Thus the same condition
is sufficient for full Kalman controllability, completing the exact
minimum-set classification for \(k<m\).

Put \(\ell=m-k\). Omitting one \(U\) and one \(V\) gives
\(\ell^2 2^k\) possibilities. Omitting one \(M\) and one unmatched
class of either side gives \(2k\ell\,2^{k-1}\) possibilities.
Their sum is \(2^k\ell(\ell+k)=2^k m(m-k)\).

### 3. Complete matching

If \(k=m\), the graph is the Cartesian product \(K_m\square K_2\).
The Laplacian eigenvalues are \(0,2,m,m+2\), of respective
multiplicities \(1,1,m-1,m-1\). For \(m\ge3\), they are distinct.
The \(m\)-eigenspace consists of vectors with matching-pair coordinates
\((a_i,a_i)\) and \(\sum_i a_i=0\); the \(m+2\)-eigenspace has
\((a_i,-a_i)\) and \(\sum_i a_i=0\). The simple eigenvectors are
constant and antisymmetric across the two cliques, respectively,
and have no zero entries.

The \(m\)-eigenspace gives \(|S|\ge m-1\). At equality, it is detected
if and only if exactly \(m-1\) *different* matched pairs contribute
an observed vertex: measuring both endpoints of a pair is redundant,
and two unobserved pairs leave a nonzero coefficient vector supported
there. For that selection, the \(m+2\)-eigenspace is also detected
because all but one matched-pair coefficient is known and its sum is
zero. Both simple eigenvectors are detected, proving sufficiency.
There are \(m\) choices of the omitted pair and \(2^{m-1}\)
independent endpoint choices on the other pairs.

Finally substituting \(k=m-1\) in the partial-matching formulas yields
the same minimum and count as \(k=m\). This proves every assertion. \(\square\)

## Verification

The accompanying `verify.py` constructs each **actual** integer graph
Laplacian, obtains exact symbolic eigenspaces and performs the PBH
restriction-rank test on **every** subset of the proposed minimum size
for \(m\in\{3,4,5\}\) and \(2\le k\le m\). This is 1,094
exact candidate-set comparisons across nine parameter cases, giving
420 controlling sets in total; all observed counts equal the theorem.
It additionally checks a full symbolic Kalman controllability matrix,
and separately tests that only 4 of the 12 optimum sets for
\(B_{3,2}\) are zero-forcing sets.

Run `python verify.py` with Python 3 and SymPy installed. The finite
checks stress-test the formulas; the proof above, not enumeration,
establishes the result for all admissible \(m,k\).

## Relationship to prior work

Monshizadeh, Zhang and Camlibel (2014) relate zero forcing to
controllability over **families** of graph-structured matrices. The
present theorem concerns **one fixed** unit-weight Laplacian and fully
classifies its smallest dedicated-coordinate input sets; those
sets need not be zero-forcing sets, as witnessed already by the
\(B_{3,2}\) comparison above. The one-bridge case is expressly
excluded because related bridge-barbell forcing formulas provide
substantial prior coverage.

Hsu (2019) gives a minimum-controller classification for *threshold
graphs*, but the present family contains induced \(P_4\) configurations
(for example the induced path \(u_j-u_1-v_1-v_j\) for \(j>k\),
while for \(k=m\) choose three distinct indices and the induced path
\(u_i-u_j-v_j-v_\ell\)); its hypothesis therefore does not hold here. Dai (2022) gives a
critical-set framework and explicit solutions for deterministic
scale-free networks and Cayley trees, rather than a matching-dependent
classification of two cliques. More general eigenspace/PBH theorems
provide the criterion, not the pair-class characterization or count
without the new spectral and combinatorial analysis.

## Limitations

The theorem does not treat unequal clique sizes, unequal edge
conductances, shared or unrestricted input columns, or arbitrary
directed graphs. It also does not claim a new universal PBH criterion.
Priority against inaccessible or unindexed specialist literature
cannot be established by database searches alone. The smallest
complete-matching case \(m=2\) is excluded because the eigenvalues
\(2\) and \(m\) then coincide, changing the eigenvector test.

## References

1. N. Monshizadeh, S. Zhang, M. K. Camlibel, *Zero forcing sets and
   controllability of dynamical systems defined on graphs*, first public
   arXiv version 19 March 2014, https://arxiv.org/abs/1403.4868 .
2. S.-P. Hsu, *Minimal Laplacian controllability problems of threshold
   graphs*, IET Control Theory & Applications, first published
   22 May 2019, https://doi.org/10.1049/iet-cta.2018.5875 .
3. L. Dai, *Minimum leader selection for controllability of undirected
   graphs with leader–follower framework*, IET Control Theory &
   Applications, first published 29 October 2022,
   https://doi.org/10.1049/cth2.12385 .
