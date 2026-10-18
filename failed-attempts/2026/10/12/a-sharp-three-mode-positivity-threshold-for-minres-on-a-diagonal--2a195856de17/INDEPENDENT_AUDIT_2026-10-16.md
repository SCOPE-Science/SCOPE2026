# Independent mathematical audit

## correctness

PASS

The k=1 residual minimizing scalar alpha=(b^T A b)/(b^T A^2 b)>0 yields a nonnegative first iterate for SPD A and b>=0. In dimensions <=2, MINRES reaches x=A^{-1}b at grade <=2 and inverse positivity for Stieltjes matrices preserves the cone. On diag(1,2,4), b=(1,1,e), exact 2x2 normal equations with moments (3+4e²,5+16e²,9+64e²,17+256e²) yield det=4(1+100e²) and third coordinate e(50e²-1)/(2(1+100e²)), negative exactly 0<e<1/sqrt(50). Independent SymPy recomputation also confirms x2=(22/25,109/200,-1/80) at e=1/10 and the connected tridiagonal Stieltjes witness x2,3=-900492530/220852842849 with positive exact solution.

## originality

FAIL

Decisive previously published theorem on exactly the same MINRES/Stieltjes object already proves strictly stronger condition-number frontier kappa<=2, sharp n=3/iteration=2, and contains identical numerical witness. Its all-kappa counterexample specializes to kappa=4 and e²<8/(256+144)=1/50: precisely the submitted sharp epsilon interval. Thus every presented novelty-bearing assertion is already an implication or literal special case; change of wording/extra irreducible witness cannot make the unchanged original novel.

## value

FAIL

Although its calculation and positivity counterexample are mathematically well motivated in isolation, the exact threshold, smallest dimension, first violating iteration, and even the specific witness are already explicit consequences of the stronger published Oct 4 theorem. No independently valuable new structural lemma, different invariant, or genuine extension remains in the unchanged final claim; reproducibility and an extra connected perturbation are not substantive new contributions to the central assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
