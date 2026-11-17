# Threshold-graph rigidity and a power-of-two equilibrium type law for triangular networks

## Finding

Let \(n\ge 3\) and let \(J(n,2)=L(K_n)\) be the triangular graph whose vertices are the unordered pairs of an \(n\)-element labelled set. Each vertex has one of two states. Simultaneous strict open-neighbor majority is used, with the existing state retained in a tie. Consider only **one-step fixed configurations**, and identify two of them if a permutation of the original \(n\) ground-set labels carries one into the other (rather than using any additional exceptional automorphisms of the triangular graph).

**Theorem.** Each fixed configuration's state-one edges form a threshold graph on the original ground set. The number of fixed-configuration equivalence classes under ground-set relabelling is exactly
\[
\boxed{U_n=2^{\lfloor n/2\rfloor}}.
\]
More precisely, write a threshold graph in its canonical creation order: begin with one vertex and successively add either a vertex isolated from all earlier vertices (bit \(0\)) or a vertex joined to all earlier vertices (bit \(1\)). Let \(k\) be the number of \(1\) bits. The number \(u_{n,k}\) of fixed-configuration types with this \(k\) is
\[
u_{n,0}=u_{n,n-1}=1,\qquad
u_{n,k}=2^{k-1}\quad(1\le k\le \lfloor(n-2)/2\rfloor),
\]
\[
u_{n,k}=u_{n,n-1-k},\qquad
u_{2m+1,m}=0\quad(m\ge1).
\]
The convention \(u_{n,k}=0\) outside \(0\le k\le n-1\) is understood. Thus when \(n\) is odd there is a missing middle creation-size class.

There is also an exact **labelled occupation-refined** polynomial. Put \(b_0=0\) and choose \(b_1,\dots,b_{n-1}\in\{0,1\}\). Define
\[
d_i(b)=i b_i+\sum_{j=i+1}^{n-1}b_j,\quad
m_r(b)=\#\{i:d_i(b)=r\},\quad
s(b)=\frac12\sum_i d_i(b).
\]
Let \(\mathcal B_n\) consist of the words for which, for every \(0\le i<j<n\),
\[
 b_j=1\Longrightarrow d_i(b)+d_j(b)\ge n,\qquad
 b_j=0\Longrightarrow d_i(b)+d_j(b)\le n-2.
\]
Then, if \(E_n(z)\) counts labelled fixed configurations by the number of state-one sites,
\[
\boxed{E_n(z)=n!\sum_{b\in\mathcal B_n}
\frac{z^{s(b)}}{\prod_{r=0}^{n-1}m_r(b)!}}.
\]
This uses at most \(2^{n-1}\) candidate words in place of \(2^{\binom n2}\) possible edge-state configurations. Complementing states gives \(E_n(z)=z^{\binom n2}E_n(z^{-1})\).

## Assumptions and scope

All graphs are finite, simple and undirected. The ground set of \(K_n\) is labelled. Two fixed states are equivalent only under the natural action of the ground-set permutation group. The canonical creation word is an isomorphism-type encoding for threshold graphs, not an arbitrary ordering of the labels. The polynomial counts states on \(\binom n2\) sites, without dividing by the automorphism group of \(J(n,2)\). Claims concern only immediate fixed states, not genuine two-cycles, attraction basins, or convergence time.

## Proof

**1. Local majority and threshold rigidity.** Let \(H\) be the graph consisting of state-one edges of \(K_n\), and write \(d_i\) for its vertex degrees. The site corresponding to an edge \(ij\) of \(K_n\) has \(2(n-2)\) neighbors in \(L(K_n)\). Of these, exactly \(d_i+d_j-2\) are one when \(ij\) itself is one, and exactly \(d_i+d_j\) are one when it is zero. By the tie-retention rule, fixing a one requires \(d_i+d_j\ge n\), and fixing a zero requires \(d_i+d_j\le n-2\). Hence, in a fixed configuration,
\[
 ij\in E(H)\quad\Longleftrightarrow\quad d_i+d_j\ge n,
\]
and no pair has degree sum \(n-1\). These actual degrees therefore serve as threshold weights; \(H\) is a threshold graph. Conversely, a threshold graph whose actual degrees satisfy these two inequalities gives a fixed configuration, directly by the same neighbor count. This proves the precise criterion without invoking any generic period-two theorem.

