# Independent mathematical audit

## correctness

PASS

This assessment is for the corrected RESULT.md, verify.py and VERIFICATION.md under repairs/5. The frozen text attributed the integral against G to the preprint's I_2, reversed the ROC density ratio and its quantile argument, and described a radial cutoff as already specified by the displayed source test. The repair gives both orientations explicitly and states the radial implementation using the verified Section 5.1 normalization. For the repaired proof symmetry gives both Mann–Whitney tail orientations 1/2; on the positive half-line J(F,G)=P(|X|<|Y|) and J(G,F)=1-J(F,G). Independent equal-variance Gaussian sum and difference give the central/outer comparisons 1/2-2q_s^2 and 1/2+2q_s r_s; the affine weight has a unique zero at w_s. Strict concavity gives q_s<r_s<3q_s, so the weights are positive and the variances differ. The two-interval event yields the claimed 1-4 Phi(-1/(2s)) TV lower bound and the positive densities force TV<1 at all fixed s. For the explicit radial rule the true ROC slope g_s(F_s^(-1)(t))/f_s(F_s^(-1)(t)) is bounded on compact quantile intervals. Both coordinates are exactly centered at their null values, so after the fixed-ratio CLT and null scaling the limiting centered Gaussian has positive mass inside every fixed positive-radius ball and zero mass on its boundary, proving non-consistency. The proof concerns fixed s, not a moving alternative. Inspected the frozen VERIFICATION.md and verify.py without running the uploaded code; the replacement's replay path is python3 verify.py with SciPy/NumPy, for the six widths actually specified, checking both oriented integrals. The infinite and asymptotic statements are analytic.

## originality

PASS

The repaired distinct claim is the exact all-width Gaussian tuning with distinct variances and a maximal TV supremum within the positive analytic class, despite both median-split orientations and the Mann–Whitney effect being null. The rank functionals, reciprocity, CLT and general non-omnibus behavior are explicitly credited. The checked antecedents do not establish the quantitative null-fiber claim.

## value

PASS

A concrete analytic unequal-variance family that is exactly invisible to the two rank-effect coordinates while approaching maximal distinguishability in total variation is a meaningful boundary of the intended two-sample summary, stronger than knowing the procedure is not omnibus. It quantifies the blind region at arbitrary small noise and does not imply a blind region for full-distribution tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
