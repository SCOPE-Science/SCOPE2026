# A uniform predator-invasion ceiling excludes predator-positive compact recurrence
## Finding
For system (1.7) of Cao–Wang–Liu on \(\mathbb R_+^3\), assume \(A_1,A_2,A_3,A_4,B_1,B_2,B_3,B_4,C_1,C_2,C_3,K_1,K_2>0\), \(k_1,k_2\ge0\), \(0\le m_1,m_2\le1\), and \(q_iE_i\ge0\). Set \(R_1=A_1-q_1E_1\), \(R_2=B_1-q_2E_2\), \(M_1=K_1\max\{R_1,0\}/A_2\), \(M_2=K_2\max\{R_2,0\}/B_2\), \(D=C_3+q_3E_3\), and \(\Gamma=C_1(1-m_1)M_1+C_2(1-m_2)M_2-D\). If \(\Gamma<0\), then every compact invariant set is contained in the predator-free plane \(y=0\). Consequently every compactly supported invariant probability measure is supported on the equilibrium set of the predator-free planar competitive subsystem; in particular, no periodic, quasiperiodic, or chaotic compact recurrent dynamics can have positive predator density under this threshold.

This gives a global recurrence-exclusion criterion, not merely a local stability test at one predator-free equilibrium. The threshold is biologically interpretable: larger refuge fractions \(m_1,m_2\), larger predator mortality/harvest \(C_3+q_3E_3\), or smaller prey carrying ceilings all move the system toward the exclusion region.

## Assumptions and scope
The object is system (1.7) in Cao, Wang and Liu (2024):
\[
\dot x_1=x_1\left(\frac{A_1-A_2x_1/K_1}{1+k_1y}-A_3x_2-A_4(1-m_1)y-q_1E_1\right),
\]
\[
\dot x_2=x_2\left(\frac{B_1-B_2x_2/K_2}{1+k_2y}-B_3x_1-B_4(1-m_2)y-q_2E_2\right),
\]
\[
\dot y=y\left(C_1(1-m_1)x_1+C_2(1-m_2)x_2-C_3-q_3E_3\right).
\]
The state space is \(\mathbb R_+^3\). Coefficients \(A_i,B_i,C_i,K_i\) appearing above are positive, \(k_i\ge0\), \(0\le m_i\le1\), and harvest products \(q_iE_i\ge0\). No assertion is made that \(\Gamma<0\) is necessary for predator extinction or is a sharp parameter boundary for all forward solutions. The claim concerns compact invariant sets and compactly supported invariant probability measures.

## Proof
Let \(K\subset\mathbb R_+^3\) be compact and invariant. The ODE is locally Lipschitz on the nonnegative orthant, and a trajectory contained in compact \(K\) extends for all positive and negative times.

Let \(X_1=\max_K x_1\). If \(X_1>0\), choose a point of \(K\) attaining this maximum and follow its complete trajectory in \(K\). Since \(x_1\) has a two-sided local maximum there, \(\dot x_1=0\). Dividing by \(X_1\) gives
\[
\frac{A_1-A_2X_1/K_1}{1+k_1y}
=A_3x_2+A_4(1-m_1)y+q_1E_1\ge q_1E_1.
\]
Therefore \(A_1-A_2X_1/K_1\ge q_1E_1\), so \(X_1\le M_1\). If \(R_1\le0\), the same equality is impossible for a positive maximum, hence \(X_1=0=M_1\). Thus \(0\le x_1\le M_1\) on every compact invariant set. The identical argument yields \(0\le x_2\le M_2\).

Now suppose some point of \(K\) has \(y>0\). Positivity is preserved along its complete orbit, and
\[
\frac{d}{dt}\log y
=C_1(1-m_1)x_1+C_2(1-m_2)x_2-D
\le\Gamma<0.
\]
For \(t<0\), integration from \(t\) to \(0\) yields
\[
\log y(t)\ge \log y(0)-\Gamma(0-t).
\]
Because \(-\Gamma>0\), the right-hand side tends to \(+\infty\) as \(t\to-\infty\), contradicting compactness of \(K\). Hence every compact invariant set satisfies \(y=0\).