**2. Unique creation words and the weighted formula.** Threshold graphs can be built by adjoining isolated or universal vertices. Their creation words, with the first vertex written as \(0\), are unique up to graph isomorphism: the last bit says whether the last-added vertex is isolated or universal, a choice determined by the final graph unless it is the one-vertex graph; deleting any member of the terminal twin class repeats this argument. In a word \(b\), a vertex born at step \(i\) is adjacent to the \(i\) predecessors when \(b_i=1\), and to each later vertex whose bit is one. Its degree is therefore \(d_i(b)\) as stated. The local test from part 1 becomes precisely the defining pairwise test for \(\mathcal B_n\). In a fixed isomorphism type, vertices with the same degree are twins: their edge relationships with other vertices are determined by degree sums, and their mutual relationship is also determined by those sums. Conversely, no permutation can move vertices of distinct degrees. Its full ground-set automorphism group thus has order \(\prod_r m_r!\), giving exactly \(n!/\prod_r m_r!\) labelled realizations, all with \(s(b)\) one-edges. The polynomial and complement symmetry follow.

**3. A lattice-path criterion for sparse creation words.** Suppose a creation word has \(k\ge1\) one-bits and \(n\ge2k+2\). Regard the complete word \(b_0\cdots b_{n-1}\) as a walk with an up-step for \(0\) and a down-step for \(1\). Its final height is \(h=n-2k\ge2\). All zero-zero pairs automatically meet the fixing inequality because each zero-vertex has degree at most \(k\). A one-vertex created after \(s\) zeros and as the \(j\)-th one has degree \(k-1+s\), and the zeros immediately preceding it have degree \(k-j+1\). For a turn \(0\to1\), the most stringent zero-one edge has degree sum \(2k-j+s\), so its fixing condition is that the walk height immediately after that down-step, \(s-j\), be at least \(h\). For a turn \(1\to0\), the most stringent absent one-zero edge gives the opposite condition that the height immediately after that down-step be at most \(h-1\). Checking these turns covers every cross-type pair, since degrees of the successive one-vertices are nondecreasing and degrees of successive zero-vertices are nonincreasing. The first down-step must land at height at least \(h\), so at least \(h+1\) initial zeros precede it. Consequently every one-vertex has degree at least \(k-1+(h+1)=k+h\), making all one-one pairs satisfy the fixing inequality. The two turn conditions are therefore necessary and sufficient.

Removing the first \(h-2\) initial zeros converts such a word bijectively into a valid word with \(k\) ones and \(k+2\) zeros (length \(2k+2\)), with the threshold height changed from \(h\) to \(2\). Re-inserting these zeros reverses the operation. Thus the number of sparse types is independent of \(n\) once \(n\ge2k+2\).

**4. Two-child recursion at height two.** At \(k=1\), the unique valid length-four word is \(0001\). For any valid word of length \(2k+2\), define two children with \(k+1\) one-bits:

- **A:** insert a \(1\) immediately after its final run of ones, then append a \(0\).
- **B:** if the word ends in \(0\), append \(01\); if it ends in \(1\), insert a \(0\) immediately before the final run of ones and append a \(1\).

Both preserve the initial \(0\), add one up-step and one down-step, and end at height two. Under the turn criterion, A lengthens only the final down-run and closes with an up-step; any final down-run followed by at least two up-steps ends at height at most zero before lengthening, so its post-lengthening endpoint still meets the \(1\to0\) bound. B either adds a final two-step peak, landing at height two, or raises the final down-run by one up-step and extends its end by one down-step. These operations preserve all turn inequalities. A always ends in \(0\), B in \(1\).

