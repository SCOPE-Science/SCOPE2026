# Exact defect-frustration and magnetic plateaux of the Fano three-spin Ising model

## Finding

Let the seven vertices be the nonzero vectors of \(\mathbb F_2^3\), with seven lines \(\mathcal L=\{\{a,b,a+b\}:a\ne b\}\) and distinguished line \(\ell_* = \{1,2,3\}\) (labels are binary integers). For spins \(\sigma_i\in\{-1,+1\}\), set
\[
Q=\prod_{i\in\ell_*}\sigma_i,\qquad
B=\sum_{\ell\in\mathcal L\setminus\{\ell_*\}}\prod_{i\in\ell}\sigma_i,\qquad
M=\sum_{i=1}^7\sigma_i,
\]
and take the classical Hamiltonian
\[
\mathcal H_{\lambda,h}(\sigma)=J(B+\lambda Q)-hM,
\qquad J>0,\quad\lambda\in\mathbb R,\quad h\ge0.
\]
Thus the six ordinary triple couplings are antiferromagnetic and \(\lambda\) is the signed strength of one marked triple coupling. Write \(u=h/J\).

For every **strictly positive field** \(u>0\), the exact ground energy in units of \(J\) is the minimum of just five affine functions:
\[
\boxed{\frac{E_0}{J}=\min\{-6-\lambda-u,\;-2+\lambda-3u,\;\lambda-5u,\;2-\lambda-5u,\;6+\lambda-7u\}.}
\]
The five terms correspond to disjoint candidate ground-state families \(A,B,C_+,C_-,D\), with respective multiplicities \(7,9,4,3,1\) and magnetizations \(1,3,5,5,7\). At a crossing, add multiplicities for **every** minimizing term; no other spin assignments minimize when \(u>0\).

For \(u=0\) the ground-state degeneracy is \(8\) if \(\lambda>-2\), \(24\) if \(\lambda<-2\), and **\(32\)** at \(\lambda=-2\). The transition is a local-frustration threshold: forcing the marked triple product to \(+1\) requires at least two positive triple products among the other six, while all seven can simultaneously have product \(-1\). Consequently one oppositely signed triple becomes favorable only when its strength exceeds twice an ordinary coupling in magnitude.

The complete zero-field partition function, for every \(\beta\ge0\), is
\[
\boxed{Z(\beta,\lambda,0)=16\cosh[\beta J(6+\lambda)]
+64\cosh(\beta J\lambda)
+48\cosh[\beta J(2-\lambda)].}
\]
The joint energy–magnetization distribution below also determines the exact finite-field partition function at every temperature.

## Assumptions and scope

The model has exactly seven labeled Ising sites and exactly the seven Fano lines as three-body interactions; no pair interactions or other fields are present. The inverse temperature \(\beta\) is arbitrary nonnegative for the partition-function statement. The field \(h\) is nonnegative; negative fields are not covered by the positive-field phase list because a three-body model need not have spin-reversal symmetry. No infinite-volume phase transition is asserted.

For explicit open-field regions, the minimizing family is as follows (all intervals refer to \(u=h/J>0\)):

| Marked ratio | Ground-state family as the field increases | Boundary fields |
|---|---|---|
| \(\lambda\le-2\) | \(B\), then \(C_+\), then \(D\) | \(1,3\) |
| \(-2<\lambda<-1\) | \(A,B,C_+,D\) | \(2+\lambda,1,3\) |
| \(\lambda=-1\) | \(A,C_+,D\) | \(1,3\), with \(A,B,C_+\) tied at \(1\) |
| \(-1<\lambda<1\) | \(A,C_+,D\) | \((3+\lambda)/2,3\) |
| \(\lambda=1\) | \(A,C_+\cup C_-,D\) | \(2,3\) |
| \(\lambda>1\) | \(A,C_-,D\) | \(2,2+\lambda\) |

At \(\lambda=1\), the middle plateau contains seven ground states of magnetization \(5\) (four from \(C_+\), three from \(C_-\)). At \(\lambda=-1,u=1\) there are exactly \(20\) coexisting ground states. At \(\lambda=1,u=2\) there are \(14\), and at \(\lambda=1,u=3\) there are \(8\). The five-function minimum formula is also a complete specification of all other boundary degeneracies.

## Proof

**Step 1: a finite-geometric identity.** For a configuration let \(S=\{i:\sigma_i=+1\}\), \(k=|S|\), and \(N_j\) be the number of Fano lines meeting \(S\) in exactly \(j\) points. Every vertex lies on three lines and every pair on one, so
\[
\sum_{j=0}^3N_j=7,\quad \sum_{j=0}^3 jN_j=3k,\quad
N_2+3N_3=\binom{k}{2}.
\]
Hence \(N_1=k(4-k)+3N_3\). A line has spin product \(+1\) precisely when it contains an odd number of positive spins, so with \(T=B+Q\),
\[
T=2(N_1+N_3)-7=2k(4-k)+8N_3-7.
\]
If \(r=|S\cap\ell_*|\), then \(Q=(-1)^{3-r}\), \(B=T-Q\), and \(M=2k-7\).

**Step 2: complete finite census.** In the Fano plane, the three-point subsets comprise seven lines and twenty-eight noncollinear triples; the four-point subsets comprise seven line-free complements of lines and twenty-eight other subsets. The number of contained lines for the possible sizes \(k=0,1,2,3,4,5,6,7\) is respectively \(0,0,0,\{0,1\},\{0,1\},2,4,7\). Classifying by \(r\) using the distinguished line gives the complete table below. The listed \(128\) states exhaust all configurations.

