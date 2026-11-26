# Independent mathematical audit

## correctness

PASS

The stated normalized windows give squared radial ambiguity multipliers e^(−s) and e^(−s)L(s)^2. The factorization L²−1=s(s−4)(s−2)²/4 forces the Gaussian optimum before 4 except at T=2, where the pointwise inequalities give the exact interval [0,η]. With u=2−s the threshold function is 4∫_0^1 e^(−tu)dt/[u(2−u)(2+u)]; its log is strictly convex in 0<u<2, so the interior minimizer can be found by a single stationarity equation. At s=4 all weights agree. The derivative there is e^(−4)(4w−1), and the w=1/4 derivative factorization proves the plateau and specifies its exit on the descending branch. This gives the whole optimizer interval at T=4 and strict uniqueness on 4<T≤T_*. Thereafter reflection about s=2 and the monotonicity of D on (2+√2,4) locate the inner minimum. The outer interval has endpoint minimum, so the strictly decreasing inner envelope and increasing outer endpoint as functions of w cross exactly once. For every s≥T_*>8, D(s)≤D(8)=−84, so F_w(T) strictly decreases in T for all w and the crossing moves strictly to the right. Near w=1 the inner active radius differs from 2+√2 by O(1−w); hence the inner envelope has leading term e^(−2−√2)(1−w), which proves both large-T limits. Independent bounded reproduction yields η=0.745182361841, T_*=8.83273551863978 and, at T=10, w=0.388201417353 and Γ=0.016964744328. Replay: branches/9b32dbc9-4bef-407a-b999-18e9a72e28fa/reproduce.py and reproduce-output.txt. Numerical samples are corroboration only. Frozen CHECK.py and VERIFICATION.md were inspected, not executed. The result is pointwise linear conditioning, not global nonlinear stability.

## originality

PASS

The distinct contribution is the exact finite-radius optimizer diagram for the Gaussian/second-Hermite restriction, particularly the protected plateau and exit. The high-radius law is already covered by the inspected general two-Hermite catalogue result; no distinct originality credit is given to that law. The conclusion is a bounded judgment, not a date-based priority inference.

## value

PASS

For these two natural normalized windows, the exact design identifies a range of disk sizes where enlarging the disk costs no worst-case gain and fixes the unique precision split that achieves that property. The exit and the exact equalization beyond it directly answer a continuous conditioning-design question not settled by coverage maps or asymptotics. No global nonlinear recovery claim is needed for this value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
