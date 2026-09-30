# Disproof of R0 strict monotonicity for exposed-mobile, infective-immobile SEIR metapopulations

## Context

The admitted target concerns an n-patch SEIR metapopulation with asymmetric dispersal: exposed individuals move with rate matrix M^E(m)=mC where C is irreducible with zero column sums and m>=0 varies, while infective individuals are immobile (M^I=0). Susceptible movement M^S is fixed and total-population conserving. The target conjunction claims: (a) R0(m)=rho(F V(m)^{-1}) is strictly increasing in m whenever isolated patch risks are heterogeneous; (b) R0(m)<=1 implies global asymptotic stability of the disease-free equilibrium (DFE); (c) R0(m)>1 implies uniform persistence of E+I and existence of a positive endemic equilibrium. Either a full proof or a rigorously verified counterexample resolves the TARGET.

## Definitions

Patches i=1..n with standard incidence; infected compartments x=(E,I). At the DFE, S^0 solves (diag(mu)-M^S)S^0=Lambda, independent of m. Define B=diag(beta_i S^0_i/N^0_i), P=diag(sigma_i+mu_i), Sigma=diag(sigma_i), Gamma=diag(gamma_i+mu_i), A(m)=P-mC, D=B Gamma^{-1} Sigma=diag(d_i) with d_i=beta_i(S^0_i/N^0_i)sigma_i/(gamma_i+mu_i). The van den Driessche-Watmough splitting is F=[[0,B],[0,0]], V(m)=[[A(m),0],[-Sigma,Gamma]]. Isolated patch risk r_i=beta_i sigma_i/((sigma_i+mu_i)(gamma_i+mu_i)).

## Result

The target conjunction is FALSE. The explicit 2-patch model with beta=(8,4), sigma=(1,1), gamma=(1,1), mu=(1,1), Lambda=(1,1), M^S=C=[[-1,1],[1,-1]], M^E(m)=mC, M^I=0 satisfies every structural hypothesis with unique DFE S^0=(1,1) and heterogeneous isolated risks r=(2,1), yet R0(0)=2 > (9+sqrt(17))/8=R0(1). Hence R0(m) is not strictly increasing in m.

## Proof / Evidence

Nonzero spectrum reduction: det(lambda I_{2n}-K(m))=lambda^n det(lambda I_n-H(m)) with H(m)=B Gamma^{-1} Sigma A(m)^{-1}=D A(m)^{-1}, so R0(m)=rho(H(m)). A(m) is a nonsingular M-matrix with nonnegative inverse, so NGM hypotheses hold. At m=0: A(0)=2I, H(0)=diag(2,1), hence R0(0)=2 exactly. At m=1: A(1)=[[3,-1],[-1,3]], det=8, inverse=[[3,1],[1,3]]/8, H(1)=[[3/2,1/2],[1/4,3/4]] with trace 9/4, determinant 1, discriminant 17/16, so eigenvalues (9+-sqrt(17))/8 and R0(1)=(9+sqrt(17))/8. Integer certificate sqrt(17)<5 from 17<25 gives R0(1)<(9+5)/8=7/4<2=R0(0). All steps use only rational arithmetic plus integer square comparison; no floating point enters. Falsity of clause (a) falsifies the conjunction; clauses (b)-(c) are not adjudicated.

## Limitations

The disproof refutes only the strict-monotonicity clause and hence the full conjunction. It does not adjudicate the R0<=1 global-stability or R0>1 persistence/endemic-equilibrium clauses, which may hold or fail independently. The witness uses standard incidence with N^0_i=1 and mu_i=1 and says nothing about other incidence forms or global monotonicity over larger m ranges.

## Reproducibility

Run python3 output/artifacts/verify_R0_monotonicity_counterexample.py; it re-derives DFE, risks, H(0), H(1), trace/determinant/discriminant, and the integer certificate using only Fraction arithmetic, printing ALL EXACT CHECKS PASSED.

## References

- O. Diekmann, J. A. P. Heesterbeek, M. G. Roberts, The construction of next-generation matrices for compartmental epidemic models, J. R. Soc. Interface 7:873-885 (2010).
- P. van den Driessche, J. Watmough, Reproduction numbers and sub-threshold endemic equilibria for compartmental models of disease transmission, Math. Biosci. 180:29-48 (2002).
- M. Lu, D. Gao, J. Huang, H. Wang, Relative prevalence-based dispersal in an epidemic patch model, J. Math. Biol. 86:52 (2023).
