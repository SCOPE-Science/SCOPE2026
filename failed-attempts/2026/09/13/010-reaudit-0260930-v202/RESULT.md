# Milnor–Tjurina gap and matrix-factorization Hochschild dimension for a Newton-nondegenerate surface singularity

## Context
Let U=A^3_C with coordinates x,y,z and
f=x^5+y^6+z^7+x^3y^2z.
The derived critical locus dCrit(f) is the (-1)-shifted symplectic derived intersection of the zero section and graph(df) in T^*U.

## Result
At the origin:
- f is convenient and Newton-nondegenerate; its only compact Newton face is the Fermat face through (5,0,0),(0,6,0),(0,0,7), because (3,2,1) lies strictly above that face.
- The local Milnor number is μ=120. Kouchnirenko gives ν=210-107+18-1=120, and the local weighted standard basis has standard monomials x^a y^b z^c with a≤3,b≤4,c≤5.
- The local Tjurina number is τ=101, so μ-τ=19. The germ is not quasihomogeneous; equivalently f∉Jac(f).
- The total affine Jacobian algebra has dimension 136. Besides the origin there are exactly 16 distinct critical points, all Morse, so their local Milnor numbers contribute 16.
- Hess(f)(0)=0 and vdim dCrit(f)=0.
- The Milnor fibre at 0 has Euler characteristic χ(F)=1+μ=121, and the Behrend function value of Crit(f) at 0 is (-1)^3(1-χ(F))=120.
- For the dg category MF(f) of matrix factorizations of this isolated hypersurface germ, the standard Hochschild-homology computation identifies HH_*(MF(f)) with the Jacobian algebra up to the usual grading/parity convention. Hence its total complex dimension is μ=120. Thus the numerical equality dim HH_*(MF(f))=ν_Crit(f)(0)=120 holds. This is a numerical equality of two invariants, not an identification of Hochschild homology of the derived critical locus itself with the Behrend function.

## Independent algebra checks
Exact Groebner calculations over Q give Jacobian colength 136 and Tjurina colength 101. The lexicographic Jacobian basis contains z^20+(13671875/81)z^12, giving z^12(81z^8+13671875); the 16 nonzero solutions are distinct. Since the origin contributes μ=120, each nonzero point has local Milnor number one.

## Reproducibility
The repository scripts are `artifacts/local_buchberger_qq.py`, `artifacts/global_jac.py`, and `artifacts/global_tjurina.py`.

## Limitations
The explicit arithmetic is for this germ only. No Arnold-modality classification is claimed. The Hochschild statement concerns the matrix-factorization category MF(f), not the structure sheaf or Hochschild homology of dCrit(f) as an unspecified derived stack.

## References
- A. G. Kouchnirenko, *Polyèdres de Newton et nombres de Milnor*, Invent. Math. 32 (1976).
- K. Saito, criterion for quasihomogeneous isolated hypersurface singularities.
- T. Dyckerhoff, *Compact generators in categories of matrix factorizations*, arXiv:0904.4713.
- K. Behrend, *Donaldson–Thomas type invariants via microlocal geometry*, Ann. of Math. 170 (2009).
