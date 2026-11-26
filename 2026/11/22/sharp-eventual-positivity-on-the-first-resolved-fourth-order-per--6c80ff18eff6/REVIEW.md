# Independent mathematical audit

## correctness

PASS

The five shifts 0, ±1, ±2 are distinct, and expanding D−D²/12 yields the stated symmetric stencil with row sum zero. The two nonzero pairs of Fourier eigenvalues of D are (−5±√5)/2; applying d−d²/12 gives −α and −β with 0<α<β. Inverting the Fourier symbol using the two cosine values φ⁻¹/2 and −φ/2 gives the displayed three orbit entries. The diagonal is positive and the nearest-neighbor numerator is (1−u)+φ(u−v)>0 for 0<v=e^(−βt)<u=e^(−αt)<1. For the distance-two numerator F, F(0)=0 and F′(0)=5Q_{j,j±2}=−5/12. The function e^(αt)F′(t)=φα−(β/φ)e^(−(β−α)t) increases strictly from that negative value to a positive limit. Thus F has one strict minimum and then increases strictly to 1, crossing zero exactly once at positive T. The cyclic orbit sizes give ten negative or zero entries before or at T, respectively, and positivity thereafter; the identity at zero adds the isolated nonnegativity time. The physical factor h²/κ, Euclidean norm bound and mass conservation follow from the scaling and the symmetric spectrum. Independent Decimal bisection reproduced T=0.1030787110077426622381848633844554940… (python3 /workspace/branches/reproduce_decisive.py). Frozen verification code and its logged spectral and sampled checks were inspected, not executed or used as a global sign proof.

## originality

PASS

Known qualitative eventual positivity and stencil signs are credited. The distinct claim is the exact sharp five-node threshold, the unique positive crossing and the complete sign classification of the global semigroup. It is not an approximate bound, a one-step positivity interval or a stability threshold.

## value

PASS

Five nodes are the first periodic grid with an unaliased stencil, not an arbitrary finite slice. The sharp crossover and exact census give a concrete test of the difference between mass-preserving spectral stability and positivity for a standard higher-order heat discretization. An exact threshold with no sign reentry is useful as a solver benchmark and is not furnished by a qualitative convergence theorem or a late-time bound. The result makes no claim about sharp larger-grid thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
