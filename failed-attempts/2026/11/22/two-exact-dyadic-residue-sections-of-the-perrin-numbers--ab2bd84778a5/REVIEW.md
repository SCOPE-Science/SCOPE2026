# Independent mathematical audit

## correctness

PASS

For the frozen companion matrix M, Cayley–Hamilton and its first three traces prove P_n=tr(M^n). The identities M^7=I+2B and M^14=I+4C can also be recovered from M³=M+I: B=M²+M and C=B+B². The decisive odd traces are tr(M^jB)=(P_(7+j)−P_j)/2=5,7 and tr(M^jC)=(P_(14+j)−P_j)/4=17,29, for j=1,3. For an odd index-parameter difference h, (M^(7h)−I)/2 is B mod two. For h=2^r w with r≥1 and w odd, the normalized quotient by 2^(r+1) is C mod two: squaring I+2^(r+1)C_r preserves C_r mod two after dividing, as does taking an odd power. The factor M^(7v) reduces to I, so the trace difference has exactly the claimed valuation for all pairs. Parity and injectivity on a block of 2^(k−1) parameters give complete even and odd sections. M mod two has order seven, and the valuation law with j=1 already forces any scalar period divisible by seven to be a multiple of 7·2^(k−1); the lifted matrix identity supplies the period, and the nonconstant seven-term parity cycle forces the factor seven. Repetition yields infinitely many index occurrences and density. Independently enumerated both sections and the first recurrence-state return for k=1 through 12. The frozen checker line 57 does not reduce the matrix power mod 2^k and by itself cannot rule out a half-period; the independent proof and first-return enumeration do not use that test.

## originality

FAIL

The exact collision law and the two sections follow by direct substitution in the separately indexed primitive Padovan recurrence theorem, not just from its headline surjectivity. Set u_0,u_1,u_2=(3,0,2), Q=M, e=(1,0,0). Its §§1–3 give the integer matrix quotients B and D=C for all index differences and give both isometric branches via b_j=d_j=1. At j=1 the state is (0,2,3), and at j=3 it is (3,2,5); eB and eD give (5,17) and (7,29), both odd. The two parities are even and odd, respectively. These are exactly the two general branches, with the same valuation law at arbitrary precision. Its full-state period is also the least period of the scalar sequence: a scalar period repeats all three consecutive coordinates, and a state period repeats the first coordinate. The same-day catalogue dates do not establish priority, but they do not remove the demonstrated stronger coverage.

## value

FAIL

Two exact sections for a named recurrence are a natural invariant, but in this record the whole claimed invariant and period are an immediate first-coordinate specialization of the already indexed primitive-seed mechanism, with the same matrix and leading quotients. The frozen assertion does not produce a distinct residue-fiber invariant beyond that implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
