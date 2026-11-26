# Independent mathematical audit

## correctness

PASS

At t=L/v_i the terminal lateral position has variance 2D_it, so its normal tail is erfc(β_i/√L)/2. Independence multiplies that tail by exp(−α_iL). Both factors are strictly decreasing in their own effective parameter for L>0, giving dominance, one-coordinate ties and an everywhere tie exactly as stated. In the strict conflict write J(L)=g(L)−δL with g=log(erfc(β₁/√L)/erfc(β₂/√L)). Comparing the Gaussian tail integral to the integral weighted by t/z proves the strict Mills bound; it gives (log Q)'=1/z−2z+2e^(−z²)/(√π erfc z)>0 for Q=z e^(−z²)/erfc z. Hence g'<0 and J'<−δ, so the unique crossing is transversal. g>0. At L→0, g=(β₂²−β₁²)/L+log(β₂/β₁)+O(L); at infinity g=2(β₂−β₁)/√(πL)+O(1/L). Thus g(L)/L decreases from ∞ to 0, and L*=inverse(g/L)(δ) tends to the correct ends. Multiplying δL*=g(L*) by √L* or L* gives respectively the weak- and strong-gap constants and both exponents for fixed β's. At the root, the partial derivatives in δ, β₁, β₂ have signs negative, negative, positive; J_L<0 gives the same signs for the sensitivities of L*. Swapping labels handles the other strictly conflicting case. Fresh 65-digit numerical check via mpmath bisection for β=(1,2) yields L*=3.2651971332625828 and shared success probability 0.04239078323849283 for α=(0.5,0.1); at δ=10⁻¹² and 10¹² the respective scaled quantities are 1.128562613218 and 3.0000012005652, close to 2/√π and 3. The β sensitivities were spot-checked. Replay cd /workspace && python3 review-evidence/reproduce.py 5; output review-evidence/5.txt. The bounded calculation is supplementary; frozen checker was inspected, not executed.

## originality

PASS

The supported distinct result is the joint classification and fixed-lateral-parameter two-regime scaling for survival through the deterministic gate multiplied by a terminal-side probability. Classical erfc, normal-tail ratios and reflection are not novel. Inspected ecology and transport results do not supply the joint exact claim.

## value

PASS

The observable is a natural minimal benchmark for two opposing access and survival mechanisms. Fixing the designs while varying reach makes exactly one switch, rather than any number of switches, a useful constraint; the two distinct limiting scales quantify how the location responds to weakening or strengthening the disadvantage. This is not an empirical river model, a first-settlement criterion, or a prescription for interventions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
