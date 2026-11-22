# Reciprocal-deformation particle–hole conjugacy in \(K\)-exclusion dynamics

## Finding

In the periodic \((q,t)\) \(K\)-exclusion process of Ayyer and Misra, let \(G_{n,t,q}\) denote the continuous-time Markov generator in the sector of \(n\) particles on \(L\) sites, each with capacity \(K\). Define the involution on configurations by

\[
(\Theta\eta)_j=K-\eta_{-j},\qquad j\in\mathbb Z/L\mathbb Z.
\]

For every admissible configuration \(\eta\), every function \(f\) on the complementary particle sector, and all parameters specified below, the **full generators** obey

\[
\boxed{(G_{KL-n,t^{-1},q}f)(\Theta\eta)
=t^{2-2K}\bigl(G_{n,t,q}(f\circ\Theta)\bigr)(\eta).}
\]

Thus if \(X_s\) is the process with \(n\) particles and deformation \(t\), then \(\Theta X_{t^{2-2K}s}\) is *exactly* the process with \(KL-n\) particles and reciprocal deformation \(1/t\), at unchanged asymmetry \(q\), for every deterministic or randomized initial law transformed by \(\Theta\). The identity is a finite-time path-law statement, not merely an equilibrium identity. Every clockwise/counterclockwise successful jump maps to a jump with the same orientation on the reflected bond, with its rate multiplied by the same constant.

Consequently the entire generator spectrum, including multiplicities and Jordan structure, is multiplied by \(t^{2-2K}\) under this mapping. Stationary bond currents obey \(J_{KL-n}(1/t,q)=t^{2-2K}J_n(t,q)\); stationary marked jump-count distributions at time \(s\) in the dual system equal the appropriately bond-reflected distributions at time \(t^{2-2K}s\) in the original. When mixing times are defined by worst-start total-variation distance, \(T_{\mathrm{mix}}^{KL-n}(1/t,q;\varepsilon)=t^{2K-2}T_{\mathrm{mix}}^{n}(t,q;\varepsilon)\).

## Assumptions and scope