| \(B\) | \(Q\) | \(M\) | States |
|---:|---:|---:|---:|
| \(-6\) | \(-1\) | \(-7\) | 1 |
| \(-6\) | \(-1\) | \(1\) | 7 |
| \(-2\) | \(1\) | \(-5\) | 3 |
| \(-2\) | \(1\) | \(-1\) | 12 |
| \(-2\) | \(1\) | \(3\) | 9 |
| \(0\) | \(-1\) | \(-5\) | 4 |
| \(0\) | \(-1\) | \(-1\) | 16 |
| \(0\) | \(-1\) | \(3\) | 12 |
| \(0\) | \(1\) | \(-3\) | 12 |
| \(0\) | \(1\) | \(1\) | 16 |
| \(0\) | \(1\) | \(5\) | 4 |
| \(2\) | \(-1\) | \(-3\) | 9 |
| \(2\) | \(-1\) | \(1\) | 12 |
| \(2\) | \(-1\) | \(5\) | 3 |
| \(6\) | \(1\) | \(-1\) | 7 |
| \(6\) | \(1\) | \(7\) | 1 |

**Step 3: minimize at positive field.** Within each fixed pair \((B,Q)\), strictly positive field selects its maximal magnetization. This leaves six possible signatures, including \((B,Q,M)=(0,-1,3)\), whose energy is \(-\lambda-3u\). For \(0<u\le3\), the \(A\) energy \(-6-\lambda-u\) is no larger. For \(u\ge1\), the \(C_-\) energy \(2-\lambda-5u\) is no larger. Because both inequalities cover the positive axis (and are not simultaneously tight against the other competitors), the sixth signature is never a ground state. The remaining five energies and multiplicities are exactly the displayed list. Pairwise comparison produces the phase table and every coexistence count, with no excluded parameter interval.

**Step 4: zero field and frustration.** At zero field the most favorable \(Q=-1\) signature has \(B=-6\) and eight realizations; the most favorable \(Q=+1\) signature has \(B=-2\) and twenty-four. Comparison of \(-6-\lambda\) with \(-2+\lambda\) gives the sharp crossing \(\lambda=-2\). Here \(B=-2\) means that precisely two of the six ordinary line products are \(+1\): indeed \(B=2r-6\) when \(r\) of these six products are positive. One cannot make all six negative while the marked product is positive, by the complete incidence census. The two extra unfavorable lines are attained by the twenty-four configurations in that sector.

**Step 5: finite-temperature identity.** The table yields the partition function
\[
Z(\beta,\lambda,h)=\sum_{(B,Q,M)}n_{B,Q,M}
\exp\![-\beta\{J(B+\lambda Q)-hM\}].
\]
At \(h=0\) the table groups into two multiplicity-eight energy classes of opposite sign, two multiplicity-thirty-two classes, and two multiplicity-twenty-four classes, giving the stated three-cosh formula.

## Verification

Run `python3 verify_fano.py` with a standard Python 3 interpreter. The program independently reconstructs the seven lines using binary exclusive-or; it computes all \(128\) spin products directly, and separately computes the same signature table using only incidence and line-containment counts. Both methods agree with every table entry. It tests the five-term minimum against the full sixteen-term census on \(4100\) rational parameter pairs, the exact zero-field threshold, and key coexistence points. This finite verification is exhaustive **for this seven-spin model**, not a proof of any thermodynamic-limit assertion. The proof above does not depend on numerical floating-point computations.

## Relationship to prior work

The hypergraph three-spin Ising interaction is standard. Liu and Stanley (1974) treated three-spin interactions with fields on particular two-dimensional lattices, not the seven-point Fano design. Strečka (2018) studied a mixed-spin centered-square lattice with multiple triplet couplings and anisotropy, not this seven-site incidence structure. Berrekkal, Ellis-Monaghan, Moody, and de Mulatier (2026) give an overarching incidence-matroid framework for higher-order parity-Ising partition functions, including ways of representing fields. That framework is relevant background, but its examined text does not tabulate the present signed-Fano joint energy–magnetization spectrum or the defect/field ground-state envelope. The present result is an explicit geometry-dependent evaluation and classification, not a new general partition-function formalism.

Related Fano-network Hamiltonians incorporating hopping and other onsite terms are not equivalent to the purely classical seven-spin Hamiltonian here; inaccessible complete texts leave some historical-priority uncertainty. No assertion of independently established novelty is made.

## Limitations

This is an exact finite-size classical result, not an infinite-system phase transition. The five-term ground-state classification is only for nonnegative uniform field and one singled-out signed line; the unrestricted temperature statement uses the full table. It makes no claims about dynamics, quantum coherence, disordered multiple-defect ensembles, or critical exponents. Historical-priority assessment is provisional because some relevant older and recent complete texts could not be obtained; an indexed search is not a proof of uniqueness.

## References

- L. L. Liu and H. E. Stanley, *Exact solution in an external magnetic field of Ising models with three-spin interactions*, Physical Review B **10**, 2958 (1974), published 1974-10-01. https://doi.org/10.1103/PhysRevB.10.2958
- J. Strečka, *Strong- and Weak-Universal Critical Behaviour of a Mixed-Spin Ising Model with Triplet Interactions on the Union Jack (Centered Square) Lattice*, Entropy **20**, 91 (2018). https://doi.org/10.3390/e20020091
- K. Berrekkal, J. A. Ellis-Monaghan, M. Moody, and C. de Mulatier, *A formal framework for higher-order spin models via hypergraphs, polymatroids, and the Tutte polynomial* (2026), arXiv:2608.14628. https://arxiv.org/abs/2608.14628
- Wolfram MathWorld, *Fano Plane*, https://mathworld.wolfram.com/FanoPlane.html (incidence-design background).
