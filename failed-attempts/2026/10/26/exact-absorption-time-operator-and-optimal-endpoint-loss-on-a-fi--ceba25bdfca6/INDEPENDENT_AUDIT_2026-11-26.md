# Independent mathematical audit

## correctness

PASS

For A=−iH−γP, an eigenvalue on the imaginary axis would require an eigenvector with zero first coordinate; the path equations propagate zero to every coordinate. Thus A is strictly stable, and integrating the matrix product gives the unique solution of A†Q+QA=−I. To verify the proposed entries let Lₛ=n−s+1 (Lₙ₊₁=0) and Dᵣ=(r−1)γ+r/γ. On interior off-diagonals the commutator vanishes by the zero second differences of these affine factors. In the first row its off-diagonal entries are −iγQ₁ₛ: for odd s−1 the neighboring entries have even distance, giving (D₂−2D₁)Lₛ/2=γLₛ/2, and for even s−1 the neighboring entries have odd distance, giving −iLₛ/2. Although the prose in line 101 labels the neighboring parities in reverse, the commutator identities and the entry formula are correct. The diagonal commutator gives i away from site 1 and −i(n−1) at site 1, where the loss term adds n. This verifies all boundary cases, including n=2. Cyclicity of trace applies to all density matrices. AM–GM gives the unique positive minimizer √(a/(a−1)) for a≥2 and the stated minimum; at a=1 the reciprocal law has no finite minimizer. An independently written column-vectorized dense Kronecker solve for n=2,…,8 at γ=0.35,0.7,1,1.6,3 matched all entries, with maximum difference 2.40×10⁻¹⁴ and residual 7.11×10⁻¹⁵. It can be replayed by solving [I⊗A†+Aᵀ⊗I] vec Q=−vec I and comparing entrywise.

## originality

FAIL

Multiple distinct indexed Findings state the full finite-path parity kernel and the localized optimum. They cover arbitrary coherent and mixed initial states, not merely the mean lifetime from a single endpoint. Hopping sign and loss-rate notation do not furnish a scientific distinction. Independently, a journal-paper precursor gives the opposite-end localized special case. This is scientific overlap, not a finding about authorship, intent or priority.

## value

FAIL

A full integrated-survival operator is intrinsically useful because it carries phase-sensitive contributions that no single localized lifetime supplies. Here, however, the indexed comparisons already supply that full operator and its optimization consequences, so the frozen finding adds no distinct exact invariant or extension. A rate reparameterization, alternating-site phase and bounded numerical corroboration do not create a separate scientific contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