Let \(L\ge3\) and \(K\ge2\) be integers, \(0\le n\le KL\), \(t>0\), and \(q\ge0\). Occupations are \(\eta_i\in\{0,\ldots,K\}\), with \(\sum_i\eta_i=n\) and periodic indices. Put \([m]_t=\sum_{h=0}^{m-1}t^h\) for integers \(m\ge0\), including \([0]_t=0\). If neighboring occupations are \((a,b)=(\eta_i,\eta_{i+1})\), the clockwise hop \(i\to i+1\) has rate \([a]_t([K]_t-[b]_t)\), and the counterclockwise hop \(i+1\to i\) has rate \(q[b]_t([K]_t-[a]_t)\). Every attempted hop that has no particle at its source or no vacancy at its destination has zero rate. Generator conventions are \((Gf)(\eta)=\sum_{\eta'\ne\eta}r(\eta,\eta')(f(\eta')-f(\eta))\). Directed jump labels retain their orientation even when two events could lead to the same configuration (the restriction \(L\ge3\) also removes the two-site orientation ambiguity).

## Proof

**One-bond rate calculation.** The elementary identities

\[
[K]_t-[b]_t=t^b[K-b]_t,\qquad
[m]_{1/t}=t^{1-m}[m]_t\quad(m\ge1)
\]

hold for every \(t>0\) and remain valid in the boundary cases by the zero conventions. Under \(\Theta\), a clockwise hop from \(i\) to \(i+1\) maps to a clockwise hop from \(-i-1\) to \(-i\). Its old source–target occupations \((a,b)\) map to \((K-b,K-a)\). The mapped rate in the reciprocal-deformation process is exactly

\[
\begin{aligned}
&[K-b]_{1/t}\bigl([K]_{1/t}-[K-a]_{1/t}\bigr)\\
&\qquad=t^{b+1-K}[K-b]_t\,t^{1-K}[a]_t\\
&\qquad=t^{2-2K}[a]_t\bigl([K]_t-[b]_t\bigr).
\end{aligned}
\]

The same calculation for a counterclockwise hop gives the same multiplier, since the extra factor \(q\) is unchanged. Vacant-source and filled-target zero rates are mapped bijectively, including \(a=0\) and \(b=K\), because \(\Theta\) exchanges these two obstructions. The map is an involution and a bijection between the two state spaces, so it maps **all** marked off-diagonal transitions with the common factor \(c=t^{2-2K}\). The diagonal holding-rate entries match because each is the negative sum of the off-diagonal rates. This proves the boxed generator identity, including the one-state endpoint sectors.

**Finite-time implications.** Uniqueness of finite-state continuous-time Markov chains gives the semigroup identity \(P^{KL-n}_{s}(\Theta\eta,\Theta A)=P^{n}_{cs}(\eta,A)\) for every state subset \(A\). The exponential holding times and destination/mark choices can be coupled edge by edge with the same deterministic time change. This proves equality of marked jump paths after relabeling reflected bonds. Generator similarity up to the scalar \(c\) gives the spectral statement. Ergodicity of each nontrivial fixed-number sector yields a unique stationary law that is sent to the dual stationary law; the current and total-variation mixing identities follow by applying the same mapping to marked transition counts and worst-start distances. The stationary relation is therefore a consequence of the dynamic conjugacy, not an independent assertion.

## Verification

The independent, standard-library exact-arithmetic script `check_duality.py` enumerates every configuration for seven representative \((L,K)\) pairs and compares individual *marked* transitions at \((t,q)\) with the transformed transitions at \((1/t,q)\). Across 112 parameter/geometry cases it verifies 22,736 configuration involutions and 90,832 exact-rational marked transition comparisons, including both directional marks, \(q=0\), \(q=1\), \(q>1\), and nontrivial reciprocal deformation values. Run with `python3 check_duality.py`. The universal proof is the preceding algebraic bijection; these bounded finite checks are corroboration, not an exhaustive search over all ring lengths and parameters.

## Relationship to prior work

Ayyer and Misra (2023), Sections 2, 3.2, 3.3, and 6, define these rates, prove stationary particle–hole symmetry and reciprocal-\(t\) invariance of stationary weights, and explicitly explain why either transformation alone does not preserve the dynamics. Their discussion does not give the **combined complement–reflection–reciprocal-parameter generator conjugacy** with the deterministic time factor. The published exact finite-density current-asymmetry theorem (2026) supplies a different comparison at **fixed** \(t\) between \(n\) and \(KL-n\), but does not state or imply the finite-time, reciprocal-\(t\) process conjugacy. Evans and Waclaw (2013) develop general factorized misanthrope-rate constructions, which underlie the model's stationarity but do not establish this parameter-and-density transformation.

The algebraic rate identity is short once the correct combined transformation is specified. Its mathematical content lies in recovering a full generator/path-space relation from two individually broken dynamical symmetries; the previous stationary formulas alone cannot determine such a path-law identity.

## Limitations

The theorem requires homogeneous nearest-neighbor rates on a periodic ring and simultaneous changes of density and deformation strength. It does **not** say that \(t\mapsto1/t\) or particle–hole transformation alone preserves trajectories, nor that complementary densities at the *same* nonunit \(t\) have the same current. No closed-form evaluation of arbitrary eigenvalues or current fluctuation cumulants is claimed; only the exact dual correspondence is proved. Open reservoirs, site-dependent rates, and other deformed inclusion/zero-range models are not covered. An implicit occurrence of this combined identity in less accessible literature cannot be excluded without independent priority assessment.

## References

1. A. Ayyer and S. Misra, *An exactly solvable asymmetric K-exclusion process*, arXiv:2310.03343, first posted 2023-10-05, https://arxiv.org/abs/2310.03343; especially Sections 2, 3.2–3.3, and 6.
2. M. R. Evans and B. Waclaw, *Condensation in stochastic mass transport models: beyond the zero-range process*, arXiv:1312.5642, first posted 2013-12-19, https://arxiv.org/abs/1312.5642; Sections 2–3.
3. *Exact finite-density current asymmetry and displaced maximum in deformed exclusion*, published 2026-10-18, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-exact-finite-density-current-asymmetry-and-displaced-maximum-in--374c69430160/RESULT.md.
