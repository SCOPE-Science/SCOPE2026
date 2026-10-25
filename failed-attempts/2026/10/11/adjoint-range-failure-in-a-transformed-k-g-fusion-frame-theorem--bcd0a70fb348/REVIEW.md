# Independent mathematical audit

## correctness

PASS

For H=C^2, K=diag(1,0), U=[[0,1],[0,0]], W=H, v=1 and Lambda=K, the original frame operator is K*K=K=KK* and thus Parseval relative to K. U*=e2 e1*, so UU*=K and ||U*f||=||K*f|| for every f, giving delta=1 and R(U)=R(K)=span(e1). But K U*=0 and hence transformed Lambda U* pi_UW=0, so at e1 target ||K*e1||²=1 but transformed coefficient energy is 0. The theorem’s sufficient implication is false. The Moore-Penrose identity incorrectly used in its proof is (K†)*K*=P_R(K), which fixes U*f only if R(U*) subset R(K), absent from the statement. For any genuinely well-defined transformed family, Lemma 1 yields S_Gamma=U S_Lambda U*, and the exact lower-frame inequality is U S_Lambda U* >= c KK*, equivalently R(K) subset R(U S_Lambda^(1/2)) by Douglas; upper boundedness comes from the original Bessel bound times ||U||².

## originality

FAIL

A separate published mathematical finding on the controlled K-g-fusion transformation has already supplied the *identical* two-by-two matrices K=diag(1,0), U=[[0,1],[0,0]], one block W=H, Lambda=K, identity controls, Parseval energy, delta=1 equality and zero transformed analysis. Setting C=C′=I in the 2020 controlled definition and Theorem 2.3 produces exactly the uncontrolled 2020 Theorem 4 transformation and hypotheses. Thus the printed theorem counterexample is an immediate specialization of a published complete counterexample, even though that other finding names a different original article. The remaining frame-operator criterion follows routinely from the 2020 published frame-operator identity and Douglas range theorem. Publication dates for both contemporary findings are 2026-10-11, so intra-day priority or independent discovery is not asserted. Mathematical coverage as of this audit, rather than title similarity, determines FAIL.

## value

PASS

Theorem 4 concerns preservation of a natural operator-valued fusion-frame lower inequality. A single rank-one instance satisfying the claimed quantitative delta bound with equality yet giving zero analysis is a substantive, precise refutation of that transport criterion. It diagnoses the exact adjoint-range error and names the standard sharp operator-domination test. Such a correction is useful to researchers relying on the original theorem. Its intrinsic mathematical value is separate from novelty: the identical witness is already published for the controlled specialization and therefore the assigned scientific claim is rejected for O.

The dated certificate retains the supplied scientific assessment, sources and limitations.
