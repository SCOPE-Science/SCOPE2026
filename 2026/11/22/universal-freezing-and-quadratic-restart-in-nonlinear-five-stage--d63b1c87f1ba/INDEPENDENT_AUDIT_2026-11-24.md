# Independent mathematical audit

## correctness

PASS

For the exact-subflow composition and fixed-step minus correction specified in RESULT.md, direct differentiation gives [f1,f2]=(-gamma omega V',-gamma omega x) and [f1,[f1,f2]]=gamma² f2. The sign is also consistent with the linear cubic-order term: to first order in omega for the quadratic oscillator the uncorrected (2,1) entry has factor omega h times the average of exp(-gamma h/6) and exp(-5 gamma h/6), whose quadratic coefficient in h is 13 gamma²/72 instead of the exact integral coefficient 12 gamma²/72. The negative correction removes that discrepancy. At h*=6 sqrt(2)/gamma the two corrected conservative stages are identities, and damping stages add to h*, yielding the entire fixed line and the claimed iterates. Continuous energy sublevels are compact; the only invariant part of x=0 has V'=0 and hence y=0, so LaSalle gives global attraction. For positive h the damping stages decrease energy and both conservative stages preserve it for either time sign (compact Hamiltonian levels give completeness). Near h*, each conservative stage has signed duration s=omega h(1-gamma² h²/72)/2 with s'(h*)=-omega. Starting at (0,y0), the first stage contributes -s²V'(y0)/2 to y; the second contributes another -s²V'(y0)/2 and the drift from momentum -exp(-2 gamma h/3)sV'(y0). This gives the stated two-sided O(|h-h*|³) expansion for each fixed y0. For u=exp(-gamma h/6), phi=s sqrt(kappa), multiplying the linear stages gives determinant u^6 and characteristic polynomial at 1 equal to (1+u²)(1+u⁴)sin²(phi), with derivative at 1 tending to 1-u_*^6>0. Moving the simple root near 1 therefore gives the coefficient in the Finding; the other root stays near exp(-6 sqrt(2)) and is strictly smaller in modulus, so the slow root determines the spectral radius. This does not give a global nonlinear rate away from h*. VERIFICATION.md, verify.py, and requirements.txt were inspected, not executed; the quoted symbolic/numerical tests do not authenticate the published scheme or prove its all-potential conclusions. Analytic replay is RESULT.md §§1–4 and the polynomial-at-1 calculation above.

## originality

PASS

The distinct assessed contribution is the sharp quantitative finite-step phenomenon for the specified 5C method: an all-potential fixed line at the cancellation, the nonlinear restart with an explicit coefficient and the sharp two-sided local slow multiplier, despite nonincrease of energy. The five-stage construction, conservative correction and energy monotonicity are antecedent. Exact cancellation alone is an immediate consequence once the double-bracket scalar is given, not an independent priority claim. The earlier RK4 resonance is closely analogous for the same linear oscillator at kappa=1, but concerns a different method and a different detuning statement. Verification of the published original 5C passages was impeded by access, so the scientific assessment is bounded by the exact method supplied and the retrieved comparisons, not a certification of the bibliographic attribution's details.

## value

PASS

Energy nonincrease is weaker than attractivity for a rank-one damped integrator. The exact potential-independent fixed line, contrasted with global continuous attraction, identifies a concrete large-step failure. The nonlinear drift and slow multiplier quantify deterioration arbitrarily close to it on either side and distinguish this from a one-off finite test or a mere substitution in a correction formula. The statement does not recommend this step for accurate integration or assert a global rate off resonance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
