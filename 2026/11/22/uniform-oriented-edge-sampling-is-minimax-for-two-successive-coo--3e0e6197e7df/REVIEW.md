# Scientific review

## Correctness — PASS

The exact two-update quadratic loss is \(a_i^2+(a_j-H_{ji}a_i)^2\) with \(a=Hx\). The constant mode bounds every joint law and forces edge support in an optimum; uniform oriented-edge sampling has a shared-eigenbasis loss whose exact nonnegative factorization proves sharp attainment. Connectedness makes the worst direction unique. Reproducibility: run `python3 verify.py`; 45 exact-rational graph/coupling checks passed. Finite checks supplement but cannot replace the analytic proof.

## Originality — PASS (qualified)

published-finding corpus searches on ordered sequential coordinate pairs, regular graph Hessians, and edge sampling were compared with the full accessible prior cyclic-block theorem and three relevant primary full texts. The closest theorem optimizes one *simultaneous* two-coordinate block projection, whereas the present result optimizes two successive singleton minimizations over **all** ordered laws. Algebraic formulas differ even on a cycle; full-permutation and volume-sampled block methods likewise do not imply this exact statement. A historical general alternating-projection theorem may subsume the statement and requires independent priority research.

## Value — PASS

A globally optimal local schedule follows from the interaction graph for a natural family of screened graph quadratics, with no imposed marginal or edge restrictions. On sparse cycles the guaranteed two-update squared-energy decrease is asymptotically 62.5% larger than that of independently structured distinct-pair sampling in a strong-coupling limit. This quantifies a real sampling-choice boundary, not a wall-clock or long-run speedup.

## Limits and closest sources

Connected simple regular graphs, strictly subcritical positive interactions, normalized exact coordinate updates, and a state-independent pair law. Other edge-supported optimal distributions are not excluded. Consult Tu et al. (arXiv:1701.03863), Rodomanov–Kropotov (arXiv:1904.04587), Wright–Lee (arXiv:1706.00908), and the publicly accessible cyclic-block Gauss–Seidel research result. Bibliographic completeness and external validation are not claimed.

Self-review: passed. Independent audit: not yet performed.
