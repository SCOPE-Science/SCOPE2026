# Independent audit — SCOPE-20260910-012

## Scope
Independent review of `2026/09/10/012` at Git tree `fb884e319f151a0bffa88409c85c75c2db99e17a` for task `20cb4fb0f42f361f7a14d25d084c5c02`. The current `main` tree matched the assigned source snapshot, so the scientific assessment used the assigned package without a stale-tree substitution.

## Correctness
**PASS_WITH_REPRODUCIBILITY_DEFECT**

Independent recomputation gives q(a,b,0)=a^2-2ab+2b^2=(a-b)^2+b^2>0 for every nonzero integer pair, so the claimed absence of q<=0 normals in the n3=0 slice is correct.

Independent depth-6 mutation BFS reproduces 40 (B,C) seeds, depth counts {0:1,1:3,2:6,3:8,4:10,5:9,6:3}, 18 c-vectors, and exactly the eight claimed n3=0 B2 roots.

The committed replay scripts are not cleanly runnable by the RESULT.md commands from the record root: b2_exact.py and cvec_bfs.py write to output/artifacts while the committed files live under artifacts, and verify_target.py reads the same absent output/artifacts paths.

## Originality
**FAIL**

Fomin-Zelevinsky's finite-type classification identifies rank-2 exchange matrix [[0,2],[-1,0]] as Cartan type B2, so finiteness of the transverse rank-2 cluster algebra and its root-system description are classical consequences, not a new fixed-joint theorem.

The additional obstruction q(a,b,0)=(a-b)^2+b^2 is a one-line specialization of the displayed symmetrized Cartan form. The six-step cycle and finite F-polynomial data are explicit replays of this standard B2 case rather than a scientifically distinct construction.

## Scientific value
**FAIL**

After the J* slice is identified as B2, the headline obstruction is elementary and the enumerated cycle is a regression/certification datum. It does not establish a new scattering phenomenon, a new theorem beyond finite-type rank 2, or a result on the off-slice non-cluster walls where the stated frontier remains open.

## Reproducibility
Status: **reproduced_independently_with_committed_path_defect**.
- Algebraic q-form identity checked exactly.
- Rank-3 mutation BFS independently reimplemented: 40 seeds / 18 c-vectors / eight n3=0 roots.
- B2 six-step closure follows under the same mutation convention.
- Limitation: The committed RESULT.md replay commands do not reproduce cleanly without repairing output/artifacts path assumptions; this is a package defect independent of the mathematical rejection.

## Literature checked
- [Cluster algebras II: Finite type classification](https://arxiv.org/abs/math/0208229): Gives the complete finite-type classification by Cartan-Killing type; rank-2 |bc|=2 is the classical B2 finite case.
- [Positivity and canonical bases in rank 2 cluster algebras of finite and affine types](https://arxiv.org/abs/math/0307082): Develops rank-2 finite/affine cluster algebras explicitly, reinforcing that the finite B2 dynamics are established rank-2 theory.
- [Relation between f-vectors and d-vectors in cluster algebras of finite type or rank 2](https://arxiv.org/abs/1904.00779): Treats F-polynomial/f-vector structure in finite-type and rank-2 cluster algebras; the record's finite F-polynomial behavior is within established theory.

## Limitations
- This judgment does not say the fixed numerical tables are wrong; it rejects them as an original/value-bearing research finding and separately records the broken committed replay paths.

## Conclusion
The package is scientifically **failed** under the three-axis audit because at least one required axis fails. Relocate the complete original package atomically to the assigned failed path, preserving all original evidence. The relocation is a publication-status decision, not a claim that every underlying computation is false.
