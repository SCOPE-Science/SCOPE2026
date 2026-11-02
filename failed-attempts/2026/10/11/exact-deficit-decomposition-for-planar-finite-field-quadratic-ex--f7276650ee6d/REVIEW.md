# Independent mathematical audit

## correctness

PASS

For odd q, j≠0 and nondegenerate binary homogeneous Q, 0∉S_j, antipodes are distinct, M=q−χ(−det A). For each nonzero pair sum s, Q(s−a)=Q(a)=j forces B(s,a)=Q(s), a line meeting the nondegenerate affine conic at ≤2 points, hence only one unordered pair. The zero fiber consists of all antipodal pairs. Exact counting therefore gives W=2T²−Σt_i²−2Σr_i²+4|Σz_i|², and additive-character orthogonality gives ||Ef||_4^4=q² W/M⁴ with normalized ||f||_2⁴=T²/M². Direct algebra with r_i²=u_iv_i, T=Σt_i, R=Σr_i gives exactly the four proposed summands and constant C=3q²(M−1)/M³. Nonnegativity: variance, (u−v)², t_i≥2r_i, triangle inequality. Equality for nonzero f forces each u_i=v_i and equal t_i and common z_i argument; converse holds. The zero f case is vacuous. Checks: independently reconstructed 7-blob assigned Git tree SHA, independent weighted pair-sum enumeration (360 cases on p=3,5,7,11, split/anisotropic), independent SymPy polynomial residual vanishing for m=1..5. Finite checks corroborate, while the all-odd-prime-power claim follows from the algebraic proof; package verify.py was read but not relied on as proof. No metric-to-extremizer distance bound is asserted.

## originality

FAIL

The scientific final claim is an exact four-term telescope of earlier *published* exact split-hyperbola and anisotropic norm-one-torus proofs. Both earlier RESULT.md proofs already display W=2T^2-sum t_i^2-2sum r_i^2+4|P|^2 and the successive phase-alignment, antipodal-balance and equal-pair-mass inequalities, with precisely the same variables. Subtracting their final upper bound from the exact W identity and retaining their three intermediate inequality gaps gives the submitted four positive terms by direct expansion; no new lemma, inequality, quantitative parameter or geometry is needed. The proposed lower bounds are immediate positive summands of this restatement. The decomposition is not printed verbatim in either earlier finding, but the combined prior proof data already directly imply it. This is stronger evidence of coverage than a failed title search; hence originality FAIL. General published Fourier papers supply earlier geometry/boundedness, but the decisive prior implication is from the two same-object exact proofs.

## value

FAIL

The object and endpoint are natural, and decomposing a deficit can be valuable in principle. In this instance however the submitted result contains no new phenomenon, cutoff, classification, sharp metric-distance stability estimate or nonstandard lemma beyond the identical earlier split/anisotropic proofs. Every displayed positive term is just the elementary slack of the previously written triangle, AM–GM and Cauchy inequalities; two advertised amplitude controls are the direct rearrangements of those same bounds. The paper itself disclaims a full metric-distance stability theorem or an optimal stability constant. The normal-form decomposition is a pedagogically useful packaging of already available sharp proof data, but as claimed it is a routine telescoping exercise, not a substantively distinct mathematical fact. This rejection is not based on computational finiteness, manuscript length, or lack of sweeping downstream consequences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