On that invariant plane the equations reduce to the competitive Lotka–Volterra system
\[
\dot x_1=x_1(R_1-s_1x_1-A_3x_2),\qquad
\dot x_2=x_2(R_2-B_3x_1-s_2x_2),
\]
where \(s_1=A_2/K_1>0\) and \(s_2=B_2/K_2>0\). In the open quadrant, the Dulac function \(B=(x_1x_2)^{-1}\) gives
\[
\frac{\partial(B\dot x_1)}{\partial x_1}+
\frac{\partial(B\dot x_2)}{\partial x_2}
=-\frac{s_1}{x_2}-\frac{s_2}{x_1}<0.
\]
Thus there is no periodic orbit in the interior; on either axis the dynamics are one-dimensional and have no non-equilibrium recurrent points. By the planar Poincaré–Bendixson alternative, every recurrent point of the predator-free subsystem is therefore an equilibrium. For any compactly supported invariant probability measure, Poincaré recurrence for the time-one map makes recurrent points full measure, so the measure is supported on the equilibrium set.

## Verification
The source PDF was inspected at the displayed system (1.7), its nonnegativity/boundedness section, and its local-stability condition (4.8) for the predator-free equilibrium. The algebraic ceiling argument above uses the exact signs of all terms in (1.7). The logarithmic predator identity is an exact division of the third equation by \(y>0\), and the Dulac divergence was independently re-expanded in the packaged checker. No finite simulation, numerical continuation, or enumeration is used as an infinite-time proof.

The source's equation (4.8) tests the predator invasion rate at one predator-free equilibrium. In contrast, \(\Gamma<0\) bounds that invasion rate uniformly over every compact invariant set using the coordinate ceilings \(M_1,M_2\), then excludes every predator-positive compact invariant set by a backward-time contradiction.

## Relationship to prior work
Cao–Wang–Liu establish nonnegativity and boundedness, enumerate equilibria, give local stability criteria (including (4.8) for \(P_6\)), prove a global-stability result for the interior equilibrium under separate hypotheses, and study Hopf bifurcation and numerically displayed chaos. Their paper does not state the compact-recurrence exclusion criterion above.

The closely related Wang–Zhai–Liu–Liu (2021) paper studies a lower-dimensional fuzzy refuge model and focuses on equilibrium stability and harvesting. Stochastic refuge/fear papers cited in the target article derive stochastic threshold/extinction statements for different stochastic objects. Those results do not imply the deterministic compact-invariant-set statement here.

## Limitations
The condition \(\Gamma<0\) is sufficient and deliberately uniform; prey competition and fear can reduce the actual prey levels below \(M_1,M_2\), so predator-positive compact recurrence may already be impossible outside this region. The theorem does not classify noncompact forward transients, does not give an optimal extinction threshold, and does not contradict the source's chaotic example because that parameter set does not satisfy \(\Gamma<0\). A residual literature risk remains that an unindexed paper on the identical weighted fuzzy system proves an equivalent global exclusion condition.

## References
1. X. Cao, Q. Wang, J. Liu, “Hopf bifurcation in a predator-prey model under fuzzy parameters involving prey refuge and fear effects,” *AIMS Mathematics* 9 (2024), 23945–23970. DOI: 10.3934/math.20241164.
2. Q. Wang, S. Zhai, Q. Liu, Z. Liu, “Stability and optimal harvesting of a predator-prey system combining prey refuge with fuzzy biological parameters,” *Mathematical Biosciences and Engineering* 18 (2021), 9094–9120. DOI: 10.3934/mbe.2021448.
3. H. Qi, X. Meng, “Threshold behavior of a stochastic predator-prey system with prey refuge and fear effect,” *Applied Mathematics Letters* 113 (2021), 106846. DOI: 10.1016/j.aml.2020.106846.
4. D. Sahoo, G. P. Samanta, “Impact of fear effect in a two prey-one predator system with switching behaviour in predation,” *Differential Equations and Dynamical Systems* 32 (2024), 377–399. DOI: 10.1007/s12591-021-00575-7.
