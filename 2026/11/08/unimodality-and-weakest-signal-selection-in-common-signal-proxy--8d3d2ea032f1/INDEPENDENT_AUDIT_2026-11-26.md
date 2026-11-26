# Independent mathematical audit

## correctness

PASS

The repaired RESULT.md gives the scope of the eventual unique optimizer in the Finding itself: a unique least-q state of fixed positive prior, fixed state parameters, and noninteger log-odds ratio. It replaces the original unqualified local-maximum statement with an exact global scan rule; e.g. in the admissible one-state case h=2, q=3/4, r=1/2, P_2(1)=45/64 while P_2(2)=P_2(3)=P_2(4)=1/2, so the dictatorship suffix can contain nonglobal weak local maxima. The pivotal gain with a correct expert is (1−q_s) times the mass at h−t−1 of the remaining direct votes; the loss with an incorrect expert is q_s times the mass at h. The binomial coefficients agree through t=h−1, and t≥h is constant by the strict vote threshold. In the sign comparison the positive and negative sums grow respectively at factors below and above 2, so a nonpositive increment is followed only by negative ones within the prefix. For fixed t the positive exponential base q_s(1−q_s) is largest at the unique least competence, and a finite T valid in all states makes the increment at T negative for all h>T, ruling out larger maximizers without exchanging limits. The resulting sign criterion t+2<α gives the stated floor and unique count. The below-half example reproduces its strict dip with the three exact fractions in the record. Frozen verify.py was inspected, not executed; the independent replay at branches/3cd852f1-36fa-4077-be18-bb8269947fc9/independent_check.py checked 5760 increments in 1280 rational environments, the counterexample, the rare-state signs for the three stated sizes, and the 11 noninteger scalar cases. The repaired VERIFICATION.md clarifies that the frozen program uses logarithms for cutoff selection and that the twelfth scalar pair is skipped; it preserves the original recorded output. These checks do not replace the proof.

## originality

PASS

The supported distinct claim in the repair is finite-state unimodality in the integer proxy count despite changing signs of the expert advantage, together with eventual selection by the unique least-q state in the fixed-prior noninteger regime. Prior coverage of the scalar cutoff and the initial one-edge increment is credited; neither alone covers the mixed-state result. The corrected scan and scope statements do not claim additional priority.

## value

PASS

A mixture of single-state objectives need not be unimodal. The strict separation of gain and loss growth establishes why it is here and yields a valid global scan despite the dictatorship plateau. Eventual control by a possibly very rare state identifies the optimizer, not just the limiting correctness, and the exact five-voter witness explains why the competence assumption matters. The repaired statement preserves these contributions without asserting an integer-tie rule or unwarranted local optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
