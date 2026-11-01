# Independent mathematical audit

## correctness

PASS

Under j∈{1/2,1,3/2,…}, d=2j+1 and normalized trace-1 Choi construction, the vectorization/partial-transpose flip identity and local time-reversal unitary make C_j^{T2} isospectral to [1/(d j(j+1))](Σ_a J_a⊗J_a)F. Casimir coupling is [L(L+1)−2j(j+1)]/2 on each spin-L subspace, dim=2L+1, with swap parity (−1)^{2j−L}. Thus every claimed eigenvalue and multiplicity follows. The full weighted q-sum Σ_{L=0}^{2j}(2L+1)[L(L+1)−2j(j+1)] vanishes, and the partial sum to L=k−1 equals k²[(k²−1)/2−2j(j+1)] with k=ceil((sqrt(1+8j(j+1))−1)/2); hence the stated trace norm and negativity including exact zero boundary. x=2L+1,y=2j+1 yields Pell x²−2y²=−1; the converse positive solutions satisfy 0≤L≤2j automatically and first nontrivial j are 2,14,84. j=1/2, j=1 boundaries are covered. Inspected all seven assigned Git blobs and reconstructed actual Git tree SHA. Original verify.py checked spin matrices and normalized Choi PT for j=1/2,…,4 and Pell j≤500; independent fresh dense-matrix eigenvalue reconstruction for 13 half-integer/integer spins j≤13/2 agreed. Finite cases corroborate the analytic proof only.

## originality

FAIL

Strong prior mathematical implication discovered from a primary paper published 2026-07-05, before the 2026-10-12 research record. Rudnicki et al. give a complete general Choi projector and rank-J tensor-operator/partial-transpose identity for all SU(2)-covariant channels; specialization to α_1=1/3 reproduces exactly the operator diagonalized in this submission. Applying the textbook Casimir+flip eigenvalues gives the claimed all-spin spectrum, and the claimed negativity and negative Pell classification are elementary arithmetic consequences. Schliemann 2005 also establishes a much broader existing formalism for all eigenvalues of the partial transpose of SU(2)-invariant spin states. Neither preprint nor paper needs to print the present formula to imply it. Original self-review omitted decisive July 2026 coverage. Resultary returned no exact table; negative search does not overturn the source-level mathematical implication.

## value

FAIL

The normalized spin-channel Choi negativity and Pell singularity locus are natural quantities and useful for exposition, but the exact spectrum is an immediate rank-one-tensor (J=1) special case of the already published 2026 SU(2)-covariant Choi partial-transpose identity with the standard Casimir eigenvalues. The negativity formula is evaluation of a basic polynomial finite sum and the Pell set merely rewrites the zero of that existing sector eigenvalue. No independent nonstandard structural lemma, new undetermined invariant, unknown arithmetic cutoff, counterexample or calculation not mechanically implied by the stronger antecedent survives. The Pell observation can be instructive but is not a separately motivated valuable theorem under the stated bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
