# Independent mathematical audit

## correctness

PASS

The realizability dichotomy and the characteristic-two local normalization specified in the proof are correct. For q=2^f, restricting scalars on the nilpotent strictly upper triangular algebra N gives an F₂-algebra. In R=F₂I⊕N only the elements I+X can be units, and their inverses are the finite geometric sums in X; N is nilpotent, the nonunits are exactly N, R/N=F₂ and |R|=2q^(n(n−1)/2). More generally a finite characteristic-two local realization of a 2-group has residue a finite field of characteristic two whose unit group is an odd-order quotient of the 2-group; thus that field is F₂ and |R|=2|R×|. This is the scope of the bound in the proof (line 140), not an unrestricted minimum over local rings of arbitrary characteristic: UT₂(2)=C₂ already has the smaller local realization F₃. For odd p and n≥3 the factors I+E₁₂ and I+E₂₃ fail to commute by the E₁₃ term. The odd-order theorem rules these groups out; at n=2 the additive field is C_p^f and Ditor's criterion applies, with explicit realization (F_{2^a})^f for p=2^a−1. Independently, an odd-order unit group forces −1=1, hence characteristic two; the subgroup 1+J(R), of 2-power order, must be trivial. The finite semisimple ring is then a product of matrix rings over fields of characteristic two, with no matrix block of size at least 2 since its units would contain an involutory transvection. If every factor has unit group of p-power order, a nontrivial factor satisfies 2^a=p^e+1, which forces e=1: even e gives 2 mod 8, and odd e>1 produces a proper odd divisor (p^e+1)/(p+1). Thus the relevant unit group is elementary abelian at a Mersenne prime. The n=1 case is trivial as stated. The bundled finite checker was inspected, not executed; the proof is symbolic.

## originality

FAIL

The classification is covered by standard algebra-group/unitization and odd-primary realizability results applied directly to the defining matrix algebra, even though the bounded search did not find this exact family statement word for word. On the even side, UT_n(q) is its defining algebra group 1+N; viewing N as a nilpotent F₂-algebra, its ordinary unitization has that group as its entire unit group because F₂× is trivial. The local residue and factor of two are the usual normalization. On the odd side, the published classification applies immediately once n=2 and n≥3 are distinguished by one matrix-product check. No new obstruction or realization beyond these direct implications is shown.

## value

FAIL

A unit-group classification of a natural linear family is a reasonable question, but here the defining algebra is already the even-field realization after ordinary unitization, and the complete odd-field answer is an immediate case of the known odd-order theorem. The characteristic-two size is standard normalization, and the small replay tests add no fact about the general family. This is a useful example collecting known mechanisms, not a distinct structural result or a non-mechanically implied classification warranting a validated finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