Conversely, a valid child ending in \(0\) must have a final run of at least two consecutive down-steps, because a one-step internal down-run cannot both start at height at least two and end at height at most one. Remove its final \(0\) and the last \(1\) of this final down-run; the turn criterion yields a valid parent, inverse to A. For a child ending in \(1\), if its final down-run has length one, remove the terminal \(01\); otherwise remove the \(0\) immediately preceding its final down-run and remove its final \(1\). In the latter case, the first landing of the shortened run is at least height two because the original run ended at height two and had length at least two. All other turn inequalities persist (and any joined down-runs only remove a turn). This is a valid parent, inverse to B. The reverse operations are disjoint and exhaustive, so each valid parent has exactly two children and every child has a unique parent. Hence the sparse class count is \(2^{k-1}\).

**5. Middle exclusion and complementation.** Complementing \(H\) exchanges ones with zeros and preserves fixedness of the majority rule. On creation words this exchanges every subsequent bit, taking \(k\) to \(n-1-k\); therefore \(u_{n,k}=u_{n,n-1-k}\). When \(n=2k+1\) and \(k\ge1\), a one-bit's first occurrence must be preceded by at least two zeros: the first zero has degree \(k\), and the first one has degree \(k-1+s\), so the edge condition \(2k-1+s\ge2k+1\) requires \(s\ge2\). But then the first two zero-vertices both have degree \(k\), violating the absent-edge requirement \(2k\le n-2=2k-1\). Thus the odd middle class is empty. Summing sparse classes, their complements, and omitting the odd middle class proves \(U_n=2^{\lfloor n/2\rfloor}\).

## Verification

The theorem is an all-size proof, not an extrapolation from enumeration. The attached `verify.py` independently evaluates the creation-word criterion and labelled-weight formula, and tests the two-child recursion together with padding. The separate C++ checker `brute.cpp` computes the original majority condition over all \(2^{\binom n2}\) configurations for \(3\le n\le7\), without using the threshold-word algorithm. To reproduce from a directory with the attached files:

```sh
python3 verify.py
c++ -O2 -std=c++17 -Wall -Wextra brute.cpp -o brute
./brute
```

The initial fixed counts for \(n=3,4,5,6,7,8,9,10,11,12\) are respectively \(2,10,12,164,268,5562,11852,300952,785534,23769244\). The recursion verification tests base sizes through \(k=8\) and padded sizes through three additional initial zeros; polynomial checks run through \(n=15\). These checks support, but do not replace, the proof.

## Relationship to prior work

The classical finite-graph majority period-two theorem, reported in Benjamini et al. (2014), concerns eventual temporal periods, not the isomorphism types of immediate equilibria on triangular graphs. Barrus (2016) surveys threshold graph creation, degree rigidity and their general enumeration, but not this dynamical self-degree restriction. A published line-graph majority classification gives a general half-factor method and a formula for unweighted fixed states on all degree-parity-compatible base graphs, including \(K_n\); that stronger **general-purpose fixed-state reduction is acknowledged**, and the current result does not claim it as new. What is supplied here is the further structural threshold-graph restriction, the explicit sparse-word doubling bijection, the odd-middle exclusion, and the evaluated \(2^{\lfloor n/2\rfloor}\) *ground-set orbit* count. An unindexed equivalent enumeration or an overlooked consequence in older threshold-graph literature remains a priority risk.

## Limitations

The equivalence relation is ground-set relabelling, not the potentially larger full automorphism group of a small triangular graph. The polynomial enumerates immediate equilibria only. A finite-sum formula is not an asymptotic approximation, and no claims are made about computational complexity optimality, all temporal two-cycles, transient depths, or attractor basins. Historical originality is a same-model best-knowledge assessment, not independent priority certification.

## References

1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1, first posted 2014-05-11, https://arxiv.org/abs/1405.2486.
2. M. D. Barrus, *Weakly threshold graphs*, arXiv:1608.01358v1, first posted 2016-08-03, https://arxiv.org/abs/1608.01358.
3. *Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics*, public mathematical result, 2026-11-01, https://github.com/published-finding corpus/2026/tree/main/2026/11/1/SCOPE-incidence-conservation-and-half-factor-classification-of-two-cyc--61b3de3ad47a.
4. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics 30 (1980), 187–189, DOI:10.1016/0012-365X(80)90121-1.
