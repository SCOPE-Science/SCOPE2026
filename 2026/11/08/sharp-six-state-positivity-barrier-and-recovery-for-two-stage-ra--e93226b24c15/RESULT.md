# Disconnected positive-step windows for two-stage Radau IIA on the directed eight-cycle

## Finding

On the unit-rate one-way eight-cycle, let \(P e_j=e_{j+1\bmod 8}\) and \(Q=P-I\), acting on column vectors. The two-stage Radau IIA endpoint \(T(h)=R(hQ)\), where \(R(z)=(6+2z)/(6-4z+z^2)\), preserves total mass for every \(h\ge0\). The matrix is strictly entrywise positive at \(h=2\) and at \(h=20\), but has a negative diagonal at \(h=4\). Thus \(\{h>0:T(h)\ge0\text{ entrywise}\}\) has at least two connected components with nonempty interiors. Recovery from the initial small-step positivity failure need not be permanent, even on a directed cycle with just one outgoing edge per vertex and identical jump rates.

## Assumptions and scope

The step \(h\) is dimensionless; for a common rate \(c>0\), the dimensionless step is \(c\) times the physical time step. This statement concerns the endpoint, not the internal stages. It does not give the number or endpoints of all the windows or claim that eight is the smallest size exhibiting this behavior.

## Proof

Set \(D=6I-4hQ+h^2Q^2\) and \(U=6I+2hQ\). The poles \(2\pm i\sqrt2\) lie in the open right half-plane, whereas \(hQ\) has eigenvalues \(h(\zeta-1)\) for eighth roots of unity \(\zeta\). Hence \(D\) is invertible and \(T=D^{-1}U\) depends continuously on \(h\ge0\). The identity \(\mathbf 1^{\mathsf T}Q=0\) gives \(\mathbf 1^{\mathsf T}T=\mathbf 1^{\mathsf T}\). Both \(D\) and \(U\) commute with \(P\); therefore the columns of \(T\) are cyclic shifts of its first column \(x=T e_0\).

Writing \(x_j=m_j/d\) with \(d>0\), the equation \(Dx=U e_0\) is the integer recurrence (indices modulo eight)
\[
(6+4h+h^2)m_j-(4h+2h^2)m_{j-1}+h^2m_{j-2}
=d\big[(6-2h)\mathbf 1_{j=0}+2h\mathbf 1_{j=1}\big].
\]
The following rows satisfy this equality by direct substitution, so invertibility proves that each is the indicated first column:

| \(h\) | \(d\) | \((m_0,\ldots,m_7)\) |
|---:|---:|:---|
| 2 | 2058973 | (231813, 660978, 536022, 329580, 173844, 81288, 33624, 11824) |
| 4 | 339145563 | (−5703833, 56028956, 73175032, 68840480, 56145856, 41935616, 29330944, 19392512) |
| 20 | 1666416340218976267 | (127548251905668327, 165339419304006540, 194402033385305400, 215921855262276000, 230967940898520000, 240500094415200000, 245376351288000000, 246360393760000000) |

Thus the first and last rows give positive neighborhoods of 2 and 20, respectively, and the negative diagonal excludes 4 and a neighborhood. Every connected subset of the real line containing 2 and 20 contains 4. The two positive neighborhoods therefore lie in distinct components. For context, the known small-step negative entry at displacement five has leading coefficient \(-h^5/108\), so \(h=0\) is isolated and is not responsible for the separation proved here. The known convergence to the uniform projection follows from \(R(0)=1\) and \(R(z)\to0\) on the other seven spectral rays; it does not prevent the finite-step loss at \(h=4\).

## Reproduction

The exact integer rows in `certificate.json` are checked by `python3 verify.py` (Python standard library), including the recurrence at every cyclic index and the signs. See `verification_output.txt`. The rows are also displayed above, so the argument does not require a floating-point calculation or a step-size grid.

## Relationship to prior work and limitations

The six-state barrier, the complete six-cycle recovery threshold, the positivity of smaller cycles, and the small-/large-step asymptotics for every larger cycle are established in *A six-state threshold and positivity recovery for Radau IIA on directed cycles* ([Resultary 1260be3011dc](https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-a-six-state-threshold-and-positivity-recovery-for-radau-iia-on-d--1260be3011dc/RESULT.md)); see also [d6e23c144dbb](https://github.com/Resultary/2026/blob/main/2026/10/27/SCOPE-six-states-are-the-sharp-small-step-positivity-barrier-for-two-s--d6e23c144dbb/RESULT.md) and [24a51aae20d9](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-sharp-six-state-recovery-of-markov-positivity-for-radau-iia-on-d--24a51aae20d9/RESULT.md). Those claims are background, not part of this contribution. The same method has disconnected windows on undirected stars ([Resultary 17146a0a41df](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-three-disjoint-positivity-windows-for-two-stage-radau-iia-on-sta--17146a0a41df/RESULT.md)), while the two-stage Gauss–Legendre \([2/2]\) map on the same directed eight-cycle has one bounded positive-step window ([Resultary 6e27618b0571](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-exact-stochasticity-reentry-for-fourth-order-gauss-stepping-on-t--6e27618b0571/RESULT.md)). Neither mechanism specifies two separated positive-step intervals for the subdiagonal \([1/2]\) map on a one-way cycle. This comparison is targeted and does not establish historical priority against unindexed work.
