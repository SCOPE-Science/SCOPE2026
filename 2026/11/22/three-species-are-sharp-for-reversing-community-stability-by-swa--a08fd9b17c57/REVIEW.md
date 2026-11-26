# Independent mathematical audit

## correctness

PASS

At the feasible equilibrium x=1, substitution of the adjusted mu cancels the interspecies row sums and self regulation in the diagonal derivative as stated, leaving the within-species block D_L and off-species B_ij. With fixed finite S, diagonalizing the identical leading blocks separates a semisimple zero eigenspace from -(a+b). In these coordinates J_L has an O(1) slow block and fast block -(a+b)L I+O(1). At bounded eigenvalue parameter the fast inverse is O(1/L), so Schur reduction gives convergence with multiplicity to the compressed slow block; the other S eigenvalues diverge left. For v=(1,1) and w=(b,a)/(a+b), the within-species row sums contribute -2 and directed-pair sums (C_ij,-C_ij) give w^T B_ij v=delta C_ij. For S<=2 the zero-diagonal C has sign-symmetric spectrum, so swapping a,b preserves the limiting slow spectrum. The weight-six directed three-cycle has eigenvalues 6,-3±3sqrt(3)i, yielding a positive limiting real mode in the first orientation and strictly negative real parts after the swap. At L=50, decomposition into C eigenmodes with eigenvalue c gives the factor z^2+(202-c)z+400+(aL-bL-2)c. Exact independent matrix replay confirms both factorizations. In particular, the first orientation's positive-root quadratic is accompanied by the quartic with coefficients (1,410,43464,294968,779344); its Hurwitz minors (17525272,5038386704896) and coefficients are positive. This supplies the additional check needed for a hyperbolic saddle, not merely instability. In the swapped case the quadratic and quartic are Hurwitz with quartic minors (17290072,614449021696). The adjusted growth rates are negative in both. Replay and output: /workspace/branches/ea1e57e5-b313-42cc-a895-255210df5b61/record5_replay.py and record5_replay_output.txt in that directory. Frozen verifier inspected, not executed. The S<=2 obstruction concerns strict limiting verdicts under fixed coefficients and not arbitrary finite-L changes or behavior at a zero limiting spectral abscissa.

## originality

PASS

Spectral compression and the effect of stage structure on ecological stability are prior. The distinct supported content is a deterministic leading-rate-ratio mechanism under zero directed-pair stage sums, its sharp minimum species count for a strict limiting stability reversal, and the exact feasible finite-rate cycle. The closest exact balanced-stage and fast-turnover statements inspected use different parameters or hypotheses. This is a bounded priority assessment.

## value

PASS

The construction gives a minimal counterexample to predicting local coexistence stability from aggregate pairwise interactions alone when the two life-stage rates are fast but unequal. Its weighted slow matrix explains why the contrast disappears under equal rates, and the three-species cycle gives strict opposite verdicts already at a certified finite rate instead of a formal singular limit only. This is useful for interpreting aggregate stability diagnostics in this stage-exchange model, not a calibrated ecological prediction or a global persistence result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
