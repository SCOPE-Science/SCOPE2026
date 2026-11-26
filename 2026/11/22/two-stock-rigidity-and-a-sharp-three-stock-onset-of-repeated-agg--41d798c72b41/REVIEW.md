# Independent mathematical audit

## correctness

PASS

Under r_i>q_iE and B_i>0 the normalized logistic solutions F_i=(1+c_i)/(1+c_i exp(-a_i t)) have positive denominators even for c_i in (-1,0). For two stocks, D is a constant multiple of F_1-F_2; equal catchabilities give identity. Otherwise clearing denominators gives H with H(0)=0. Unless H is identically zero, H' has at most one positive zero, including the equal-rate and equilibrium cases. Two additional roots of H, or one positive root with zero derivative, would contradict Rolle's theorem, so any positive intersection is unique and changes ordering. For the three-stock witness, independent exact reconstruction gave weights (48,12,-60) in 299D, the stated numerator P, its factor 12(z-1), and all 20 transformed coefficients, with two sign changes. The exact signs at z=1/100,1/3,9/10 are -,+,-; denominators are positive, and z=e^(-t) bijects positive times with (0,1). This gives exactly two distinct simple roots and two sign changes, not just crossings seen in a simulation. Replay: python3 /workspace/branches/independent-exact-4-5.py. The frozen checker was inspected, not executed. The result is about normalized levels, not slopes, for independent surviving stocks at constant effort; three stocks can, but need not, exhibit two reversals.

## originality

PASS

The two-stock reduction uses a standard exponential zero bound; neither that tool nor the aggregate CPUE model is claimed new. The supported distinct contribution is the model-specific sharp species-count onset, with an all-initial-state two-stock obstruction and a three-stock witness certified to have exactly two order changes. No verified comparator covers that combined claim. Direct full-text comparison of the closest fisheries paper was not possible, so this is a best-of-knowledge judgment rather than a priority determination.

## value

PASS

The minimum assemblage size permitting repeated reversals is a structural boundary for a widely used abundance proxy, not just a fit or simulation. The admissible witness has exactly two reversals, and the obstruction covers any positive starting abundance in the two-stock model. No claim about empirical frequency, interacting stocks, variable effort, or higher-stock maximum counts is needed for that distinction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
