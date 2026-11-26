# Independent mathematical audit

## correctness

PASS

Character orthogonality after substituting a=2b-z gives F_chi F_psi=|A| F_(chi inverse) exactly when psi=chi^(-2), otherwise zero. Since |A| is odd and invertible, the character basis and inverse-square permutation are valid. A fixed character has cube one; a character fixed by the square of the permutation also has cube one, so all remaining cycles have length at least three. The commutators have zero fixed-character outputs; individual basis commutators span every other output and those outputs span a subalgebra. For a cycle of length three use cyclic relabeling to make a nonzero prescribed c_0 first, then vectors (1,0), (0,c_0), (-c_1/c_0,-c_2), or zeros if all targets vanish. For a longer cycle, shorten it by replacing the final two targets with a closing edge of determinant one; insert c_last times the last old vector plus c_penultimate times the first old vector. Its two determinants are the original two prescribed values, including in characteristic two. Apply this independently to the cycles with targets given by the desired inverse-character coefficients divided by |A|, and the resulting two Fourier expansions give one bracket. The dual group has |A[3]| elements of order dividing three, making the derived dimension and exact width as stated, including A trivial and finite-field splitting e dividing q-1. Independently enumerating the images of actual vectors gives every determinant list over F_2 in lengths 3–10 and F_3 in lengths 3–6 (checks/frozen_checks.py argument 2, checks/2.txt); this is finite corroboration of the lemma only.

## originality

FAIL

A distinct available Resultary finding records the exact theorem under the same hypotheses, with the same Fourier-cycle reduction and the same arbitrary-field cycle determinant surjectivity lemma. It is not just an overlap in the linear commutator subalgebra or finite tables. The different proof of that intermediate lemma in the frozen record does not distinguish the stated width theorem. This is a finding of equivalent published coverage for the claim now under review, not a finding that the distinct later-dated catalogue entry had earlier priority, or a finding of derivation or copied work.

## value

PASS

As a mathematical result this determines a motivated width invariant for arbitrary finite abelian groups in the split odd-order regime and gives witnesses, rather than only computing a known linear span. The determinant existence argument works over all fields, while the application is correctly limited to splitting fields. This scientific usefulness is distinct from the lack of a nonduplicated stated theorem in the available corpus.

The dated certificate retains the supplied scientific assessment, sources and limitations.
