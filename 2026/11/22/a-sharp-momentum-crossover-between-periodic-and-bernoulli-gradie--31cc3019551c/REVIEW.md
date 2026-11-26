# Independent mathematical audit

## correctness

PASS

For the scalar recurrence with one active step in a fixed period m≥2, the product has determinant β^m and trace 1+β^m−τ(1−β^m)/(1−β). Cyclic phase shifts preserve both even when β=0. The strict second-order Jury conditions yield exactly the asserted periodic ceiling; the upper endpoint has eigenvalue −1 and the lower one has +1. Bounded intra-period products pass geometric convergence to every iteration. For iid probability p=1/m, let a=1+β−pτ and v=p(1−p)τ². The exact covariance action has rows (a²+v,−2βa,β²), (a,−β,0), (1,0,0) and det(I−T)=pτ[2(1−β²)−τ(1+β−2pβ)]. Below the ceiling, the proposed H has positive diagonal and det H>0 for β>0 since pτ<2(1+β), and the expected drift is a negative multiple of x_k². Summing proves mean-square convergence; β=0 instead has exact scalar second-moment multiplier 1−2pτ+pτ². At or above the upper ceiling T has a real eigenvalue ≥1; the covariance vectors from (1,0),(0,1),(1,1) span the real symmetric covariance space, so not every deterministic start converges. The positive prefactor multiplying G_m(β)−1 in the difference of the ceilings gives one strict interior root and the stated sign directions (with equality also at β=0). Bernoulli's inequality gives b_m<1−1/m; on this domain the factor mz²+2z−m in G_{m+1}−G_m is negative at b_m, proving strict increase. Taking logs in b_m^m=1/(m/b_m+m−1), with b_m≥√2−1, first gives 1−b_m=O(log m/m), and reinsertion gives the claimed error order around log(2m)/m. The two exact roots and the displayed sign examples agree with the formulas.

## originality

PASS

The iid-erasure ceiling is already exactly covered, and a catalogue result supplies closely related period-two monodromy. The frozen contribution explicitly excludes priority on either ingredient and instead compares the two schedules at matched active frequency for every m, with an ordered system of sharp reversal boundaries and their asymptotic. The inspected sources do not provide or imply that full comparison by substitution.

## value

PASS

Matching the active frequency removes a simple confounder and leaves a qualitative reversal: neither periodic nor iid scheduling has the uniformly larger admissible active step in this benchmark. The exact threshold tells where the ordering changes, and how close to unit momentum the change is forced as delivery becomes sparse. That exact comparison and trend are useful to design or interpret scalar benchmarks and do not require asserting novelty for the iid ceiling or ordinary stability machinery.

The dated certificate retains the supplied scientific assessment, sources and limitations.
