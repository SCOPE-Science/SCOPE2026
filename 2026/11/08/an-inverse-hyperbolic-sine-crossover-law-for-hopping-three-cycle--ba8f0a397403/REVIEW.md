# Review of the three-cycle crossover theorem

## Correctness

**PASS.** A direct expansion of the exact third iterate at the three half-grid sites gives a normalized return equation converging in the uniform \(C^1\) topology on every fixed compact rectangle to \(2(t-\sinh u)\). Its strict negative derivative establishes local existence and uniqueness, and implicit differentiation determines the singular parameter response. The multiplier comes from the derivative of the same exact return displacement, with an explicit uniform error. All bounds are for fixed rescaled detuning and sufficiently large steepness, and all three derivative factors remain positive and less than one. The accompanying standalone numerical implementation of the original recurrence checks 25 cases at high precision; the all-parameter conclusions rely on the written proof, not the numerical tests.

## Originality

**PASS in examined evidence, with residual priority risk.** The 2026 source studies the same EOS map and describes hopping near its three-cycle window but does not state a two-parameter inverse-hyperbolic-sine transition profile. The 2024 source proves fixed-rational attracting cycles and is therefore insufficient for the new singular detuning limit. The closest publicly published prior result determines half-grid locations and the multiplier at fixed rational parameters, matching the \(t=0\) slice, but says nothing about detuning of the same order as the exponentially small return displacement. The present claim explicitly incorporates this prior slice rather than reasserting it as novel. Semantic records searches covered hopping, EOS maps, three-cycles, the inverse-hyperbolic-sine profile and equivalent singular-layer wording, without locating a dominating theorem. Absence of a match is not proof of historical uniqueness; related singular perturbation literature remains a risk.

## Mathematical value

**PASS.** The dramatic parameter susceptibility in the motivating period-three bifurcation diagram is a natural quantitative gap, and a derivative estimate at the rational center alone cannot describe the nonlinear regime in which the parameter displacement matches the exponentially small restorative force. The explicit \(\operatorname{arsinh}\) crossover, its natural \(e^{-a/6}\) width, and the dependence of the local contraction gap on detuning characterize a complete physically and mathematically motivated singular layer rather than a routine parameter substitution. The theorem provides a reproducible asymptotic benchmark for small-period windows of steep interval maps.

## Closest literature and limitations

The closest paper is *Singular half-grid selection and exponentially weak attraction in rational EOS maps*, whose result at fixed \(b=1/3\) is compatible but does not quantify detuning. The motivating *Strange bifurcation diagrams* by Bielawski et al. describes extreme motion of three-cycles. The 2024 *Interval maps mimicking circle rotations* proves existence/attraction at fixed rational parameters. No global basin classification, full parameter-window width, uniform large-\(t\) limit, or independent priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
