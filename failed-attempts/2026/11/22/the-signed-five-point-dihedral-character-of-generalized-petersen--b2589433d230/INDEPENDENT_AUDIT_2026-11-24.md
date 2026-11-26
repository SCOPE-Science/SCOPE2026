# Independent mathematical audit

## correctness

PASS

Kim's Theorem 4.6 gives the asserted rank four concentrated in degree 3q-1 for n=5q, and the exact sphere types for other d>=5. A setwise fixed independent face is a union of j compatible vertex cycles; for m original vertices its orientation sign is (-1)^(m-j), so including the empty face the reduced Lefschetz number is -I_Q(-1). For a rotation the residue classes modulo d=gcd(n,s) give the two-layer quotient, discarding internal loops. The d=1,2,3,4 evaluations are 1,-1,1,-1; in d=4 the empty outer choice contributes +1, singletons 0, and both opposite pairs -1 each. An independent exact eight-state transfer calculation (audit-checks/petersen.py) finds the characteristic polynomial z^4(z^4-z^3+z^2-z+1) and gives the same orbit evaluations in every period; its four nonzero eigenvalues are -zeta_5^j. For larger d the parity of Kim's sphere dimension gives the same formula. Multiplying by (-1)^q to pass from -I_Q(-1) to the lone homology trace gives the signed rotation law: 5 divides d precisely if 5 divides s, and d and s have the same parity when n is even. The four rotation eigenvalues on homology are epsilon_n(r) times the nontrivial fifth roots; inverses are distinct, so a reflection interchanges the paired eigenspaces and has zero trace. Rational semisimplicity and character equality give the stated isomorphism. None of the rotation eigenvalues is 1. After equivariant barycentric subdivision there are no inversions, and rational orbit chains give coinvariants, canonically isomorphic to invariants by averaging; this proves the quotient conclusion even for a nonfree action.

## originality

FAIL

Resultary 6056ae77d731 is a distinct same-day catalog record with demonstrated mathematical coverage: it gives the complete rational character for the same canonical dihedral action on the same graph family for all n>=5 and explicitly gives rational quotient cohomology. The n=5q restriction specializes without additional hypotheses to every claimed trace and the acyclic quotient. Stating this character as the signed inflated augmentation of the five-point action is a direct character calculation, and the rotational invariant assertion follows immediately by averaging the specialized character or reading its roots. The date does not settle within-day priority, but it does not negate equivalent coverage.

## value

FAIL

The uniform character is a natural worthwhile invariant, but the reviewed version restricts an already available all-n solution to the easiest nontrivial homology-rank family. The signed augmentation description and reflection eigenpair argument are useful exposition; the representation, invariant-space consequence and rational quotient are all mechanical consequences of the broader character. No standalone material gain is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
